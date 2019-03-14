import os
import secrets
from PIL import Image
from setup import app

def save_image(form_img, relative_path):
    _, form_img_ext = os.path.splitext(form_img.filename)
    random_hex = secrets.token_hex(8)
    form_img_new_fn = random_hex + form_img_ext
    img_storing_path = os.path.join(app.root_path, relative_path, form_img_new_fn)
    img_obj = Image.open(form_img)
    img_obj.thumbnail(size=(200, 270))
    img_obj.save(img_storing_path)
    return form_img_new_fn
