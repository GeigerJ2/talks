
from aiida_workgraph import task

# define add task
@task
def add(x, y):
    return x + y

# define multiply task
@task
def multiply(x, y):
    return x * y

# Build the graph task
@task.graph
def AddMultiply(x, y, z):
    the_sum = add(x=x, y=y).result
    return multiply(x=the_sum, y=z).result

# Concretize and run workflow
wg = AddMultiply.build_graph(x=2, y=3, z=4)
wg.run()

