from rdflib import Graph, Literal, RDF, RDFS, URIRef, BNode, Seq
from rdflib.namespace import XSD
from .namespace import MBA


def type_str(rdf_type: URIRef) -> str:
    s = str(rdf_type)
    return s.split("#")[1]


def create_ref(rdf_type: URIRef, name: str) -> URIRef:
    identifier = type_str(rdf_type) + "-"+name.replace(" ", "-").replace("\\", "-")
    return URIRef(MBA.URL+"#"+identifier)


class GraphWrapper:

    def __init__(self, graph: Graph):
        self.graph = graph

    def add_bnode(self, rdf_type: URIRef) -> URIRef:
        rdf_object = BNode()
        self.graph.add((rdf_object, RDF.type, rdf_type))
        return rdf_object

    def add_named_instance(self, rdf_type: URIRef, name: str, unique_name: str = None) -> URIRef:
        if unique_name is None:
            unique_name = name
        rdf_object = create_ref(rdf_type, unique_name)
        self.graph.add((rdf_object, RDF.type, rdf_type))
        self.graph.add((rdf_object, MBA.name, Literal(name, datatype=XSD.string)))
        return rdf_object

    def add_instance(self, rdf_type: URIRef, name: str, unique_name: str = None) -> URIRef:
        if unique_name is None:
            unique_name = name
        rdf_object = create_ref(rdf_type, unique_name)
        self.graph.add((rdf_object, RDF.type, rdf_type))
        return rdf_object

    def add_labeled_instance(self, rdf_type: URIRef, name: str, unique_name: str = None) -> URIRef:
        if unique_name is None:
            unique_name = name
        rdf_object = create_ref(rdf_type, unique_name)
        self.graph.add((rdf_object, RDF.type, rdf_type))
        self.graph.add((rdf_object, RDFS.label, Literal(name, datatype=XSD.string)))
        return rdf_object

    def add_type(self, rdf_type: URIRef, rdf_object: URIRef):
        self.graph.add((rdf_object, RDF.type, rdf_type))

    def add_sequence(self, name: str) -> URIRef:
        rdf_object = create_ref(RDF.Seq, name)
        self.graph.add((rdf_object, RDF.type, RDF.Seq))
        return rdf_object

    def add_sequence_to(self, rdf_object: URIRef) -> Seq:
        return Seq(self.graph, rdf_object)

    def add_reference(self, reference_type: URIRef, source: URIRef, target: URIRef) -> None:
        self.graph.add((source, reference_type, target))

    def add_str_property(self, property_type: URIRef, source: URIRef, value: str) -> None:
        self.graph.add((source, property_type, Literal(value, datatype=XSD.string)))

    def add_integer_property(self, property_type: URIRef, source: URIRef, value: int) -> None:
        self.graph.add((source, property_type, Literal(value, datatype=XSD.integer)))

    def add_bool_property(self, property_type: URIRef, source: URIRef, value: bool) -> None:
        self.graph.add((source, property_type, Literal(value, datatype=XSD.boolean)))

    def add_url_property(self, property_type: URIRef, source: URIRef, value: str) -> None:
        self.graph.add((source, property_type, URIRef(value)))
