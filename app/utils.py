import pandas as pd
import cv2

def get_depths(csv_path):
    data = pd.read_csv(csv_path)
    return data['depth']

def apply_color_map(input_path, output_path):
    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    colored_img = cv2.applyColorMap(img, cv2.COLORMAP_JET)
    cv2.imwrite(output_path, colored_img)
