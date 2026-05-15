from utils.llm import call_llm

async def analyze_security(code_diff: str) -> str:
    system_prompt = (
        "You are an expert Cybersecurity Engineer. Your sole mission is to analyze the following git diff code changes "
        "for security vulnerabilities. Look out for critical issues such as:\n"
        "- Hardcoded credentials, secrets, passwords, or API keys.\n"
        "- SQL Injection, Cross-Site Scripting (XSS), or Command Injection risks.\n"
        "- Unsafe dependency imports or deprecated cryptography methods.\n"
        "- Broken Access Control or logical security bypasses.\n\n"
        "Provide your analysis using crisp markdown bullet points. Be specific about line numbers if visible. "
        "If absolutely no security vulnerabilities are detected, reply strictly with: '✅ **No security vulnerabilities detected.**'"
    )
    return await call_llm(system_prompt, code_diff)