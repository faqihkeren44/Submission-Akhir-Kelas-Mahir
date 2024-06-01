import pickle
import streamlit as st
import pandas as pd

# Membaca model
with open("model3.pkl", "rb") as model_file:
    model_load = pickle.load(model_file)

# Tombol prediksi
kolom_data = ['Marital_status', 'Displaced', 'Debtor', 'Tuition_fees_up_to_date',
              'Gender', 'Scholarship_holder', 'Age_at_enrollment',
              'Curricular_units_1st_sem_credited', 'Curricular_units_1st_sem_enrolled',
              'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade',
              'Curricular_units_2nd_sem_credited', 'Curricular_units_2nd_sem_enrolled',
              'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade']

def yesno_convert(option):
    if (option == 'Yes'):
        option = int('1')
        return option
    else:
        option = int('0')
        return option
        
def gender_convert(option):
    if (option == 'Man'):
        option = int('1')
        return option
    else:
        option = int('0')
        return option
        
def marital_convert(option):
    if (option == 'Single'):
        option = int('1')
        return option
    elif (option == 'Married'):
        option = int('2')
        return option
    elif(option == 'Widower'):
        option = int('3')
        return option
    elif(option == 'Divorced'):
        option = int('4')
        return option
    elif(option == 'Facto Union'):
        option = int('5')
        return option
    else:
        option = int('6')
        return option

with st.sidebar:
    st.header('Predict Machine', divider='rainbow')

    st.subheader('Gender')
    Gender = gender_convert(st.radio('Pilih jenis kelamin', ['Man', 'Woman'],
                                     horizontal=True, label_visibility='collapsed'))
    st.subheader('Marital Status')
    Marital_status = marital_convert(st.selectbox('Pilih status pernikahan',
                                                  ['Single', 'Married', 'Widower', 'Divorced',
                                                   'Factco Union', 'Legally Separated'],
                                                   label_visibility='collapsed'))
    st.subheader('Age At Enrollment')
    Age_at_enrollment = st.slider('Umur saat enrollment', 10, 100, label_visibility='collapsed')

    st.subheader('Debtor')
    Debtor = yesno_convert(st.radio('Debtor', ['Yes', 'No'], horizontal=True,
                                    label_visibility='collapsed'))
    st.subheader('Tuition Fees')
    Tuition_fees_up_to_date = yesno_convert(st.radio('Tuition Fees Up To Date',
                                                     ['Yes', 'No'], horizontal=True,
                                                     label_visibility='collapsed'))
    st.subheader('Scholarship Holder')
    Scholarship_holder = yesno_convert(st.radio('Scholarship Holder', ['Yes', 'No'],
                                                horizontal=True, label_visibility='collapsed'))
    st.subheader('Displaced')
    Displaced = yesno_convert(st.radio('Displaced', ['Yes', 'No'], horizontal=True,
                                       label_visibility='collapsed'))

    st.subheader('Curriculum Unit Credited')
    col1, col2 = st.columns(2)
    with col1:
        Curricular_units_1st_sem_credited = st.number_input('1st Semester Credited')
    with col2:
        Curricular_units_2nd_sem_credited = st.number_input('2nd Semester Credited')
    
    st.subheader('Curriculum Unit Enrolled')
    col1, col2 = st.columns(2)
    with col1:
        Curricular_units_1st_sem_enrolled = st.number_input('1st Semester Enrolled')
    with col2:
        Curricular_units_2nd_sem_enrolled = st.number_input('2nd Semester Enrolled')

    st.subheader('Curriculum Unit Approved')
    col1, col2 = st.columns(2)
    with col1:
        Curricular_units_1st_sem_approved = st.number_input('1st Semester Approved')
    with col2:
        Curricular_units_2nd_sem_approved = st.number_input('2nd Semester Approved')

    st.subheader('Curriculum Unit Grade')
    col1, col2 = st.columns(2)
    with col1:
        Curricular_units_1st_sem_grade = st.number_input('1st Semester Grade')
    with col2:
        Curricular_units_2nd_sem_grade = st.number_input('2nd Semester Grade')

    new_data = [[Marital_status, Displaced, Debtor,
             Tuition_fees_up_to_date, Gender, Scholarship_holder, Age_at_enrollment,
             Curricular_units_1st_sem_credited, Curricular_units_2nd_sem_credited,
             Curricular_units_1st_sem_enrolled, Curricular_units_2nd_sem_enrolled,
             Curricular_units_1st_sem_approved, Curricular_units_2nd_sem_approved,
             Curricular_units_1st_sem_grade, Curricular_units_2nd_sem_grade]]
    
    if st.sidebar.button('Predict'):
        new_data = pd.DataFrame(new_data, columns=kolom_data)
        result = model_load.predict(new_data)
        if(result[0] == 0):
            st.success('Siswa tidak dropout')
            st.balloons()
        else:
            st.error('Siswa dropout')

# Judul web
st.title('Jaya Jaya Institut')
st.subheader('Apa itu Jaya Jaya Institut?',  divider='grey')
st.markdown('''Jaya Jaya Institut merupakan pendidikan perguruan internasional yang
            sudah menarik perhatian berbagai kalangan siswa, bahkan dari mancanegara.
            Institut ini sudah berdiri sejak tahun 2000. Dengan tawaran beasiswa yang''')
st.subheader('Apa fungsi Predict Machine di samping?',  divider='grey')
st.markdown('''Predict Machnine adalah sebuah mesin model yang dibuat untuk kebutuhan
            prediksi. Mesin ini dibuat dan dilatih berdasarkan data yang ada pada
            Jaya Jaya Institute.''')
st.subheader('Bagaimana cara menggunakan Predict Machine?',  divider='grey')
st.markdown('''Untuk menampilkan mesin model klik tombol panah (>) di pojok kiri atas
            halaman. Pada tampilannya, ada beberapa inputan yang harus diisi, yaitu:''')
st.text('Gender: Jenis kelamin siswa (Man = Pria, Woman = Wanita)')
st.text('Marital Status: Status pernikahan (Single = Belum menikah, Married = Menikah, Widower = Janda/Duda, Divorced = Cerai, Facto Union = Pernikahan tidak resmi, Legally Separated = Perceraian resmi)')
st.text('Age At Enrollment: Usia siswa saat melakukan enrollment')
st.text('Debtor: Apakah siswa memiliki tanggungan hutang?')
st.text('Tuition Fees: Apakah siswa sudah melunasi pembayaran terkini?')
st.text('Scholarship Holder: Apakah siswa mendapatkan beasiswa?')
st.text('Displaced: Apakah siswa berasal dari keluarga kurang mampu?')
st.text('Curriculum Unit: Jumlah Curriculum yang dikreditkan, dienrollment, disetujui, dan nilainya. Baik pada semester 1 maupun semester 2')