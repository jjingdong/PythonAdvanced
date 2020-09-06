'''
bisect.bisect(list,num,beg,end)
bisect.bisect_left(list,num,beg,end)
bisect.bisect_right(list,num,beg,end)
'''
import bisect

a = [1, 3, 4, 4, 4, 6, 7]
# b = 5, the rightmost index to insert
b = bisect.bisect(a, 4)
# c = 2, the leftmost index to insert
c = bisect.bisect_left(a,4)
# d = 4, the rightmost index to insert, so list remains sorted
d = bisect.bisect_right(a, 4, 0, 4)

def searchInsert(self, nums: List[int], target: int) -> int:
    return bisect.bisect_left(nums, target)

# Time O(NlogN) Space O(1), runtime - 40 ms
def searchInsert(self, nums: List[int], target: int) -> int:

    if not nums or not target: return 0

    lo, hi = 0, len(nums)-1
    while lo <= hi:
        mid = lo + (hi-lo)//2
        m_value = nums[mid]
        if m_value == target:
            return mid
        elif m_value > target:
            hi = mid - 1
        else:
            lo = mid + 1

    return lo

'''
insort(list, num, beg, end)
insort_left(list, num, beg, end)
insort_right(list, num, bed, end)
'''