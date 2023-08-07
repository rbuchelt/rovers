class Rover:
    def __init__(self, x, y, a, commands):
        """
        O código apresentado simula o movimento de Rovers em um plateu em Marte.

        O Plateu possui uma dimensão (5,5) e o Rover deve se movimentar dentro desses limites.

        O código fornece um tratamento de segurança para que caso o rover tente extrapolar os limites, o operador seja
        avisado e não deixe o Rover sair do Plateu.
        :param x: Posição inicial do Rover fornecida pelo operador em relação ao eixo x do Plateu
        :param y: Posição inicial do Rover fornecida pelo operador em relação ao eixo y do Plateu
        :param a: Direção atual do rover
        :param commands: Lista de comandos a ser fornecida pelo operador

        Se caso a sequência de comandos fornecida extrapolar os limites do Plateu, o Rover não se movimentará e guardará
        a posição no Plateu.
        """
        self.x = x
        self.y = y
        self.a = a
        self.commands = commands

    def turn_r(self, d):
        """
        Este método gira o rover para a direita a partir da direção atual onde:
        :param d: Direção atual do rover, sendo:
        N (North) para E (East)
        E (East) para S (South)
        S (South) para W (West)
        W (West) para N (North)
        :return: O código retorna a posição futura após o comando R para virar para a direita
        """
        self.d = d
        right = {
            "N": "E",
            "E": "S",
            "S": "W",
            "W": "N"
        }
        p = right[self.d]
        return p

    def turn_l(self, d):
        """
        Este método gira o rover para a esquerda a partir da direção atual onde:
        :param d: Direção atual do rover, sendo:
        N (North) para W (West)
        W (West) para S (South)
        S (South) para E (East)
        E (East) para N (North)
        :return: O código retorna a posição futura após o comando L para virar para a Esquerda
        """
        self.d = d
        left = {
            "N": "W",
            "W": "S",
            "S": "E",
            "E": "N"
        }
        p = left[self.d]
        return p

class Movement(Rover):
    def __init__(self, x, y, a, commands):
        super().__init__(x, y, a, commands)

    def move(self):
        try:
            coordinates = ["N", "E", "S", "W"]

            for i in self.commands:
                if self.a in coordinates and i == "R":
                    self.a = self.turn_r(self.a)
                elif self.a in coordinates and i == "L":
                    self.a = self.turn_l(self.a)
                elif self.a == "N" and i == "M" and self.y < 5:
                    self.y += 1
                elif self.a == "E" and i == "M" and self.x < 5:
                    self.x += 1
                elif self.a == "S" and i == "M" and self.y > 0:
                    self.y -= 1
                elif self.a == "W" and i == "M" and self.x > 0:
                    self.x -= 1
                else:
                    raise Exception(f"O comando {i} fornecido é inválido")

            return self.x, self.y, self.a
        except Exception as e:
            print(e)

command_list1 = ["L", "M", "L", "M", "L", "M", "L", "M", "M"]
rover1 = Movement(1, 2, "N", command_list1)
print(rover1.move())

command_list2 = ["M", "M", "R", "M", "M", "R", "M", "R", "R", "M"]
rover2 = Movement(3, 3, "E", command_list2)
print(rover2.move())
