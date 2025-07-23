#!/usr/bin/env python3
"""
Release script for nb4llm.
Helps with version bumping and creating release tags.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path


def get_current_version():
    """Get current version from __init__.py"""
    init_file = Path("src/__init__.py")
    with open(init_file, 'r') as f:
        content = f.read()
    match = re.search(r"__version__ = '([^']+)'", content)
    if match:
        return match.group(1)
    raise ValueError("Could not find version in __init__.py")


def update_version(version):
    """Update version in both __init__.py and pyproject.toml"""
    # Update __init__.py
    init_file = Path("src/__init__.py")
    with open(init_file, 'r') as f:
        content = f.read()
    content = re.sub(r"__version__ = '[^']+'", f"__version__ = '{version}'", content)
    with open(init_file, 'w') as f:
        f.write(content)
    print(f"Updated {init_file} to version {version}")
    
    # Update pyproject.toml
    pyproject_file = Path("pyproject.toml")
    with open(pyproject_file, 'r') as f:
        content = f.read()
    content = re.sub(r'version = "[^"]+"', f'version = "{version}"', content)
    with open(pyproject_file, 'w') as f:
        f.write(content)
    print(f"Updated {pyproject_file} to version {version}")


def bump_version(version, bump_type):
    """Bump version according to semantic versioning"""
    major, minor, patch = map(int, version.split('.'))
    
    if bump_type == 'major':
        major += 1
        minor = 0
        patch = 0
    elif bump_type == 'minor':
        minor += 1
        patch = 0
    elif bump_type == 'patch':
        patch += 1
    else:
        raise ValueError(f"Invalid bump type: {bump_type}")
    
    return f"{major}.{minor}.{patch}"


def create_tag(version, message=None):
    """Create and push a git tag"""
    tag_name = f"v{version}"
    
    if message is None:
        message = f"Release version {version}"
    
    # Create tag
    subprocess.run(["git", "tag", "-a", tag_name, "-m", message], check=True)
    print(f"Created tag: {tag_name}")
    
    # Push tag
    subprocess.run(["git", "push", "origin", tag_name], check=True)
    print(f"Pushed tag: {tag_name}")


def main():
    parser = argparse.ArgumentParser(description="Release script for nb4llm")
    parser.add_argument(
        "action",
        choices=["bump", "tag", "release"],
        help="Action to perform"
    )
    parser.add_argument(
        "--type",
        choices=["major", "minor", "patch"],
        default="patch",
        help="Version bump type (default: patch)"
    )
    parser.add_argument(
        "--version",
        help="Specific version to use (overrides --type)"
    )
    parser.add_argument(
        "--message",
        help="Tag message (for tag action)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes"
    )
    
    args = parser.parse_args()
    
    try:
        current_version = get_current_version()
        print(f"Current version: {current_version}")
        
        if args.version:
            new_version = args.version
        else:
            new_version = bump_version(current_version, args.type)
        
        print(f"New version: {new_version}")
        
        if args.dry_run:
            print("DRY RUN - No changes will be made")
            if args.action == "bump":
                print(f"Would update version to {new_version}")
            elif args.action == "tag":
                print(f"Would create tag v{new_version}")
            elif args.action == "release":
                print(f"Would update version to {new_version} and create tag v{new_version}")
            return
        
        if args.action == "bump":
            update_version(new_version)
            print(f"Version bumped to {new_version}")
            print("Don't forget to commit and push the changes!")
            
        elif args.action == "tag":
            create_tag(new_version, args.message)
            
        elif args.action == "release":
            update_version(new_version)
            create_tag(new_version, args.message)
            print(f"Release {new_version} created and pushed!")
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main() 