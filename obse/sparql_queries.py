import string
from rdflib import Literal

class SparQLWrapper:

    def __init__(self,graph):
        self.graph = graph

    def get_references(self):
        q = """
            SELECT ?s ?o
            WHERE {
                ?s ?p ?o .
                ?s a ?t1 .
                ?o a ?t2 .
            }
            """

        return [(r['s'],r['o']) for r in self.graph.query(q)]
    
    def get_references_by_type(self,type):
        q = """
            SELECT ?s ?o
            WHERE {
                ?s ?p ?o .
                ?s a ?t1 .
                ?o a ?t2 .
            }
            """

        return [(r['s'],r['o']) for r in self.graph.query(q,initBindings = {'p' : type })]

    def get_type(self,obj):
        q = """
            SELECT ?t
            WHERE {
                ?s a ?t .
            }
            """
        n = [r['t'] for r in self.graph.query(q,initBindings = {'s' : obj })]
        if(len(n) != 1): raise ValueError(f"Not a single result: {n} for {obj}")
        return n[0]

    def get_instances_of_type(self,type):
        q = """
            SELECT ?s
            WHERE {
                ?s a ?t .
            }
            """
        n = [r['s'] for r in self.graph.query(q,initBindings = {'t' : type })]
        return n

    def get_instances(self):
        q = """
            SELECT ?s
            WHERE {
                ?s a ?t .
            }
            """
        n = [r['s'] for r in self.graph.query(q)]
        return n

    def get_object_properties(self,obj,prop):
        q = string.Template("""
            SELECT ?value
            WHERE {
                ?s <$PROP> ?value .
            }
            """).substitute(PROP=prop)

        n = [r['value'] for r in self.graph.query(q,initBindings = {'s' : obj })]
        return list(map(lambda x : x.value, n))
        

    def get_single_object_property(self,obj,prop):

        q = string.Template("""
            SELECT ?value
            WHERE {
                ?s <$PROP> ?value .
            }
            """).substitute(PROP=prop)

        n = [r['value'] for r in self.graph.query(q,initBindings = {'s' : obj })]
        if(len(n) != 1): raise ValueError(f"Not a single result {str(n)} for {obj}")
        if isinstance(n[0],Literal):
            return n[0].value
        return n[0]

    
    def get_in_references(self,obj,prop):
        q = string.Template("""
            SELECT ?s
            WHERE {
                ?s <$PROP> ?o .
                ?s a ?t .
            }
            """).substitute(PROP=prop)

        n = [r['s'] for r in self.graph.query(q,initBindings = {'o' : obj })]
        return n

    def get_out_references(self,obj,prop):
        q = string.Template("""
            SELECT ?o
            WHERE {
                ?s <$PROP> ?o .
                ?o a ?t .
            }
            """).substitute(PROP=prop)

        n = [r['o'] for r in self.graph.query(q,initBindings = {'s' : obj })]
        return n
    def get_single_out_reference(self,obj,prop):
        r = self.get_out_references(obj,prop)
        if(len(r) != 1): raise ValueError(f"Not a single result {str(r)} for {obj}")
        return r[0]

    def get_sequence(self,obj):
        q = """
            SELECT ?o ?ix
            WHERE {
                ?s ?ix ?o .
                ?o a ?t .
            }
            """
        n = [r['o'] for r in sorted(self.graph.query(q,initBindings = {'s' : obj }),key = lambda x : int(x['ix'][44:]))]
        return n
            