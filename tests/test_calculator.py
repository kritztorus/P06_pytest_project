from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_add_normal_2(self):
        # arrange
        a = 2
        b = 2
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 4
        assert result == expected

    def test_add_negative(self):
        # arrange
        a = -1
        b = -2
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = -3
        assert result == expected

    def test_subtract(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 3087
        assert result == expected

    def test_subtract_normal_2(self):
        # arrange
        a = 2
        b = 2
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 0
        assert result == expected
    
    def test_subtract_negative(self):
        # arrange
        a = -1
        b = -2
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 1
        assert result == expected

    def test_multiply(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 5339314
        assert result == expected
    
    def test_multiply_normal_2(self):
        # arrange
        a = 2
        b = 2
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 4
        assert result == expected
        
    def test_multiply_negative(self):
        # arrange
        a = -1
        b = -2
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 2
        assert result == expected

    def test_divide(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 3.5
        assert result == expected

    def test_divide_normal_2(self):
        # arrange
        a = 2
        b = 2
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 1
        assert result == expected
    
    def test_divide_negative(self):
        # arrange
        a = -1
        b = -2
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 0.5
        assert result == expected

    def test_divide_by_zero(self):
        # arrange
        a = 1
        b = 0
        cal = Calculator()

        # act
        try:
            result = cal.divide(a, b)
        except ZeroDivisionError as e:
            result = e

        # assert
        expected = "Division by zero error"
        assert str(result) == expected

# Run the test

    

    
