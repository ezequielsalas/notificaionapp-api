from fastapi import FastAPI
# from app.controllers import messages, notifications
from app.database import engine
from app.controllers import user_controller, message_controller, log_controller
from app.config import API_HOST, API_PORT
from app.database import engine
from app.database import Base
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Configure CORS
origins = [
    "http://notificationappui-lb-687586515.us-east-1.elb.amazonaws.com",
    "http://localhost",
    "http://localhost:3000",
    "http://example.com",  # Add your frontend URL here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

Base.metadata.create_all(bind=engine)

app.include_router(user_controller.router, prefix="/api", tags=["users"])
app.include_router(message_controller.router, prefix="/api", tags=["messages"])
app.include_router(log_controller.router, prefix="/api", tags=["logs"])

@app.get("/")
def root():
    return {"message": "Notification app API"}
    
if __name__ == "__main__":
    uvicorn.run(app, host=API_HOST, port=API_PORT)