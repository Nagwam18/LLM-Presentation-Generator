📊 LLM Presentation Generator
Auto-Generate Professional PowerPoint Presentations Using LLaMA 3 + FastAPI + Dash + Ngrok

This project is an end-to-end AI system that creates full PowerPoint presentations automatically from a single user prompt.

It integrates:

✅ HuggingFace LLaMA 3–8B Instruct
✅ FastAPI backend
✅ Dash UI with animated front-end
✅ Ngrok for public access
✅ Dynamic JSON generation + PPTX slide builder
✅ Smart topic classification (tech, education, sports, health, general)
✅ Automatic PowerPoint export (.pptx)

🚀 Features
🔥 1. AI-Generated Presentations

You enter any topic (e.g., “AI Ethics 12 slides without agenda”) →
the model produces full structured slides, with:

Title slide

Optional agenda

Detailed content slides

Conclusion

Any Questions

Thank You

All output is clean JSON.

📦 2. Template-Based PPTX Builder

Slides are built using category-specific PowerPoint templates:

🎓 Education

💻 Technology

🏥 Health

⚽ Sports

🌐 General

🎨 3. Modern Web UI (Dash + Bootstrap)

Users get a clean interface:

Text input box

Animated question prompt

“✨ Generate Presentation” button

Loading spinner

Download button once PPTX is ready

🌍 4. Accessible Anywhere with Ngrok

The app exposes a public URL automatically:

Public URL: https://xxxx.ngrok-free.app

⚙️ 5. Complete Backend Integration

Mixing:

FastAPI download endpoint

Flask + Dash mounted using WSGI

Full async support (nest_asyncio)

HuggingFace Hub login

JSON cleaning + repairing

PPTX generation safety

🛠️ Installation

Install required packages:

pip install -U transformers
pip install fastapi json-repair uvicorn pyngrok dash dash-bootstrap-components python-pptx nest-asyncio torch mangum


Log into HuggingFace:

from huggingface_hub import login
login(token="YOUR_HF_TOKEN")

📁 Project Structure
📦 LLM-Presentation-Generator
 ┣ 📁 templates/              # PowerPoint templates
 ┣ 📄 app.py                  # Main FastAPI + Dash app
 ┣ 📄 generator.py            # JSON generation logic
 ┣ 📄 ppt_builder.py          # PPTX builder
 ┣ 📄 README.md
 ┗ requirements.txt

✨ How It Works
⭐ 1. User enters topic

Example:

"Explain cyber security for beginners in 10 slides without agenda."

⭐ 2. System detects topic category

(Tech, Health, Sports, Education, General)

⭐ 3. LLaMA model generates JSON

Slide titles

3–4 detailed bullet points per slide

Respecting exclusions

⭐ 4. JSON → PPTX converter

Slides inserted into a template with:

Titles

Bullets

RTL support

Clean formatting

⭐ 5. User downloads .pptx file

Through the FastAPI /download_pptx endpoint.

▶️ Running the App

Start the public server:

uvicorn app:app --host 0.0.0.0 --port 8000


Ngrok generates the URL automatically:

Public URL: https://your-ngrok-url.ngrok-free.app


Open it → use the UI → generate your file.

🧠 Model Used

Meta-LLaMA-3-8B-Instruct

Loaded with:

torch.float16

device_map="auto"

repetition_penalty=1.15

Up to 10,000 tokens for full slide generation

🔒 JSON Cleaning & Repairing

The system includes:

Unicode cleanup

Trailing comma removal

Control character removal

Automatic JSON repairing

Duplicate slide filtering

Enforcing slide count

🎯 Use Cases

✔ Teachers creating lessons
✔ HR teams making training slides
✔ Students preparing assignments
✔ Businesses producing reports
✔ Startup founders pitching ideas

📥 Example Output

User prompt:

“Create 12 slides on Digital Marketing. Exclude Thank You slide.”

System returns:

JSON with exactly 12 slides

Tailored content

No Thank You slide

PPT ready for download

🤝 Contributions

PRs, issues, and suggestions are welcome!
This tool is perfect for LLM, FastAPI, and automation enthusiasts.

📜 License

MIT License — free for personal & commercial use.
