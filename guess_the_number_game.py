import random
import sys

sys.stdout.buffer.write(b"Input number minimum n.\n")
sys.stdout.flush()
n = sys.stdin.buffer.readline()

sys.stdout.buffer.write(b"Input number maximum m.\n")
sys.stdout.flush()
m = sys.stdin.buffer.readline()

n_int = int(n.decode())
m_int = int(m.decode())

if (n_int > m_int):
	sys.stdout.buffer.write(b"Your inputs n and m is wrong. Make sure that n is less than or equal to m.\n")
	sys.stdout.flush()
else:
	i = 0
	correct_value = random.randint(n_int, m_int)
	while (True):
		sys.stdout.buffer.write(b"Input prediceted value.\n")
		sys.stdout.flush()
		predicted_value = sys.stdin.buffer.readline()
		predicted_value_int = int(predicted_value.decode())
		if (correct_value == predicted_value_int):
			sys.stdout.buffer.write(b"Correct!\n")
			sys.stdout.flush()
			break
		else:
			sys.stdout.buffer.write(b"Wrong!\n")
			sys.stdout.flush()
