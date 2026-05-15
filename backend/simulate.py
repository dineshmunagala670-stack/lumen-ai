# backend/simulate.py
import json
import httpx
import asyncio

async def trigger_mock_webhook():
    url = "http://localhost:8000/webhook/github"
    
    # This mock payload tells your backend that someone just opened a Pull Request
    mock_payload = {
        "action": "opened",
        "number": 12,
        "repository": {
            "full_name": "Arpithajain26/lumen_ai"
        },
        "pull_request": {
            "diff_url": "https://patch-diff.githubusercontent.com/raw/Arpithajain26/lumen_ai/pull/1.diff"
        }
    }
    
    headers = {"Content-Type": "application/json"}
    
    print("🚀 Sending simulated Pull Request event to your FastAPI backend...")
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, json=mock_payload, headers=headers)
            print(f"📥 Server Response Status: {response.status_code}")
            print(f"📄 Server Body: {response.json()}")
            print("\n🎉 Check your browser window now! The agents should be moving!")
        except Exception as e:
            print(f"❌ Failed to reach backend. Ensure main.py is running. Error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(trigger_mock_webhook())