# generator.py
import re
import json
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load model
model_name = "meta-llama/Meta-Llama-3-8B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir="./temp_model", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    cache_dir="./temp_model",
    device_map="auto",
    torch_dtype=torch.float16,
    trust_remote_code=True,
    repetition_penalty=1.15
)

# Keyword mapping
KEYWORDS_MAP = {
    "education": ["school", "students", "teaching", "classroom", "curriculum", "exam"],
    "technology": ["ai", "cybersecurity", "artificial intelligence", "machine learning", "software", "hardware", "robotics", "tech"],
    "health": ["medical", "medicine", "health", "wellness", "therapy", "hospital", "disease", "nutrition"],
    "sports": ["football", "soccer", "basketball", "athlete", "olympics", "training", "fitness", "sport"],
    "general": []
}

def infer_topic_category(user_input):
    user_lower = user_input.lower()
    for category, keywords in KEYWORDS_MAP.items():
        if any(kw in user_lower for kw in keywords):
            return category
    return "general"

def generate_presentation_json(user_input, default_slide_count=15):
    user_lower = user_input.lower()
    match = re.search(r'(\d+)\s*slides?', user_lower)
    slide_count = int(match.group(1)) if match else default_slide_count

    # Excluded slides
    excluded_slides = set()
    exclusions = {
        "agenda": ["exclude agenda", "no agenda", "without agenda"],
        "conclusion": ["exclude conclusion", "no conclusion", "without conclusion"],
        "thank you": ["exclude thank you", "no thank you", "without thank you"],
        "any questions": ["exclude any questions", "no any questions", "without any questions"]
    }
    for key, phrases in exclusions.items():
        if any(phrase in user_lower for phrase in phrases):
            excluded_slides.add(key)

    topic_category = infer_topic_category(user_input)

    prompt_template = f"""
You are a professional PowerPoint presentation creator.
Generate exactly {slide_count} slides for the topic: "{user_input.strip()}".
Output ONLY valid JSON.
"""

    messages = [{"role": "user", "content": prompt_template}]
    inputs = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=True,
        return_dict=True,
        return_tensors="pt"
    ).to(model.device)

    outputs = model.generate(
        **inputs, max_new_tokens=10000,
        top_p=0.1, temperature=0.4, do_sample=False
    )

    generated_text = tokenizer.decode(
        outputs[0][inputs["input_ids"].shape[-1]:],
        skip_special_tokens=True
    )

    json_match = re.search(r'\{[\s\S]*\}', generated_text)
    if not json_match:
        print("❌ No valid JSON found")
        return None

    json_str = json_match.group(0)
    json_str = json_str.replace('“', '"').replace('”', '"').replace("’", "'").strip()
    json_str = re.sub(r',\s*([\]}])', r'\1', json_str)

    try:
        data = json.loads(json_str)
    except json.JSONDecodeError:
        print("❌ Failed to parse JSON")
        return None

    # Clean slides
    final_slides = []
    seen_titles = set()
    for slide in data.get("slides", []):
        title = slide.get("title", "").strip()
        lower_title = title.lower()
        if not title or lower_title in seen_titles or lower_title in excluded_slides:
            continue
        seen_titles.add(lower_title)
        final_slides.append({
            "title": title,
            "content": slide.get("content", [])
        })

    data["slides"] = final_slides[:slide_count]
    data["topic_category"] = topic_category
    return data
