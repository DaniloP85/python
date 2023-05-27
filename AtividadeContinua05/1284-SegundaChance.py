contadorP = 0
contadorS = 0
qtd_alunos = []
numero_aluno = int(input())
qtd_alunos.append(numero_aluno)
n = 0
nota_original = []
nota_atividade = []
for i in range(0, qtd_alunos[n]):
    if qtd_alunos[n] != 0:
        while qtd_alunos[n] != contadorP:
            nota_aluno = float(input())
            nota_original.append(nota_aluno)
            contadorP += 1
        while qtd_alunos[n] != contadorS:
            atividade_aluno = float(input())
            nota_atividade.append(atividade_aluno)
            contadorS += 1
    else:
        print('sem notas')
t = 0
f = len(nota_original)
quantidade_nota_alterada=0
for j in range(f):
    if (nota_original[j] > 0 and nota_atividade[j] > nota_original[j]):
        quantidade_nota_alterada=quantidade_nota_alterada+1
print('NOTAS ALTERADAS:',quantidade_nota_alterada)
for w in range(f):
    print("*" if nota_original[w] > 0 and nota_atividade[w] > nota_original[w] else "-",'({:03d})'.format(w+1),'original:',f'{nota_original[w]:0>5.2f}','|','final:',f'{nota_atividade[w]:0>5.2f}')
