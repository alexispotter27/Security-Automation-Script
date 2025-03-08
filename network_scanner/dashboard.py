from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

# Dummy data for now (to be replaced with real scan results)
scan_results = []


@app.get("/")
def home():
    return {"message": "Cybersecurity Automation Dashboard"}


@app.get("/scan-results", response_model=List[Dict])
def get_scan_results():
    return scan_results


@app.post("/add-scan-result/")
def add_scan_result(ip: str, status: str):
    scan_results.append({"ip": ip, "status": status})
    return {"message": "Scan result added", "data": scan_results}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
