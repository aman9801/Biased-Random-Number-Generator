# Random-Number-Generator
Write a custom random number generation algo which should be 73% biased to the higher number. Like if I want a random number between 1 to 10 100times then it should give number more than 5 73times and less than 5 27times.

Algorithm:

Step 1 : Take input from user:                                     
        	a := lower limit                      
        	b := upper limit
       
Step 2 : Calculating mid value for biased probability                                      
       		mid_val := (a+b)/2

Step 3 : Calculate range of biased numbers by mid_val (excluding mid_val) eg. 73% above 5 and 27% below 5                                 
        	min_list := min_list will contain value from range 'a' to mid_val-1                                                  
        	max_list := max_list will contain value from range mid_val+1 to b+1

Step 4 : Calculate random number using Linear congruential generator(Pseudo-random Number Genrator)  

		      while(length of max_list =! 73)	
			     number = (current_time +increment_value * multiplier) % mod
			     value = number/mod
			     value_in_range = (mid_val+1) + value * ((b+1)-(mid_val+1))
			     add value_in_range to max_list

		      while(length of min_list =! 27)	
		       number = (current_time +increment_value * multiplier) % mod
			     value = number/mod
			     value_in_range = a + value * ((mid_val-1)-a)
			     add value_in_range to min_list

Step 5 : Show min_list , max_list and final_list (concatenation of min_list and max_list)

Explanation:
1. First take the lower limit and upper limit of range from user. Calculate mid value from these two limits to separate the range into two parts upper range and lower range. 

2. Then create two list say min_list which will contain values from lower limit to mid value(excluding) and max_list which will contain values from mid value (excluding) to upper limit.

3. Start the while loop1 until the length of max_list becomes 73. 
   In this loop random number is generated using Linear congruential generator(LCG) method in which an equation is used ie                  [number = (increment + current time * multiplier) % mod] and then 'number' generated from this equation is put into                      [value = number / mod] (which will give output value between 0 and 1). And this value is put into a formula                              [lower limit + value * (upper limit - lower limit] to calculate random number in given desired range. 
   Then add final value to max_list

4. Start the second while loop2 until the length of min list becomes 27.
   Same procedure is done as above while loop1
   Then add final value to min_list

5. Print both the max_list and min_list

6. Then print final_list ie concatenated list of max_list and min_list
