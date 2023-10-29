import os
from dotenv import load_dotenv
import pymongo
import streamlit as st
import torch
import easyocr
from PIL import Image
import numpy as np
import cv2
from io import BytesIO,StringIO

load_dotenv()

def initConn():
    #helper function to connect to mongodb
    murl = os.getenv('MURL')
    mclient = pymongo.MongoClient(murl)
    mdb = 'sample_analytics'
    conn = mclient[mdb]
    return conn


def extractTextFromImg(img):
    reader = easyocr.Reader(['en', 'en'])
    #img needs to be file path, url, or bytes
    img_text = reader.readtext(img)
    text = ' '.join([x[1] for x in img_text])
    return text


def load_image(img):
    im = Image.open(img)
    image = np.array(im)
    return image