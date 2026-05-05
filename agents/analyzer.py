import ast
from agents.base_agent import Agent

class AnalyzerAgent(Agent):
    def run(self, context):
        code = context["code"]
        tree = ast.parse(code)

        functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]

        context["analysis"] = {
            "functions": functions,
            "lines": len(code.splitlines())
        }

        print(f"[Analyzer] Functions: {functions}")
        return context
