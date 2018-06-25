import json
import sys
import os

fname = "test.json"
log = open("log.txt", "w")

class Test(object):
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
		print("Created:", a, file=log)
		print("Created:", b, file=log)
		print("Created:", c, "\n", file=log)

		self.data = {
		    "save":{
		        "a":a,
		        "b":b,
		        "c":c
		    }
		}

	def save(self):
		self.data["save"] = { # overwrite old save (or creates new save)
		    "a":self.a,
		    "b":self.b,
		    "c":self.c
		}

		with open(fname, "w") as f: # write save to file
			f.write(json.dumps(self.data, sort_keys=True, indent=4))
			print("Saved JSON!", file=log)

	def load(self):
		with open(fname, "r") as f: # open save file
			json_data = f.read() # get save file contents
			self.data = json.loads(json_data)
			self.json = json.dumps(json_data, sort_keys=True, indent=4)

			self.a, self.b, self.c = self.data["save"].values()

			print("Loaded JSON!\n", file=log)
			try:
				log.write("JSON: %s\n" % self.json) # check if json was successfully converted
				print("Params: {}, {}, {}\nData: ".format(self.a, self.b, self.c), end="", file=log) # check if parameters were saved & loaded
				print(*self.data["save"].values(), sep=", ", file=log) # check if data matches parameters
				print(file=log)
			except Exception as e:
				print(sys.exc_info(), file=log)

			del json_data # garbage collection
			del self.json

print("Run #1\n", file=log)
temp = Test(2,8,5)
temp.save()
temp.load()

print("\nRun #2\n", file=log)
temp.a, temp.b, temp.c = [temp.a*2,temp.b*2,temp.c*2]
temp.save()
temp.load()
log.close()
os.startfile(fname)
os.startfile("log.txt")
