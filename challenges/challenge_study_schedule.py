def study_schedule(permanence_period, target_time):
    try:
        students_quantity = 0
        for study_entry, study_exit in permanence_period:
            if study_entry <= target_time <= study_exit:
                students_quantity += 1
        return students_quantity
    except (TypeError):
        return None
