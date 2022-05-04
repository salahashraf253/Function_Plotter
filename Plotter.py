import matplotlib.pyplot as plt

class Plotter:
    def __init__(self):
        print("Hello in plotter class")
    def calcYCooridante(self, x, equation):
        x=x
        val = eval(equation)
        return val

    def calcCooridantes(self, minValue, maxValue, equation):
        x_Coor = []
        y_Coor = []
        for i in range(minValue, maxValue):
            x_Coor.append(i)
            y_Coor.append(self.calcYCooridante(i, equation))
        return x_Coor, y_Coor

    def plot(self, minValue, maxValue, equation,orginialEqu):
        x, y = self.calcCooridantes(minValue, maxValue, equation)

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
