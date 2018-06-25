import json
import sys
import os

fname = "test.json"
log = open("log.txt", "w")
runs = 5

class Test(object):
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
		log.write("\nCreated: %d\nCreated: %d\nCreated: %d\n\n" % (a,b,c))

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
			log.write("Saved JSON!\n")

	def load(self):
		with open(fname, "r") as f: # open save file
			json_data = f.read() # get save file contents
			self.data = json.loads(json_data)
			self.json = json.dumps(json_data, sort_keys=True, indent=4).replace("\"{", "{").replace("}\"", "}").replace("\\n", "\n").replace("\\", "")

			self.a, self.b, self.c = self.data["save"].values()

			log.write("Loaded JSON!\n\n")
			try:
				log.write("JSON: %s\n" % self.json) # check if json was successfully converted
				log.write("Params: {}, {}, {}\nData: ".format(self.a, self.b, self.c)) # check if parameters were saved & loaded
				log.write("%d, %d, %d" % tuple(self.data["save"].values())) # check if data matches parameters
				log.write("\n")
			except Exception:
				error = sys.exc_info()
				log.write("%s: %s" % (error[0], error[1]))

			del json_data # garbage collection
			del self.json

for i in range(runs):
	log_str = "Run #%d\n\n" % i # save time + easier to write

	if i is 0: # can do this for low numbers (up to 8-bit numbers, max 255)
		log.write(log_str)
		temp = Test(2,8,5) # add values to save
		temp.save() # save data
		temp.load() # load data to check data saved
	else:
		log_str = "\n\n" + log_str

		log.write(log_str)
		temp.a, temp.b, temp.c = [x*10 for x in temp.data["save"].values()]
		temp.save()
		temp.load()

log.close()
os.startfile(fname)
os.startfile("log.txt")
