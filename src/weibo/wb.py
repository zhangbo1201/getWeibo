'''
Created on 2017年7月29日

@author: zhangbo
'''

import requests; #兼容版本的库
import json; #字典
import re; #解析不规则文本
from pydoc import html

#评论请求所需要的参数
'''
uid:1742566624
type:uid
value:1742566624
containerid:1076031742566624
'''

class Weibo(object):
    def get_weibo(self,id,page):#个人ID
        '''
                        获取指定博主的内容
        '''
        url='https://m.weibo.cn/api/container/getIndex?uid={}&type=uid&value={}&containerid=107603{}&page={}'.format(id,id,id,page);
        response = requests.get(url);
        ob_json = json.loads(response.text);
        #print(ob_json);
        list_crads = ob_json.get('cards');
        return list_crads;
    
    def get__comments(self,id,page):
        
        '''
        id=4078091594410720
        '''
        url = 'https://m.weibo.cn/api/comments/show?id={}&page={}'.format(id,page);
        response = requests.get(url);
        ob_json =  json.loads(response.text);
        list_comment = ob_json.get('hot_data');
        return list_comment;
    
    def main(self,uid,page):
        list_cards = self.get_weibo(uid,page);
        for card in list_cards:
            if card.get('card_type')== 9:#等于9的才是微博，其他都是推荐
                id = card.get('mblog').get('id'); #微博的id
                text = card.get('mblog').get('text'); #微博的内容
                source = card.get('mblog').get('source');
                if source == '':
                        source = u'未知';
                print('***');
                print(u'@@@用户'+id+u'@@@微博'+text+u'@@@来源'+source+'\n');
                
                
                list_comments = self.get__comments(id,1);
                count_hotcomments = 0;
                for comment in list_comments:
                    created_at = comment.get('created_at');#获取时间
                    like_counts = comment.get('like_counts');#点赞数
                    text = comment.get('text');#回复
                    #tree = html.preformat(text);
                    #text = tree.xpath('string(.)');#用string函数过滤多余标签
                    name_user = comment.get('user').get('screen_name');
                    commentSource = comment.get('source');
                    if commentSource == '':
                        commentSource = u'未知';
                    print (str(count_hotcomments),':**',name_user,'**',u' ** 发表于** '+created_at,u'点赞：'+str(like_counts),u'来自：'+commentSource+'\n');
                    print (text+'\n');
                    count_hotcomments +=1;
                print('==================================');
                    
if __name__ == '__main__':
    Weibo = Weibo()
    for page in range(1,2):
        Weibo.main(1742566624, page);
    




