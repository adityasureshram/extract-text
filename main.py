import os
import streamlit as st
import torch
import easyocr
import numpy as np
from io import BytesIO,StringIO

def extractTextFromImg(img):
    reader = easyocr.Reader(['en', 'en'])
    #img needs to be file path, url, or bytes
    img_text = reader.readtext(img)
    text = ' '.join([x[1] for x in img_text])
    return text