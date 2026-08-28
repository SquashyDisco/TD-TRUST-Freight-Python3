TOCS = {}

MESSAGES = {
    "0001": "ACTIVATED",
    "0002": "CANCELLED",
    "0003": "PASS",
    "0004": "_unidentified ",
    "0005": "REINSTATE",
    "0006": "NEWORIGIN",
    "0007": "IDENTITY",
    "0008": "LOCATION"
    }


def print_trust_frame(parsed):
    for a in parsed:
        body = a["body"]

        toc = a["body"].get("toc_id", '')
        platform = a["body"].get("platform", '')
        loc_stanox = a["body"].get("loc_stanox", "")
        actual_timestamp = a["body"].get("actual_timestamp", '')
        variation_status = a["body"].get("variation_status", '')
        lateness = a["body"].get("timetable_variation",'')
        direction = a["body"].get("direction_ind"," ")
        line = a["body"].get("line_ind"," ")
        

        summary = "{}, {}, {:9s}, {:3s}, {:4s}, {}, {:<6s}, {}, {:3s}, {}".format(
            toc,
            body["train_id"][2:6],
            MESSAGES[a["header"]["msg_type"]], platform, direction, line, loc_stanox, actual_timestamp, lateness, variation_status)

        print(summary)
