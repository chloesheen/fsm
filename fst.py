#############################################################################################
# Chloe Sheen
# FST object class
# Resources: python.org for help because I'm not familiar with the language and stackoverflow
# for specific questions.
#############################################################################################
from string import lowercase

class Transducer:
	def __init__ (self, final=1):
		self.state = 0
		self.final = final
		self.transition = {}
		self.output = ""		# this time, we need to keep track of the output string

	# adds transition specifying start, end, and string if "accepting" passes
	# initially .extend, using .append now: https://stackoverflow.com/questions/2022031/
	# python-append-vs-operator-on-lists-why-do-these-give-different-results
	def addTransition(self, startState, endState, alpha, alphaOutput):
		if alpha in lowercase:
			self.transition[(startState, alpha)] = [endState, alphaOutput]  # keeping track of output string
			return True
		return False

	def getTransition(self, alpha, state):
		if (state, alpha) in self.transition:
			return self.transition[(state, alpha)]
		else:
			return [False, ""]   	# because it will be unpacked into 2

	# sets the final state
	def setFinal(self, state):
		if state is not self.final: self.final = state

	# runs the string through the FST
	def execute(self, string):
		if not isinstance(string, str):
			# str is not string
			print "Not a string."
			return False

		for c in string:
			transition, tempOutput = self.getTransition(c, self.state)		# unpack
			if not transition is False:
				self.state = transition
				self.output += tempOutput	# add temp output to output
			else:
				print "Input string '" + str(string) + "' is not accepted."
				return False

		if self.state == self.final:
			print "%s outputs %s" % (string, self.output)
			return True
		else:
			print "%s outputs %s" % (string, self.output)
			return False

	# demo of my program, returns the string you gave it except when it sees the first 'a', outputs 'b'
	def demo(self):
		# initialize
		for i in ["c", "abab", "bbbbbb", "aaa", "abaab", "bababa", "baa", "A", "a1", "!a", "ab?!"]:
			fst = Transducer()
			fst.setFinal(1)
			fst.addTransition(0,1, "a", "b")
			fst.addTransition(0,0, "b", "b")
			fst.addTransition(1,1, "a", "a")
			fst.addTransition(1,1, "b", "b")

			fst.execute(i)

# Python doesn't have "Main"?: http://python.berkeley.edu/events/assets/newbie_nugget_Oct2_2013.html
if __name__ == '__main__':
	acc = Transducer()
	acc.demo()
