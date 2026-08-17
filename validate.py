#!/usr/bin/env python3
"""Validate a rate limits document against rate-limits-json-schema.yml.

Usage:
  python3 validate.py rate-limits-example-1.yml [more.yml ...]

Exits non-zero if any document fails, so it can gate a pipeline.
"""

import os
import sys

try:
    import yaml
    from jsonschema import Draft202012Validator
except ImportError:
    sys.exit("Requires pyyaml and jsonschema:  pip install jsonschema pyyaml")

HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMA_PATH = os.path.join(HERE, "rate-limits-json-schema.yml")


def pick_form(doc, schema):
    """Choose the branch of the document oneOf that this file is trying to be.

    Validating against the oneOf directly reports only "not valid under any of the
    given schemas", which hides the actual mistake. Detecting the intended form first
    means every error points at a real field.
    """
    looks_like_property = (
        isinstance(doc, list)
        and doc
        and isinstance(doc[0], dict)
        and ("data" in doc[0] or doc[0].get("type") == "RateLimits")
    )
    ref = "rateLimitsProperty" if looks_like_property else "rateLimit"
    return {
        "$schema": schema["$schema"],
        "type": "array",
        "minItems": 1,
        "items": {"$ref": f"#/$defs/{ref}"},
        "$defs": schema["$defs"],
    }


def validate(path, schema):
    with open(path) as f:
        doc = yaml.safe_load(f)

    validator = Draft202012Validator(pick_form(doc, schema))
    errors = sorted(validator.iter_errors(doc), key=lambda e: list(e.absolute_path))
    if not errors:
        count = len(doc) if isinstance(doc, list) else 1
        print(f"PASS  {path}  ({count} entries)")
        return True

    print(f"FAIL  {path}  ({len(errors)} errors)")
    for e in errors:
        where = "/".join(str(p) for p in e.absolute_path) or "(root)"
        print(f"      {where}: {e.message}")
    return False


def main(argv):
    if not argv:
        sys.exit(__doc__)

    with open(SCHEMA_PATH) as f:
        schema = yaml.safe_load(f)

    Draft202012Validator.check_schema(schema)

    ok = all([validate(p, schema) for p in argv])
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
