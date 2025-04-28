class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        cur_index = 0
        start_index = 0
        total = 0


        while cur_index < len(gas):
            if gas[cur_index] - cost[cur_index] > 0:
                start_index = cur_index
                break
            cur_index += 1
        
        while cur_index < len(gas):
            total += gas[cur_index] - cost[cur_index]
            if total < 0:
                start_index = cur_index + 1
                total = 0
            cur_index += 1
        return start_index

            