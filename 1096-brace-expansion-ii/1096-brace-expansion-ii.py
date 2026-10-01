class Solution:
    def braceExpansionII(self, expression: str):
        
        def multiply(set1, set2):
            result = set()

            for a in set1:
                for b in set2:
                    result.add(a + b)

            return result

        def parse():
            nonlocal i

            result = set()
            current = set()

            while i < len(expression) and expression[i] != '}':
                
                if expression[i] == '{':
                    i += 1
                    part = parse()
                    i += 1   # skip '}'

                elif expression[i].isalpha():
                    part = {expression[i]}
                    i += 1

                if not current:
                    current = part
                else:
                    current = multiply(current, part)

                if i < len(expression) and expression[i] == ',':
                    result.update(current)
                    current = set()
                    i += 1

            result.update(current)

            return result

        i = 0
        answer = parse()

        return sorted(answer)