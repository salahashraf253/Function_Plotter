import unittest

import self as self

import MainWindow
import Plotter


class MyTestCase(unittest.TestCase):
    def test_validateEquation(self):
        try:
            result = MainWindow.Ui_MainWindow.validateEquation(self,"x^,qn.")
            assert  result == "Invalid Function" , "should be Invalid Function"

            result = MainWindow.Ui_MainWindow.validateEquation(self,"x+fsdd2")
            assert  result == "Invalid Function" , "should be Invalid Function"

            result=MainWindow.Ui_MainWindow.validateEquation(self,"x+2")
            assert result=="x+2","Should be x+2"

            result=MainWindow.Ui_MainWindow.validateEquation(self,"")
            assert result == "The Functon Field is Empty, Please Enter it" , "should be not empty"
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            print('Passed invalid func')

    def test_validate_range(self):
        result = MainWindow.Ui_MainWindow.isValidRange(self, 10,100)
        assert result==True, "should be true"

        result = MainWindow.Ui_MainWindow.isValidRange(self, 100,10)
        assert result==False, "should be false"

    def test_validate_numbers(self):
        result = MainWindow.Ui_MainWindow.validateNumbers(self, "fd")
        assert result==False

        result = MainWindow.Ui_MainWindow.validateNumbers(self, "23432")
        assert result==True

    def test_calcYCooridante(self):
        result=Plotter.Plotter.calcYCooridante(self,1,"x+2")
        assert result==3
        result=Plotter.Plotter.calcYCooridante(self,10,"x-7")
        assert result==3
        result=Plotter.Plotter.calcYCooridante(self,10,"x/2")
        assert result==5
if __name__ == '__main__':
    unittest.main()
