import requests
import streamlit as st
from PIL import Image


STYLES = {
    "candy": "candy",
    "composition 6": "composition_vii",
    "feathers": "feathers",
    "la_muse": "la_muse",
    "mosaic": "mosaic",
    "starry night": "starry_night",
    "the scream": "the_scream",
    "the wave": "the_wave",
    "udnie": "udnie",
}


st.set_option("deprecation.showfileUploaderEncoding", False)
st.title("Style transfer web app")
# 파일 업로더
image = st.file_uploader("Choose an image")
# selectbox
style = st.selectbox("Choose the style", [STYLE for STYLE in STYLES.keys()])
# 버튼 표시
if st.button("Style Transfer"):
    if image is not None and style is not None:
        files = {"file": image.getvalue()}
        result = requests.post(f"http://backend:8080/{style}", files=files)

        image_path = result.json()
        image = Image.open(image_path.get("name"))
        st.image(image, width=500)
