from rdflib import Graph
import os

output_dir = "serialised-ontologies"
os.makedirs(output_dir, exist_ok=True)


## SKOS
skos_rdf_graph = Graph()
skos_rdf_graph.parse(
    "https://www.w3.org/2009/08/skos-reference/skos.rdf",
    format="xml" 
)
skos_rdf_graph.serialize(
    destination="serialised-ontologies/skos.ttl",
    format="turtle"
)

# SOSA
sosa_graph = Graph()
sosa_graph.parse("https://raw.githubusercontent.com/w3c/sdw-sosa-ssn/refs/heads/gh-pages/ssn/rdf/ontology/core/sosa-actuation.ttl", format="turtle")
sosa_graph.parse("https://raw.githubusercontent.com/w3c/sdw-sosa-ssn/refs/heads/gh-pages/ssn/rdf/ontology/core/sosa-common.ttl", format="turtle")
sosa_graph.parse("https://raw.githubusercontent.com/w3c/sdw-sosa-ssn/refs/heads/gh-pages/ssn/rdf/ontology/core/sosa-deprecated.ttl", format="turtle")
sosa_graph.parse("https://raw.githubusercontent.com/w3c/sdw-sosa-ssn/refs/heads/gh-pages/ssn/rdf/ontology/core/sosa-observation.ttl", format="turtle")
sosa_graph.parse("https://raw.githubusercontent.com/w3c/sdw-sosa-ssn/refs/heads/gh-pages/ssn/rdf/ontology/core/sosa-sampling.ttl", format="turtle")
sosa_graph.parse("https://raw.githubusercontent.com/w3c/sdw-sosa-ssn/refs/heads/gh-pages/ssn/rdf/ontology/core/sosa.ttl", format="turtle")
sosa_graph.serialize(
    destination="serialised-ontologies/sosa-editors-edition.ttl",
    format="turtle"
)

# SSN
ssn_graph = Graph()
ssn_graph.parse("https://raw.githubusercontent.com/w3c/sdw-sosa-ssn/refs/heads/gh-pages/ssn/rdf/ontology/core/ssn-actuation.ttl", format="turtle")
ssn_graph.parse("https://raw.githubusercontent.com/w3c/sdw-sosa-ssn/refs/heads/gh-pages/ssn/rdf/ontology/core/ssn-common.ttl",format="turtle")
ssn_graph.parse("https://raw.githubusercontent.com/w3c/sdw-sosa-ssn/refs/heads/gh-pages/ssn/rdf/ontology/core/ssn-deprecated.ttl",format="turtle")
ssn_graph.parse("https://raw.githubusercontent.com/w3c/sdw-sosa-ssn/refs/heads/gh-pages/ssn/rdf/ontology/core/ssn-observation.ttl",format="turtle")
ssn_graph.parse("https://raw.githubusercontent.com/w3c/sdw-sosa-ssn/refs/heads/gh-pages/ssn/rdf/ontology/core/ssn-sampling.ttl",format="turtle")
ssn_graph.parse("https://raw.githubusercontent.com/w3c/sdw-sosa-ssn/refs/heads/gh-pages/ssn/rdf/ontology/core/ssn.ttl",format="turtle")
sosa_ssn_graph = sosa_graph + ssn_graph
sosa_ssn_graph.serialize(
    destination="serialised-ontologies/sosa-ssn-editors-edition.ttl",
    format="turtle"
)

# Hydra (the official ttl link is broken so serialising the json-ld into ttl)
hydra = Graph()
hydra.parse("https://www.hydra-cg.com/spec/latest/core/core.jsonld", format="json-ld")
hydra.serialize(
    destination="serialised-ontologies/hydra-core-vocabulary.ttl",
    format="turtle"
)

# FOAF
foaf = Graph()
foaf.parse("https://xmlns.com/foaf/spec/20140114.rdf", format="xml")
foaf.serialize(
    destination="serialised-ontologies/foaf.ttl",
    format="turtle"
)
