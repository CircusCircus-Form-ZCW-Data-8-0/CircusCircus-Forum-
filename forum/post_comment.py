#
#
# @login_required
# @app.route('/addpost')
# def addpost():
#     subforum_id = int(request.args.get("sub"))
#     subforum = Subforum.query.filter(Subforum.id == subforum_id).first()
#     if not subforum:
#         return error("That subforum does not exist!")
#
#     return render_template("createpost.html", subforum=subforum)
#
#
# @app.route('/viewpost')
# def viewpost():
#     postid = int(request.args.get("post"))
#     post = Post.query.filter(Post.id == postid).first()
#     if not post:
#         return error("That post does not exist!")
#     if not post.subforum.path:
#         subforum.path = generateLinkPath(post.subforum.id)
#     comments = Comment.query.filter(Comment.post_id == postid).order_by(
#         Comment.id.desc())  # no need for scalability now
#     return render_template("viewpost.html", post=post, path=subforum.path, comments=comments)
#
#
# # ACTIONS
#
# @login_required
# @app.route('/action_comment', methods=['POST', 'GET'])
# def comment():
#     post_id = int(request.args.get("post"))
#     post = Post.query.filter(Post.id == post_id).first()
#     if not post:
#         return error("That post does not exist!")
#     content = request.form['content']
#     postdate = datetime.datetime.now()
#     comment = Comment(content, postdate)
#     current_user.comments.append(comment)
#     post.comments.append(comment)
#     db.session.commit()
#     return redirect("/viewpost?post=" + str(post_id))
#
#
# @login_required
# @app.route('/action_post', methods=['POST'])
# def action_post():
#     subforum_id = int(request.args.get("sub"))
#     subforum = Subforum.query.filter(Subforum.id == subforum_id).first()
#     if not subforum:
#         return redirect(url_for("subforums"))
#
#     user = current_user
#     title = request.form['title']
#     content = request.form['content']
#     # check for valid posting
#     errors = []
#     retry = False
#     if not valid_title(title):
#         errors.append("Title must be between 4 and 140 characters long!")
#         retry = True
#     if not valid_content(content):
#         errors.append("Post must be between 10 and 5000 characters long!")
#         retry = True
#     if retry:
#         return render_template("createpost.html", subforum=subforum, errors=errors)
#     post = Post(title, content, datetime.datetime.now())
#     subforum.posts.append(post)
#     user.posts.append(post)
#     db.session.commit()
#     return redirect("/viewpost?post=" + str(post.id))
#
