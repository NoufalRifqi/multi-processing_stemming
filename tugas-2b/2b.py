from concurrent.futures import process
import multiprocessing
from multiprocessing import Process
from multiprocessing import cpu_count
from tracemalloc import start
from encodings import utf_8
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import time

factory = StemmerFactory()

# Stemming tanpa multi-processing (file ukuran 10mb)
file_10mb = open('10mb.txt', 'r', encoding='utf_8').read()
start1 = time.perf_counter()
stemmer1 = factory.create_stemmer()
teks_stem1 = stemmer1.stem(file_10mb)
hasil1 = open('stemming10.txt', 'w', encoding='utf_8').write(teks_stem1)
finish1 = time.perf_counter()
print('Waktu proses untuk stemming file ukuran 10 mb : {} detik'.format(finish1-start1))

# Stemming tanpa multi-processing (file ukuran 15mb)
file_15mb = open('15mb.txt', 'r', encoding='utf_8').read()
start2 = time.perf_counter()
stemmer2 = factory.create_stemmer()
teks_stem2 = stemmer2.stem(file_15mb)
hasil2 = open('stemming15.txt', 'w', encoding='utf_8').write(teks_stem2)
finish2 = time.perf_counter()
print('Waktu proses untuk stemming file ukuran 15 mb : {} detik'.format(finish2-start2))

# Stemming tanpa multi-processing (file ukuran 20mb)
file_20mb = open('20mb.txt', 'r', encoding='utf_8').read()
start3 = time.perf_counter()
stemmer3 = factory.create_stemmer()
teks_stem3 = stemmer3.stem(file_20mb)
hasil3 = open('stemming20.txt', 'w', encoding='utf_8').write(teks_stem3)
finish3 = time.perf_counter()
print('Waktu proses untuk stemming file ukuran 20 mb : {} detik'.format(finish3-start3))


# Stemming dengan multi-processing
def stemming(teks):
    stemmer = factory.create_stemmer()
    teks_stem = stemmer.stem(teks)
    file = open('stemming10.txt', 'a', encoding='utf-8').write(teks_stem)
    # file = open('stemming15.txt', 'a', encoding='utf-8').write(teks_stem)
    # file = open('stemming20.txt', 'a', encoding='utf-8').write(teks_stem)

if __name__ == "__main__":
    teks = open('10mb.txt', 'r', encoding='utf-8').read()
    # teks = open('15mb.txt', 'r', encoding='utf-8').read()
    # teks = open('20mb.txt', 'r', encoding='utf-8').read()
    
    start = time.perf_counter()
    array = []
    cpu = cpu_count()
    awal_kalimat = 0
    for i in range(cpu):
        jumlah = int(len(teks)/cpu)
        akhir_kalimat = teks.find(" ", awal_kalimat+jumlah)
        if (akhir_kalimat == -1):
            akhir_kalimat = len(teks)
        array.append(teks[awal_kalimat:akhir_kalimat])
        awal_kalimat = akhir_kalimat

    process = []
    for i in range(cpu):
        s = multiprocessing.Process(target=stemming, args=(array[i], ))
        process.append(s)
        process[i].start()

    for s in process:
        s.join()
    finish = time.perf_counter()
    print('Waktu proses stemming dengan multi-processing untuk file ukuran 10 mb : {} detik'.format(finish-start))
    # print('Waktu proses stemming dengan multi-processing untuk file ukuran 15 mb : {} detik'.format(finish-start))
    # print('Waktu proses stemming dengan multi-processing untuk file ukuran 20 mb : {} detik'.format(finish-start))