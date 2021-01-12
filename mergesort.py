
def merge(arr1, arr2):
  output = []
  start_length_arr1 = len(arr1)
  start_length_arr2 = len(arr2)
  target_output_length = start_length_arr1 + start_length_arr2

  while len(output) < target_output_length:
    print('---------')
    print('arr1: ', arr1)
    print('arr2: ', arr2)
    print('output: ', output)
    if len(arr1) == 0:
      output += arr2
      arr2 = []
    elif len(arr2) == 0:
      output += arr1
      arr1 = []
    elif arr1[0] < arr2[0]:
      output.append(arr1[0])
      arr1 = arr1[1:]
    else:
      output.append(arr2[0])
      arr2 = arr2[1:]
  return output


def split(arr):
  print('splitting: ', arr)
  midpoint = len(arr) // 2
  arr1 = arr[:midpoint]
  arr2 = arr[midpoint:]
  if len(arr1) <= 1 and len(arr2) <= 1:
    return merge(arr1, arr2)
  split_arr1 = split(arr1)
  split_arr2 = split(arr2)
  return merge(split_arr1, split_arr2)
print('final result: ', split([1,2,5, 4, 8, 7]))