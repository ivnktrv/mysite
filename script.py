import os

files = os.listdir("img/blender/audio_vis")
for file in files:
    print(f'''
<video controls class="video-audvis-container">
    <source class="video-audvis-container" src="/img/blender/audio_vis/{file}">
</video>''')