#! /usr/bin/python

import youtube
import ultrajson as json
import argparse

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Pull some youtube with a key')

    parser.add_argument("--key", help="https://cloud.google.com/console", required=True)

    args = parser.parse_args()

    key = args.key

    playlist = "PLTcojYWKm_xq4mQ7K0uRo0q_ecLlE9Efk"

    # Create client with dev key
    client = youtube.YTClient(key)

    # Single playlist info
    playlist_info = client.get_playlist_info(playlist)
    print "PLAYLIST INFO --> ", json.dumps(playlist_info), "\n\n"

    # Videos for playlist
    videos = client.get_videos_from_playlist(playlist)

    print "PLAYLIST VIDEOS --> ", json.dumps(videos), "\n\n"

    # For each video
    for video in videos.get("items",[]):
        # Grab video id
        vid_id = video["contentDetails"]["videoId"]
        
        # Grab video info based on id
        video_info = client.get_video_info(vid_id)
        print "VIDEO ID --> ", vid_id, "\n\nINFO --> ", json.dumps(video_info), "\n\n"

        # Grab top level comments, replies, and commenting user id's for a video.
        # Some 'some_replies' will be duplicates of the replies in top_level_comments.
        top_level_comments, some_replies, commenting_user_ids = client.get_video_data(vid_id)

        print "COMMENTS --> ", json.dumps(top_level_comments), "\n\n"

        print "SOME REPLIES --> ", json.dumps(some_replies), "\n\n"

        print "USER/CHANNEL IDS --> ", commenting_user_ids, "\n\n"

        # Get activities for all users.  Note that this might take a while.
        for uid in commenting_user_ids:
            if uid:
                print "USER ID --> ", uid, "\n\n"
                user_activities = client.get_all_activities_for_channel(uid)
                print  "ACTIVITIES --> ", json.dumps(user_activities), "\n\n"