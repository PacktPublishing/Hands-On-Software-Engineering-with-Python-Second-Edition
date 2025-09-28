# CH15-code README

## zip-package-example

Provides a very simple script and requirements.txt file that can be used to create a usable (if trivial) ZIP-archive package with the following commands:

```bash
# From the directory that the zip-package-example
# directory lives in:

# - Create the directory that will be used to zip
# the package up
mkdir my-package

# - Copy the source code from the project
cp zip-package-example/my_code/example.py my-package

# - Install the package dependencies into the new directory
pip install -r zip-package-example/requirements.txt \
  --target my-package/

# Zip the directory into the package file
zip my-package.zip my-package/*

# Remove the package directory
rm -fR
```
