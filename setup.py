from setuptools import setup, find_packages

setup(
        name             = 'waste_flow',
        version          = '1.0.1',
        description      = 'A package for retrieving data concerning waste management on the European continent.',
        long_description = open('README.md').read(),
        long_description_content_type = 'text/markdown',
        license          = 'MIT',
        url              = 'http://github.com/xapple/waste_flow/',
        author           = 'Lucas Sinclair',
        author_email     = 'lucas.sinclair@me.com',
        packages         = find_packages(),
        install_requires = ['pandas>=1.0.0', 'requests', 'numpy>=1.16', 'matplotlib',
                            'autopaths>=1.3.6', 'plumbing>=2.6.5', 'pymarktext>=1.3.2'],
        include_package_data = True,
)
