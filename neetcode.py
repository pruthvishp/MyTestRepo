class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        list_of_keys = []
        freq_dict = {'a': 0}
        for element in nums:
            print(f'dict is {freq_dict}')
            if element not in freq_dict.keys():
                freq_dict = freq_dict.update({element: 1})
            else:
                freq_dict[element] +=1
        for value in sorted(set(freq_dict.values())):
            for ke,va in freq_dict:
                if va == value:
                    list_of_keys.append(ke)
                if len(list_of_keys) == k:
                    break
        return list_of_keys
sol = Solution()
sol.topKFrequent([1,1,1,3,4,5,63,4], 2)

