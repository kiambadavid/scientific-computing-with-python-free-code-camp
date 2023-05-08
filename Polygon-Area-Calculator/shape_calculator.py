class Rectangle:
    def __init__(self, width, height=None):
        self.width = width
        self.height = height
        if height is None:
            self.height = self.width

    def __str__(self):
        call = "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
        return call

    def set_width(self, new_width):
        self.width = new_width
        return self.width

    def set_height(self, new_height):
        self.height = new_height
        return self.height

    def get_area(self):
        area = self.height * self.width
        return area

    def get_perimeter(self):
        perimeter = (2 * self.height) + (2 * self.width)
        return perimeter

    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = ""
            for index in range(self.height):
                picture += "*" * self.width + "\n"
        return picture

    def get_amount_inside(self, shape):
        inside = (self.width * self.height) / (shape.width * shape.height)
        return int(inside)


class Square(Rectangle):

    def __str__(self):
        call = "Square(side=" + str(self.width) + ")"
        return call

    def set_side(self, side):
        self.width = side
        self.height = side
        