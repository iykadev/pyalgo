def hanoi_tower_algorithm(n, x, y, z):
	"""
	Source: http://en.wikipedia.org/wiki/Tower_of_Hanoi
	Fransız matematikçi, Edouard Lucas tarafından önerilen bir kule problemidir.
	A,B ve C gibi dik konumda yerleştirilmiş üç çubuk ve n adet disk verilmektedir.
	Başlangıç durumunda diskler, üstteki her diskin çapı daha küçük olmak koşuluyla A çubuğuna yerleştirilmiştir.
	Her seferinde yalnız bir diskin hareketine izin verildiğinde, büyük diski küçüğünün üzerine yerleştirmeden,
	disklerin C çubuğuna taşınması istenmektedir.

	Hanoi problemini, problemi alt problemlere parçalayarak çözebiliriz. Problemde N sayıda disk varsa recursive şekilde
	genel çözüm şöyle olabilir:

		Tek disk direkt 3. çubuğa koyuluyor
		N sayıda disk 3 adıma koyulmalı

	A- (N-1) disk orta çubuğa taşınır.
	B- En alttaki disk direkt sağa konulur.
	C- (N-1) disk sağa taşınır.

	Output (Number of Disc 4):

		Diski A çubuğundan B çubuğuna koy
		Diski A çubuğundan C çubuğuna koy
		Diski B çubuğundan C çubuğuna koy
		Diski A çubuğundan B çubuğuna koy
		Diski C çubuğundan A çubuğuna koy
		Diski C çubuğundan B çubuğuna koy
		Diski A çubuğundan B çubuğuna koy
		Diski A çubuğundan C çubuğuna koy
		Diski B çubuğundan C çubuğuna koy
		Diski B çubuğundan A çubuğuna koy
		Diski C çubuğundan A çubuğuna koy
		Diski B çubuğundan C çubuğuna koy
		Diski A çubuğundan B çubuğuna koy
		Diski A çubuğundan C çubuğuna koy
		Diski B çubuğundan C çubuğuna koy

	4 adet diskli bir durumda disk sayısı n = 1 olduğunda toplam 3 durum ve çözüm için K1 = 1 olmakta.
	Disk sayısı n = 2 olduğunda toplam 9 durum ve minimum geçiş K2 = 3 olmakta.
	Disk sayısı n = 3 olduğunda toplam 27 durum ve minimum geçiş K3 = 7 olmakta.
	Disk sayısı n = 4 olduğunda toplam durum sayısı 81 ve minimum geçiş ise K4 = 15 olmakta.

	Çubuk sayısı 3 olduğunda N adet disk için minimum geçişler, yinelemeli biçimde Kn = (2 Kn-1 +1) veya
	n'ye bağımlı olarak Kn = 2^n - 1 şeklinde bulunmaktadır.
	"""
	if n == 1:
		print("Diski %s çubuğundan %s çubuğuna koy" % (x,z))
	else:
		hanoi_tower_algorithm(n-1, x, z, y)
		hanoi_tower_algorithm(1, x, y, z)
		hanoi_tower_algorithm(n-1, y, x, z)

def hanoi_tower_algorithm_main(ndisc):
	# ndisc = Number of Disc
	hanoi_tower_algorithm(ndisc, "A", "B", "C")

hanoi_tower_algorithm_main(10)

# profiling result for 10 numbers

# profile: python -m profile hanoi_tower_algorithm.py

"""
         6654 function calls (5121 primitive calls) in 0.078 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     2046    0.000    0.000    0.000    0.000 :0(charmap_encode)
        1    0.000    0.000    0.078    0.078 :0(exec)
     1023    0.062    0.000    0.078    0.000 :0(print)
        1    0.000    0.000    0.000    0.000 :0(setprofile)
     2046    0.016    0.000    0.016    0.000 cp857.py:18(encode)
        1    0.000    0.000    0.078    0.078 hanoi_tower_algorithm.py:1(<module
>)
   1534/1    0.000    0.000    0.078    0.078 hanoi_tower_algorithm.py:1(hanoi_t
ower_algorithm)
        1    0.000    0.000    0.078    0.078 hanoi_tower_algorithm.py:44(hanoi_
tower_algorithm_main)
        1    0.000    0.000    0.078    0.078 profile:0(<code object <module> at
 0x01DCC2A0, file "hanoi_tower_algorithm.py", line 1>)
        0    0.000             0.000          profile:0(profiler)
"""