import collections
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
# Time O(NlogK)
b_dict = collections.Counter(a)
heapq.nlargest(3, b_dict, key=b.dict.get)
heapq.nsmallest(3, b_dict, key=b_dict.get)