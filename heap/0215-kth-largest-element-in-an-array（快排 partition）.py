from typing import List


class Solution:

    # 数组中的第 K 个最大元素
    # 数组中第 k 大的元素，它的索引是 len(nums) - k
    def findKthLargest(self, nums: List[int], k: int) -> int:

        size = len(nums)
        if size < k:
            raise Exception('程序出错')

        # [0,1,2,3,4,5]
        # 第 k 大元素的索引是 len(nums) - k
        left = 0
        right = len(nums) - 1

        while True:
            index = self.__partition(nums, left, right)
            if index == len(nums) - k:
                return nums[index]
            if index > len(nums) - k:
                right = index - 1
            else:
                left = index + 1

    def __partition(self, nums, left, right):
        """
        partition 是必须要会的子步骤，一定要非常熟练
        在 [left, right] 这个区间执行 partition
        遇到比第一个元素大的或等于的，就放过，遇到小的，就交换
        :param nums:
        :param left:
        :param right:
        :return:
        """
        pivot = nums[left]
        k = left
        for index in range(left + 1, right + 1):
            if nums[index] < pivot:
                k += 1
                nums[k], nums[index] = nums[index], nums[k]
        nums[left], nums[k] = nums[k], nums[left]
        return k


if __name__ == '__main__':
    nums = [3, 7, 8, 1, 2, 4]
    solution = Solution()
    result = solution.findKthLargest(nums, 2)
    print(result)
