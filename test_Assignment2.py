from ast import Pass
import pytest
from Assignment2 import*

#function 1 Test

@pytest.mark.parametrize("weight", [125, 34, 67, "cat", 43])
def test_convertWeight(weight):
    value1 = weight * 0.45
    assert weight * 0.45 == value1

#function 2 Test

@pytest.mark.parametrize("height", [190.5, "dog" , 182.88, 213.36, "bird"])
def test_convertHeight(height):
    value2 = height * 0.45
    assert height * 0.45 == value2
    

#function 3 Test

@pytest.mark.parametrize("value2", [1.524, "elephant" , 1.8288, 1.6002, "lion"])
def test_squareHeight(value2):
    value3 = value2 * value2
    assert value3 == value2 * value2

#function 4 Test


@pytest.mark.parametrize("value1, value3", [(105.3, 2.56) , (130, 1.6002), ("lion", "elephant"), (90, 1.0)])
def test_divideFinal(value1, value3):
    value4 = value1 / value3
    assert value1 == value4 * value3

    #function 5 BMI Boundary shift testing



#underweight upper bound nx1
def test_finalResult_under_off():
     assert finalResult(18.6) != "under"

def test_finalResult_under_on():
     assert finalResult(18.5) != "under"

def test_finalResult_under_onon():
     assert finalResult(18.4) == "under"

#normal weight lower boundary shift of 0.1
def test_finalResult_norm_off():
     assert finalResult(18.5) != "normal"

def test_finalResult_norm_on():
     assert finalResult(18.6) == "normal"

def test_finalResult_norm_onon():
     assert finalResult(18.7) == "normal"

#normal weight upper nx1
def test_finalResult_norm_off():
     assert finalResult(25) != "normal"

def test_finalResult_norm_on():
     assert finalResult(24.9) == "normal"

def test_finalResult_norm_onon():
     assert finalResult(24.8) == "normal"

#over weight lower bound
def test_finalResult_over_off():
     assert finalResult(24.9) != "over"

def test_finalResult_over_on():
     assert finalResult(25) == "over"

def test_finalResult_over_onon():
     assert finalResult(25.1) == "over"

#over weight upper bound
def test_finalResult_over_off():
     assert finalResult(30) != "over"

def test_finalResult_over_on():
     assert finalResult(29.9) == "over"

def test_finalResult_over_onon():
     assert finalResult(29.8) == "over"


#OBESE lower
def test_finalResult_obese_off():
     assert finalResult(29.9) != "obese"

def test_finalResult_obese_on():
     assert finalResult(30) == "obese"

def test_finalResult_obese_onon():
     assert finalResult(30.1) == "obese"