n1, n2, n3, n4 = input().split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
media = (2 * n1 + 3 * n2 + 4 * n3 + 1 * n4)/10.0
print('Media:', f'{media:.1f}')
if media>= 7.0:
    print('Aluno aprovado.')
elif media<5.0:
    print('Alun reprovado.')
elif 5.0<media<6.9:
    print('Aluno em exame.')
    exame = float(input().strip())
    print(f"Nota do exame: {exame:.1f}")
    media = (media + exame)/2

    if(media >= 5.0):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    
    print(f"Media final: {media:.1f}")