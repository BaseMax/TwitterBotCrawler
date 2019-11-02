'''
@Copyright (c) 2019, Ryo Currency Project
@Author Max Base, Asrez Team
@Version 1.0
@Date 2019-11-02

Please see LICENSE for details
All rights reserved.
'''

status=False #default
def push():
	global status
	if status == False:
		status=True
	else:
		status=False

print(status)
push()
print(status)

