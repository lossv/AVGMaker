from app.node import ConfigMgr, StoryNodeConfig, StageNodeConfig


class StoryArchive:
    stage_story_id: int = None
    stage: int = None


class StoryLoop:
    def __init__(self, _story_node_config_dir):
        self.config_mgr = ConfigMgr(_story_node_config_dir)
        self.story_achieve: StoryArchive = StoryArchive()
        self.story_node = StoryNodeConfig()
        self.stage_config = StageNodeConfig()

    def load_story_achieve(self):
        # 加载存档
        pass

    def save_story_achieve(self):
        # 存档
        pass

    def choose_story_achieve(self):
        pass

    def game_story_loop(self):

        if self.story_achieve.stage is None and self.story_achieve.stage_story_id is None:
            self.story_achieve.stage = 1
            self.story_achieve.stage_story_id = 1
            # 剧情开始 初始化剧情

        # 开始上一次的剧情
        self.stage_config: StageNodeConfig = self.config_mgr.stage_dict[self.story_achieve.stage]
        self.story_node: StoryNodeConfig = self.stage_config.stage_story_list[self.story_achieve.stage_story_id]

        try:
            while True:
                self.try_enter_new_stage()

                print(f"剧情描述：{self.story_node.text}")

                if self.story_node.end_story:
                    print("故事结束")
                    return

                print("选择以下选择支线")
                for index, value in enumerate(self.story_node.choose_story_id_list):
                    print(f"{index}: {self.stage_config.stage_story_list[value].simple_desc_text}")

                while True:
                    select_index = input("请选择剧情:\n")
                    if select_index == "quit":
                        print("游戏结束")
                        return
                    int_select_index = int(select_index)
                    if 0 <= int_select_index <= len(self.story_node.choose_story_id_list):
                        self.do_choose_story(int(select_index))
                        break

        except Exception as e:
            print(e)

    def do_choose_story(self, index: int):
        story_id = self.story_node.choose_story_id_list[index]
        self.story_node: StoryNodeConfig = self.stage_config.stage_story_list[story_id]

    def try_enter_new_stage(self):
        if not self.story_node.jump:
            return

        self.stage_config: StageNodeConfig = self.config_mgr.stage_dict[self.story_node.jump_stage]
        self.story_node: StoryNodeConfig = self.stage_config.stage_story_list[self.story_node.jump_stage_story_id]
