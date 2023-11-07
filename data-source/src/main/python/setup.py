from distutils.util import convert_path
import os
import setuptools

ver_path = convert_path('spyt/version.py')
with open(ver_path) as ver_file:
    exec(ver_file.read())

SCRIPTS_PATH = convert_path('deps/bin')
script_names = [
    'spark-discovery-yt', 'spark-launch-yt', 'spark-manage-yt', 'spark-shell-yt',
    'spark-submit-yt', 'spyt_cli.py',
]
scripts = [os.path.join(SCRIPTS_PATH, x) for x in script_names]

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name='ytsaurus-spyt',
    version=__version__,
    author='YTsaurus',
    author_email='dev@ytsaurus.tech',
    description='YTsaurus SPYT high-level client',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords="yt ytsaurus python spyt",
    url='https://github.com/ytsaurus/ytsaurus/tree/main/yt/spark/spark-over-yt',
    packages=[
        'spyt',
        'spyt.jars',
        'pyspark.bin',
        'pyspark.conf',
        'pyspark.jars',
    ],
    install_requires=[
        'ytsaurus-pyspark=={}'.format(__spark_version__),
        'pyarrow',
        'pyyaml'
    ],
    scripts=scripts,
    license='http://www.apache.org/licenses/LICENSE-2.0',
    package_dir={
        'spyt.jars': 'deps/spyt_jars',
        'pyspark.bin': 'deps/pyspark_deps/bin',
        'pyspark.conf': 'deps/pyspark_deps/conf',
        'pyspark.jars': 'deps/pyspark_deps/jars',
    },
    package_data={
        'spyt.jars': ['*.jar'],
    },
    include_package_data=True,
)
