from PIL import Image
import os

# get paths to all images in the gallery folder
# images in the gallery folder are the unprocessed, not resized ones.
cwd = os.getcwd()
gallerydir = os.path.join(cwd, "gallery")
photo_names = [x for x in os.listdir(gallerydir) if os.path.isfile(os.path.join(gallerydir, x))]

for photo_name in photo_names:
    fpath = os.path.join(gallerydir, photo_name)
    print(fpath)

    image = Image.open(fpath)
    x, y = image.size
    scalex = round(x/1920,3)
    scaley = round(y/1080,3)
    scalef = scalex if scalex < scaley else scaley
    
    newx = int(x//scalef)
    newy = int(y//scalef)

    image = image.resize((newx, newy))

    print(os.path.isfile(fpath), image.size, (newx, newy), scalef, photo_name)

    #https://stackoverflow.com/questions/19303621/why-is-the-quality-of-jpeg-images-produced-by-pil-so-poor
    image.save(os.path.join(gallerydir,f"resized_{photo_name}"), format='jpeg', subsampling=0, quality=95)
breakpoint()