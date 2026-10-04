import fal_client
import os
from dotenv import load_dotenv

load_dotenv()

def generate_thumbnail(prompt: str, output_path: str = "thumbnail.png"):
    """
    Generate a YouTube thumbnail using fal.ai
    """
    # Use fal.ai's fast image generation model
    result = fal_client.run(
        "fal-ai/fast-sdxl",
        arguments={
            "prompt": prompt + ", youtube thumbnail, high quality, vibrant colors, professional design, 1280x720",
            "image_size": "landscape_hd",
            "num_inference_steps": 30,
            "guidance_scale": 7.5
        }
    )
    
    # Download the generated image
    image_url = result["images"][0]["url"]
    import requests
    response = requests.get(image_url)
    
    with open(output_path, "wb") as f:
        f.write(response.content)
    
    print(f"✅ Thumbnail saved to {output_path}")
    return output_path

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", type=str, required=True, help="Description of thumbnail")
    parser.add_argument("--output", type=str, default="thumbnail.png", help="Output file path")
    args = parser.parse_args()
    
    generate_thumbnail(args.prompt, args.output)
