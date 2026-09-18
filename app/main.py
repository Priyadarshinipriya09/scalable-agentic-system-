from agent import run_agent


print("=== Scalable Agentic System ===")

request = input("\nEnter your request: ")

result = run_agent(request)

print("\n=== Agent Response ===")

if result["success"]:

    print("\nRAG Information:")

    if result["rag_results"]:
        for information in result["rag_results"]:
            print("-", information)
    else:
        print("No relevant information found")

    print("\nSystem Search:")

    if result["system_results"]:
        print("Matching tools found:", len(result["system_results"]))

        for tool in result["system_results"]:
            print("-", tool["name"])
    else:
        print("No matching tools found")

    print("\nSelected Tool:", result["tool"])

    print("Parameters:", result["parameters"])

    print("\nResult:")
    print(result["result"])

else:

    print(result["message"])

    if "rag_results" in result:
        print("\nRAG Information:")

        for information in result["rag_results"]:
            print("-", information)

    if "system_results" in result:
        print("\nSystem Search:")

        print(
            "Matching tools found:",
            len(result["system_results"])
        )