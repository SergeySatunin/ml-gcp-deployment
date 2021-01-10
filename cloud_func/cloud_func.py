model = None


def pred(request):
    from google.cloud import storage
    import pickle as pk
    import pandas as pd
    from flask import jsonify

    global model
    if not model:
        bucket_name = "model_store_bucket"
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)

        blob = bucket.blob("model.pkl")
        blob.download_to_filename("/tmp/model.pkl")
        model = pk.load(open("/tmp/model.pkl", 'rb'))

    data = {"success": False}
    params = request.get_json()

    if "G1" in params:
        new_row = {"G1": params.get("G1"), "G2": params.get("G2"),
                   "G3": params.get("G3"), "G4": params.get("G4"),
                   "G5": params.get("G5"), "G6": params.get("G6"),
                   "G7": params.get("G7"), "G8": params.get("G8"),
                   "G9": params.get("G9"), "G10": params.get("G10")}

        new_x = pd.DataFrame.from_dict(new_row, orient="index").transpose()

        data["response"] = str(model.predict_proba(new_x)[0][1])
        data["success"] = True

    return jsonify(data)