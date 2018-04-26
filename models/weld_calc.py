from flask import jsonify

class Pqr():
    
    def __init__ (self, test_thickness):
        self.test_thickness = test_thickness

    def bw_thickness_range(self):
        t = self.test_thickness
        if t <= 3:
            thk_min_sl = 0.7*t  # sl= single layer
            thk_max_sl = 1.3*t
            thk_min_ml = 0.7*t  # ml= multi layer
            thk_max_ml = 2*t
        elif t>3 and t<=12:
            thk_min_sl = max(0.5*t, 3.0)
            thk_max_sl = 1.3*t
            thk_min_ml = 3.0
            thk_max_ml = 2*t
        elif t>12 and t<=100:
            thk_min_sl = 0.5*t
            thk_max_sl = 1.1*t
            thk_min_ml = 0.5*t
            thk_max_ml = 2*t
        elif t>100:
            thk_min_sl = -1     # -1 equivale a un messaggio di errore, in questo caso la tabella della norma prevede 'n.a.'
            thk_max_sl = -1
            thk_min_ml = 50
            thk_max_ml = 2*t
    
        response = {
            "thk_min_sl": round(thk_min_sl, 2) ,
            "thk_max_sl": round(thk_max_sl, 2),
            "thk_min_ml": round(thk_min_ml, 2),
            "thk_max_ml": round(thk_max_ml, 2),
            "thk_range_verbose": "Single layer: from {} to {}. Multi layer: from {} to {}.".format(
                round(thk_min_sl,2), round(thk_max_sl,2), round(thk_min_ml,2), round(thk_max_ml,2))
        }
        
        return response
