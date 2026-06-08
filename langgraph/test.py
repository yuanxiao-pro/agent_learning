from tavily import TavilyClient
client = TavilyClient(api_key="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")
print(client.search(query="北京明天天气", max_results=2))