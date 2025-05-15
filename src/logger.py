### Crea una cartella logs nella directory corrente se non esiste.
### Genera un file .log con data e ora nel nome.
### Configura il logging in modo da scrivere messaggi dettagliati lì dentro.
### Se esegui lo script, scrive una riga nel log con un messaggio di test.

import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "logs")
os.makedirs(log_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    
)
### Salva i log nel file specificato.
### Definisce il formato del messaggio di log.
### Imposta il livello di log a INFO (cioè registra info, warning, errori, ecc.)

### if __name__=="__main__":
###    logging.info("Logging has started")   
    
### Serve per testare il logging se il file è eseguito direttamente, scrive nel log la riga Logging has started