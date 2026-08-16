class Solution:
    def isValid(self, s: str) -> bool:
        #create an empty stack
        #append each opening element into the stack
        #create a while loop to go thru the string s
        #if closing character is found, then see    end of may    
        #if yes, then pop both chars
        #if not return false    
        stack = []
        if len(s) <=1:
            return False
                    
        for x in s:
            if(x == '(' or x=='[' or x=='{'):
                stack.append(x)
            elif x==')':
                if stack and stack.pop() == '(':
                    pass
                else:
                    return False
            elif x==']':
                if stack and stack.pop()== '[':
                    pass
                else:
                    return False
            elif x=='}':
                if stack and stack.pop() == '{':
                    pass
                else:
                    return False

        return len(stack)==0