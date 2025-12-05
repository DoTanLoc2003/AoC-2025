import sys
import os
import importlib.util

def run_day(day_str, mode):
    # Code file
    code_path = os.path.join("code", f"{day_str}.py")
    if not os.path.isfile(code_path):
        print(f"❌ Code not found: {code_path}")
        return

    if mode == "test":
        input_path = os.path.join("inputs/tests", f"{day_str}.txt")
    else:
        input_path = os.path.join("inputs", f"{day_str}.txt")

    if not os.path.isfile(input_path):
        print(f"❌ Input file not found: {input_path}")
        return

    with open(input_path, "r") as f:
        input_data = f.read()

    spec = importlib.util.spec_from_file_location(day_str, code_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if not hasattr(module, "solve"):
        print(f"❌ Missing solve(input_data) in {code_path}")
        return

    print(f"▶ Running {day_str} with: {input_path}")
    print("---- Output ----")
    print(module.solve(input_data))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 main.py day01")
        print("  python3 main.py day01 input")
        print("  python3 main.py day01 test")
        sys.exit(1)

    day_str = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) >= 3 else "input"

    run_day(day_str, mode)
