import os
import sys

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if project_root not in sys.path:
    sys.path.append(project_root)

from router import route_request
from executor import execute_tool
from state import AgentState

from rag.rag_tool import search_knowledge
from system_search.system_search import search_system


def run_agent(user_request):

    state = AgentState()

    # Store the user's request
    state.user_request = user_request

    # Step 1: Search the knowledge base using RAG
    rag_results = search_knowledge(user_request)

    # Step 2: Search the tool registry
    system_results = search_system(user_request)

    # Step 3: Route the request to the correct tool
    tools = route_request(user_request)

    if not tools:
        return {
            "success": False,
            "message": "No suitable tool found",
            "rag_results": rag_results,
            "system_results": system_results
        }

    # Step 4: Select the first matching tool
    selected_tool = tools[0]

    state.selected_tool = selected_tool["name"]

    # Demo parameters
    if selected_tool["name"] == "create_invoice":
        state.parameters = {
            "amount": 50
        }

    elif selected_tool["name"] == "send_invoice":

        amount = 50

        if "$" in user_request:

            amount_text = user_request.split("$")[1].split()[0]

            try:
                amount = float(amount_text)

            except ValueError:
                amount = 50

        state.parameters = {
            "invoice_id": "INV001",
            "amount": amount
        }

    elif selected_tool["name"] == "get_invoice":

        state.parameters = {
            "invoice_id": "INV001"
        }

    elif selected_tool["name"] == "process_payment":

        state.parameters = {
            "amount": 100
        }

    elif selected_tool["name"] == "refund_payment":

        state.parameters = {
            "payment_id": "PAY001"
        }

    elif selected_tool["name"] == "create_dispute":

        state.parameters = {
            "payment_id": "PAY001"
        }

    elif selected_tool["name"] == "get_dispute":

        user_id = "USER001"

        # Extract a user ID such as user_123
        words = user_request.replace("?", "").split()

        for word in words:

            if word.lower().startswith("user_"):

                user_id = word

                break

        state.parameters = {
            "user_id": user_id
        }

    elif selected_tool["name"] == "create_customer":

        state.parameters = {
            "name": "Demo Customer"
        }

    elif selected_tool["name"] == "get_customer":

        state.parameters = {
            "customer_id": "CUS001"
        }

    else:

        state.parameters = {}

    # Step 5: Execute the selected tool
    state.result = execute_tool(
        state.selected_tool,
        state.parameters
    )

    # Return complete agent information
    return {
        "success": True,
        "tool": state.selected_tool,
        "parameters": state.parameters,
        "rag_results": rag_results,
        "system_results": system_results,
        "result": state.result
    }