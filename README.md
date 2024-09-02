API Documentation
1. State Coverage Comparison API
Base URL: https://usstatecoverageapi.onrender.com

Endpoints
POST /state-coverage-comparison/

Request:

json
Copy code
{
    "carriers": ["UPS", "FedEx"]
}
Response:

json
Copy code
{
    "UPS": {"Alabama": 0.85, "Alaska": 0.72, ...},
    "FedEx": {"Alabama": 0.88, "Alaska": 0.75, ...}
}
GET /

Response:

json
Copy code
{
    "message": "Welcome to the State Coverage Comparison API!"
}
2. Customer Sentiment Comparison API
Base URL: https://sentimentapi-vq9g.onrender.com

Endpoints
POST /customer-sentiment-comparison/

Request:

json
Copy code
{
    "carriers": ["UPS", "FedEx"]
}
Response:

json
Copy code
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

json
Copy code
{
    "message": "Welcome to the Customer Sentiment Comparison API!"
}
3. Carrier Interactive Comparison API
Base URL: https://nteractivecarriercomparisonapi.onrender.com

Endpoints
POST /carrier-interactive-comparison/

Request:

json
Copy code
{
    "carriers": ["UPS", "FedEx"]
}
Response:

json
Copy code
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

json
Copy code
{
    "message": "Welcome to the Carrier Interactive Comparison API!"
}
4. Shipping Cost Comparison API
Base URL: https://shippingcostapi.onrender.com

Endpoints
POST /shipping-cost-comparison/

Request:

json
Copy code
{
    "carriers": ["UPS", "FedEx"],
    "num_examples": 5
}
Response:

json
Copy code
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

json
Copy code
{
    "message": "Welcome to the Shipping Cost Comparison API!"
}
5. Carrier Rate Comparison API
Base URL: https://carrierratecomparisonapi.onrender.com

Endpoints
POST /carrier-rate-comparison/

Request:

json
Copy code
{
    "carriers": ["UPS", "FedEx"],
    "years": 4
}
Response:

json
Copy code
{
    "data": [
        {"year": 2020, "UPS": 3.2, "FedEx": 2.8},
        {"year": 2021, "UPS": 4.5, "FedEx": 3.1},
        ...
    ]
}
GET /

Response:

json
Copy code
{
    "message": "Welcome to the Carrier Rate Comparison API!"
}
How to Interact with These APIs
Send a POST request to the appropriate endpoint with a JSON body specifying the carriers or other parameters.
Receive a JSON response with the requested comparison data.
Use the GET / endpoint to verify the API is running and to receive a welcome message.
Note: The structure and fields of the response are consistent across these APIs, designed for easy integration into your applications.
