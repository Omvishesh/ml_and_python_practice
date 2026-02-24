class Shape:
    def area():
        pass
    
class Circle:
    def area(self, radius):
        area_c = 3.14 * (radius**2)
        print(area_c)

class Rectange:
    def area(self, length, breadth):
        area_r = length * breadth
        print(area_r)

class Triangle:
    def area(self, base, height):
        area_t = 1/2 * (base * height)
        print(area_t)
    
circle1 = Circle()
circle1.area(5)

rectange1 = Rectange()
rectange1.area(5,4)

triangle1 = Triangle()
triangle1.area(10,20)