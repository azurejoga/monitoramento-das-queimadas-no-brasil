# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98735973-1f35-35d3-b814-28f9c79088d4 | -16.57459 | -51.62855 | 2026-08-23 05:06:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 767accfd-4c2f-3f06-a585-a2ad02af8b26 | -16.04882 | -50.44141 | 2026-08-23 05:06:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0f62a0b9-2b0e-30b4-b772-feec7f8f3567 | -14.96399 | -52.66471 | 2026-08-23 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 30574a4e-4380-3af8-9b23-ef116b76715d | -11.74027 | -54.80101 | 2026-08-23 05:06:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1e07902-d43d-3dec-a4a1-fc884835ef4f | -13.93823 | -45.35271 | 2026-08-23 05:06:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93a6f7ea-8e55-37a3-9944-5b2cf1a4f9e9 | -12.73734 | -48.39165 | 2026-08-23 05:06:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 137efd98-41f0-3a4a-af42-5e9782208149 | -14.99291 | -52.68888 | 2026-08-23 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7d1bc4f9-6500-3732-96e5-14a2c76ad4ab | -13.44015 | -57.08204 | 2026-08-23 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f97a0c6-b8e1-3155-9a07-5e97b7c0ec08 | -14.30739 | -53.23377 | 2026-08-23 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b44705ec-d5f8-3975-a698-8e796c14145c | -13.89439 | -53.99933 | 2026-08-23 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7422ab15-20e5-3e9f-9131-461b3c25a0ed | -15.24515 | -52.86041 | 2026-08-23 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7571a30c-3a15-3ab6-b814-9e83a6e591c3 | -13.41607 | -57.0187 | 2026-08-23 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9271c2d4-bc93-382a-9f1b-04d6ddb371e1 | -11.6812 | -54.58678 | 2026-08-23 05:06:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7cc3bfd-70ab-3ee1-8b54-b1e06ba27277 | -16.39832 | -51.33286 | 2026-08-23 05:06:00 | NOAA-20 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b729aa3-9c17-39f1-89e2-d0bb99d3eea4 | -12.84418 | -48.46632 | 2026-08-23 05:06:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2bebf253-1ab1-3aa5-93b3-9a30d150ca3d | -14.54171 | -53.05907 | 2026-08-23 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7984776e-97e7-3b9f-ba82-26686b93685f | -12.73651 | -48.39794 | 2026-08-23 05:06:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| aef50f69-5f87-3f6f-90db-7c3b6cfb8fa6 | -15.25313 | -52.85717 | 2026-08-23 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6a950d4-e53d-372a-8e19-a484a3791b2d | -13.18505 | -51.4462 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c59d907b-bdec-3fbf-9e44-7328706b7763 | -13.17161 | -51.42898 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68519f0a-5f84-3a14-9429-eaba8a471fdb | -14.36153 | -51.77697 | 2026-08-23 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8b021e1-1949-36bb-a27f-ec93a2a7f43b | -15.72593 | -56.01403 | 2026-08-23 05:06:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 5b05d660-b8c0-34a7-8f77-117072f3a173 | -12.74945 | -48.40906 | 2026-08-23 05:06:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f4851ee7-684d-3e40-b3be-3853a8ece9fe | -15.73197 | -56.04084 | 2026-08-23 05:06:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 75af439a-c043-3094-90a2-46cc015ed695 | -15.49735 | -57.92315 | 2026-08-23 05:06:00 | NOAA-20 | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10d6ef6d-a234-353b-bf69-846b8af5c45a | -13.68335 | -51.84876 | 2026-08-23 05:06:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4f59f1b7-f367-320c-b7ad-605891df7784 | -13.15675 | -51.42172 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8b4e380c-bd67-3945-b96b-71d9326443d4 | -18.66171 | -48.18261 | 2026-08-23 05:06:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7e3c2160-ad01-3b83-8edc-899862fb8ccc | -14.50929 | -59.81973 | 2026-08-23 05:06:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d5b10632-f908-3c4e-91a3-756f7cd90182 | -12.01869 | -55.342 | 2026-08-23 05:06:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f475b106-746c-31f6-8995-788dfb40845b | -12.84302 | -48.47512 | 2026-08-23 05:06:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6097ecb5-b2db-3c57-86b7-2e1c83da039f | -15.3146 | -53.80035 | 2026-08-23 05:06:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e57f11bc-c452-336c-97cb-88173c098f71 | -13.25922 | -51.60025 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8bf25bf8-a807-3825-9648-212dc2fbc1ae | -12.59356 | -47.8912 | 2026-08-23 05:06:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f5952b6-9a0d-3fd5-8bf3-7d0df16a4a54 | -15.68303 | -56.17993 | 2026-08-23 05:06:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1dbc96b1-3675-36e1-b19a-85a26bdb5437 | -12.93623 | -56.62209 | 2026-08-23 05:06:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| edaaa898-69b6-3cca-b17d-8b74e5e492f0 | -13.43329 | -43.85776 | 2026-08-23 05:06:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 71f0e28c-f542-3475-9b5e-bc795569d1de | -13.17301 | -51.41901 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 86ff398e-25c9-399e-8076-c3493cb0048d | -15.39646 | -59.50522 | 2026-08-23 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1feb94cb-4c24-359c-9e96-280b63face6f | -15.75954 | -55.55238 | 2026-08-23 05:06:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55b0a6e2-0c92-3618-bc89-0a1a8c9a75ab | -18.52189 | -47.15883 | 2026-08-23 05:06:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 73ac096c-2846-36a7-8f82-5728e7c49ca1 | -17.88553 | -51.67094 | 2026-08-23 05:06:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03a5fb13-958d-327f-a7fb-16ebbaf7fd78 | -16.30954 | -53.18764 | 2026-08-23 05:06:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b4838613-b609-3c2d-a92b-1a6c75ab9ac6 | -17.6203 | -51.06213 | 2026-08-23 05:06:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7be91ad-2170-3593-92b0-5df18a561411 | -15.63651 | -56.0433 | 2026-08-23 05:06:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| ed1327ac-9be3-3ec9-9b02-5415792e3bb6 | -14.96094 | -52.65967 | 2026-08-23 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 324ebeab-0951-363b-8a21-a0afc2e0c5c9 | -16.40599 | -51.84238 | 2026-08-23 05:06:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9aabcd24-3240-3642-9de7-5e6038880b6b | -12.00527 | -53.41901 | 2026-08-23 05:06:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37c7ee0c-3c07-36e6-a5e5-0c7edc7758f5 | -16.57058 | -51.62793 | 2026-08-23 05:06:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4d9ca2e-6d61-3272-a328-0ed9356a65f4 | -14.96157 | -52.65523 | 2026-08-23 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 01bbdee5-fd00-359d-87fc-122b505b4ccf | -14.50814 | -59.82214 | 2026-08-23 05:06:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b37ff049-51b0-3ad2-b01f-d573b2cca32f | -14.95851 | -52.65018 | 2026-08-23 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5dd5dcb5-1564-30b4-ab7a-b9aa601d1b48 | -17.64316 | -50.48956 | 2026-08-23 05:06:00 | NOAA-20 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21c7a314-b9b0-3aa9-85a4-d0ecde6a85b9 | -13.16702 | -51.4334 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| df950b8e-f135-386e-9a48-fa7666881403 | -13.19247 | -51.42184 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c5ea3129-0796-391c-ad5a-244bf4b62018 | -14.39676 | -51.78963 | 2026-08-23 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22b59a3d-ab10-3790-b476-5aec0f7087fc | -12.74887 | -48.41343 | 2026-08-23 05:06:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b527c11d-93bb-3a7f-8a46-c150c101d593 | -14.97446 | -52.67091 | 2026-08-23 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9427a427-debd-350d-b54e-6539e46090a9 | -12.95503 | -56.63258 | 2026-08-23 05:06:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a3d43b7-d51f-3939-8267-2dc389954c26 | -14.31608 | -53.32401 | 2026-08-23 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4fd5df42-acae-3e31-9d0e-947233e6d597 | -13.20344 | -51.42854 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce507d30-3f28-3be0-8ddb-110e31dd6048 | -13.18398 | -51.4257 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| df1389e3-be56-31ad-96f0-556d605b3c87 | -15.5127 | -49.83398 | 2026-08-23 05:06:00 | NOAA-20 | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0027894-676d-370b-b946-8fc34732812d | -13.1762 | -51.42456 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| feeed594-f4ad-3f95-bd9c-71e8f5343c7b | -12.94013 | -56.61909 | 2026-08-23 05:06:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f39700a3-0f31-3922-bbcf-450c9182654a | -14.4892 | -51.81514 | 2026-08-23 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64584b74-2916-3c6a-ac54-4d41d077852c | -14.40063 | -51.79019 | 2026-08-23 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdbaa26a-2c5e-39c8-996f-aa6f605aad0a | -12.84889 | -48.46695 | 2026-08-23 05:06:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 753ba227-5046-31ca-80b3-1f575885670a | -14.56462 | -53.05387 | 2026-08-23 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5026b77e-4b5e-3656-9eab-2171cf6d9685 | -15.76289 | -55.55294 | 2026-08-23 05:06:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15c7b519-e109-3f02-9a9f-bb34015bde4a | -14.49514 | -59.83632 | 2026-08-23 05:06:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48780104-6671-3982-aac3-6a600805a44a | -14.99599 | -52.69384 | 2026-08-23 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7d94186b-19b7-346f-b8f3-b2d3253d72a1 | -17.74784 | -47.03521 | 2026-08-23 05:06:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1a639b22-97fa-35ca-b72a-9236792cb551 | -16.27864 | -57.66474 | 2026-08-23 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| dc25d4cb-8544-3cf6-998b-93bbf3bf3dd2 | -16.02166 | -58.18993 | 2026-08-23 05:06:00 | NOAA-20 | GLÓRIA D'OESTE | MATO GROSSO | Brasil | 5103957 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| c68867d7-390a-30e0-9fae-50ed88bfc9aa | -17.74825 | -47.03121 | 2026-08-23 05:06:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 675f217b-414c-346e-8e99-a48718ebe449 | -14.50328 | -59.83284 | 2026-08-23 05:06:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e07455d-67fe-30ea-b83d-656a603d8cb9 | -16.40215 | -51.85054 | 2026-08-23 05:06:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a0a59fc7-6a14-3566-8017-1e994f2037d0 | -14.34605 | -51.7747 | 2026-08-23 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| af2609e6-721a-356b-b8b1-9ad706f09df8 | -15.76424 | -49.9694 | 2026-08-23 05:06:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 600d5a30-f382-3d4f-bbc8-ab976c9fb226 | -13.84272 | -54.0149 | 2026-08-23 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 448e9603-f1de-3365-92ac-c4e8cecc159d | -16.3097 | -53.16045 | 2026-08-23 05:06:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 826e4a4f-a9ad-3fb0-b184-fea76785e15a | -13.19637 | -51.42241 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2804b703-53e2-36c7-a76f-e1b33fae1227 | -18.53257 | -47.16388 | 2026-08-23 05:06:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec37d10f-7752-338c-83cc-826a1bbb8c8b | -17.21258 | -47.52627 | 2026-08-23 05:06:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3df56fd0-9578-3a9f-a7bc-c64c2bf8fb21 | -13.44073 | -57.07843 | 2026-08-23 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8dcb9e9c-487b-34c7-a3d9-483c72f64375 | -16.40283 | -51.84562 | 2026-08-23 05:06:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 70558530-f6c8-347d-b2d2-e31762153458 | -15.33877 | -52.77726 | 2026-08-23 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 820358f3-de62-371c-8231-ae06bbbe2c52 | -14.37423 | -51.78127 | 2026-08-23 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5f81e1d9-a388-31d0-9eb0-5a451f745eb7 | -14.35876 | -51.77899 | 2026-08-23 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 738eefec-a081-3293-a4a4-5031cb1ab613 | -15.6433 | -55.95602 | 2026-08-23 05:06:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb05a42d-07d4-385e-8808-13debf515ba6 | -10.55609 | -61.46088 | 2026-08-23 05:06:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d397ff4-3b28-38d3-8f0b-bdc7cc7e5905 | -14.49826 | -59.81802 | 2026-08-23 05:06:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec03e19b-e721-3077-bbda-6090a772864e | -14.49881 | -59.83693 | 2026-08-23 05:06:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ded3113e-2e4e-35af-9b8c-4c0cecc16321 | -12.94678 | -56.6202 | 2026-08-23 05:06:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84ddf47b-6e68-3584-8ae4-1c26f54f1a34 | -12.75892 | -48.41012 | 2026-08-23 05:06:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f93de685-198c-3aa5-9c61-4ab2b68fe76c | -13.23489 | -51.4351 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9bfefd89-ec23-30ab-af2d-ac357d6e7d59 | -15.51717 | -49.83449 | 2026-08-23 05:06:00 | NOAA-20 | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd3060aa-cbac-3f2d-be83-c23c7a792097 | -13.18116 | -51.44563 | 2026-08-23 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 97114bf1-2d71-3277-906e-05d84ac61508 | -16.44995 | -54.67839 | 2026-08-23 05:06:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README59.md)
