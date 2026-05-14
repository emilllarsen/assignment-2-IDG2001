"""Token Shop - Handles token purchases with secret codes."""
import hashlib
import random
import string
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory storage for purchases
purchases = {}

# Price: how much money per token
token_price = 2


class BuyRequest(BaseModel):
    """Schema for buying tokens."""
    username: str
    password: str
    money: int


class CodeRequest(BaseModel):
    """Schema for verifying a code."""
    code: str


class PriceUpdate(BaseModel):
    """Schema for updating token price."""
    price: int


@app.post("/buy")
def buy_tokens(payload: BuyRequest):
    """Buy tokens with money. Returns a secret code."""
    tokens = payload.money // token_price

    random_str = ''.join(
        random.choices(string.ascii_letters + string.digits, k=32)
    )
    secret = hashlib.sha256(random_str.encode()).hexdigest()

    purchases[secret] = {
        "username": payload.username,
        "tokens": tokens,
        "used": False,
    }

    return {"secret": secret}


@app.post("/verify")
def verify_code(payload: CodeRequest):
    """Verify a secret code. Returns tokens. One-time use."""
    purchase = purchases.get(payload.code)

    if not purchase:
        raise HTTPException(status_code=404, detail="Invalid code")

    if purchase["used"]:
        raise HTTPException(
            status_code=400, detail="Code already used"
        )

    purchase["used"] = True

    return {"tokens": purchase["tokens"]}


@app.get("/price")
def get_price():
    """Return the current token price."""
    return {"price": token_price}


@app.post("/price")
def set_price(payload: PriceUpdate):
    """Admin endpoint to update the token price."""
    global token_price
    token_price = payload.price
    return {"price": token_price}