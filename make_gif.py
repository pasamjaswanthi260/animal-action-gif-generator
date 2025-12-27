from PIL import Image


img = Image.open("duck_actions.jpg")

width, height = img.size

frames = []
frames_count = 4  

frame_width = width 

for i in range(frames_count):
    left = i * frame_width
    right = left + frame_width
    frame = img.crop((left, 0, right, height))
    frames.append(frame)

frames[0].save(
    "dog.gif",
    save_all=True,
    append_images=frames[1:],
    duration=400,
    loop=0
)

print("GIF created successfully")

