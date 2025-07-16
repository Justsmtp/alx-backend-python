#!/usr/bin/env python3
"""Unit and integration tests for client.GithubOrgClient"""

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    [TEST_PAYLOAD[0]]  # index-based access because TEST_PAYLOAD is a list
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient.public_repos"""

    @classmethod
    def setUpClass(cls):
        """Patch requests.get and configure return values based on fixtures"""
        cls.get_patcher = patch("requests.get")
        mock_get = cls.get_patcher.start()

        # Prepare Mock response objects with .json() return values
        mock_org_response = Mock()
        mock_org_response.json.return_value = cls.org_payload

        mock_repos_response = Mock()
        mock_repos_response.json.return_value = cls.repos_payload

        # Simulate sequence of calls to requests.get().json()
        mock_get.side_effect = [
            mock_org_response, mock_repos_response,  # for test_public_repos
            mock_org_response, mock_repos_response   # for test_public_repos_with_license
        ]

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos returns expected repo names"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos filters repos by license"""
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )
