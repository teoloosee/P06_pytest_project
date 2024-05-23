import pytest
from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()
    
        #act
        result= cal.add(a,b)

        #assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
         # Arrange
        a = 4321
        b = 1234
        cal = Calculator()
    
        # Act
        result= cal.subtract(a,b)

        # Assert
        expected = 3087
        assert result == expected

    def test_multiply(self):
         # arrange
        a = 4321
        b = 1234
        cal = Calculator()
    
        # act
        result= cal.multiply(a,b)

        # assert
        expected = 5332114
        assert result == expected

    def test_divide(self):
        # Arrange
        a = 10
        b = 2
        cal = Calculator()
    
        # Act
        result= cal.divide(a,b)

        # Assert
        expected = 5
        assert result == expected

    def test_divide_by_zero(self):
        # Arrange
        a = 4321
        b = 0
        cal = Calculator()
    
        # Act & Assert
        with pytest.raises(ZeroDivisionError): 
            cal.divide(a,b)