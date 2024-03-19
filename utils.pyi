import cv2 as cv
import numpy as np


def put_text_rect(img: np.ndarray, text: str, scale: int, thickness: int,
                  text_color: tuple[int, int, int], rectangle_color: tuple[int, int, int],
                  font: int, offset: int, border: int | None, border_color: tuple[int, int, int]) -> np.ndarray:
    ox: int
    oy: int

    w: int
    h: int

    x1: int
    y1: int
    x2: int
    y2: int


def corner_rect(img: np.ndarray, bbox: list[int, int, int, int],
                l: int, rt: int, rectangle_color: tuple[int, int, int],
                center_color: tuple[int, int, int]) -> np.ndarray:
    x: int
    y: int
    w: int
    h: int
