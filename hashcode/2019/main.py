from Pizza import Pizza
import time

time_out = 60 * 5 # 5 minutes
file_names = ["a_example.in", "b_small.in"]
#file_names = ["a_example.in", "b_small.in", "c_medium.in", "d_big.in"]

for file in file_names:
    zza = Pizza(file)
    start_time = time.time()
    while(time.time() - start_time <= time_out):
        # find the best solution

    zza.save_to_file("solution_to_"+file)
