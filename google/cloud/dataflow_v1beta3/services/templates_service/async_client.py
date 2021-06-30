# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict
import functools
import re
from typing import Dict, Sequence, Tuple, Type, Union
import pkg_resources

import google.api_core.client_options as ClientOptions  # type: ignore
from google.api_core import exceptions as core_exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.dataflow_v1beta3.types import environment
from google.cloud.dataflow_v1beta3.types import jobs
from google.cloud.dataflow_v1beta3.types import templates
from google.protobuf import timestamp_pb2  # type: ignore
from google.rpc import status_pb2  # type: ignore
from .transports.base import TemplatesServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import TemplatesServiceGrpcAsyncIOTransport
from .client import TemplatesServiceClient


class TemplatesServiceAsyncClient:
    """Provides a method to create Cloud Dataflow jobs from
    templates.
    """

    _client: TemplatesServiceClient

    DEFAULT_ENDPOINT = TemplatesServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = TemplatesServiceClient.DEFAULT_MTLS_ENDPOINT

    common_billing_account_path = staticmethod(
        TemplatesServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        TemplatesServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(TemplatesServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        TemplatesServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        TemplatesServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        TemplatesServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(TemplatesServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        TemplatesServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(TemplatesServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        TemplatesServiceClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            TemplatesServiceAsyncClient: The constructed client.
        """
        return TemplatesServiceClient.from_service_account_info.__func__(TemplatesServiceAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            TemplatesServiceAsyncClient: The constructed client.
        """
        return TemplatesServiceClient.from_service_account_file.__func__(TemplatesServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> TemplatesServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            TemplatesServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(TemplatesServiceClient).get_transport_class, type(TemplatesServiceClient)
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, TemplatesServiceTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the templates service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.TemplatesServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = TemplatesServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def create_job_from_template(
        self,
        request: templates.CreateJobFromTemplateRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> jobs.Job:
        r"""Creates a Cloud Dataflow job from a template.

        Args:
            request (:class:`google.cloud.dataflow_v1beta3.types.CreateJobFromTemplateRequest`):
                The request object. A request to create a Cloud Dataflow
                job from a template.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dataflow_v1beta3.types.Job:
                Defines a job to be run by the Cloud
                Dataflow service. nextID: 26

        """
        # Create or coerce a protobuf request object.
        request = templates.CreateJobFromTemplateRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_job_from_template,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def launch_template(
        self,
        request: templates.LaunchTemplateRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> templates.LaunchTemplateResponse:
        r"""Launch a template.

        Args:
            request (:class:`google.cloud.dataflow_v1beta3.types.LaunchTemplateRequest`):
                The request object. A request to launch a template.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dataflow_v1beta3.types.LaunchTemplateResponse:
                Response to the request to launch a
                template.

        """
        # Create or coerce a protobuf request object.
        request = templates.LaunchTemplateRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.launch_template,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def get_template(
        self,
        request: templates.GetTemplateRequest = None,
        *,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> templates.GetTemplateResponse:
        r"""Get the template associated with a template.

        Args:
            request (:class:`google.cloud.dataflow_v1beta3.types.GetTemplateRequest`):
                The request object. A request to retrieve a Cloud
                Dataflow job template.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dataflow_v1beta3.types.GetTemplateResponse:
                The response to a GetTemplate
                request.

        """
        # Create or coerce a protobuf request object.
        request = templates.GetTemplateRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_template,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-dataflow-client",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("TemplatesServiceAsyncClient",)
