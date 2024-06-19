from cassiopeia import cassiopeia as cass
from cassiopeia import Account, Summoner
import json


def get_participant_data(participants, puuid):
    for p in participants:
        if puuid == p.stats.puuid:
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
                "ff": {
                    "gameEndedInEarlySurrender": p.stats.gameEndedInEarlySurrender,
                    "gameEndedInSurrender": p.stats.gameEndedInSurrender,
                },
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
        # print(match.game_type)

        if "aram" in str(match.queue).lower():
            continue
        r = get_participant_data(match.blue_team.participants, puuid)
        if not r:
            r = get_participant_data(match.red_team.participants, puuid)
        if r:
            r["duration"] = match.duration.total_seconds()
            ret.append(r)

    return ret


def main():
    name = "Pobelter"
    tagline = "NA1"
    region = "NA"
    account = Account(name=name, tagline=tagline, region=region)
    summoner = account.summoner
    print_match_history(summoner, 5)


if __name__ == "__main__":
    main()
