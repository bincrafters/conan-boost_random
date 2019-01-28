#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/stable")

class BoostRandomConan(base.BoostBaseConan):
    name = "boost_random"
    version = "1.68.0"
    url = "https://github.com/bincrafters/conan-boost_random"
    lib_short_names = ["random"]
    cycle_group = "boost_cycle_group_c"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    b2_requires = ["boost_cycle_group_c"]
