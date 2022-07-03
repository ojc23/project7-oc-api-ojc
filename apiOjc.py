
from fastapi import FastAPI


app = FastAPI(
    title="DeepLabV3 image segmentation",
    description="""Obtain semantic segmentation maps of the image in input via DeepLabV3 implemented in PyTorch.
                           Visit this URL at port 8501 for the streamlit interface.""",
    version="0.1.0",
)

@app.get('/')
def index():
    return {'message': 'Hello, API for Credit scoring'}

@app.post("/segmentation")
def get_segmentation_map(file: bytes = File(...)):
    return {'message': 'Hello, API for Credit scoring'}