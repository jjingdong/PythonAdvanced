# Time O(NlogN) Space O(1), runtime = 104 ms
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

def maxDistance(self, position: List[int], m: int) -> int:
    position = sorted(position)
    lo = 0
    hi = position[-1]
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if find_distance(mid) >= m:
            lo = mid + 1
        else:
            hi = mid - 1

    return hi