# python2
from PIL import Image
import boto3
import json
import os

inputBucket = 'eafit-team5-input'
outputBucket = 'eafit-team5-output'
s3Resource = boto3.resource('s3')
client = boto3.client('rekognition', 'us-east-1')

deb = False


def lambda_handler(event, context):
    dummy()


def dummy():
    for inputImages in s3Resource.Bucket(inputBucket).objects.filter(Prefix='People/'):
        inputPath = inputImages.key
        inputFilename = inputPath.split('/')[-1]
        if len(inputFilename):
            if deb:
                print('File being processed: {}'.format(inputFilename))
                print('  Identifying faces...')
            response = client.detect_faces(
                Image={
                    'S3Object': {
                        'Bucket': inputBucket,
                        'Name': inputPath
                    }
                },
                Attributes=['ALL']
            )

            if deb:
                print('  Gathering original file...')
            inputImage = getImage(inputPath, inputBucket)
            (inputImageWidth, inputImageHeigth) = inputImage.size

            ignored = set()
            for ignoredInput in s3Resource.Bucket(inputBucket).objects.filter(Prefix='Ignored/'):
                if ignoredInput.key[-1] != '/':
                    comparison = client.compare_faces(
                        SimilarityThreshold=70,
                        SourceImage={
                            'S3Object': {
                                'Bucket': inputBucket,
                                'Name': ignoredInput.key
                            }
                        },
                        TargetImage={
                            'S3Object': {
                                'Bucket': inputBucket,
                                'Name': inputPath
                            }
                        }
                    )
                    for faceMatch in comparison['FaceMatches']:
                        ignored.add(json.dumps(faceMatch['Face']['BoundingBox']))

            if deb:
                print('  Processing each face...')
            faceCounter = 1
            for faceDetail in response['FaceDetails']:
                if deb:
                    print('    Processing face {}/{}'.format(faceCounter,
                                                           len(response['FaceDetails'])))
                if json.dumps(faceDetail['BoundingBox']) not in ignored:
                    if deb:
                        print('    Identifying predominant emotion...')
                    detectedEmotion = ''
                    maxValue = -1.0
                    for emotion in faceDetail['Emotions']:
                        confidence = float(emotion['Confidence'])
                        if confidence > maxValue:
                            maxValue = confidence
                            detectedEmotion = emotion['Type'].encode(
                                'ascii', 'ignore').lower()

                    if deb:
                        print('    Identifying face location...')
                    faceUpperLeftX = int(
                        faceDetail['BoundingBox']['Left']*inputImageWidth)
                    faceUpperLeftY = int(
                        faceDetail['BoundingBox']['Top']*inputImageHeigth)
                    faceHeight = int(
                        faceDetail['BoundingBox']['Height']*inputImageHeigth)
                    faceWidth = int(
                        faceDetail['BoundingBox']['Width']*inputImageWidth)

                    if deb:
                        print('    Gathering emoji...')
                    emoji = getImage(
                        'Emojis/'+detectedEmotion+'.png', inputBucket)

                    if deb:
                        print('    Resizing emoji...')
                    emoji = emoji.resize(
                        (faceWidth, faceHeight), Image.ANTIALIAS)

                    if deb:
                        print('    Pasting emoji...')
                    inputImage.paste(
                        emoji, (faceUpperLeftX, faceUpperLeftY), emoji)
                else:
                    if deb:
                        print('    Ignored!')
                faceCounter += 1

            if deb:
                print('  Uploading new file...')
            upload_image(inputImage, inputFilename, outputBucket)

            if deb:
                print('Done with file {}\n'.format(inputFilename))


def getImage(path, bucket):
    locaPath = '/tmp/' + path.split('/')[-1]
    s3Resource.Bucket(bucket).download_file(path, locaPath)
    image = Image.open(locaPath)
    os.remove(locaPath)
    return image


def upload_image(image, filename, bucket):
    tmpPath = '/tmp/' + filename
    image.save(tmpPath)
    boto3.client('s3').upload_file(tmpPath, bucket, filename)
    os.remove(tmpPath)


if deb:
dummy()
