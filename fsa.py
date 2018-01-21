#############################################################################################
# Chloe Sheen
# FSA object class
# Resources: python.org for help because I'm not familiar with the language and stackoverflow
# for specific questions.
#############################################################################################
from string import lowercase

class Acceptor:
	def __init__ (self, final=1):
		self.state = 0
		self.final = final
		self.transition = {}

	# adds transition specifying start, end, and string if "accepting" passes
	# initially .extend, using .append now: https://stackoverflow.com/questions/2022031/
	# python-append-vs-operator-on-lists-why-do-these-give-different-results
	def addTransition(self, startState, endState, alpha):
		if alpha in lowercase:
			self.transition[(startState, alpha)] = endState
			return True
		return False

	def getTransition(self, alpha, state):
		if (state, alpha) in self.transition:
			return self.transition[(state, alpha)]
		else:
			return False

	# sets the final state
	def setFinal(self, state):
		if state is not self.final: self.final = state

	# runs the string through the FSA
	def execute(self, string):
		for c in string:
			transition = self.getTransition(c, self.state)
			if not transition is False:
				self.state = transition
			else:
				print "Input string '" + str(string) + "' is not accepted."
				return False

		if self.state == self.final:
			print "Input string '" + str(string) + "' is accepted."
			return True
		else:
			print "Input string '" + str(string) + "' is not accepted."
			return False

	# demo of my program, my string needs to have at least one 'a'
	def demo(self):
		# initialize
		for i in ["c", "abab", "bbbbbb", "aaa", "ab", "bab", "baa", "A", "a1", "!a", "ab?!"]:
			fsa = Acceptor()
			fsa.setFinal(1)
			fsa.addTransition(0,1, "a")
			fsa.addTransition(0,0, "b")
			fsa.addTransition(1,1, "a")
			fsa.addTransition(1,1, "b")

			fsa.execute(i)

# Python doesn't have "Main"?: http://python.berkeley.edu/events/assets/newbie_nugget_Oct2_2013.html
if __name__ == '__main__':
	acc = Acceptor()
	acc.demo()
