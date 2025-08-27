import runpod

def handler(job):
    input_data = job.get("input", {})
    a = input_data.get("a")
    b = input_data.get("b")
    operation = input_data.get("op")

    if a is None or b is None or operation not in {"add", "sub", "mul", "div"}:
        return {"error": "Missing or invalid input"}

    try:
        result = {
            "add": a + b,
            "sub": a - b,
            "mul": a * b,
            "div": a / b if b != 0 else "inf"
        }[operation]
    except Exception as e:
        return {"error": str(e)}

    return {"result": result}

if __name__ == "__main__":
    runpod.serverless.start({"handler": handler})
