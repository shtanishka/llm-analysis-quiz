from fastapi import FastAPI, Request
from solver import solve_quiz
import uvicorn

EMAIL = "your-email"
SECRET = "TaniSecure543!!"

app = FastAPI()

@app.post("/")
async def root(request: Request):
    try:
        data = await request.json()
    except:
        return {"error": "Invalid JSON"}, 400

    if "secret" not in data or data["secret"] != SECRET:
        return {"error": "Forbidden"}, 403

    quiz_url = data.get("url")
    if not quiz_url:
        return {"error": "URL missing"}, 400

    result = await solve_quiz(quiz_url, EMAIL, SECRET)
    return result

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=10000)
