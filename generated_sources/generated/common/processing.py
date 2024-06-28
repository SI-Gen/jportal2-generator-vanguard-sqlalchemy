def process_bind_params(session, types, params):
    processed_params = []
    dialect = session.bind.dialect

    for i in range(len(params)):
        i_type = types[i]
        if hasattr(i_type, "process_bind_param_cls"):
            processed_params.append(i_type.process_bind_param_cls(params[i], dialect))
        else:
            processed_params.append(params[i])

    return processed_params


def process_result_rec(cls, session, types, rec):
    processed_rec = []
    dialect = session.bind.dialect

    for i in range(len(rec)):
        i_type = types[i]
        if hasattr(i_type, "process_result_value_cls"):
            processed_rec.append(i_type.process_result_value_cls(rec[i], dialect))
        else:
            processed_rec.append(rec[i])

    return cls(*processed_rec)


def process_result_recs(cls, session, types, recs):
    return [process_result_rec(cls, session, types, r) for r in recs]
