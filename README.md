# sketch_generator

![Sketch Banner](https://huggingface.co/spaces/gopi135942/ghibli_art/resolve/main/banner.png)

Transform your favorite photos into stunning pencil sketches in seconds using this lightweight AI-powered web app!  
Built with **OpenCV**, **Gradio**, and optimized for **CPU** usage – no GPU required!

🌐 [Try it live on Hugging Face →](https://huggingface.co/spaces/gopi135942/ghibli_art)

---

## 🚀 Features

- 📸 Upload any image and turn it into a pencil sketch
- 🎚️ Customize line thickness, contrast, and brightness
- 🖥️ Fully CPU-compatible and lightweight
- 🧰 Built with Python, OpenCV, Pillow, and Gradio
- 🧪 Includes example images for quick testing

---

## 🖼️ Demo

| Original Image | Pencil Sketch |
|----------------|----------------|
| ![original](examples/sample1.jpg) | ![sketch](examples/sample1_sketch.jpg) |

---

## 🧠 How It Works

1. Convert image to grayscale
2. Invert the grayscale image
3. Apply Gaussian Blur
4. Blend original grayscale with blurred inverted image using `cv2.divide`
5. Enhance the result with adjustable contrast and brightness

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/gopi135942/instant-sketch-generator.git
cd instant-sketch-generator
