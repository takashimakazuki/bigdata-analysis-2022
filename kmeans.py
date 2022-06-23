

from math import inf
import matplotlib.pyplot as plt

points = {
    'A': [2, 10],
    'B': [2, 5],
    'C': [8, 4],
    'D': [5, 8],
    'E': [7, 5],
    'F': [6, 4],
    'G': [1, 2],
    'H': [4, 9]
}



def get_dist(point1, point2):
    return pow(point1[0] - point2[0], 2) + pow(point1[1] - point2[1], 2)


def calculate_cluster_center(cluster_center_points):
    cluster_info = {}

    # 各ポイントが所属するクラスタを計算
    for point_key, point in points.items():
        min_dist = inf
        min_cluster_point = 0
        for cluster_index, cluster_point in enumerate(cluster_center_points):
            dist = get_dist(cluster_point, point)
            if min_dist > dist:
                min_dist = dist
                min_cluster_point = cluster_index
        
        try:
            cluster_info[min_cluster_point].append(point_key)
        except KeyError:
            cluster_info[min_cluster_point] = [point_key]


    # 各クラスタの中心点を計算
    cluster_center_points = []
    for cluster_index, point_keys in cluster_info.items():
        x_g = sum([points[key][0] for key in point_keys]) / len(point_keys)
        y_g = sum([points[key][1] for key in point_keys]) / len(point_keys)
        cluster_center_points.append([x_g, y_g])

    return cluster_center_points, cluster_info


def is_same(old, new):
    if len(old) != len(new):
        return False

    for o, n in zip(old, new):
        if not (o[0] == n[0] and o[1] == n[1]):
            return False
    return True
    

def main():
    # cluster 0, 1, 2の中心点
    cluster_center_points = [
        [2, 10],
        [5, 8],
        [1, 2],
    ]
    old_cluster_center_points = []

    cluster_info = None
    while not is_same(old_cluster_center_points, cluster_center_points):
        old_cluster_center_points = cluster_center_points
        cluster_center_points, cluster_info = calculate_cluster_center(cluster_center_points)
        print(cluster_center_points, cluster_info)
    

    colors = ['red', 'green', 'blue']
    for color, pos_key_list in zip(colors, cluster_info.values()):
        x = []
        y = []
        for pos_key in pos_key_list:
            x.append(points[pos_key][0])
            y.append(points[pos_key][1])
        plt.scatter(x, y, c=color)

    plt.show()



if __name__ == '__main__':
    main()