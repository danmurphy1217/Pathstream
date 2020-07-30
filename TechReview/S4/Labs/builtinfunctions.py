from views_likes import video_views, video_likes
print(f"Likes: {video_likes}")
print(f" Views: {video_views}")

# TASK ONE: Zip the video_likes and video_views lists
zipped = list(zip(video_likes, video_views))


# TASK TWO: Use map to divide the video likes by video views, use the zipped list
def divide_likes_views(pairs):
    return round(pairs[0]/pairs[1], 2)
percent_likes = list(map(divide_likes_views, zipped))



# TASK THREE: Use a function and a for loop to print the percentage of viewers who liked each video.

def output_percentages(percentages):
    for percentage in percentages:
        print(f"{round(percentage*100, 2)}% of viewers liked this video")
output_percentages(percent_likes)


# TASK FOUR: Use the filter() function to determine the number of videos that have a ratio of likes to views over 50%
def remove_lower(percent):
    if percent > .50:
        return True
    return False
print(list(filter(remove_lower, percent_likes)))

