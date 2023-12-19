# obse
Ontology Based System Engineering


## Installation

```bash
pip install obse
```

## Installation for development purposes
```
pip install -e .   
```

## Usage

### create Graph
```
from rdflib import Graph, URIRef
from obse.graphwrapper import GraphWrapper


graph = Graph()

graph_wrapper = GraphWrapper(graph)
instance_type = URIRef("https://www.frittenburger.de/test#TestClass")
graph_wrapper.add_named_instance(instance_type, "test-instance")

graph.serialize(destination="model.ttl, format='turtle')
```

### read Graph
```
from rdflib import Graph, URIRef
from obse.sparql_queries import SparQLWrapper


graph = Graph()
graph.parse("model.ttl")
graph_wrapper = SparQLWrapper(graph)
instances = graph_wrapper.get_instances()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Authors and acknowledgment

- For readme file I used format from https://www.makeareadme.com/

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
