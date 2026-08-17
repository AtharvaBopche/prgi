from typing import List, Tuple, Set
from app.core.constants import ERR_TITLE_COMBINATION
from app.services.preprocessing.normalizer import normalize_title

class TitleCombinationChecker:
    def check(self, title: str, registered_titles_set: Set[str]) -> List[Tuple[str, str, str]]:
        """
        Checks whether the title is formed by concatenating two or more existing titles.
        Example: "HINDU" + "INDIAN EXPRESS" -> "HINDU INDIAN EXPRESS"
        """
        violations = []
        norm = normalize_title(title)
        tokens = norm.split()
        
        if len(tokens) < 2:
            return violations

        # Greedy / recursive combination search
        found_combinations = []
        
        def find_splits(remaining_tokens, current_chain):
            if not remaining_tokens:
                if len(current_chain) >= 2:
                    found_combinations.append(list(current_chain))
                return
                
            for i in range(1, len(remaining_tokens) + 1):
                part = " ".join(remaining_tokens[:i])
                if part in registered_titles_set:
                    find_splits(remaining_tokens[i:], current_chain + [part])

        find_splits(tokens, [])
        
        if found_combinations:
            combo = found_combinations[0]
            violations.append((
                ERR_TITLE_COMBINATION,
                f"Title is a combination of existing titles: {' + '.join(combo)}",
                f"Combining registered titles ({', '.join(combo)}) into a single title is prohibited under PRGI rules."
            ))
            
        return violations

title_combination_checker = TitleCombinationChecker()
