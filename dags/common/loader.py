from .helper import add

# Define the function to be executed by the task
def hello_world(n,a):
    import time
    time.sleep(int(a))
    print(add(n,9))

    return n
