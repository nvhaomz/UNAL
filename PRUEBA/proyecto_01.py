# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 18:55:26 2023

@author: nvhao
"""

datos =	{'https://es.wikipedia.org/wiki/Invasión_rusa_de_Ucrania_(2022-presente)' : 'guerra',
		'https://es.wikipedia.org/wiki/Guerra_civil_española' : 'guerra',
		'https://es.wikipedia.org/wiki/Guerra_de_Vietnam' : 'guerra',
		'https://es.wikipedia.org/wiki/Guerra_Fría' : 'guerra',
		'https://es.wikipedia.org/wiki/Guerra_mundial' : 'guerra',
		'https://es.wikipedia.org/wiki/Incendios_forestales_en_Chile_de_2023' : 'carastrofe',
		'https://es.wikipedia.org/wiki/Terremotos_de_Turquía_y_Siria_de_2023' : 'carastrofe',
		'https://es.wikipedia.org/wiki/Terremoto' : 'carastrofe',
		'https://es.wikipedia.org/wiki/Incendio' : 'carastrofe',
		'https://es.wikipedia.org/wiki/Ciclón' : 'carastrofe',
		'https://es.wikipedia.org/wiki/Tornado' : 'carastrofe',
		'https://es.wikipedia.org/wiki/UAE_Tour_2023' : 'deporte',
		'https://es.wikipedia.org/wiki/Rally' : 'deporte',
		'https://es.wikipedia.org/wiki/Rally' : 'deporte',
		'https://es.wikipedia.org/wiki/Copa_del_Rey' : 'deporte',
		'https://es.wikipedia.org/wiki/Natación_(deporte)' : 'deporte',
		'https://es.wikipedia.org/wiki/Tenis' : 'deporte',
		'https://es.wikipedia.org/wiki/Golf' : 'deporte',
		'https://es.wikipedia.org/wiki/Béisbol' : 'deporte',
		'https://es.wikipedia.org/wiki/Medicina' : 'salud',
		'https://es.wikipedia.org/wiki/Infarto' : 'salud',
		'https://es.wikipedia.org/wiki/Diabetes_mellitus' : 'salud',
		'https://es.wikipedia.org/wiki/Pulmón' : 'salud',
		'https://es.wikipedia.org/wiki/Hígado' : 'salud',
		'https://es.wikipedia.org/wiki/Cáncer' : 'salud',
		'https://es.wikipedia.org/wiki/VIH/sida' : 'salud',
		'https://es.wikipedia.org/wiki/COVID-19 ' : 'salud',
		'https://es.wikipedia.org/wiki/Ingeniería' : 'tecnologia',
		'https://es.wikipedia.org/wiki/Ingeniería_eléctrica' : 'tecnologia',
		'https://es.wikipedia.org/wiki/Tecnología' : 'tecnologia',
		'https://es.wikipedia.org/wiki/Ingeniería_mecánica' : 'tecnologia',
		'https://es.wikipedia.org/wiki/Ingeniería_mecatrónica' : 'tecnologia',
		'https://es.wikipedia.org/wiki/Software' : 'tecnologia',
		'https://es.wikipedia.org/wiki/Hardware' : 'tecnologia'}




for key, value in datos.items():
    print(f'{key[:16]} : {value}')