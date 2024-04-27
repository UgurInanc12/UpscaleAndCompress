from PIL import Image
import os
import subprocess

def upscale_image_with_upscayl(input_image, output_image):
    try:
        

        subprocess.run(["upscayl-bin", "-i", input_image, "-o", output_image, "-n", "ultrasharp", "-f", "png", "-g", "0"])
        print(f"Upscaled {input_image} and saved to {output_image}.")
        
        print("---- nvidia bc3 starting ---")
        print("image is: ", os.path.splitext(os.path.basename(input_image))[0])
        print("output_image is: ", os.path.dirname(os.path.dirname(output_image)))
        
        subprocess.run(["nvcompress", "-bc3", "-highest", output_image, os.path.dirname(os.path.dirname(output_image)) + "\\" + os.path.splitext(os.path.basename(input_image))[0]+ ".dds"])
        print(f"Converted {output_image} to {os.path.dirname(os.path.dirname(output_image))}\{os.path.splitext(os.path.basename(input_image))[0]}.dds using bc3 compression.")

    except subprocess.CalledProcessError as e:
        print(f"Error upscaling {input_image}: {e}")

def batch_upscale_images(input_folder):
    for root, _, files in os.walk(input_folder):
        for filename in files:
            if filename.lower().endswith(".png"):
                input_path = os.path.join(root, filename)
                output_folder = os.path.join(root, "upscaled")
                os.makedirs(output_folder, exist_ok=True)
                output_path = os.path.join(output_folder, filename)
                
                upscale_image_with_upscayl(input_path, output_path)

if __name__ == "__main__":
    input_folder2 = input("What is the location? ")
    input_folder = input_folder2.replace("\\", "\\\\")
    print(input_folder)

    batch_upscale_images(input_folder)  # Upscaled files will be saved in the "upscaled" folder