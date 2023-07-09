======
Ecoute
======


.. image:: https://img.shields.io/pypi/v/ecoute.svg
        :target: https://pypi.python.org/pypi/ecoute


Ecoute is a wrapper on OpenAPI Whisper API. It's provide support for long audio files.


OpenAPI Whisper support only files that are less than 25 MB. Ecoute twill break the audio file into chunks of 25 MB's or less.
https://platform.openai.com/docs/guides/speech-to-text/longer-inputs

Ecoute will also fixe the timing of the subtitle. So once you export the subtitle the timestamp of the subtitle will be right.

You can open and save WAV files with pure python. For opening and saving non-wav files – like mp3 – you'll need ffmpeg or libav.

* Free software: Apache Software License 2.0


Features
--------

* Drop-in replacement to the OpenAPI *openai.Audio.transcribe*
* Support for large audio file


Why Ecoute?
-----------

Ecoute is the french word for listen. The original author of Ecoute is french.


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
