# example-subtree
Example of Git subtree usage in Django

## Setup

See [here](https://git-scm.com/book/en/v1/Git-Tools-Subtree-Merging) for guidance.

Steps to follow:

1. Create project-level repo in GitHub, eg. Thomas-95/example-subtree
2. Start Django project locally. 
3. Initialise with remote project-level repo and push initial commit.
4. Create app-level repo in GitHub, eg. Thomas-95/myapp
5. Add that as a remote to your project:

```
$ git remote add myapp_remote git@github.com:Thomas-95/myapp
```

6. Run `$ git remote`. You should see the following:

```
$ git remote
myapp_remote
origin
```

7. Set root of `myapp` application to a myapp_branch using:

```
$ git checkout -b myapp_branch myapp_remote/master
```

&nbsp;&nbsp;&nbsp;&nbsp;You now have both the project and the app at `master` and `myapp_branch`, respectively.

8. Checkout `master`.
9. Pull `myapp_branch` into `myapp` subdirectory within your project using:

```
git read-tree --prefix=myapp/ -u myapp_branch
```

&nbsp;&nbsp;&nbsp;&nbsp; Your project-level directory should now contain the `myapp` application, complete with its independent git repo and history.

___

#TODO - Check that the below is not, in fact, the correct way to do this:

`$ git subtree git subtree add --prefix=myapp/ dc9c11fc35ce10db866514c2c4a4437cbf8cadd3`

where the code is that of the subtree master's latest commit. Try merging changes onto this instead of read-tree.
___


## Handling changes

Update changes within in the `myapp` repo at a project level using:

```
$ git checkout myapp_branch
$ git pull
```

Then merge these changes back into master using:

```
$ git checkout master
$ git merge --squash -s subtree --no-commit myapp_branch
```

___
#TODO - Check that `$ git subtree pull --prefix=myapp_subtree/ --squash myapp_remote master` wouldn't be better.
___

The reverse can also be done; make changes in the `\myapp` subdirectory of the master branch then merge them into your `myapp_branch` to push them upstream.

```
$ git subtree push -P myapp_subtree/ myapp_remote test-using-subtree-push
```

This will take *every* commit which touched the subtree and push them to a new branch `test-using-subtree-push`. The changes can then be merged into its master branch in the repo itself.

[This](https://medium.com/@porteneuve/mastering-git-subtrees-943d29a798ec) article suggests the push can be done manually with `$ git cherry-pick`. May be useful to note later on.




## Example usage

1. Checkout `myapp_branch`
2. Make changes to `models.py`
3. Add and commit these changes.
4. Run `$ git push myapp_remote myapp_branch`
5. You will see that a new branch has been made at Thomas-95/myapp called `myapp_branch` which contains the changes made.
6. Instead push the changes to `myapp_remote/master` using `$ git push myapp_remote HEAD:master`
7. Checkout project's `master` branch: `$ git checkout master`
8. Merge the changes to `myapp_remote/master` into `master`:

```
$ git merge --squash -s subtree --no-commit myapp_branch
```
9. Add all the changes with `$ git add .` then commit & push them.

___

#TODO - Check commands 8. and 9. above are the desired ones.
___
