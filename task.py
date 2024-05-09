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
        for i in range(5):
            self.list.append(int(input(f"{i+1} ededi daxil edin:")))

    def list_goster(self):
        return self.list

    def hedef_deyer_yoxlama(self):
        self.hedef_deyer = int(input("hedef deyeri daxil edin:"))
        indeks_1 = randint(0, 4)
        indeks_2 = randint(0, 4)

        # * Ternary Operator
        # return (
        #     f"indeks_1: {indeks_1} , indeks_2: {indeks_2}"
        #     if (self.list[indeks_1] + self.list[indeks_2]) == (self.hedef_deyer)
        #     else -1
        # )

        if (self.list[indeks_1] + self.list[indeks_2]) == self.hedef_deyer:
            return f"indeks_1:{indeks_1} , indeks_2:{indeks_2}"
        else:
            return -1


# -------------------------------------------------------------------------------------------------
main = Main()
main.list_al()
print(main.list_goster())
print(main.hedef_deyer_yoxlama())
