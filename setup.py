from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='kivy-swr',
    version='0.1.0',
    description='Kivy hook library for remote data fetching',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Yann Cabral',
    author_email='iamyanndias@gmail.com',
    keywords=['swr', 'fetch', 'data remote'],
    url='https://github.com/yanncabral/kivy-swr',
    download_url='https://pypi.org/project/kivy-swr/'
)

install_requires = [
    'kivy',
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)