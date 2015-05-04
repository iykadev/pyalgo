def e_number(start, end):
	for i in range(start, end):
		result = (1 + (1/i))**i
		print(result)

def e_number_main():
	e_number(1,100000)

e_number_main()

# profiling result for 1 million

# profile: python -m profile e_number.py

"""
         500001 function calls in 6.708 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   199998    1.045    0.000    1.045    0.000 :0(charmap_encode)
        1    0.000    0.000    6.708    6.708 :0(exec)
    99999    4.368    0.000    6.193    0.000 :0(print)
        1    0.000    0.000    0.000    0.000 :0(setprofile)
   199998    0.780    0.000    1.825    0.000 cp857.py:18(encode)
        1    0.000    0.000    6.708    6.708 e_number.py:1(<module>)
        1    0.515    0.515    6.708    6.708 e_number.py:1(e_number)
        1    0.000    0.000    6.708    6.708 e_number.py:6(e_number_main)
        1    0.000    0.000    6.708    6.708 profile:0(<code object <module> at
 0x0175B390, file "e_number.py", line 1>)
        0    0.000             0.000          profile:0(profiler)
"""