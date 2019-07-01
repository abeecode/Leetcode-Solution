# coding=utf-8
'''
@Time	  : 2019-04-08 16:06
@Author   : Bxf
@FileName : TwoSum.py
@License  : (C)LINKINGMED,2019
@Contact  : bi.xinfang@linkingmed.com, 17603912161
@==============================@
@        ___   ___             @
@       / _ | / _ )___ ___     @
@      / __ |/ _  / -_) -_)    @
@     /_/ |_/____/\__/\__/     @
@                        ABee  @
@==============================@
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            pass
        else:
            for item in nums:
                if (target - item) in nums:
                    if item != target - item:
                        return [nums.index(item), nums.index(target - item)]
                    else:
                        nums_n = nums[nums.index(item) + 1:]
                        if target - item in nums_n:
                            return [nums.index(item), nums.index(item) + nums_n.index(target - item) + 1]

        return 0


if __name__ == '__main__':

    s = Solution()
    ret = s.twoSum([2, 6, 3], 6)
    print(ret)
