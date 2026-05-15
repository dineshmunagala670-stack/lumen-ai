import os
import httpx

async def post_github_comment(repo_name: str, pr_number: int, markdown_body: str):
    """
    The action execution layer. It turns code thinking into actual physical 
    side effects by writing the review back onto the GitHub pull request thread.
    """
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("❌ Action aborted: GITHUB_TOKEN variable was missing from internal system scope.")
        return
        
    url = f"https://api.github.com/repos/{repo_name}/issues/{pr_number}/comments"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "Lumen-AI-Orchestration-Engine"
    }
    
    payload = {"body": markdown_body}
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, json=payload, headers=headers)
            if response.status_code == 201:
                print(f"🎉 Success! Code review evaluation feedback successfully written on PR #{pr_number}.")
            else:
                print(f"❌ Integration Error: Repository rejected submission package ({response.status_code}): {response.text}")
        except Exception as e:
            print(f"❌ Connection error while pushing updates to GitHub network lanes: {str(e)}")