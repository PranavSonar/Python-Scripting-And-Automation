import gkeepapi, os

username = 'user'
password = 'your app password'

keep = gkeepapi.Keep()
success = keep.login(username,password)
dir_path = os.path.dirname(os.path.realpath(__file__))
for fn in os.listdir(dir_path):
	if os.path.isfile(fn) and fn.endswith('.txt'):
		with open(fn, 'r') as mf:
			data=mf.read()
			keep.createNote(fn.replace('.txt',''), data)
			keep.sync();

			