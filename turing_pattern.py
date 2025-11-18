from PIL import Image, ImageFilter

# Load the original image
img = Image.open('original.jpg')

# Apply blur and sharpen repeatedly for 1000 iterations
for i in range(1000):
    # Apply blur
    if (i + 1) % 100 == 0:
        print(f"Iteration {i+1}/1000: Applying blur and sharpen")
    img = img.filter(ImageFilter.BLUR)
    # Apply sharpen (using UnsharpMask for sharpening effect)
    img = img.filter(ImageFilter.UnsharpMask(radius=1, percent=150, threshold=3))

# Save the resulting image
img.save('turing_pattern.jpg')

print("Turing pattern generation complete. Saved as 'turing_pattern.jpg'")
