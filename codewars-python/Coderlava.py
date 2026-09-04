#!/bin/python3
"""
Author: Marvel Gulane { 
												https://github.com/coderlava, 
												https://github.com/interceptX,
												https://facebook.com/marvel.gulane
												https://reddit.com/interceptX
												https://github.com/maxanthonypablea
												https://codewars.com/maxanthonypablea
											}
"""
class Coderlava:
	def bacterias():
		gd_bacteria = '99.9%';
		bd_bacteria = '1%';
		bacterias = [gd_bacteria, bd_bacteria];
		return "Stat Bacterias: %s "%(bacterias);
	
	def wastes()		:
		green_color = False;
		brown_color = True;
		red_color = False;
		wastes = [green_color, brown_color, red_color];
		return "Stat Wastes : %s"%(wastes);
		
	def organs()		:
		heart = '91%';
		lungs = '91%';
		kidneys = '100%';
		eyes = '100%';
		liver = '80%';
		penis = '100%';
		testicles = '100%';
		brain = '100%';
		neck = 'nanobots conflict!';
		large_intestine = 'good';
		small_intestine = 'good';
		organs = [penis, testicles, lungs, liver, heart, eyes, brain, neck, large_intestine, small_intestine];
		return "Stat Organs : %s"%(organs);
	
	def bloods()		:
		redblood_cells = '80%';
		whiteblood_cells = '85%';
		bloods = [redblood_cells, whiteblood_cells];
		return "Stat Bloods : %s"%(bloods);
		
	def bones()		:
		nutrients = '100%';
		strength = '91%';
		osteoperosis = False;
		scoliosis = False;
		bones = [nutrients, strength, osteoperosis, scoliosis];
		return "Stat Bones :  %s"%(bones);
		
	def bodies()		:
		skin_color = 'brown';
		skin_top = 'brown';
		skin_midtop = 'brown';
		skin_middle = 'brown';
		skin_midbottom = 'brown';
		skin_bottom = 'brown';
		bodies =  [skin_color, skin_top, skin_midtop, skin_middle, skin_midbottom, skin_bottom];
		return "Stat Bodies : %s" %(bodies);
		
	def brains()		:
		neurons = '100%';
		subconscious = '99.9%';
		conscious = '94%';
		left_cortex = 'better-good';
		right_cortex = 'better-good';
		cortex_alignment = 'align';
		visual = '20/20';
		right_auditory_cortex = 'better-good';
		left_auditory_cortex = 'better-good';
		blood_cycle = 'good';
		muscle_memory = 'good';
		nutrients = '100%';
		brains = [neurons, subconscious, conscious, left_cortex, right_cortex, cortex_alignment, visual, right_auditory_cortex, left_auditory_cortex, blood_cycle, muscle_memory, nutrients];
		return "Stat Brains : %s" %(brains);
		
	def healths()	:
		heart_statistics = '58bps';
		lung_statistics = '98%';
		oxygen_levels = '100$';
		blood_levels = 'better-good';
		healths = [heart_statistics, lung_statistics, oxygen_levels, blood_levels];
		return "Stat Health : %s" %(healths);
	
class Foods:
	def chips():
		chipees = ['red','blue'];
		chocolates = True;
		breads = True;
		ramen = True;
		cornchips = True;
		beans = 'Hans Pork & Beans';
		porks = True;
		salads= ['pasta','vegetables'];
		cakes = True;
		foods = [cakes, ramen, breads, chipees, chocolates, cornchips, beans, porks, salads];
		return "Foods: %s"%(foods);
	
	def bldd():
		#breakfasts, lunchs, dinners & deserts
		rice = ['sticky rices', 'rice cakes'];
		chocolates = True;
		breads = True;
		ramen = True;
		cornchips = True;
		beans = 'Hans Pork & Beans';
		porks = True;
		salads= ['pasta','vegetables'];
		sweets = True;
		bldd = [rice, chocolates, breads, ramen, cornchips, beans, porks, salads, sweets];
		return "BLDD : %s"%(bldd);


class Waters:
	def drinks():
		sodas = ['cola', 'pepsi', 'tea',  'pepper'];
		chocolates = True;
		mineral = True;
		distilled = True;
		coffee = True;
		milk = True;
		waters = [sodas, chocolates, mineral, distilled, coffee, milk];
		return "Waters : %s"%(waters);

class Internets:
	def active_equipments():
		radios = True;
		computers = True;
		electricities = True;
		active_equipments = [radios, computers, electricities];
		return "Active Equipments: %s"%(active_equipments);

	def inactive_equipments():
		plastics = True;
		alloys = True;
		alluminums = True;
		bronzes = True;
		coppers = True;
		golds = True;
		silvers = True;
		carbons = True;
		metals  = True;
		rare_metals = True;
		inactive_equipments = [plastics, alloys, alluminums, bronzes, coppers, golds, silvers, carbons, metals, rare_metals];
		return "Inactive Equipments :%s"%(inactive_equipments);
		
class Communications:
	def verbal():
			communication_skills = True;
			offline_activities = True;
			online_activities = True;
			extras = True;
			verbal = [communication_skills, offline_activities, online_activities, extras];
			return "Verbal : %s"%(verbal);

	def non_verbal():
			actions = True;
			mimicing = True;
			synthetic_telepathies = True;
			telepathies = True;
			non_verbal = [actions, mimicing, synthetic_telepathies, telepathies];
			return "Non Verbal : %s"%(non_verbal);
			
class Securities:
	def digital_security():
		online = True;
		offline = True;
		sources = True;
		browsers = ['clearnet', 'darknet', 'darkweb'];
		frontends = True;
		backends = True;
		servers = True;
		ports = True;
		public_networks = True;
		private_networks = True;
		downloads = True;
		packets = True;
		digital_securities = [online, offline, sources, browsers, frontends, backends, servers, ports, public_networks, private_networks, downloads, packets];
		return "Digital Security : %s"%(digital_securities);

	def physical_security():
		karates = True;
		items = True;
		armors = True;
		clothes = True;
		bodies = True;
		dnas = True;
		foods = True;
		waters = True;
		electricities= True;
		physical_security = [karates, items, armors, clothes, bodies, dnas, foods, waters, electricities];
		return "Physical Security : %s"%(physical_security);
		
class Items:
	def devices():
		laptops = True;
		phones = True;
		ham_radios = True;
		chargers = True;
		securities = True;
		personal_computers = True;
		devices = [securities, laptops, phones, ham_radios, chargers, personal_computers];
		return "Items : %s"%(devices);
		
class Academics:
	def nursery():
		honors = True;
		certs = True;
		extras = True;
		nurseries = [honors, certs, extras];
		return "Nurseries : %s"%(nurseries);
	
	def kindergarten():
		honors = True;
		extras = True;
		activities = True;
		kindergartens = [honors, extras, activities];
		return "Kindergartens : %s"%(kindergartens); 

	def primary():
		honors = True;
		certs = True;
		extras = True;
		primaries = [honors, certs, extras];
		return "Primaries : %s"%(primaries);

	def secondary():
		honors = True;
		certs = True;
		extras = True;
		secondaries = [honors, certs, extras];
		return "Secondaries : %s"%(secondaries);

	def colleges():
		honors = True;
		private = True;
		certs = True;
		intrams = True;
		colleges = [honors, private, certs, intrams];
		return "Colleges : %s"%(colleges);
	
	def internships():
		online = True;
		offline = True;
		religion = True;
		conferences = True;
		internships = [online, offline, religion, conferences];
		return "Internships : %s"%(internships);

	def experiences():
		conferences = True;
		religion = True;
		seafare = True;
		coding = True;
		logistics = True;
		hiking = True;
		biking = True;
		poetry_writing = True;
		drawing = True;
		musics = ['piano', 'guitar', 'singing'];
		physical_activity = ['swimming', 'hiking', 'jogging', 'karate'];
		experiences = [drawing, conferences, religion, seafare, coding, logistics, hiking, biking, poetry_writing, musics, physical_activity];
		return "Experiences : %s"%(experiences);
		
class Environments:
	def rural():
		leyte_islands = True;
		iloilo_islands = True;
		pampanga_regions = True;
		sorsogon_regions = True;
		bicol_regions = True;
		rural = [leyte_islands, iloilo_islands, pampanga_regions, bicol_regions, sorsogon_regions];
		return "Rural : %s"%(rural);
		
	def urban():
		manila = True;
		cebu = True;
		pampanga = True;
		urban = [manila, cebu, pampanga];
		return "Urban : %s"%(urban); 

class Spiritual:
	def religion():
		baptists = True;
		protestants = True;
		roman_catholics = True;
		born_agains = True;
		mcgi = True;
		no_religions = True;
		religion = [baptists, protestants, roman_catholics, born_agains, mcgi, no_religions];
		return "Religion : %s"%(religion);

class Cleaners:
	def filters():
		waters =  True;
		foods = True;
		snacks = True;
		internet_packets = True;
		filters = [waters, foods, snacks, internet_packets];
		return "Filters : %s"%(filters);
	
	def cleaning():
		organs = True;
		blood = True;
		dirts = False;
		cleaning = [organs, blood, dirts];
		return "Cleaning : %s"%(cleaning);
	
	def healing():
		organs = True;
		bloods = True;
		bones = True;
		bodies = True;
		healing = [organs, bloods, bones, bodies];
		return "Healing : %s "%(healing);

class Main:
	def main():
		m = '∫10 ∫101 π2 dxdy = 1 − xy 6';
		coderlava_results = Coderlava;
		academics_results = Academics;
		communications_results = Communications;
		environments_results = Environments;
		foods_results = Foods;
		waters_results = Waters;
		internets_results = Internets;
		items_results = Items;
		securities_results = Securities;
		spirituals_results = Spiritual;
		cleaners_results = Cleaners;
		
		coderlava_values = [coderlava_results.wastes(), coderlava_results.organs(), coderlava_results.bloods(), coderlava_results.bones(), coderlava_results.bodies(), coderlava_results.brains(), coderlava_results.healths()];
		academics_values = [academics_results.nursery(), academics_results.kindergarten(), academics_results.primary(), academics_results.secondary(), academics_results.colleges(), academics_results.internships(), academics_results.experiences()];
		communications_values = [communications_results.verbal(), communications_results.non_verbal()];
		environments_values = [environments_results.rural(), environments_results.urban()];
		foods_values = [foods_results.chips(), foods_results.bldd()];
		waters_values = [waters_results.drinks()];
		internets_values = [internets_results.active_equipments(), internets_results.inactive_equipments()];
		items_values = [items_results.devices()];
		securities_values = [securities_results.digital_security(), securities_results.physical_security()];
		spirituals_values = [spirituals_results.religion()];
		cleaners_values = [cleaners_results.cleaning(), cleaners_results.filters(), cleaners_results.healing()];
		
		values = [coderlava_values, academics_values, communications_values, environments_values, foods_values, waters_values, internets_values, items_values, securities_values, spirituals_values, cleaners_values];
		return "%s\n%s"%(m, values);
		#for data_values in main_result.main(): print(data_values);

data = Main;
print(data.main());
