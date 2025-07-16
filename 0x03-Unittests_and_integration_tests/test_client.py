#!/usr/bin/env python3
"""Unit tests for client.GithubOrgClient"""

from typing import Self
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient.org property"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org calls get_json with correct URL"""
        test_payload = {"name": org_name}
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )
        self.assertEqual(result, test_payload)

class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient"""

    def test_public_repos_url(self):
        """Test that _public_repos_url returns correct URL from mocked org"""
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/test_org/repos"
            }

            client = GithubOrgClient("test_org")
            result = client._public_repos_url

            self.assertEqual(
                result,
                "https://api.github.com/orgs/test_org/repos"
            )


@patch("client.get_json")
def test_public_repos(self, mock_get_json):
    """Test that public_repos returns list of repo names from get_json"""
    test_payload = [
        {"name": "repo1"},
        {"name": "repo2"},
        {"name": "repo3"}
    ]
    mock_get_json.return_value = test_payload

    with patch.object(GithubOrgClient, "_public_repos_url", return_value="https://fakeurl.com"):
        client = GithubOrgClient("test_org")
        result = client.public_repos()

        # Assert the result is the list of repo names
        self.assertEqual(result, ["repo1", "repo2", "repo3"])

        # Assert _public_repos_url and get_json were each called once
        mock_get_json.assert_called_once_with("https://fakeurl.com")
