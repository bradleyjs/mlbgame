#!/usr/bin/env python

import unittest


class TestStandings(unittest.TestCase):
    
    def test_standings(self):
        import mlbgame
        from datetime import datetime
        standings = mlbgame.standings()
        self.assertEqual(standings.standings_schedule_date, 'standings_schedule_date')
        self.assertIsInstance(standings.last_update, datetime)
        self.assertIsInstance(standings.divisions, list)
        for division in standings.divisions:
            self.assertIsInstance(division.name, str)
            self.assertIsInstance(division.teams, list)
            for team in division.teams:
                self.assertIsInstance(team.away, str)
                self.assertIsInstance(team.clinched_sw, str)
                self.assertIsInstance(team.division, str)
                self.assertIsInstance(team.division_champ, str)
                self.assertIsInstance(team.division_id, int)
                self.assertIsInstance(team.division_odds, float)
                self.assertIsInstance(team.elim, (str, int))
                self.assertIsInstance(team.elim_wildcard, (str, int))
                self.assertIsInstance(team.extra_inn, str)
                self.assertIsInstance(team.file_code, str)
                self.assertIsInstance(team.gb, (str, float))
                self.assertIsInstance(team.gb_wildcard, (str, float))
                self.assertIsInstance(team.home, str)
                self.assertIsInstance(team.interleague, str)
                self.assertIsInstance(team.is_wildcard_sw, str)
                self.assertIsInstance(team.l, int)
                self.assertIsInstance(team.last_ten, str)
                self.assertIsInstance(team.one_run, str)
                self.assertIsInstance(team.opp_runs, int)
                self.assertIsInstance(team.pct, float)
                self.assertIsInstance(team.place, int)
                self.assertIsInstance(team.playoff_odds, float)
                self.assertIsInstance(team.playoff_points_sw, str)
                self.assertIsInstance(team.playoffs_flag_milb, str)
                self.assertIsInstance(team.playoffs_flag_mlb, str)
                self.assertIsInstance(team.playoffs_sw, str)
                self.assertIsInstance(team.points, str)
                self.assertIsInstance(team.runs, int)
                self.assertIsInstance(team.sit_code, str)
                self.assertIsInstance(team.streak, str)
                self.assertIsInstance(team.team_abbrev, str)
                self.assertIsInstance(team.team_full, str)
                self.assertIsInstance(team.team_id, int)
                self.assertIsInstance(team.team_short, str)
                self.assertIsInstance(team.vs_central, str)
                self.assertIsInstance(team.vs_division, str)
                self.assertIsInstance(team.vs_east, str)
                self.assertIsInstance(team.vs_left, str)
                self.assertIsInstance(team.vs_right, str)
                self.assertIsInstance(team.vs_west, str)
                self.assertIsInstance(team.w, int)
                self.assertIsInstance(team.wild_card, str)
                self.assertIsInstance(team.wildcard_odds, float)
                self.assertIsInstance(team.x_wl, str)
                self.assertIsInstance(team.x_wl_seas, str)

    def test_standings_historical(self):
        import mlbgame
        from datetime import datetime
        date = datetime(2016, 6, 1)
        standings = mlbgame.standings(date)
        self.assertEqual(standings.standings_schedule_date, 'historical_standings_schedule_date')
        self.assertIsInstance(standings.last_update, datetime)
        self.assertIsInstance(standings.divisions, list)
        for division in standings.divisions:
            self.assertIsInstance(division.name, str)
            self.assertIsInstance(division.teams, list)
            for team in division.teams:
                self.assertIsInstance(team.away, str)
                self.assertIsInstance(team.clinched_sw, str)
                self.assertIsInstance(team.division, str)
                self.assertIsInstance(team.division_champ, str)
                self.assertIsInstance(team.division_id, int)
                self.assertIsInstance(team.division_odds, float)
                self.assertIsInstance(team.elim, (str, int))
                self.assertIsInstance(team.elim_wildcard, (str, int))
                self.assertIsInstance(team.extra_inn, str)
                self.assertIsInstance(team.file_code, str)
                self.assertIsInstance(team.gb, (str, float))
                self.assertIsInstance(team.gb_wildcard, (str, float))
                self.assertIsInstance(team.home, str)
                self.assertIsInstance(team.interleague, str)
                self.assertIsInstance(team.is_wildcard_sw, str)
                self.assertIsInstance(team.l, int)
                self.assertIsInstance(team.last_ten, str)
                self.assertIsInstance(team.one_run, str)
                self.assertIsInstance(team.opp_runs, int)
                self.assertIsInstance(team.pct, float)
                self.assertIsInstance(team.place, int)
                self.assertIsInstance(team.playoff_odds, float)
                self.assertIsInstance(team.playoff_points_sw, str)
                self.assertIsInstance(team.playoffs_flag_milb, str)
                self.assertIsInstance(team.playoffs_flag_mlb, str)
                self.assertIsInstance(team.playoffs_sw, str)
                self.assertIsInstance(team.points, str)
                self.assertIsInstance(team.runs, int)
                self.assertIsInstance(team.sit_code, str)
                self.assertIsInstance(team.streak, str)
                self.assertIsInstance(team.team_abbrev, str)
                self.assertIsInstance(team.team_full, str)
                self.assertIsInstance(team.team_id, int)
                self.assertIsInstance(team.team_short, str)
                self.assertIsInstance(team.vs_central, str)
                self.assertIsInstance(team.vs_division, str)
                self.assertIsInstance(team.vs_east, str)
                self.assertIsInstance(team.vs_left, str)
                self.assertIsInstance(team.vs_right, str)
                self.assertIsInstance(team.vs_west, str)
                self.assertIsInstance(team.w, int)
                self.assertIsInstance(team.wild_card, str)
                self.assertIsInstance(team.wildcard_odds, float)
                self.assertIsInstance(team.x_wl, str)
                self.assertIsInstance(team.x_wl_seas, str)
        division = standings.divisions[0]
        self.assertEqual(division.name, 'NL West')
        team = division.teams[0]
        self.assertEqual(team.away, '17-11')
        self.assertEqual(team.clinched_sw, 'N')
        self.assertEqual(team.division, 'National League West')
        self.assertEqual(team.division_champ, 'Y')
        self.assertEqual(team.division_id, 203)
        self.assertEqual(team.division_odds, 54.4)
        self.assertEqual(team.elim, '-')
        self.assertEqual(team.elim_wildcard, '')
        self.assertEqual(team.extra_inn, '4-3')
        self.assertEqual(team.file_code, 'sf')
        self.assertEqual(team.gb, '-')
        self.assertEqual(team.gb_wildcard, '')
        self.assertEqual(team.home, '16-11')
        self.assertEqual(team.interleague, '1-2')
        self.assertEqual(team.is_wildcard_sw, 'Y')
        self.assertEqual(team.l, 22)
        self.assertEqual(team.last_ten, '0-0')
        self.assertEqual(team.one_run, '12-6')
        self.assertEqual(team.opp_runs, 220)
        self.assertEqual(team.pct, .6)
        self.assertEqual(team.place, 1)
        self.assertEqual(team.playoff_odds, 77.1)
        self.assertEqual(team.playoff_points_sw, 'N')
        self.assertEqual(team.playoffs_flag_milb, '')
        self.assertEqual(team.playoffs_flag_mlb, '')
        self.assertEqual(team.playoffs_sw, 'N')
        self.assertEqual(team.points, '')
        self.assertEqual(team.runs, 242)
        self.assertEqual(team.sit_code, 'h0')
        self.assertEqual(team.streak, 'L1')
        self.assertEqual(team.team_abbrev, 'SF')
        self.assertEqual(team.team_full, 'San Francisco Giants')
        self.assertEqual(team.team_id, 137)
        self.assertEqual(team.team_short, 'San Francisco')
        self.assertEqual(team.vs_central, '6-3')
        self.assertEqual(team.vs_division, '22-12')
        self.assertEqual(team.vs_east, '4-5')
        self.assertEqual(team.vs_left, '11-8')
        self.assertEqual(team.vs_right, '22-14')
        self.assertEqual(team.vs_west, '22-12')
        self.assertEqual(team.w, 33)
        self.assertEqual(team.wild_card, 'N')
        self.assertEqual(team.wildcard_odds, 22.7)
        self.assertEqual(team.x_wl, '30-25')
        self.assertEqual(team.x_wl_seas, '88-74')
