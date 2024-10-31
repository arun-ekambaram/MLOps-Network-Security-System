import sys
import os
import certifi
ca = certifi.where()
from dotenv import load_dotenv
load_dotenv
mongo_db_url = os.getenv("MONGODB_URL_KEY")
print(mongo_db_url)
import pymongo
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
from network_security.pipeline.training_pipeline import TrainingPipeline
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Request
from uvicorn import run as app_run
from fastapi.responses import Response
from starlette.responses import RedirectResponse
import pandas as pd
