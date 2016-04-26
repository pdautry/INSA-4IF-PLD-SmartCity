from .gen_criteria import gen_criteria

class le_administration_psd(gen_criteria): 
    MAX_DIST = 1500.0 # meters

    def rank(self, coord):
        records = get_criteria('le_administration_psd')
        dist, record = closest_record(records, coord)
        mark = 10.0 * (1.0 - (min(dist, le_administration_psd.MAX_DIST)/le_administration_psd.MAX_DIST))
        return mark
       