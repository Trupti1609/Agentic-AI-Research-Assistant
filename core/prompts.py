def build_prompt(query, context=""):
    return f"""
You are an AI Research Assistant.

Instructions:
- Understand the query carefully
- Use provided context if available
- Give clear, structured answer

Context:
{context}

Question:
{query}

Answer:
"""
