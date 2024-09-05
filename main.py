from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.filter import router as filter_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to match your frontend's origin
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)
app.include_router(filter_router,prefix='/api/v1/filters')
