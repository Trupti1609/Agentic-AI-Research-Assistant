def log_query(query, response):
    with open("logs.txt", "a") as f:
        f.write(f"Query: {query}\n")
        f.write(f"Response: {response}\n")
        f.write("="*50 + "\n")
