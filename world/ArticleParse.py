class NaturalCommand(Command):
    """
    A command that may be specified with with a preposition, e.g. put apple in box.  The regular expression is designed
    to pull the sentence apart into its component parts by recognising common or specified prepositions and the words
    position in the sentence.  It is able to distinguish nouns (apple, box, car), adjectives (dirty, new, rotten),
    articles (the, a, an) and prepositions.  The command verb is set via the BaseCommand key attribute and isn't
    passed via the parser here.  Sentence groups are defined thus:

        article1 = The article (if any) preceding the first noun
        noun1 = The noun (and at this time the associated adjectives) preceding the preposition
        preposition = One of the default or specified prepositions.
                      Prepositions can be overloaded inside the child command class.  This should be done for all
                      commands in order to make the regex more efficient and to avoid grammatically inconsistent
                      prepositions from being allowed.  The default list is employed as a catch all in the event no
                      prepositions have been declared so that the command is (probably) functional.
        article2 = The article (if any) following the preposition
        noun2 = The noun following the preposition

    In the even that there is no preposition, the first regex fails and no sentence group is created.  This is tested
    and if self.sentence is None, a second regex is tried which excludes the preposition criteria.  All sentence groups
    are defined by the end, even if None, so that the command function can test for their presence (or absence) when
    applying grammatical rules (such as resolved nouns being the same, or no second noun being defined).

    Nouns need to be resolved to objects via the self.caller.search() function, in order for the command to apply to
    objects.  The parser simply finds references to objects, not the objects themselves.
    """

    # This is the default preposition list
    prepositions = ["above", "after", "against", "along", "around", "as", "at", "before", "behind", "below",
                    "beneath", "beside", "between", "by", "close to", "down", "except", "excluding", "for"
                    "from", "in", "inside", "into", "near", "near to", "next to", "of", "off", "on", "onto",
                    "on to", "opposite", "outside", "over", "on top of", "out of", "past", "round", "than",
                    "through", "till", "to", "touching", "toward", "towards", "together with", "under",
                    "underneath", "until", "up", "upon", "up against", "up to", "up until", "versus", "via",
                    "with", "within", "without"]

    def parse(self):

        # This sets the sentence components to none
        self.article1 = None
        self.noun1 = None
        self.preposition = None
        self.article2 = None
        self.noun2 = None

        # This is the prepositional regex
        regex = r"^\s?\b(?P<article1>the|an|a)?\b\s?(?P<noun1>.*?\w+)\s?\b(?P<preposition>" + \
                r"|".join(self.prepositions) + r")\b\s?\b(?P<article2>the|an|a)?\b\s+(?P<noun2>.*?\w+)$"
        self.sentence = re.match(regex, self.args.lower())

        if not self.sentence:
            # This is the non-prepositional regex
            regex =  r"^\s?\b(?P<article1>the|an|a)?\b\s?(?P<noun1>.*?\w+)$"
            self.sentence = re.match(regex, self.args.lower())

        # Sentence components are set by attempting to set each group in turn.  If any group doesn't exist, an
        # IndexError exception is raised and the nex group is tried.  I'd rather change this out for a less "cludgy"
        # solution, but just now I can't find how to iterate the group titles, only the values.
        try:
            self.article1 = self.sentence.group("article1")
        except IndexError:
            pass
        try:
            self.noun1 = self.sentence.group("noun1")
        except IndexError:
            pass
        try:
            self.preposition = self.sentence.group("preposition")
        except IndexError:
            pass
        try:
            self.article2 = self.sentence.group("article2")
        except IndexError:
            pass
        try:
            self.noun2 = self.sentence.group("noun2")
        except IndexError:
            pass