from collections import defaultdict

from dungeonsheets import features, weapons
from dungeonsheets.classes.classes import CharClass, SubClass


# PHB
class BloodwrathGuardian(SubClass):
    """The primal power you wield has formed an intrinsic bond with the
    creatures of the wild, and you have taken up the task of defending them.
    Because you share in the beast’s ferocity, tenacity, and animal instinct,
    you can summon a beast’s primal strength from within yourself, and slay
    your enemies in an animalistic trance.

    While entranced, you can sense a connection to a greater being, the Primal
    Beast, the first predator, from which all hunters are descended. As your
    commitment to defending the wilds from corruption grows, you grow closer
    to the Primal Beast, until you can at last adopt its ancient form yourself,
    and allow it to hunt once again.

    """

    name = "Bloodwrath Guardian"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.FeralTrance]
    features_by_level[6] = [features.PredatorsScent]
    features_by_level[13] = [features.Evasion]
    features_by_level[20] = [features.FormOfThePrimalBeast]


class CarrionKing(SubClass):
    """A master and champion of vermin, you are called defend the lowliest
    creatures of all: insects, rats, spiders, and other pests. You know that
    these creatures mean no harm, that they’re merely trying to survive in a
    world too large for them, so you come to their aide, and they flock to
    your side. Unmistakably, your coming is signaled by the scrambling of
    little claws and the cawing of the crows. Legions of pests wait at your
    command to swarm, bite, and claw at anyone who might thin their numbers.

    """

    name = "Carrion King"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.GnawingMark]
    features_by_level[6] = [features.Infested]
    features_by_level[13] = [features.Evasion]
    features_by_level[20] = [features.LordOfTheFlies]


class FeyTrailblazer(SubClass):
    """Crossing a fey bridge into the enchanted Feywild beyond can be a
    perilous journey, threatening travelers with dangerous wild magic, fey
    tricksters, and horrific magical beasts. You, however, have heard the
    carefree call of magic in these few places where the Feywild intersects
    with the mortal plane, and have cultivated your skill in guiding travelers
    through the Feywild’s hazards. In turn, the Feywild has left its mark on
    you, adorning your mark with capricious magic and letting you step easily
    through the planes.

    """

    name = "Fey Trailblazer"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.AlluringMark]
    features_by_level[6] = [features.MistyJaunt]
    features_by_level[13] = [features.SpellResistance]
    features_by_level[20] = [features.ArchfeyOfMajesty]


class Godsworn(SubClass):
    """
    The whispers of gods, the ringing of bells, and the meter of hymns called
    you, compelling you to swear an oath of protection. With your blade, you
    defend temples, holy sites, and other sacred ground, and with your shield,
    you protect pilgrims as they make their grand journeys. With your mark,
    you watch over magicless priests and ensure that their message turns
    hearts and minds, even in the most dangerous places. You know that your
    purpose is grander than just one life, and you look forward to seeing what
    designs the gods have set on your travels.

    """

    name = "Godsworn"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.BonusProficienciesGodsworn, features.AnointedMark]
    features_by_level[6] = [features.HolyAllies]
    features_by_level[13] = [features.Unshakable]
    features_by_level[20] = [features.SaintedMantle]


class GreyWatchman(SubClass):
    """Ever vigilant and unceasing in your duties, you are a watcher of the
    realms of men, called to keep vigil over a keep or wall. As a grey
    watchman, trained in the arts of combat, you have honed your skills to a
    razor’s edge to repel any invaders that might challenge your land. You
    need not keep watch over the same keep your entire life, but, wherever you
    travel, you are dedicated to keeping your land safe from invading armies,
    marauding monsters, and other external threats.

    """

    name = "Grey Watchman"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.BattleTactics, features.HoldTheLine]
    features_by_level[6] = [features.FortificationExpert]
    features_by_level[13] = [features.ImprovedBattleTactics, features.Mettle]
    features_by_level[20] = [features.UnbreakableSentinel]


class Hellkeeper(SubClass):
    """Some wardens hear a call of flames and tormented screams rising up from
    the bowels of the earth. These grim few become Hellkeepers, tasked by
    devils with watching the gates of the underworld, safeguarding the
    innocent from wandering inside, and trapping the damned prisoners within.
    Some Hellkeepers feel that their position is a merciful one, for it
    protects mortals from unspeakable fiendish cruelties. Others know full
    well the implications of their calling and relish in the vileness of their
    deeds.

    """

    name = "Hellkeeper"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.Tormenter, features.HellishGrasp]
    features_by_level[6] = [features.FellResistance, features.SpitefulMark]
    features_by_level[13] = [features.Evasion]
    features_by_level[20] = [features.Hellbent]


class IceheartBastion(SubClass):
    """When you heard the call, it was in the form of howling winds flecked
    with snow, beckoning you to north’s frigid, barren, majestic reaches. It
    is placed upon you to drive back the horrors that thrive in the utter
    frost, as well as incursions from warmer southern lands, to protect the
    hardy people and noble animals of this cold place. Wherever you travel,
    the ice of the northern lands lives in your heart, and as such, you can
    summon it to your hands with icy gales from the most northern mountain
    peaks.

    """

    name = "Iceheart Bastion"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.Snowshoes, features.IcyGrasp]
    features_by_level[6] = [features.NorthWind]
    features_by_level[13] = [features.Mettle]
    features_by_level[20] = [features.FormOfTheOldHoarfrost]


class Lawbringer(SubClass):
    """Lawbringers hear the steady, unyielding call of universal law and
    follow it without question. This set of invisible guidelines organizes the
    universe into its current state, but deviations from it threaten to
    destabilize all of creation. Reckless reality changing, time travel, and
    immortality are all violations of this law, and must be punished.
    Lawbringers are called to enforce laws both magical and mundane, and to
    deliver such punishment when necessary.

    """

    name = "Lawbringer"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.AxiomaticMark, features.Astute]
    features_by_level[6] = [features.Mandate]
    features_by_level[13] = [features.ClockworkMind]
    features_by_level[20] = [features.UniversalAxiom]


class Loreseeker(SubClass):
    """You have heard the call of rotting scrolls and antediluvian
    artifacts, remnants of wisdom now almost lost to time.  As a
    loreseeker, you uncover and protect ancient relics, whether they be
    mundane scrolls or powerful magic items, that they might be archived
    for future generations. Some loreseekers are called to defend places
    of learning, from the halls of wisdom to great libraries, whereas
    others are entrusted with safeguarding a dangerous secret that could
    do irreparable harm in the wrong hands. All loreseekers, however, are
    students of what they protect, cultivating skill in the arcane arts,
    even as they hone their talents with the blade.

    """

    name = "Loreseeker"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.LoreseekerSpellcasting, features.Bookmark]
    features_by_level[6] = [features.EnsnaringMark]
    features_by_level[13] = [features.SpellResistance]
    features_by_level[20] = [features.LibrarianOfTheEternal]
    spellcasting_ability = "intelligence"
    spell_slots_by_level = {
        # char_lvl: (cantrips, 1st, 2nd, 3rd, ...)
        1: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        2: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        3: (2, 2, 0, 0, 0, 0, 0, 0, 0, 0),
        4: (2, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        5: (2, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        6: (2, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        7: (2, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        8: (2, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        9: (2, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        10: (3, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        11: (3, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        12: (3, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        13: (3, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        14: (3, 4, 2, 2, 0, 0, 0, 0, 0, 0),
        15: (3, 4, 2, 2, 0, 0, 0, 0, 0, 0),
        16: (3, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        17: (3, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        18: (3, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        19: (3, 4, 3, 3, 1, 0, 0, 0, 0, 0),
        20: (3, 4, 3, 3, 1, 0, 0, 0, 0, 0),
    }


class Nightgaunt(SubClass):
    """Blood-drinkers, undead, and other creatures of the night are often
    feared and hunted, and few stand in their defense; except, of course, the
    grim and terrible nightgaunt. Tales of the nightgaunt are whispered of in
    fairy tales, casting them as a things to be feared: hunters of clerics and
    goodly vampire slayers. Their appearance always presages long nights and
    great rises in hungry undead.  You felt the calling of the moon bringing
    you to the graveside of living corpses. Though vampires, zombies, and
    skeletons are mighty, they are always outnumbered, hunted, and turned by
    clerics; never given a fair chance to live peacefully. They require an
    ally among the living to continue their ceaseless existences, and you have
    risen by moonlight to the task.

    """

    name = "Nightgaunt"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.Darkvision, features.MarkedForDeath]
    features_by_level[6] = [features.UndeadEmpathy]
    features_by_level[13] = [features.Evasion]
    features_by_level[20] = [features.Gravelord]


class SoulbloodShaman(SubClass):
    """The ancestral spirits called you by starlight to enact their will on
    the world, to protect their descendants, and to safeguard their resting
    places. You are a Soulblood Shaman, a manipulator of soul and ascetic of
    primal magic. Your community looks to you as a leader as well as a vital
    connection to the afterlife, for if you play your role, they too will join
    their ancestors in the great beyond.

    """

    name = "Soulblood Shaman"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.SoulbloodShamanSpellcasting, features.Soulblood]
    features_by_level[6] = [features.WhispersOfBeyond]
    features_by_level[13] = [features.Unshakable]
    features_by_level[20] = [features.EtherealWatcher]
    spellcasting_ability = "wisdom"
    spell_slots_by_level = {
        # char_lvl: (cantrips, 1st, 2nd, 3rd, ...)
        1: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        2: (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        3: (2, 2, 0, 0, 0, 0, 0, 0, 0, 0),
        4: (2, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        5: (2, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        6: (2, 3, 0, 0, 0, 0, 0, 0, 0, 0),
        7: (2, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        8: (2, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        9: (2, 4, 2, 0, 0, 0, 0, 0, 0, 0),
        10: (3, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        11: (3, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        12: (3, 4, 3, 0, 0, 0, 0, 0, 0, 0),
        13: (3, 4, 3, 2, 0, 0, 0, 0, 0, 0),
        14: (3, 4, 2, 2, 0, 0, 0, 0, 0, 0),
        15: (3, 4, 2, 2, 0, 0, 0, 0, 0, 0),
        16: (3, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        17: (3, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        18: (3, 4, 3, 3, 0, 0, 0, 0, 0, 0),
        19: (3, 4, 3, 3, 1, 0, 0, 0, 0, 0),
        20: (3, 4, 3, 3, 1, 0, 0, 0, 0, 0),
    }


class StoneheartDefender(SubClass):
    """You heard the steadfast, unyielding call from the mountains, which
    dwarves and gnomes have felt for generations. The stones called to you,
    beckoning for a protector to defend the mountains from those that would
    despoil them, from both within and without. You might be a watchman of old
    dwarven walls, or a sentinel, patrolling the lookouts of high mountain
    peaks; regardless of where you stand, you are unmovable: a mountain in the
    shape of a man. You draw your power from the earth beneath your feet and
    can crush your enemies with the strength of stone.

    """

    name = "Stoneheart Defender"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.RootsOfRock]
    features_by_level[6] = [features.Earthshatter]
    features_by_level[13] = [features.Mettle]
    features_by_level[20] = [features.ImmortalMountain]


class StormSentinel(SubClass):
    """Your strength originates among furious storm clouds and flashes of
    lightning. As a storm sentinel, you are called to protect wayward sailors
    and coastal villages from the wrath of the tempests and the arrival of
    great waves that might strike them defenseless. You despise pirates and
    others that pose a threat to coastal peoples, and will oppose them
    wherever they strike.  From your fingertips, you can deliver the awe of
    lightning and the roar of thunder to devastate your foes. With practice
    and patience, you can harness the power of the storm itself to fly and
    rain thunderbolts from above.

    """

    name = "Storm Sentinel"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.FlashFromAbove, features.Thunderblast]
    features_by_level[6] = [features.StaticBurst]
    features_by_level[13] = [features.Evasion]
    features_by_level[20] = [features.Stormlord]


class VerdantProtector(SubClass):
    """You draw your strength from the trees of the forest and the loamy earth
    beneath your feet. As a Verdant Protector, you are the champion of the
    green things in nature, and defend them against those who would despoil
    the wilds. You easily find allies among druids, and others that understand
    the forest’s sacred trees and ancient spirits.  At your command, the
    plants of the earth sprout up to assist you in your duty. At the pinnacle
    of your power, you can assume the form of an elder tree guardian, which
    looks much like a treant, with tough, bark skin, and long, branchlike arms.

    """

    name = "Verdant Protector"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.GreenMark]
    features_by_level[6] = [features.VerdantSkin]
    features_by_level[13] = [features.Mettle]
    features_by_level[20] = [features.FormOfTheOakSentinel]


class WitchbaneHunter(SubClass):
    """Where there is magic, there is evil. Witches lurks in the shadows with
    hags and warlocks, waiting for your guard to lower, such that they might
    turn their hexes upon the innocent. But your ever-vigilant sword is ready
    for them, ready to defend the nonmagical folk from evil spellcasters the
    world-over. You slay vampires, hexers, devils, and fey alike with
    impunity, for anyone who might despoil the world with magic shall be
    hunted and put to the stake.

    """

    name = "Witchbane Hunter"
    features_by_level = defaultdict(list)
    features_by_level[3] = [features.WitchbaneMark]
    features_by_level[6] = [features.EldritchReflection]
    features_by_level[13] = [features.SpellResistance]
    features_by_level[20] = [features.Antimage]


class Warden(CharClass):
    name = "Warden"
    hit_dice_faces = 10
    subclass_select_level = 3
    saving_throw_proficiencies = ("strength", "constitution")
    primary_abilities = (
        "strength",
        "constitution",
    )
    _proficiencies_text = ("light armor", "medium armor", "shields", "simple weapons", "martial weapons")
    weapon_proficiencies = (weapons.SimpleWeapon, weapons.MartialWeapon)
    multiclass_weapon_proficiencies = weapon_proficiencies
    _multiclass_proficiencies_text = (
        "light armor",
        "medium armor",
        "shields",
        "simple weapons",
        "martial weapons",
    )
    class_skill_choices = (
        "Animal Handling",
        "Athletics",
        "Nature",
        "Perception",
        "Survival",
    )
    features_by_level = defaultdict(list)
    features_by_level[1] = [features.SentinelsStand, features.WardensGrasp]
    features_by_level[2] = [features.WardenFightingStyle, features.WardensMark]
    features_by_level[3] = [features.ChampionsCall, features.WardensResolve]
    features_by_level[4] = [features.FontOfLife]
    features_by_level[5] = [features.ExtraAttackWarden]
    features_by_level[7] = [features.SentinelsStep]
    features_by_level[9] = [features.Undying]
    features_by_level[10] = [features.Interrupt]
    features_by_level[17] = [features.SentinelsSoul]
    subclasses_available = (
        BloodwrathGuardian,
        CarrionKing,
        FeyTrailblazer,
        Godsworn,
        GreyWatchman,
        Hellkeeper,
        IceheartBastion,
        Lawbringer,
        Loreseeker,
        Nightgaunt,
        SoulbloodShaman,
        StoneheartDefender,
        StormSentinel,
        VerdantProtector,
        WitchbaneHunter
    )
