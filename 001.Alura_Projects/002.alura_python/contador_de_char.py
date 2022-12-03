total = 0
palavra = "python rocks!aaaaaaaaaaaa"
acabou = False
while (not acabou):
    acabou = ( total == len(palavra) ) 
    total += 1
print(total - 1)