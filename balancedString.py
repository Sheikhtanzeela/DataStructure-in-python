# we use stck
# when we find an open term we push it to the stack
# when a  closed term is found which matches to TOS we pop it
# otherwsise string is unbalanced

class Solution:
    l = [{'{','}'},{'(',')'},{'[',']'}]

    def isOpenTerm(c):
        for char[] array : TOKENS:
            if array[0] == c:
                return True
        return False


    def matches(openterm, closedterm):
        for char[] array : TOKENS:
            if array[0] == openterm:
                return array[1] == closedterm
        return False



    def isBalanced(exp):
        Stack<Character> stack = new Stack<Character>()
        for char : exp.toCharArray():
            if isOpenTerm(c):
                stack.push(c)
            else:
                if(stack.isEmpty() or !matches(stack.pop(),c)):
                    return False
                
        return stack.isEmpty()