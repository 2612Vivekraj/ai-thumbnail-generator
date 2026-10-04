import fal_client
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def generate_batch(prompts: list, output_folder: str = "thumbnails"):
    """
    Generate multiple thumbnails in one go
    """
    os.makedirs(output_folder, exist_ok=True)
    
    for i, prompt in enumerate(prompts):
        print(f"Generating thumbnail {i+1}/{len(prompts)}...")
        
        result = fal_client.run(
            "fal-ai/fast-sdxl",
            arguments={
                "prompt": prompt + ", youtube thumbnail, high quality, vibrant, professional, 1280x720",
                "image_size": "landscape_hd",
                "num_inference_steps": 25,
                "guidance_scale": 7.0
            }
        )
        
        image_url = result["images"][0]["url"]
        response = requests.get(image_url)
        
        output_path = f"{output_folder}/thumbnail_{i+1}.png"
        with open(output_path, "wb") as f:
            f.write(response.content)
        
        print(f"✅ Saved: {output_path}")
    
    print(f"\n🎉 All {len(prompts)} thumbnails generated!")

if __name__ == "__main__":
    # Example prompts for gaming channel
    sample_prompts = [
        "Epic gaming setup with RGB lights, gaming controller, dark background with neon blue",
        "Minecraft gameplay thumbnail, character with diamond sword, explosion background",
        "Fortnite battle royale, character jumping, storm clouds, vibrant colors",
        "GTA 6 news thumbnail, luxury car, city skyline, dramatic lighting",
        "Valorant gameplay, character with gun, tactical background, red and black theme",
        "Among us gameplay, astronaut character, space background, funny expression",
        "Free fire battle, character shooting, fire effects, action scene",
        "PUBG mobile, squad gameplay, helicopter, battleground, intense action",
        "Call of Duty warzone, soldier with sniper, urban warfare, dark theme",
        "Roblox gaming, cartoon character, colorful game world, fun and exciting"
    ]
    
    generate_batch(sample_prompts)
