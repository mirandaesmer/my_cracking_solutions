class ChapterSix:
    def problem6(self) -> int:
        # There are 100 closed lockers in a hallway. A man begins by opening all
        # 100 lockers. Next, he closes every second locker. Then, on his third
        # pass, he toggles every third locker (closes it if it is open or opens
        # it if it is closed). This process continues for 100 passes, such that
        # on each pass i, the man toggles every ith locker. After his 100th pass
        # in the hallway, in which he toggles only locker #100, how many lockers
        # are open?
        
        # Complexity: O( 100 x 100 + 1 ) comparisons, constant
        # Only looking for solution to problem, not
        
        arr = [True] * 100  # skip first iteration, all open
        for jump_size in range(2, 101):
            for i in range(1, 100):
                if i % jump_size == 0:
                    arr[i] = not arr[i]
        return len([a for a in arr if a])
