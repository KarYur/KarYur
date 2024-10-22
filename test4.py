
# shirina = int(input())
# # trek = int(input())

shirina = 3100
krishk_list = 6000
kolichestvo_krishek = 1
mnojitel = 2
while mnojitel > 0:

    if shirina <= krishk_list:
        krishk_list -= shirina
        mnojitel -= 1
    else:
        kolichestvo_krishek += 1
        krishk_list = 6000
print(kolichestvo_krishek)
