from fastapi import FastAPI
import json
#

app = FastAPI()

def read_posts(data,search,page_num: int = 1, page_size: int = 10):
    start = (page_num - 1) * page_size
    end = start + page_size
    data_length = len(data)
    response = {
        "data": data[start:end],
        "total": data_length,
        "count": page_size,
        "pagination": {}
    }

    if end >= data_length:
        response["pagination"]["next"] = None

        if page_num > 1:
            response["pagination"]["previous"] = f"/search-keywords?page_num={page_num-1}&page_size={page_size}&search={search}"
        else:
            response["pagination"]["previous"] = None
    else:
        if page_num > 1:
            response["pagination"]["previous"] = f"/search-keywords?page_num={page_num-1}&page_size={page_size}&search={search}"
        else:
            response["pagination"]["previous"] = None

        response["pagination"]["next"] = f"/search-keywords?page_num={page_num+1}&page_size={page_size}&search={search}"

    return response