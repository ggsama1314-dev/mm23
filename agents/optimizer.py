from agents.base_agent import Agent

class OptimizerAgent(Agent):
    def run(self, context):
        issues = context["issues"]

        suggestions = []

        for issue in issues:
            if "过长" in issue:
                suggestions.append("拆分函数（单一职责）")
            if "缺少函数" in issue:
                suggestions.append("封装函数提高复用性")

        context["suggestions"] = suggestions

        print(f"[Optimizer] Suggestions: {suggestions}")
        return context
