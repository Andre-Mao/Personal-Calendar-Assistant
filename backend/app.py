from fastapi import fastapi, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel 
from datetime import datetime, timedelta
from typing import Optional, List
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title = "Calendar Assistant API", version = "1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"],
    allow_credentials = True,
    allow_methods= ["*"],
    allow_headers= ["*"],
)

DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_NAME', 'calendar-assistant')
}

