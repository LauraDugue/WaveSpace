from setuptools import setup, find_packages

with open('app/README.md') as f:
    long_description = f.read()

setup(
    name='WaveSpace',
    version='0.8.0',
    description='A Python package for the analysis of cortical traveling waves',
    package_dir={'': 'app'},
    packages=find_packages(where='app'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kpetras/WaveSpace',
    author='Kirsten Petras',
    author_email='k.petras@web.de',
    license='GNU General Public License',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
    install_requires=[
        "matplotlib>=3.9.2",
        "scipy>=1.13.1",
        "plotly>=5.24.1",
        "pint>=0.24.4",
        "pyvista>=0.44.2",
        "pandas>=2.2.3",
        "scikit-learn>=1.6.1",
        "tvb-gdist>=2.2.1",
        "emd>=0.8.0",
      ]
)
    