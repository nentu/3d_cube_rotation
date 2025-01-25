import cv2
import numpy as np


def draw_point(img, coord: np.array):
    cv2.circle(img, coord.astype(np.int32), 3, (0, 255, 0), 2)


def draw_line(img, p1, p2):
    cv2.line(img, p1.astype(np.int32), p2.astype(np.int32), (0, 0, 255), 1, 1, 0)


def gen_idx_seq():
    res = list()
    for i in range(4):  # upper plane
        res.append([i, (i + 1) % 4])
    for i in range(4):  # down plane
        res.append([i + 4, (i + 1) % 4 + 4])
    for i in range(4):  # vertical lines
        res.append([i, i + 4])
    return res


def draw_cube(plane, angle_coordinates):
    idx_seq = gen_idx_seq()

    for p1_idx, p2_idx in idx_seq:
        draw_line(plane, angle_coordinates[p1_idx], angle_coordinates[p2_idx])

    for i in angle_coordinates:
        draw_point(plane, i)
