def find_max_min(num_list):
   if min(num_list) == max(num_list):
     return [len(num_list)]
   else:
     return [min(num_list), max(num_list)]
