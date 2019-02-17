from setuptools import setup

setup(
    name='pgdocs',
    entry_points={
        'console_scrits': [
            'pgdocs = pgdocs:main'
        ]
    }
)
