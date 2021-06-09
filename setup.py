import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vcf2hl7v2",
    version="0.0.16",
    author="",
    test_suite='vcf2hl7v2.test.test_vcf2hl7v2.suite',
    author_email="info@elimu.io",
    description="Convert .vcf files to HL7V2 message",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elimuinformatics/vcf2hl7v2",
    packages=['vcf2hl7v2', 'vcf2hl7v2.test'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License"
    ],
    tests_require=[
        'unittest',
    ],
    install_requires=[
        'pyVCF >=0.6.8',
        'pyranges >= 0.0.96'
    ],
    python_requires='>=3.6',
)
