# **📊 LLM Presentation Generator**
### **Auto-Generate Professional PowerPoint Presentations Using LLaMA 3 + FastAPI + Dash + Ngrok**

This project is a complete end-to-end AI system that **automatically creates full PowerPoint presentations** from a single user prompt.

It integrates:

- ✅ **HuggingFace LLaMA 3–8B Instruct**  
- ✅ **FastAPI backend**  
- ✅ **Dash UI with animated front-end**  
- ✅ **Ngrok for public access**  
- ✅ **Dynamic JSON generation + PPTX slide builder**  
- ✅ **Smart topic classification** (**tech**, **education**, **sports**, **health**, **general**)  
- ✅ **Automatic PowerPoint export (.pptx)**  

---

## **🚀 Features**

### **🔥 1. AI-Generated Presentations**
You enter any topic (e.g., **“AI Ethics 12 slides without agenda”**) and the model produces:

- **Title slide**  
- **Optional agenda**  
- **Structured content slides**  
- **Conclusion**  
- **Any Questions**  
- **Thank You**  

All output is clean, structured **JSON**.

---

### **🎨 2. Template-Based PPTX Builder**
Slides are created using category-specific PowerPoint templates:

- 🎓 **Education**  
- 💻 **Technology**  
- 🏥 **Health**  
- ⚽ **Sports**  
- 🌐 **General**  

---

### **💻 3. Modern Web UI (Dash + Bootstrap)**
UI includes:

- **Input text box**  
- **Animated question prompt**  
- **✨ Generate Presentation button**  
- **Loading spinner**  
- **File download button** once PPTX is generated  

---

---

### **⚙️ 4. Full Backend Integration**
Combines:

- **FastAPI (download endpoint)**  
- **Dash mounted inside FastAPI**  
- **Ngrok automatic tunneling**  
- **JSON validation + repairing**  
- **PPTX generation with python-pptx**  
- **HuggingFace Hub login**  

---

## **🛠️ Installation**

###   Install dependencies 

```bash
pip install -U transformers
pip install fastapi json-repair uvicorn pyngrok dash dash-bootstrap-components python-pptx nest-asyncio torch mangum
```
---
###  Login to HuggingFace 
```bash
from huggingface_hub import login
login(token="YOUR_HF_TOKEN")
```
---
### 📁 Project Structure

📦 LLM-Presentation-Generator
├─ 📁 templates/              # PowerPoint templates
├─ 📄 app.py                  # Main FastAPI + Dash app
├─ 📄 generator.py            # JSON generation logic
├─ 📄 ppt_builder.py          # PPTX builder
├─ 📄 README.md               # This README file
└─ 📄 requirements.txt        # Project dependencies

---
