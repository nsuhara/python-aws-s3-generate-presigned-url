# PythonでAWS-S3の署名付き(期限付き)URLを生成する

## はじめに

`Mac環境の記事ですが、Windows環境も同じ手順になります。環境依存の部分は読み替えてお試しください。`

### 目的

この記事を最後まで読むと、次のことができるようになります。

| No.  | 概要            | キーワード                 |
| :--- | :-------------- | :------------------------- |
| 1    | 署名付きURL生成 | s3, generate_presigned_url |

### 実行環境

| 環境           | Ver.    |
| :------------- | :------ |
| macOS Catalina | 10.15.3 |
| Python         | 3.7.3   |
| boto3          | 1.11.17 |

### ソースコード

実際に実装内容やソースコードを追いながら読むとより理解が深まるかと思います。是非ご活用ください。

[GitHub](https://github.com/nsuhara/python-aws-s3-generate-presigned-url.git)

### 関連する記事

- [Boto 3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html#boto-3-documentation)

## 署名付きURLの生成

```run.py
import os

import boto3

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID', '')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY', '')
region_name = os.getenv('REGION_NAME', '')

bucket = os.getenv('BUCKET', '')
key = os.getenv('KEY', '')
expires_in = os.getenv('EXPIRES_IN', '')  # sec / 1hour = 3600sec.


def main():
    s3 = boto3.client(
        service_name='s3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name
    )

    presigned_url = s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': bucket,
            'Key': key
        },
        ExpiresIn=expires_in,
        HttpMethod='GET'
    )

    print('-----\n{}\n-----'.format(presigned_url))


if __name__ == '__main__':
    main()
```
