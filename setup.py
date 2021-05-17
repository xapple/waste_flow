from setuptools import setup, find_namespace_packages

setup(
        name             = 'waste_flow',
        version          = '1.2.0',
        description      = 'A package for retrieving data concerning waste management on the European continent.',
        license          = 'MIT',
        url              = 'http://github.com/xapple/waste_flow/',
        author           = 'Lucas Sinclair',
        author_email     = 'lucas.sinclair@me.com',
        packages         = find_namespace_packages(),
        install_requires = ['autopaths>=1.4.0', 'plumbing>=2.7.9', 'pymarktex>=1.3.8'
                            'pandas>=1.0.0', 'numpy>=1.16', 'requests', 'matplotlib'],
        long_description = open('README.md').read(),
        long_description_content_type = 'text/markdown',
        include_package_data = True,
)
