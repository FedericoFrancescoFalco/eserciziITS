 #Si definisca una nuova classe Pagamento che contiene un attributo privato e di tipo float che memorizza l'importo del pagamento 
 #e si definiscano appropriati metodi get() e set(). L'importo non è un parametro da passare in input alla classe Pagamento 
 #ma deve essere inizializzato utilizzando il metodo set() dove opportuno. Si crei inoltre un metodo dettagliPagamento() 
 # che visualizza una frase che descrive l'importo del pagamento, ad esempio: "Importo del pagamento: €20.00". 
 # Quando viene stampato, l'importo è sempre con 2 cifre decimali.

#Successivamente, si definisca una classe PagamentoContanti che sia derivata da Pagamento e definisca l'importo. 
#Questa classe dovrebbe ridefinire il metodo dettagliPagamento() per indicare che il pagamento è in contanti. 
# Si definisca inoltre il metodo inPezziDa() che stampa a schermo quante banconote da 500 euro, 200 euro, 100 euro, 50 euro, 20 euro, 10 euro,
#  5 euro e/o in quante monete da 2 euro, 1 euro, 0,50 euro, 0,20 euro, 0,10 euro, 0,05 euro, 0,01 euro sono necessarie per pagare l'importo 
# in contanti.

#Si definisca una classe PagamentoCartaDiCredito derivata anch'essa da Pagamento e che definisce l'importo. 
#Questa classe deve contenere gli attributi per il nome del titolare della carta, la data di scadenza, e il numero della carta di credito. 
# si ridefinisca il metodo dettagliPagamento() per includere tutte le informazioni della carta di credito oltre all'importo del pagamento.

#Per il test, si creino almeno due oggetti di tipo PagamentoContanti e due di tipo PagamentoCartaDiCredito con valori differenti e si invochi 
# dettagliPagamento() per ognuno di essi.


class Pagamento:
    def __init__(self):
        self.__importo: float = 0.0

    def get(self):
        return self.__importo

    def set(self, importo: float):
        self.__importo = importo

    def dettagliPagamento(self):
        importo_formattato = "{:.2f}".format(self.__importo)
        print(f"Importo del pagamento: €{importo_formattato}")

class PagamentoContanti(Pagamento):
    def dettagliPagamento(self):
        importo_formattato = "{:.2f}".format(self.get())
        print(f"Importo del pagamento in contanti: €{importo_formattato}")
    
    def inPezziDa(self):
        importo = self.get()
        pezzi = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.01]
        result = {}
        
        for pezzo in pezzi:
            count = int(importo // pezzo)
            if count > 0:
                result[pezzo] = count
                importo -= count * pezzo
                importo = round(importo, 2)  
        
        print("Pezzi necessari per il pagamento:")
        for pezzo, count in result.items():
            print(f"€{pezzo}: {count} pezzi")

class PagamentoCartaDiCredito(Pagamento):
    def __init__(self):
        super().__init__()
        self.nome_titolare: str = ""
        self.data_scadenza: str = ""
        self.numero_carta: str = ""

    def set_dettagli_carta(self, nome_titolare: str, data_scadenza: str, numero_carta: str):
        self.nome_titolare = nome_titolare
        self.data_scadenza = data_scadenza
        self.numero_carta = numero_carta

    def dettagliPagamento(self):
        importo_formattato = "{:.2f}".format(self.get())
        print(f"Importo del pagamento con carta di credito: €{importo_formattato}")
        print(f"Nome titolare: {self.nome_titolare}")
        print(f"Data di scadenza: {self.data_scadenza}")
        print(f"Numero carta di credito: {self.numero_carta}")

# serie di test 
pagamento_contanti1 = PagamentoContanti()
pagamento_contanti1.set(1234.56)
pagamento_contanti1.dettagliPagamento()
pagamento_contanti1.inPezziDa()

pagamento_contanti2 = PagamentoContanti()
pagamento_contanti2.set(789.01)
pagamento_contanti2.dettagliPagamento()
pagamento_contanti2.inPezziDa()

pagamento_carta1 = PagamentoCartaDiCredito()
pagamento_carta1.set(567.89)
pagamento_carta1.set_dettagli_carta("Mario Rossi", "12/24", "1234 5678 9876 5432")
pagamento_carta1.dettagliPagamento()

pagamento_carta2 = PagamentoCartaDiCredito()
pagamento_carta2.set(432.10)
pagamento_carta2.set_dettagli_carta("Giulia Bianchi", "08/25", "9876 5432 1234 5678")
pagamento_carta2.dettagliPagamento()
