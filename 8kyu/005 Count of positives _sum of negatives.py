#Count the positive numbers, sum the negative ones, 0 doesn't count, return None if none

def count_positives_sum_negatives(arr):
    counter = 0
    sum = 0
    if arr == []:
        return []
    else:
        for num in arr:
            if num > 0:
                counter += 1
            if num < 0:
                sum = sum + num
            else:
                pass
        return[counter,sum]