class TextMake:
    def __init__(self, font, text, color, screensize):
        self.text = text
        self.font = font
        self.color = color
        self.text_sprite = self.font.render(self.text, True, self.color)
        self.dimensions = self.font.size(text)
        self.screensize = screensize

    def set_position(self):
        text_width, text_height = self.dimensions
        x_centered = (self.screensize[0] / 2) - (text_width / 2)
        y_centered = (self.screensize[1] / 2) - (text_height / 2)
        position = (x_centered, y_centered)
        return position
