from setuptools import setup, find_packages

setup(
    name='SE20HWnew',
    version='1.0.0',
    description='Demonstrating tools for a good repo',
    author='Caitlin Smith',
    author_email='hmkachha@ncsu.edu',
    url='https://github.com/chsmith/SE20-HW',

    packages=find_packages(include=['SE20HW', 'SE20HW.*', 'data']),
    long_description="""demonstrating tools for a good repo""",
    classifiers=[
        "License :: MIT License",
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: cool github repo",
    ],
    keywords='csc-510 hw1',
    license='MIT License',
    # install_requires=['numpy'],  # numpy is just for sample
    tests_require=['pytest']
)
