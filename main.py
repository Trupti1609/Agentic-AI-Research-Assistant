from agent.ai_agent import AIAgent

def main():
    agent = AIAgent()

    print("🤖 AI Assistant (type 'exit' to quit)\n")

    while True:
        query = input("Ask: ")

        if query.lower() == "exit":
            break

        response = agent.process_query(query)
        print("\n💡", response, "\n")


if __name__ == "__main__":
    main()
