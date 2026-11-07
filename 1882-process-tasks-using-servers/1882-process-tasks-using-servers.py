import heapq


class Solution:

  def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
    # Min-heap of available servers: (weight, index)
    free = [(weight, i) for i, weight in enumerate(servers)]
    heapq.heapify(free)

    # Min-heap of busy servers: (free_time, weight, index)
    busy = []

    ans = [0] * len(tasks)
    current_time = 0

    for j, duration in enumerate(tasks):
      # Advance time to at least the arrival of the j-th task
      current_time = max(current_time, j)

      # If all servers are busy, fast-forward time to the earliest completion
      if not free:
        current_time = busy[0][0]

      # Move all servers that have finished by current_time back to the free heap
      while busy and busy[0][0] <= current_time:
        _, weight, idx = heapq.heappop(busy)
        heapq.heappush(free, (weight, idx))

      # Pop the best available server and assign the task
      weight, idx = heapq.heappop(free)
      ans[j] = idx
      heapq.heappush(busy, (current_time + duration, weight, idx))

    return ans
