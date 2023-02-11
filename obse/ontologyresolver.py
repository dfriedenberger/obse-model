from rdflib import Graph
import string
import pkgutil

class OntologyResolver:

    def __init__(self,path):
        self.graph = Graph()
        data = pkgutil.get_data(__package__, path)
        self.graph.parse(data)

    def _select_named_type(self,name,type):
        q = string.Template("""
            SELECT DISTINCT ?subject
            WHERE {
            ?subject a $TYPE.
            FILTER( STRENDS(STR(?subject),str(<$NAME>)) )
        }
        """).substitute(NAME = name,TYPE=type)

        n = [r['subject'] for r in self.graph.query(q)]

        if len(n) != 1: raise ValueError(f" not a singleton {n}")

        return n[0]

    def get_class(self,name):
        return self._select_named_type(name,"owl:Class")
        
    def get_object_property(self,name):
        return self._select_named_type(name,"owl:ObjectProperty")
