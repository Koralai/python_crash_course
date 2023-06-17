from employee import Employee
import pytest

# given
@pytest.fixture
def new_employee():
    """An employee that will be available for all tests"""
    employee = Employee('cassandra', 'klegg', 62500)
    return employee

def test_give_default_raise(new_employee):
    """Test that a default raise is indeed $5,000"""
    
    # when
    new_salary = new_employee.give_raise()
   
    # then
    assert new_salary == 67500
    
def test_give_custom_raise(new_employee):
    """Test that a custom raise is stored correctly"""
      
    # when
    new_salary = new_employee.give_raise(2500)
    
    # then
    assert new_salary == 65000
