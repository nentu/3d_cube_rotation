import numpy as np
from dataclasses import dataclass


@dataclass
class Model:
    vertex_list: np.array
    edges_list_id: np.array
    poly_list_id: np.array

    def apply_tranform(self, matrix: np.array):
        for i in range(len(self.vertex_list)):
            self.vertex_list[i] = matrix.dot(self.vertex_list[i])
            self.vertex_list[i] = self.vertex_list[i] / self.vertex_list[i][2]


if __name__ == "__main__":
    print(Model([1, 2], [], []).vertex_list)
