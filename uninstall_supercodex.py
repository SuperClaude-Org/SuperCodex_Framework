#!/usr/bin/env python3
"""
SuperCodex Uninstall Script
Standalone uninstall script that doesn't rely on complex imports
"""

import shutil
import json
import sys
from pathlib import Path


def uninstall_supercodex(install_dir=None, verbose=False):
    """Uninstall SuperCodex framework"""
    
    # Default to ~/.codex directory
    if install_dir is None:
        install_dir = Path.home() / '.codex'
    else:
        install_dir = Path(install_dir)
    
    # Check if directory exists
    if not install_dir.exists():
        print(f"⚠️ No SuperCodex installation found at {install_dir}")
        return 0
    
    # Safety check - ensure it's the Codex directory
    if install_dir.name != '.codex':
        response = input(f"❓ Directory {install_dir} doesn't appear to be a standard SuperCodex installation. Continue? (y/N): ")
        if response.lower() != 'y':
            print("Uninstall cancelled.")
            return 1
    
    # Get metadata if available
    metadata_file = install_dir / '.supercodex-metadata.json'
    components = {}
    if metadata_file.exists():
        try:
            with open(metadata_file) as f:
                metadata = json.load(f)
                components = metadata.get('components', {})
        except:
            pass
    
    # Display what will be removed
    print("\n" + "="*60)
    print("       SuperCodex Uninstall")
    print("="*60)
    print(f"\n📂 Installation directory: {install_dir}")
    
    if components:
        print("\n📦 Installed components:")
        for comp, info in components.items():
            version = info.get('version', 'unknown') if isinstance(info, dict) else info
            print(f"  - {comp}: v{version}")
    
    # Count files
    file_count = sum(1 for _ in install_dir.rglob('*') if _.is_file())
    dir_count = sum(1 for _ in install_dir.rglob('*') if _.is_dir())
    
    print(f"\n📊 Statistics:")
    print(f"  Files: {file_count}")
    print(f"  Directories: {dir_count}")
    
    # Confirm removal
    print(f"\n⚠️  WARNING: This will permanently delete {install_dir}")
    if '--yes' not in sys.argv and '-y' not in sys.argv:
        response = input("Continue with uninstall? (y/N): ")
        if response.lower() != 'y':
            print("Uninstall cancelled.")
            return 1
    
    # Perform uninstall
    print(f"\n🗑️  Removing {install_dir}...")
    try:
        shutil.rmtree(install_dir)
        print("✅ SuperCodex uninstalled successfully!")
        print("\nYou can reinstall anytime using:")
        print("  pip install -e . && python -m SuperCodex install")
        return 0
    except Exception as e:
        print(f"❌ Error during uninstall: {e}")
        return 1


def main():
    """Main entry point"""
    # Parse simple command line arguments
    verbose = '--verbose' in sys.argv or '-v' in sys.argv
    
    # Check for custom install directory
    install_dir = None
    for i, arg in enumerate(sys.argv):
        if arg == '--install-dir' and i + 1 < len(sys.argv):
            install_dir = sys.argv[i + 1]
            break
    
    # Run uninstall
    return uninstall_supercodex(install_dir, verbose)


if __name__ == "__main__":
    sys.exit(main())