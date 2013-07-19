# run this one first, to update the overall code from the base ("periodic_table.html")
# then run add_xSLD_toperiodic.py to add the xray bits.

import periodictable as pt
import simplejson

#sa = open('periodic_table.html', 'r').readlines()
#sout = open('periodic_table.json', 'w')
wl = 1.5418 # copper K-alpha

by_el_name = {}
by_symbol = {}
ptable = []

for n in range(1,119):
    #n = el.number
    if n in pt.elements._element:
        el = pt.elements[n]
        if not hasattr(el, 'symbol'): continue
        item = {
            "symbol": el.symbol,
            "name": el.name,
            "number": el.number,
            "nSLD": el.neutron.sld()[0],
            "iSLD": el.neutron.sld()[2],
            "xSLD": el.xray.sld(wavelength=wl)[0],
            "b_c": el.neutron.b_c,
            "b_p": el.neutron.bp,
            "density": el.density,
            "number_density": el.number_density *1e-22 if el.number_density else None
            }
    else: item = {}
    ptable.append(item)
    
simplejson.dump(ptable, open('periodic_table.json', 'w'), indent=4)
jspt = simplejson.dumps(ptable, indent=4)
with open('periodic_table.js', 'w') as jsout:
    jsout.write("elements = ")
    jsout.write(jspt)
    

        
    
