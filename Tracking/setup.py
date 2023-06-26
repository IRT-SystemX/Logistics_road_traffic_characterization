import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as rq:
    req = rq.read().splitlines()

setuptools.setup(
    name="lead_vehicles_detection",
    version="0.1",
    description="Package to detect logistic vehicles from video",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.irt-systemx.fr/lead/camera_task/logistic_vehicles_detection",
    packages=setuptools.find_packages(),
    install_requires=req,
    python_requires=">=3.8",
    entry_points={"console_scripts": []},
)
