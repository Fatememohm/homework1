import math


class Point:

    def move(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def reset(self) -> None:
        self.move(0, 0, 0)

    def calculate_distance(self, other: "Point") -> float:
        return math.hypot(self.x - other.x, self.y - other.y, self.z - other.z)

    def equal(self, other: "Point"):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False


point1 = Point()
point2 = Point()
point3 = Point()
point4 = Point()
point5 = Point()



point1.reset()
point2.move(0, 1, 8)
point3.move(4, 4, 4)
point4.move(7, 7, 7)
point5.move(1, 8, 4)

print(point5.equal(point3))
print(point1.calculate_distance(point4))
point2.move(3, 4, 5)
print(point2.x, point2.y, point2.z)
point5.reset()
print(point5.x, point5.y, point5.z)
