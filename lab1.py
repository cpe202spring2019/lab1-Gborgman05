
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   # bad input handling
   if int_list == None:
      raise ValueError
   elif len(int_list) == 0:
      return None
   # iteration to find max
   max_int = int_list[0]
   for num in int_list:
      if num > max_int:
         max_int = num
   return max_int

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   # bad input handling
   if int_list == None:
      raise ValueError
   elif len(int_list) == 0:
      return []
   #just as inefficient, how to order correctly without inserting, which i assume is inefficient
   current_num = int_list.pop(0)
   reverse_rec(int_list)
   (int_list).append(current_num)
   return int_list

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   
   # bad input handling
   if int_list == None:
      raise ValueError
   
   #((high - low) // 2) + low is midpoint
   #move goalposts dependent on if target is in high half or low half
   if high - low <= 1:
      return None
   elif int_list[((high - low) // 2) + low] > target:
      return bin_search(target, low, ((high - low) // 2) + low, int_list)
   elif int_list[((high - low) // 2) + low] < target:
      return bin_search(target, ((high - low) // 2) + low, high, int_list)
   
   # value should be between high and low at all times, if low is greater than high
   # or they are 1 index apart, the item must not be in the list
   elif int_list[((high - low) // 2) + low] == target:
      return ((high - low) // 2) + low
   

