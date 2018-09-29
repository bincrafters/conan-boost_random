#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostRandomConan(base.BoostBaseConan):
    name = "boost_random"
    url = "https://github.com/bincrafters/conan-boost_random"
    lib_short_names = ["random"]
    options = {"shared": [True, False]}
    default_options = "shared=False"
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_core",
        "boost_integer",
        "boost_io",
        "boost_math",
        "boost_mpl",
        "boost_range",
        "boost_static_assert",
        "boost_system",
        "boost_throw_exception",
        "boost_type_traits",
        "boost_utility"
    ]


