# -*- coding: utf-8 -*-

"""Test HTTP basic auth method.

:copyright: (c) 2016 by Detlef Stern
:license: Apache 2.0, see LICENSE
"""

from django.test import TestCase, override_settings

from django_auth_http_basic import (
    canonical_username, is_insensitive, HttpBasicAuthBackend)


class TestIsInsensitive(TestCase):
    """Test the is_insensitive function."""

    def test_none(self):
        """Test for no setting."""
        self.assertFalse(is_insensitive())

    @override_settings(HTTP_BASIC_AUTH_CASE=None)
    def test_none_explicit(self):
        """Test for explicit None setting."""
        self.assertTrue(is_insensitive())

    @override_settings(HTTP_BASIC_AUTH_CASE=0)
    def test_int_zero(self):
        """Test for explicit integer zero setting."""
        self.assertTrue(is_insensitive())

    @override_settings(HTTP_BASIC_AUTH_CASE=1)
    def test_int_one(self):
        """Test for explicit integer one setting."""
        self.assertFalse(is_insensitive())

    @override_settings(HTTP_BASIC_AUTH_CASE="NoIn")
    def test_noin(self):
        """Test for explicit insensitive setting."""
        self.assertTrue(is_insensitive())

    @override_settings(HTTP_BASIC_AUTH_CASE="falSch")
    def test_falsch(self):
        """Test for explicit insensitive setting."""
        self.assertTrue(is_insensitive())

    @override_settings(HTTP_BASIC_AUTH_CASE="0")
    def test_string_zero(self):
        """Test for explicit insensitive setting."""
        self.assertTrue(is_insensitive())

    @override_settings(HTTP_BASIC_AUTH_CASE="riChtig")
    def test_richtig(self):
        """Test for explicit sensitive setting."""
        self.assertFalse(is_insensitive())

    @override_settings(HTTP_BASIC_AUTH_CASE="yEs")
    def test_yes(self):
        """Test for explicit sensitive setting."""
        self.assertFalse(is_insensitive())

    @override_settings(HTTP_BASIC_AUTH_CASE="Wahr")
    def test_wahr(self):
        """Test for explicit sensitive setting."""
        self.assertFalse(is_insensitive())


class TestCanonical(TestCase):
    """Test the canonical_username function."""

    USERNAMES = ('lower', 'UPPER', 'mIXeD')

    def test_none(self):
        """Test for no setting."""
        for username in self.USERNAMES:
            self.assertEqual(username, canonical_username(username))

    @override_settings(HTTP_BASIC_AUTH_CASE="0")
    def test_string_zero(self):
        """Test for lower-case user names."""
        for username in self.USERNAMES:
            self.assertEqual(username.lower(), canonical_username(username))


class TestBackend(TestCase):
    def setUp(self):
        self.backend = HttpBasicAuthBackend()


class TestPwChecker(TestBackend):
    """Test the checkpw_pasic_auth method."""

    def test_none(self):
        """A None URL results in successful checks."""
        for username in (None, '', 'a', 'admin', 'zombie'):
            for password in (None, '', '1', '12345', '*'):
                self.assertTrue(
                    self.backend.checkpw_basic_auth(None, username, password),
                    "%s / %s" % (username, password))


class TestAuthenticate(TestBackend):
    """Test the authenticate mathod."""

    @override_settings(HTTP_BASIC_AUTH_URL=None)
    def test_simple(self):
        """A None URL results in successful checks."""
        for username in ('a', 'admin', 'zombie'):
            for password in (None, '', '1', '12345', '*'):
                user = self.backend.authenticate(
                    username=username, password=password)
                self.assertEqual(username, user.username)

    @override_settings(HTTP_BASIC_AUTH_URL=None, HTTP_BASIC_AUTH_CASE='n')
    def test_case_insensitive(self):
        """A None URL results in successful checks."""
        for username in ('A', 'ADMIN', 'ZOMbIE'):
            user = self.backend.authenticate(username=username, password="1")
            self.assertEqual(username.lower(), user.username)
