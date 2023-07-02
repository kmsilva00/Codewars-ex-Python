# [
#  0, # 0 is the root and does not depend on any skill.
#  0, # 1 is unlocked by skill 0 (skill at index 0).
#  0, # 2 is unlocked by skill 0.
#  1, # 3 is unlocked by skill 1.
#  3, # 4 is unlocked by skill 3.
#  3, # 5 is unlocked by skill 3.
#  2  # 6 is unlocked by skill 2.
# ]

# visualized:
        # 0
        # ├── 1
        # │   └── 3
        # │       ├── 4
        # │       └── 5
        # └── 2
        #     └── 6


def count_skillsSol(tree, required):
    skils = set()
    for r in required:
        while r not in skils:
            skils.add(r)
            r = tree[r]
    return len(skils)


def count_skills(tree, required):
    # your code here
    requiredSkills = [0] * 200000
    
    if(len(required) == 0):
        return 0
    
    for t in required:        
        # get current skill
        curSkill = t
                
        # if not end
        while curSkill != 0:
            if requiredSkills[curSkill] > 0:
                break

            # add to required skills
            requiredSkills[curSkill] = 1
            
            # go to next skill
            curSkill = tree[curSkill]
            
    requiredSkills[0] = 1
    return sum(requiredSkills)