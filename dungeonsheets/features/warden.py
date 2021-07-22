from dungeonsheets.features.features import Feature, FeatureSelector
from dungeonsheets.features.ranger import Archery, Defense, Dueling, TwoWeaponFighting

# Features added for all PHB classes
# SCAG and XGTE needed


# PHB
class GreatWeaponFighting(Feature):
    """When you roll a 1 or 2 on a damage die for an attack you make with a melee
    weapon that you are wielding with two hands, you can reroll the die and
    must use the new roll, even if the new roll is a 1 or a 2. The weapon must
    have the two-handed or versatile property for you to gain this benefit.
    """

    name = "Fighting Style (Great Weapon Fighting)"
    source = "Warden"


class Crippling(Feature):
    """When you hit a creature with a melee weapon attack, its speed is
    reduced by 10 feet, to a minimum of 0, until the end of its next turn, and
    it can’t take the Dash action until the end of its turn.

    """

    name = "Fighting Style (Crippling)"
    source = "Warden"


class Protection(Feature):
    """When a creature you can see attacks a target other than you that is
    within 5 feet of you, you can use your reaction to impose disadvantage on
    the attack roll. You must be wielding a weapon or shield.

    """

    name = "Fighting Style (Protection)"
    source = "Warden"


class TitanFighting(Feature):
    """You gain a +2 bonus to melee weapon attack rolls you make against Large
    or larger creatures

    """

    name = "Fighting Style (Titan Fighting)"
    source = "Warden"


class WardenFightingStyle(FeatureSelector):
    """Select a Fighting Style by choosing in feature_choices:

    - Crippling
    - Great Weapon Fighting 
    - Protection
    - Titan Fighting

    """

    options = {
        "Crippling": Crippling,
        "Great Weapon Fighting": GreatWeaponFighting,
        "Protection": Protection,
        "Titan Fighting": TitanFighting,
    }
    name = "Fighting Style (Select One)"
    source = "Warden"


class Mettle(Feature):
    """At 13th level, your determination allows you to shrug off effects that
    would otherwise harm you. When you are subjected to an effect that allows
    you to make a Constitution saving throw to take only half damage, you
    instead take no damage if you succeed on the saving throw, and only half
    damage if you fail.
    """

    name = "Mettle"
    source = "Warden"


class FeralTrance(Feature):
    """Starting when you hear this call at 3rd level, you can fall into a
    primal battle trance as a bonus action. While in your trance, you gain the
    following benefits if you aren’t holding a shield or wearing heavy armor:

    * You have advantage on Strength checks and Strength saving throws.
    * Your base movement speed increases by 10 feet.
    * Once per turn, when you make an attack roll against a creature, you can
    end your current mark, and mark that creature instead.
    * When an attacker that you can see hits you with an attack, you can use
    your reaction to halve the attack’s damage against you.

    Your trance lasts for 1 minute. It ends early if you are knocked
    unconscious or if your turn ends and you haven’t attacked a hostile
    creature since your last turn or taken damage since then. You can also end
    your trance on your turn as a bonus action.

    Once you use this ability, you can’t use it again until you finish a short
    or long rest.

    """

    name = "Feral Trance"
    source = "Warden (Bloodwrath Guardian)"


class PredatorsScent(Feature):
    """By 6th level, you hunt like an animal. A creature you have marked can
    remain marked for up to 24 hours, even if it moves out of your sight.
    Additionally, while this creature is marked, you can track it
    effortlessly; you know the direction and distance to the creature while it
    remains on the same plane of existence.

    """

    name = "Predator's Scent"
    source = "Warden (Bloodwrath Guardian)"


class Evasion(Feature):
    """Beginning at 13th level, you can nimbly dodge out of the way of certain
    area effects, such as a red dragon’s fiery breath or an ice storm spell.
    When you are subjected to an effect that allows you to make a Dexterity
    saving throw to take only half damage, you instead take no damage if you
    succeed on the saving throw, and only half damage if you fail.

    """

    name = "Evasion"
    source = "Warden"


class FormOfThePrimalBeast(Feature):
    """At 20th level, as an action, you can transform into a hunched thing of
    fur and shadow, an echo of the Primal Beast. For 1 minute, you gain the
    following features:

    * You gain all the benefits of Feral Trance.
    * You gain temporary HP equal to twice your level.
    * Once per turn, when you hit a creature with a melee weapon attack, you
    can wound the target. At the start of each of the wounded creature’s
    turns, it takes 1d8 necrotic damage for each time you’ve wounded it, and
    it can then make a Constitution saving throw (save DC equals 8 + your
    proficiency bonus + your Strength modifier), ending the effect of all such
    wounds on itself on a success. Alternatively, the wounded creature, or a
    creature within 5 feet of it, can use an action to make a DC 15 Wisdom
    (Medicine) check, ending the effect of such wounds on it on a success.

    Once you use this feature, you can’t use it again until you finish a long rest.

    """

    name = "Form of the Primal Beast"
    source = "Warden (Bloodwrath Guardian)"


class GnawingMark(Feature):
    """Starting when you hear this call at 3rd level, the vermin heed your
    every word. When you mark a creature, insects swarm its eyes and mouth and
    crawl on its skin. Whenever the creature makes an attack roll or ability
    check while it is marked, it must roll a d4 and subtract the number rolled
    from the result.

    """

    name = "Gnawing Mark"
    source = "Warden (Carrion King)"


class Infested(Feature):
    """By 6th level, insects and rodents inhabit every nook and cranny of your
    clothes and gear. Whenever a creature within 5 feet of you hits you with
    an attack, these vermin retaliate, dealing 1d6 piercing damage to the
    attacker. Additionally, on each subsequent attack the creature makes
    before the end of its turn, it must roll a d4 and subtract the number
    rolled from the attack roll.

    """

    name = "Infested"
    source = "Warden (Carrion King)"


class LordOfTheFlies(Feature):
    """At 20th level, you can use your action to beckon forth a colossal
    swarm of flying insects and scurrying rodents, which envelop you like a
    cloud. For the next minute, a 10-foot radius sphere of vermin is centered
    upon you. The area is heavily obscured. Each creature you choose within
    the sphere has disadvantage on attack rolls and ability checks and takes
    6d4 piercing damage when it enters the area for the first time on a turn
    or starts its turn there.

    Once you use this ability, you can’t use it again until you finish a long rest.

    """

    name = "Lord of the Flies"
    source = "Warden (Carrion King)"


class AlluringMark(Feature):
    """Starting when you hear this call at 3rd level, you can place your mark
    upon the affections within a creature’s mind. When you use your Warden’s
    Mark, you can attempt to place an Alluring Mark. When you do so, the
    target must make a Wisdom saving throw, with a DC equal to 8 + your
    proficiency bonus + your Constitution modifier. On a failed save, instead
    of the normal effects of Warden’s Mark, while the marked creature is
    within 5 feet of you, it is charmed by you. Your Alluring Mark ends early
    if you deal damage to the marked creature.

    """

    name = "Alluring Mark"
    source = "Warden (Fey Trailblazer)"


class MistyJaunt(Feature):
    """By 6th level, your connection to the Feywild enables you to blink from
    place to place. You can spend your entire movement to teleport up to half
    your movement speed.

    """

    name = "Misty Jaunt"
    source = "Warden (Fey Trailblazer)"


class ArchfeyOfMajesty(Feature):
    """At 20th level, as an action, you can channel the majesty of the archfey
    that rule the fey courts, becoming an embodiment of unnatural grace and
    beauty for the next minute. You gain the following benefits:

    * Whenever a creature tries to attack you, it must make a Wisdom saving
    throw (DC equals 8 + your proficiency bonus + your Constitution modifier.)
    On a failed save, its attack misses. On a successful save, the creature is
    immune to this ability for the next 24 hours.
    * As a bonus action, you can teleport up to 30 feet to an unoccupied space
    it can see.

    Once you use this ability, you can’t use it again until you finish a long
    rest.

    """

    name = "Archfey Of Majesty"
    source = "Warden (Fey Trailblazer)"


class BonusProficienciesGodsworn(Feature):
    """When you adopt this oath at 3rd level, you gain proficiency in the
    Medicine and Religion skills. If you already have proficiency in one of
    these skills, your proficiency bonus is doubled for any ability check you
    make that uses it.

    """

    name = "Bonus Proficiencies"
    source = "Warden (Godsworn)"

    def __init__(self, owner=None):
        super().__init__(owner=owner)
        if "medicine" not in self.owner.skill_proficiencies:
            self.owner.skill_proficiencies.append("medicine")
        if "religion" not in self.owner.skill_proficiencies:
            self.owner.skill_proficiencies.append("religion")


class AnointedMark(Feature):
    """At 3rd level, you can use your Warden’s Mark to target a friendly
    creature within 30 feet. Doing so places the creature under the effects of
    the bless spell while it remains marked.

    """

    name = "Anointed Mark"
    source = "Warden (Godsworn)"


class HolyAllies(Feature):
    """By 6th level, the spirits of saints and martyrs rise to protect you.
    You can use your action to cast the spell spirit guardians (DC equals 8 +
    your proficiency bonus + your Strength modifier) without using a spell
    slot. Once you use this ability, you can’t use it again until you finish a
    long rest.

    """

    name = "Holy Allies"
    source = "Warden (Godsworn)"


class Unshakable(Feature):
    """At 13th level, your determination allows you to shrug off effects that
    would otherwise harm you. When you make a saving throw against a spell or
    magical effect, you can choose to instead make a Constitution save against
    the effect instead of the normal saving throw.

    """

    name = "Unshakable"
    source = "Warden (Godsworn)"


class SaintedMantle(Feature):
    """At 20th level, you can use your bonus action to wreathe yourself in
    divine protection, a soft glow and faint halo signifying the sainted
    mantle. For the next minute, while you are conscious, you regain 5 hit
    points at the start of each of your turns. If you have less than half your
    hit points at the start of your turn, you instead regain 10 hit points.
Once you use this ability, you can’t use it again until you finish a long rest.

    """

    name = "Sainted Mantle"
    source = "Warden (Godsworn)"


class BattleTactics(Feature):
    """When you hear this call at 3rd level, you learn maneuvers that are
    fueled by special dice called battle dice. 

    ***Maneuvers.*** You learn three maneuvers of your choice, which are
    detailed under “Maneuvers” below. Many maneuvers enhance an attack in some
    way. You can use only one maneuver per attack.  You learn two additional
    maneuvers of your choice at 6th and 13th level. Each time you gain a level
    in this class, you can also replace one maneuver you know with a different
    one.

    ***Battle Dice.*** You have four battle dice, which are d8s. A battle die is
    expended when you use it. You regain all of your expended battle dice when
    you finish a short or long rest.

    You gain another battle die at 6th level and one more at 13th level.

    ***Saving Throws.*** Some of your maneuvers require your target to make a
    saving throw to resist the maneuver’s effects. The saving throw DC is
    calculated as follows:

    **Maneuver save DC** = 8 + your proficiency bonus + your Strength or
    Dexterity modifier (your choice)

    """

    name = "Battle Tactics"
    source = "Warden (Grey Watchman)"


class WardenManeuver(Feature):
    """
    A generic maneuver
    """
    source = "Warden Manuever (Battle Tactics)"


class AvengingStrike(WardenManeuver):
    """When a creature you have marked damages a friendly creature within 5
    feet of you, you can use your reaction and expend one battle die to make a
    melee weapon attack against the creature. If you hit, you add the battle
    die to the attack’s damage roll.
    """
    name = "Avenging Strike"


class BullsCharge(WardenManeuver):
    """When you move at least 10 feet in a straight line, you can use a bonus
    action to expend a battle die and charge a creature. Make a melee weapon
    attack and add the battle die to the attack’s damage roll. On a hit, the
    target is pushed 10 feet away from you.
    """

    name = "Bull's Charge"


class Bulwark(WardenManeuver):
    """When you hit a creature you have marked with a melee weapon attack, you
    can expend a battle die to brace yourself for its counterattack. The next
    time the creature damages you before the start of your next turn, you can
    roll the battle die and subtract the result from the damage dealt.
    """

    name = "Bulwark"


class Cleave(WardenManeuver):
    """When you reduce a hostile creature to 0 hit points with a melee weapon
    attack on your turn, you can spend a battle die to move up to 15 feet and
    make an additional melee weapon attack. You add the battle die to the
    attack’s damage roll.
    """

    name = "Cleave"


class DisarmingStrike(WardenManeuver):
    """When you hit a creature you have marked with a melee weapon attack, you
    can expend one battle die to attempt to disarm the target, forcing it to
    drop one item of your choice that it’s holding. You add the battle die to
    the attack’s damage roll, and the target must make a Strength saving throw.
    On a failed save, it drops the object you choose. The object lands at its
    feet.
    """

    name = "Disarming Strike"


class Heelcutter(WardenManeuver):
    """When you make an opportunity attack against a creature you have marked,
    you can expend one battle die to knock the creature off balance, preventing
    it from escaping. You add the battle die to the attack’s damage roll, and
    the target must make a Strength saving throw. On a failed save, its speed
    is reduced to 0 until the end of its turn.
    """

    name = "Heelcutter"


class RecklessAssault(WardenManeuver):
    """When you make an attack against a creature you have marked, you can
    expend a battle die to make a wild, desperate strike, leaving you
    vulnerable. You have advantage on the attack roll and you can add the
    battle die to the attack’s damage roll. Until the beginning of your next
    turn, however, attacks against you have advantage.
    """

    name = "Reckless Assault"


class SkullBash(WardenManeuver):
    """When you hit a creature you have marked with a melee weapon attack, you
    can expend one battle die to daze the target. You add the battle die to
    the attack’s damage roll, and the target can’t take reactions until the
    start of its next turn.
    """

    name = "Skull Bash"


class StaggeringBlow(WardenManeuver):
    """When you hit a creature you have marked with a melee weapon attack, you
    can expend one battle die to stagger the creature. You add the battle die
    to the attack’s damage roll, and the target has disadvantage the next
    attack it makes before the start of your next turn.
    """

    name = "Staggering Blow"


class HoldTheLine(Feature):
    """At 3rd level, when you use your Warden’s Grasp, any creature you choose
    other than yourself within the effect’s area gains a +1 bonus to Armor
    Class and saving throws until the beginning of your next turn while it
    remains in the effect’s area.

    """

    name = "Hold the Line"
    source = "Warden (Grey Watchman)"


class FortificationExpert(Feature):
    """By 6th level, your experience manning battlements and blockades has
    given you insight in how to raise and reinforce them. You have advantage
    on any ability check you make to erect defensive fortifications, examine
    walls and other defenses for weak points and entryways, or climb
    constructed walls. Additionally, you can treat three- quarters cover as
    full cover.

    """

    name = "Fortification Expert"
    source = "Warden (Grey Watchman)"


class ImprovedBattleTactics(Feature):
    """At 13th level, your battle dice turn into d10s. At 20th level, they
    turn into d12s.

    """

    name = "Improved Battle Tactics"
    source = "Warden (Grey Watchman)"


class UnbreakableSentinel(Feature):
    """Starting at 20th level, you can use your action to transform into a
    paragon of battle, an unstoppable sentinel, channeling the strength of
    every man, woman, and child beneath your charge. For the next minute, you
    gain the following benefits:

    * You have a +2 bonus to Armor Class.
    * Whenever you hit a creature you have marked, you regain an expended
    battle die.
    * You can take an additional reaction each turn.

    Once you use this ability, you can’t use it again until you finish a long
    rest.


    """

    name = "Unbreakable Sentinel"
    source = "Warden (Grey Watchman)"


class Tormenter(Feature):
    """Starting when you hear this call at 3rd level, you can double your
    proficiency bonus for any Charisma (Intimidation) check you make to
    intimidate a creature that is restrained.

    """

    name = "Tormentor"
    source = "Warden (Hellkeeper)"


class HellishGrasp(Feature):
    """At 3rd level, when you use your Warden’s Grasp ability, each creature
    affected takes 1d6 fire damage. At 14th level, this fire damage increases
    to 2d6.

    """

    name = "Hellish Grasp"
    source = "Warden (Hellkeeper)"


class FellResistance(Feature):
    """By 6th level, your flesh is darkens and toughens to match that of a
    fiend as you come closer to death. You have advantage on Strength and
    Constitution saving throws when your hit points are less than half your
    maximum.

    """

    name = "Fell Resistance"
    source = "Warden (Hellkeeper)"


class SpitefulMark(Feature):
    """Also at 6th level, when you mark a creature with Warden’s Mark, the
    target takes 1d6 fire damage. At 11th level, this fire damage increases to
    2d6.

    """

    name = "Spiteful Mark"
    source = "Warden (Hellkeeper)"


class Hellbent(Feature):
    """At 20th level, as an action, you can transform into the fiendish shape 
    of a true devil. For the next minute, your melee weapon attacks deal an
    additional 2d8 fire damage on a hit. Moreover, fire damage you deal
    ignores damage resistance and immunity. Once during the duration, if you
    fail a saving throw, you can choose to succeed instead. 

    Once you use this ability, you can’t use it again until you finish a long
    rest.

    """

    name = "Hellbent"
    source = "Warden (Hellkeeper)"


class Snowshoes(Feature):
    """Beginning when you hear this call at 3rd level, you move unhindered by
    snow and ice. You ignore difficult terrain caused by such conditions and
    it doesn’t slow your travel.

    """

    name = "Snowshoes"
    source = "Warden (Iceheart Bastion)"


class IcyGrasp(Feature):
    """At 3rd level, when you use your Warden’s Grasp, a layer of thick ice
    frosts upon you and anchors you to the ground, granting you temporary hit
    points equal to your Constitution modifier until the beginning of your
    next turn.
    """

    name = "Icy Grasp"
    source = "Warden (Iceheart Bastion)"


class NorthWind(Feature):
    """Starting at 6th level, you can exhale a breath of the true North Wind,
    an icy gale which affects a 100-foot long, 5-foot wide line in a direction
    you choose. Each creature in the line must make a Dexterity saving throw.
    On a failed save, a creature takes 4d6 cold damage and its speed is halved
    until the end of its next turn. On a success, a creature takes half damage
    and its speed isn’t halved.

    Once you use this ability, you can’t use it again until you finish a short
    or long rest.

    """

    name = "North Wind"
    source = "Warden (Iceheart Bastion)"


class FormOfTheOldHoarfrost(Feature):
    """At 20th level, you can use your action to transform into a creature of
    deepest cold, a sentinel of the old hoarfrost. For one minute, you are
    surrounded by a frigid 15-foot radius vortex which extinguishes any
    nonmagical flames in its area. This area is difficult terrain. When a
    creature enters the area for the first time on a turn or starts its turn
    there, it takes 8d6 cold damage. You can choose for creatures to be immune
    to the effects of the area.

    Once you use this feature, you can’t use it again until you finish a long
    rest.

    """

    name = "Form of the Old Hoarfrost"
    source = "Warden (Iceheart Bastion)"


class AxiomaticMark(Feature):
    """Starting at 3rd level, lawbreakers can never escape your mark. When a
    creature you have marked within 30 feet of you moves, you can use your
    reaction to move up to half your movement speed. You must end your
    movement closer to the marked creature than you began.

    """

    name = "Axiomatic Mark"
    source = "Warden (Lawbringer)"


class Astute(Feature):
    """At 3rd level, you have advantage on ability checks you make to discern
    if a creature you can see is telling the truth.

    """

    name = "Astute"
    source = "Warden (Lawbringer)"


class Mandate(Feature):
    """At 6th level, you can cast the spell command once without using a spell
    slot. This spell targets each creature you choose within 30 feet, using
    the same command for each target. The saving throw for this ability is 8 +
    your proficiency bonus + your Constitution modifier. Once you use this
    ability, you can’t use it again until you finish a short or long rest.

    """

    name = "Mandate"
    source = "Warden (Lawbringer)"


class ClockworkMind(Feature):
    """Starting at 13th level, your mind is a fortress, unbendable and
    unbreakable. You have advantage on saving throws against being charmed or
    frightened. Whenever you succeed on a saving throw against an enchantment
    spell or an ability that attempts to cloud your thoughts or control your
    mind, the caster takes 4d6 psychic damage.

    """

    name = "Clockwork Mind"
    source = "Warden (Lawbringer)"


class UniversalAxiom(Feature):
    """At 20th level, as an action, you can transform into an embodiment of
    universal law, a ticking construct of inevitable intent. For 1 minute, you
    gain the following features:

    * You can’t be exhausted, frightened, grappled, incapacitated, paralyzed,
    petrified, poisoned, knocked prone, restrained, or stunned.
    * You have advantage on all saving throws.
    * You can use your Mandate ability at will.

    Once you use this feature, you can’t use it again until you finish a long
    rest.

    """

    name = "Universal Axiom"
    source = "Warden (Lawbringer)"


class LoreseekerSpellcasting(Feature):
    """You know three 1st-level wizard spells of your choice, two of which you
    must choose from the abjuration and evocation spells on the wizard spell
    list.

    The Spells Known column of the Loreseeker Spellcasting table shows
    when you learn more wizard spells of 1st level or higher. Each of these
    spells must be an abjuration or evocation spell of your choice, and must be
    of a level for which you have spell slots. For instance, when you reach 7th
    level in this class, you can learn one new spell of 1st or 2nd level.

    The spells you learn at 8th, 14th, and 20th level can come from any school
    of magic.

    Whenever you gain a level in this class, you can replace one of the wizard
    spells you know with another spell of your choice from the wizard spell
    list. The new spell must be of a level for which you have spell slots, and
    it must be an abjuration or evocation spell, unless you're replacing the
    spell you gained at 8th, 14th, or 20th level.

    """

    name = "Spellcasting"
    source = "Warden (Loreseeker)"


class Bookmark(Feature):
    """At 3rd level, any creature that is marked by you subtract 1d4 from
    saving throws it makes against your spells and effects.

    """

    name = "Bookmark"
    source = "Warden (Loreseeker)"


class EnsnaringMark(Feature):
    """Starting at 6th level, when you place your Warden’s Mark on a creature,
    you can teleport the creature to an unoccupied space within 5 feet of you.

    Once you use this ability, you can’t use it again until you finish a short
    or long rest.

    """

    name = "Ensnaring Mark"
    source = "Warden (Loreseeker)"


class LibrarianOfTheEternal(Feature):
    """At 20th level, as an action, you can channel the power of the lore and
    stories you have collected, becoming a living embodiment of ancient
    knowledge for the next minute and gaining the following benefits:

    • When you cast a spell, you gain 15 temporary hit points.
    • When you cast a cantrip that has a casting time of 1 action, you can
    cast it as a bonus action instead.
    • Any creature that is marked by you has disadvantage on saving throws
    against spells you cast.

    Once you use this ability, you can’t use it again until you finish a long
    rest.

    """

    name = "Librarian of the Eternal"
    source = "Warden (Loreseeker)"


class Darkvision(Feature):
    """Starting when you hear this call at 3rd level, you can see in dim
    light within 60 feet of you as if it were bright light, and in darkness as
    if it were dim light. You can’t discern color in darkness, only shades of
    gray. If you already possess darkvision, its range increases by 30 feet.

    Starting at 13th level, you can see through magical, as well as
    nonmagical, darkness.

    """

    name = "Darkvision"
    source = "Warden (Nightgaunt)"


class MarkedForDeath(Feature):
    """At 3rd level, your mark leaves a shadow of undeath on your target,
    beckoning it to die. If you deal damage to a creature you have marked with
    a melee weapon attack and its remaining hit points are lower than the
    damage you dealt to it with that attack, the marked creature instead drops
    to 0 hit points.

    """

    name = "Marked for Death"
    source = "Warden (Nightgaunt)"


class UndeadEmpathy(Feature):
    """By 6th level, you are a friend even to mindless undead. Whenever an
    undead tries to attack you, it must make a Wisdom saving throw (DC equals
    8 + your proficiency bonus + your Constitution modifier.) On a failed
    save, its attack misses and, if its Intelligence is 4 or lower, it becomes
    friendly to you and your allies.

    """

    name = "Undead Empathy"
    source = "Warden (Nightgaunt)"


class Gravelord(Feature):
    """At 20th level, you can use your action to invite the necromantic
    energies of true undead into your body, divorcing yourself from life for
    the next minute and gaining the following benefits:

    * You are immune to poison damage and being poisoned.
    * You can use your Undying feature up to three times, even if you have
    already used it today.
    * Once per turn, when you deal damage with a melee weapon attack, you can
    deal an extra 4d6 necrotic damage and gain temporary hit points, which
    last until the beginning of your next turn, equal to the necrotic damage
    dealt.

    Once you use this feature, you can’t use it again until you finish a long
    rest.

    """

    name = "Gravelord"
    source = "Warden (Nightgaunt)"


class SoulbloodShamanSpellcasting(Feature):
    """You know three 1st-level druid spells of your choice, two of which you
    must choose from the evocation or transmutation spells on the druid spell
    list.

    The Spells Known column of the Soulblood Shaman Spellcasting table shows
    when you learn more druid spells of 1st level or higher. Each of these
    spells must be an evocation or transmutation spell of your choice, and
    must be of a level for which you have spell slots.

    The spells you learn at 8th, 14th, and 20th level can come from any school
    of magic.

    Whenever you gain a level in this class, you can replace one of the druid
    spells you know with another spell of your choice from the druid spell
    list. The new spell must be of a level for which you have spell slots, and
    it must be an evocation or transmutation spell, unless you’re replacing
    the spell you gained at 3rd, 8th, 14th, or 20th level from any school of
    magic.

    """

    name = "Spellcasting"
    source = "Warden (Soulblood Shaman)"


class Soulblood(Feature):
    """Also at 3rd level, as a reaction when a creature within 5 feet of you
    deals damage to you, you can mark that creature.

    """

    name = "Soulblood"
    source = "Warden (Soulblood Shaman)"


class WhispersOfBeyond(Feature):
    """At 6th level, you can hear the small voices of ancient spirits when you
    need guidance. If you spend one minute in contemplation when you make an
    Intelligence or Wisdom check, you can consult the spirits to gain
    advantage on the roll. However, the GM can decline to give you advantage
    on this check if the spirits would not possess appropriate guidance of
    knowledge.

    """

    name = "Whispers of Beyond"
    source = "Warden (Soulblood Shaman)"


class EtherealWatcher(Feature):
    """At 20th level, as an action, you can shrug off your mortal form for a
    short time to become something spiritual and material, an ethereal watcher.
    For the next minute, you gain the following benefits:

    • As a bonus action on your turn or as a reaction when you take damage, you
    can become ethereal, as per the etherealness spell. You can return from
    being ethereal as a bonus action, or when you use your Warden’s Mark or
    Warden’s Grasp feature. When you return from being ethereal, each creature
    you choose within 10 feet of you takes 4d10 force damage, as they are
    pulled partially between the planes.

    • You can move through other creatures and objects as if they were
    difficult terrain. You take 4d10 force damage if you end your turn inside
    a creature or object, as you are ejected into the nearest unoccupied space.

    Once you use this ability, you can’t use it again until you finish a long
    rest.

    """

    name = "Ethereal Watcher"
    source = "Warden (Soulblood Shaman)"


class RootsOfRock(Feature):
    """Starting when you hear this call at 3rd level, when you use your
    Warden’s Grasp ability, rocky roots sprout from your feet, anchoring you
    securely. Until the beginning of your next turn, you have a +2 bonus to
    your Armor Class.

    Additionally, until you move, you can’t be shoved or pushed from wherever
    you are standing by hostile actions, spells, or effects, unless you choose
    to be. You have advantage on Strength saving throws against being knocked
    down, cannot slip or fall from ledges, and are immune to the spells fly,
    levitate, and telekinesis.

    """

    name = "Roots of Rock"
    source = "Warden (Stoneheart Defender)"


class Earthshatter(Feature):
    """Starting at 6th level, you can choose to use Warden’s Grasp as an 
    action, rather than a bonus action.  When you do so, each creature
    affected must make a Strength saving throw (DC equals 8 + your proficiency
    bonus + your Strength modifier) or be knocked prone.

    You can use this ability a number of times equal to your Strength
    modifier, and regain all uses when you finish a long rest.

    """

    name = "Earthshatter"
    source = "Warden (Stoneheart Defender)"


class ImmortalMountain(Feature):
    """By 20th level, you can summon the power of true earth as an action,
    protecting yourself in an encasement of stone. For the next minute, you
    gain the following benefits: 

    * Bludgeoning, piercing, and slashing damage you take is reduced by 5.  
    * You gain the effects of your Roots of Rock ability for the entire duration.
    * As you move, you can choose to upend the earth at your feet, leaving
    behind a 5-foot wide trail of difficult terrain behind you wherever you move.

    Once you use this feature, you can’t use it again until you finish a long rest.

    """

    name = "Immortal Mountain"
    source = "Warden (Stoneheart Defender)"


class FlashFromAbove(Feature):
    """Starting when you hear this call at 3rd level, whenever you are
    standing under the open sky, you can use your action to conjure a
    harmless, but impressive, bolt of lightning or peal of thunder. You can
    use this ability even when there are no clouds above you.

    """

    name = "Flash from Above"
    source = "Warden (Storm Sentinel)"


class Thunderblast(Feature):
    """At 3rd level, whenever you hit a creature you have marked with a melee
    weapon attack, each creature you choose within 5 feet of the target takes
    1d8 lightning damage.

    """

    name = "Thunderblast"
    source = "Warden (Storm Sentinel)"


class StaticBurst(Feature):
    """Starting at 6th level, when you use Warden’s Grasp as a bonus action,
    each creature affected can’t take reactions until the beginning of your
    next turn.

    """

    name = "Static Burst"
    source = "Warden (Storm Sentinel)"


class Stormlord(Feature):
    """Starting at 20th level, you have a flight speed equal to your movement
    speed.  

    Additionally, you can use your action to summon a bolt of lightning to
    strike you, imbuing your body with the storm’s fury. For 1 minute, you
    gain the following benefits:

    • Your flight speed is doubled.
    • You can cast the spell call lightning as a bonus action (DC equals 8 +
    your proficiency bonus + your Constitution modifier) without using a spell
    slot. You can call a bolt of lightning on subsequent turns as a bonus action.

    Once you use this feature, you can’t use it again until you finish a long rest.

    """

    name = "Stormlord"
    source = "Warden (Storm Sentinel)"


class GreenMark(Feature):
    """Starting when you hear this call at 3rd level, when you mark a creature,
    the plants of the earth come alive to hinder its progress. While this
    creature is within 30 feet of you, the ground it walks on is difficult
    terrain.

    """

    name = "Green Mark"
    source = "Warden (Verdant Protector)"


class VerdantSkin(Feature):
    """At 6th level, you gain proficiency in the Stealth skill, if you did not
    have it before. Additionally, you can use your action to draw a thick mass
    of vines and leaves to conceal you. Until you move, you have advantage on
    Dexterity (Stealth) checks you make to hide among vegetation.

    """

    name = "Verdant Skin"
    source = "Warden (Verdant Protector)"


class FormOfTheOakSentinel(Feature):
    """Starting at 20th level, you can use your action to transform into an
    oak sentinel, a bark-covered titan of the forest. For 1 minute, you gain
    the following features:

    * Your AC becomes 20, if it was lower.
    * Your attacks have Reach, if they did not have it before.
    * You can use Warden’s Grasp as an action, rather than a bonus action.
    When you do so, you can make an attack against each creature affected,
    with a separate attack roll for each target.

    Once you use this feature, you can’t use it again until you finish a long rest.

    """

    name = "Form of the Oak Sentinel"
    source = "Warden (Verdant Protector)"


class WitchbaneMark(Feature):
    """Starting when you hear this call at 3rd level, you have advantage on
    saving throws you make against the spells and effects of any creature you
    have marked. Additionally, the marked creature has disadvantage
    Constitution saving throws it makes to maintain concentration.

    """

    name = "Withbane Mark"
    source = "Warden (Witchbane Hunter)"


class EldritchReflection(Feature):
    """At 6th level, when you succeed on a saving throw against a spell, you
    can use your reaction to cast the spell back at the caster, as though it
    originated from you, turning the caster into the target. Once you reflect
    a spell in this way, you can’t do so again until you finish a long rest.

    """

    name = "Eldritch Reflection"
    source = "Warden (Witchbane Hunter)"


class SpellResistance(Feature):
    """Beginning at 13th level, you have advantage on saving throws you make
    against spells.

    """

    name = "Spell Resistance"
    source = "Warden"


class Antimage(Feature):
    """At 20th level, you can use your bonus action to transform into an
    arbiter of spellcasters, a breaker of mages, wreathed with antimagic. For
    the next minute, you have advantage the first attack roll you make on each
    of your turns. Additionally, whenever you use your Warden’s Grasp, the
    area affected becomes an antimagic field, as per the spell. You can wrap
    the field around creatures you choose within its radius, creating pockets
    where magic still functions, even though magic originating there can’t
    extend to the rest of the field.

    Once you use this ability, you can’t use it again until you finish a long
    rest.

    """

    name = "Antimage"
    source = "Warden (Witchbane Hunter)"


class ArmorProficiencyWarden(Feature):
    """You gain proficiency with heavy armor.
    """

    name = "Armor Proficiency"
    source = "Warden (Sentinel's Stand)"


class PrimalToughness(Feature):
    """Your hit point maximum increases by 1 + your Constitution modifier, and
    it increases by 1 every time you gain a level in this class.
    """

    name = "Primal Toughness"
    source = "Warden (Sentinel's Stand)"


class StalwartSpirit(Feature):
    """You gain proficiency in one saving throw of your choice.
    """

    name = "Stalwart Spirit"
    source = "Warden (Sentinel's Stand)"


class SentinelsStand(Feature):
    """Wardens are towers that cannot easily be felled. At 1st level, choose
    one of the following features:

    - Armor Proficiency
    - Primal Toughness
    - Stalwart Spirit

    """

    options = {
        "Armor Proficiency": ArmorProficiencyWarden,
        "Primal Toughness": PrimalToughness,
        "Stalwart Spirit": StalwartSpirit
    }
    name = "Sentinel's Stand"
    source = "Warden"


class WardensGrasp(Feature):
    """At 1st level, as a bonus action, you can use the force of your daunting
    presence to ensnare nearby enemies into combat. Until the beginning of
    your next turn, you can’t move, and each Large or smaller creature you
    choose within 5 feet can’t willingly move away from you unless it first
    takes the Disengage action.

    At 14th level, the range of this ability increases to 10 feet.

    """

    name = "Warden's Grasp"
    source = "Warden"


class WardensMark(Feature):
    """At 2nd level, you can use your bonus action to mark a creature you can
    see within 30 feet. While a marked creature is within 5 feet of you, it
    has disadvantage on any attack roll that doesn’t target you. The mark
    lasts for 1 minute, or until you mark another creature, become
    incapacitated, or die.

    At 11th level, whenever you take the Attack action on your turn, you can
    make an additional attack against a creature you have marked.

    """

    name = "Warden's Mark"
    source = "Warden"


class ChampionsCall(Feature):
    """By the time you reach 3rd level, you feel the inexorable pull of an
    important duty or task that you assume as your own. No outside force
    compels your choice or enforces your conduct; if you fail in your charge,
    you alone are responsible.

    Your choice grants you features at 3rd level and again at 6th, 13th, and
    20th level.

    - Bloodwrath Guardian
    - Carrion King
    - Fey Trailblazer
    - Godsworn
    - Grey Watchman
    - Hellkeeper
    - Iceheart Bastion
    - Lawbringer
    - Lorekeeper
    - Nightgaunt
    - Soulblood Shaman
    - Stoneheart Defender
    - Storm Sentinel
    - Verdant Protector
    - Witchbane Hunter

    """

    name = "Champion's Call"
    source = "Warden"


class WardensResolve(Feature):
    """Starting at 3rd level, whenever your hit points are less than half your
    maximum, you have resistance to bludgeoning, piercing, and slashing damage.

    Starting at 17th level, when your hit points are less than half your
    maximum, you have resistance to all damage except psychic.

    """

    name = "Warden's Resolve"
    source = "Warden"


class FontOfLife(Feature):
    """By 4th level, you can use your action to end either one disease or one
    condition afflicting you. The condition can be blinded, charmed, deafened,
    frightened, paralyzed, or poisoned. You can use this action even if the
    condition you end would otherwise prevent it. Once you use this ability,
    you must finish a short or long rest before you can use it again.


    At 15th level, once per day when you use this ability, your hit points are
    also restored to half your maximum, if they were lower.

    """

    name = "Font of Life"
    source = "Warden"


class ExtraAttackWarden(Feature):
    """Beginning at 5th level, you can attack twice, instead of once, whenever
    you take the Attack action on your turn.

    """

    name = "Extra Attack"
    source = "Warden"


class Earthstrength(Feature):
    """You possess the might of the earth itself. Your carrying capacity
    doubles, and you have advantage on ability checks and saving throws
    against being pushed against your will or knocked prone.
    """

    name = "Earthstrength"
    source = "Warden (Sentinel's Step)"


class ThunderingCharge(Feature):
    """On your first round of combat, your speed increases by 30 feet and you
    have advantage on the first melee weapon attack you make.
    """

    name = "Thundering Charge"
    source = "Warden (Sentinel's Step)"


class Wildblood(Feature):
    """Your reflexes have been honed by the perils of nature. You can’t be
    surprised while you are conscious. Additionally, you have a +5 bonus to
    your passive Wisdom (Perception) and passive Intelligence (Investigation)
    scores.
    """

    name = "Wildblood"
    source = "Warden (Sentinel's Step)"


class SentinelsStep(Feature):
    """Wardens are faultless trackers, which can navigate hazardous terrain
    with ease. At 7th level, select one of the following features.

    - Earthstrength
    - Thundering Charge
    - Wildblood

    """

    options = {
        "Earthstrength": Earthstrength,
        "Thundering Charge": ThunderingCharge,
        "Wildblood": Wildblood
    }
    name = "Sentinel's Step"
    source = "Warden"


class Undying(Feature):
    """At 9th level, when you are reduced to 0 hit points and are not killed
    outright, you can choose to drop to 1 hit point instead. Once you use this
    ability, you can’t use it again until you finish a long rest.

    """

    name = "Undying"
    source = "Warden"


class Interrupt(Feature):
    """Starting at 10th level, as a reaction when a creature within 5 feet of
    you makes a melee attack against you, you can punctuate its strikes. After
    that attack, the creature can make one fewer attack than normal on this
    turn.

    """

    name = "Interrupt"
    source = "Warden"


class AgelessGuardian(Feature):
    """You are immune to poison and disease, no longer need food or water,
    suffer none of the frailty of old age, and can’t be aged magically. You
    can still die of old age, however.

    Additionally, you have advantage on Dexterity saving throws.
    """

    name = "Ageless Guardian"
    source = "Warden (Sentinel's Soul)"


class EyesOfTheMountain(Feature):
    """ou gain tremorsense with a range of 15 feet, and can detect the
    presence of hidden or invisible creatures within 30 feet.

    Additionally, you have advantage on Constitution saving throws.
    """

    name = "Eyes of the Mountain"
    source = "Warden (Sentinel's Soul)"


class ImpenetrableMind(Feature):
    """Your thoughts can't be read, and you can't be charmed or frightened.
    """

    name = "Impenetrable Mind"
    source = "Warden (Sentinel's Soul)"


class SentinelsSoul(Feature):
    """Wardens are unshakable guardians that cannot be bowed. At 18th level,
    choose one of the following features:

    - Ageless Guardian
    - Eyes of the Mountain
    - Impenetrable Mind

    """

    options = {
        "Ageless Guardian": AgelessGuardian,
        "Eyes of the Mountain": EyesOfTheMountain,
        "Impenetrable Mind": ImpenetrableMind
    }

    name = "Sentinel's Soul"
    source = "Warden"
