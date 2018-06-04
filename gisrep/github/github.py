"""
Github requester
"""

from github import Github

from ..reporter import Reporter

DEFAULT_TEMPLATE = r"""{% for issue in issues %}
- {{ issue.title }} [#{{ issue.number }}]
{% endfor %}"""


class GithubRequester(Reporter):

    def __init__(self, credentials=None):
        # Create PyGithub API object
        if credentials is not None:
            self.api = Github(
                credentials['username'],
                credentials['password'])
        else:
            self.api = Github()

        # Call Reporter initialiser
        super().__init__(DEFAULT_TEMPLATE)

    def _request(self, query):
        """ Request the issues """
        return self.api.search_issues(query, sort="created", order="asc")