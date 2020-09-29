import setuptools

setuptools.setup(
    name="studentvue_cli",
    version="0.5",
    packages=["studentvue_cli"],  # same as name
    entry_points={"console_scripts": ["svue = studentvue_cli.studentvue_cli:main"]},
    license="MIT",
    description="description",
    url="https://github.com/g-kienzle/studentvue_cli",
    download_url="https://github.com/g-kienzle/studentvue_cli/archive/v0.5.tar.gz",
    include_package_data=True,
    install_requires=[
        "fire",
        "datetime",
        "studentvue",
        "bullet",
        "configparser",
    ],
)