class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        count = 0
        check = set()

        for e in emails:
            if self.convertAddress(e) not in check:
                check.add(self.convertAddress(e))
                count += 1

        return count
    
    def convertAddress(self, email: str) -> str:
        i = 0
        plus = 0
        output = ''
        
        while email[i] != '@':
            if plus == 0:
                if email[i] == '+':
                    plus = 1
                elif email[i] != '.':
                    output += email[i]
            i += 1
        
        while i < len(email):
            output += email[i]
            i += 1

        return output