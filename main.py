from fastapi import FastAPI, Request
from solver import solve_quiz

EMAIL = "your-email"
SECRET = "TaniSecure543!!"

app = FastAPI()

async def handle_request(request: Request):
    try:
        data = await request.json()
    except:
        return {"error": "Invalid JSON"}, 400

    if data.get("secret") != SECRET:
        return {"error": "Forbidden"}, 403

    quiz_url = data.get("url")
    if not quiz_url:
        return {"error": "URL missing"}, 400

    return await solve_quiz(quiz_url, EMAIL, SECRET)

@app.post("/")
async def root(request: Request):
    return await handle_request(request)

@app.post("/solve")
async def solve(request: Request):
    return await handle_request(request)


