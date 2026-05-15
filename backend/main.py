import os
from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from agents.orchestrator import run_orchestrator

# Load keys from the local .env configuration file
load_dotenv()

app = FastAPI(
    title="Lumen AI Multi-Agent Backend",
    description="Event-driven autonomous pipeline code review engine."
)

# Open network lanes for your Next.js dashboard panel to communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {"status": "online", "engine": "Lumen Multi-Agent Core"}

@app.post("/webhook/github")
async def github_webhook(request: Request, background_tasks: BackgroundTasks):
    """
    Receives automated real-time alerts from GitHub whenever a developer 
    interacts with code inside a Pull Request.
    """
    payload = await request.json()
    
    # Filter incoming requests to trace matching Pull Request timelines
    if "pull_request" in payload:
        action = payload.get("action")
        
        # We trigger analyses when a PR is freshly built ('opened') or pushed to ('synchronize')
        if action in ["opened", "synchronize"]:
            repo_name = payload["repository"]["full_name"]
            pr_number = payload["number"]
            diff_url = payload["pull_request"]["diff_url"]
            
            print(f"🚀 [Trigger] Live activity intercepted on {repo_name} (PR #{pr_number})")
            
            # Spin out the processing thread asynchronously so GitHub gets an instant 200 OK receipt
            background_tasks.add_task(run_orchestrator, repo_name, pr_number, diff_url)
            
            return {"status": "Pipeline engaged", "repo": repo_name, "pr": pr_number}
            
    return {"status": "Event recognized but skipped"}

if __name__ == "__main__":
    import uvicorn
    # Boots up the local engine container at http://localhost:8000
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)