
BaiJiaYun 使用文档
========================================

BaiJiaYun 是百家云 Python SDK。

快速入门
-------------

.. toctree::
   :maxdepth: 2

   install


开始使用
--------------------
建议在使用前先阅读 `百家云开发文档 <http://dev.baijiayun.com/>`_

.. toctree::
   :glob:
   :maxdepth: 2

   client/index

调用示例::

    from baijiayun import BaiJiaYunClient

    client = BaiJiaYunClient('<partner_id>', '<secret_key>', '<private_domain>')

    rooms = client.room.list()


Changelogs
---------------

.. toctree::
   :maxdepth: 1

   changelog

