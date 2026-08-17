from typing import List, Set
from app.models.result import GuidelineViolation
from app.services.guidelines.prohibited_words import prohibited_checker
from app.services.guidelines.prefix_suffix import prefix_suffix_checker
from app.services.guidelines.periodicity import periodicity_checker
from app.services.guidelines.title_combination import title_combination_checker
from app.services.guidelines.multilingual import multilingual_checker

class GuidelineChecker:
    def evaluate(self, title: str, candidate_titles: List[str], registered_titles_set: Set[str]) -> List[GuidelineViolation]:
        """Runs all PRGI guideline checks against a submitted title."""
        violations = []
        
        # 1. Prohibited words check
        pw_violations = prohibited_checker.check(title)
        for code, msg, details in pw_violations:
            violations.append(GuidelineViolation(code=code, message=msg, details=details))

        # 2. Disallowed Prefix/Suffix check
        ps_violations = prefix_suffix_checker.check(title, candidate_titles)
        for code, msg, details in ps_violations:
            violations.append(GuidelineViolation(code=code, message=msg, details=details))

        # 3. Periodicity modification check
        per_violations = periodicity_checker.check(title, candidate_titles)
        for code, msg, details in per_violations:
            violations.append(GuidelineViolation(code=code, message=msg, details=details))

        # 4. Title Combination check
        tc_violations = title_combination_checker.check(title, registered_titles_set)
        for code, msg, details in tc_violations:
            violations.append(GuidelineViolation(code=code, message=msg, details=details))

        # 5. Multilingual Semantic match check
        multi_violations = multilingual_checker.check(title, candidate_titles)
        for code, msg, details in multi_violations:
            violations.append(GuidelineViolation(code=code, message=msg, details=details))

        return violations

guideline_engine = GuidelineChecker()
