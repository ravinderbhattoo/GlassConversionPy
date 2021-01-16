from distutils.core import setup
setup(
    name = 'GlassConversionPy',         # How you named your package folder
    packages = ['GlassConversionPy'],   # Chose the same as "name"
    version = '0.1',      # Start with a small number and increase it with every change you make
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description = 'Library to do simple conversions in glass science.',   # Give a short description about your library
    author = 'Ravinder Bhattoo',                   # Type in your name
    author_email = '',      # Type in your E-Mail
    url = 'https://github.com/ravinderbhattoo/GlassConversionPy',   # Provide either the link to your github or to your website
    download_url = 'https://github.com/ravinderbhattoo/GlassConversionPy/archive/v_01.tar.gz',    # I explain this later on
    keywords = ['Conversion', 'Glass', 'Glass Science'],   # Keywords that define your package best
    install_requires=[            # I get to this in a second
            'numpy',
            'pandas',
            'mendeleev'
        ],
    classifiers=[
      'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
      'Intended Audience :: Science/Research',      # Define that your audience are developers
      'License :: OSI Approved :: MIT License',   # Again, pick a license
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      'Programming Language :: Python :: 3.8',
      'Programming Language :: Python :: 3.9',
      'Programming Language :: Python :: 3.10',
    ],
)
