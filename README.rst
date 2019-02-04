django-pg-timepart
==================
.. image:: https://img.shields.io/badge/License-MIT-orange.svg?style=flat-square
   :target: https://raw.githubusercontent.com/chaitin/django-partitioning/master/LICENSE
.. image:: https://img.shields.io/badge/Django-2.0_2.1-green.svg?style=flat-square&logo=django
   :target: https://www.djangoproject.com/
.. image:: https://img.shields.io/badge/PostgreSQL-11-lightgrey.svg?style=flat-square&logo=postgresql
   :target: https://www.postgresql.org/

一个实现 PostgreSQL 表基于日期进行分区和管理的 Django 扩展。
它适用于像记录日志、消息或文章等具有时间列的巨型表进行分区管理，定期创建新的分区并归档旧的分区。

----

A Django extension that implements PostgreSQL tables for partitioning and management based on dates.
It is suitable for partition management of giant tables with time columns like logging, messages or articles,
periodically creating new partitions and archiving old partitions.

Documentation
  https://django-pg-timepart.readthedocs.io/en/latest/

Contributing
------------

如果您有意为本开源项目出一份力，我们十分欢迎！在此之前，请首先阅读我们的 `Contributing Guidelines <https://raw.githubusercontent.com/chaitin/django-partitioning/master/CONTRIBUTING>`__。

----

If you want to contribute to a project and make it better, you help is very welcome!
Please read through `Contributing Guidelines <https://raw.githubusercontent.com/chaitin/django-pg-timepart/master/CONTRIBUTING>`__.

License
-------

django-pg-timepart 使用 MIT 开源协议。协议文本请阅读 LICENSE。

----

django-pg-timepart is licensed under the MIT. Please see `LICENSE <https://raw.githubusercontent.com/chaitin/django-pg-timepart/master/LICENSE>`_.