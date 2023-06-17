from employee import Employee

def test_give_default_raise():
    # given
    new_employee = Employee('nigel', 'jones', 35000)
    
    # when
    new_salary = new_employee.give_raise()
   
    # then
    assert new_salary == 40000
    
def test_give_custom_raise():
    # given
    new_employee = Employee('sydney', 'hapsburg', 50000)
    
    # when
    new_salary = new_employee.give_raise(2500)
    
    # then
    assert new_salary == 52500
