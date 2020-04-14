import math

def estimator(data):
  return data


def get_period_days(period_type, period_days):
    if period_type.lower() == 'days':
      return period_days
    elif period_type.lower() == 'weeks':
      return period_days * 7
    elif period_type.lower() == 'months':
      return period_days * 30
    return "Invalid Period Type"


def impact_estimator(input_data):
    num_of_days = get_period_days(input_data.get('periodType'), input_data.get('timeToElapse'))
    num_of_days = int(num_of_days / 3)
    output_data = {}
    impact = {}
    severe_impact = {}

    currently_infected_impact = int(input_data.get('reportedCases') * 10)
    infections_by_requested_time_impact = int(currently_infected_impact * math.pow(2, num_of_days))
    currently_infected_severe_impact = int(input_data.get('reportedCases') * 50)
    infections_by_requested_time_severe_impact = int(currently_infected_severe_impact * math.pow(2, num_of_days))

    impact['currentlyInfected'] = currently_infected_impact
    impact['infectionsByRequestedTime'] = infections_by_requested_time_impact
    severe_impact['currentlyInfected'] = currently_infected_severe_impact
    severe_impact['infectionsByRequestedTime'] = infections_by_requested_time_severe_impact

    output_data['data'] = input_data
    output_data['impact'] = impact
    output_data['severe_impact'] = severe_impact

    return output_data