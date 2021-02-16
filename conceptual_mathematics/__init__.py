import itertools
from typing import List, Dict


def all_maps(domain: List[str], codomain: List[str]) -> List[Dict[str, str]]:
    """compute all possible mappings from domain to codomain"""
    return [dict(zip(domain, p)) for p in itertools.product(codomain, repeat=len(domain))]


def same_mapping_rule(domain: List[str], rule1: Dict[str, str], rule2: Dict[str, str]):
    return list(rule1.keys()) == domain and list(rule2.keys()) == domain
