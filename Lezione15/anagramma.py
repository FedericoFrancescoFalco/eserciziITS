
class Anagram:
    def anagram(s: str, t: str) -> bool:
    # Converte entrambe le stringhe in minuscolo e poi le ordina
    # Confronta le versioni ordinate delle due stringhe
    # Ritorna True se sono uguali, False altrimenti
        return sorted(s.lower()) == sorted(t.lower())
    print(anagram("anagram","nagaram"))
    print(anagram("rat", "car"))
    print(anagram("silent","listen"))
    print(anagram("NeurIPS","UniReps"))
    print("\n")