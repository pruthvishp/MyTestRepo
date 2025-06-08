class sorting_test():
    def __init__(self, num_list: list)->list:
        self.num_list = num_list

    def bubble_sort(self):
        n = len(self.num_list)
        for i in range(n):
            for j in range(n-i-1):
                # sorting window starts at n-2 index and pushes greatest element to n-1th index and shrinks with each iteration to 0
                # swapping happens left to right
                if self.num_list[j]>self.num_list[j+1]:
                    self.num_list[j],self.num_list[j+1] = self.num_list[j+1],self.num_list[j]
        return self.num_list
    
    def insertion_sort(self):
        n = len(self.num_list)
        for i in range(n):
            #sorting window starts at 0 and grows with each iteration
            #numbers are slid right until an element greater is found
            k = self.num_list[i]
            j = i-1 
            while(j>=0 and self.num_list[j]> k):
                self.num_list[j+1] = self.num_list[j]
                j = j-1
            self.num_list[j+1] = k
        return self.num_list
            




cl_sor = sorting_test([ 1,7,0,9,1,9,8,7])
print(cl_sor.bubble_sort())
cl_sor_i = sorting_test([ 1,7,0,9,1,9,8,7])
print(cl_sor_i.insertion_sort())     

