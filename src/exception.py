
### Ha lo scopo di creare una gestione personalizzata degli errori in Python,
### fornendo messaggi di errore dettagliati, incluso il nome del file, numero di riga e il messaggio dell’errore.

import sys
### Serve per accedere a sys.exc_info(), una funzione che restituisce informazioni sull'eccezione attiva.
import logging

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in Python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))
    
    return error_message

### Ottiene i dettagli dell’eccezione (in particolare la traccia dello stack exc_tb).
### Estrae:
### Il nome del file in cui si è verificato l’errore.
### Il numero di riga.
### Il messaggio di errore.
### Compone un messaggio di errore dettagliato.


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail)
    
    def __str__(self):
        return self.error_message
    
### Cosa fa: è una classe di eccezione personalizzata che estende Exception.
### Alla creazione, usa la funzione error_message_detail() per creare un messaggio d'errore dettagliato.
### Ridefinisce __str__() per restituire questo messaggio personalizzato quando l'eccezione viene stampata.

