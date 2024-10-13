from flask import Blueprint, request, render_template, redirect, url_for
from .database import add_sotrudnik, delete_sotrudnik, update_sotrudnik, get_all_sotrudniki, get_table_data

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    sotrudniki = get_all_sotrudniki()
    return render_template('index.html', sotrudniki=sotrudniki)

@bp.route('/add', methods=['POST'])
def add():
    data = {
        'familiya': request.form['familiya'],
        'inmya': request.form['inmya'],
        'otchestvo': request.form.get('otchestvo'),
        'Kod_sot': request.form.get('Kod_sot'),
        'Kod_dol': request.form.get('Kod_dol'),
        'Kod_step': request.form.get('Kod_step'),
        'Kod_fac': request.form.get('Kod_fac'),
        'stazh': request.form.get('stazh'),
        'Kod_prin': request.form.get('Kod_prin'),
        'kabinet': request.form.get('kabinet'),
        'Kod_caf': request.form.get('Kod_caf')
    }
    add_sotrudnik(data)
    return redirect(url_for('main.index'))

@bp.route('/delete', methods=['POST'])
def delete():
    sotrudnik_id = request.form['employee_id']
    delete_sotrudnik(sotrudnik_id)
    return redirect(url_for('main.index'))

@bp.route('/update', methods=['POST'])
def update():
    sotrudnik_id = request.form['employee_id']
    data = {
        request.form['field']: request.form['new_value']
    }
    update_sotrudnik(sotrudnik_id, data)
    return redirect(url_for('main.index'))


@bp.route('/view_table', methods=['POST'])
def view_table():
    selected_table = request.form['table']
    print(selected_table)  # отладка
    table_data = get_table_data(selected_table)
    print(table_data)
    return render_template('index.html', sotrudniki=get_all_sotrudniki(), table_data=table_data, selected_table=selected_table)



