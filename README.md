# bioverse-positions
Within `bioverse` we want to provide an easily usable map of species positions. `iNaturalist` already has all of this information but unfortunately they have serious limits on their API (60 requests per second) that would absolutely hinder scalability. Therefore we're going to build out our own API for this. 

## Running the API
```bash
cd bioverse-positions
python app.py
```

You can use Postman for testing. 