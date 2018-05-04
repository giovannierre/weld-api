# Definisco una classe QualificationRange con proprietà generali che mi servirà per definire delle sottoclassi
# per le varie normative e situazioni, ad esempio: QualificationRangePqrIso, QualificationRangePqrASME,
# QualificationRangeWpqISO, QualificationRangeWpqASME, ...
# In questo modo le proprietà comuni le definisco una volta sola e nelle sottoclassi andrò a definire eventualmente 
# solo proprietà aggiuntive.
# Tenere a mente che si può applicare sia a Procedimenti che a Saldatori/Operatori.
# In linea di principio il QualificationRange non è necessario che sia memorizzato in una tabella, perchè può 
# essere calcolato ogni volta all'occorrenza, se memorizzarlo o meno in una tabella andrà deciso sulla base di 
# considerazioni di prestazioni.
# Lo definisco comunque subito come modello (cioè tabella) in modo da poterlo sfruttare su database, se deciderò
# di non memorizzare i dati, semplicement la tabella rimarrà vuota

from db import db

class QualificationRange(db.Model):
    __tablename__ = 'qualification_range'
    
    id = db.Column(db.Integer, primary_key=True)
    
    # Thickness range for base material, case buttweld(bw) single layer (sl) and multi layer (ml)
    # Attenzione: bisogna prendere in considerazione anche il caso di materiali di spessore dissimile, ad esempio
    # la nuova ISO 15614-1:2017 dice che nel caso di saldatura di spessori dissimili, lo spessore della parte più
    # spessa è illimitato purchè la prova di qualifica sia stata effettuata su uno spessore di almeno 30 mm.
    # Per tenere conto di questo ho impostato un campo 'max2' che vorrebbe esprimere lo spessore max del secondo materiale
    bm_thk_range_bw_sl_min = db.Column(db.Decimal(precision=2))
    bm_thk_range_bw_sl_max = db.Column(db.Decimal(precision=2))
    bm_thk_range_bw_sl_max2 = db.Column(db.Decimal(precision=2)) # spessore della parte più spessa nel caso di spessori dissimili
    bm_thk_range_bw_ml_min = db.Column(db.Decimal(precision=2))
    bm_thk_range_bw_ml_max = db.Column(db.Decimal(precision=2))
    bm_thk_range_bw_ml_max2 = db.Column(db.Decimal(precision=2)) # spessore della parte più spessa nel caso di spessori dissimili
    bm_thk_range_bw = db.Column(db.String(150)) # range esposto in forma verbale
    # Attenzione! bisogna aggiungere il caso di impact test (limitazioni sullo spessore)
    
    # Thickness range for filler metal, normally only an upper value is specified
    # It is considered a welding process composed of n.3 single processes at most
    fm1_thk_range_bw_max = db.Column(db.Decimal(precision=2))
    fm2_thk_range_bw_max = db.Column(db.Decimal(precision=2))
    fm3_thk_range_bw_max = db.Column(db.Decimal(precision=2))
    
    
    def __init__(self, qualification_test):
        # 'qualification_test' è un oggetto della classe QualificationTest che definisce le caratteristiche
        # del tallone di saldatura
        self.qualification_test = qualification_test
    
    