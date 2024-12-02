import pandas as pd
import numpy as np
from PIL import Image

def preprocess_images(csv_path, save_folder, target_width=150):
    data = pd.read_csv(csv_path)
    depths = data['depth']
    pixel_data = data.drop(columns=['depth'])

    for i, depth in enumerate(depths):
        image_array = pixel_data.iloc[i].values.reshape(200, -1)
        img = Image.fromarray(np.uint8(image_array))
        resized_img = img.resize((target_width, image_array.shape[0]), Image.ANTIALIAS)
        resized_img.save(f"{save_folder}/frame_{depth}.png")
