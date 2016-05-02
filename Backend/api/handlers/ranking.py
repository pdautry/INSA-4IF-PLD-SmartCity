from ..py_rest.pyrest.rest_server.rest_api.response import Response
from ..criteria.gen_criteria import rank
from ..criteria.criterias import criterias_dict
import json


def ranking_handler(path, data, api_param):
    """
        TODO : doc
    """
    # extraire les criteres utiles
    d = json.loads(data['data'][0])
    criteres = d['criteres']
    nomcriteres = [k for k, v in criteres.items() if v != 0]
    # evaluer les criteres
    notes = {}
    ret_note = []
    somme = 0
    for i in nomcriteres:
        if criteres[i] == 0 :
            ret_note.append({'name': criterias_dict[i]['realname'], 'note': -1, 'closest': None, 'density': None})
        else :
            spec = {'criteria': criterias_dict[i], 'coordinates': {'lat': d['lat'], 'lon': d['lon']}}
            notes[i], closest, density = rank(spec)
            somme = somme + notes[i] * criteres[i]
            note_finale=notes[i]
            if d['applyCoeff'] == 1 :
                note_finale=criteres[i]*note_finale/10
            ret_note.append({'name': criterias_dict[i]['realname'], 'note': round(note_finale, 2), 'closest': closest, 'density': density})
    # faire une moyenne
    if sum(criteres.values()) != 0:
        moy = somme / sum(criteres.values())
    else:
        moy = 0.0
    # retourner les notes
    ret_data = {'moyenne': round(moy, 2), 'notes': ret_note}
    return Response(api_param).serialized(ret_data)
