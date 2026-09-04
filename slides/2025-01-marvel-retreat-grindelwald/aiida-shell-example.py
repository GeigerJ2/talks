from aiida import load_profile
from aiida.orm import Int, load_computer
from aiida_shell import launch_shell_job
load_profile()

results, node = launch_shell_job(
    "expr",
    arguments=['{x}', "+", "{y}"],
    nodes={"x": Int(2), "y": Int(3)},
    metadata={
        "computer": load_computer("localhost")
    },
)

