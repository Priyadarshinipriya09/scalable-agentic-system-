class AgentState:
    def __init__(self):
        self.user_request = None
        self.selected_tool = None
        self.parameters = {}
        self.result = None

    def show_state(self):
        print("\n--- Agent State ---")
        print("User Request:", self.user_request)
        print("Selected Tool:", self.selected_tool)
        print("Parameters:", self.parameters)
        print("Result:", self.result)