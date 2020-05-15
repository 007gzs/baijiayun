百家云相关接口
===========================================

.. module:: baijiayun.client

.. autoclass:: BaiJiaYunClient
   :members:
   :inherited-members:


`BaiJiaYunClient` 基本使用方法::

    from baijiayun import BaiJiaYunClient

    client = BaiJiaYunClient('<partner_id>', '<secret_key>', '<private_domain>')

    rooms = client.room.list()


.. toctree::
   :maxdepth: 2
   :glob:

   api/*

