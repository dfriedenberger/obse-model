from obse.graphwrapper import GraphWrapper
from rdflib import Graph, URIRef


def test_01():
    graph = Graph()
    graph_wrapper = GraphWrapper(graph)
    instance_type = URIRef("https://www.frittenburger.de/test#TestClass")
    graph_wrapper.add_named_instance(instance_type, "test-instance")

    assert len(graph) == 2
