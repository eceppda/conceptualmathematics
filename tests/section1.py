import pytest

from conceptual_mathematics import all_maps, same_mapping_rule

A = ['John', 'Mary', 'Sam']
B = ['eggs', 'coffee']

R1 = {'John': 'eggs', 'Mary': 'coffee', 'Sam': 'coffee'}
R2 = {'John': 'coffee', 'Mary': 'coffee', 'Sam': 'coffeee'}


@pytest.mark.parametrize('domain, codomain, expected_count', [
    (A, B, 8),
    (A, A, 27),
    (B, A, 9),
    (B, B, 4)])
def test_exercises(domain, codomain, expected_count):
    """How many different maps f are there with domain A and codomain B?"""
    assert len(all_maps(domain=domain, codomain=codomain)) == expected_count


@pytest.mark.parametrize('domain, rule1, rule2', [
    (A, R1, R2)
])
def test_exercises2(domain, rule1, rule2):
    assert same_mapping_rule(domain, rule1, rule2)
