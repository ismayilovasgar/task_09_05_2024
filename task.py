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

        self.hedef_deyer = int(input("hedef deyer daxil edin:"))
        for i in range(len(self.list)):
            for j in range(len(self.list)):
                if self.list[i] + self.list[j] == self.hedef_deyer:
                    return f"indeksler: {i} ve {j} elementler"

        return -1


# -------------------------------------------------------------------------------------------------
main = Main()
main.liste_menimset([1, 2, 3, 4, 5])
print(main.list_goster())
print(main.hedef_deyer_yoxlama())
