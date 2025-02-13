# main.py
from task1 import kwargsAcceptFun
from task2 import typeBasedTransformer
from task3 import decorator_1

@decorator_1
def sample_function():
    print("Executing sample_function...")
    result = 0
    for i in range(1000000):
        result += i ** 2
    return result

if __name__ == "__main__":
    
    kwargs_result = kwargsAcceptFun(name="Aziza", age=21, is_student=True)
    print("Task 1 Result:", kwargs_result)

    
    transformed_result = typeBasedTransformer(
        number=4,
        text="Hello",
        flag=True,
        items=[1, 2, 3],
        data={"a": 1, "b": 2}
    )
    print("Task 2 Result:", transformed_result)

    
    sample_function()
