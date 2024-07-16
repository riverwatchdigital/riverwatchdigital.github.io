from PIL import Image
import os

# get paths to all images
cwd = os.getcwd()
gallerydir = os.path.join(cwd, "gallery")
photo_names = os.listdir(gallerydir)
gallery_photos = [os.path.join(gallerydir, photo_name) for photo_name in photo_names]

for photo_name in photo_names:
    fpath = os.path.join(gallerydir, photo_name)
    image = Image.open(fpath)
    x, y = image.size
    scalex = round(x/1920,3)
    scaley = round(y/1080,3)
    scalef = scalex if scalex < scaley else scaley
    image.resize((int(x//scalef), int(y//scalef)))
    print(os.path.isfile(fpath), image.size, (int(x//scalef), int(y//scalef)), scalef, photo_name)
    #https://stackoverflow.com/questions/19303621/why-is-the-quality-of-jpeg-images-produced-by-pil-so-poor
    image.save(os.path.join(gallerydir,f"resized_{photo_name}"), format='JPEG', subsampling=0, quality=95)
breakpoint()