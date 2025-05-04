from constant import BASE_URL

import requests

class ApiData:
    def __init__(self):
        self.api_url = BASE_URL

    def get_all_meetings(self):
        """Meeting Provides information about meetings.A meeting refers to a Grand Prix or testing weekend and usually 
        includes multiple sessions (practice, qualifying, race, ...)."""
    
        meeting_endpoint = f"{self.api_url}/meetings"

        all_meetings = requests.get(meeting_endpoint)

        if all_meetings.status_code != 200:
            raise Exception(f"Error fetching data: {all_meetings.status_code}")
        
        return all_meetings.json()
    
    def get_meeting_info(self, meeting_id):
        """Meeting Provides information about meetings.A meeting refers to a Grand Prix or testing weekend and usually 
        includes multiple sessions (practice, qualifying"""

    def fetch_data(self):
        # Simulate fetching data from the API
        print(f"Fetching data from {self.api_url}")
        return {"data": "sample data from API from this base url "}
    

if __name__ == "__main__":
    api_data = ApiData()
    data = api_data.get_all_meetings()
    print(data)  