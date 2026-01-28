class Solution:
    def average(self, salary: List[int]) -> float:
        total=sum(salary)
        return (total-min(salary)-max(salary))/(len(salary)-2)