class circle:
    def __init__(self, r):
        self.r = r
    def perimeter(self):
        return 2 * 3.1416 * self.r
    def area(self):
        return 3.1416 * self.r ** 2
radius = int(input("Enter radius: "))
choices = int(input("Enter choice (1 is perimeter, 2 is area): "))
obj = circle(radius)
if choices == 1:
    result = obj.perimeter()
    print(f"Result = {result}")
elif choices == 2:
    result = obj.area()
    print(f"Result = {result}")