material of https://github.com/AlekseyDurachenko/vkdevastator


5603207


https://oauth.vk.com/authorize?client_id=5603207&scope=friends,photos,audio,video,docs,notes,pages,status,wall,groups,offline&display=page&redirect_uri=https://oauth.vk.com/blank.html&response_type=token&


https://oauth.vk.com/blank.html#access_token=b573f43b7d46841e677b35011f10a07dfec563f7774dc1dd593c2036da80d340ac9335ea5a6c4ee3a438d&expires_in=0&user_id=153597



b573f43b7d46841e677b35011f10a07dfec563f7774dc1dd593c2036da80d340ac9335ea5a6c4ee3a438d



cd ~/vkdevastator/src

python ./vksearchactivities.py --access-token b573f43b7d46841e677b35011f10a07dfec563f7774dc1dd593c2036da80d340ac9335ea5a6c4ee3a438d --target-id 153597 --state-file state.txt --activities-file activities.txt --activities-detail-file detail.txt


python ./vksearchactivities.py --access-token b573f43b7d46841e677b35011f10a07dfec563f7774dc1dd593c2036da80d340ac9335ea5a6c4ee3a438d --target-id 153597 --state-file state.txt --activities-file activities.txt --activities-detail-file detail.txt --search-user-depth 1 --search-group-depth 2 --limit-member-count 1000

python ./vkdeleteactivities.py --access-token b573f43b7d46841e677b35011f10a07dfec563f7774dc1dd593c2036da80d340ac9335ea5a6c4ee3a438d --activities-file activities.txt

