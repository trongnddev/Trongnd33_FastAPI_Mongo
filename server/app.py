from fastapi import FastAPI
from server.routes.student import router as router_student


app = FastAPI()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}

for router in (
    {'module': router_student, 'prefix': '/student', },
):
    app.include_router(
        router.get('module'),
        prefix=router.get('prefix'),
        tags=router.get('tags')
    )
