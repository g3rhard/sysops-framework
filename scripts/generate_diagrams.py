#!/usr/bin/env python3
"""
Professional Diagram Generator for SysOps Framework Documentation

This script generates high-quality PNG diagrams for the documentation.
It dynamically discovers diagram definitions from the diagrams folder.
"""

import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend — must come before any other matplotlib import

import matplotlib.pyplot as plt
import os
import sys
import importlib.util
from pathlib import Path
import argparse
import warnings

# Suppress harmless font / glyph warnings
warnings.filterwarnings("ignore", "Glyph.*missing from font.*")
warnings.filterwarnings("ignore", "findfont.*")

# Base rcParams — individual diagram modules may further override these
plt.rcParams.update({
    'figure.dpi':       150,    # screen quality during module import; overridden at save time
    'savefig.dpi':      300,    # final output quality
    'font.family':      'sans-serif',
    'font.size':        10,
    'axes.spines.top':  False,
    'axes.spines.right': False,
})


def discover_diagram_modules():
    """Dynamically discover all diagram definition modules."""
    diagrams_dir = Path(__file__).parent / 'diagrams'
    diagram_modules = []

    if not diagrams_dir.exists():
        print(f"⚠️  Warning: Diagrams directory not found: {diagrams_dir}")
        return []

    # Make the diagrams directory importable so modules can do
    # `from _design_system import ...` without relative-import gymnastics.
    diagrams_dir_str = str(diagrams_dir)
    if diagrams_dir_str not in sys.path:
        sys.path.insert(0, diagrams_dir_str)

    print(f"🔍 Discovering diagram definitions in {diagrams_dir}...")

    # Find all Python files in diagrams directory
    for py_file in sorted(diagrams_dir.glob('*.py')):
        if py_file.name.startswith('_'):
            continue  # Skip private/shared files (e.g. _design_system.py)

        try:
            # Import the module dynamically
            spec = importlib.util.spec_from_file_location(py_file.stem, py_file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # Check if module has required functions and info
            if hasattr(module, 'create_diagram') and hasattr(module, 'DIAGRAM_INFO'):
                diagram_modules.append({
                    'module': module,
                    'info': module.DIAGRAM_INFO,
                    'create_func': module.create_diagram,
                    'source_file': py_file.name
                })
                print(f"   ✅ {module.DIAGRAM_INFO['description']} (Chapter {module.DIAGRAM_INFO['chapter']})")
            else:
                print(f"   ⚠️  Skipping {py_file.name}: Missing create_diagram() or DIAGRAM_INFO")
                
        except Exception as e:
            print(f"   ❌ Error loading {py_file.name}: {e}")
    
    return diagram_modules


def generate_all_diagrams(output_dir=None, dpi=300):
    """Generate all diagrams and save as PNG files"""
    
    # Discover all diagram modules
    diagram_modules = discover_diagram_modules()
    
    if not diagram_modules:
        print("❌ No valid diagram definitions found!")
        return 0
    
    # Sort by chapter number for consistent order
    diagram_modules.sort(key=lambda x: x['info']['chapter'])
    
    # Ensure output directory exists
    if output_dir is None:
        output_dir = Path(__file__).parent.parent / 'content' / 'assets'
    else:
        output_dir = Path(output_dir)
    
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n🎯 Generating {len(diagram_modules)} professional diagrams...")
    print(f"📁 Output directory: {output_dir}")
    print(f"📐 DPI: {dpi}")
    
    success_count = 0
    
    for diagram_data in diagram_modules:
        try:
            info = diagram_data['info']
            print(f"\n📊 Generating {info['description']} (Chapter {info['chapter']})...")
            
            # Create the diagram
            fig = diagram_data['create_func']()
            
            # Save as high-quality PNG
            output_path = output_dir / info['filename']
            fig.savefig(
                output_path, 
                dpi=dpi, 
                bbox_inches='tight', 
                facecolor='white', 
                edgecolor='none',
                format='png',
                pad_inches=0.2
            )
            plt.close(fig)  # Free memory
            
            file_size = output_path.stat().st_size / 1024  # KB
            print(f"   ✅ Saved: {output_path.name} ({file_size:.1f} KB)")
            success_count += 1
            
        except Exception as e:
            print(f"   ❌ Error generating {info['description']}: {e}")
            import traceback
            traceback.print_exc()
    
    print(f"\n🎉 Generation complete!")
    print(f"✅ Successfully generated: {success_count} diagram(s)")
    print(f"📁 Files saved to: {output_dir}")
    
    return success_count


def main():
    """Main entry point with command line argument support"""
    parser = argparse.ArgumentParser(
        description="Generate professional PNG diagrams for SysOps Framework"
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Directory to save PNG files (default: ../content/assets)"
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=300,
        help="DPI for PNG output (default: 300)"
    )
    
    args = parser.parse_args()
    
    # Generate all diagrams
    success_count = generate_all_diagrams(
        output_dir=args.output_dir,
        dpi=args.dpi
    )
    
    if success_count == 0:
        sys.exit(1)


if __name__ == '__main__':
    main()