import inspect

def retrieve_name(var):
    """
    https://itbloger.tistory.com/1027
    Gets the name of var. Does it from the out most frame inner-wards.
    :param var: variable to get name from.
    :return: string
    """
    for fi in reversed(inspect.stack()):
        names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
        if len(names) > 0:
            return names[0]
        
def printn(_var):
    """
    변수의 이름과 변수의 값을 출력하는 함수
    """
    varName = retrieve_name(_var)
    print("{}: {}".format(varName, _var))
    
def printt(_var):
    """
    변수의 이름과 변수의 데이터 타입을 출력하는 함수
    """
    varName = retrieve_name(_var)
    print(f"type-{varName}:{type(_var)}")
    
def prints(_var):
    """
    변수의 이름과 변수의 데이터 타입을 출력하는 함수
    """
    varName = retrieve_name(_var)
    print(f"shape-{varName}:{_var.shape}")