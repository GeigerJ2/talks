from aiida_workgraph import task, WorkGraph
from aiida import load_profile

load_profile()

# define add task
@task.calcfunction()
def add(x, y):
    import time
    time.sleep(60)
    return x + y

# define multiply task
@task.calcfunction()
def multiply(x, y):
    return x * y

# create workgraph
wg = WorkGraph("multiply_add")

# add tasks to workgraph
multiply_task = wg.add_task(multiply, name="multiply")
add_task = wg.add_task(add, name="add")

# link multiply output to add input
wg.add_link(multiply_task.outputs["result"], add_task.inputs["x"])

# Submit the workgraph
inputs = {"multiply": {"x": 2, "y": 3}, "add": {"y": 4}}
wg.run(inputs=inputs)

