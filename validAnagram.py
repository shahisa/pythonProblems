class Solution(object):
	def validAnagram(self,s,t):
		return collections.Counter(s) == collections.Counter(t)

