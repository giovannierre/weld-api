from flask_restful import Resource
from models.weld_calc import Pqr
from flask_restful import reqparse


class PqrRange(Resource):
    # definisco un oggetto parser
    # e lo metto nella classe in modo che sia disponibile a tutti i metodi
    parser = reqparse.RequestParser() # definisce un oggetto parser
    # nota: il parser così definito recepisce automaticamente la request (il json payload) passata dall'utente con il metodo post o altri metodi
    
    # definisco gli argomenti del parser
    parser.add_argument('test_thickness',
        type=float,
        required=True,
        help="This field cannot be left blank")
        
    parser.add_argument('response_type',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    
    # Attenzione: visto che parser appartiene alla definizione della classe e
    # non all'oggetto di classe (se no sarebbe definito come self.parser),
    # quando lo richiamo devo specificare anche la classe, quindi:
    # data = Item.parser.parse_args()

    def post(self):

        data = self.parser.parse_args()
        
        pqr=Pqr(data['test_thickness'])
        
        if data["response_type"] == 'bw_thickness_range':
            return pqr.bw_thickness_range()
        else:
            return {'message': 'response_type not recognized'}
