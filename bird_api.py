from ebird.api import get_observations
from tokens import tokens


def get_bird_names():
	record = get_observations(tokens['api_key'], 'L227544', back=7)
	
	bird_list = []
	prev_name = ''

	for bird in record:
		name = ''
		
		try:
			name = bird['comName']
			
			try:
				name = name.split(' ')[-1]
			except:
				pass

			try:
				name = name.split('.')[-1]
			except:
				pass

			if name != prev_name and name:
				prev_name = name
				bird_list.append(name.lower())
		
		except:
			pass
	
	return bird_list
