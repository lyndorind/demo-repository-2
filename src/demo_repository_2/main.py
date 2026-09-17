from fastapi import FastAPI


app = FastAPI(title="Demo Repository API")


@app.get("/echo/{message}")
def echo(message: str) -> dict[str, str]:
    """Return the message supplied in the URL."""
    return {"message": message}