from __future__ import annotations

from abc import ABCMeta
from typing import List
from typing import Dict
from typing import Tuple

from codemagic import cli
from codemagic.apple.resources import Platform
from codemagic.apple.resources import ResourceId
from codemagic.apple.resources import ReviewSubmission
from codemagic.apple.resources import ReviewSubmissionItem

from ..abstract_base_action import AbstractBaseAction
from ..action_group import AppStoreConnectActionGroup
from ..arguments import AppArgument
from ..arguments import AppStoreVersionArgument
from ..arguments import ReviewSubmissionArgument


class ReviewSubmissionsActionGroup(AbstractBaseAction, metaclass=ABCMeta):
    @cli.action(
        'create',
        AppArgument.APPLICATION_ID_RESOURCE_ID,
        AppStoreVersionArgument.PLATFORM,
        action_group=AppStoreConnectActionGroup.REVIEW_SUBMISSIONS,
    )
    def create_review_submission(
        self,
        application_id: ResourceId,
        platform: Platform,
        should_print: bool = True,
    ) -> ReviewSubmission:
        """
        Create a review submission request for application's latest App Store Version
        """
        return self._create_resource(
            self.api_client.review_submissions,
            should_print,
            app=application_id,
            platform=platform,
        )

    @cli.action(
        'get',
        ReviewSubmissionArgument.REVIEW_SUBMISSION_ID,
        action_group=AppStoreConnectActionGroup.REVIEW_SUBMISSIONS,
    )
    def get_review_submission(
        self,
        review_submission_id: ResourceId,
        should_print: bool = True,
    ) -> ReviewSubmission:
        """
        Read Review Submission information
        """
        return self._get_resource(
            review_submission_id,
            self.api_client.review_submissions,
            should_print,
        )

    @cli.action(
        'cancel',
        ReviewSubmissionArgument.REVIEW_SUBMISSION_ID,
        action_group=AppStoreConnectActionGroup.REVIEW_SUBMISSIONS,
    )
    def cancel_review_submission(
        self,
        review_submission_id: ResourceId,
        should_print: bool = True,
    ) -> ReviewSubmission:
        """
        Discard a specific review submission from App Review
        """
        return self._modify_resource(
            self.api_client.review_submissions,
            review_submission_id,
            should_print,
            canceled=True,
        )

    @cli.action(
        'confirm',
        ReviewSubmissionArgument.REVIEW_SUBMISSION_ID,
        action_group=AppStoreConnectActionGroup.REVIEW_SUBMISSIONS,
    )
    def confirm_review_submission(
        self,
        review_submission_id: ResourceId,
        should_print: bool = True,
    ) -> ReviewSubmission:
        """
        Confirm pending review submission for App Review
        """
        return self._modify_resource(
            self.api_client.review_submissions,
            review_submission_id,
            should_print,
            submitted=True,
        )
    
    @cli.action(
        'list-items-in-review-submission',
        ReviewSubmissionArgument.REVIEW_SUBMISSION_ID,
        action_group=AppStoreConnectActionGroup.REVIEW_SUBMISSIONS,
    )
    def list_items_in_review_submission(
        self,
        review_submission_id: ResourceId,
        should_print: bool = False,
    ) -> Tuple[List[ReviewSubmissionItem], List[Dict]]:
        """
        List items in specific review submission
        """

        items_filter = self.api_client.review_submissions_items.Filter(
            review_submission_id=review_submission_id
            )
        
        return self._list_resources(
            items_filter,
            self.api_client.review_submissions_items,
            should_print,
        )
