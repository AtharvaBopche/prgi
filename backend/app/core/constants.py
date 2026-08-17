# Statuses
STATUS_ACCEPTED = "ACCEPTED"
STATUS_REJECTED = "REJECTED"
STATUS_FLAGGED = "FLAGGED_FOR_REVIEW"

# Guideline Violation Error Codes
ERR_DISALLOWED_WORD = "ERR_DISALLOWED_WORD"
ERR_DISALLOWED_PREFIX = "ERR_DISALLOWED_PREFIX"
ERR_DISALLOWED_SUFFIX = "ERR_DISALLOWED_SUFFIX"
ERR_PERIODICITY_MODIFICATION = "ERR_PERIODICITY_MODIFICATION"
ERR_TITLE_COMBINATION = "ERR_TITLE_COMBINATION"
ERR_MULTILINGUAL_MEANING = "ERR_MULTILINGUAL_MEANING"
ERR_HIGH_SIMILARITY = "ERR_HIGH_SIMILARITY"

# Guideline Violation Messages
MSG_MAP = {
    ERR_DISALLOWED_WORD: "Title contains prohibited official or restricted word(s).",
    ERR_DISALLOWED_PREFIX: "Title uses a disallowed prefix that causes close resemblance to existing titles.",
    ERR_DISALLOWED_SUFFIX: "Title uses a disallowed suffix that causes close resemblance to existing titles.",
    ERR_PERIODICITY_MODIFICATION: "Title modifies an existing registered title by adding periodicity terms (e.g. Daily, Weekly).",
    ERR_TITLE_COMBINATION: "Title is created by combining two or more existing registered titles.",
    ERR_MULTILINGUAL_MEANING: "Title has identical/similar semantic meaning to an existing title in another language.",
    ERR_HIGH_SIMILARITY: "Title is phonetically or structurally too similar to an existing title."
}
