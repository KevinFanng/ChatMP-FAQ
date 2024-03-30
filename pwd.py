from os import * 
from pwd import * 
def get_username():
	return getpwuid(getuid())[0]
