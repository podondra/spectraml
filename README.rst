spectraml
=========

Run test with :code:`python -m pytest tests` or :code:`python setup.py test`.

Travis CI
---------

This project is tested using
`Travis CI <https://travis-ci.org/podondra/spectraml>`_:

.. image:: https://travis-ci.org/podondra/spectraml.svg?branch=master
    :target: https://travis-ci.org/podondra/spectraml

Docker
------

To run a Docker container use the commands below after you build the image
from provided Dockerfile:

.. code::

    $ docker run -it -v "$PWD":/root --name $CONTAINER_NAME $IMAGE_NAME bash
    # pip install -e .
