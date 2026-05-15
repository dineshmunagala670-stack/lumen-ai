import os
import httpx

async def call_llm(system_prompt: str, user_content: str) -> str:
    """
    Executes a high-performance raw async transaction against the LLM gateway.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "⚠️ Error: The engine's configuration parameter [OPENAI_API_KEY] is unassigned."
        
    url = "https://api.openai.com/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "gpt-4o-mini",  # Highly scalable, low latency, exceptional reasoning
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content}
        ],
        "temperature": 0.2  # Keeps agent reasoning highly deterministic and objective
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, json=data, headers=headers, timeout=30.0)
            if response.status_code != 200:
                return f"❌ AI Connection Fault ({response.status_code}): {response.text}"
            
            result = response.json()
            return result["choices"][0]["message"]["content"]
        except Exception as e:
            return f"❌ Agent engine timed out or experienced a networking anomaly: {str(e)}"