class Participante:
   def __init__(self, matricula, nome, email):
      self.matricula = matricula
      self.nome = nome
      self.email = email
      
   def __str__(self):
      return (self.matricula + ' '+ self.nome + " " + self.email)