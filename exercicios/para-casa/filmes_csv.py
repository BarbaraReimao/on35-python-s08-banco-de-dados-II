import csv

filmes = [
     [1, 'O Poderoso Chefão', 'Francis Ford Coppola', 1972, 'Drama', 25.99],  
     [2, 'A Origem','Christopher Nolan', 2010, 'Ficção Científica', 19.99],
     [3, 'A Vida de Brian', 'Terry Gilliam', 1979, 'Comédia', 15.99],
     [4, 'Pulp Fiction', 'Quentin Tarantino', 1994, 'Crime', 22.99],
     [5, 'Senhor dos Anéis: A Sociedade do Anel', 'Peter Jackson', 2001, 'Fantasia', 30.99]
 ]

with open('filmes.csv', 'w', newline = '', encoding = 'UTF-8' ) as csvfile: 
     escritor = csv.writer(csvfile) 
     escritor.writerow(['id', 'Título', 'Diretor', 'Lancamento', 'Genero', 'Preco']) 
     escritor.writerows(filmes) 
