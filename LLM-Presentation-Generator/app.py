# app.py
from flask import Flask
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, State
import re
import time
from generator import generate_presentation_json
from ppt_builder import create_ppt_from_json_safe
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.wsgi import WSGIMiddleware
from pyngrok import ngrok

#  Flask + Dash App 
flask_app = Flask(__name__)

dash_app = dash.Dash(
    __name__,
    server=flask_app,
    url_base_pathname="/",
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

dash_app.layout = html.Div([
    html.H1("📃 LLM Presentation Generator"),
    html.Div([
        html.Div("Enter your topic below:"),
        dcc.Textarea(id="user_input", style={"width":"100%","height":"150px"}),
        html.Button("✨ Generate Presentation", id="generate_btn", n_clicks=0),
        html.Div(id="download_section")
    ])
])

@dash_app.callback(
    Output("download_section","children"),
    Input("generate_btn","n_clicks"),
    State("user_input","value"),
    prevent_initial_call=True
)
def generate_presentation(n_clicks, user_message):
    if not user_message:
        return html.Div("❌ Please enter a topic.", style={"color":"red"})

    presentation_json = generate_presentation_json(user_message)
    if presentation_json is None:
        return html.Div("❌ Failed to generate presentation.", style={"color":"red"})

    topic = presentation_json.get("topic_category","General")
    first_title = presentation_json["slides"][0]["title"]
    topic_name = re.sub(r'[^A-Za-z0-9_]+','_',first_title.strip())
    file_name = f"{topic_name}_{topic}.pptx"
    output_path = f"./{file_name}"

    create_ppt_from_json_safe(presentation_json, output_path)

    download_btn = html.A(html.Button(f"⬇️ Download {file_name}"),
                          href=f"/download_pptx?file={file_name}",
                          download=file_name)
    return download_btn

#  FastAPI App 
fastapi_app = FastAPI()
fastapi_app.mount("/", WSGIMiddleware(flask_app))

@fastapi_app.get("/download_pptx")
def download_pptx(file: str):
    import os
    if os.path.exists(file):
        return FileResponse(file, media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation")
    return {"error":"File not found"}

#  Ngrok 
public_url = ngrok.connect(8000)
print("Public URL:", public_url)
