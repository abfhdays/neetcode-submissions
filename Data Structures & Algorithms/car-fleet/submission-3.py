class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        carfleet = []
        for n in range(len(position)):
            carfleet.append((position[n], speed[n], (target - position[n]) / speed[n]))

        cfs = sorted(carfleet, key=lambda item: item[0], reverse=True)

        # Decreasing Monotonic Stack
        stack = []
        tracked_time = 0
        for c in cfs:
            if not stack or c[2] > tracked_time:
                stack.append(c)
                tracked_time = c[2]

        return len(stack)




        

        