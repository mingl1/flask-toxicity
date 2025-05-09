from cassiopeia import cassiopeia as cass
from cassiopeia import Account, Summoner
import os
from dotenv import load_dotenv
load_dotenv()
cass.set_riot_api_key(os.environ.get('RIOTAPIKEY'))

def get_participant_data(participants, puuid):
    for p in participants:
        if puuid == p.summoner().puuid:
            p_data = {
                "champion": p.champion.name,
                "pings": {
                    "onMyWayPings": p.stats.onMyWayPings,
                    "assistMePings": p.stats.assistMePings,
                    "commandPings": p.stats.commandPings,
                    "dangerPings": p.stats.dangerPings,
                    "getBackPings": p.stats.getBackPings,
                    "holdPings": p.stats.holdPings,
                    "needVisionPings": p.stats.needVisionPings,
                    "allInPings": p.stats.allInPings,
                    "pushPings": p.stats.pushPings,
                    "visionClearedPings": p.stats.visionClearedPings,
                    "enemyMissingPings": p.stats.enemyMissingPings,
                },
                # "ff": {
                #     "gameEndedInEarlySurrender": p.endedInEarlySurrender,
                #     "gameEndedInSurrender": p.endedInSurrender,
                # },
                "role": str(p.role),
                # "kills": p.stats.kills,
                # "assist": p.stats.assists,
                "deaths": p.stats.deaths,
                "kda_ratio": round(p.stats.kda, 2),
                # "damage_dealt": p.stats.total_damage_dealt,
                # "creep_score": p.stats.total_minions_killed,
                "vision_score": p.stats.vision_score,
            }
            return p_data

        # p_items = []
        # number_of_item_slots = 6
        # for i in range(number_of_item_slots):
        #     try:
        #         p_items.append(p.stats.items[i].name)
        #     except AttributeError:
        #         p_items.append("None")
        # p_data["items"] = p_items
        # team_participant_data.append(p_data)
    return None


def print_match_history(summoner, num_matches, puuid):
    ret = []
    for i, match in enumerate(
        summoner.match_history[0:num_matches],
        start=1,
    ):
        if 'ranked' in str(match.queue).lower():
            targetPlayerStats = get_participant_data(match.blue_team.participants, puuid)
            if not targetPlayerStats:
                targetPlayerStats = get_participant_data(match.red_team.participants, puuid)
            targetPlayerStats["duration"] = match.duration.total_seconds()
            ret.append(targetPlayerStats)
        else:
            continue
    return ret


def main():
    name = "bming"
    tagline = "lin"
    region = "NA"
    account = Account(name=name, tagline=tagline, region=region)
    summoner = account.summoner
    print(print_match_history(summoner, 5,summoner.puuid))


if __name__ == "__main__":
    main()
