from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from app.preprocess import preprocess_images
from app.utils import get_depths, apply_color_map
import os

app = FastAPI()

# Constants
DATA_FOLDER = "data/"
RESIZED_FOLDER = os.path.join(DATA_FOLDER, "resized_images")
COLORED_FOLDER = os.path.join(DATA_FOLDER, "colored_images")
CSV_FILE = os.path.join(DATA_FOLDER, "Challenge.csv")

# Ensure folders exist
os.makedirs(RESIZED_FOLDER, exist_ok=True)
os.makedirs(COLORED_FOLDER, exist_ok=True)

# Preprocess images at startup
preprocess_images(CSV_FILE, RESIZED_FOLDER)

@app.get("/get_frames")
def get_frames(depth_min: float, depth_max: float):
    depths = get_depths(CSV_FILE)
    filtered_depths = depths[(depths >= depth_min) & (depths <= depth_max)]

    if filtered_depths.empty:
        raise HTTPException(status_code=404, detail="No frames found for the specified depth range.")

    files = []
    for depth in filtered_depths:
        input_path = os.path.join(RESIZED_FOLDER, f"frame_{depth}.png")
        output_path = os.path.join(COLORED_FOLDER, f"colored_frame_{depth}.png")
        if not os.path.exists(output_path):
            apply_color_map(input_path, output_path)
        files.append(FileResponse(output_path, media_type="image/png"))

    return files
