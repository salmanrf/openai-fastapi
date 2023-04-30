from motor.motor_asyncio import AsyncIOMotorClient
from config import config

client = AsyncIOMotorClient(config.DATABASE_URL)
db = client["mochat"]
