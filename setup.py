from setuptools import setup

setup(
    name='SE20-HW',
    version='1.0.0',
    description='Demonstrating tools for a good repo',
    author='Caitlin Smith',
    author_email='hmkachha@ncsu.edu',
    url='https://github.com/chsmith/SE20-HW',

    packages=['code'],
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
