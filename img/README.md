This folder contains images used in the main website.

## MAIN
The images in this folder are those shown on the homepage as the hero images. They are called within the grayscale.css file.

## GALLERY
The images in this folder are those shown on the mosaic gallery page. There is liquid templating that Jekyll reads to figure out which images to use. In short, those rules are:<br>
- if image.path contains 'img/gallery'
- if image.path contains 'resized_'
- unless image.path contains 'vert'
<br>
pay close attention to the naming convention used.

## RESIZEIMG.PY
This script is used to resize all the images uploaded. This is done to optimize them for web viewing.<br>
To run the script, install the Pillow python library to a virtual environment.<br>
The script will save the resized image as a file with the same name but 'resized_' appended to the front. (resized_ORIGINALNAME)<br>

## USAGE
This script should be called from the directory that this README file is in - ie, from the ```/img``` directory.<br>
1) Place all images you want into the ```/img/gallery/``` folder.
2) Run the script with ```python resizeimg.py```.
3) Move the resized photos with name ```resized_*``` to the desired folders, such as ```/img/gallery/automotive/```
4) Delete the original pictures from the ```/img/gallery/``` folder, or move them elsewhere.
