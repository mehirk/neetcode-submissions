class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stack = []

        cars = list(zip(position, speed))
        cars.sort(reverse = True)

        for pos, spd in cars:
            current_time = (target - pos) / spd

            if not stack or current_time > stack[-1]:
                stack.append(current_time)
        
        return len(stack)
