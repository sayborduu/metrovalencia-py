from metrovalencia.resources.v2.incidencias import Incidencias as IncidenciasV2


class V2Client:
    def __init__(self, http):
        self.incidencias = IncidenciasV2(http)