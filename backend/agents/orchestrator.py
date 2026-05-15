import asyncio
import httpx
from agents.security import analyze_security
from agents.performance import analyze_performance
from agents.quality import analyze_quality
from agents.publisher import post_github_comment

async def fetch_code_diff(diff_url: str) -> str:
    """Gets the raw patch file data directly from the GitHub server repository."""
    headers = {"User-Agent": "Lumen-AI-Orchestration-Engine"}
    async with httpx.AsyncClient() as client:
        response = await client.get(diff_url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Failed to extract text data payload. HTTP Status: {response.status_code}")
        return response.text

async def run_orchestrator(repo_name: str, pr_number: int, diff_url: str):
    print(f"📥 Pulling structural code modifications from GitHub for PR #{pr_number}...")
    try:
        code_diff = await fetch_code_diff(diff_url)
    except Exception as e:
        print(f"❌ Failed to extract target diff data stream: {str(e)}")
        return

    # Keep payloads safe within default context window maximum limits
    if len(code_diff) > 25000:
        code_diff = code_diff[:25000] + "\n\n... [Truncated by Lumen AI to preserve processing context limits] ..."

    print("🧠 Dispatching worker agents concurrently across async process links...")
    
    # Fire all three workers simultaneously into background processes
    security_task = asyncio.create_task(analyze_security(code_diff))
    performance_task = asyncio.create_task(analyze_performance(code_diff))
    quality_task = asyncio.create_task(analyze_quality(code_diff))
    
    # Wait for all running worker processes to sync back up together
    security_res, performance_res, quality_res = await asyncio.gather(
        security_task, performance_task, quality_task
    )
    
    print("✍️ Assembling feedback summaries into technical markdown structure...")
    final_report = (
        f"## 🤖 Lumen AI Automated Pull Request Review\n\n"
        f"### 🔒 Security Analysis\n{security_res}\n\n"
        f"### ⚡ Performance Review\n{performance_res}\n\n"
        f"### 🛠️ Code Quality & Style\n{quality_res}\n\n"
        f"--- \n*Review completed autonomously by your Lumen Multi-Agent Engine. 🚀*"
    )
    
    print("📤 Dispatching publisher transaction action link back to GitHub UI platform...")
    await post_github_comment(repo_name, pr_number, final_report)