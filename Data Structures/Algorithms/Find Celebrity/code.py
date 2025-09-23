class Solution:
    def findCelebrity(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        # A celebrity is known by everyone but knows no one.
        # So if we find a person who knows someone, they cannot be a celebrity.
        # If we find a person who is not known by someone, they cannot be a celebrity.
        
        # Step 1: Find a candidate for celebrity
        def knows():
            pass
        
        celeb = 0
        for i in range(n):
            if knows(celeb, i):
                celeb = i
        
        for i in range(n):
            if celeb != i:
                if knows(celeb, i) or not knows(i, celeb):
                    return -1
        
        return celeb