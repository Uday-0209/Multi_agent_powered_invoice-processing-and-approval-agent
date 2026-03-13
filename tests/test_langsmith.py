from langsmith import traceable


@traceable
def test_function():
    print("hello")


test_function()