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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ad6a110-cf10-34e4-8eb1-8080bea621a4 | -12.49801 | -46.92289 | 2025-07-17 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b83f77b0-fe61-3aa6-bebb-045622cb4949 | -12.49666 | -46.92927 | 2025-07-17 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44e7c24e-0ce9-3556-a285-8b7ce39e145b | -12.49776 | -46.92341 | 2025-07-17 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19f5a593-a909-3735-aaa6-cba5d186b024 | -13.00401 | -44.86928 | 2025-07-17 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7b58df8-16a8-333f-93ee-d8559f9e9454 | -12.48568 | -46.91339 | 2025-07-17 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 29c2103b-c5ab-3520-90fc-333ab8c477d9 | -12.70814 | -46.8061 | 2025-07-17 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82ff5d6e-7a30-3f95-bead-20d8688ddcd8 | -17.16048 | -46.117 | 2025-07-17 03:34:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d5ea8724-114d-3495-a734-9c72924f1114 | -18.85067 | -45.20579 | 2025-07-17 03:34:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c22088b2-f48e-3b65-8f6a-5d710e33c8ae | -12.47883 | -46.91192 | 2025-07-17 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d0dc7cd4-b763-3de2-ad2e-9871bff25968 | -14.51993 | -47.67653 | 2025-07-17 03:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8d69e5c4-433b-3a64-8c91-76580f637f38 | -12.48431 | -46.91988 | 2025-07-17 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8145765e-f5b4-310b-a917-e188124a459f | -13.00218 | -44.87823 | 2025-07-17 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 545ce423-57c6-363b-9246-cac6e6bf054f | -12.49231 | -46.9155 | 2025-07-17 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96ba68ae-859e-361e-8df1-2a7a789bf700 | -12.48245 | -44.50279 | 2025-07-17 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aac2c664-060c-3801-87b1-a0cb2aff08a6 | -19.74511 | -40.69296 | 2025-07-17 03:34:00 | NPP-375D | SÃO ROQUE DO CANAÃ | ESPÍRITO SANTO | Brasil | 3204955 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e3cceed7-959b-34c1-b5f1-a2810d6e7452 | -14.25123 | -42.84511 | 2025-07-17 03:34:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| cd9d7d47-c0b3-3b53-ae16-b02b51e9ae92 | -12.99716 | -44.87203 | 2025-07-17 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7f8d957-31f8-353b-ba51-0c9f2a8d57b1 | -14.25187 | -42.84189 | 2025-07-17 03:34:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d8e746c5-8ec4-316b-ac5a-025e4e006859 | -12.47651 | -44.50153 | 2025-07-17 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 050b7acf-f9ad-386d-946e-1f56fb2bb262 | -12.47747 | -46.91837 | 2025-07-17 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3a43d430-56ed-342d-a853-be0a65624b78 | -19.74927 | -40.69344 | 2025-07-17 03:34:00 | NPP-375D | SÃO ROQUE DO CANAÃ | ESPÍRITO SANTO | Brasil | 3204955 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 56d75e1a-b756-3a7b-a963-e2a3afe4106e | -12.99296 | -44.8618 | 2025-07-17 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6e107e6-19f7-3a6f-a4c3-c0d52de46d01 | -14.51354 | -47.67712 | 2025-07-17 03:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 940137e7-da30-3913-87c8-c0bd0d423fbc | -19.53927 | -49.67644 | 2025-07-17 03:36:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c9c75590-23b1-3726-8d12-e1e1f372c4cb | -19.44828 | -48.54673 | 2025-07-17 03:36:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aace66b5-afee-312c-ad12-792c82147e42 | -20.01024 | -49.05298 | 2025-07-17 03:36:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b366e90d-2540-3c5f-98f0-1cb73d799b2b | -19.47523 | -49.29552 | 2025-07-17 03:36:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 19b7e12f-ac63-3f66-ac4d-29105287d9b9 | -20.99674 | -49.76637 | 2025-07-17 03:36:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 05c2be02-aa65-3d58-86d4-1b30d013de0b | -20.99509 | -49.77309 | 2025-07-17 03:36:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| e4807c17-31ad-39fc-a4e0-eb02c09a7da8 | -19.53756 | -49.68333 | 2025-07-17 03:36:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8640c943-0f23-3874-9c6c-6aa9192cb4f2 | -19.44691 | -48.53768 | 2025-07-17 03:36:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f9d602fd-883e-3f7c-9a9b-57def5a66b7b | -20.01182 | -49.04655 | 2025-07-17 03:36:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fe79f9f-e7e6-382a-959d-c0a23ad0e4f8 | -20.98832 | -49.771 | 2025-07-17 03:36:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 7ec62586-073e-3e52-8082-5b8442c48ec6 | -19.47687 | -49.28873 | 2025-07-17 03:36:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e786c472-7de5-3650-b501-81d7979e46b2 | -20.99338 | -49.78003 | 2025-07-17 03:36:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| f5b5dba8-c6a5-3262-b5fd-f0733bfbaf06 | -19.48208 | -49.29735 | 2025-07-17 03:36:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8fcf685b-a4de-3d6b-9c1c-c0b93906e9c6 | -19.54097 | -49.68584 | 2025-07-17 03:36:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1383d0a5-e233-3221-8480-589243e0e992 | -19.54261 | -49.67904 | 2025-07-17 03:36:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a25d0658-9364-360b-87a4-9744ad2c5e40 | -21.27729 | -44.51139 | 2025-07-17 03:36:00 | NPP-375D | NAZARENO | MINAS GERAIS | Brasil | 3144508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| eef3266d-3611-3463-a87d-6d24b6cf896f | -19.95939 | -48.99094 | 2025-07-17 03:36:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac66db73-23ec-397b-a540-e50be0da524b | -19.44991 | -48.54002 | 2025-07-17 03:36:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1eb9f6bb-4776-3c21-8974-b0cff87b049d | -19.47616 | -49.28775 | 2025-07-17 03:36:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1dc1c400-d1fa-3826-8c63-b836954728c3 | -20.00881 | -49.05196 | 2025-07-17 03:36:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fe6e5386-6dc1-3d67-a24c-c715802870d4 | -21.08297 | -48.68711 | 2025-07-17 03:36:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8893be3a-78bf-30fa-98fd-c74134109a37 | -19.47447 | -49.29455 | 2025-07-17 03:36:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e4d4ebb4-32ef-38fe-a11d-e0976a404201 | -21.08152 | -48.69323 | 2025-07-17 03:36:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bea5ade3-d5ac-348d-815e-8974738382fc | -19.48132 | -49.29638 | 2025-07-17 03:36:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c7f8cc47-d920-3d43-96bd-c40736fa328c | -19.44349 | -48.5376 | 2025-07-17 03:36:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75b52b23-3f41-3479-974c-bc4612577d20 | -19.44529 | -48.54455 | 2025-07-17 03:36:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62a8c946-e590-392f-bfc1-f2e7513ad960 | -19.54451 | -49.68535 | 2025-07-17 03:36:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8f79fc6a-407e-3c95-b777-ab74ab486ead | -20.98998 | -49.76428 | 2025-07-17 03:36:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| de743a59-9c1a-33ba-aaa1-4dfbc6895c7d | -19.53568 | -49.67694 | 2025-07-17 03:36:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 73862c1a-1a57-3f8b-9170-a564d878e930 | -20.98838 | -49.76573 | 2025-07-17 03:36:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| aff18d82-0f76-3f7f-9a76-1dfec1edf8f2 | -23.25424 | -45.58017 | 2025-07-17 03:36:00 | NPP-375D | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a17a4f71-3ea4-32a7-9586-5124f32c0b61 | -22.55243 | -44.12614 | 2025-07-17 03:36:00 | NPP-375D | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 42fb484b-090b-3d0b-b79f-0ff985be2678 | -22.39725 | -49.79747 | 2025-07-17 03:36:00 | NPP-375D | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3a16c6fc-fe31-3a3e-9ac3-cf7709e58314 | -22.39051 | -49.796 | 2025-07-17 03:36:00 | NPP-375D | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e552bc60-3d26-32f6-a231-150431d7e14e | -23.51793 | -47.01744 | 2025-07-17 03:36:00 | NPP-375D | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7da59640-37ab-3f38-ba36-5a50d3229db1 | -20.99344 | -49.77454 | 2025-07-17 03:36:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 371fc34a-e41d-3bd0-87e7-3f11d2babc1f | -22.69676 | -43.34982 | 2025-07-17 03:36:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dbbfa376-f710-36e9-a8f2-d8be8a9ce83f | -20.99516 | -49.76777 | 2025-07-17 03:36:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| ed13ea4a-45c5-32d3-8332-6fb6f62cb8d4 | -23.23036 | -46.40427 | 2025-07-17 03:36:00 | NPP-375D | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1007c5a8-c861-36c9-816f-e27776b76d0d | -23.08563 | -49.7338 | 2025-07-17 03:36:00 | NPP-375D | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 1a42b985-0746-3a56-8673-8243d408f1d3 | -23.51696 | -47.02158 | 2025-07-17 03:36:00 | NPP-375D | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 97f8086b-31e0-31f2-8e03-70e38fef701a | -22.39332 | -49.79401 | 2025-07-17 03:36:00 | NPP-375D | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b5e7ec23-0820-3e96-9f1d-04ef6c47a41b | -23.25351 | -45.58347 | 2025-07-17 03:36:00 | NPP-375D | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| e2ecf7e8-c14d-3251-8615-a685e5f7ab7f | -23.52076 | -47.01971 | 2025-07-17 03:36:00 | NPP-375D | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e466a39b-ca5f-3823-8ed9-463cbd56dd9a | -23.51524 | -47.01794 | 2025-07-17 03:36:00 | NPP-375D | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 884f9512-f116-3bdf-a67f-9b5e05e4026b | -23.15206 | -46.24421 | 2025-07-17 03:36:00 | NPP-375D | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2380e3cb-a316-395d-b510-1b7a11c135d0 | -22.6983 | -43.34865 | 2025-07-17 03:36:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ef22cd16-14b5-3efb-a58b-4ccc5f9d9af0 | -22.10468 | -45.13702 | 2025-07-17 03:36:00 | NPP-375D | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 34918f47-5775-3456-946a-38bdbcf62ee9 | -23.23043 | -46.40297 | 2025-07-17 03:36:00 | NPP-375D | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d97846ca-71b2-3436-879a-fc7a953ce56b | -23.15741 | -46.24574 | 2025-07-17 03:36:00 | NPP-375D | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cf1b8c86-ab0d-3c16-b055-352a326131d4 | -27.21189 | -50.66264 | 2025-07-17 03:38:00 | NPP-375D | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 78b39a6e-f753-39c3-9bcf-bf806a5e19f8 | -25.1144 | -49.18825 | 2025-07-17 03:38:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4f47a82f-9cf6-32f1-8dd3-c218532ab74b | -25.11592 | -49.18214 | 2025-07-17 03:38:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5bac3a65-963b-305d-aa4b-73a3a40399da | -5.6754 | -43.7147 | 2025-07-17 03:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 195.7 |
| 48e8de17-5a93-32fa-8568-5ad1fc43e095 | -6.7194 | -44.3231 | 2025-07-17 03:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| c4b35ea7-2ae6-3fea-a8b2-912ed6599318 | -9.2449 | -48.5546 | 2025-07-17 03:40:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 1dd0b775-a1be-346f-9a26-f76108b403bd | -3.3958 | -47.4785 | 2025-07-17 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 7058f0e5-7ace-35fa-936d-095c621342ab | -5.6565 | -43.7393 | 2025-07-17 03:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 700f5886-c1cc-351d-9dfb-f2ee92225897 | -5.6567 | -43.7161 | 2025-07-17 03:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 274.6 |
| 79ccbdfa-4b1f-3a49-bf17-765df1b5db1c | -5.6752 | -43.7379 | 2025-07-17 03:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 6845ed4e-c520-3141-a1a7-a54ba2c80181 | -3.3772 | -47.4792 | 2025-07-17 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 5862612f-5124-3adb-be7e-b6350c77ef6f | -5.6569 | -43.6929 | 2025-07-17 03:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 386ad9fb-65db-39a4-aa40-cf8ef8b6bc9e | -5.6754 | -43.7147 | 2025-07-17 03:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 1ead276d-5bf2-3dbb-b9d8-ae5a657a89f1 | -3.3958 | -47.4785 | 2025-07-17 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 49f95f16-1ed6-3762-8f48-b1fb750eac91 | -5.6567 | -43.7161 | 2025-07-17 03:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 376.4 |
| 8bccfe68-f2b8-37f3-97fe-5ccc128a7c7d | -6.7194 | -44.3231 | 2025-07-17 03:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 19709745-16dc-3a8e-a115-e61e7bbc16ae | -5.6569 | -43.6929 | 2025-07-17 03:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| d3601cec-9fc4-3be6-bf5e-b5d5f1bbe407 | -3.3772 | -47.4792 | 2025-07-17 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| d5359f63-3b95-3a82-a3f5-a2d57c9499a5 | -5.6565 | -43.7393 | 2025-07-17 03:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 7521a62c-fd27-338d-ba86-f126e94f811e | -8.08446 | -47.62088 | 2025-07-17 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fae4d3ec-a71b-3afc-9ce3-909180eb12a0 | -5.01549 | -38.52959 | 2025-07-17 03:53:00 | NOAA-20 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e5e5f27b-2837-3097-a3e8-b1451878d1fe | -6.82276 | -43.78666 | 2025-07-17 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a0f2e2d6-be10-3adf-b7a1-ac197c45c61b | -7.18989 | -43.12107 | 2025-07-17 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| b2495a69-1620-38fa-b2ef-b7d47333d20e | -9.13249 | -40.54103 | 2025-07-17 03:53:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 39f6ae7a-5dc8-3044-9b06-4e903447b87d | -6.7316 | -44.33791 | 2025-07-17 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ead22769-91d8-3931-86e6-9e5fb07804da | -5.93285 | -43.36872 | 2025-07-17 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 46781f11-2382-3052-b376-f5a3b644548f | -5.51624 | -41.32559 | 2025-07-17 03:53:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |


[Clique aqui para ver as próximas entradas](README12.md)
