"""
IGC Parser

Specification can be found here
http://carrier.csi.cam.ac.uk/forsterlewis/soaring/igc_file_format/igc_format_2008.html
"""
import datetime


class IGCParser:
    def pfx_fix_record(self, line):
        """Turns a B IGC Record into lat/long/alt data"""
        assert(len(line) >= len("BHHMMSSDDMMmmmNDDDMMmmmEA0000000000"))
        time = datetime.strptime(line[1:7], "%H%M%S")
        lat = line[8:14]
        long = line[15:23]
        valid_fix = (line[24] == "A")
        baro_alt = int(line[25:30])
        gps_alt = int(line[31:35])
        return dict(time=time, lat=lat, long=long, valid=valid_fix, baro_alt=baro_alt, gps_alt=gps_alt)

    prefixes = {
        "B": pfx_fix_record,
    }


    def parse(self, filename):
        lines = open(filename, "r").readlines()
        data = []
        for line in lines:
            for key in self.prefixes.keys():
                if line.startswith(key):
                    data.append(self.prefixes[key](line))
