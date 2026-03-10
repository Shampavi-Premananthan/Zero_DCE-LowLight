import torch
import torch.nn as nn
import torchvision
import numpy as np
from PIL import Image
import gradio as gr
import os
import sys

# Add the code directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Zero-DCE_code'))

import model as DCEModel


class LowLightEnhancer:
    def __init__(self, checkpoint_path='Zero-DCE_code/snapshots/Epoch99.pth'):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        print(f"Using device: {self.device}")
        
        # Load model
        self.model = DCEModel.enhance_net_nopool().to(self.device)
        
        if os.path.exists(checkpoint_path):
            state_dict = torch.load(checkpoint_path, map_location=self.device)
            load_info = self.model.load_state_dict(state_dict, strict=False)
            if load_info.missing_keys:
                print(f"Warning: missing keys in checkpoint: {load_info.missing_keys}")
            if load_info.unexpected_keys:
                print(f"Warning: unexpected keys in checkpoint: {load_info.unexpected_keys}")
            print("Model loaded successfully!")
        else:
            print(f"Warning: Checkpoint not found at {checkpoint_path}")
        
        self.model.eval()
    
    def enhance(self, image):
        """
        Enhance low-light image (no user strength control)
        Args:
            image: PIL Image or numpy array
        Returns:
            Tuple of (Intermediate Enhanced PIL Image, Final Enhanced PIL Image)
        """
        # Convert to numpy if needed
        if isinstance(image, Image.Image):
            image = np.array(image)
        # Normalize to [0, 1]
        data_lowlight = image.astype(np.float32) / 255.0
        # Convert to tensor
        data_lowlight = torch.from_numpy(data_lowlight).float()
        data_lowlight = data_lowlight.permute(2, 0, 1)
        data_lowlight = data_lowlight.to(self.device).unsqueeze(0)
        # Inference - model returns (enhance_image_1, enhance_image, r)
        with torch.no_grad():
            enhance_image_1, enhanced_image, _ = self.model(data_lowlight)
        # Convert intermediate to PIL Image
        intermediate_img = enhance_image_1.squeeze().permute(1, 2, 0).cpu().numpy()
        intermediate_img = (intermediate_img * 255).astype(np.uint8)
        # Convert final to PIL Image
        final_img = enhanced_image.squeeze().permute(1, 2, 0).cpu().numpy()
        final_img = (final_img * 255).astype(np.uint8)
        return Image.fromarray(intermediate_img), Image.fromarray(final_img)


# Initialize the enhancer
enhancer = LowLightEnhancer()


def enhance_image(image):
    """Gradio interface function (no strength)"""
    if image is None:
        return None, None
    intermediate, final = enhancer.enhance(image)
    return intermediate, final


# Modern professional theme
custom_theme = gr.themes.Soft(
    primary_hue="indigo",
    secondary_hue="blue",
    neutral_hue="slate",
).set(
    button_primary_background_fill="linear-gradient(90deg, #4F46E5 0%, #7C3AED 100%)",
    button_primary_background_fill_hover="linear-gradient(90deg, #4338CA 0%, #6D28D9 100%)",
    button_primary_text_color="white",
)

custom_css = """
    .gradio-container {
        max-width: 1600px !important;
        margin: 0 auto !important;
    }
    footer {
        visibility: hidden !important;
    }
    .app-header {
        text-align: center !important;
        padding: 30px 20px !important;
        margin-bottom: 30px !important;
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%) !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1) !important;
    }
    .app-header h1 {
        color: white !important;
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        margin: 0 0 10px 0 !important;
    }
    .app-header p {
        color: rgba(255, 255, 255, 0.95) !important;
        font-size: 1.1rem !important;
        margin: 0 !important;
    }
"""

# Create modern Blocks interface
with gr.Blocks(title="Zero-DCE Enhancement", theme=custom_theme, css=custom_css) as demo:
    
    # Header
    gr.HTML("""
        <div class="app-header">
            <h1>🌙 Zero-DCE Low-Light Enhancement</h1>
            <p>Transform dark images into bright, clear photos with AI</p>
        </div>
    """)
    
    with gr.Row():
        with gr.Column(scale=1):
            input_image = gr.Image(
                type="pil", 
                label="📸 Input Image",
                height=450
            )
            # Removed strength slider
            enhance_btn = gr.Button("✨ Enhance Image", variant="primary", size="lg")
        
        with gr.Column(scale=2):
            with gr.Row():
                output_intermediate = gr.Image(
                    type="pil", 
                    label="⚡ Intermediate Result (4 iterations)",
                    height=450
                )
                output_final = gr.Image(
                    type="pil", 
                    label="🌟 Final Result (8 iterations)",
                    height=450
                )
    
    # Info section
    with gr.Accordion("ℹ️ Information", open=False):
        gr.Markdown("""
        ### About Zero-DCE
        Zero-DCE (Zero-Reference Deep Curve Estimation) is a lightweight deep learning method for low-light image enhancement.
        
        **Features:**
        - No paired training data required
        - Fast inference speed
        - Preserves image details
        - Adjustable enhancement strength
        
        **Usage:**
        1. Upload a low-light image
        2. Adjust strength if needed (default 1.0 works well)
        3. Click "Enhance Image"
        4. Compare intermediate and final results
        """)
    
    # Event handlers
    enhance_btn.click(
        fn=enhance_image,
        inputs=[input_image],
        outputs=[output_intermediate, output_final]
    )

if __name__ == "__main__":
    demo.queue().launch(
        server_name="0.0.0.0", 
        server_port=7860,
        show_api=True
    )
