from app.core import StoryLoop

if __name__ == '__main__':
    stage_list = "stage_list"
    loop = StoryLoop(stage_list)
    loop.game_story_loop()
