# from umongo.frameworks import MotorAsyncIOInstance

from  motor.motor_asyncio import AsyncIOMotorClient
import asyncio

MONGO_DETAILS = "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGO_DETAILS).demodb
client.get_io_loop = asyncio.get_running_loop
database = client
# database = client.demodb
# database = MotorAsyncIOInstance(client)







