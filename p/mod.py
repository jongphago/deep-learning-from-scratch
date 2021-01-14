import inspect
import numpy as np

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
    
# chapter 4 - 신경망 학습
def mse(y, t):
    """
    mean_squared_error
    """
    return np.sum((y-t)**2) / 2

def _cee(y, t):
    delta = 1e-7
    arr = np.log(np.array(y) + delta)
    return -np.sum(arr * t)

def cee(y, t):
    """
    cross_entropy_error
    """
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    
    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size) ,t] + 1e-7)) / batch_size

def num_diff(f, x):
    """
    중심차분(중앙차분)
    """
    h = 1e-4
    return (f(x+h)-f(x-h)) / (2*h)

def num_grad(f, x):
    """
    numerical_gradient
    함수 f에 대해 점 x의 편미분값을 구하는 함수
    """
    grad = np.zeros_like(x)

    for idx in range(x.size):
        tmp_val = x[idx]

        #f(x+h) 계산
        x[idx] = tmp_val + h
        fxh1 = f(x)

        #f(x-h) 계산
        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val

    return grad

def grad_descent(f, init_x, lr=.01, step_num=100):
    """
    gradient_descent
    """
    x = init_x
    for _ in range(step_num):
        x -= lr * num_grad(f, x)
    return x

def step_function(x:list)->list:
    y = x > 0
    return y.astype(np.int)

def relu(x):
    return np.maximum(0, x)

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    exp_sum = np.sum(exp_a)
    y = exp_a / exp_sum
    if(y.sum().round() != 1):
        print("softmax function ERROR")
        return -99999999
    return y