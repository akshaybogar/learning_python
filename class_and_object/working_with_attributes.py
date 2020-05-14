class Colors():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # Called everytime when attributes are accessed
    def __getattr__(self, attr):
        if attr == 'rgbcolor':
            return(self.red, self.green, self.blue)
        else:
            raise AttributeError

if __name__ == '__main__':
    color = Colors()
    # Below statement will return a rgb tuple
    print(color.rgbcolor)
