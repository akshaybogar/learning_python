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

    def __setattr__(self, attr, val):
        if attr == 'rgbcolor':
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr, val)

if __name__ == '__main__':
    color = Colors()
    # Below statement will return a rgb tuple
    print(color.rgbcolor)

    #Below statement will set values using a tuple
    color.rgbcolor = (60, 70, 80)
    print(color.rgbcolor)
