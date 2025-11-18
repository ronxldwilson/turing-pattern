import numpy as np
from PIL import Image

# Parameters for Gray-Scott model (spots pattern)
width, height = 256, 256
Du = 0.16  # Diffusion rate for u
Dv = 0.08  # Diffusion rate for v
F = 0.035  # Feed rate
K = 0.065  # Kill rate
dt = 0.1   # Time step
steps = 10000  # Number of iterations

# Initialize concentrations
u = np.ones((height, width))
v = np.zeros((height, width))

# Add perturbation in the center
u[height//2-10:height//2+10, width//2-10:width//2+10] = 0.5
v[height//2-10:height//2+10, width//2-10:width//2+10] = 0.25

# Function to compute Laplacian using finite differences
def laplacian(Z):
    return (np.roll(Z, 1, 0) + np.roll(Z, -1, 0) + np.roll(Z, 1, 1) + np.roll(Z, -1, 1) - 4 * Z) / (1**2)

# Simulation loop
for step in range(steps):
    lap_u = laplacian(u)
    lap_v = laplacian(v)
    uvv = u * v * v
    u += (Du * lap_u - uvv + F * (1 - u)) * dt
    v += (Dv * lap_v + uvv - (F + K) * v) * dt

# Normalize u to 0-255 and save as image
u_normalized = (u - u.min()) / (u.max() - u.min()) * 255
u_img = u_normalized.astype(np.uint8)
img = Image.fromarray(u_img, mode='L')
img.save('gray_scott.jpg')

print("Gray-Scott simulation complete. Saved as 'gray_scott.jpg'")
