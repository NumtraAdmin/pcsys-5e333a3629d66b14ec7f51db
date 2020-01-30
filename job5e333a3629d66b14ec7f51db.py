import traceback
import sys
from operations import TopOperation
from operations import JoinOperation
from operations import AggregationOperation
from operations import FormulaOperation
from operations import FilterOperation
from connectors import DBFSConnector
from connectors import CosmosDBConnector
from datatransformations import TranformationsMainFlow
from automl import tpot_execution
from core import PipelineNotification
import json

try: 
	PipelineNotification.PipelineNotification().started_notification('5e333a3629d66b14ec7f51dc','567a95c8ca676c1d07d5e3e7','http://104.40.91.74:3200/pipeline/notify')
	pcsystemtest_DBFS = DBFSConnector.DBFSConnector.fetch([], {}, "5e333a3629d66b14ec7f51dc", spark, "{'url': '/Demo/PredictiveChurnTrain.csv', 'file_type': 'Delimeted', 'dbfs_token': 'dapi743e2d3cc92a32916f8c2fa9bd7d0606', 'dbfs_domain': 'westus.azuredatabricks.net', 'delimiter': ',', 'is_header': 'Use Header Line'}")

	PipelineNotification.PipelineNotification().completed_notification('5e333a3629d66b14ec7f51dc','567a95c8ca676c1d07d5e3e7','http://104.40.91.74:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5e333a3629d66b14ec7f51dc','567a95c8ca676c1d07d5e3e7','http://104.40.91.74:3200/pipeline/notify','http://104.40.91.74:3200/logs/getProductLogs')
	sys.exit(1)
try: 
	PipelineNotification.PipelineNotification().started_notification('5e333a3629d66b14ec7f51dd','567a95c8ca676c1d07d5e3e7','http://104.40.91.74:3200/pipeline/notify')
	pcsystemtest_AutoFE = TranformationsMainFlow.TramformationMain.run(["5e333a3629d66b14ec7f51dc"],{"5e333a3629d66b14ec7f51dc": pcsystemtest_DBFS}, "5e333a3629d66b14ec7f51dd", spark,json.dumps( {"FE": [{"transformationsData": {"feature_label": "State"}, "feature": "State", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "3332", "mean": "", "stddev": "", "min": "AK", "max": "WY", "missing": "0", "distinct": "51"}, "transformation": "String Indexer"}, {"transformationsData": {}, "feature": "Account_Length", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "3332", "mean": "101.06", "stddev": "39.83", "min": "1", "max": "243", "missing": "0"}}, {"transformationsData": {}, "feature": "Area_Code", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "3332", "mean": "437.19", "stddev": "42.38", "min": "408", "max": "510", "missing": "0"}}, {"transformationsData": {"feature_label": "Phone"}, "feature": "Phone", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "3332", "mean": "", "stddev": "", "min": "327-1058", "max": "422-9964", "missing": "0", "distinct": "321"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "Intl_Plan"}, "feature": "Intl_Plan", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "3332", "mean": "", "stddev": "", "min": "no", "max": "yes", "missing": "0", "distinct": "2"}, "transformation": "String Indexer"}, {"transformationsData": {"feature_label": "VMail_Plan"}, "feature": "VMail_Plan", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "3332", "mean": "", "stddev": "", "min": "no", "max": "yes", "missing": "0", "distinct": "2"}, "transformation": "String Indexer"}, {"transformationsData": {}, "feature": "VMail_Message", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "3332", "mean": "8.09", "stddev": "13.69", "min": "0", "max": "51", "missing": "0"}}, {"transformationsData": {}, "feature": "Day_Mins", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "3332", "mean": "179.75", "stddev": "54.46", "min": "0.0", "max": "350.8", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "Day_Calls", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "3332", "mean": "100.43", "stddev": "20.07", "min": "0", "max": "165", "missing": "0"}}, {"transformationsData": {}, "feature": "Day_Charge", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "3332", "mean": "30.56", "stddev": "9.26", "min": "0.0", "max": "59.64", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "Eve_Mins", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "3332", "mean": "200.98", "stddev": "50.72", "min": "0.0", "max": "363.7", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "Eve_Calls", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "3332", "mean": "100.11", "stddev": "19.93", "min": "0", "max": "170", "missing": "0"}}, {"transformationsData": {}, "feature": "Eve_Charge", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "3332", "mean": "17.08", "stddev": "4.31", "min": "0.0", "max": "30.91", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "Night_Mins", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "3332", "mean": "200.86", "stddev": "50.58", "min": "23.2", "max": "395.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "Night_Calls", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "3332", "mean": "100.11", "stddev": "19.57", "min": "33", "max": "175", "missing": "0"}}, {"transformationsData": {}, "feature": "Night_Charge", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "3332", "mean": "9.04", "stddev": "2.28", "min": "1.04", "max": "17.77", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "Intl_Mins", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "3332", "mean": "10.24", "stddev": "2.79", "min": "0.0", "max": "20.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "total_Mins", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "3332", "mean": "591.83", "stddev": "89.94", "min": "284.3", "max": "885.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "Intl_Calls", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "3332", "mean": "4.48", "stddev": "2.46", "min": "0", "max": "20", "missing": "0"}}, {"transformationsData": {}, "feature": "Intl_Charge", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "3332", "mean": "2.76", "stddev": "0.75", "min": "0.0", "max": "5.4", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "Total_Charge", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "3332", "mean": "59.44", "stddev": "10.5", "min": "22.93", "max": "96.15", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "CustServ_Calls", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "3332", "mean": "1.56", "stddev": "1.32", "min": "0", "max": "9", "missing": "0"}}, {"transformationsData": {}, "feature": "Churn", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "3332", "mean": "0.14", "stddev": "0.35", "min": "0", "max": "1", "missing": "0"}}, {"transformationsData": {"feature_label": "cluster_labels"}, "feature": "cluster_labels", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "3332", "mean": "", "stddev": "", "min": "day_callers", "max": "vmailers", "missing": "0", "distinct": "6"}, "transformation": "String Indexer"}, {"feature": "State_transform", "transformation": "", "transformationsData": {}, "type": "real", "selected": "True", "stats": {"count": "321", "mean": "19.07", "stddev": "13.8", "min": "0.0", "max": "50.0", "missing": "0"}}, {"feature": "Phone_transform", "transformation": "", "transformationsData": {}, "type": "real", "selected": "True", "stats": {"count": "321", "mean": "160.0", "stddev": "92.81", "min": "0.0", "max": "320.0", "missing": "0"}}, {"feature": "Intl_Plan_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "321", "mean": "0.12", "stddev": "0.33", "min": "0", "max": "1", "missing": "0"}}, {"feature": "VMail_Plan_transform", "transformation": "", "transformationsData": {}, "type": "numeric", "selected": "True", "stats": {"count": "321", "mean": "0.28", "stddev": "0.45", "min": "0", "max": "1", "missing": "0"}}, {"feature": "cluster_labels_transform", "transformation": "", "transformationsData": {}, "type": "real", "selected": "True", "stats": {"count": "321", "mean": "2.35", "stddev": "1.7", "min": "0.0", "max": "5.0", "missing": "0"}}]}))

	PipelineNotification.PipelineNotification().completed_notification('5e333a3629d66b14ec7f51dd','567a95c8ca676c1d07d5e3e7','http://104.40.91.74:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5e333a3629d66b14ec7f51dd','567a95c8ca676c1d07d5e3e7','http://104.40.91.74:3200/pipeline/notify','http://104.40.91.74:3200/logs/getProductLogs')
	sys.exit(1)
try: 
	PipelineNotification.PipelineNotification().started_notification('5e333a3629d66b14ec7f51de','567a95c8ca676c1d07d5e3e7','http://104.40.91.74:3200/pipeline/notify')
	pcsystemtest_AutoML = tpot_execution.Tpot_execution.run(["5e333a3629d66b14ec7f51dd"],{"5e333a3629d66b14ec7f51dd": pcsystemtest_AutoFE}, "5e333a3629d66b14ec7f51de", spark,json.dumps( {"model_type": "classification", "label": "Churn", "features": ["State", "Account_Length", "Area_Code", "Phone", "Intl_Plan", "VMail_Plan", "VMail_Message", "Day_Mins", "Day_Calls", "Day_Charge", "Eve_Mins", "Eve_Calls", "Eve_Charge", "Night_Mins", "Night_Calls", "Night_Charge", "Intl_Mins", "total_Mins", "Intl_Calls", "Intl_Charge", "Total_Charge", "CustServ_Calls", "cluster_labels"], "percentage": "10", "executionTime": "5", "sampling": "1", "sampling_value": "over", "run_id": "", "ProjectName": "Retail Scenarios", "PipelineName": "pcsystemtesthh", "userid": "567a95c8ca676c1d07d5e3e7", "runid": "", "url_ResultView": "http://104.40.91.74:3200", "experiment_id": "895518857185768"}))

	PipelineNotification.PipelineNotification().completed_notification('5e333a3629d66b14ec7f51de','567a95c8ca676c1d07d5e3e7','http://104.40.91.74:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5e333a3629d66b14ec7f51de','567a95c8ca676c1d07d5e3e7','http://104.40.91.74:3200/pipeline/notify','http://104.40.91.74:3200/logs/getProductLogs')
	sys.exit(1)

