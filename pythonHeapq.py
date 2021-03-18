import collections
import heapq

'''
Python heapq is minHeap
Java priority Queue is minHeap
*(-1) to make maxHeap

heapq.heappush(heap, item)
heapq.heappop(heap)
heapq.heappushpop(heap, item) is more efficient than (heappush + heappop)
heapq.heapify(x)
heapq.nlargest(n, iterable, key=None)
heapq.nsmallest(n, iterable, key=None)
'''


a = [1, 3, 5, 7, 9]
# Time O(NlogN)
heapq.heapify(a)
# Time O(logN) -> N is the size of the heap
heapq.heappush(a, 4)
# Time O(logN)
heapq.heappop(a)
# Time O(NlogK)
b_dict = collections.Counter(a)
heapq.nlargest(3, b_dict, key=b.dict.get)
heapq.nsmallest(3, b_dict, key=b_dict.get)