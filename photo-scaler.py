#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Alberto Salcines Menezo
# Created Date: //
# Description :
# version ='1.0'
# ---------------------------------------------------------------------------
from PIL import Image
import os


def check_and_adjust_aspect_ratio(input_folder, output_folder, target_width, target_height):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Calculate the target aspect ratios for both landscape and portrait
    target_aspect_ratio_landscape = target_width / target_height
    target_aspect_ratio_portrait = target_height / target_width

    # Iterate over each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.JPG')):
            # Open the image
            img = Image.open(os.path.join(input_folder, filename))
            img_width, img_height = img.size

            # Calculate the aspect ratio.
            aspect_ratio = img_width / img_height

            # Check if the aspect ratio fits either landscape or portrait.
            if not (aspect_ratio == target_aspect_ratio_landscape or aspect_ratio == target_aspect_ratio_portrait):
                # Determine the new size for the canvas.
                if aspect_ratio > 1:
                    new_img = Image.new("RGB", (target_width, target_height), (255, 255, 255))
                    new_size = (target_width, int(target_width / aspect_ratio))
                    new_img.paste(img.resize(new_size), ((target_width - new_size[0]) // 2, (target_height - new_size[1]) // 2))

                else:
                    new_img = Image.new("RGB", (target_height, target_width), (255, 255, 255))
                    new_size = (int(target_width * aspect_ratio), target_width)
                    new_img.paste(img.resize(new_size), ((target_height - new_size[0]) // 2, (target_width - new_size[1]) // 2))

                # Save the new image to the output folder.
                new_img.save(os.path.join(output_folder, filename))
            else:
                # Save the original image to the output folder if it already fits the aspect ratio.
                img.save(os.path.join(output_folder, filename))


# Define input and output folders and target dimensions in cm (converted to pixels assuming 300 DPI)
input_folder = "C:/Users/Alberto/Desktop/Nueva carpeta"
output_folder = "C:/Users/Alberto/Desktop/output_folder"
target_height_cm = 11
target_width_cm = 15

dpi = 300
target_width_px = int(target_width_cm * dpi / 2.54)
target_height_px = int(target_height_cm * dpi / 2.54)

# Call the function to check and adjust aspect ratios of images in the input folder
check_and_adjust_aspect_ratio(input_folder, output_folder, target_width_px, target_height_px)
