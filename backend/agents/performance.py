from utils.llm import call_llm

async def analyze_performance(code_diff: str) -> str:
    system_prompt = (
        "You are an expert Performance and Database Reliability Engineer. Your sole mission is to analyze the following git diff code changes "
        "for performance bottlenecks and efficiency issues. Look out for critical bugs such as:\n"
        "- High algorithmic complexity issues (e.g., unnecessary nested loops, O(N^2) operations on big data).\n"
        "- Database N+1 query problems, missing indexes, or unoptimized network fetches.\n"
        "- Memory leaks, unclosed file descriptors, or missing stream cleanups.\n"
        "- Redundant calculations or missing caching mechanisms.\n\n"
        "Provide your analysis using crisp markdown bullet points. "
        "If absolutely no performance bottlenecks are found, reply strictly with: '✅ **No performance bottlenecks detected.**'"
    )
    return await call_llm(system_prompt, code_diff)
