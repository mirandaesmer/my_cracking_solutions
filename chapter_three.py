from stack import Stack


class ChapterThree:
    def problem1(self) -> None:
        # Describe how you could use a single array to implement three stacks
        
        # NOTE: see three_stack.py and three_stack_tests.py
        pass
        
    def problem2(self) -> None:
        # Stack Min: How would you design a stack which, in addition to push and
        # pop, has a function min which returns the minimum element? Push, pop
        # and min should all operate in 0(1) time.
        
        # NOTE: see min_stack.py and min_stack_tests.py
        pass

    def problem3(self) -> None:
        # Imagine a (literal) stack of plates. If the stack gets too high, it
        # might topple. Therefore, in real life, we would likely start a new
        # stack when the previous stack exceeds some threshold. Implement a
        # data structure SetOfStacks that mimics this. SetO-fStacks should be
        # composed of several stacks and should create a new stack once the
        # previous one exceeds capacity. SetOfStacks. push() and SetOfStacks.
        # pop() should behave identically to a single stack (that is, pop()
        # should return the same values as it would if there were just a single
        # stack).
        # FOLLOW UP
        # Implement a function popAt(int index) which performs a pop operation
        # on a specific sub-stack.
        
        # NOTE: see MinStack class in set_of_stacks.py
        # TODO missing tests (set_of_stacks_tests.py)
        pass

    def problem4(self) -> None:
        # Implement a MyQueue class which implements a queue using two stacks
        
        # NOTE: see TwoStackQueue class in two_stack_queue.py
        # TODO missing tests (two_stack_queue_tests.py)
        pass

    def problem5(self, stack: Stack) -> Stack:
        # Write a program to sort a stack such that the smallest items are on
        # the top. You can use an additional temporary stack, but you may not
        # copy the elements into any other data structure (such as an array).
        # The stack supports the following operations: push, pop, peek, and
        # isEmpty.
        
        # TODO rethink strategy
        return stack

    def problem6(self):
        # An animal shelter, which holds only dogs and cats, operates on a
        # strictly "first in, first out" basis. People must adopt either the
        # "oldest" (based on arrival time) of all animals at the shelter, or
        # they can select whether they would prefer a dog or a cat (and will
        # receive the oldest animal of that type). They cannot select which
        # specific animal they would like. Create the data structures to
        # maintain this system and implement operations such as enqueue,
        # dequeueAny, dequeueDog, and dequeueCat. You may use the built-in
        # Linked list data structure.
        
        # NOTE: see AnimalShelterQueue class in animal_shelter_queue.py
        # TODO missing tests (animal_shelter_queue_tests.py)
        pass
