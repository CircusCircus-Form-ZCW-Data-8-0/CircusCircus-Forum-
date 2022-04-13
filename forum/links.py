from Flask import Markup

url_label = Markup("<a href='YOUR_URL'>Main Website</a>)



# @login_required
# @app.route('/action_post', methods=['POST'])
# def action_post():
# 	subforum_id = int(request.args.get("sub"))
# 	subforum = Subforum.query.filter(Subforum.id == subforum_id).first()
# 	if not subforum:
# 		return redirect(url_for("subforums"))
#
# 	user = current_user
# 	title = request.form['title']
# 	content = request.form['content']
# 	#check for valid posting
# 	errors = []
# 	retry = False
# 	if not valid_title(title):
# 		errors.append("Title must be between 4 and 140 characters long!")
# 		retry = True
# 	if not valid_content(content):
# 		errors.append("Post must be between 10 and 5000 characters long!")
# 		retry = True
# 	if retry:
# 		return render_template("createpost.html",subforum=subforum,  errors=errors)
# 	post = Post(title, content, datetime.datetime.now())
# 	subforum.posts.append(post)
# 	user.posts.append(post)
# 	db.session.commit()
# 	return redirect("/viewpost?post=" + str(post.id))