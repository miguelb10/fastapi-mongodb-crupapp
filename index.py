#Import statements
from fastapi import FastAPI
from routes.student import student_router
from fastapi.middleware.cors import CORSMiddleware

#Our React app url
client_apps = ['http://localhost:3000']

#Create app
app = FastAPI()

#Register your router
app.include_router(student_router)

#Register App with CORS middleware to allow resources sharing between differents domains/origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=client_apps,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)