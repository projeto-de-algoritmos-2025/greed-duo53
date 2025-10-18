class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        i, j = 0, len(people) - 1
        boats = 0

        while i <= j:
            # parear o mais leve (i) com o mais pesado (j)
            if people[i] + people[j] <= limit:
                i += 1  # coube com o leve
            #  o mais pesado (j) embarca agora
            j -= 1
            boats += 1

        return boats
