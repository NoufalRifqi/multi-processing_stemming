import nltk.tokenize.punkt

f = open('teks_asli.txt', 'r', encoding='utf-8', errors='ignore')
d = f.read()

seg_kalimat = nltk.data.load('indonesian.pickle')
teks_kalimat = seg_kalimat.tokenize(d)
file = open('hasil_punkt.txt', 'w', encoding='utf-8', errors='ignore')
for kalimat in teks_kalimat:
    file.write(kalimat.strip())
    file.write("\n")
