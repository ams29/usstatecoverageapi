API Documentation

1. State Coverage Comparison API
Base URL: https://usstatecoverageapi.onrender.com

Endpoints
POST /state-coverage-comparison/

Request:
{
    "carriers": ["UPS", "FedEx"]
}

Response:
{
    "UPS": {"Alabama": 0.85, "Alaska": 0.72, ...},
    "FedEx": {"Alabama": 0.88, "Alaska": 0.75, ...}
}

GET /

Response:
{
    "message": "Welcome to the State Coverage Comparison API!"
}

---

2. Customer Sentiment Comparison API
Base URL: https://sentimentapi-vq9g.onrender.com

Endpoints
POST /customer-sentiment-comparison/

Request:
{
    "carriers": ["UPS", "FedEx"]
}

Response:
{
    "UPS": [
        {"attribute": "Customer Service", "score": 85},
        {"attribute": "On-time Delivery", "score": 90},
        ...
    ],
    "FedEx": [
        {"attribute": "Customer Service", "score": 80},
        {"attribute": "On-time Delivery", "score": 85},
        ...
    ]
}

GET /

Response:
{
    "message": "Welcome to the Customer Sentiment Comparison API!"
}

---

3. Carrier Interactive Comparison API
Base URL: https://nteractivecarriercomparisonapi.onrender.com

Endpoints
POST /carrier-interactive-comparison/

Request:
{
    "carriers": ["UPS", "FedEx"]
}

Response:
{
    "data": [
        {
            "name": "UPS",
            "onboardingTime": 2,
            "trackingCapabilities": "Advanced",
            "sustainabilityScore": 85
        },
        {
            "name": "FedEx",
            "onboardingTime": 3,
            "trackingCapabilities": "Intermediate",
            "sustainabilityScore": 78
        }
    ]
}

GET /

Response:
{
    "message": "Welcome to the Carrier Interactive Comparison API!"
}

---

4. Shipping Cost Comparison API
Base URL: https://shippingcostapi.onrender.com

Endpoints
POST /shipping-cost-comparison/

Request:
{
    "carriers": ["UPS", "FedEx"],
    "num_examples": 5
}

Response:
{
    "data": [
        {
            "Distance": "Zone 1",
            "fedex": 12.04,
            "ups": 6.99,
            "usps": 6.77,
            "orchestro": 5.85
        },
        ...
    ]
}

GET /

Response:
{
    "message": "Welcome to the Shipping Cost Comparison API!"
}

---

5. Carrier Rate Comparison API
Base URL: https://carrierratecomparisonapi.onrender.com

Endpoints
POST /carrier-rate-comparison/

Request:
{
    "carriers": ["UPS", "FedEx"],
    "years": 4
}

Response:
{
    "data": [
        {"year": 2020, "UPS": 3.2, "FedEx": 2.8},
        {"year": 2021, "UPS": 4.5, "FedEx": 3.1},
        ...
    ]
}

GET /

Response:
{
    "message": "Welcome to the Carrier Rate Comparison API!"
}

---

How to Interact with These APIs
1. Send a POST request to the appropriate endpoint with a JSON body specifying the carriers or other parameters.
2. Receive a JSON response with the requested comparison data.
3. Use the GET / endpoint to verify the API is running and to receive a welcome message.

Note: The structure and fields of the response are consistent across these APIs, designed for easy integration into your applications.
