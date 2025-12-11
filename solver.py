from browser import open_page
import requests

async def solve_quiz(url, email, secret):
    html = await open_page(url)

    # Extract the question
    # (for now, we just send a dummy answer so your endpoint works)
    answer = 1  

    payload = {
        "email": email,
        "secret": secret,
        "url": url,
        "answer": answer
    }

    submit_url = url.replace("quiz", "submit")
    resp = requests.post(submit_url, json=payload)

    return {"submitted": True, "status": resp.text}
