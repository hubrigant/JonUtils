import numpy as np
from scipy import spatial


def find_nearest(row, dest_df=None, geom1_col='geometry', geom2_col='geometry'):
    if dest_df is None:
        raise ValueError('Destination DataFrame (df2) argument not provided')
    distance_matrix: object = spatial.distance_matrix([[row[geom1_col].x, row[geom1_col].y]],
                                [[pt.x, pt.y] for pt in dest_df[geom2_col]])
    nn = np.array([[np.min(distance_matrix[0, ]), np.argmin(distance_matrix[0, ])]])
    distance = float(nn[:, 0][0])
    nearest_index = int(nn[:, 1][0])
    return nearest_index, distance
