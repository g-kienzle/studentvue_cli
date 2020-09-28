import setuptools

setuptools.setup(
    name="studentvue_cli",
    version="0.2",
    description="A useful module",
    packages=["studentvue_cli"],  # same as name
    entry_points={"console_scripts": ["svue = studentvue_cli.studentvue_cli:main"]},
    license="MIT",
    url="https://github.com/g-kienzle/studentvue_cli",
    download_url="https://github.com/g-kienzle/studentvue_cli/archive/v0.2.tar.gz",
    package_data={"": ["config.ini"]},
    include_package_data=True,
    install_requires=[
        "fire",
        "datetime",
        "studentvue",
        "bullet",
        "configparser",
    ],  # external packages as dependencies
)