from typing import Dict
from collections import defaultdict
from datetime import datetime

class ActivityFinder:
    def __init__(self, activities_repository) -> None:
        self.__activities_repository=activities_repository
    def find_from_trip(self, trip_id) -> Dict:
        try:
            activities = self.__activities_repository.find_activities_from_trip(trip_id)
            grouped_activities = defaultdict(list)
            for activity in activities:
                # Convert the string to a datetime object
                occurs_at = datetime.fromisoformat(activity[3]) if isinstance(activity[3], str) else activity[3]
                activity_date = occurs_at.date()
                grouped_activities[activity_date].append({
                    "id": activity[0],
                    "title": activity[2],
                    "occurs_at": occurs_at.isoformat()
                })
            formatted_activities = []
            for date, activities in grouped_activities.items():
                formatted_activities.append({
                    "date": date.isoformat(),
                    "activities": activities
                })
            return {
                "body": formatted_activities,
                "status_code": 200
            }
        except Exception as exception:
                return {
                    "body": {"error": "Bad Request","message":str(exception)},
                    "status_code": 400
                }