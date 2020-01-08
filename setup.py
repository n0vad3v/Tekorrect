import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tekorrect",
    version="0.0.2",
    author="Nova Kwok",
    author_email="noc@nova.moe",
    description="用於給已經完成的 Markdown 遍寫的文檔進行優化，它會將壹些非標準，或不推薦的排版方式，進行自動格式化、標準化。",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/n0vad3v/Tekorrect",
    packages=setuptools.find_packages(),
    keywords='pangu text-spacing spacing text typesetting readability chinese japanese korean obsessive-compulsive-disorder ocd paranoia',
    classifiers=[
        "Programming Language :: Python :: 3",
        'Natural Language :: Chinese (Traditional)',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Japanese',
        'Natural Language :: Korean',
        'Topic :: Education',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: General',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Utilities',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "pangu",
    ],
    # scripts=['smv2/smv2.py'],
    entry_points={
        'console_scripts': [
            'tekorrect = tekorrect.tekorrect:exe_main',
        ],
    }
)
