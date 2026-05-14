"""Token Shop - Handles token purchases with secret codes."""
import hashlib
import random
import string
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator

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

    @field_validator("price")
    @classmethod
    def price_must_be_positive(cls, v):
        """Ensure price is at least 1 to prevent division by zero."""
        if v < 1:
            raise ValueError("price must be at least 1")
        return v


@app.post("/buy")
def buy_tokens(payload: BuyRequest):
    """Buy tokens with money. Returns a secret code."""
    tokens_to_give = payload.money // token_price

    random_characters = ''.join(
        random.choices(string.ascii_letters + string.digits, k=32)
    )
    secret_code = hashlib.sha256(random_characters.encode()).hexdigest()

    purchases[secret_code] = {
        "username": payload.username,
        "tokens": tokens_to_give,
        "used": False,
    }

    return {"secret": secret_code}


@app.post("/verify")
def verify_code(payload: CodeRequest):
    """Verify a secret code. Returns tokens. One-time use."""
    existing_purchase = purchases.get(payload.code)

    if not existing_purchase:
        raise HTTPException(status_code=404, detail="Invalid code")

    if existing_purchase["used"]:
        raise HTTPException(
            status_code=400, detail="Code already used"
        )

    existing_purchase["used"] = True

    return {"tokens": existing_purchase["tokens"]}


@app.get("/price")
def get_price():
    """Return the current token price."""
    return {"price": token_price}


@app.post("/price")
def set_price(payload: PriceUpdate):
    """Admin endpoint to update the token price."""
    if payload.price < 1:
        raise HTTPException(status_code=422, detail="price must be at least 1")
    global token_price
    token_price = payload.price
    return {"price": token_price}