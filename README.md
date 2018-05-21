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
$ git checkout -b myapp_\branch myapp\_remote/master
```

&nbsp;&nbsp;&nbsp;&nbsp;You now have both the project and the app at `master` and `myapp_branch`, respectively.

8. Checkout `master`.
9. Pull `myapp_branch` into `myapp` subdirectory within your project using:

```
git read-tree --prefix=myapp/ -u myapp_branch
```

&nbsp;&nbsp;&nbsp;&nbsp; Your project-level directory should now contain the `myapp` application, complete with its independent git repo and history.

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

The reverse can also be done; make changes in the `\myapp` subdirectory of the master branch then merge them into your `myapp_branch` to push them upstream.

___

#TODO - Add code snippets illustrating how reverse commits can be made.


