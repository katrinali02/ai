def ask(var, value, evidence, bn): #calculate conditional probability P(var=value | evidence)
    
    # extend evidence to include hypothesis variable with its value in evidence dict
    extended_evidence = evidence.copy()
    extended_evidence[var] = value #used to include hypothesis in prob calculation

    """
    why we need to create a copy of the evidence: here, the algorithm needs to explore different hypothetical
    scenarios where the values of certain variables are assumed to be True or False, especially when those values
    are not known in the evidence

    the function also needs to modify the dictionary by changing the values of some variables,
    so to keep the og evidence immutable, we create an independent copy
        --> if we modify the og evidence dict, these changes will persist across recursive calls, leading to incorrect
        calculations, so each recursive call needs a version of evidence independent of others

    also: dictionaries do not store actual objects, but references to memory locations where those objects are held
    """

    # calculate joint probabilities for hypothesis and evidence + joint prob for evidence alone; done for normalization
    joint_prob = joint_probability(bn.variables, extended_evidence, bn)
    evidence_prob = joint_probability(bn.variables, evidence, bn)

    # normalize joint prob by joint evidence (alone) prob to get conditional prob of hypothesis given evidence
    return joint_prob / evidence_prob

def joint_probability(variables, evidence, bn): #recursively calculates joint prob. of given set of evidence
    
    #when no more bn variables are left to process
    if not variables:
        return 1 #1 is multiplicative identity in probability

    #process first variable
    var = variables[0] #select first variable; use 'variables' instead of bn.variables bc then joint_probability can process each variable exactly once w/o repeating
    remaining_vars = variables[1:] #separate remaining variables
    
    #directly calculate probability if variable value is known
    if var.name in evidence:
        prob = var.probability(evidence[var.name], evidence)
        return prob * joint_probability(remaining_vars, evidence, bn)
    
    # sum over both possible values if variable value is unknown
    else:
        true_evidence = evidence.copy() #create scenario where variable is True
        true_evidence[var.name] = True
        false_evidence = evidence.copy() #create scenario where variable is False
        false_evidence[var.name] = False

        """
        like explained in the ask function, we have to use evidence.copy() again here so that we maintain the integrity
        of the original evidence dictionary but still allow us to explore different hypothetical scenarios in its recursive calls
        """

        return (var.probability(True, evidence) * joint_probability(remaining_vars, true_evidence, bn) +
                var.probability(False, evidence) * joint_probability(remaining_vars, false_evidence, bn))
