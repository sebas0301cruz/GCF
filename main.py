import json
import datetime

# Definir las fechas de subida de las vacantes
fecha_subida_vacante1 = datetime.datetime(2023, 9, 4, 1, 0, 0)
fecha_subida_vacante2 = datetime.datetime(2023, 9, 4, 1, 0, 0)
fecha_subida_vacante3 = datetime.datetime(2023, 9, 4, 1, 0, 0)
fecha_subida_vacante4 = datetime.datetime(2023, 9, 4, 1, 0, 0)
fecha_subida_vacante5 = datetime.datetime(2023, 9, 4, 1, 0, 0)
fecha_subida_vacante6 = datetime.datetime(2023, 9, 4, 1, 0, 0)

# Definir los textos de las vacantes
texto_vacante1 = "👷‍♂️ <b>INGENIERO ES SISTEMAS</b><br>(Aplica hasta el <b>30 de agosto a las 5:00 pm</b>)<br><i><font size='1'>Aplica para todos los sites Medellin Y Bogota</font></i><p></p><div align='justify'> Buscamos estudiante profesional o tecnólogo en sistemas de la computación ingeniero en sistemas o a arreas afines conocimientos configuración en switches (cambios de puerto vlan) manejo de herramientas de monitoreo, redes y soporte técnico a nivel estándar.</div><br><br>🔹 <b>Experiencia</b> 6 meses en Webhelp<br>🔹 <b>Requisición</b> 13984<br><br><b>Aplica a esta convocatoria haciendo</b> <a href='https://forms.office.com/Pages/ResponsePage.aspx?id=fMRoFb4vtE-wfVY7T09XQNAaFPmu-Y5LqhMkytpEWIxUMVdaR1BUWElYUURDMENWS1FDNVlYRkg1Wi4u' target='_blank'><b>clic aquí</b></a> 👈<br><br>___________________________<br><br>"
texto_vacante2 = "👷‍♂️ <b>INGENIERO DE SOFTWARE</b> (Aplica hasta el <b>30 de agosto a las 5:00 pm</b>)<br><i><font size='1'>Aplica para todos los sites Medellin</font></i><p></p><div align='justify'>Buscamos estudiante profesional o tecnólogo en sistemas de la computación ingeniero en sistemas o a arreas afines conocimientos configuración en switches (cambios de puerto vlan) manejo de herramientas de monitoreo, redes y soporte técnico a nivel estándar.</div><br><br>🔹 <b>Experiencia</b> 6 meses en Webhelp<br>🔹 <b>Requisición</b> 13579<br><br><b>Aplica a esta convocatoria haciendo</b> <a href='https://forms.office.com/Pages/ResponsePage.aspx?id=fMRoFb4vtE-wfVY7T09XQNAaFPmu-Y5LqhMkytpEWIxUMVdaR1BUWElYUURDMENWS1FDNVlYRkg1Wi4u' target='_blank'><b>clic aquí</b></a> 👈<br><br>__________________________<br><br>"
texto_vacante3 = "👷‍♂️  <b>INGENIERO INDUSTRIAL</b> (Aplica hasta el <b>30 de agosto a las 5:00 pm</b>)<br><i><font size='1'>Aplica para todos los sites Medellin</font></i><p></p><div align='justify'>Buscamos estudiante profesional o tecnólogo en sistemas de la computación ingeniero en sistemas o a arreas afines conocimientos configuración en switches (cambios de puerto vlan) manejo de herramientas de monitoreo, redes y soporte técnico a nivel estándar.</div><br><br>🔹 <b>Experiencia</b> 6 meses en Webhelp<br>🔹 <b>Requisición</b> 12345<br><br><b>Aplica a esta convocatoria haciendo</b><a href='https://forms.office.com/Pages/ResponsePage.aspx?id=fMRoFb4vtE-wfVY7T09XQNAaFPmu-Y5LqhMkytpEWIxUMVdaR1BUWElYUURDMENWS1FDNVlYRkg1Wi4u' target='_blank'><b>clic aquí</b></a> 👈<br><br>__________________________<br><br>"
texto_vacante4 = "👷‍♂️  <b>INGENIERO AEREONAUTICO</b> (Aplica hasta el <b>30 de agosto a las 5:00 pm</b>)<br><i><font size='1'>Aplica para todos los sites Medellin</font></i><p></p><div align='justify'>Buscamos estudiante profesional o tecnólogo en sistemas de la computación ingeniero en sistemas o a arreas afines conocimientos configuración en switches (cambios de puerto vlan) manejo de herramientas de monitoreo, redes y soporte técnico a nivel estándar.</div><br><br>🔹 <b>Experiencia</b> 6 meses en Webhelp<br>🔹 <b>Requisición</b> 09876<br><br><b>Aplica a esta convocatoria haciendo</b><a href='https://forms.office.com/Pages/ResponsePage.aspx?id=fMRoFb4vtE-wfVY7T09XQNAaFPmu-Y5LqhMkytpEWIxUMVdaR1BUWElYUURDMENWS1FDNVlYRkg1Wi4u' target='_blank'><b>clic aquí</b></a> 👈<br><br>___________________________<br><br>"
texto_vacante5 = "👷‍♂️  <b>CHEFCITO</b> (Aplica hasta el <b>4 de septiembre a las 5:00 pm</b>)<br><i><font size='1'>Aplica para todos los sites Medellin</font></i><p></p><div align='justify'>Buscamos estudiante profesional o tecnólogo en gastronomia molecular con experiencia en suchi pulpo y ramen.</div><br><br>🔹 <b>Experiencia</b> 6 meses en Webhelp<br>🔹 <b>Requisición</b> 12345<br><br><b>Aplica a esta convocatoria haciendo</b><a href='https://forms.office.com/Pages/ResponsePage.aspx?id=fMRoFb4vtE-wfVY7T09XQNAaFPmu-Y5LqhMkytpEWIxUMVdaR1BUWElYUURDMENWS1FDNVlYRkg1Wi4u' target='_blank'><b>clic aquí</b></a> 👈<br><br>___________________________<br><br>"
texto_vacante6 = "👷‍♂️  <b>CHEFCITO</b> (Aplica hasta el <b>4 de septiembre a las 5:00 pm</b>)<br><i><font size='1'>Aplica para todos los sites Medellin</font></i><p></p><div align='justify'>Buscamos estudiante profesional o tecnólogo en gastronomia molecular con experiencia en suchi pulpo y ramen.</div><br><br>🔹 <b>Experiencia</b> 6 meses en Webhelp<br>🔹 <b>Requisición</b> 12345<br><br><b>Aplica a esta convocatoria haciendo</b><a href='https://forms.office.com/Pages/ResponsePage.aspx?id=fMRoFb4vtE-wfVY7T09XQNAaFPmu-Y5LqhMkytpEWIxUMVdaR1BUWElYUURDMENWS1FDNVlYRkg1Wi4u' target='_blank'><b>clic aquí</b></a> 👈<br><br>___________________________<br><br>"

# Número de días que las vacantes estarán disponibles
dias_vigencia3 = 3  # LUNES MARTES MIERCOLES
dias_vigencia4 = 5  # JUEVES VIERNES


def consult_vacantes(request):
    request_json = request.get_json()

    if request_json and 'fulfillmentInfo' in request_json:
        fulfillment_info = request_json['fulfillmentInfo']
        tag = fulfillment_info.get('tag')

        if tag == 'consultar_vacantes':
            now = datetime.datetime.now()
            response_messages = []

            if now < fecha_subida_vacante1 + datetime.timedelta(days=dias_vigencia3):
                response_messages.append(texto_vacante1)
            if now < fecha_subida_vacante2 + datetime.timedelta(days=dias_vigencia3):
                response_messages.append(texto_vacante2)
            if now < fecha_subida_vacante3 + datetime.timedelta(days=dias_vigencia3):
                response_messages.append(texto_vacante3)
            if now < fecha_subida_vacante4 + datetime.timedelta(days=dias_vigencia3):
                response_messages.append(texto_vacante4)
            if now < fecha_subida_vacante5 + datetime.timedelta(days=dias_vigencia3):
                response_messages.append(texto_vacante5)
            if now < fecha_subida_vacante6 + datetime.timedelta(days=dias_vigencia3):
                response_messages.append(texto_vacante6)

            # Dos <p></p> entre los textos
            combined_text = "<p></p><p></p>".join(response_messages)

            if combined_text:
                fulfillment_response = {
                    'messages': [{'text': {'text': [combined_text]}}],
                }
            else:
                fulfillment_response = {
                    'messages': [{'text': {'text': ['En estos momentos no hay vacantes disponibles.']}}],
                }
        else:
            fulfillment_response = {
                'messages': [{'text': {'text': ['Etiqueta no reconocida.']}}],
            }
    else:
        fulfillment_response = {
            'messages': [{'text': {'text': ['No se detectó una consulta válida.']}}],
        }

    return json.dumps({"fulfillmentResponse": fulfillment_response})
