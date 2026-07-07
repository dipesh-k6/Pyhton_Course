# Setup



git config --global user.name "Name"      # set identity name

git config --global user.email "email"    # set identity email

git config --global init.defaultBranch main  # set default branch to main

git config --list                         # see all settings



-----------------------------------------------------------------------------



# Starting repo



git init                    # create new local repo

git remote add origin URL   # connect local repo to GitHub

git remote -v               # verify remote connection



-----------------------------------------------------------------------------



# Workflow



git status                  # check what changed

git add filename            # stage specific file

git add .                   # stage everything

git commit -m "message"     # take snapshot

git push                    # upload to GitHub

git push -u origin main     # first push (sets default)



-----------------------------------------------------------------------------



# History



git log                     # see all commits

git log --oneline           # compact version



-----------------------------------------------------------------------------



# Undo things



git restore filename        # discard changes in working directory

git restore --staged file   # unstage a file

git commit --amend -m "msg" # fix last commit message



-----------------------------------------------------------------------------



# Branches



git branch                  # list all branches

git branch -a               # list local + remote branches

git branch name             # create new branch

git checkout name           # switch to branch

git checkout -b name        # create and switch in one command

git branch -m old new       # rename branch

git branch -d name          # safe delete (merged only)

git branch -D name          # force delete

git merge branchname        # merge branch into current



-----------------------------------------------------------------------------



# SSH



ssh-keygen -t ed25519 -C "email"  # generate new key

ssh-add \~/.ssh/keyname             # add key to agent

ssh-add -l                         # list loaded keys

ssh -T git@github.com              # test GitHub connection



-----------------------------------------------------------------------------



|

