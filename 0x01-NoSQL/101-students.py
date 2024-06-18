#!/usr/bin/env python3
"""" returns all studnets sorted by average score"""


def top_students(mongo_collection):
    """Returns all students sorted by average"""

    pipeline = [
        {
            "$project": {
                "name": 1,
                "averageScore": {"$avg": "$scores.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]

    return list(mongo_collection.aggregate(pipeline))
