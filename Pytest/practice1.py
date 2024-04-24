import subprocess

output = subprocess.check_output('python tables.py')
output2 = output.decode()
output3 = output2.split('\n')
print(output3)