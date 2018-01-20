import math
import time

class RandomNumberGenerator():
    def __init__(self, current_time=time.time(), multiplier=1664525, increment=1013904223, modulus=math.pow(2, 32)):
        # initialise variable
        self.multiplier = multiplier
        self.increment = increment
        self.modulus = modulus
        self.current_time = current_time

    def lcg(self):
        # Creating Pseudo-Rnadom Number Genrator using LCG
        self.current_time = int(self.increment + self.current_time * self.multiplier) % self.modulus
        value = 0
        value = self.current_time / self.modulus
        return value

    def lcg_to_range(self,min,max):
        # Generating random number in given range
        lcg = self.lcg()
        value = min + lcg * (max-min)
        return value

if __name__ == "__main__":
    obj = RandomNumberGenerator()
    min_list = []
    max_list = []
    final_list = []
    min_limit = int(input("Enter Lower value of range\n"))
    max_limit =int(input("Enter Upper value of range\n"))
    mid_val = (min_limit + max_limit) / 2
    # random number generating 73 times upper values
    while len(max_list) != 73:
        val = int(obj.lcg_to_range(mid_val+1, max_limit+1))
        max_list.append(val)
        continue
    # random number generating 27 times lower values
    while len(min_list) != 27:
        val = int(obj.lcg_to_range(min_limit,mid_val-1))
        min_list.append(val)
        continue

    print("Number of values in max_list :" + str(len(max_list)))
    print(max_list)
    print("Number of values in min_list :" + str(len(min_list)))
    print(min_list)
    final_list = min_list+max_list
    print("Final list: ")
    print(final_list)

