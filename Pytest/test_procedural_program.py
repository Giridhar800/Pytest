import subprocess

output = subprocess.check_output('python tables.py')
output2 = output.decode()
output3 = output2.split("\n")

def test_first_line():
    output4  = output3[0].rstrip("\r")
    assert "5 X 1" in output4

def test_last_line():
    output5 = output3[9].rstrip("\r")
    assert output5 == "5 X 10 = 50"

def test_length():
    assert len(output3)-1 == 10

def test_type():
    assert type(output2).__name__ == "str"