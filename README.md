# Training Provider Enrolments API
[![codecov](https://codecov.io/gh/ACWIC/training-provider-enrolment/branch/main/graph/badge.svg?token=I2PY1FM841)](https://codecov.io/gh/ACWIC/training-provider-enrolment/branch/main)
[![CircleCI](https://circleci.com/gh/ACWIC/training-provider-enrolment.svg?style=svg&circle-token=64b831fa7529e245f0695eca10be3e4af69b7b03)](https://circleci.com/gh/ACWIC/training-provider-enrolment)

This is a reference implementation of a proposed API
enabling Training Providers to interact with Aged Care Providers
(employers) in a standardised way.

Specifically, it provides the endpoints for the training provider to manage
their course catalogue, so that customers (Aged Care Providers i.e. employers)
can search and browse for courses that match their requirements
(using the Training Provider Catalogue service), so that they can
procure training services (using the Training Provider Enrolment service)

This is a companion service to
- [Training Provider Admin](https://github.com/ACWIC/training-provider-admin)
- [Training Provider Catalogue](https://github.com/ACWIC/training-provider-catalogue)

[DEVELOPMENT.md](DEVELOPMENT.md) and [DEPLOYMENT.md](DEPLOYMENT.md)
contain information about running
the software and making changes to it.

There is a test endpoint with a self-documenting API specification
[Dev](https://wpz8gp45w1.execute-api.us-east-1.amazonaws.com/dev/enrolment/docs)
[Prod](https://6l2n6aweqg.execute-api.us-east-1.amazonaws.com/prod/enrolment/docs)

This is equivalent to what you will have running locally
if you create a local development environment
(per [DEVELOPMENT.md](DEVELOPMENT.md))

The test endpoint is continuously deployed
from the `main` branch in this repository, so should be considered unstable.
It is also completely open (do not require authentication),
which is not a realistic simulation of any kind of production environment.
