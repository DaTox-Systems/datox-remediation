import os
import sys
import re

FORBIDDEN_PATTERNS = [
    (r'[A-Za-z]:[\\/]Projects', 'Absolute Windows disk path'),
    (r'projects[\\/]+datox_remediation', 'Internal workspace path'),
    (r'work[\\/]+portfolio', 'Internal portfolio path'),
    (r'#KRN-\d+', 'Internal Kernel Law tag (#KRN-XX)'),
    (r'_DaToxSys', 'System core folder reference'),
    (r'DaToxAIctrL|\bDAC\b', 'Internal DAC tool reference'),
    (r'DevDeck', 'Internal DevDeck tool reference'),
    (r'<!--\s*FILE:', 'Internal file header tag (<!-- FILE:)'),
    (r'SESSION_LEDGER', 'Internal session ledger reference'),
    (r'DTX-CORE-|DTX-REMEDIATION-', 'Internal document ID prefix'),
]

DEFAULT_IGNORE = {'.git', '.dart_tool', 'build', '.idea', '.vscode'}
EXTENSIONS = {'.dart', '.md', '.yaml', '.yml', '.json', '.txt', '.toml', '.xml', '.gradle', '.kts', '.properties'}

def load_gitignore(target_dir):
    ignored = set(DEFAULT_IGNORE)
    gitignore_path = os.path.join(target_dir, '.gitignore')
    if os.path.exists(gitignore_path):
        try:
            with open(gitignore_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        clean = line.rstrip('/\\')
                        ignored.add(clean.replace('/', os.sep))
        except:
            pass
    return ignored

def scan_file(filepath):
    violations = []
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        for idx, line in enumerate(lines, 1):
            for pattern, desc in FORBIDDEN_PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
                    violations.append((idx, desc, line.strip()))
    except Exception as e:
        violations.append((0, f"Read error: {e}", ""))
    return violations

def run_preflight(target_dir):
    print("=" * 70)
    print(f"🔍 DATOX PRE-FLIGHT SANITIZATION AUDIT (v2.1 .gitignore-Aware)")
    print(f"Target: {os.path.abspath(target_dir)}")
    print("=" * 70)

    ignored_entries = load_gitignore(target_dir)
    total_violations = 0
    scanned_files = 0

    for root, dirs, files in os.walk(target_dir):
        rel_root = os.path.relpath(root, target_dir)
        
        # Пропуск игнорируемых папок из .gitignore
        parts = rel_root.split(os.sep)
        if any(ign in parts or rel_root == ign for ign in ignored_entries if ign != '.'):
            dirs[:] = []
            continue

        dirs[:] = [d for d in dirs if d not in ignored_entries]

        for file in files:
            if any(file.endswith(ext) for ext in EXTENSIONS):
                normalized_root = root.replace('\\', '/')
                if '/before' in normalized_root or normalized_root.endswith('/before'):
                    continue

                filepath = os.path.join(root, file)
                scanned_files += 1
                violations = scan_file(filepath)
                if violations:
                    rel_path = os.path.relpath(filepath, target_dir)
                    print(f"\n❌ [LEAK DETECTED] {rel_path}:")
                    for line_num, desc, line_content in violations:
                        print(f"   Line {line_num}: [{desc}] ──► {line_content[:80]}")
                        total_violations += 1

    print("\n" + "=" * 70)
    print(f"Scan complete. Scanned files: {scanned_files}. Total leaks: {total_violations}")
    
    if total_violations > 0:
        print("🛑 [VERDICT: FAIL] Repository contains internal leaks!")
        return False
    else:
        print("✅ [VERDICT: PASS] Zero leaks found. 100% Clean for Public Release.")
        return True

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else '.'
    success = run_preflight(target)
    sys.exit(0 if success else 1)
