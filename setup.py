from setuptools import setup, find_packages

setup(
    name='FlowXcel',  # The name of your package
    version='0.1',  # Version number (should be incremented with each release)
    description='A compact traffic simulation module for low-end processors.',
    long_description=open('README.md').read(),  # Reads content from README.md
    long_description_content_type='text/markdown',
    author='Kamal',  # Your name
    author_email='kamalakk16107@gmail.com',  # Your email
    url='https://github.com/Kamal1612-sys/kamal_module-RL-flowexcel',  # Your project URL or GitHub repo
    packages=find_packages(),  # Automatically finds packages to include
    install_requires=[  # List any dependencies your module needs
        'matplotlib',  # Example, add others as needed
    ],
    classifiers=[  # PyPI classifiers to help users find your package
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Define the required Python version
)
