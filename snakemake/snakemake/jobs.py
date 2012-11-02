# -*- coding: utf-8 -*-

__author__ = "Johannes Köster"

class Job:
	def __init__(self, rule, targetfile = None):
		self.rule = rule
		self.targetfile = targetfile
		
		self.input, self.output, self.log, self.wildcards = rule.expand_wildcards(self.targetfile)
		self.message = rule.message.format(input=self.input, 
		                                   output=self.output, 
		                                   wildcards=self.wildcards, 
		                                   threads=self.threads, 
		                                   log=self.log, 
		                                   **globals())
		
		self.dynamic_output, self.temp_output, self.protected_output = set(), set(), set()
		for i, f in self.output:
			f_ = self.rule.output[i]
			if f_ in self.rule.dynamic_output:
				self.dynamic_output.add(f)
			if f_ in self.rule.temp_output:
				self.temp_output.add(f)
			if f_ in self.rule.protected_output:
				self.protected_output.add(f)

	def __repr__(self):
		return self.rule.name
	
	@lru_cache()			
	def __eq__(self, other):
		return self.rule == other.rule and self.output == other.output
	
	@lru_cache()
	def __hash__(self):
		h = self.rule.__hash__()
		for o in self.output:
			h ^= o.__hash__()
		return h
