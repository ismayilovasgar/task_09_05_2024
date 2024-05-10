# salam, Hərvaxtınız xeyir.
# Bir classdan istifadə edərək 2 metod yazın.
# İlk metodda dəyər olaraq bir list içərisində rəqəmləri alın  və onu bir listə əlavə edin ( bu şəkildə olacaq: mylist=[1,2,3,4,5])
# Daha sonra bir metod daha yazın. Bu metodda isə bizim bir argumentimiz olacaq (Hədəf rəqəm). Burada ilk metodda aldığımız listin
# dəyərləri içərisində hər hansı 2 rəqəmin cəmi verilmiş hədəf rəqəmə bərabərdirsə həmin rəqəmlərin indexlərini qaytarın.
# Əgər belə rəqəmlər yoxdursa -1 cavabı qaytarın.
# Əlavə olaraq argumentləri hansı metodunuzda istifadə etmək istədiyiniz barəsində sərbəstsiniz və əlavə arqumentlərdən istifadə edəbilərsiniz.

from random import randint


class Main:
    def __init__(self):
        self.list = []

    def list_al(self):
        # for i in range(5):
        #     self.list.append(int(input(f"{i+1} ededi daxil edin:")))
        self.list = [1, 2, 3, 4, 5]

    def list_goster(self):
        return self.list

    def hedef_deyer_yoxlama(self):

        self.hedef_deyer = int(input("hedef deyer daxil edin:"))
        for i in range(len(self.list)):
            for j in range(len(self.list)):
                if self.list[i] + self.list[j] == self.hedef_deyer:
                    return f"indeksler: {i} ve {j} elementler"

        else:
            return -1


# -------------------------------------------------------------------------------------------------
main = Main()
main.list_al()
print(main.list_goster())
print(main.hedef_deyer_yoxlama())
