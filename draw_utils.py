import cv2
import numpy as np
from model import Model


def draw_point(img, coord: np.array):
    cv2.circle(img, coord.astype(np.int32), 3, (0, 255, 0), 2)


def draw_line(img, p1, p2):
    cv2.line(img, p1.astype(np.int32), p2.astype(np.int32), (0, 0, 255), 1, 1, 0)


def draw_model(plane, model: Model):
    for p1_idx, p2_idx in model.edges_list_id:
        assert model.vertex_list[p1_idx][2] == 1 and model.vertex_list[p2_idx][2] == 1
        draw_line(plane, model.vertex_list[p1_idx][:2], model.vertex_list[p2_idx][:2])

    for i in model.vertex_list:
        draw_point(plane, i[:2])
