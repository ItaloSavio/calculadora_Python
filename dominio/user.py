class user:
    def __init__(self, nome, sobre):
        self.nome = nome
        self.sobre = sobre

    def exibir_user(self):
        return f'{self.nome} {self.sobre}'
