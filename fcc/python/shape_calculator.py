class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width*self.height
    
    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2)** .5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        output = ""
        for i in range(self.height):
            for i in range(self.width):
                output += "*"
            output += "\n"
            
        return output
    
    def get_amount_inside(self, shape):
        if shape.width > self.width or shape.height > self.height:
            return 0
        return int(self.get_area() / shape.get_area())
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side
        
    
    def set_side(self,side):
        self.side = side
        self.width = side
        self.height = side
    
    def set_width(self, width):
        self.side= width
    
    def set_height(self, height):
        self.side = height
    
    def __str__(self):
        return f"Square(side={self.side})"

        


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_width(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

