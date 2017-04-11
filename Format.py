with open('d:\\data\\corpus.dat', 'r') as r:
    lines = r.readlines()
with open('d:\\data\\corpus.txt', 'w') as w:
    for l in lines:
        l.replace('<content>', '').replace('</content>', '').replace('\t', '').replace('\n', '').replace(' ', '')
        if l.strip() == "":
            continue
        w.write(l)
