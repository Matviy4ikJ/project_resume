import base64

from flask_login import login_user, login_required, logout_user, current_user
from flask import render_template, redirect, url_for, flash, request, make_response
from fpdf import FPDF
from pdfkit import pdfkit

from app import app, tools, db
from app.forms import *
from app.models import *
from werkzeug.security import (
    generate_password_hash,
    check_password_hash,
)


@app.route("/")
def index():
    if current_user.is_authenticated:
        return render_template("profile.html")
    return render_template("index.html")


@app.route('/profile')
def profile():
    pass


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(User).where(User.email == form.email.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for("index"))

            flash("Wrong password")
            return redirect(url_for("login"))

        flash("Wrong nickname")
        return redirect(url_for("login"))

    return render_template("login.html", form=form, title="Login")


@app.route('/resume', methods=['GET', 'POST'])
@login_required
def change_resume():
    form = ProfileForm()

    if form.validate_on_submit():
        current_user.first_name = form.name.data

        current_user.phone = form.phone.data
        current_user.education = form.education.data
        current_user.soft_skills = form.soft_skills.data
        current_user.hard_skills = form.hard_skills.data
        current_user.address = form.address.data
        current_user.profession = form.profession.data
        current_user.lang = form.lang.data
        current_user.description = form.description.data
        if form.image.data:
            current_user.image = form.image.data

        db.session.commit()
        return redirect(url_for('index'))


    form.name.data = current_user.first_name
    form.phone.data = current_user.phone
    form.education.data = current_user.education
    form.soft_skills.data = current_user.soft_skills
    form.hard_skills.data = current_user.hard_skills
    form.address.data = current_user.address
    form.profession.data = current_user.profession
    form.lang.data = current_user.lang
    form.description.data = current_user.description

    return render_template('change_profile.html', form=form)


@app.route('/generate_pdf')
@login_required
def generate_pdf():

    user = current_user

    name_surname = user.name_surname
    phone_number = user.phone_number
    email = user.email
    education = user.education
    lang = user.lang
    lang_level = user.lang_level
    country = user.country
    city = user.city
    description = user.description
    profession = user.profession
    soft_skills = user.soft_skills
    tech_skills = user.tech_skills
    projects = user.projects
    how_long = user.how_long
    job_description = user.job_description
    past_work = user.past_work
    image = user.image
    photo_data = ''

    if image is not None:
        photo_data = base64.b64encode(image).decode('utf-8')

    html_content = render_template('download_aspdf.html', profession=profession, name_surname=name_surname,
                                  phone_number=phone_number, email=email, education=education,
                                  tech_skills=tech_skills, soft_skills=soft_skills, projects=projects,
                                  lang=lang, lang_level=lang_level, country=country, city=city,
                                  past_work=past_work, how_long=how_long, job_description=job_description,
                                  description=description, photo_data=photo_data)

    pdf = pdfkit.from_string(html_content, False)
    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "attachment; filename=Resume.pdf"
    return response

@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        user = db.session.execute(db.select(User).where(User.email == form.email.data)).scalar()
        if user:
            flash("User currently exists")
            return redirect(url_for("login"))
        new_user = User(
            email=form.email.data,
            password=generate_password_hash(form.password.data)
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html", form=form, title="Signup")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))
