import read, copy
from util import *
from logical_classes import *

verbose = 0

class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules
        self.ie = InferenceEngine()

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def _get_fact(self, fact):
        """INTERNAL USE ONLY
        Get the fact in the KB that is the same as the fact argument

        Args:
            fact (Fact): Fact we're searching for

        Returns:
            Fact: matching fact
        """
        for kbfact in self.facts:
            if fact == kbfact:
                return kbfact

    def _get_rule(self, rule):
        """INTERNAL USE ONLY
        Get the rule in the KB that is the same as the rule argument

        Args:
            rule (Rule): Rule we're searching for

        Returns:
            Rule: matching rule
        """
        for kbrule in self.rules:
            if rule == kbrule:
                return kbrule

    def kb_add(self, fact_rule):
        """Add a fact or rule to the KB
        Args:
            fact_rule (Fact or Rule) - Fact or Rule to be added
        Returns:
            None
        """
        printv("Adding {!r}", 1, verbose, [fact_rule])
        if isinstance(fact_rule, Fact):
            if fact_rule not in self.facts:
                self.facts.append(fact_rule)
                for rule in self.rules:
                    self.ie.fc_infer(fact_rule, rule, self)
            else:
                if fact_rule.supported_by:
                    ind = self.facts.index(fact_rule)
                    for f in fact_rule.supported_by:
                        self.facts[ind].supported_by.append(f)
                else:
                    ind = self.facts.index(fact_rule)
                    self.facts[ind].asserted = True
        elif isinstance(fact_rule, Rule):
            if fact_rule not in self.rules:
                self.rules.append(fact_rule)
                for fact in self.facts:
                    self.ie.fc_infer(fact, fact_rule, self)
            else:
                if fact_rule.supported_by:
                    ind = self.rules.index(fact_rule)
                    for f in fact_rule.supported_by:
                        self.rules[ind].supported_by.append(f)
                else:
                    ind = self.rules.index(fact_rule)
                    self.rules[ind].asserted = True

    def kb_assert(self, fact_rule):
        """Assert a fact or rule into the KB

        Args:
            fact_rule (Fact or Rule): Fact or Rule we're asserting
        """
        printv("Asserting {!r}", 0, verbose, [fact_rule])
        self.kb_add(fact_rule)

    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Statement to be asked (will be converted into a Fact)

        Returns:
            listof Bindings|False - list of Bindings if result found, False otherwise
        """
        print("Asking {!r}".format(fact))
        if factq(fact):
            f = Fact(fact.statement)
            bindings_lst = ListOfBindings()
            # ask matched facts
            for fact in self.facts:
                binding = match(f.statement, fact.statement)
                if binding:
                    bindings_lst.add_bindings(binding, [fact])

            return bindings_lst if bindings_lst.list_of_bindings else []

        else:
            print("Invalid ask:", fact.statement)
            return []

    def kb_retract(self, fact_rule):
        """Retract a fact or a rule from the KB

        Args:
            fact_rule (Fact or Rule) - Fact or Rule to be retracted

        Returns:
            None
        """
        printv("Retracting {!r}", 0, verbose, [fact_rule])
        ####################################################
        
        # check if the fact_rule is a fact
        if factq(fact_rule):
            fact_rule = self._get_fact(fact_rule) #get matching fact from kb
            #checks if fact is asserted
            if fact_rule.asserted == True:
                fact_rule.asserted = False
            if fact_rule.supported_by: #break out of recursion if we are at the base case or if fact supported by other facts/rules
                return
            self.facts.remove(fact_rule) #remove fact if it's not supported by any other facts/rules
            
        else:  # if it's not a fact it's a rule
            fact_rule = self._get_rule(fact_rule) #get matching rule
            #checks if rule is asserted
            if fact_rule.asserted == True:
                fact_rule.asserted = False
            if fact_rule.supported_by: #break if at base case
                return
            self.rules.remove(fact_rule) #remove the fact if it's not supported by any other facts/rules

        # adjust supported_by lists of facts/rules supported by fact_rule
        for fact in fact_rule.supports_facts:
            for pair in fact.supported_by: #iterate over all facts supported by fact_rule
                if fact_rule in pair:
                    fact.supported_by.remove(pair) #remove if fact_rule is a fact/rule that supports the fact
            # if fact not supported by any other rule/fact or is asserted after removal, retract the fact
            if not fact.supported_by and not fact.asserted:
                self.kb_retract(fact)

        #adjust supported rules
        for rule in fact_rule.supports_rules:
            for pair in rule.supported_by: #iterate over all rules
                if fact_rule in pair:
                    rule.supported_by.remove(pair) #remove if fact_rule is a fact/rule that supports the rule
            # recursively check if this rule should be retracted
            if not rule.supported_by and not rule.asserted:
                self.kb_retract(rule) #retract rule if it's not supported by any other facts/rules or asserted


class InferenceEngine(object):
    def fc_infer(self, fact, rule, kb):
        """Forward-chaining to infer new facts and rules

        Args:
            fact (Fact) - A fact from the KnowledgeBase
            rule (Rule) - A rule from the KnowledgeBase
            kb (KnowledgeBase) - A KnowledgeBase

        Returns:
            Nothing
        """
        printv('Attempting to infer from {!r} and {!r} => {!r}', 1, verbose,
            [fact.statement, rule.lhs, rule.rhs])
        ####################################################
        
        # attempt to match fact with first left hand statement statement of rule; return variable bindings that make them equivalent if statements match
        bindings = match(fact.statement, rule.lhs[0])
        
        # if there are valid bindings from match
        if bindings:
            #using found bindings, create new right hand side via replacing variables in og rhs with matched values
            new_rhs = instantiate(rule.rhs, bindings)
            new_lhs = [instantiate(lhs_stmt, bindings) for lhs_stmt in rule.lhs[1:]] #does ^^ with remaining lhs statments of rule; skips one matched alr

            # if there's no more lhs after applying the bindings - aka everything has been matched and all conditions of rule satisfied by facts available
            if not new_lhs:
                new_fact = Fact(new_rhs, [[fact, rule]]) #infer new fact from instantiated rhs
                kb.kb_assert(new_fact) #assert new fact into kb
                #record og fact and rule as entities that support new fact
                fact.supports_facts.append(new_fact)
                rule.supports_facts.append(new_fact)

            else: #if not all conditions met
                new_rule = Rule([new_lhs, new_rhs], [[fact, rule]]) #new rule created with remaining unmatched lhs conditions and instantiated rhs cond.
                kb.kb_assert(new_rule) #same as fact above but with the rule
                fact.supports_rules.append(new_rule)
                rule.supports_rules.append(new_rule)
