import heapq

'''

'''


a = [1, 3, 5, 7, 9]
# Time O(NlogN)
heapq.heapify(a)
# Time O(logN)
heapq.heappush(a, 4)
# Time O(logN)
heapq.heappop(a)