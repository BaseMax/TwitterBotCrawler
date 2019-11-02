'''
@Copyright (c) 2019, Ryo Currency Project
@Author Max Base, Asrez Team
@Version 1.0
@Date 2019-11-02

Please see LICENSE for details
All rights reserved.
'''

state=False #default
def push():
	global state
	if state == False:
		state=True
	else:
		state=False

print(state)
push()
print(state)
push()
print(state)

