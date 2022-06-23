import matplotlib.pyplot as plt


class Point(object):
    def __init__(self, key, coordinate) -> None:
        self.key = key
        self.x = coordinate[0]
        self.y = coordinate[1]
        self.visited = False
        self.label = -1
        self.point_type = ""

    def visit(self):
        self.visited = True
    

# eps = 2
# minpts = 3
# manhattan distance

class Dbscan(object):
    def __init__(self, points, eps, minpts) -> None:
        self.points = points
        self.eps = eps
        self.minpts = minpts
        self.label = 0
    
    def get_neighbor_pts(self, point):
        return [p for p in self.points if self.get_mht_dist(p, point) < self.eps]

    def fit(self):
        for p in self.points:
            if not p.visited:
                p.visit()
                neighbor_pts = self.get_neighbor_pts(p)
                if len(neighbor_pts) >= self.minpts:
                    p.point_type = "CORE"
                    self.expand_neighbor(p, neighbor_pts)
                    self.label += 1
                else:
                    p.point_type = "NOISE"
    
    def expand_neighbor(self, p, neighbor_pts):
        p.label = self.label
        for q in neighbor_pts:
            if not q.visited:
                q.visit()
                neighbor_pts_q = self.get_neighbor_pts(q)
                if len(neighbor_pts_q) >= self.minpts:
                    q.point_type = "CORE"
                    self.expand_neighbor(q, neighbor_pts_q)
            if q.label == -1:
                q.label = self.label

    def get_mht_dist(self, point1, point2):
        return abs(point1.x - point2.x) + abs(point1.y - point2.y)
    

def main():
    points = [
        {'key': 'A', 'coordinate': [0, 0]},
        {'key': 'B', 'coordinate': [2, 0]},
        {'key': 'C', 'coordinate': [2, 1]},
        {'key': 'D', 'coordinate': [3, 0]},
        {'key': 'E', 'coordinate': [4, 1]},
        {'key': 'F', 'coordinate': [5, 0]},
        {'key': 'G', 'coordinate': [6, 0]},
        {'key': 'H', 'coordinate': [8, 0]},
    ]
    EPS = 2
    MIN_PTS = 3
    points = [Point(p['key'], p['coordinate']) for p in points]
    dbscan = Dbscan(points, EPS, MIN_PTS)
    dbscan.fit()
    colors = ['red', 'green', 'blue']

    for p in points:
        plt.scatter(p.x, p.y, c=colors[p.label])
    
    plt.legend(loc='upper left')
    plt.xlim(-1, 10)
    plt.ylim(-1, 10)
    plt.show()


if __name__ == '__main__':
    main()