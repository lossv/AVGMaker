import json
import os
from typing import List


# 阶段内单个对话配置
class StoryNodeConfig:
    # 当日剧情ID
    stage_story_id: str
    # 剧情文本
    text: str
    # 选择描述
    simple_desc_text: str
    # 是否跳转到指定阶段的剧情
    jump: bool
    # 跳到哪个阶段阶段
    jump_stage: int
    # 跳转到那个剧情
    jump_stage_story_id: int
    # 故事结束 通关
    end_story: bool
    # 可选当前阶段剧情ID
    choose_story_id_list: List[int]

    def __repr__(self):
        return json.dumps(self.__dict__, indent=4, ensure_ascii=False)


# 阶段节点配置
class StageNodeConfig:
    # 第几阶段
    stage: int
    stage_story_list: {} = None

    def __repr__(self):
        return json.dumps(self.__dict__, indent=4, ensure_ascii=False)


class ConfigMgr:
    def __init__(self, _story_node_config_dir):
        self.story_node_config_dir = _story_node_config_dir
        self.stage_dict = {}
        self.parse_config()
        print("配置载入成功")

    def parse_config(self):
        file_list = os.listdir(self.story_node_config_dir)

        for stage in file_list:
            stage_story_node_file_path = os.path.join(self.story_node_config_dir, stage)
            story_node_file_list = os.listdir(stage_story_node_file_path)

            stage_config = StageNodeConfig()
            stage_config.stage = stage
            stage_config.stage_story_list = {}
            for story_node_file_name in story_node_file_list:
                real_path = os.path.join(stage_story_node_file_path, story_node_file_name)
                with open(real_path, 'r', encoding='utf-8') as f:
                    try:
                        # 从文件中读取 JSON 数据并解析为 Python 对象
                        story_node = StoryNodeConfig()
                        tmp_dict = json.load(f)
                        stage_story_id = int(tmp_dict["stage_story_id"])

                        for key, value in tmp_dict.items():
                            setattr(story_node, key, value)

                        stage_config.stage_story_list[stage_story_id] = story_node

                        print(f"解析{real_path} 完成")

                    except json.JSONDecodeError as e:
                        raise ValueError("JSON 解析错误") from e

            self.stage_dict[int(stage)] = stage_config
