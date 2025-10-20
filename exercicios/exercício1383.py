class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        import heapq

        MOD = 10**9 + 7
        engineers = []

        for i in range(n):
            engineers.append((efficiency[i], speed[i]))
        
        engineers.sort(reverse=True)

        min_heap = []
        speed_sum = 0
        max_performance = 0
        
        for curr_efficiency, curr_speed in engineers:
            heapq.heappush(min_heap, curr_speed)
            speed_sum += curr_speed
            
            if len(min_heap) > k:
                removed_speed = heapq.heappop(min_heap)
                speed_sum -= removed_speed
            
            current_performance = speed_sum * curr_efficiency
            
            max_performance = max(max_performance, current_performance)
        
        return max_performance % MOD