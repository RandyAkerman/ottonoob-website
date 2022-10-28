from jinja2 import Template
import codecs
import os
from slugify import slugify

roster = {#'title': 'TEAM NAME roster for DATE',
          'date': '2020-10-30',
        #   'description': 'Bobby Cox',
        #   'lead': 'Bobby Cox',
          'team_name': 'Bobby Cox',
          'batters': [{'Pos': 'CF', '1B': '0.60', '2B': '0.15', '3B': '0.02', 'HR': '0.28', 'R': '0.62', 'BB': '0.55', 'SO': '1.35', 'player_id': 15640, 'player_slug': 'aaron-judge'}, 
                      {'Pos': 'SS', '1B': '0.66', '2B': '0.17', '3B': '0.02', 'HR': '0.17', 'R': '0.61', 'BB': '0.33', 'SO': '0.70', 'player_id': 12916, 'player_slug': 'francisco-lindor'}, 
                      {'Pos': 'C', '1B': '0.57', '2B': '0.17', '3B': '0.01', 'HR': '0.15', 'R': '0.52', 'BB': '0.51', 'SO': '1.13', 'player_id': 11609, 'player_slug': 'willson-contreras'},
                      {'Pos': '3.0', '1B': '0.57', '2B': '0.17', '3B': '0.02', 'HR': '0.14', 'R': '0.47', 'BB': '0.28', 'SO': '0.83', 'player_id': 6153, 'player_slug': 'eduardo-escobar'}, 
                      {'Pos': 'LF', '1B': '0.67', '2B': '0.19', '3B': '0.01', 'HR': '0.10', 'R': '0.51', 'BB': '0.56', 'SO': '1.22', 'player_id': 2967, 'player_slug': 'tommy-pham'}, 
                      {'Pos': 'LF', '1B': '0.54', '2B': '0.17', '3B': '0.02', 'HR': '0.10', 'R': '0.46', 'BB': '0.45', 'SO': '1.09', 'player_id': 13757, 'player_slug': 'chris-taylor'}, 
                      {'Pos': 'LF', '1B': '0.50', '2B': '0.14', '3B': '0.01', 'HR': '0.08', 'R': '0.37', 'BB': '0.44', 'SO': '0.70', 'player_id': 10815, 'player_slug': 'jurickson-profar'}, 
                      {'Pos': 'RF', '1B': '0.62', '2B': '0.19', '3B': '0.02', 'HR': '0.15', 'R': '0.46', 'BB': '0.25', 'SO': '0.76', 'player_id': 14551, 'player_slug': 'anthony-santander'}, 
                      {'Pos': 'RF', '1B': '0.56', '2B': '0.16', '3B': '0.01', 'HR': '0.14', 'R': '0.39', 'BB': '0.24', 'SO': '1.15', 'player_id': 10243, 'player_slug': 'randal-grichuk'}, 
                      {'Pos': '2.0', '1B': '0.62', '2B': '0.18', '3B': '0.01', 'HR': '0.13', 'R': '0.43', 'BB': '0.32', 'SO': '0.71', 'player_id': 5827, 'player_slug': 'wilmer-flores'}, 
                      {'Pos': 'SS', '1B': '0.51', '2B': '0.14', '3B': '0.01', 'HR': '0.08', 'R': '0.31', 'BB': '0.24', 'SO': '0.79', 'player_id': 26294, 'player_slug': 'bryson-stott'}, 
                      {'Pos': 'RF', '1B': '0.55', '2B': '0.15', '3B': '0.01', 'HR': '0.12', 'R': '0.41', 'BB': '0.31', 'SO': '0.74', 'player_id': 19901, 'player_slug': 'gavin-sheets'}, 
                      {'Pos': '2.0', '1B': '0.71', '2B': '0.16', '3B': '0.02', 'HR': '0.12', 'R': '0.44', 'BB': '0.27', 'SO': '0.82', 'player_id': 16426, 'player_slug': 'thairo-estrada'}, 
                      {'Pos': 'SS', '1B': '0.87', '2B': '0.20', '3B': '0.02', 'HR': '0.10', 'R': '0.59', 'BB': '0.27', 'SO': '0.81', 'player_id': 15518, 'player_slug': 'amed-rosario'}, 
                      {'Pos': 'C', '1B': '0.53', '2B': '0.14', '3B': '0.01', 'HR': '0.07', 'R': '0.31', 'BB': '0.14', 'SO': '0.63', 'player_id': 16725, 'player_slug': 'jose-trevino'}, 
                      {'Pos': 'DH', '1B': '0.49', '2B': '0.11', '3B': '0.01', 'HR': '0.11', 'R': '0.42', 'BB': '0.48', 'SO': '0.91', 'player_id': 9929, 'player_slug': 'darin-ruf'}], 
          'pitchers': [{'IP': '0.4', '1B': '0.23', '2B': '0.06', '3B': '0.01', 'HR': '0.04', 'BB': '0.12', 'SO': '0.00', 'player_id': 7005, 'player_slug': 'ryan-pressly'}, 
                       {'IP': '0.1', '1B': '0.06', '2B': '0.02', '3B': '0.00', 'HR': '0.01', 'BB': '0.04', 'SO': '0.00', 'player_id': 8048, 'player_slug': 'will-smith'}, 
                       {'IP': '5.4', '1B': '3.99', '2B': '1.15', '3B': '0.11', 'HR': '0.50', 'BB': '1.18', 'SO': '4.56', 'player_id': 9132, 'player_slug': 'nathan-eovaldi'}, 
                       {'IP': '1.0', '1B': '0.60', '2B': '0.17', '3B': '0.01', 'HR': '0.11', 'BB': '0.38', 'SO': '0.00', 'player_id': 4264, 'player_slug': 'mark-melancon'}, 
                       {'IP': '6.2', '1B': '3.44', '2B': '0.91', '3B': '0.09', 'HR': '0.68', 'BB': '1.93', 'SO': '6.54', 'player_id': 15873, 'player_slug': 'sean-manaea'}, 
                       {'IP': '4.6', '1B': '3.15', '2B': '0.77', '3B': '0.09', 'HR': '0.45', 'BB': '1.96', 'SO': '3.05', 'player_id': 19206, 'player_slug': 'dakota-hudson'}, 
                       {'IP': '0.9', '1B': '0.46', '2B': '0.12', '3B': '0.01', 'HR': '0.09', 'BB': '0.53', 'SO': '0.00', 'player_id': 17586, 'player_slug': 'tanner-scott'}, 
                       {'IP': '0.2', '1B': '0.13', '2B': '0.03', '3B': '0.00', 'HR': '0.03', 'BB': '0.13', 'SO': '0.00', 'player_id': 19677, 'player_slug': 'gregory-soto'}, 
                       {'IP': '0.7', '1B': '0.40', '2B': '0.12', '3B': '0.01', 'HR': '0.08', 'BB': '0.26', 'SO': '0.00', 'player_id': 12730, 'player_slug': 'nick-martinez'}]
                       
}
curpath = os.path.abspath(os.curdir)

with open('archetypes/daily_roster.md', 'r') as file:
    template = Template(file.read(), trim_blocks=True)
rendered_file = template.render(roster=roster)

output_file = codecs.open(os.path.join(curpath, "content/blog",f"roster-{slugify(roster['team_name'])}-{roster['date']}.md"), "a", "utf-8")

output_file.write(rendered_file)
output_file.close()