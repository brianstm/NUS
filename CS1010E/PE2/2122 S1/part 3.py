# PE2 Part 3


def sum_of_3(L, n):
    # Sort the list
    L = sorted(L)

    # Iterate over the list
    for i in range(len(L) - 2):
        left = i + 1
        right = len(L) - 1

        # Use two pointers to find a pair that sums up to n - L[i]
        while left < right:
            current_sum = L[i] + L[left] + L[right]

            # If the current sum is equal to n, return True
            if current_sum == n:
                return True
            # If the current sum is less than n, move the left pointer to the right
            elif current_sum < n:
                left += 1
            # If the current sum is greater than n, move the right pointer to the left
            else:
                right -= 1

    # If no triplet is found that sums up to n, return False
    return False


print(sum_of_3((11, 14, 13, 12), 39))
print(sum_of_3((11, 14, 13, 12), 40))
print(sum_of_3(tuple(range(1, 1000)), 2500))
print(sum_of_3(tuple(range(1, 1000)), 2998))
print(sum_of_3(tuple(range(1, 4000)), 11994))
print(sum_of_3(tuple(range(1, 4000)), 11995))
