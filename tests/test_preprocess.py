from app.preprocess import preprocess_images
import os

def test_preprocess_images():
    test_csv = "tests/test_data.csv"
    output_folder = "tests/output"
    preprocess_images(test_csv, output_folder)
    assert len(os.listdir(output_folder)) > 0
