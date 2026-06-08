import os
import glob
import numpy as np
from PIL import Image

# tab10 colors
old_colors = np.array([
    [31, 119, 180],   # 0: blue
    [255, 127, 14],   # 1: orange
    [44, 160, 44],    # 2: green
    [214, 39, 40],    # 3: red
    [148, 103, 189],  # 4: purple
    [140, 86, 75],    # 5: brown
    [227, 119, 194],  # 6: pink
    [127, 127, 127],  # 7: gray
    [188, 189, 34],   # 8: olive
    [23, 190, 207],   # 9: cyan
])

# New colors from app.py
def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

new_colors_hex = [
    "#b76563",  # 0: Vegetarians
    "#bc7933",  # 1: Regulars
    "#687643",  # 2: Wellness
    "#b64828",  # 3: Promoters
    "#c88d40",  # 4: Loyalists
    "#368689",  # 5: Families
    "#36668d",  # 6: Economizers
    "#6c4d36"   # 7: Techies
]
new_colors = np.array([hex_to_rgb(c) for c in new_colors_hex])

def recolor_image(img_path):
    img = Image.open(img_path).convert("RGB")
    pixels = np.array(img, dtype=np.float32)
    
    # Calculate difference between max and min RGB for each pixel
    max_c = np.max(pixels, axis=2)
    min_c = np.min(pixels, axis=2)
    saturation = max_c - min_c
    
    # Only recolor pixels that are not grayscale
    mask = saturation > 15
    
    colored_pixels = pixels[mask]
    if len(colored_pixels) == 0:
        return
        
    # We estimate the original solid color by assuming it's a blend of tab10 and white.
    # We can just match the hue. To do this simply, we find the tab10 color that is closest in angle.
    # Normalize pixels and tab10 to have unit length for cosine similarity
    cp_norm = colored_pixels / np.linalg.norm(colored_pixels, axis=1, keepdims=True)
    tab10_norm = old_colors / np.linalg.norm(old_colors, axis=1, keepdims=True)
    
    # Compute cosine similarity
    similarity = np.dot(cp_norm, tab10_norm.T)
    best_match = np.argmax(similarity, axis=1)
    
    # Now we know which cluster each pixel belongs to.
    # We want to replace it with the new color, keeping the same lightness/blend with white.
    # A simple way: find how much white was mixed in.
    # old_pixel = alpha * old_color + (1-alpha) * 255
    # So alpha * (255 - old_color) = 255 - old_pixel
    # alpha = mean((255 - old_pixel) / (255 - old_color))
    
    new_pixels = np.zeros_like(colored_pixels)
    for i in range(8):  # We only have 8 new colors
        cluster_mask = (best_match == i)
        if not np.any(cluster_mask):
            continue
            
        cp = colored_pixels[cluster_mask]
        old_c = old_colors[i]
        new_c = new_colors[i]
        
        # Estimate alpha (0 = white, 1 = solid color)
        # We avoid division by zero by adding a small epsilon
        alpha = np.mean((255.0 - cp) / (255.0 - old_c + 1e-5), axis=1, keepdims=True)
        alpha = np.clip(alpha, 0, 1)
        
        # Apply alpha to new color
        new_p = alpha * new_c + (1 - alpha) * 255.0
        new_pixels[cluster_mask] = new_p
    
    # Update the image
    pixels[mask] = new_pixels
    
    # Save the recolored image
    result = Image.fromarray(np.clip(pixels, 0, 255).astype(np.uint8))
    result.save(img_path)
    print(f"Recolored {os.path.basename(img_path)}")

charts_dir = r"c:\Users\carlo\Documents\Semestre 4\ML 2\costumer_seg_app_cm\imagens\charts"
for img_name in ["pca_projection.png", "umap_projection.png", "tsne_projection.png", "silhouette_blades.png"]:
    p = os.path.join(charts_dir, img_name)
    if os.path.exists(p):
        recolor_image(p)
