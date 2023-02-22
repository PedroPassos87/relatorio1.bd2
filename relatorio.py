class Professor:
    def __init__(self,nome):
        self.nome = nome
    
    
    def ministrar_aula(self,assunto):
        print(f'O professor {self.nome} esta ministrando uma aula sobre {assunto}.')



class Aluno:
    def __init__(self,nome):
        self.nome = nome

    def presenca(self):
        print(f'O aluno {self.nome} esta presente.')



class Aula:

    def __init__(self,prof,assunto):
        self.prof = prof
        self.assunto = assunto
        
    def adicionar_aluno(self,aluno):
        alunos.append(aluno)

    def listar_presenca(self):
        print(f"Presença na aula sobre {self.assunto} ,ministrada pelo professor {self.prof.nome}: ")

        print(aluno1.presenca())

        print(aluno2.presenca())


alunos = []
professor1 = Professor("Lucas")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")    
aula1 = Aula(professor1,"Poo")
aula1.adicionar_aluno(aluno1)
aula1.adicionar_aluno(aluno2)
print(aula1.listar_presenca())
