# def find_most_frequent_keywords(scenes):
  
#   keywordCounter = {}
#   frequentKeywords = []
  
#   for keywordList in scenes.values():
#     for keyword in keywordList:
#       if keyword not in keywordCounter:
#         keywordCounter[keyword] = 0
#       keywordCounter[keyword] += 1
    
    
#   max_keyword = max(keywordCounter.values())
  
#   for keyword, count in keywordCounter.items():
#     if count == max_keyword:
#       frequentKeywords.append(keyword)
    
#   return frequentKeywords
  
  
# # Example Usage:

# scenes = {
#     "Scene 1": ["action", "hero", "battle"],
#     "Scene 2": ["hero", "action", "quest"],
#     "Scene 3": ["battle", "strategy", "hero"],
#     "Scene 4": ["action", "strategy"]
# }
# print(find_most_frequent_keywords(scenes))

# scenes = {
#     "Scene A": ["love", "drama"],
#     "Scene B": ["drama", "love"],
#     "Scene C": ["comedy", "love"],
#     "Scene D": ["comedy", "drama"]
# }
# print(find_most_frequent_keywords(scenes)) 
# # Example Output:

# ['action', 'hero']
# ['love', 'drama']

# from collections import deque

# def track_scene_transitions(scenes):
#     scenes = deque(scenes)
    
#     lastScene = None
#     while scenes:
#       currScene = scenes.popleft()
      
#       if currScene and lastScene:
#         print(f"transition from {lastScene} to {currScene}")
#       lastScene = currScene
      
# scenes = ["Opening", "Rising Action", "Climax", "Falling Action", "Resolution"]
# track_scene_transitions(scenes)
# scenes = ["Introduction", "Conflict", "Climax", "Denouement"]
# track_scene_transitions(scenes)
      
      
# def organize_scene_data_by_date(scene_records):
#   return sorted(scene_records)
    
# scene_records = [
#     ("2024-08-15", "Climax"),
#     ("2024-08-10", "Introduction"),
#     ("2024-08-20", "Resolution"),
#     ("2024-08-12", "Rising Action")
# ]
# print(organize_scene_data_by_date(scene_records))

# scene_records = [
#     ("2023-07-05", "Opening"),
#     ("2023-07-07", "Conflict"),
#     ("2023-07-01", "Setup"),
#     ("2023-07-10", "Climax")
# ]
# print(organize_scene_data_by_date(scene_records))

# def filter_scenes_by_keyword(scenes, keyword):
#   filteredScenes = []
  
#   for scene in scenes:
#     if keyword not in scene:
#       filteredScenes.append(scene)
  
  
#   return filteredScenes
# # Example Usage:

# scenes = [
#     "The hero enters the dark forest.",
#     "A mysterious figure appears.",
#     "The hero finds a hidden treasure.",
#     "An eerie silence fills the air."
# ]
# keyword = "hero"

# filtered_scenes = filter_scenes_by_keyword(scenes, keyword)
# print(filtered_scenes)

# scenes = [
#     "The spaceship lands on an alien planet.",
#     "A strange creature approaches the crew.",
#     "The crew prepares to explore the new world."
# ]
# keyword = "crew"

# filtered_scenes = filter_scenes_by_keyword(scenes, keyword)
# print(filtered_scenes)
# # Example Output:

# ['An eerie silence fills the air.', 'A mysterious figure appears.']
# ['The spaceship lands on an alien planet.']
     
     
    
     
def manage_character_arc(events):




