import streamlit as st
import pandas as pd

# Função para formatar o CNPJ no formato XX.XXX.XXX/0001-XX
def format_cnpj(cnpj):
    cnpj_str = f'{int(cnpj):014d}'  # Garantir que seja uma string de 14 dígitos
    return f'{cnpj_str[:2]}.{cnpj_str[2:5]}.{cnpj_str[5:8]}/{cnpj_str[8:12]}-{cnpj_str[12:14]}'

st.set_page_config(page_title='Database MCMV', layout='wide')

# Ler o arquivo CSV
df = pd.read_csv('mcmv_subsidiado_ogu202404.csv', encoding='ISO-8859-1')
st.title('Análise de Obras por Construtora/Entidade')

# Contar o número de obras para cada construtora/entidade, junto com o CNPJ
obra_por_construtora = df.groupby(['txt_nome_construtora_entidade', 'txt_cnpj_construtora_entidade']).size().reset_index(name='Quantidade de Obras')

# Aplicar a formatação ao CNPJ
obra_por_construtora['txt_cnpj_construtora_entidade'] = obra_por_construtora['txt_cnpj_construtora_entidade'].apply(format_cnpj)

# Exibir o resultado no Streamlit
st.write("Quantidade de Obras por Construtora ou Entidade com CNPJ:")
st.write(obra_por_construtora)

# Ler o arquivo CSV
df = pd.read_csv('mcmv_subsidiado_ogu202404.csv', encoding='ISO-8859-1')
st.title('Análise de Obras por Construtora/Entidade e Região')

# Contar o número de obras para cada construtora/entidade e região, junto com o CNPJ
obra_por_regiao_construtora = df.groupby(['txt_regiao', 'txt_nome_construtora_entidade', 'txt_cnpj_construtora_entidade']).size().reset_index(name='Quantidade de Obras')

# Aplicar a formatação ao CNPJ
obra_por_regiao_construtora['txt_cnpj_construtora_entidade'] = obra_por_regiao_construtora['txt_cnpj_construtora_entidade'].apply(format_cnpj)

# Ordenar as construtoras por região e quantidade de obras (em ordem decrescente)
obra_por_regiao_construtora = obra_por_regiao_construtora.sort_values(by=['txt_regiao', 'Quantidade de Obras'], ascending=[True, False])

# Agrupar por região e pegar os 20 primeiros de cada região
top_20_por_regiao = obra_por_regiao_construtora.groupby('txt_regiao').head(20).reset_index(drop=True)

# Exibir o resultado no Streamlit
st.write("Top 20 Construtoras com mais obras por região:")
st.write(top_20_por_regiao)

# Ler o arquivo CSV
df = pd.read_csv('mcmv_subsidiado_ogu202404.csv', encoding='ISO-8859-1')
st.title('Análise de Obras por Construtora/Entidade e Estado')

# Contar o número de obras para cada construtora/entidade e região, junto com o CNPJ
obra_por_uf_construtora = df.groupby(['txt_sigla_uf', 'txt_nome_construtora_entidade', 'txt_cnpj_construtora_entidade']).size().reset_index(name='Quantidade de Obras')

# Aplicar a formatação ao CNPJ
obra_por_uf_construtora['txt_cnpj_construtora_entidade'] = obra_por_uf_construtora['txt_cnpj_construtora_entidade'].apply(format_cnpj)

# Ordenar as construtoras por região e quantidade de obras (em ordem decrescente)
obra_por_uf_construtora = obra_por_uf_construtora.sort_values(by=['txt_sigla_uf', 'Quantidade de Obras'], ascending=[True, False])

# Agrupar por região e pegar os 20 primeiros de cada região
top_20_por_uf = obra_por_uf_construtora.groupby('txt_sigla_uf').head(20).reset_index(drop=True)

# Exibir o resultado no Streamlit
st.write("Top 20 Construtoras com mais obras por UF:")
st.write(top_20_por_uf)



