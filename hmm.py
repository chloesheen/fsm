#############################################################################################
# Chloe Sheen
# HMM
# Resources: lecture slides, geeksforgeeks.org
#############################################################################################
from itertools import product as nPk
from numpy import product

class HMM:
	"""
	get_state_sequence_prob: takes a sequence of hidden states and returns the probability of that sequence.
	Note: My get_state_sequence_prob takes observation probabilities into account also, so that my viterbi
	function would not be as complex.
	"""
	def get_state_sequence_prob(self, trans_p, obs_p, obs, states, states_dict):
		prob_list = []
		for i, state in enumerate(states):
			curr_state_idx = states_dict[state]
			if i == len(states)-1: break
			else :
				next_state_idx = (states_dict[states[i+1]])-1
				temp_trans_p = trans_p[curr_state_idx][next_state_idx]
				temp_obs_p = obs_p[next_state_idx][obs[i]-1]
				prob = temp_trans_p *  temp_obs_p
				prob_list.append(prob)

		answer = product(prob_list)
		return answer

	"""
	uniq: rids of duplicates, will be used in weeding out permutations in Viterbi
	"""
	def uniq (self, l):
		rtr = []
		for i in l:
			if not i in rtr:
				rtr.append(i)
		return rtr

	"""
	Viterbi: takes a sequence of observations; determines the path through the hidden states
	with the highest probability and returns that path.
	"""
	def viterbi(self, trans_p, obs_p, obs, states, states_dict):
		# for every perm of state excluding 'start'
		perms = [['start']+list(i) for i in list(nPk(states[1:], repeat=len(obs)))]
		probs = [self.get_state_sequence_prob(trans_p, obs_p, obs, perm, states_dict) for perm in self.uniq(perms)]
		return perms[probs.index(max(probs))], max(probs)

def demo():
	# demo of the ice cream HMM from class
	hmm = HMM()

	my_trans_p = [
		[0.8, 0.2], # start -> hot/cold
		[0.7, 0.3], # hot   -> hot/cold
		[0.4, 0.6]  # cold  -> hot/cold
	]
	my_obs_p = [
		[0.2, 0.4, 0.4], # Hot
		[0.5, 0.4, 0.1]  # Cold
	]

	my_obs = [1, 2, 3]  # as you add to this obs list, my_states will be incremented as a pair
	my_states = ['start', 'hot', 'cold']
	my_states_dict = {'start':0, 'hot':1, 'cold':2}

	# demo get_state_sequence_prob
	print "The probability of " + str(my_states) + " is " + str(hmm.get_state_sequence_prob(my_trans_p, my_obs_p, my_obs, my_states, my_states_dict))
	# demo viterbi
	print "The sequence with the highest probability is: " + str(hmm.viterbi(my_trans_p, my_obs_p, my_obs, my_states, my_states_dict)[0])
	# demo prob in viterbi
	print "Its probability is: " + str(hmm.viterbi(my_trans_p, my_obs_p, my_obs, my_states, my_states_dict)[1])

if __name__ == '__main__':
	demo()
