import pygal
import json
from country_codes import get_country_code
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

cc_pops1, cc_pops2, cc_pops3 = {}, {}, {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            if population < 10000000:
                cc_pops1[code] = population
            elif population < 1000000000:
                cc_pops2[code] = population
            else:
                cc_pops3[code] = population


wm_style = RotateStyle("#336699",base_style=LightColorizedStyle)
#wm_style = LightColorizedStyle
world_map = pygal.Worldmap(style=wm_style)
world_map.title = "World Population in 2010, by country"
world_map.add('0-10m', cc_pops1)
world_map.add('10m-10b',cc_pops2)
world_map.add('>10b',cc_pops3)
world_map.render_to_file("world_population_map.svg")