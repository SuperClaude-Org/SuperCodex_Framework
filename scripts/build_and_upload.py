#!/usr/bin/env python3
"""
PyPI Build and Upload Script for SuperCodex Framework
Handles building, validation, and uploading to PyPI with proper error handling
"""

import os
import sys
import shutil
import subprocess
import argparse
from pathlib import Path
from typing import Tuple, List, Optional

# Project root
PROJECT_ROOT = Path(__file__).parent.parent
DIST_DIR = PROJECT_ROOT / "dist"
BUILD_DIR = PROJECT_ROOT / "build"

def update_version_refs():
    """Update version references from VERSION file"""
    print("🔄 Updating version references...")
    try:
        subprocess.run([sys.executable, "scripts/update_version_refs.py"], 
                      cwd=PROJECT_ROOT, check=True)
        print("✅ Version references updated")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to update version references: {e}")
        sys.exit(1)

def run_command(cmd: List[str], description: str) -> Tuple[bool, str]:
    """Run a command and return success status and output"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            cwd=PROJECT_ROOT,
            check=True
        )
        print(f"✅ {description} completed successfully")
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"   Exit code: {e.returncode}")
        print(f"   Error: {e.stderr}")
        return False, e.stderr
    except Exception as e:
        print(f"❌ {description} failed with exception: {e}")
        return False, str(e)

def clean_build_artifacts():
    """Clean previous build artifacts"""
    artifacts = [DIST_DIR, BUILD_DIR, PROJECT_ROOT / "SuperCodex.egg-info"]
    
    for artifact in artifacts:
        if artifact.exists():
            print(f"🧹 Removing {artifact}")
            if artifact.is_dir():
                shutil.rmtree(artifact)
            else:
                artifact.unlink()

def install_build_tools() -> bool:
    """Install required build tools"""
    tools = ["build", "twine"]
    
    for tool in tools:
        success, _ = run_command(
            [sys.executable, "-m", "pip", "install", "--upgrade", tool],
            f"Installing {tool}"
        )
        if not success:
            return False
    
    return True

def validate_project_structure() -> bool:
    """Validate project structure before building"""
    required_files = [
        "pyproject.toml",
        "README.md", 
        "LICENSE",
        "SuperCodex/__init__.py",
        "SuperCodex/__main__.py",
        "setup/__init__.py"
    ]
    
    print("🔍 Validating project structure...")
    
    for file_path in required_files:
        full_path = PROJECT_ROOT / file_path
        if not full_path.exists():
            print(f"❌ Missing required file: {file_path}")
            return False
    
    # Check if version is consistent
    try:
        from SuperCodex import __version__
        print(f"📦 Package version: {__version__}")
    except ImportError as e:
        print(f"❌ Could not import version from SuperCodex: {e}")
        return False
    
    print("✅ Project structure validation passed")
    return True

def build_package() -> bool:
    """Build the package"""
    return run_command(
        [sys.executable, "-m", "build"],
        "Building package distributions"
    )[0]

def validate_distribution() -> bool:
    """Validate the built distribution"""
    if not DIST_DIR.exists():
        print("❌ Distribution directory does not exist")
        return False
    
    dist_files = list(DIST_DIR.glob("*"))
    if not dist_files:
        print("❌ No distribution files found")
        return False
    
    print(f"📦 Found distribution files:")
    for file in dist_files:
        print(f"   - {file.name}")
    
    # Check with twine
    return run_command(
        [sys.executable, "-m", "twine", "check"] + [str(f) for f in dist_files],
        "Validating distributions with twine"
    )[0]

def upload_to_testpypi() -> bool:
    """Upload to TestPyPI for testing"""
    dist_files = list(DIST_DIR.glob("*"))
    return run_command(
        [sys.executable, "-m", "twine", "upload", "--repository", "testpypi"] + [str(f) for f in dist_files],
        "Uploading to TestPyPI"
    )[0]

def upload_to_pypi() -> bool:
    """Upload to production PyPI"""
    dist_files = list(DIST_DIR.glob("*"))
    
    # Check if we have API token in environment
    if os.getenv('PYPI_API_TOKEN'):
        cmd = [
            sys.executable, "-m", "twine", "upload",
            "--username", "__token__",
            "--password", os.getenv('PYPI_API_TOKEN')
        ] + [str(f) for f in dist_files]
    else:
        # Fall back to .pypirc configuration
        cmd = [sys.executable, "-m", "twine", "upload"] + [str(f) for f in dist_files]
    
    return run_command(cmd, "Uploading to PyPI")[0]

def test_installation_from_testpypi() -> bool:
    """Test installation from TestPyPI"""
    print("🧪 Testing installation from TestPyPI...")
    print("   Note: This will install in a separate process")
    
    success, output = run_command([
        sys.executable, "-m", "pip", "install", 
        "--index-url", "https://test.pypi.org/simple/",
        "--extra-index-url", "https://pypi.org/simple/",
        "SuperCodex", "--force-reinstall", "--no-deps"
    ], "Installing from TestPyPI")
    
    if success:
        print("✅ Test installation successful")
        # Try to import the package
        try:
            import SuperCodex
            print(f"✅ Package import successful, version: {SuperCodex.__version__}")
            return True
        except ImportError as e:
            print(f"❌ Package import failed: {e}")
            return False
    
    return False

def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(description="Build and upload SuperCodex to PyPI")
    parser.add_argument("--testpypi", action="store_true", help="Upload to TestPyPI instead of PyPI")
    parser.add_argument("--test-install", action="store_true", help="Test installation from TestPyPI")
    parser.add_argument("--skip-build", action="store_true", help="Skip build step (use existing dist)")
    parser.add_argument("--skip-validation", action="store_true", help="Skip validation steps")
    parser.add_argument("--clean", action="store_true", help="Only clean build artifacts")
    
    args = parser.parse_args()
    
    # Change to project root
    os.chdir(PROJECT_ROOT)
    
    if args.clean:
        clean_build_artifacts()
        return
    
    print("🚀 SuperCodex PyPI Build and Upload Script")
    print(f"📁 Working directory: {PROJECT_ROOT}")
    
    # Update version references first
    update_version_refs()
    
    # Step 1: Clean previous builds
    clean_build_artifacts()
    
    # Step 2: Install build tools
    if not install_build_tools():
        print("❌ Failed to install build tools")
        sys.exit(1)
    
    # Step 3: Validate project structure
    if not args.skip_validation and not validate_project_structure():
        print("❌ Project structure validation failed")
        sys.exit(1)
    
    # Step 4: Build package
    if not args.skip_build:
        if not build_package():
            print("❌ Package build failed")
            sys.exit(1)
    
    # Step 5: Validate distribution
    if not args.skip_validation and not validate_distribution():
        print("❌ Distribution validation failed")
        sys.exit(1)
    
    # Step 6: Upload
    if args.testpypi:
        if not upload_to_testpypi():
            print("❌ Upload to TestPyPI failed")
            sys.exit(1)
        
        # Test installation if requested
        if args.test_install:
            if not test_installation_from_testpypi():
                print("❌ Test installation failed")
                sys.exit(1)
    else:
        # Confirm production upload
        response = input("🚨 Upload to production PyPI? This cannot be undone! (yes/no): ")
        if response.lower() != "yes":
            print("❌ Upload cancelled")
            sys.exit(1)
        
        if not upload_to_pypi():
            print("❌ Upload to PyPI failed")
            sys.exit(1)
    
    print("✅ All operations completed successfully!")

if __name__ == "__main__":
    main()