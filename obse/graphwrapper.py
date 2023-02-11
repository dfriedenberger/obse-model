from .namespace import MBA

from rdflib import Graph, Literal, RDF, URIRef
from rdflib.namespace import  XSD 

def type_str(type : URIRef) -> str:
    s = str(type)
    return s.split("#")[1]

def create_ref(type : URIRef,name : str) -> URIRef:
    id = type_str(type) + "-"+name.replace(" ","-")
    return URIRef(MBA.URL+"#"+id)

class GraphWrapper:

    def __init__(self,graph : Graph):
        self.graph = graph

    def add_named_instance(self,type : URIRef,name : str,unique_name : str = None) -> URIRef:
        if unique_name == None: unique_name = name
        rdf_object  = create_ref(type,unique_name)
        self.graph.add((rdf_object, RDF.type, type))
        self.graph.add((rdf_object, MBA.name, Literal(name, datatype=XSD.string)))
        return rdf_object
    
    def add_sequence(self,name : str) -> URIRef:
        rdf_object  = create_ref(RDF.Seq,name)
        self.graph.add((rdf_object, RDF.type, RDF.Seq))
        return rdf_object

    def add_reference(self,type : URIRef,source : URIRef,target : URIRef) -> None:
        self.graph.add((source, type, target))

    def add_str_property(self,type : URIRef,source : URIRef,value : str) -> None:
        self.graph.add((source, type, Literal(value, datatype=XSD.string)))

    def add_url_property(self,type : URIRef,source : URIRef,value : str) -> None:
        self.graph.add((source, type, URIRef(value)))
