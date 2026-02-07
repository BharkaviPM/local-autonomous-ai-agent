import ollama

MODEL = "llama3"   # change if using mistral etc.

def create_plan(topic):
    prompt = f"""
You are an expert research planner.

Break this research topic into clear actionable steps.

Topic: {topic}

Return ONLY a numbered plan.
"""

    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content']
