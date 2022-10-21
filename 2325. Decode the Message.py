class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        az = (chr(a) for a in range(97, 123))
        answer = {' ': ' '}
        for s in key:
            if s not in answer:
                answer[s] = next(az)
        return ''.join([answer[m] for m in message])
