#Date due stringhe s e t, restituire True se t è un anagramma di s, e False altrimenti.
#Un anagramma è una parola o una frase formata riorganizzando le lettere di una parola 
#o frase diversa, in genere utilizzando tutte le lettere originali esattamente una volta.


import unittest

def anagram(s: str, t: str) -> bool:
    # Converte entrambe le stringhe in minuscolo e poi le ordina
    # Confronta le versioni ordinate delle due stringhe
    # Ritorna True se sono uguali, False altrimenti
    return sorted(s.lower()) == sorted(t.lower())

class TestAnagram(unittest.TestCase):

    def read_input(self, filename):
        with open(filename, 'r') as file:
            s = file.readline().strip()
            t = file.readline().strip()
        
        print(s, t)
        return s, t

    def write_output(self, filename, result):
        with open(filename, 'w') as file:
            file.write(str(result))

    def test_anagram_case1(self):
        s, t = self.read_input('/home/user/cyber/VSCodeProject/esercizi/Lezione15/test_input1.txt')
        result = anagram(s, t)
        self.write_output('test_output1.txt', result)
        self.assertTrue(result)

    def test_anagram_case2(self):
        s, t = self.read_input('/home/user/cyber/VSCodeProject/esercizi/Lezione15/test_input2.txt')
        result = anagram(s, t)
        self.write_output('test_output2.txt', result)
        self.assertFalse(result)

    def test_anagram_case3(self):
        s, t = self.read_input('/home/user/cyber/VSCodeProject/esercizi/Lezione15/test_input3.txt')
        result = anagram(s, t)
        self.write_output('/home/user/cyber/VSCodeProject/esercizi/Lezione15/test_output3.txt', result)
        self.assertTrue(result)

    def test_anagram_case4(self):
        s, t = self.read_input('/home/user/cyber/VSCodeProject/esercizi/Lezione15/test_input4.txt')
        result = anagram(s, t)
        self.write_output('test_output4.txt', result)
        self.assertFalse(result)

    def test_anagram_case5(self):
        s, t = self.read_input('test_input5.txt')
        result = anagram(s, t)
        self.write_output('test_output5.txt', result)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()