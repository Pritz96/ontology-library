from rdflib import Graph

skos_rdf_graph = Graph()

skos_rdf_graph.parse(
    "https://www.w3.org/2009/08/skos-reference/skos.rdf",
    format="xml" 
)

skos_rdf_graph.serialize(
    destination="skos.ttl",
    format="turtle"
)

sosa_ssn_graph = Graph()

# Load SOSA
sosa_ssn_graph.parse("https://raw.githubusercontent.com/w3c/sdw-sosa-ssn/refs/heads/gh-pages/ssn/rdf/ontology/core/sosa-actuation.ttl", format="turtle")
sosa_ssn_graph.parse("https://raw.githubusercontent.com/w3c/sdw-sosa-ssn/refs/heads/gh-pages/ssn/rdf/ontology/core/sosa-common.ttl", format="turtle")
sosa_ssn_graph.parse("https://raw.githubusercontent.com/w3c/sdw-sosa-ssn/refs/heads/gh-pages/ssn/rdf/ontology/core/sosa-deprecated.ttl", format="turtle")
sosa_ssn_graph.parse("https://raw.githubusercontent.com/w3c/sdw-sosa-ssn/refs/heads/gh-pages/ssn/rdf/ontology/core/sosa-observation.ttl", format="turtle")
sosa_ssn_graph.parse("https://raw.githubusercontent.com/w3c/sdw-sosa-ssn/refs/heads/gh-pages/ssn/rdf/ontology/core/sosa-sampling.ttl", format="turtle")
sosa_ssn_graph.parse("https://raw.githubusercontent.com/w3c/sdw-sosa-ssn/refs/heads/gh-pages/ssn/rdf/ontology/core/sosa.ttl", format="turtle")

# Load SSN
sosa_ssn_graph.parse("https://raw.githubusercontent.com/w3c/sdw-sosa-ssn/refs/heads/gh-pages/ssn/rdf/ontology/core/ssn-actuation.ttl", format="turtle")
sosa_ssn_graph.parse("https://raw.githubusercontent.com/w3c/sdw-sosa-ssn/refs/heads/gh-pages/ssn/rdf/ontology/core/ssn-common.ttl",format="turtle")
sosa_ssn_graph.parse("https://raw.githubusercontent.com/w3c/sdw-sosa-ssn/refs/heads/gh-pages/ssn/rdf/ontology/core/ssn-deprecated.ttl",format="turtle")
sosa_ssn_graph.parse("https://raw.githubusercontent.com/w3c/sdw-sosa-ssn/refs/heads/gh-pages/ssn/rdf/ontology/core/ssn-observation.ttl",format="turtle")
sosa_ssn_graph.parse("https://raw.githubusercontent.com/w3c/sdw-sosa-ssn/refs/heads/gh-pages/ssn/rdf/ontology/core/ssn-sampling.ttl",format="turtle")
sosa_ssn_graph.parse("https://raw.githubusercontent.com/w3c/sdw-sosa-ssn/refs/heads/gh-pages/ssn/rdf/ontology/core/ssn.ttl",format="turtle")

sosa_ssn_graph.serialize(
    destination="sosa-ssn-editors-edition.ttl",
    format="turtle"
)

# Load and serialise hydra json-ld into turtle as the turtle link is broken
hydra = Graph()
hydra.parse("https://www.hydra-cg.com/spec/latest/core/core.jsonld", format="json-ld")
hydra.serialize(
    destination="hydra.ttl",
    format="turtle"
)
