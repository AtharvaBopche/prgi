from app.services.guidelines.prohibited_words import prohibited_checker
from app.services.guidelines.title_combination import title_combination_checker
from app.services.guidelines.periodicity import periodicity_checker

def test_prohibited_words():
    violations = prohibited_checker.check("Police News")
    assert len(violations) > 0
    assert violations[0][0] == "ERR_DISALLOWED_WORD"

def test_title_combination():
    registered = {"HINDU", "INDIAN EXPRESS"}
    violations = title_combination_checker.check("Hindu Indian Express", registered)
    assert len(violations) > 0
    assert violations[0][0] == "ERR_TITLE_COMBINATION"

def test_periodicity_modification():
    candidates = ["ABC NEWS"]
    violations = periodicity_checker.check("ABC Daily News", candidates)
    assert len(violations) > 0
    assert violations[0][0] == "ERR_PERIODICITY_MODIFICATION"
