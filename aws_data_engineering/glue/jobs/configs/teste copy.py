import datetime
import os
import yaml

s3_event = {
  "Records": [
    {
      "messageId": "a3f8ee01-58d8-4369-a6ff-908d8951e971",
      "receiptHandle": "AQEBXHsxR48ztjKvJo4L2k+cEej6FErEGvHLDxEMhBsXNVLKvz2mr0lteo61gHfFchHPG+80ktIofbspP7lmDxqxpRVq6w2MN049CJKmd859WXifkKCnN+ds1R+YoevrexwS2/76G15HMhJzGMhuOztf+qgZ2HdRt2FpnYWq48vdViI71hxbzI7AIK6UHf3AeJP8FMYFzSR/P92wKOdVbTlqOQpWe5fqyWZcTFRk5QJvHYyBXUT6e3UU6Wh6HWfQW24hy3WQb3VhOlEdxgwUqBXgkVCRKyALTlkbHUEHr+Q3Y2OxMuyrXjXWnuNtxyoXjrzGYP/MbVkNNSJYb7VGUrlUdicWFywb5c+Qp1T3Am0ZRS9SjTsH/9NRnoi6T1qgp7OC36aBPpzAAiAI75YnD76O5tLsWBDP/eLDMHv0sG3vqDo=",
      "body": {
        "Records": [
          {
            "eventVersion": "2.1",
            "eventSource": "aws:s3",
            "awsRegion": "us-east-1",
            "eventTime": "2024-01-16T16:54:44.685Z",
            "eventName": "ObjectCreated:Put",
            "userIdentity": {
              "principalId": "AWS:AROA36GF25KS4NEPDIFCH:a1645192"
            },
            "requestParameters": {
              "sourceIPAddress": "136.226.53.28"
            },
            "responseElements": {
              "x-amz-request-id": "R8EN1S76JASQPAK8",
              "x-amz-id-2": "scdJAiohkznF5vY2vlWRWa9BhCp5WpRbJH1U/MJUD8KxUASrURF2YQHl8RszcVO+fMMmeIvFcG6NM0zUvf17yaQbt43kV4JS"
            },
            "s3": {
              "s3SchemaVersion": "1.0",
              "configurationId": "grs-datalake-file-sync-s3-sqs-event",
              "bucket": {
                "name": "fdr-staging-bucket-venus-dev",
                "ownerIdentity": {
                  "principalId": "A3SP3B540TS6Z5"
                },
                "arn": "arn:aws:s3:::fdr-staging-bucket-venus-dev"
              },
              "object": {
                "key": "ingestion/inbound/corp/MNB/300_bytes/test.csv",
                "size": 77,
                "eTag": "14d5e65f3bb37ec5505aaa1bea2dd40a",
                "versionId": "z1H61Icmn9gxwDX3gyLloYHv_2utTaC6",
                "sequencer": "0065A6B4D4A2021445"
              }
            }
          }
        ]
      },
      "attributes": {
        "ApproximateReceiveCount": "4",
        "SentTimestamp": "1705424085879",
        "SenderId": "AROA4R74ZO52XAB5OD7T4:S3-PROD-END",
        "ApproximateFirstReceiveTimestamp": "1705424085885"
      },
      "messageAttributes": {},
      "md5OfBody": "c80129ad3a264f576f22ce32855cef0e",
      "eventSource": "aws:sqs",
      "eventSourceARN": "arn:aws:sqs:us-east-1:820753656485:grs-datalake-file-sync-dev-queue",
      "awsRegion": "us-east-1"
    }
  ]
}

list_s3_event = {
  "Records": [
    {
      "messageId": "a3f8ee01-58d8-4369-a6ff-908d8951e971",
      "receiptHandle": "AQEBXHsxR48ztjKvJo4L2k+cEej6FErEGvHLDxEMhBsXNVLKvz2mr0lteo61gHfFchHPG+80ktIofbspP7lmDxqxpRVq6w2MN049CJKmd859WXifkKCnN+ds1R+YoevrexwS2/76G15HMhJzGMhuOztf+qgZ2HdRt2FpnYWq48vdViI71hxbzI7AIK6UHf3AeJP8FMYFzSR/P92wKOdVbTlqOQpWe5fqyWZcTFRk5QJvHYyBXUT6e3UU6Wh6HWfQW24hy3WQb3VhOlEdxgwUqBXgkVCRKyALTlkbHUEHr+Q3Y2OxMuyrXjXWnuNtxyoXjrzGYP/MbVkNNSJYb7VGUrlUdicWFywb5c+Qp1T3Am0ZRS9SjTsH/9NRnoi6T1qgp7OC36aBPpzAAiAI75YnD76O5tLsWBDP/eLDMHv0sG3vqDo=",
      "body": {
        "Records": [
          {
            "eventVersion": "2.1",
            "eventSource": "aws:s3",
            "awsRegion": "us-east-1",
            "eventTime": "2024-01-16T16:54:44.685Z",
            "eventName": "ObjectCreated:Put",
            "userIdentity": {
              "principalId": "AWS:AROA36GF25KS4NEPDIFCH:a1645192"
            },
            "requestParameters": {
              "sourceIPAddress": "136.226.53.28"
            },
            "responseElements": {
              "x-amz-request-id": "R8EN1S76JASQPAK8",
              "x-amz-id-2": "scdJAiohkznF5vY2vlWRWa9BhCp5WpRbJH1U/MJUD8KxUASrURF2YQHl8RszcVO+fMMmeIvFcG6NM0zUvf17yaQbt43kV4JS"
            },
            "s3": {
              "s3SchemaVersion": "1.0",
              "configurationId": "grs-datalake-file-sync-s3-sqs-event",
              "bucket": {
                "name": "fdr-staging-bucket-venus-dev",
                "ownerIdentity": {
                  "principalId": "A3SP3B540TS6Z5"
                },
                "arn": "arn:aws:s3:::fdr-staging-bucket-venus-dev"
              },
              "object": {
                "key": "ingestion/inbound/corp/MNB/300_bytes/test.csv",
                "size": 77,
                "eTag": "14d5e65f3bb37ec5505aaa1bea2dd40a",
                "versionId": "z1H61Icmn9gxwDX3gyLloYHv_2utTaC6",
                "sequencer": "0065A6B4D4A2021445"
              }
            }
          }
        ]
      },
      "attributes": {
        "ApproximateReceiveCount": "4",
        "SentTimestamp": "1705424085879",
        "SenderId": "AROA4R74ZO52XAB5OD7T4:S3-PROD-END",
        "ApproximateFirstReceiveTimestamp": "1705424085885"
      },
      "messageAttributes": {},
      "md5OfBody": "c80129ad3a264f576f22ce32855cef0e",
      "eventSource": "aws:sqs",
      "eventSourceARN": "arn:aws:sqs:us-east-1:820753656485:grs-datalake-file-sync-dev-queue",
      "awsRegion": "us-east-1"
    },
    {
      "messageId": "a3f8ee01-58d8-4369-a6ff-908d8951e971",
      "receiptHandle": "AQEBXHsxR48ztjKvJo4L2k+cEej6FErEGvHLDxEMhBsXNVLKvz2mr0lteo61gHfFchHPG+80ktIofbspP7lmDxqxpRVq6w2MN049CJKmd859WXifkKCnN+ds1R+YoevrexwS2/76G15HMhJzGMhuOztf+qgZ2HdRt2FpnYWq48vdViI71hxbzI7AIK6UHf3AeJP8FMYFzSR/P92wKOdVbTlqOQpWe5fqyWZcTFRk5QJvHYyBXUT6e3UU6Wh6HWfQW24hy3WQb3VhOlEdxgwUqBXgkVCRKyALTlkbHUEHr+Q3Y2OxMuyrXjXWnuNtxyoXjrzGYP/MbVkNNSJYb7VGUrlUdicWFywb5c+Qp1T3Am0ZRS9SjTsH/9NRnoi6T1qgp7OC36aBPpzAAiAI75YnD76O5tLsWBDP/eLDMHv0sG3vqDo=",
      "body": {
        "Records": [
          {
            "eventVersion": "2.1",
            "eventSource": "aws:s3",
            "awsRegion": "us-east-1",
            "eventTime": "2024-01-16T16:54:44.685Z",
            "eventName": "ObjectCreated:Put",
            "userIdentity": {
              "principalId": "AWS:AROA36GF25KS4NEPDIFCH:a1645192"
            },
            "requestParameters": {
              "sourceIPAddress": "136.226.53.28"
            },
            "responseElements": {
              "x-amz-request-id": "R8EN1S76JASQPAK8",
              "x-amz-id-2": "scdJAiohkznF5vY2vlWRWa9BhCp5WpRbJH1U/MJUD8KxUASrURF2YQHl8RszcVO+fMMmeIvFcG6NM0zUvf17yaQbt43kV4JS"
            },
            "s3": {
              "s3SchemaVersion": "1.0",
              "configurationId": "grs-datalake-file-sync-s3-sqs-event",
              "bucket": {
                "name": "fdr-staging-bucket-venus-dev",
                "ownerIdentity": {
                  "principalId": "A3SP3B540TS6Z5"
                },
                "arn": "arn:aws:s3:::fdr-staging-bucket-venus-dev"
              },
              "object": {
                "key": "ingestion/inbound/corp/LNW/300_bytes/test.csv",
                "size": 77,
                "eTag": "14d5e65f3bb37ec5505aaa1bea2dd40a",
                "versionId": "z1H61Icmn9gxwDX3gyLloYHv_2utTaC6",
                "sequencer": "0065A6B4D4A2021445"
              }
            }
          },
          {
            "eventVersion": "2.1",
            "eventSource": "aws:s3",
            "awsRegion": "us-east-1",
            "eventTime": "2024-01-16T16:54:44.685Z",
            "eventName": "ObjectCreated:Put",
            "userIdentity": {
              "principalId": "AWS:AROA36GF25KS4NEPDIFCH:a1645192"
            },
            "requestParameters": {
              "sourceIPAddress": "136.226.53.28"
            },
            "responseElements": {
              "x-amz-request-id": "R8EN1S76JASQPAK8",
              "x-amz-id-2": "scdJAiohkznF5vY2vlWRWa9BhCp5WpRbJH1U/MJUD8KxUASrURF2YQHl8RszcVO+fMMmeIvFcG6NM0zUvf17yaQbt43kV4JS"
            },
            "s3": {
              "s3SchemaVersion": "1.0",
              "configurationId": "grs-datalake-file-sync-s3-sqs-event",
              "bucket": {
                "name": "fdr-staging-bucket-venus-dev",
                "ownerIdentity": {
                  "principalId": "A3SP3B540TS6Z5"
                },
                "arn": "arn:aws:s3:::fdr-staging-bucket-venus-dev"
              },
              "object": {
                "key": "ingestion/inbound/corp/OCG/300_bytes/test.csv",
                "size": 77,
                "eTag": "14d5e65f3bb37ec5505aaa1bea2dd40a",
                "versionId": "z1H61Icmn9gxwDX3gyLloYHv_2utTaC6",
                "sequencer": "0065A6B4D4A2021445"
              }
            }
          }
        ]
      },
      "attributes": {
        "ApproximateReceiveCount": "4",
        "SentTimestamp": "1705424085879",
        "SenderId": "AROA4R74ZO52XAB5OD7T4:S3-PROD-END",
        "ApproximateFirstReceiveTimestamp": "1705424085885"
      },
      "messageAttributes": {},
      "md5OfBody": "c80129ad3a264f576f22ce32855cef0e",
      "eventSource": "aws:sqs",
      "eventSourceARN": "arn:aws:sqs:us-east-1:820753656485:grs-datalake-file-sync-dev-queue",
      "awsRegion": "us-east-1"
    }
  ]
}

failed_sns_event = {
    "Records": [
        {
            "messageId": "5b63c469-09d5-4e7e-84f5-4e29978e120c",
            "receiptHandle": "AQEBX5i6ZFu5rVzbPFXbClb343Ohu4u/hL9wkgeIiBZguQTOMRLW+MAFdWIIrmbY96qhjg5Clf9W+mFdfH5s6puSLPnYeYT7wI+eCHEmDz9OCIzHY7rq20DRXozX62WVkxN7xOyp0JTeP+44sVczS/KfgIVOnHbR6dCIO7t370HRcw7djQiu64+EgcXkj+kJy5mJG+NDSRmIsDdtZPluPxIN7APDa0+TkhK5uiqFiq9pu3bt52C43QV0Iz2XSmwNQRo6FbN9/Zs7ufmxpq11VTVV7Jcm47ii2HvYbozNLSKFCR0uzibI6oFuIfCC/yxyErasJ7OiMYxu984om309sC2vCusIMa6zA9e9j8kone3LyJEThlyAXvhwuVasD+fqjcXi0v4G+TKMTSPVBtVl7CexsvjKsgE9U60y9y+LyFL7xlQ=",
            "body": {
                "Type": "Notification",
                "MessageId": "566dd5b3-a978-5914-96c9-8b93c465e162",
                "TopicArn": "arn:aws:sns:us-east-1:820753656485:grs-datalake-dev-reconciliation-sns",
                "Message": {
                    "file_key": "s3://fdr-bucket/table1",
                    "row_count": 142314
                },
                "Timestamp": "2024-01-16T11:39:09.842Z",
                "SignatureVersion": "1",
                "Signature": "S12Y9wcGW8+EbFiegPqM5ZvMeEpZqDZdgR1zv6l8GMxOqSotXnn8UuziiwzSZkAkxlIkdNlKkqfLB6kSEzFo9MF3W/urp6ErdEIctoF+xCjtwovLGsNYhjqozb5u4xR68sIMz1co0LXMfGRM2euW3DqJ7pbPHcH+P6jJ58WAWrBtgj6B4IlIlsBf/R8iz20xTo4GDdzIiZKzOxMMnOBV8Uv/3aQ8GnUyy9PFoY4K3sTgxFTgabr38z6EdH8hHqI3skJU+G5+jXApYMjDT20TYTfAS3F7zPbgFU1DVJuILnca3ccQyUuQ5bmn3lDDb2SffftJHN6uNSo4Iiya3d3d/Q==",
                "SigningCertURL": "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-60eadc530605d63b8e62a523676ef735.pem",
                "UnsubscribeURL": "https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:820753656485:grs-datalake-dev-reconciliation-sns:51096253-d02a-4bb3-b241-a3dd0c39354a",
                "MessageAttributes": {
                    "stream_name": {
                        "Type": "String",
                        "Value": "stream_test"
                    },
                    "business_unit": {
                        "Type": "String",
                        "Value": "FDR"
                    },
                    "data_source": {
                        "Type": "String",
                        "Value": "table1"
                    }
                }
            },
            "attributes": {
                "ApproximateReceiveCount": "9",
                "SentTimestamp": "1705405149877",
                "SenderId": "AIDAIT2UOQQY3AUEKVGXU",
                "ApproximateFirstReceiveTimestamp": "1705405149879"
            },
            "messageAttributes": {},
            "md5OfBody": "9473504663c4b3b538cb13cc7e0393c4",
            "eventSource": "aws:sqs",
            "eventSourceARN": "arn:aws:sqs:us-east-1:820753656485:grs-datalake-sns-fdr-dataprocessing-dev",
            "awsRegion": "us-east-1"
        }
    ]
}

success_sns_event = {
    "Records": [
        {
            "messageId": "5b63c469-09d5-4e7e-84f5-4e29978e120c",
            "receiptHandle": "AQEBX5i6ZFu5rVzbPFXbClb343Ohu4u/hL9wkgeIiBZguQTOMRLW+MAFdWIIrmbY96qhjg5Clf9W+mFdfH5s6puSLPnYeYT7wI+eCHEmDz9OCIzHY7rq20DRXozX62WVkxN7xOyp0JTeP+44sVczS/KfgIVOnHbR6dCIO7t370HRcw7djQiu64+EgcXkj+kJy5mJG+NDSRmIsDdtZPluPxIN7APDa0+TkhK5uiqFiq9pu3bt52C43QV0Iz2XSmwNQRo6FbN9/Zs7ufmxpq11VTVV7Jcm47ii2HvYbozNLSKFCR0uzibI6oFuIfCC/yxyErasJ7OiMYxu984om309sC2vCusIMa6zA9e9j8kone3LyJEThlyAXvhwuVasD+fqjcXi0v4G+TKMTSPVBtVl7CexsvjKsgE9U60y9y+LyFL7xlQ=",
            "body": {
                "Type": "Notification",
                "MessageId": "566dd5b3-a978-5914-96c9-8b93c465e162",
                "TopicArn": "arn:aws:sns:us-east-1:820753656485:grs-datalake-dev-reconciliation-sns",
                "Message": {
                    "file_key": "s3://fdr-staging-bucket-venus-dev/ingestion/inbound/corp/MNB/300_bytes/table1.csv",
                    "row_count": 142314
                },
                "Timestamp": "2024-01-16T11:39:09.842Z",
                "SignatureVersion": "1",
                "Signature": "S12Y9wcGW8+EbFiegPqM5ZvMeEpZqDZdgR1zv6l8GMxOqSotXnn8UuziiwzSZkAkxlIkdNlKkqfLB6kSEzFo9MF3W/urp6ErdEIctoF+xCjtwovLGsNYhjqozb5u4xR68sIMz1co0LXMfGRM2euW3DqJ7pbPHcH+P6jJ58WAWrBtgj6B4IlIlsBf/R8iz20xTo4GDdzIiZKzOxMMnOBV8Uv/3aQ8GnUyy9PFoY4K3sTgxFTgabr38z6EdH8hHqI3skJU+G5+jXApYMjDT20TYTfAS3F7zPbgFU1DVJuILnca3ccQyUuQ5bmn3lDDb2SffftJHN6uNSo4Iiya3d3d/Q==",
                "SigningCertURL": "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-60eadc530605d63b8e62a523676ef735.pem",
                "UnsubscribeURL": "https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:820753656485:grs-datalake-dev-reconciliation-sns:51096253-d02a-4bb3-b241-a3dd0c39354a",
                "MessageAttributes": {
                    "stream_name": {
                        "Type": "String",
                        "Value": "stream_test"
                    },
                    "business_unit": {
                        "Type": "String",
                        "Value": "FDR"
                    },
                    "data_source": {
                        "Type": "String",
                        "Value": "table1"
                    }
                }
            },
            "attributes": {
                "ApproximateReceiveCount": "9",
                "SentTimestamp": "1705405149877",
                "SenderId": "AIDAIT2UOQQY3AUEKVGXU",
                "ApproximateFirstReceiveTimestamp": "1705405149879"
            },
            "messageAttributes": {},
            "md5OfBody": "9473504663c4b3b538cb13cc7e0393c4",
            "eventSource": "aws:sqs",
            "eventSourceARN": "arn:aws:sqs:us-east-1:820753656485:grs-datalake-sns-fdr-dataprocessing-dev",
            "awsRegion": "us-east-1"
        }
    ]
}

list_success_sns_event = {
    "Records": [
        {
            "messageId": "5b63c469-09d5-4e7e-84f5-4e29978e120c",
            "receiptHandle": "AQEBX5i6ZFu5rVzbPFXbClb343Ohu4u/hL9wkgeIiBZguQTOMRLW+MAFdWIIrmbY96qhjg5Clf9W+mFdfH5s6puSLPnYeYT7wI+eCHEmDz9OCIzHY7rq20DRXozX62WVkxN7xOyp0JTeP+44sVczS/KfgIVOnHbR6dCIO7t370HRcw7djQiu64+EgcXkj+kJy5mJG+NDSRmIsDdtZPluPxIN7APDa0+TkhK5uiqFiq9pu3bt52C43QV0Iz2XSmwNQRo6FbN9/Zs7ufmxpq11VTVV7Jcm47ii2HvYbozNLSKFCR0uzibI6oFuIfCC/yxyErasJ7OiMYxu984om309sC2vCusIMa6zA9e9j8kone3LyJEThlyAXvhwuVasD+fqjcXi0v4G+TKMTSPVBtVl7CexsvjKsgE9U60y9y+LyFL7xlQ=",
            "body": {
                "Type": "Notification",
                "MessageId": "566dd5b3-a978-5914-96c9-8b93c465e162",
                "TopicArn": "arn:aws:sns:us-east-1:820753656485:grs-datalake-dev-reconciliation-sns",
                "Message": {
                    "file_key": "s3://fdr-staging-bucket-venus-dev/ingestion/inbound/corp/OCG/300_bytes/table1.csv",
                    "row_count": 142314
                },
                "Timestamp": "2024-01-16T11:39:09.842Z",
                "SignatureVersion": "1",
                "Signature": "S12Y9wcGW8+EbFiegPqM5ZvMeEpZqDZdgR1zv6l8GMxOqSotXnn8UuziiwzSZkAkxlIkdNlKkqfLB6kSEzFo9MF3W/urp6ErdEIctoF+xCjtwovLGsNYhjqozb5u4xR68sIMz1co0LXMfGRM2euW3DqJ7pbPHcH+P6jJ58WAWrBtgj6B4IlIlsBf/R8iz20xTo4GDdzIiZKzOxMMnOBV8Uv/3aQ8GnUyy9PFoY4K3sTgxFTgabr38z6EdH8hHqI3skJU+G5+jXApYMjDT20TYTfAS3F7zPbgFU1DVJuILnca3ccQyUuQ5bmn3lDDb2SffftJHN6uNSo4Iiya3d3d/Q==",
                "SigningCertURL": "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-60eadc530605d63b8e62a523676ef735.pem",
                "UnsubscribeURL": "https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:820753656485:grs-datalake-dev-reconciliation-sns:51096253-d02a-4bb3-b241-a3dd0c39354a",
                "MessageAttributes": {
                    "stream_name": {
                        "Type": "String",
                        "Value": "stream_test"
                    },
                    "business_unit": {
                        "Type": "String",
                        "Value": "FDR"
                    },
                    "data_source": {
                        "Type": "String",
                        "Value": "table1"
                    }
                }
            },
            "attributes": {
                "ApproximateReceiveCount": "9",
                "SentTimestamp": "1705405149877",
                "SenderId": "AIDAIT2UOQQY3AUEKVGXU",
                "ApproximateFirstReceiveTimestamp": "1705405149879"
            },
            "messageAttributes": {},
            "md5OfBody": "9473504663c4b3b538cb13cc7e0393c4",
            "eventSource": "aws:sqs",
            "eventSourceARN": "arn:aws:sqs:us-east-1:820753656485:grs-datalake-sns-fdr-dataprocessing-dev",
            "awsRegion": "us-east-1"
        },
        {
            "messageId": "5b63c469-09d5-4e7e-84f5-4e29978e120c",
            "receiptHandle": "AQEBX5i6ZFu5rVzbPFXbClb343Ohu4u/hL9wkgeIiBZguQTOMRLW+MAFdWIIrmbY96qhjg5Clf9W+mFdfH5s6puSLPnYeYT7wI+eCHEmDz9OCIzHY7rq20DRXozX62WVkxN7xOyp0JTeP+44sVczS/KfgIVOnHbR6dCIO7t370HRcw7djQiu64+EgcXkj+kJy5mJG+NDSRmIsDdtZPluPxIN7APDa0+TkhK5uiqFiq9pu3bt52C43QV0Iz2XSmwNQRo6FbN9/Zs7ufmxpq11VTVV7Jcm47ii2HvYbozNLSKFCR0uzibI6oFuIfCC/yxyErasJ7OiMYxu984om309sC2vCusIMa6zA9e9j8kone3LyJEThlyAXvhwuVasD+fqjcXi0v4G+TKMTSPVBtVl7CexsvjKsgE9U60y9y+LyFL7xlQ=",
            "body": {
                "Type": "Notification",
                "MessageId": "566dd5b3-a978-5914-96c9-8b93c465e162",
                "TopicArn": "arn:aws:sns:us-east-1:820753656485:grs-datalake-dev-reconciliation-sns",
                "Message": {
                    "file_key": "s3://fdr-staging-bucket-venus-dev/ingestion/inbound/corp/LNW/300_bytes/table1.csv",
                    "row_count": 142314
                },
                "Timestamp": "2024-01-16T11:39:09.842Z",
                "SignatureVersion": "1",
                "Signature": "S12Y9wcGW8+EbFiegPqM5ZvMeEpZqDZdgR1zv6l8GMxOqSotXnn8UuziiwzSZkAkxlIkdNlKkqfLB6kSEzFo9MF3W/urp6ErdEIctoF+xCjtwovLGsNYhjqozb5u4xR68sIMz1co0LXMfGRM2euW3DqJ7pbPHcH+P6jJ58WAWrBtgj6B4IlIlsBf/R8iz20xTo4GDdzIiZKzOxMMnOBV8Uv/3aQ8GnUyy9PFoY4K3sTgxFTgabr38z6EdH8hHqI3skJU+G5+jXApYMjDT20TYTfAS3F7zPbgFU1DVJuILnca3ccQyUuQ5bmn3lDDb2SffftJHN6uNSo4Iiya3d3d/Q==",
                "SigningCertURL": "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-60eadc530605d63b8e62a523676ef735.pem",
                "UnsubscribeURL": "https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:820753656485:grs-datalake-dev-reconciliation-sns:51096253-d02a-4bb3-b241-a3dd0c39354a",
                "MessageAttributes": {
                    "stream_name": {
                        "Type": "String",
                        "Value": "stream_test"
                    },
                    "business_unit": {
                        "Type": "String",
                        "Value": "FDR"
                    },
                    "data_source": {
                        "Type": "String",
                        "Value": "table1"
                    }
                }
            },
            "attributes": {
                "ApproximateReceiveCount": "9",
                "SentTimestamp": "1705405149877",
                "SenderId": "AIDAIT2UOQQY3AUEKVGXU",
                "ApproximateFirstReceiveTimestamp": "1705405149879"
            },
            "messageAttributes": {},
            "md5OfBody": "9473504663c4b3b538cb13cc7e0393c4",
            "eventSource": "aws:sqs",
            "eventSourceARN": "arn:aws:sqs:us-east-1:820753656485:grs-datalake-sns-fdr-dataprocessing-dev",
            "awsRegion": "us-east-1"
        }
    ]
}

def load_config() -> dict:

    config_path = f'test.yaml'
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    
    return config


def search_key_in_dict(data: dict, search_key: str) -> str:

    if not isinstance(data, dict):
        return None

    if search_key in data:
        return data[search_key]

    for value in data.values():
        result = search_key_in_dict(value, search_key)
        if result is not None:
            return result  # return the result if the key is found in nested dictionaries
    
    return None # the search_key was not found


def split_s3_path(s3_path: str) -> tuple[str]:
    
    path_parts = s3_path.replace('s3://', '').split('/')
    bucket = path_parts.pop(0)
    key = '/'.join(path_parts)
    
    return bucket, key
    

def capture_files_from_sns(event: dict) -> list[str]:
    
    keys_candidates = ['file_key']
    
    i = 0
    while not search_key_in_dict(event['Records'][0]['body']['Message'], keys_candidates[i]):
        print(f'Key {keys_candidates[i]} was not found')
        i += 1
    print(f'INFO: key {keys_candidates[i]} was found')
    
    keyword = keys_candidates[i]
    
    files_paths = []
    for record in event['Records']:
        keyword_value = search_key_in_dict(record['body']['Message'], keyword)
        # bucket, key = split_s3_path(keyword_value)
        files_paths.append(keyword_value)
        
    return files_paths


def capture_files_from_s3(event: dict) -> tuple[str, list[dict]]:

    files_paths = []

    for record in event.get('Records', []):
        body_records = record.get('body', {}).get('Records', [])  
        
        for body_record in body_records:

            s3_record = body_record.get('s3')
            
            bucket = s3_record.get('bucket', {}).get('name')
            key = s3_record.get('object', {}).get('key')
            
            files_paths.append(f's3://{bucket}/{key}')
            

    return files_paths


def search_source_trigger(event: dict) -> str:

    message_body = event['Records'][0]['body']

    if 'Records' in event and 'TopicArn' in message_body:
        return 'sns'
    elif 'Records' in event and 'eventName' in message_body['Records'][0].keys() and 's3' in message_body['Records'][0]['eventSource'].lower():
        return 's3'
    else:
        raise Exception('source type not identified')
    

def copy_object_to_raw(source_file_path: str, destination_file_path: str) -> None:
        
    source_bucket, source_key = split_s3_path(source_file_path)
    destination_bucket, destination_key = split_s3_path(destination_file_path)

    try:      
        print(f"INFO: File copied from {source_file_path} to {destination_file_path}!")
        
    except Exception as e: 
        raise Exception(f"ERROR: Copy file from {source_file_path} to {destination_file_path} failed due {e}")


def formatting_destination_path(config: dict) -> str:

    if config['destination_partition_flag']:

        now = datetime.datetime.now()
        year = now.strftime("yyyy")
        month = now.strftime("mm")
        day = now.strftime("dd")

        formatted_destination_path = f"{config['destination_bucket']}/{config['business_unit']}/{config['data_source']}/year={year}/month={month}/day={day}/"
    else: 
        formatted_destination_path = f"{config['destination_bucket']}/{config['business_unit']}/{config['data_source']}"

    return formatted_destination_path


def handler(event, context):

    # print(event)

    event_record = event['Records'][0]
    source_type = search_source_trigger(event)

    if source_type == 'sns':
        list_source_file_paths = capture_files_from_sns(event)
        
    elif source_type == 's3':
        list_source_file_paths = capture_files_from_s3(event)
  
    # if files_paths:
    #     raise(f'ERROR: File path of S3 is empty, please check the event that arrived  - {event}')

    config = load_config()

    destination_config_source_paths = [source_config['source_path'] for source_config in config]
    destination_config_source_buckets = [source_config['source_bucket'] for source_config in config]

    for source_file_path in list_source_file_paths:

        bucket, key = split_s3_path(source_file_path)

        # search for the config of the source_file_path
        key_validation_flag = list(map(lambda config_source_path: config_source_path in key, destination_config_source_paths))
        
        if bucket in destination_config_source_buckets and any(key_validation_flag):
            
            # get the right config from a list of configs
            
            specific_config = config[key_validation_flag.index(True)]

            # print(f'INFO: configs chosen {specific_config}')

            # adding partition substring if flagged
            destination_file_path = formatting_destination_path(specific_config)
            
            copy_object_to_raw(source_file_path, destination_file_path)
        else: 
            raise Exception(f"Configs to {source_file_path} not found in configs file")
                    
        


handler(s3_event, None)
print(40*'-')
handler(list_s3_event, None)
print(40*'-')
handler(success_sns_event, None)
print(40*'-')
handler(list_success_sns_event, None)
print(40*'-')
handler(failed_sns_event, None)