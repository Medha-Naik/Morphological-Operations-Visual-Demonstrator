import streamlit as st
import numpy as np
from operations import get_kernel, apply_operation
from utils import load_image,to_grayscale,generate_test_image


st.title("Morphological Operations Visual Demonstrator")

st.sidebar.header("Controls")
use_sample=st.sidebar.checkbox("Use sample image")

if use_sample:
    image=generate_test_image()
else:
    uploaded=st.sidebar.file_uploader("Upload an image", type=["jpg","png","jpeg"])
    if uploaded:
        image=to_grayscale(load_image(uploaded))
    else:
        st.info("Upload an image or use the sample image.")
        st.stop()

operation = st.sidebar.selectbox("Operation", [
    "Erosion", "Dilation", "Opening", "Closing",
    "Gradient", "Top Hat", "Black Hat"
])

kernel_shape = st.sidebar.selectbox("Kernel Shape", ["Rectangle", "Ellipse", "Cross"])
kernel_size = st.sidebar.slider("Kernel Size", min_value=3, max_value=21, step=2, value=5)

kernel = get_kernel(kernel_shape, kernel_size)
result = apply_operation(image, operation, kernel)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Original")
    st.image(image, clamp=True)
with col2:
    st.subheader("Result")
    st.image(result, clamp=True)