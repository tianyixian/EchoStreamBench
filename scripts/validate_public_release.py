from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / 'manifest.json').read_text(encoding='utf-8'))
items = manifest['items']
assert manifest['total_items'] == 657 and len(items) == 657
assert len({x['public_id'] for x in items}) == 657
assert sum(x['eval_mode'] == 'mcq_letter' for x in items) == 647
assert sum(x['eval_mode'] != 'mcq_letter' for x in items) == 10
answer_fields = {'gold_' + 'label', 'pred' + 'iction', 'cor' + 'rect'}
for x in items:
    assert answer_fields.isdisjoint(x)
    text = json.dumps(x, ensure_ascii=False)
    assert ('/' + 'inspire/') not in text and ('C:' + '\\Users\\') not in text and ('D:' + '\\') not in text
    assert not re.search(r'(?i)(pass' + 'word|api[_-]?key|sec' + 'ret)', text)
    assert x['question']
    assert isinstance(x['options'], list)

answer_path = ROOT / 'answers' / 'answers.jsonl'
answer_manifest = json.loads((ROOT / 'answers' / 'answers_manifest.json').read_text(encoding='utf-8'))
answer_rows = [json.loads(line) for line in answer_path.read_text(encoding='utf-8').splitlines() if line.strip()]
assert len(answer_rows) == 657
assert len({x['public_id'] for x in answer_rows}) == 657
assert sum(x['eval_mode'] == 'mcq_letter' for x in answer_rows) == 647
assert sum(x['eval_mode'] == 'openqa_free_text' for x in answer_rows) == 10
assert {x['public_id'] for x in answer_rows} == {x['public_id'] for x in items}
manifest_by_id = {x['public_id']: x for x in items}
for answer in answer_rows:
    assert set(answer) == {'public_id', 'eval_mode', 'answer', 'question_sha256'}
    item = manifest_by_id[answer['public_id']]
    assert answer['eval_mode'] == item['eval_mode']
    assert answer['question_sha256'] == item['question_sha256']
    assert answer['answer']
    if answer['eval_mode'] == 'mcq_letter':
        assert re.fullmatch(r'[A-E]', answer['answer'])
    text = json.dumps(answer, ensure_ascii=False)
    assert ('/' + 'inspire/') not in text and ('C:' + '\\Users\\') not in text and ('D:' + '\\') not in text
assert answer_manifest['answer_key_included'] is True
assert answer_manifest['total_items'] == 657
assert answer_manifest['mcq_items'] == 647
assert answer_manifest['openqa_items'] == 10
import hashlib
assert hashlib.sha256(answer_path.read_bytes()).hexdigest() == answer_manifest['answer_file_sha256']
for path in ROOT.rglob('*'):
    if path.is_file() and path.name != 'SHA256SUMS.txt' and path.suffix in {'.json', '.md', '.csv'}:
        text = path.read_text(encoding='utf-8', errors='ignore')
        assert ('/' + 'inspire/') not in text and ('C:' + '\\Users\\') not in text and ('D:' + '\\paper2_') not in text
print('PUBLIC_RELEASE_VALIDATION_PASS', len(items), 'items', 'answers', len(answer_rows))
