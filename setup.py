from setuptools import setup, find_packages


with open('README.rst') as f:
    long_description = ''.join(f.readlines())

setup(
        name='spectraml',
        version='0.0.0',
        description='',  # TODO
        long_description=long_description,
        author='Ondřej Podsztavek',
        author_email='podszond@fit.cvut.cz',
        keywords='',  # TODO
        license='MIT License',
        url='https://github.com/podondra/spectraml',
        packages=find_packages(),
        classifiers=[
            'Environment :: Console',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
            'Topic :: Scientific/Engineering :: Astronomy',
            ],
        entry_points={
            'console_scripts': [
                'spectraml = spectraml.cli:cli',
                ],
            },
        install_requires=['numpy', 'astropy'],  # TODO
        setup_requires=['pytest-runner'],
        tests_reqires=['pytest'],
)
