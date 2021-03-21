"Desenvolvido por Flávia"

taxa_video = float(input())
taxa_audio = float(input())
taxa_dados = float(input())
capacidade_canal = float(input())
qntd_max = float(taxa_video*5.2 + taxa_audio*3.4 + taxa_dados*1.5) / capacidade_canal
print("{:.2f}".format(qntd_max))