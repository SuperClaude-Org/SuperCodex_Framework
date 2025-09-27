#!/usr/bin/env python3
"""
PyPI Readiness Validation Script
Checks if SuperCodex project is ready for PyPI publication
"""

import sys
import toml
from pathlib import Path
from typing import List, Tuple

# Project root
PROJECT_ROOT = Path(__file__).parent.parent

def check_file_exists(file_path: Path, description: str) -> bool:
    """Check if a required file exists"""
    if file_path.exists():
        print(f"✅ {description}: {file_path}")
        return True
    else:
        print(f"❌ Missing {description}: {file_path}")
        return False

def check_version_consistency() -> bool:
    """Check if versions are consistent across files"""
    print("\n🔍 Checking version consistency...")
    
    versions = {}
    
    # Check pyproject.toml
    try:
        pyproject_path = PROJECT_ROOT / "pyproject.toml"
        with open(pyproject_path, 'r') as f:
            pyproject = toml.load(f)
        versions['pyproject.toml'] = pyproject['project']['version']
        print(f"📋 pyproject.toml version: {versions['pyproject.toml']}")
    except Exception as e:
        print(f"❌ Error reading pyproject.toml: {e}")
        return False
    
    # Check SuperCodex/__init__.py
    try:
        sys.path.insert(0, str(PROJECT_ROOT))
        from SuperCodex import __version__
        versions['SuperCodex/__init__.py'] = __version__
        print(f"📦 Package version: {versions['SuperCodex/__init__.py']}")
    except Exception as e:
        print(f"❌ Error importing SuperCodex version: {e}")
        return False
    
    # Check setup/__init__.py
    try:
        from setup import __version__ as setup_version
        versions['setup/__init__.py'] = setup_version
        print(f"🔧 Setup version: {versions['setup/__init__.py']}")
    except Exception as e:
        print(f"❌ Error importing setup version: {e}")
        return False
    
    # Check consistency
    all_versions = list(versions.values())
    if len(set(all_versions)) == 1:
        print(f"✅ All versions consistent: {all_versions[0]}")
        return True
    else:
        print(f"❌ Version mismatch: {versions}")
        return False

def check_package_structure() -> bool:
    """Check if package structure is correct"""
    print("\n🏗️ Checking package structure...")
    
    required_structure = [
        ("SuperCodex/__init__.py", "Main package __init__.py"),
        ("SuperCodex/__main__.py", "Main entry point"),
        ("SuperCodex/Core/__init__.py", "Core module __init__.py"),
        ("SuperCodex/Commands/__init__.py", "Commands module __init__.py"),
        ("SuperCodex/Agents/__init__.py", "Agents module __init__.py"),
        ("SuperCodex/Modes/__init__.py", "Modes module __init__.py"),
        ("SuperCodex/MCP/__init__.py", "MCP module __init__.py"),
        ("setup/__init__.py", "Setup package __init__.py"),
    ]
    
    all_good = True
    for file_path, description in required_structure:
        full_path = PROJECT_ROOT / file_path
        if not check_file_exists(full_path, description):
            all_good = False
    
    return all_good

def check_required_files() -> bool:
    """Check if all required files are present"""
    print("\n📄 Checking required files...")
    
    required_files = [
        ("pyproject.toml", "Package configuration"),
        ("README.md", "Project README"),
        ("LICENSE", "License file"),
        ("MANIFEST.in", "Package manifest"),
        ("setup.py", "Setup script"),
    ]
    
    all_good = True
    for file_path, description in required_files:
        full_path = PROJECT_ROOT / file_path
        if not check_file_exists(full_path, description):
            all_good = False
    
    return all_good

def check_pyproject_config() -> bool:
    """Check pyproject.toml configuration"""
    print("\n⚙️ Checking pyproject.toml configuration...")
    
    try:
        pyproject_path = PROJECT_ROOT / "pyproject.toml"
        with open(pyproject_path, 'r') as f:
            pyproject = toml.load(f)
        
        project = pyproject.get('project', {})
        
        # Required fields
        required_fields = ['name', 'version', 'description', 'authors']
        for field in required_fields:
            if field in project:
                print(f"✅ {field}: {project[field]}")
            else:
                print(f"❌ Missing required field: {field}")
                return False
        
        # Check entry points
        scripts = project.get('scripts', {})
        if any(name in scripts for name in ['SuperCodex', 'supercodex', 'sg']):
            for name in ['SuperCodex', 'supercodex', 'sg']:
                if name in scripts:
                    print(f"✅ CLI entry point: {name} = {scripts[name]}")
        else:
            print("❌ Missing CLI entry point")
            return False
        
        # Check classifiers
        classifiers = project.get('classifiers', [])
        if len(classifiers) > 0:
            print(f"✅ {len(classifiers)} PyPI classifiers defined")
        else:
            print("⚠️ No PyPI classifiers defined")
        
        return True
        
    except Exception as e:
        print(f"❌ Error reading pyproject.toml: {e}")
        return False

def check_import_test() -> bool:
    """Test if the package can be imported"""
    print("\n🧪 Testing package import...")
    
    try:
        sys.path.insert(0, str(PROJECT_ROOT))
        import SuperCodex
        print(f"✅ SuperCodex import successful")
        print(f"📦 Version: {SuperCodex.__version__}")
        print(f"👤 Author: {SuperCodex.__author__}")
        return True
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False

def main():
    """Main validation function"""
    print("🔍 SuperCodex PyPI Readiness Validation")
    print(f"📁 Project root: {PROJECT_ROOT}")
    print("=" * 50)
    
    checks = [
        ("Required Files", check_required_files),
        ("Package Structure", check_package_structure),
        ("Version Consistency", check_version_consistency),
        ("PyProject Configuration", check_pyproject_config),
        ("Import Test", check_import_test),
    ]
    
    results = []
    
    for name, check_func in checks:
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"❌ {name} check failed with exception: {e}")
            results.append((name, False))
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 VALIDATION SUMMARY")
    print("=" * 50)
    
    passed = 0
    total = len(results)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {name}")
        if result:
            passed += 1
    
    print(f"\n📈 Overall: {passed}/{total} checks passed")
    
    if passed == total:
        print("🎉 Project is ready for PyPI publication!")
        print("\nNext steps:")
        print("1. ./scripts/publish.sh test    # Test on TestPyPI")
        print("2. ./scripts/publish.sh prod    # Publish to PyPI")
        return True
    else:
        print("❌ Project needs fixes before PyPI publication")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)