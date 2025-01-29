import os
import httpx
from fastapi import FastAPI, Depends
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# FatSecret API credentials
CLIENT_ID = os.getenv("FATSECRET_CLIENT_ID")
CLIENT_SECRET = os.getenv("FATSECRET_CLIENT_SECRET")
TOKEN_URL = "https://oauth.fatsecret.com/connect/token"
SEARCH_URL = "https://platform.fatsecret.com/rest/server.api"

# FastAPI app instance
app = FastAPI(title="FatSecret API Integration")

# Cache token to reduce API calls
TOKEN_CACHE = {"access_token": None, "expires_in": None}


async def get_access_token():
    """Fetch OAuth 2.0 access token from FatSecret API"""
    if TOKEN_CACHE["access_token"]:
        return TOKEN_CACHE["access_token"]

    async with httpx.AsyncClient() as client:
        response = await client.post(
            TOKEN_URL,
            data={"grant_type": "client_credentials"},
            auth=(CLIENT_ID, CLIENT_SECRET),
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        if response.status_code == 200:
            token_data = response.json()
            TOKEN_CACHE["access_token"] = token_data["access_token"]
            TOKEN_CACHE["expires_in"] = token_data["expires_in"]
            return token_data["access_token"]
        else:
            return {"error": "Failed to obtain access token", "details": response.text}


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Welcome to FatSecret API Integration with FastAPI"}


@app.get("/token")
async def fetch_token(token: str = Depends(get_access_token)):
    """Fetch OAuth 2.0 Access Token"""
    return {"access_token": token}


@app.get("/search_foods/")
async def search_foods(query: str, token: str = Depends(get_access_token)):
    """Search for foods using FatSecret API"""
    params = {
        "method": "foods.search",
        "search_expression": query,
        "format": "json",
    }

    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient() as client:
        response = await client.get(SEARCH_URL, headers=headers, params=params)
        return response.json()
