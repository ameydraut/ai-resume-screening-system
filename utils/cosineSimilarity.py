def cosineSimilarity(vec1,vec2):
    if len(vec1) != len(vec2):
        return 0
    dot = 0
    mag1 = 0
    mag2 = 0
    for i in range(len(vec1)):
        dot += vec1[i] * vec2[i]
        mag1 += vec1[i]**2
        mag2 += vec2[i]**2
    
    if mag1 == 0 or mag2 == 0:
        return 0
    return dot / (mag1*mag2)