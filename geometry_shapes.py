# İntizar Güzelçay 
# Question5

class Rectangle :
    
    def __init__(self,long_side,short_edge):
        self.long_side = long_side
        self.short_edge = short_edge
        

    def rectangle_area(self):
        area = (self.long_side * self.short_edge) * 2
        return area

    def rectangle_perimeter(self):
        perimeter = 2*(self.long_side + self.short_edge)
        return perimeter
    

class Square :
     
    def __init__(self,side):
        self.side = side

    def square_area(self):
        area = self.side *self.side
        return area
    
    def square_perimeter(self):
        perimeter = self.side * 4
        return perimeter
    


class Triangle:

    def __init__(self,base_lenght,height,side1,side2):
        self.base_lenght = base_lenght
        self.height = height
        self.side1 = side1
        self.side2 = side2
         

    def triangle_area(self):
        area = (self.base_lenght * self.height)  / 2
        return area

    def triangle_perimeter(self):
        perimeter = self.side1 + self.side2 + self.base_lenght
        return perimeter  