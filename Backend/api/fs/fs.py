def get_profiles() : 
	data = None 
	with open('../../profile/profiles.json') as f : 
		data = json.load(f) 
	return data

def get_critere(nom_critere) :
	data = None
	with open('../../data/database/'+nom_critere+'_psd.json') as f:
		data = json.load(f)
	return data
