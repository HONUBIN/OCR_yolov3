import json


brush = json.load(open("via_region_data.json", encoding='UTF-8'))
brush = list(brush.values())

f=open("train.txt","w")
for i, a in enumerate(brush):
    f.write('images/' + a['filename'])
    f.write(" ")
    b = list(a['regions'].values())
    i = False
    for j, c in enumerate(b):
        i = True
        d= c['shape_attributes']
        f.write(str(d['x']))
        f.write(",")
        f.write(str(d['y']))
        f.write(",")
        f.write(str(d['x']+d['width']))
        f.write(",")
        f.write(str(d['y']+d['height']))
        f.write(",")
        f.write("0")
        if j < len(b) - 1:
            f.write(" ")
    brush_list = list(brush[i]['regions'].values())
f.close()