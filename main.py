import numpy as np
import cv2
from draw_utils import draw_model
from cube import Cube
from scipy.spatial.transform import Rotation


def get_intrinsic_matrix(angle_x, angle_y, w, h):
    fx = w / np.tan(angle_x / 2)
    fy = h / np.tan(angle_y / 2)

    cx = w / 2
    cy = h / 2

    return np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]])


def project_point(intrinsic_matrix, point):
    uv = intrinsic_matrix.dot(point)
    return uv[:2] / uv[2]


if __name__ == "__main__":
    plane_shape = np.array([640, 640])
    camera_angle = (90, 90)

    r = 100

    intrinsic_matrix = get_intrinsic_matrix(*camera_angle, *plane_shape)
    # print(angle_coordinates)

    shift = 0
    rotation = 1

    while True:
        cube = Cube(r)

        matrix = Rotation.from_euler(
            "zx", [rotation, rotation * 0.5], degrees=True
        ).as_matrix()

        cube.vertex_list = cube.vertex_list.dot(matrix)

        cube.vertex_list[:, 2] += 400
        plane = np.zeros(shape=(*plane_shape, 3))

        # plane += 255

        # draw_point(plane, plane_shape / 2)
        cube.vertex_list[:, 0] += shift

        cube.apply_tranform(intrinsic_matrix)
        draw_model(plane, cube)

        cv2.imshow("res", plane)
        if cv2.waitKey(1) == ord("q"):
            break

        shift += 0
        rotation += 0.2

    cv2.destroyAllWindows()
