import gradio as gr
import numpy as np
import cv2
import os
from PIL import Image, ImageEnhance

def convert_to_sketch(img, kernel_size=21, contrast=1.5, brightness=1.1):
    """
    Converts an image to sketch using OpenCV with adjustable parameters
    Args:
        img: Input PIL Image
        kernel_size: Controls line thickness (must be odd)
        contrast: Enhances line darkness (>1 = darker)
        brightness: Adjusts overall lightness (>1 = brighter)
    Returns:
        PIL Image of the sketch
    """
    # Convert PIL Image to OpenCV format (numpy array)
    img_cv = np.array(img)
    
    # Convert to grayscale
    gray = cv2.cvtColor(img_cv, cv2.COLOR_RGB2GRAY)
    
    # Invert colors
    inverted = 255 - gray
    
    # Apply Gaussian blur - kernel size affects line thickness
    if kernel_size % 2 == 0:  # Ensure odd number
        kernel_size += 1
    blurred = cv2.GaussianBlur(inverted, (kernel_size, kernel_size), 0)
    
    # Create pencil sketch effect
    sketch = cv2.divide(gray, 255 - blurred, scale=256)
    
    # Convert back to PIL Image
    sketch_pil = Image.fromarray(sketch)
    
    # Enhance contrast and brightness
    enhancer = ImageEnhance.Contrast(sketch_pil)
    sketch_pil = enhancer.enhance(contrast)
    
    enhancer = ImageEnhance.Brightness(sketch_pil)
    sketch_pil = enhancer.enhance(brightness)
    
    return sketch_pil
# Create a directory for example images if it doesn't exist
os.makedirs("examples", exist_ok=True)

# Sample image paths (relative to app directory)
EXAMPLE_IMAGES = [
    "examples/sample1.jpg",
    "examples/sample2.jpg"
]
# Gradio Interface
with gr.Blocks(title="Instant Sketch Generator (CPU)") as demo:
    gr.Markdown("""
    # ✏️ Instant Pencil Sketch (CPU Optimized)
    Converts photos to sketches in seconds using computer vision
    """)
    
    with gr.Row():
        with gr.Column():
            # Image upload
            input_img = gr.Image(
                label="Upload Image", 
                type="pil",
                height=300
            )
            
            # Sketch controls
            with gr.Accordion("Sketch Settings", open=False):
                line_thickness = gr.Slider(
                    3, 51, value=21, step=2,
                    label="Line Thickness (Odd numbers work best)"
                )
                contrast = gr.Slider(
                    1.0, 3.0, value=1.5, step=0.1,
                    label="Contrast (Darker lines)"
                )
                brightness = gr.Slider(
                    0.5, 2.0, value=1.1, step=0.1,
                    label="Brightness"
                )
            
            generate_btn = gr.Button("Generate Sketch", variant="primary")
        
        with gr.Column():
            # Output sketch
            output_img = gr.Image(
                label="Pencil Sketch", 
                type="pil",
                height=400
            )
  # Only add examples if the files exist
    if all(os.path.exists(img) for img in EXAMPLE_IMAGES):
        gr.Examples(
            examples=[
                [EXAMPLE_IMAGES[0], 21, 1.5, 1.1],
                [EXAMPLE_IMAGES[1], 15, 1.8, 1.0]
            ],
            inputs=[input_img, line_thickness, contrast, brightness],
            outputs=output_img,
            fn=convert_to_sketch,
            cache_examples=False  # Disable caching to prevent errors
        )
    # Button action
    generate_btn.click(
        fn=convert_to_sketch,
        inputs=[input_img, line_thickness, contrast, brightness],
        outputs=output_img
    )

# Launch app
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0")