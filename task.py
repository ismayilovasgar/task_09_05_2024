import itertools


class Main:
    def __init__(self):
        self.list = []

    def liste_menimset(self, mylist):
        # for i in range(5):
        #     self.list.append(int(input(f"{i+1} -ci ededi daxil edin:")))
        # self.list = [1, 2, 3, 4, 5]
        self.list = [i for i in mylist]

    def list_goster(self):
        return self.list

    def hedef_deyer_yoxlama(self):
        my_target = self.hedef = int(input("hedef deyer daxil edin:"))
        my_list = self.list

        for i in range(len(my_list)):
            for j in range(len(my_list)):
                if (my_list[i] + my_list[j] == my_target) and (i != j):
                    return f"list[{i}] = {my_list[i]}  ve list[{j}] = {my_list[j]}"
        return -1

        # 2_Yol
        # for numbers in itertools.combinations(self.list, 2):
        #     if sum(numbers) == self.hedef:
        #         return [self.list.index(number) for number in numbers]

        # return -1


# -------------------------------------------------------------------------------------------------
main = Main()
main.liste_menimset([1, 2, 3, 4, 5])
print(main.list_goster())
print(main.hedef_deyer_yoxlama())
