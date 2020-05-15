##########################
BaiJiaYun Sdk for Python
##########################
.. image:: https://travis-ci.org/007gzs/baijiayun.svg?branch=master
       :target: https://travis-ci.org/007gzs/baijiayun
.. image:: https://img.shields.io/pypi/v/baijiayun.svg
       :target: https://pypi.org/project/baijiayun

百家云 Python SDK。
`【阅读文档】 <http://baijiayun.readthedocs.io/zh_CN/latest/>`_。

********
安装
********

目前 BaiJiaYun 支持的 Python 环境有 2.7, 3.4, 3.5, 3.6, 3.7 和 pypy。

为了简化安装过程，推荐使用 pip 进行安装

.. code-block:: bash

    pip install baijiayun

升级 baijiayun 到新版本::

    pip install -U baijiayun

如果需要安装 GitHub 上的最新代码::

    pip install https://github.com/007gzs/baijiayun/archive/master.zip


调用示例
********
 ::

    from baijiayun import BaiJiaYunClient

    client = BaiJiaYunClient('<partner_id>', '<secret_key>', '<private_domain>')

    rooms = client.room.list()
