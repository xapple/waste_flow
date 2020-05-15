from setuptools import setup, find_packages

setup(
        name             = 'waste_flow',
        version          = '1.1.2',
        description      = 'A package for retrieving data concerning waste management on the European continent.',
        long_description = open('README.md').read(),
        long_description_content_type = 'text/markdown',
        license          = 'MIT',
        url              = 'http://github.com/xapple/waste_flow/',
        author           = 'Lucas Sinclair',
        author_email     = 'lucas.sinclair@me.com',
        packages         = find_packages(),
        install_requires = ['pandas>=1.0.0', 'numpy>=1.16', 'requests', 'matplotlib',
                            'autopaths>=1.3.8', 'plumbing>=2.7.3', 'pymarktex>=1.3.4'],
        include_package_data = True,
)
