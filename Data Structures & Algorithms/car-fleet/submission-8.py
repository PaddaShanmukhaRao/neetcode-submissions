class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p,s] for p,s in zip(position,speed) ]
        pairs.sort(reverse=True)
        fleet=[]
        for p,s in pairs:
            t = (target-p)/s
            if not fleet or fleet[-1]<t:
                fleet.append(t)
        return len(fleet)