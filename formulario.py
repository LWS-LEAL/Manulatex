import streamlit as st
from supabase import create_client
# Conexão com Supabase
url = st.secrets["supabase_url"]
key = st.secrets["supabase_key"]
supabase = create_client(url, key)

st.title("Controle de parada de máquina")

with st.form(key='formulario', clear_on_submit=True):
    nome_mecanico = st.selectbox('Selecione o nome do mecânico:', ['', 'MICHEL', 'UILIMI', 'ANDERSON', 'TALLES', 'DOUGLAS', 'ADILSON', 'TED', 'RICARDO'])

    nome_maquina = st.selectbox('Qual máquina?', ['', 'B-01', 'B-02', 'B-03', 'B-04', 'B-05', 'B-06', 'B-07', 'B-08', 'B-09', 'B-10', 'B-11',
    'B-12', 'B-13', 'B-14', 'B-15', 'B-16', 'B-17', 'B-18', 'B-19', 'B-20', 'B-21', 'B-22'])

    data_parada = st.date_input("Data da parada")
    hora_parada = st.time_input("Hora da parada")

    inicio_conserto = st.date_input("Início do conserto")
    hora_conserto = st.time_input("Hora do conserto")

    termino_conserto = st.date_input("Término do conserto")
    hora_termino_conserto = st.time_input("Hora do término do conserto")

    parada_maquina = st.selectbox('Motivo da parada da maquina:', ['', 'AFIAR FACAS', 'AJUSTE DE FOLGAS', 'AJUSTE DE SINCRONIZAÇÃO', 'AJUSTE DO PASSE DO CARRINHO',
    'AJUSTE MOLDES LATERAIS', 'AJUSTE NA BASE DO ELETRODO', 'AJUSTE SUPORTE DE ELETRODO', 'ALARME DE COLIZÃO ACIONADO', 'AMOLAR FACA', 'ARGOLA CRUZANDO',
    'ARGOLA DESCENDO NA FORMAÇÃO', 'BOBINA TRAVADA', 'CAPTURA DOS SENSORES', 'CENTRALIZAÇÃO DA PINÇA INFERIOR', 'CONTROLE DE SOLDA',
    'EMPILHAMENTO DE MALHA', 'ELETRODO QUEBRADO', 'ENERGIA OSCILANDO', 'FALHA SENSOR ABERTURA DE PORTA', 'FALTA DE ENERGIA', 'LIMAR ELETRODO',
    'LIMPEZA DA MÁQUINA', 'MANUTENÇÃO CORRETIVA', 'MÁQUINA TRAVADA', 'PROBLEMA FORMAÇÃO DE ARGOLA', 'PROBLEMA TORRE DE SOLDA', 'PROBLEMAS DE SENSORES',
    'REGULAGEM DA PINÇA', 'REGULAGEM DE MÁQUINA', 'REGULAGEM DE POUSSOIRS', 'REGULAGEM DO GLISSOIR', 'REGULAGEM TOURELA', 'RETIFICA DE ELETRODO',
    'RETIFICA DE FACA', 'SOLDA RUIM', 'TROCA DE AGULHA', 'TROCA DE BUCHA', 'TROCA DE CHAPAS', 'TROCA DE DEDINHO', 'TROCA DE EIXO', 'TROCA DE ELETRODO',
    'TROCA DE FACA', 'TROCA DE FIO', 'TROCA DE MOLA DO SUPORTE DA PINÇA', 'TROCA DE PROGRAMA',
    'TROCA DE ROLAMENTO', 'TROCA MOLDES LATERAIS', 'TROCA ROLAMENTO DE DISCO', 'NÃO SE APLICA'])

    lista_pecas = ['', '0OUACIJEUP057.56 - APLICADOR DE BOTAO DE PLASTICO EM LUVAS', '1PCDIVEMBO001 - ROLAMENTO DE ROSCA ESQUERDA',
    '0OUT0082M01A - CONJUNTO DE INSTALACAO DE REBITES PECA INFERIOR', '1PCDIVEMBO002 - ROLAMENTO DE ROSCA DIREITA',
    '0OUT0083M01A - CONJUNTO DE INSTALACAO DE REBITES PECA SUPERIOR', '1PCDIVEMBO003 - ROLAMENTO RODOBAL',
    '0OUTPINS.001 - APLICADOR DE BOTAO DE PLASTICO EM LUVAS NOVO', '1PCDIVGALE001 - ROLAMENTO DE DISCO',
    '0PCDIVACCO005 - ACOPLAMENTO EIXO MOTOR DE PASSO 12H7', '1PCDIVLIMD001 - LIMA DIAMANTADA',
    '0PCDIVACCO006 - ACOPLAMENTO EIXO VIS A BILLE 14H7', '1PCDIVLIMI007BR - VALVULA REGULADORA DE FLUXO GRLA1/8-QS8D',
    '0PCDIVCLIN001 - ISOLAMENTO PARA ELETRODO', '1PCDIVLIMI008BR - VALVULA PNEUMATICA - MODELO (AC 5/2X1/8 DUPLO SOL.SIST.M)',
    'OUTRA', 'NÃO SE APLICA']  ##############################

    peca_1 = st.selectbox('Qual peça foi trocada 1?', lista_pecas)
    quantidade_1 = st.number_input("Quantidade 1", min_value=0, step=1)

    peca_2 = st.selectbox('Qual peça foi trocada 2?', lista_pecas)
    quantidade_2 = st.number_input("Quantidade 2", min_value=0, step=1)

    peca_3 = st.selectbox('Qual peça foi trocada 3?', lista_pecas)
    quantidade_3 = st.number_input("Quantidade 3", min_value=0, step=1)

    observacao = st.text_area("Observação")

    enviado = st.form_submit_button('Enviar')

if enviado:
    linha = {
        "NOME DO MECANICO": nome_mecanico,
        "QUAL MAQUINA": nome_maquina,
        "DATA DA PARADA": data_parada.isoformat(),
        "HORA DA PARADA": hora_parada.isoformat(),
        "INICIO DO CONSERTO": inicio_conserto.isoformat(),
        "HORA DO CONSERTO": hora_conserto.isoformat(),
        "TERMINO DO CONSERTO": termino_conserto.isoformat(),
        "HORA DO TERMINO DO CONSERTO": hora_termino_conserto.isoformat(),
        "PARADA DA MAQUINA": parada_maquina,
        "QUAL PECA FOI TROCADA 1": peca_1,
        "QUANTIDADE 1": quantidade_1,
        "QUAL PECA FOI TROCADA 2": peca_2,
        "QUANTIDADE 2": quantidade_2,
        "QUAL PECA FOI TROCADA 3": peca_3,
        "QUANTIDADE 3": quantidade_3,
        "OBSERVACAO": observacao,
    }

    supabase.table("Parada_maquina").insert(linha).execute()
    st.success("Registro salvo com sucesso!")