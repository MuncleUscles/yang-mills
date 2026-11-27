"""Exercise the same pinned proof checker as a signed research contribution."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

problem = Path(sys.argv[1]).resolve()
config = json.loads((problem / '.open-math/open.json').read_text())
policy = problem / config['policy']['path']
repo_head = subprocess.check_output(['git', '-C', problem, 'rev-parse', 'HEAD'], text=True).strip()
tools_head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
assert tools_head == config['protocol']['commit']
assert hashlib.sha256(policy.read_bytes()).hexdigest() == config['policy']['sha256']

def check(directory, proof, valid):
    artifact = directory / 'positive-bound.json'
    artifact.write_text(json.dumps({
        'version': 2, 'imports': [], 'dependencies': [], 'theorem': 'MassGap.positive',
        'source': 'namespace MassGap\ntheorem positive (gap energy : Nat) (h : 0 < gap) '
                  '(bound : gap ≤ energy) : 0 < energy := ' + proof + '\nend MassGap\n',
    }, indent=2, ensure_ascii=False) + '\n')
    result = subprocess.run([
        sys.executable, 'scripts/verify_open.py', str(artifact), '--policy', str(policy),
        '--policy-hash', config['policy']['sha256'], '--head', repo_head, '--base', repo_head,
        '--protocol-commit', tools_head, '--repository', config['repository'],
    ], capture_output=True, text=True)
    report = json.loads(result.stdout)
    if valid:
        assert result.returncode == 0 and report['production_verified'] is True, report
        print('Verified positive-bound implication with', ', '.join(report['full_kernel']['checker_set']), flush=True)
    else:
        assert result.returncode == 1 and report['production_verified'] is False, report
        assert any(word in report['error'].lower() for word in ('sorry', 'axiom', 'warning')), report
        print('Rejected incomplete proof.', flush=True)

with tempfile.TemporaryDirectory() as temporary:
    check(Path(temporary), 'Nat.lt_of_lt_of_le h bound', True)
    check(Path(temporary), 'by sorry', False)
