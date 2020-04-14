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
    num_of_days = get_period_days(input_data.get('data').get('periodType'), input_data.get('data').get('timeToElapse'))
    num_of_days = int(num_of_days / 3)
    reportedCases = int(input_data.get('data').get('reportedCases'))
    output_data = {}
    impact = {}
    severe_impact = {}

    currently_infected_impact = reportedCases * 10
    infections_by_requested_time_impact = int(currently_infected_impact * math.pow(2, num_of_days))
    currently_infected_severe_impact = reportedCases * 50
    infections_by_requested_time_severe_impact = int(currently_infected_severe_impact * math.pow(2, num_of_days))

    impact['currentlyInfected'] = currently_infected_impact
    impact['infectionsByRequestedTime'] = infections_by_requested_time_impact
    severe_impact['currentlyInfected'] = currently_infected_severe_impact
    severe_impact['infectionsByRequestedTime'] = infections_by_requested_time_severe_impact

    output_data['estimate'] = {}
    output_data['estimate'].update({"impact":impact})
    output_data['estimate'].update({"severeImpact":severe_impact})
    return output_data