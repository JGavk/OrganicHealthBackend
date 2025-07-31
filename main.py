from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pathc.link import router as answers_router
from pathc.link import router as link

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://3-d-organic-health.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(answers_router)
app.include_router(link)


@app.get("/")
async def root():
    return {"message": "Hello World"}
