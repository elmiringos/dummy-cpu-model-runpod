import runpod

def handler(job):
    print("Handling job:", job)
    input_data = job.get("input", {}).get("data", "")
    return {"result": f"Processed: {input_data} — Dummy response."}

if __name__ == "__main__":
    runpod.serverless.start({"handler": handler})