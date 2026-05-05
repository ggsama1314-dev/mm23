import textwrap
from core.orchestrator import Orchestrator
from examples.demo_code import bad_code
import inspect

if __name__ == "__main__":
    code = inspect.getsource(bad_code)
    code = textwrap.dedent(code)

    orchestrator = Orchestrator()
    result = orchestrator.run(code)

    print("\n=== Final Report ===")
    for k, v in result.items():
        print(f"{k}: {v}")
