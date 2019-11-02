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

# default setting
state=State.OPEN
# price=30

# Pay Money
def coin():
	global state
	# global price
	# if price > 10:
	# 	price=price-10
	# 	state = State.OPEN
	# 	push()
	# else:
	# 	print("You not have money, Charge it!")
	if state == State.LOCKED:
		state = State.OPEN
	else:
		return

# Cross the road
def push():
	global state
	if state == State.LOCKED:
		print("You cannot cross from the road!")
		return
	else:
		print("You cross from the road.")
		state=State.LOCKED

coin()
coin()
coin()
coin()
coin()
coin()
push()
push()
push()
push()
