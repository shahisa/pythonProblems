def airport(tickets):
	
	d = { }
	for t in tickets:
		d[t.origin] = t.destination #I have a key and value pair here. Find out he starting city. 
	c = { } # this dictionary is for cities. the first loop puts all the origins into it. The second loop removes destinations for the dictionary. at the end of the two loops i should have one city left. 
	for 	 