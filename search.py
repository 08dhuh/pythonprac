#!/usr/bin/env python
# coding: utf-8

# <h2>Implement Linear Search</h2>

# In[18]:


def linear_search(search_list, target_value):
    matches = []
    for i, value in enumerate(search_list):
        print(value)
        if value == target_value:
            matches.append(i)
    if matches: return matches
    raise ValueError(f"{target_value} not in the list")


# <h2>Binary Search</h2>
# Using recursive approach

# In[19]:


def binary_search(sorted_list:list, target):
    if not sorted_list:
        return "value not found"
    mid_idx = int(len(sorted_list)/2)
    mid_val = sorted_list[mid_idx]
    if mid_val == target:
        return mid_idx
    if mid_val > target:
        left_half = sorted_list[:mid_idx]
        return binary_search(left_half, target)
    elif mid_val < target:
        right_half = sorted_list[mid_idx+1:]
        result = binary_search(right_half, target)
        if result == "value not found":
            return result
        return result + mid_idx + 1

binary_search(list(range(12)),0)


# In[20]:


#binary search using pointers
def binary_search(sorted_list:list, target, left_index=None, right_index=None):
    if left_index is None or right_index is None:
        left_index = 0
        right_index = len(sorted_list)
    if left_index >= right_index:
        return "value not found"
    mid_index = (left_index + right_index) // 2
    mid_val = sorted_list[mid_index]
    if mid_val == target:
        return mid_index
    elif mid_val < target:
        return binary_search(sorted_list, target, left_index, mid_index)
    elif mid_val > target:
        return binary_search(sorted_list, target, mid_index+1, right_index)
    


# In[23]:


def sparse_search(data, search_val):
  print("Data: " + str(data))
  print("Search Value: " + str(search_val))
  first = 0
  last = len(data) -1
  while first<= last:
    mid = (first+last)//2
    if not data[mid]:
      left = mid-1
      right = mid+1
      while True:
        if left<first and right>last:
          print(f'{search_val} is not in the dataset')
          return
        elif right <= last and data[right]:
          mid = right
          break
        elif left>=first and data[left]:
          mid = left
          break
        left -= 1
        right += 1
    if data[mid] == search_val:
      print(f"{search_val} found at position {mid}")
      return
    if data[mid] > search_val:
      last = mid - 1
    if data[mid] < search_val:
      first = mid + 1
  print(f'{search_val} not found in the list')


# In[22]:


sparse_search(["A", "", "", "", "B", "", "", "", "C"], "B")

sparse_search(["A", "", "", "", ""], "A")
sparse_search(["", "", "", "", "Z"], "Z")

