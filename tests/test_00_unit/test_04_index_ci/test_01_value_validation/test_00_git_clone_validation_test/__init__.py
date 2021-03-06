from tests.test_00_unit.test_04_index_ci.indexcibase import IndexCIBase, \
    DUMMY_INDEX_FILE
from ci.container_index.lib.constants import *
import ci.container_index.lib.checks.value_validation as value_validation
import ci.container_index.lib.state as index_ci_state


class GitCloneValidationTests(IndexCIBase):

    def test_00_setup_test(self):
        self._setup_test()

    def test_01_succeeds_valid_git_url_git_branch_with_clone_request(self):
        self.assertTrue(
            value_validation.GitCloneValidator(
                {
                    CheckKeys.CLONE: True,
                    FieldKeys.GIT_URL:
                        "https://github.com/bamachrn/cccp-python.git",
                    FieldKeys.GIT_BRANCH: "master",
                    CheckKeys.STATE: index_ci_state.State()
                },
                DUMMY_INDEX_FILE
            ).validate().success
        )

    def test_02_fails_invalid_git_url_valid_git_branch_with_clone_request(self):
        self.assertFalse(
            value_validation.GitCloneValidator(
                {
                    CheckKeys.CLONE: True,
                    FieldKeys.GIT_URL:
                        "https://github.com/bamachrn/does-not-exist.git",
                    FieldKeys.GIT_BRANCH: "master",
                    CheckKeys.STATE: index_ci_state.State()
                },
                DUMMY_INDEX_FILE
            ).validate().success
        )

    def test_03_fails_valid_git_url_invalid_git_branch_with_clone_request(self):
        self.assertFalse(
            value_validation.GitCloneValidator(
                {
                    CheckKeys.CLONE: True,
                    FieldKeys.GIT_URL:
                        "https://github.com/bamachrn/cccp-python.git",
                    FieldKeys.GIT_BRANCH: "some-nonexistant-branch",
                    CheckKeys.STATE: index_ci_state.State()
                },
                DUMMY_INDEX_FILE
            ).validate().success
        )
