class Solution(object):
    def leastInterval(self, tasks, n):
        from collections import Counter, deque
        import heapq

        counts = Counter(tasks)

        max_heap = [-count for count in counts.values()]
        heapq.heapify(max_heap)

        time = 0
        cooldown = deque()

        while max_heap or cooldown:
            time += 1

            if cooldown and cooldown[0][0] <= time:
                _, remaining = cooldown.popleft()
                heapq.heappush(max_heap, -remaining)

            if max_heap:
                most_frequent = -heapq.heappop(max_heap)
                most_frequent -= 1

                if most_frequent > 0:
                    cooldown.append((time + n + 1, most_frequent))

        return time
