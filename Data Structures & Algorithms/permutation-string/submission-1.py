class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = {}
        window = {}

        # Count s1
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)

        # Build first window
        for i in range(len(s1)):
            window[s2[i]] = 1 + window.get(s2[i], 0)

        # Check first window
        if window == count1:
            return True

        left = 0

        # Slide the window
        for right in range(len(s1), len(s2)):

            # Add new character
            window[s2[right]] = 1 + window.get(s2[right], 0)

            # Remove old character
            window[s2[left]] -= 1

            if window[s2[left]] == 0:
                del window[s2[left]]

            left += 1

            # Compare
            if window == count1:
                return True

        return False