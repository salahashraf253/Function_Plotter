import matplotlib.pyplot as plt


class Plotter:
    def __init__(self):
        print("gd")

    def FuncSubstitute(self, x, equation):
        x=x
        val = eval(equation)  # built in function to substitute easily
        return val

    def GenerateFunc(self, minValue, maxValue,equation):
        x_Coor = []
        y_Coor = []
        for i in range(minValue, maxValue):
            x_Coor.append(i)
            y_Coor.append(self.FuncSubstitute(i,equation))
        return x_Coor, y_Coor

    def plot(self, minValue, maxValue, equation,orginialEqu):
        x, y = self.GenerateFunc(minValue, maxValue,equation)

        # plotting the points
        plt.plot(x, y)

        # naming the x axis
        plt.xlabel('x - axis')
        # naming the y axis
        plt.ylabel('y - axis')

        # giving a title to my graph
        plt.title(orginialEqu)

        # function to show the plot
        plt.show()
