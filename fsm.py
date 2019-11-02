'''
@Copyright (c) 2019, Ryo Currency Project
@Author Max Base, Asrez Team
@Version 1.0
@Date 2019-11-02

Please see LICENSE for details
All rights reserved.
'''

import enum

class State(enum.Enum):
	OPEN = 0
	LOCKED = 1

state=State.OPEN # default

def coin():
	return

def push():
	global state
	if state == State.LOCKED:
		state=State.OPEN
	else:
		state=State.LOCKED

print(state)
push()
print(state)
push()
print(state)
push()
print(state)
