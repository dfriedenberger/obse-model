from rdflib import Graph, URIRef


from obse.graphwrapper import GraphWrapper
from obse.sparql_queries import SparQLWrapper


def test_workflow(tmp_path):

    graph = Graph()

    graph_wrapper = GraphWrapper(graph)
    instance_type = URIRef("https://www.frittenburger.de/test#TestClass")
    graph_wrapper.add_named_instance(instance_type, "test-instance")

    graph.serialize(destination=f"{tmp_path}/model.ttl", format='turtle')

    g = Graph()
    g.parse(f"{tmp_path}/model.ttl")
    graph_wrapper = SparQLWrapper(g)
    instances = graph_wrapper.get_instances()

    assert len(instances) == 1
