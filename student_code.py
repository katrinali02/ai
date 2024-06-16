def ask(var, value, evidence, bn):

    #copy evidence
    extended_evidence = evidence.copy()

    #create extended evidence dictionary to include hypothesis
    extended_evidence[var] = value

    #calculate joint proobabilities
    joint_prob = joint_probability(bn.variables, extended_evidence, bn)
    evidence_prob_only = joint_probability(bn.variables, evidence, bn)

    #get conditional probability
    conditional_probability = joint_prob / evidence_prob_only
    return conditional_probability

def joint_probability(variables, evidence, bn):
    
    #if we have no variables
    if not variables:
        return 1
    
    #when we have the variable names
    else:
    
    #look at first variable, and separate the rest; will use later
        var = variables[0]
        remaining_varibles = variables[1:]

    #if variable value is known we can calculate direct prob
        if var.name in evidence:
            prob = var.probability(evidence[var.name], evidence)
            return prob * joint_probability(remaining_varibles, evidence, bn)
        
        #if variable value is not known we need to sum over both possible vals
        else:
            evidence_true = evidence.copy()
            evidence_true[var.name] = True

            evidence_false = evidence.copy()
            evidence_false[var.name] = False

            prob_true_vals = var.probability(True,evidence) * joint_probability(remaining_varibles, evidence_true, bn)
            prob_false_vals = var.probability(False,evidence) * joint_probability(remaining_varibles, evidence_false, bn)

            return (prob_true_vals + prob_false_vals)