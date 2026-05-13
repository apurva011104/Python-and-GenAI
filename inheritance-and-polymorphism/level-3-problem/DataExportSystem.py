class Exporter:
    def export(self, data):
        pass


class CSVExporter(Exporter):
    def export(self, data):
        print("Exporting data as CSV...")


class JSONExporter(Exporter):
    def export(self, data):
        print("Exporting data as JSON...")


class XMLExporter(Exporter):
    def export(self, data):
        print("Exporting data as XML...")


for e in [CSVExporter(), JSONExporter()]:
    e.export({"name": "Alex"})
