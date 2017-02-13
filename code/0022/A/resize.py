#al.py

def resize(img, iw, ih):
    w, h = img.size
    w_ratio = w/iw
    h_ratio = h/ih
    if w_ratio > 1 and w_ratio > h_ratio:
        ratio = w_ratio
    elif h_ratio > 1 and h_ratio > w_ratio:
        ratio = h_ratio
    else:
        ratio = 1
    return img.resize(
        (int(w / ratio), int(h / ratio))
        , Image.ANTIALIAS)