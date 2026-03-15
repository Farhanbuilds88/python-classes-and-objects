class NumberUtils:

    @staticmethod
    def check_number(num):
        if num > 0:
            print("Positive")
        elif num < 0:
            print("Negative")
        else:
            print("Zero")

NumberUtils.check_number(-5)

class Geometry:

    @staticmethod
    def circle_area(radius):
        return 3.14 * radius * radius

print(Geometry.circle_area(5))

class Voting:

    @staticmethod
    def is_eligible(age):
        if age >= 18:
            print("Eligible to vote")
        else:
            print("Not eligible")

Voting.is_eligible(20)