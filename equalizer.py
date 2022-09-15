"""
Main logic body.
"""
from math import sqrt
try:
    import asyncio
except ImportError:
    import uasyncio as asyncio  # noqa


variance = list()
assignments = list()


class Equalizer:
    """
    This will issue unique task-delay values in the form of prime numbers.
    """
    def __init__(self, spread: int = 100):
        global variance
        global assignments
        self.spread = spread
        self.get_primes()

    @staticmethod
    def isprime(n):
        """
        Determines if a candidate is a prime number.
        """
        prime_flag = 0

        if n > 1:
            for i in range(2, int(sqrt(n)) + 1):
                if n % i == 0:
                    prime_flag = 1
                    break
            if prime_flag == 0:
                return True
            else:
                return False
        else:
            return False

    def get_primes(self):
        """
        Gets a unique prime delay times.
        """
        global variance
        global assignments
        for number in range(self.spread):
            if self.isprime(number) and number not in variance:
                variance.append(number / 100000)
        if not assignments:
            assignments = [0] * len(variance)
        else:
            variance_length = len(variance)
            assignments.extend([0] * (len(assignments) - variance_length))
        return self

    @staticmethod
    def assign(delay_var: [int, float] = 0, base: [int, float] = 0):
        """
        This will assign a unique delay time.
        """
        if not delay_var:
            global assignments
            result = None
            for idx, (assignment, variant) in enumerate(zip(assignments, variance)):
                if not assignment:
                    result = variant
                    assignments[idx] = 1
                    break
            if result is None:
                print('Out of assignments, please increase variance spread')
                print(variance)
                print(assignments)
                raise RuntimeError
            result += base
            delay_var = result
        return delay_var

    async def wait(self, delay_var: [int, float] = 0, base: [float, int] = 0):
        """
        Returns the wait action.
        """
        delay_var = self.assign(delay_var, base)
        await asyncio.sleep(delay_var)
        return delay_var
