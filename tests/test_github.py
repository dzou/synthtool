# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest
import os

from autosynth import github

requires_github_token = unittest.skipIf(
    not os.environ.get("GITHUB_TOKEN", False),
    "Set the environment variable GITHUB_TOKEN to run this test.",
)


def new_gh():
    return github.GitHub(os.environ["GITHUB_TOKEN"])


@requires_github_token
def test_list_repos():
    gh = new_gh()
    repos = gh.list_repos("googleapis")
    assert len(repos) > 10


@requires_github_token
def test_default_branch():
    gh = new_gh()
    default_branch = gh.get_default_branch("googleapis/sloth")
    assert default_branch == "main"
