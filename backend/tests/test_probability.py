from app.services.probability.calculator import calculate_verification_probability
from app.models.result import GuidelineViolation

def test_probability_calculation():
    # 80% similarity -> Probability <= 20%
    prob, status, summary = calculate_verification_probability(80.0, [])
    assert prob == 20.0
    assert status == "REJECTED"

def test_guideline_violation_probability():
    v = [GuidelineViolation(code="ERR_DISALLOWED_WORD", message="Prohibited word")]
    prob, status, summary = calculate_verification_probability(10.0, v)
    assert prob == 0.0
    assert status == "REJECTED"
