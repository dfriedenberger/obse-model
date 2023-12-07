from rdflib.term import URIRef
from rdflib.namespace import DefinedNamespace, Namespace
from .ontologyresolver import OntologyResolver


stateMachineOntology = OntologyResolver("statemachine.ttl")

class MBA(DefinedNamespace):

    """
    Microservice Batch Architecture Definition Language (XSD) 
    Datatypes
    """
    URL = "https://frittenburger.de/2022/11/EULYNX"
    _NS = Namespace(URL+"/Schema#")
    # http://www.w3.org/2000/01/rdf-schema#Class

    #IPO model
    Subsystem: URIRef
    Interface: URIRef
    Component: URIRef

    #Message: URIRef
    Property: URIRef

    # Configuration
    Secret: URIRef

    #StateMachine
    StateMachine: URIRef = stateMachineOntology.get_class('#StateMachine')
    State: URIRef = stateMachineOntology.get_class('#State')
    FinalState: URIRef = stateMachineOntology.get_class('#FinalState')
    PseudoState: URIRef = stateMachineOntology.get_class('#PseudoState')
    InitialState: URIRef = stateMachineOntology.get_class('#InitialState')
    Junction: URIRef = stateMachineOntology.get_class('#Junction')


    Transition: URIRef = stateMachineOntology.get_class('#Transition')

    ## statemachine properties
    guard: URIRef

    ## statemachine relations
    source: URIRef = stateMachineOntology.get_object_property("#source")
    target: URIRef = stateMachineOntology.get_object_property("#target")


    # http://www.w3.org/1999/02/22-rdf-syntax-ns#Property
    name: URIRef #All Objects have names
    datatype: URIRef


    # general relations
    has: URIRef
    
    # Messages
    structure: URIRef
    #hasRecipient: URIRef
    #hasSender: URIRef



    ## interface relations
    #provides: URIRef
    #requires: URIRef

    # C3 Level relations
    #contains: URIRef
    use: URIRef

    # C3 Level properties
    #pattern: URIRef

    # C3 Level / Library properties
    #target_path: URIRef
    #project_ref: URIRef

    # Implementation relations
    #implement: URIRef
    portnumber: URIRef


