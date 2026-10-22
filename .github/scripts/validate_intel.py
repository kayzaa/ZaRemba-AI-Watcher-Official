"""Quality gate for intel/threats.json (mirrors ThreatIntel::validate in the app).
A feed with any problem is not signed, so it never reaches users."""
import json, re, sys

feed = json.load(open(sys.argv[1]))
problems = []
if feed.get("schema") != 1:
    problems.append("unsupported schema")
if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(feed.get("updated", ""))):
    problems.append("'updated' must be YYYY-MM-DD")
ids, keys = set(), set()
for e in feed.get("entries", []):
    at = f"{e.get('id')} ({e.get('name')})"
    if not str(e.get("id", "")).startswith("ZRW-INTEL-") or e["id"] in ids:
        problems.append(f"{at}: id must be unique and start with ZRW-INTEL-")
    ids.add(e.get("id"))
    if e.get("kind") not in ("npm_package", "pypi_package", "agent_skill"):
        problems.append(f"{at}: unknown kind")
    name = str(e.get("name", ""))
    if not name.strip() or re.search(r"\s", name) or len(name) > 214:
        problems.append(f"{at}: invalid name")
    key = (e.get("kind"), name, tuple(e.get("versions", [])))
    if key in keys:
        problems.append(f"{at}: duplicate entry")
    keys.add(key)
    if not str(e.get("reference", "")).startswith("https://"):
        problems.append(f"{at}: reference must be https://")
    desc = str(e.get("description", ""))
    if len(desc.strip()) < 20:
        problems.append(f"{at}: description too short")
    versions = e.get("versions", [])
    if not versions and not any(w in desc.lower() for w in ("impersonat", "typosquat", "malicious package", "fake", "malware-only")):
        problems.append(f"{at}: empty version list requires an impersonation/typosquat/fake package description")
    if any((not str(v).strip()) or any(c in str(v) for c in "*^~") for v in versions):
        problems.append(f"{at}: versions must be exact")
if problems:
    print("\n".join(problems))
    sys.exit(1)
print(f"OK – {len(feed['entries'])} entries, updated {feed['updated']}")
