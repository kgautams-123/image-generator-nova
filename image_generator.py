import streamlit as st
import boto3
import json
import base64
from PIL import Image
import io

# Page configuration
st.set_page_config(
    page_title="AI Image Generator",
    page_icon="🎨",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
    }
    .stTitle {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

class ImageGenerator:
    def __init__(self):
        self.bedrock = boto3.client(
            service_name='bedrock-runtime',
            region_name='us-east-1'
        )

    def generate_image(self, prompt, negative_prompt="none", width=1024, height=1024, quality="standard", num_images=1):
        try:
            body = {
                "textToImageParams": {
                    "text": prompt,
                    "negativeText": negative_prompt if negative_prompt else "none"
                },
                "taskType": "TEXT_IMAGE",
                "imageGenerationConfig": {
                    "numberOfImages": num_images,
                    "quality": quality,
                    "cfgScale": 7.5,
                    "height": height,
                    "width": width
                }
            }

            response = self.bedrock.invoke_model(
                modelId="amazon.nova-canvas-v1:0",
                body=json.dumps(body)
            )

            response_body = json.loads(response.get('body').read())
            images = []
            
            if 'images' in response_body:
                for img_data in response_body['images']:
                    image_bytes = base64.b64decode(img_data)
                    image = Image.open(io.BytesIO(image_bytes))
                    images.append(image)

            return images

        except Exception as e:
            st.error(f"Error generating image: {str(e)}")
            return None

def main():
    st.title("🎨 AI Image Generator")
    st.subheader("Powered by Amazon Nova Canvas")

    generator = ImageGenerator()

    with st.sidebar:
        st.header("Settings")
        quality = st.select_slider(
            "Image Quality",
            options=["draft", "standard", "premium"],
            value="standard"
        )
        
        width = st.select_slider(
            "Width",
            options=[512, 768, 1024, 1536, 2048],
            value=1024
        )
        
        height = st.select_slider(
            "Height",
            options=[512, 768, 1024, 1536, 2048],
            value=1024
        )
        
        num_images = st.slider(
            "Number of Images",
            min_value=1,
            max_value=3,
            value=1
        )

    col1, col2 = st.columns([2, 1])
    
    with col1:
        prompt = st.text_area(
            "Enter your prompt:",
            height=100,
            placeholder="Describe the image you want to generate..."
        )
        
        negative_prompt = st.text_area(
            "Negative prompt:",
            height=50,
            placeholder="Describe what you don't want in the image..."
        )

    with col2:
        st.markdown("<br>" * 2, unsafe_allow_html=True)
        generate_button = st.button("🎨 Generate Image")

    if generate_button and prompt:
        with st.spinner("🎨 Generating your masterpiece..."):
            images = generator.generate_image(
                prompt=prompt,
                negative_prompt=negative_prompt,
                width=width,
                height=height,
                quality=quality,
                num_images=num_images
            )
            
            if images:
                cols = st.columns(min(num_images, 2))
                for idx, image in enumerate(images):
                    with cols[idx % 2]:
                        st.image(image, caption=f"Generated Image {idx+1}", use_column_width=True)
                        
                        buf = io.BytesIO()
                        image.save(buf, format='PNG')
                        st.download_button(
                            label="Download Image",
                            data=buf.getvalue(),
                            file_name=f"generated_image_{idx+1}.png",
                            mime="image/png"
                        )

if __name__ == "__main__":
    main()