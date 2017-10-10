# Submitting projects

From here on out, you'll be working on full (if small and limited)
applications, which have many more
supporting files (like controller and model files, as well as storyboard and
asset files) than the first lab required. In addition, starting with Lab 3 and
going to the end of the class, you'll be working on one larger application,
adding features every week. So, you will submit your work from here on out
by providing me with a repository link to a (private - see
[here](https://education.github.com/guide/private_repos) for information on
how to get these on github with a student email address) repository on github
or bitbucket. Hopefully you're at least a little familiar with using Git for
version control, but to submit assignments here you'll need to learn a little
bit about how Xcode integrates with Git.

I'm just going to go over the extreme basics (creating a repository for an app,
making commits, and adding/pushing to a remote repository), if you would like
more information on how Xcode integrates advanced Git features like branches,
reverting to old versions, etc,
[this](https://www.raywenderlich.com/153084/use-git-source-control-xcode-9)
is a pretty good article.

## The basics

### Initialization

When you create a new Application project (As you'll do at least twice in this
class), Xcode will prompt you to pick a location to save the project. This will
create a directory for your project at that location. At the bottom of this
window is a checkbox labelled 'Create Git repository on my Mac' - if you check
this, Xcode will initialize the project's folder as a Git repository. Do this
when you're creating your new projects for this class. Xcode will also perform
an initial commit of the default files your project comes with - you can view
this commit by going to the Source Control Navigator (Command-2) and looking
at the master branch.

When you change and save a file, you'll notice that it gets a little
'M' next to its
file name in the navigator - this means it's been modified since your last
commit. To commit the changes you've made (after you confirm they haven't
broken everything), just go to the Source Control menu at the top of the screen
and press 'Commit' (or hit Alt-Command-C). You'll be taken to a screen which
summarizes the changes that have been made since your last commit and allows
you to choose what should go in this new commit. By default, all your changes
will be selected. You can choose not to commit some files, or even discard
changes in the diff that it shows you. When you're done, you can hit enter
a commit message at the bottom and hit 'Commit 1 File' (or however many) to
make your commit. If you have remotes available, you can also push them
right now with the little bottom-left checkbox.

### Remotes

For the TAs to grade your work, you'll need a remote repository to push your
changes to. GitHub integration is really easy with Xcode - You can add a GitHub
account in the Xcode -> Preferences... menu (Accounts tab) - hit the + and
select 'GitHub', then enter your credentials. You can then switch to SSH
authentication, if you have that set up for GitHub.

Creating a remote is easy if you've done this - right click on the project name
in the Source Control navigator (left pane, second tab) and select 'Create
"<projectname>" Remote on GitHub...' - then you can choose a repository name,
whether to make it public or private, and a Remote Name, and Xcode will add the
remote for you, as well as pushing any commits you've already made.

This is all you need to know for submitting your work, but if any of it was
unclear
or you feel like you want to learn/use more advanced features of Git with
Xcode, I highly recommend [this tutorial](https://www.raywenderlich.com/153084/use-git-source-control-xcode-9).
