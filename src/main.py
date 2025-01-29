from fastapi import FastAPI
from router.chat_router import chat_routers 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],   
)

app.include_router(chat_routers)  
