# Oxford102_CaffeModel_CoreMLGenerator
This repository creates CoreML model form the Oxford 102 Caffe Model. Import this model into the FlowerID project

Installation Instructions:

1. Install CoreML Tools:

$ python -m pip install --user --upgrade pip

$ python -m venv coremltools-venv

$ source coremltools-venv/bin/activate

$ pip install coremltools==5.0b2


2. Download the Caffe Model into this repository (It must be in the same folder as the convert.py file):

https://nam12.safelinks.protection.outlook.com/?url=https%3A%2F%2Fs3.amazonaws.com%2Fjgoode%2Foxford102.caffemodel&data=02%7C01%7CCC.Cooper%40wwt.com%7C66c905c8b324449d263908d869277dcb%7Ca2d8e6b4e26e44218f3dec288c827c7d%7C1%7C1%7C637374965621890457&sdata=mtmc0jMjAYateh8G5NrB4Rsv4dmthYasDZYAfxQ9Q1E%3D&reserved=0

3. Convert the model to CoreML:

$ python convert.py

4. Grab yourself a cup of coffee (or caffe) while the model is converted :)
