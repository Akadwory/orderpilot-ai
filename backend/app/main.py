from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import routes


app = FastAPI()

#Middleware to allow fronted calls 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Mount the route module 
app.include_router(routes.router)

@app.get("/")
def root():
    return {"message": "OrderPilot AI Backend is Live"}