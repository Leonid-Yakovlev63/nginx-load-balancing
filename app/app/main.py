from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class HealthCheck(BaseModel):
    status: str = "OK"

@app.get(
    "/health",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
async def get_health() -> HealthCheck:
    return HealthCheck(status="OK")

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}
