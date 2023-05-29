from dataclasses import dataclass
from typing import List
from typing import Dict
from typing import Optional
from typing import Tuple
from typing import Type
from typing import Union

from codemagic.apple.app_store_connect.resource_manager import ResourceManager
from codemagic.apple.resources import AppStoreVersion
from codemagic.apple.resources import LinkedResourceData
from codemagic.apple.resources import ResourceId
from codemagic.apple.resources import ResourceType
from codemagic.apple.resources import ReviewSubmission
from codemagic.apple.resources import ReviewSubmissionItem


class ReviewSubmissionItems(ResourceManager[ReviewSubmissionItem]):
    """
    Review Submission Items
    https://developer.apple.com/documentation/appstoreconnectapi/review_submission_items
    """

    @property
    def resource_type(self) -> Type[ReviewSubmissionItem]:
        return ReviewSubmissionItem
    
    @dataclass
    class Filter(ResourceManager.Filter):
        review_submission_id: Optional[Union[ResourceId, str]] = None

    def create(
        self,
        review_submission: Union[ResourceId, ReviewSubmission],
        app_custom_product_page_version: Optional[ResourceId] = None,
        app_event: Optional[ResourceId] = None,
        app_store_version: Optional[Union[ResourceId, AppStoreVersion]] = None,
        app_store_version_experiment: Optional[ResourceId] = None,
    ) -> ReviewSubmissionItem:
        """
        https://developer.apple.com/documentation/appstoreconnectapi/post_v1_reviewsubmissionitems
        """
        relationships = {
            'reviewSubmission': {
                'data': self._get_attribute_data(review_submission, ResourceType.REVIEW_SUBMISSIONS),
            },
        }

        optional_relationships: Dict[str, Tuple[Optional[Union[ResourceId, LinkedResourceData]], ResourceType]] = {
            'appCustomProductPageVersion': (
                app_custom_product_page_version,
                ResourceType.APP_CUSTOM_PRODUCT_PAGE_VERSIONS,
            ),
            'appEvent': (app_event, ResourceType.APP_EVENTS),
            'appStoreVersion': (app_store_version, ResourceType.APP_STORE_VERSIONS),
            'appStoreVersionExperiment': (
                app_store_version_experiment,
                ResourceType.APP_STORE_VERSION_EXPERIMENTS,
            ),
        }

        for relationship_name, (resource, resource_type) in optional_relationships.items():
            if resource is not None:
                relationships[relationship_name] = {'data': self._get_attribute_data(resource, resource_type)}

        payload = self._get_create_payload(
            ResourceType.REVIEW_SUBMISSION_ITEMS,
            relationships=relationships,
        )
        response = self.client.session.post(f'{self.client.API_URL}/reviewSubmissionItems', json=payload).json()
        return ReviewSubmissionItem(response['data'], created=True)

    def delete(self, review_submission_item: Union[LinkedResourceData, ResourceId]):
        """
        https://developer.apple.com/documentation/appstoreconnectapi/delete_v1_reviewsubmissionitems_id
        """
        review_submission_item_id = self._get_resource_id(review_submission_item)
        self.client.session.delete(f'{self.client.API_URL}/reviewSubmissionItems/{review_submission_item_id}')
    
    def list(self, resource_filter: Filter = Filter()) -> Tuple[List[ReviewSubmissionItem], List[Dict]]:
        """
        https://developer.apple.com/documentation/appstoreconnectapi/list_the_items_in_a_review_submission
        """
        review_submission_id = resource_filter.review_submission_id
        params = {"include": "appCustomProductPageVersion,appEvent,appStoreVersion,appStoreVersionExperiment"}
        paginate_result = self.client.paginate_with_included(
            f'{self.client.API_URL}/reviewSubmissions/{review_submission_id}/items',
            params=params
        )
        review_submission_list = paginate_result.data
        included_list = paginate_result.included
        review_submission_items = [ReviewSubmissionItem(item_info) for item_info in review_submission_list]
        return review_submission_items, included_list
