# from ass import db, Crop

crops = { 	
			'plum':
					{
					'_name':'plum',
					'_variety':'tomato',
				 	'_family':'fruit',
					'_yield':2.8, # kg
					'_space_x':0.3, # m
					'_space_y':0.3, # m
					'_space_z':1.1, # m
					'_density':11.11, # plants/m2
					'_fruit_quantity':26,
					'_fruit_size':0.076, # m
					'_fruit_weight':0.062, # kg
					'_water':1, # l/day
					'_nutrient':18, # mSiemens
					'_radiation':12, # h/day
					'_dtg':12, # day
					'_dtm':180, # day
					'_soil_ph_min':6, 		'_soil_ph_opt':6.5, 		'_soil_ph_max':6.8,			# pH
					'_soil_temp_min':15,	'_soil_temp_opt':23,		'_soil_temp_max':30, 		# ºC
					'_soil_humi_min':50,	'_soil_humi_opt':60,		'_soil_humi_max':75, 		# %RH
					'_soil_nutrient_min':2,	'_soil_nutrient_opt':16,	'_soil_nutrient_max':40,	# mSiemens
					'_air_temp_min':17,		'_air_temp_opt':25,			'_air_temp_max':28, 		# ºC
					'_air_humi_min':60,		'_air_humi_opt':63,			'_air_humi_max':70,			# %RH
					},
			'romaine': 
					{
					'_name':'romaine',
					'_variety':'lettuce',
				 	'_family':'leafy',
					'_yield':0.626,
					'_space_x':0.2,
					'_space_y':0.2,
					'_space_z':0.35,
					'_density':25,
					'_fruit_quantity':1,
					'_fruit_size':0.35,
					'_fruit_weight':0.626,
					'_water':0.8,
					'_nutrient':0.8,
					'_radiation':11,
					'_dtg':10,
					'_dtm':70,
					'_soil_ph_min':6, 		'_soil_ph_opt':6.2, 	'_soil_ph_max':6.8,
					'_soil_temp_min':0,		'_soil_temp_opt':0,		'_soil_temp_max':0,
					'_soil_humi_min':40,	'_soil_humi_opt':45,	'_soil_humi_max':60,
					'_soil_nutrient_min':0,	'_soil_nutrient_opt':0,	'_soil_nutrient_max':0,
					'_air_temp_min':10,		'_air_temp_opt':16,		'_air_temp_max':19,
					'_air_humi_min':60,		'_air_humi_opt':65,		'_air_humi_max':70,
					},
			'arugula':
					{
					'_name':'arugula',
					'_variety':'herb',
				 	'_family':'leafy',
					'_yield':0.000671,
					'_space_x':0.0204,
					'_space_y':0.0204,
					'_space_z':30,
					'_density':2402.92,
					'_fruit_quantity':1,
					'_fruit_size':25,
					'_fruit_weight':0.000671,
					'_water':0.5,
					'_nutrient':0.5,
					'_radiation':10,
					'_dtg':6,
					'_dtm':47,
					'_soil_ph_min':6, 		'_soil_ph_opt':6.3, 	'_soil_ph_max':6.8,
					'_soil_temp_min':0,		'_soil_temp_opt':0,		'_soil_temp_max':0,
					'_soil_humi_min':0,		'_soil_humi_opt':0,		'_soil_humi_max':0,
					'_soil_nutrient_min':0,	'_soil_nutrient_opt':0,	'_soil_nutrient_max':0,
					'_air_temp_min':10,		'_air_temp_opt':18,		'_air_temp_max':26,
					'_air_humi_min':0,		'_air_humi_opt':0,		'_air_humi_max':0,
					}, 
			'radicchio':
					{
					'_name':'radicchio',
					'_variety':'unknow',
				 	'_family':'leafy',
					'_yield':0,
					'_space_x':0,
					'_space_y':0,
					'_space_z':0,
					'_density':0,
					'_fruit_quantity':0,
					'_fruit_size':0,
					'_fruit_weight':0,
					'_water':0,
					'_nutrient':0,
					'_radiation':0,
					'_dtg':0,
					'_dtm':0,
					'_soil_ph_min':0, 		'_soil_ph_opt':0, 		'_soil_ph_max':0,
					'_soil_temp_min':0,		'_soil_temp_opt':0,		'_soil_temp_max':0,
					'_soil_humi_min':0,		'_soil_humi_opt':0,		'_soil_humi_max':0,
					'_soil_nutrient_min':0,	'_soil_nutrient_opt':0,	'_soil_nutrient_max':0,
					'_air_temp_min':0,		'_air_temp_opt':0,		'_air_temp_max':0,
					'_air_humi_min':0,		'_air_humi_opt':0,		'_air_humi_max':0,
					},
			'bell pepper':
					{
					'_name':'bell pepper',
					'_variety':'something',
				 	'_family':'something',
					'_yield':0,
					'_space_x':0,
					'_space_y':0,
					'_space_z':0,
					'_density':0,
					'_fruit_quantity':0,
					'_fruit_size':0,
					'_fruit_weight':0,
					'_water':0,
					'_nutrient':0,
					'_radiation':0,
					'_dtg':0,
					'_dtm':0,
					'_soil_ph_min':0, 		'_soil_ph_opt':0, 		'_soil_ph_max':0,
					'_soil_temp_min':0,		'_soil_temp_opt':0,		'_soil_temp_max':0,
					'_soil_humi_min':0,		'_soil_humi_opt':0,		'_soil_humi_max':0,
					'_soil_nutrient_min':0,	'_soil_nutrient_opt':0,	'_soil_nutrient_max':0,
					'_air_temp_min':0,		'_air_temp_opt':0,		'_air_temp_max':0,
					'_air_humi_min':0,		'_air_humi_opt':0,		'_air_humi_max':0,
					},
			'cabbage':
					{
					'_name':'cabbage',
					'_variety':'something',
				 	'_family':'something',
					'_yield':0,
					'_space_x':0,
					'_space_y':0,
					'_space_z':0,
					'_density':0,
					'_fruit_quantity':0,
					'_fruit_size':0,
					'_fruit_weight':0,
					'_water':0,
					'_nutrient':0,
					'_radiation':0,
					'_dtg':0,
					'_dtm':0,
					'_soil_ph_min':0, 		'_soil_ph_opt':0, 		'_soil_ph_max':0,
					'_soil_temp_min':0,		'_soil_temp_opt':0,		'_soil_temp_max':0,
					'_soil_humi_min':0,		'_soil_humi_opt':0,		'_soil_humi_max':0,
					'_soil_nutrient_min':0,	'_soil_nutrient_opt':0,	'_soil_nutrient_max':0,
					'_air_temp_min':0,		'_air_temp_opt':0,		'_air_temp_max':0,
					'_air_humi_min':0,		'_air_humi_opt':0,		'_air_humi_max':0,
					},
			'coriander':
					{
					'_name':'coriander',
					'_variety':'something',
				 	'_family':'something',
					'_yield':0,
					'_space_x':0,
					'_space_y':0,
					'_space_z':0,
					'_density':0,
					'_fruit_quantity':0,
					'_fruit_size':0,
					'_fruit_weight':0,
					'_water':0,
					'_nutrient':0,
					'_radiation':0,
					'_dtg':0,
					'_dtm':0,
					'_soil_ph_min':0, 		'_soil_ph_opt':0, 		'_soil_ph_max':0,
					'_soil_temp_min':0,		'_soil_temp_opt':0,		'_soil_temp_max':0,
					'_soil_humi_min':0,		'_soil_humi_opt':0,		'_soil_humi_max':0,
					'_soil_nutrient_min':0,	'_soil_nutrient_opt':0,	'_soil_nutrient_max':0,
					'_air_temp_min':0,		'_air_temp_opt':0,		'_air_temp_max':0,
					'_air_humi_min':0,		'_air_humi_opt':0,		'_air_humi_max':0,
					},
			'basil':
					{
					'_name':'basil',
					'_variety':'something',
				 	'_family':'something',
					'_yield':0,
					'_space_x':0,
					'_space_y':0,
					'_space_z':0,
					'_density':0,
					'_fruit_quantity':0,
					'_fruit_size':0,
					'_fruit_weight':0,
					'_water':0,
					'_nutrient':0,
					'_radiation':0,
					'_dtg':0,
					'_dtm':0,
					'_soil_ph_min':0, 		'_soil_ph_opt':0, 		'_soil_ph_max':0,
					'_soil_temp_min':0,		'_soil_temp_opt':0,		'_soil_temp_max':0,
					'_soil_humi_min':0,		'_soil_humi_opt':0,		'_soil_humi_max':0,
					'_soil_nutrient_min':0,	'_soil_nutrient_opt':0,	'_soil_nutrient_max':0,
					'_air_temp_min':0,		'_air_temp_opt':0,		'_air_temp_max':0,
					'_air_humi_min':0,		'_air_humi_opt':0,		'_air_humi_max':0,
					},
			'squash':
					{
					'_name':'squash',
					'_variety':'something',
				 	'_family':'something',
					'_yield':0,
					'_space_x':0,
					'_space_y':0,
					'_space_z':0,
					'_density':0,
					'_fruit_quantity':0,
					'_fruit_size':0,
					'_fruit_weight':0,
					'_water':0,
					'_nutrient':0,
					'_radiation':0,
					'_dtg':0,
					'_dtm':0,
					'_soil_ph_min':0, 		'_soil_ph_opt':0, 		'_soil_ph_max':0,
					'_soil_temp_min':0,		'_soil_temp_opt':0,		'_soil_temp_max':0,
					'_soil_humi_min':0,		'_soil_humi_opt':0,		'_soil_humi_max':0,
					'_soil_nutrient_min':0,	'_soil_nutrient_opt':0,	'_soil_nutrient_max':0,
					'_air_temp_min':0,		'_air_temp_opt':0,		'_air_temp_max':0,
					'_air_humi_min':0,		'_air_humi_opt':0,		'_air_humi_max':0,
					},
			'chive':
					{
					'_name':'chive',
					'_variety':'something',
				 	'_family':'something',
					'_yield':0,
					'_space_x':0,
					'_space_y':0,
					'_space_z':0,
					'_density':0,
					'_fruit_quantity':0,
					'_fruit_size':0,
					'_fruit_weight':0,
					'_water':0,
					'_nutrient':0,
					'_radiation':0,
					'_dtg':0,
					'_dtm':0,
					'_soil_ph_min':0, 		'_soil_ph_opt':0, 		'_soil_ph_max':0,
					'_soil_temp_min':0,		'_soil_temp_opt':0,		'_soil_temp_max':0,
					'_soil_humi_min':0,		'_soil_humi_opt':0,		'_soil_humi_max':0,
					'_soil_nutrient_min':0,	'_soil_nutrient_opt':0,	'_soil_nutrient_max':0,
					'_air_temp_min':0,		'_air_temp_opt':0,		'_air_temp_max':0,
					'_air_humi_min':0,		'_air_humi_opt':0,		'_air_humi_max':0,
					},
			'sweet_corn':
					{
					'_name':'sweet corn',
					'_variety':'something',
				 	'_family':'something',
					'_yield':0,
					'_space_x':0,
					'_space_y':0,
					'_space_z':0,
					'_density':0,
					'_fruit_quantity':0,
					'_fruit_size':0,
					'_fruit_weight':0,
					'_water':0,
					'_nutrient':0,
					'_radiation':0,
					'_dtg':0,
					'_dtm':0,
					'_soil_ph_min':0, 		'_soil_ph_opt':0, 		'_soil_ph_max':0,
					'_soil_temp_min':0,		'_soil_temp_opt':0,		'_soil_temp_max':0,
					'_soil_humi_min':0,		'_soil_humi_opt':0,		'_soil_humi_max':0,
					'_soil_nutrient_min':0,	'_soil_nutrient_opt':0,	'_soil_nutrient_max':0,
					'_air_temp_min':0,		'_air_temp_opt':0,		'_air_temp_max':0,
					'_air_humi_min':0,		'_air_humi_opt':0,		'_air_humi_max':0,
					},
			'black bean':
					{
					'_name':'black bean',
					'_variety':'something',
				 	'_family':'something',
					'_yield':0,
					'_space_x':0,
					'_space_y':0,
					'_space_z':0,
					'_density':0,
					'_fruit_quantity':0,
					'_fruit_size':0,
					'_fruit_weight':0,
					'_water':0,
					'_nutrient':0,
					'_radiation':0,
					'_dtg':0,
					'_dtm':0,
					'_soil_ph_min':0, 		'_soil_ph_opt':0, 		'_soil_ph_max':0,
					'_soil_temp_min':0,		'_soil_temp_opt':0,		'_soil_temp_max':0,
					'_soil_humi_min':0,		'_soil_humi_opt':0,		'_soil_humi_max':0,
					'_soil_nutrient_min':0,	'_soil_nutrient_opt':0,	'_soil_nutrient_max':0,
					'_air_temp_min':0,		'_air_temp_opt':0,		'_air_temp_max':0,
					'_air_humi_min':0,		'_air_humi_opt':0,		'_air_humi_max':0,
					},
			'strawberry':
					{
					'_name':'strawberry',
					'_variety':'something',
				 	'_family':'something',
					'_yield':0,
					'_space_x':0,
					'_space_y':0,
					'_space_z':0,
					'_density':0,
					'_fruit_quantity':0,
					'_fruit_size':0,
					'_fruit_weight':0,
					'_water':0,
					'_nutrient':0,
					'_radiation':0,
					'_dtg':0,
					'_dtm':0,
					'_soil_ph_min':0, 		'_soil_ph_opt':0, 		'_soil_ph_max':0,
					'_soil_temp_min':0,		'_soil_temp_opt':0,		'_soil_temp_max':0,
					'_soil_humi_min':0,		'_soil_humi_opt':0,		'_soil_humi_max':0,
					'_soil_nutrient_min':0,	'_soil_nutrient_opt':0,	'_soil_nutrient_max':0,
					'_air_temp_min':0,		'_air_temp_opt':0,		'_air_temp_max':0,
					'_air_humi_min':0,		'_air_humi_opt':0,		'_air_humi_max':0,
					},
			'plum2':
					{
					'_name':'plum2',
					'_variety':'something',
				 	'_family':'something',
					'_yield':0,
					'_space_x':0,
					'_space_y':0,
					'_space_z':0,
					'_density':0,
					'_fruit_quantity':0,
					'_fruit_size':0,
					'_fruit_weight':0,
					'_water':0,
					'_nutrient':0,
					'_radiation':0,
					'_dtg':0,
					'_dtm':0,
					'_soil_ph_min':0, 		'_soil_ph_opt':0, 		'_soil_ph_max':0,
					'_soil_temp_min':0,		'_soil_temp_opt':0,		'_soil_temp_max':0,
					'_soil_humi_min':0,		'_soil_humi_opt':0,		'_soil_humi_max':0,
					'_soil_nutrient_min':0,	'_soil_nutrient_opt':0,	'_soil_nutrient_max':0,
					'_air_temp_min':0,		'_air_temp_opt':0,		'_air_temp_max':0,
					'_air_humi_min':0,		'_air_humi_opt':0,		'_air_humi_max':0,
					},
			'rice':
					{
					'_name':'rice',
					'_variety':'something',
				 	'_family':'something',
					'_yield':0,
					'_space_x':0,
					'_space_y':0,
					'_space_z':0,
					'_density':0,
					'_fruit_quantity':0,
					'_fruit_size':0,
					'_fruit_weight':0,
					'_water':0,
					'_nutrient':0,
					'_radiation':0,
					'_dtg':0,
					'_dtm':0,
					'_soil_ph_min':0, 		'_soil_ph_opt':0, 		'_soil_ph_max':0,
					'_soil_temp_min':0,		'_soil_temp_opt':0,		'_soil_temp_max':0,
					'_soil_humi_min':0,		'_soil_humi_opt':0,		'_soil_humi_max':0,
					'_soil_nutrient_min':0,	'_soil_nutrient_opt':0,	'_soil_nutrient_max':0,
					'_air_temp_min':0,		'_air_temp_opt':0,		'_air_temp_max':0,
					'_air_humi_min':0,		'_air_humi_opt':0,		'_air_humi_max':0,
					},
			'chilli':
					{
					'_name':'chilli',
					'_variety':'something',
				 	'_family':'something',
					'_yield':0,
					'_space_x':0,
					'_space_y':0,
					'_space_z':0,
					'_density':0,
					'_fruit_quantity':0,
					'_fruit_size':0,
					'_fruit_weight':0,
					'_water':0,
					'_nutrient':0,
					'_radiation':0,
					'_dtg':0,
					'_dtm':0,
					'_soil_ph_min':0, 		'_soil_ph_opt':0, 		'_soil_ph_max':0,
					'_soil_temp_min':0,		'_soil_temp_opt':0,		'_soil_temp_max':0,
					'_soil_humi_min':0,		'_soil_humi_opt':0,		'_soil_humi_max':0,
					'_soil_nutrient_min':0,	'_soil_nutrient_opt':0,	'_soil_nutrient_max':0,
					'_air_temp_min':0,		'_air_temp_opt':0,		'_air_temp_max':0,
					'_air_humi_min':0,		'_air_humi_opt':0,		'_air_humi_max':0,
					},
			'cottom':
					{
					'_name':'cottom',
					'_variety':'something',
				 	'_family':'something',
					'_yield':0,
					'_space_x':0,
					'_space_y':0,
					'_space_z':0,
					'_density':0,
					'_fruit_quantity':0,
					'_fruit_size':0,
					'_fruit_weight':0,
					'_water':0,
					'_nutrient':0,
					'_radiation':0,
					'_dtg':0,
					'_dtm':0,
					'_soil_ph_min':0, 		'_soil_ph_opt':0, 		'_soil_ph_max':0,
					'_soil_temp_min':0,		'_soil_temp_opt':0,		'_soil_temp_max':0,
					'_soil_humi_min':0,		'_soil_humi_opt':0,		'_soil_humi_max':0,
					'_soil_nutrient_min':0,	'_soil_nutrient_opt':0,	'_soil_nutrient_max':0,
					'_air_temp_min':0,		'_air_temp_opt':0,		'_air_temp_max':0,
					'_air_humi_min':0,		'_air_humi_opt':0,		'_air_humi_max':0,
					},
		}

def add_crops(crops):
	for crop in crops:
		print (crop)

add_crops()
# def calc_density(crop):
# 	density = (crops[crop]['space_x']) * (crops[crop]['space_y'])
# 	return density

# def add_crop(*args, **kwargs):
# 	print (args)
# 	print ()
# 	print (kwargs)