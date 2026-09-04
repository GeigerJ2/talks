from aiida import load_profile
from aiida.manage import get_manager


profile = load_profile("lms-gm")
manager = get_manager()
storage = manager.get_profile_storage()
container = storage.get_container()

# First hashkey via sqlitebrowser
file_content = container.get_object_content(
    hashkey="0e9fe1db41eedc6159fee33bbe927e37106dc9bc9f0fbcf79d653dfd4b1677a2"
)
print(file_content.decode("utf-8"))

# This maps to file:
# `.aiida/calcinfo.json`

# In the working directory of the corresponding `ArithmeticAddCalculation` of the first `MultiplyAddWorkChain`
# /home/geiger_j/aiida_projects/lms-gm/.aiida/scratch/lms-gm/51/fc/f84a-8455-4f3a-82db-e637143e0ca0

#
