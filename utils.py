import cv2 as cv
import numpy as np
from utils import *

def put_text_rect(img, text, pos, scale=3, thickness=3, text_color=(255, 255, 255),
                  rectangle_color=(255, 0, 255), font=cv.FONT_HERSHEY_PLAIN,
                  offset=10, border=None, border_color=(0, 255, 0)) -> np.ndarray:
    ox, oy = pos
    w, h = cv.getTextSize(text, font, scale, thickness)[0]

    x1, y1, x2, y2 = ox - offset, oy + offset, ox + w + offset, oy - h - offset

    cv.rectangle(img, (x1, y1), (x2, y2), rectangle_color, cv.FILLED)
    if border is not None:
        cv.rectangle(img, (x1, y1), (x2, y2), border_color, border)
    cv.putText(img, text, (ox, oy), font, scale, text_color, thickness)

    return img

def corner_rect(img, bbox, l=30, t=5, rt=1,
                rectangle_color=(255, 0, 255), center_color=(0, 255, 0)) -> np.ndarray:
    x, y, w, h = bbox
    x1, y1 = x + w, y + h
    if rt != 0:
        cv.rectangle(img, bbox, rectangle_color, rt)

    cv.line(img, (x, y), (x + l, y), center_color, t)
    cv.line(img, (x, y), (x, y + l), center_color, t)

    cv.line(img, (x1, y), (x1 - l, y), center_color, t)
    cv.line(img, (x1, y), (x1, y + l), center_color, t)

    cv.line(img, (x, y1), (x + l, y1), center_color, t)
    cv.line(img, (x, y1), (x, y1 - l), center_color, t)

    cv.line(img, (x1, y1), (x1 - l, y1), center_color, t)
    cv.line(img, (x1, y1), (x1, y1 - l), center_color, t)

    return img