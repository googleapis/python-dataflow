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
import proto  # type: ignore

from google.protobuf import struct_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.dataflow.v1beta3",
    manifest={
        "ExecutionState",
        "MetricStructuredName",
        "MetricUpdate",
        "GetJobMetricsRequest",
        "JobMetrics",
        "GetJobExecutionDetailsRequest",
        "ProgressTimeseries",
        "StageSummary",
        "JobExecutionDetails",
        "GetStageExecutionDetailsRequest",
        "WorkItemDetails",
        "WorkerDetails",
        "StageExecutionDetails",
    },
)


class ExecutionState(proto.Enum):
    r"""The state of some component of job execution."""
    EXECUTION_STATE_UNKNOWN = 0
    EXECUTION_STATE_NOT_STARTED = 1
    EXECUTION_STATE_RUNNING = 2
    EXECUTION_STATE_SUCCEEDED = 3
    EXECUTION_STATE_FAILED = 4
    EXECUTION_STATE_CANCELLED = 5


class MetricStructuredName(proto.Message):
    r"""Identifies a metric, by describing the source which generated
    the metric.

    Attributes:
        origin (str):
            Origin (namespace) of metric name. May be
            blank for user-define metrics; will be
            "dataflow" for metrics defined by the Dataflow
            service or SDK.
        name (str):
            Worker-defined metric name.
        context (Sequence[google.cloud.dataflow_v1beta3.types.MetricStructuredName.ContextEntry]):
            Zero or more labeled fields which identify the part of the
            job this metric is associated with, such as the name of a
            step or collection.

            For example, built-in counters associated with steps will
            have context['step'] = . Counters associated with
            PCollections in the SDK will have context['pcollection'] = .
    """

    origin = proto.Field(proto.STRING, number=1,)
    name = proto.Field(proto.STRING, number=2,)
    context = proto.MapField(proto.STRING, proto.STRING, number=3,)


class MetricUpdate(proto.Message):
    r"""Describes the state of a metric.

    Attributes:
        name (google.cloud.dataflow_v1beta3.types.MetricStructuredName):
            Name of the metric.
        kind (str):
            Metric aggregation kind.  The possible metric
            aggregation kinds are "Sum", "Max", "Min",
            "Mean", "Set", "And", "Or", and "Distribution".
            The specified aggregation kind is case-
            insensitive.
            If omitted, this is not an aggregated value but
            instead a single metric sample value.
        cumulative (bool):
            True if this metric is reported as the total
            cumulative aggregate value accumulated since the
            worker started working on this WorkItem. By
            default this is false, indicating that this
            metric is reported as a delta that is not
            associated with any WorkItem.
        scalar (google.protobuf.struct_pb2.Value):
            Worker-computed aggregate value for
            aggregation kinds "Sum", "Max", "Min", "And",
            and "Or".  The possible value types are Long,
            Double, and Boolean.
        mean_sum (google.protobuf.struct_pb2.Value):
            Worker-computed aggregate value for the "Mean" aggregation
            kind. This holds the sum of the aggregated values and is
            used in combination with mean_count below to obtain the
            actual mean aggregate value. The only possible value types
            are Long and Double.
        mean_count (google.protobuf.struct_pb2.Value):
            Worker-computed aggregate value for the "Mean" aggregation
            kind. This holds the count of the aggregated values and is
            used in combination with mean_sum above to obtain the actual
            mean aggregate value. The only possible value type is Long.
        set_ (google.protobuf.struct_pb2.Value):
            Worker-computed aggregate value for the "Set"
            aggregation kind.  The only possible value type
            is a list of Values whose type can be Long,
            Double, or String, according to the metric's
            type.  All Values in the list must be of the
            same type.
        distribution (google.protobuf.struct_pb2.Value):
            A struct value describing properties of a
            distribution of numeric values.
        gauge (google.protobuf.struct_pb2.Value):
            A struct value describing properties of a
            Gauge. Metrics of gauge type show the value of a
            metric across time, and is aggregated based on
            the newest value.
        internal (google.protobuf.struct_pb2.Value):
            Worker-computed aggregate value for internal
            use by the Dataflow service.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp associated with the metric value.
            Optional when workers are reporting work
            progress; it will be filled in responses from
            the metrics API.
    """

    name = proto.Field(proto.MESSAGE, number=1, message="MetricStructuredName",)
    kind = proto.Field(proto.STRING, number=2,)
    cumulative = proto.Field(proto.BOOL, number=3,)
    scalar = proto.Field(proto.MESSAGE, number=4, message=struct_pb2.Value,)
    mean_sum = proto.Field(proto.MESSAGE, number=5, message=struct_pb2.Value,)
    mean_count = proto.Field(proto.MESSAGE, number=6, message=struct_pb2.Value,)
    set_ = proto.Field(proto.MESSAGE, number=7, message=struct_pb2.Value,)
    distribution = proto.Field(proto.MESSAGE, number=11, message=struct_pb2.Value,)
    gauge = proto.Field(proto.MESSAGE, number=12, message=struct_pb2.Value,)
    internal = proto.Field(proto.MESSAGE, number=8, message=struct_pb2.Value,)
    update_time = proto.Field(proto.MESSAGE, number=9, message=timestamp_pb2.Timestamp,)


class GetJobMetricsRequest(proto.Message):
    r"""Request to get job metrics.

    Attributes:
        project_id (str):
            A project id.
        job_id (str):
            The job to get metrics for.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Return only metric data that has changed
            since this time. Default is to return all
            information about all metrics for the job.
        location (str):
            The [regional endpoint]
            (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints)
            that contains the job specified by job_id.
    """

    project_id = proto.Field(proto.STRING, number=1,)
    job_id = proto.Field(proto.STRING, number=2,)
    start_time = proto.Field(proto.MESSAGE, number=3, message=timestamp_pb2.Timestamp,)
    location = proto.Field(proto.STRING, number=4,)


class JobMetrics(proto.Message):
    r"""JobMetrics contains a collection of metrics describing the
    detailed progress of a Dataflow job. Metrics correspond to user-
    defined and system-defined metrics in the job.

    This resource captures only the most recent values of each
    metric; time-series data can be queried for them (under the same
    metric names) from Cloud Monitoring.

    Attributes:
        metric_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp as of which metric values are
            current.
        metrics (Sequence[google.cloud.dataflow_v1beta3.types.MetricUpdate]):
            All metrics for this job.
    """

    metric_time = proto.Field(proto.MESSAGE, number=1, message=timestamp_pb2.Timestamp,)
    metrics = proto.RepeatedField(proto.MESSAGE, number=2, message="MetricUpdate",)


class GetJobExecutionDetailsRequest(proto.Message):
    r"""Request to get job execution details.

    Attributes:
        project_id (str):
            A project id.
        job_id (str):
            The job to get execution details for.
        location (str):
            The [regional endpoint]
            (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints)
            that contains the job specified by job_id.
        page_size (int):
            If specified, determines the maximum number
            of stages to return.  If unspecified, the
            service may choose an appropriate default, or
            may return an arbitrarily large number of
            results.
        page_token (str):
            If supplied, this should be the value of next_page_token
            returned by an earlier call. This will cause the next page
            of results to be returned.
    """

    project_id = proto.Field(proto.STRING, number=1,)
    job_id = proto.Field(proto.STRING, number=2,)
    location = proto.Field(proto.STRING, number=3,)
    page_size = proto.Field(proto.INT32, number=4,)
    page_token = proto.Field(proto.STRING, number=5,)


class ProgressTimeseries(proto.Message):
    r"""Information about the progress of some component of job
    execution.

    Attributes:
        current_progress (float):
            The current progress of the component, in the range [0,1].
        data_points (Sequence[google.cloud.dataflow_v1beta3.types.ProgressTimeseries.Point]):
            History of progress for the component.
            Points are sorted by time.
    """

    class Point(proto.Message):
        r"""A point in the timeseries.

        Attributes:
            time (google.protobuf.timestamp_pb2.Timestamp):
                The timestamp of the point.
            value (float):
                The value of the point.
        """

        time = proto.Field(proto.MESSAGE, number=1, message=timestamp_pb2.Timestamp,)
        value = proto.Field(proto.DOUBLE, number=2,)

    current_progress = proto.Field(proto.DOUBLE, number=1,)
    data_points = proto.RepeatedField(proto.MESSAGE, number=2, message=Point,)


class StageSummary(proto.Message):
    r"""Information about a particular execution stage of a job.

    Attributes:
        stage_id (str):
            ID of this stage
        state (google.cloud.dataflow_v1beta3.types.ExecutionState):
            State of this stage.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Start time of this stage.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            End time of this stage.
            If the work item is completed, this is the
            actual end time of the stage. Otherwise, it is
            the predicted end time.
        progress (google.cloud.dataflow_v1beta3.types.ProgressTimeseries):
            Progress for this stage.
            Only applicable to Batch jobs.
        metrics (Sequence[google.cloud.dataflow_v1beta3.types.MetricUpdate]):
            Metrics for this stage.
    """

    stage_id = proto.Field(proto.STRING, number=1,)
    state = proto.Field(proto.ENUM, number=2, enum="ExecutionState",)
    start_time = proto.Field(proto.MESSAGE, number=3, message=timestamp_pb2.Timestamp,)
    end_time = proto.Field(proto.MESSAGE, number=4, message=timestamp_pb2.Timestamp,)
    progress = proto.Field(proto.MESSAGE, number=5, message="ProgressTimeseries",)
    metrics = proto.RepeatedField(proto.MESSAGE, number=6, message="MetricUpdate",)


class JobExecutionDetails(proto.Message):
    r"""Information about the execution of a job.

    Attributes:
        stages (Sequence[google.cloud.dataflow_v1beta3.types.StageSummary]):
            The stages of the job execution.
        next_page_token (str):
            If present, this response does not contain all requested
            tasks. To obtain the next page of results, repeat the
            request with page_token set to this value.
    """

    @property
    def raw_page(self):
        return self

    stages = proto.RepeatedField(proto.MESSAGE, number=1, message="StageSummary",)
    next_page_token = proto.Field(proto.STRING, number=2,)


class GetStageExecutionDetailsRequest(proto.Message):
    r"""Request to get information about a particular execution stage
    of a job. Currently only tracked for Batch jobs.

    Attributes:
        project_id (str):
            A project id.
        job_id (str):
            The job to get execution details for.
        location (str):
            The [regional endpoint]
            (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints)
            that contains the job specified by job_id.
        stage_id (str):
            The stage for which to fetch information.
        page_size (int):
            If specified, determines the maximum number
            of work items to return.  If unspecified, the
            service may choose an appropriate default, or
            may return an arbitrarily large number of
            results.
        page_token (str):
            If supplied, this should be the value of next_page_token
            returned by an earlier call. This will cause the next page
            of results to be returned.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Lower time bound of work items to include, by
            start time.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Upper time bound of work items to include, by
            start time.
    """

    project_id = proto.Field(proto.STRING, number=1,)
    job_id = proto.Field(proto.STRING, number=2,)
    location = proto.Field(proto.STRING, number=3,)
    stage_id = proto.Field(proto.STRING, number=4,)
    page_size = proto.Field(proto.INT32, number=5,)
    page_token = proto.Field(proto.STRING, number=6,)
    start_time = proto.Field(proto.MESSAGE, number=7, message=timestamp_pb2.Timestamp,)
    end_time = proto.Field(proto.MESSAGE, number=8, message=timestamp_pb2.Timestamp,)


class WorkItemDetails(proto.Message):
    r"""Information about an individual work item execution.

    Attributes:
        task_id (str):
            Name of this work item.
        attempt_id (str):
            Attempt ID of this work item
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Start time of this work item attempt.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            End time of this work item attempt.
            If the work item is completed, this is the
            actual end time of the work item.  Otherwise, it
            is the predicted end time.
        state (google.cloud.dataflow_v1beta3.types.ExecutionState):
            State of this work item.
        progress (google.cloud.dataflow_v1beta3.types.ProgressTimeseries):
            Progress of this work item.
        metrics (Sequence[google.cloud.dataflow_v1beta3.types.MetricUpdate]):
            Metrics for this work item.
    """

    task_id = proto.Field(proto.STRING, number=1,)
    attempt_id = proto.Field(proto.STRING, number=2,)
    start_time = proto.Field(proto.MESSAGE, number=3, message=timestamp_pb2.Timestamp,)
    end_time = proto.Field(proto.MESSAGE, number=4, message=timestamp_pb2.Timestamp,)
    state = proto.Field(proto.ENUM, number=5, enum="ExecutionState",)
    progress = proto.Field(proto.MESSAGE, number=6, message="ProgressTimeseries",)
    metrics = proto.RepeatedField(proto.MESSAGE, number=7, message="MetricUpdate",)


class WorkerDetails(proto.Message):
    r"""Information about a worker

    Attributes:
        worker_name (str):
            Name of this worker
        work_items (Sequence[google.cloud.dataflow_v1beta3.types.WorkItemDetails]):
            Work items processed by this worker, sorted
            by time.
    """

    worker_name = proto.Field(proto.STRING, number=1,)
    work_items = proto.RepeatedField(
        proto.MESSAGE, number=2, message="WorkItemDetails",
    )


class StageExecutionDetails(proto.Message):
    r"""Information about the workers and work items within a stage.

    Attributes:
        workers (Sequence[google.cloud.dataflow_v1beta3.types.WorkerDetails]):
            Workers that have done work on the stage.
        next_page_token (str):
            If present, this response does not contain all requested
            tasks. To obtain the next page of results, repeat the
            request with page_token set to this value.
    """

    @property
    def raw_page(self):
        return self

    workers = proto.RepeatedField(proto.MESSAGE, number=1, message="WorkerDetails",)
    next_page_token = proto.Field(proto.STRING, number=2,)


__all__ = tuple(sorted(__protobuf__.manifest))
