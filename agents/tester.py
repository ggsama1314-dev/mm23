from agents.base_agent import Agent

class TesterAgent(Agent):
    def run(self, context):
        issues = context["issues"]

        if len(issues) == 0:
            result = "PASS"
        elif len(issues) == 1:
            result = "WARNING"
        else:
            result = "FAIL"

        context["test_result"] = result

        print(f"[Tester] Result: {result}")
        return context
