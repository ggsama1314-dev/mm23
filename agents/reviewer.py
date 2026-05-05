from agents.base_agent import Agent

class ReviewerAgent(Agent):
    def run(self, context):
        analysis = context["analysis"]

        issues = []

        if analysis["lines"] > 15:
            issues.append("函数过长，建议拆分")

        if len(analysis["functions"]) == 0:
            issues.append("缺少函数封装")

        context["issues"] = issues

        print(f"[Reviewer] Issues: {issues}")
        return context
