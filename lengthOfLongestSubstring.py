# coding=utf-8
'''
@Time	  : 2019-07-01 11:39
@Author   : Bxf

@==============================@
@        ___   ___             @
@       / _ | / _ )___ ___     @
@      / __ |/ _  / -_) -_)    @
@     /_/ |_/____/\__/\__/     @
@                        ABee  @
@==============================@
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long_sub = []
        long = []
        for obj in s:
            if not obj in long_sub:
                long_sub.append(obj)

            else:
                while obj in long_sub:
                    del long_sub[0]

                long_sub.append(obj)

            if len(long_sub) > len(long):
                long = long_sub.copy()

        return len(long)



if __name__ == '__main__':

    s=" "
    class_solution = Solution()
    res = class_solution.lengthOfLongestSubstring(s)
    print(res)