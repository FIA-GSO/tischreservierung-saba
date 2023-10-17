import flask
from flask import request   # wird benötigt, um die HTTP-Parameter abzufragen
import sqlite3
from datetime import datetime, timedelta
from datetime import datetime, timedelta

app = flask.Flask(__name__)

app.config["DEBUG"] = True  # Zeigt Fehlerinformationen im Browser, statt nur einer generischen Error-Message




def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/', methods=['POST'])
def tischreservierung():
    conn = sqlite3.connect('schema.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    tische = cur.execute(f'SELECT * FROM tische WHERE anzahlPlaetze >= {request.form.get("anzahlPlaetze")};').fetchall()
    if tische is not None:
        for tisch in tische:
            
            reservierungen  = cur.execute(f'SELECT * FROM reservierungen WHERE tischnummer = {tisch["tischnummer"]};').fetchall()
            belegte_zeiten = []
            for reservierung in reservierungen: 
                belegte_zeiten.append(datetime.strptime(reservierung["zeitpunkt"], "%Y-%m-%d %H:%M:%S"))
            angeforderder_zeitpunkt = is_tisch_verfügbar(request.form.get("start_zeitpunkt"), request.form.get("end_zeitpunkt"), belegte_zeiten)
            if angeforderder_zeitpunkt:
                return f"Du bekommst den Tisch {tisch['tischnummer']} am {angeforderder_zeitpunkt}."
    return "Kein Tisch zurverfügung"

def is_tisch_verfügbar(start_zeitpunkt, end_zeitpunkt, belegte_zeiten):
    start_zeitpunkt = datetime.strptime(start_zeitpunkt, "%Y-%m-%d %H:%M:%S")
    current_time = start_zeitpunkt
    end_zeitpunkt = datetime.strptime(end_zeitpunkt, "%Y-%m-%d %H:%M:%S")

    while current_time <= end_zeitpunkt:
        # Setze die Minuten auf 30
        current_time = current_time.replace(minute=30)
        if current_time not in belegte_zeiten:
            return current_time
        # Füge 1 Stunde zur aktuellen Zeit hinzu
        current_time += timedelta(hours=1)
    return False


if __name__ == '__main__':
    app.run()
