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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46b91bde-9496-3368-bde4-935e0cb93cac | -6.44333 | -42.4213 | 2025-08-28 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| afd6e5a7-03f8-36dc-b835-19d92daa659d | -2.44417 | -47.33231 | 2025-08-28 04:06:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d6682a6-b306-3fbd-bb4a-cdf1d66e0c01 | -7.42141 | -42.05999 | 2025-08-28 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e3328d44-0569-33cc-8587-b99a679b6b50 | -6.07872 | -44.00546 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c0c7deb-1002-31dc-afab-ce94d394f003 | -7.43848 | -42.03785 | 2025-08-28 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| de5cc7fe-8d43-3997-b9f2-d7f7928def42 | -6.18696 | -44.16372 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c67b1b5a-728b-3678-b862-e98702875902 | -6.86954 | -43.63058 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 187ade86-99e3-371b-8fc1-f0f7f334df32 | -6.1632 | -47.2787 | 2025-08-28 04:06:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1ebb45a3-a109-3f7a-8063-9e97c6b5ec7a | -6.57095 | -47.37995 | 2025-08-28 04:06:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1bca174c-3730-376c-addf-ba2a6b0dfdae | -6.44387 | -44.56548 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 47355e66-a57e-3a16-8fd7-a1a62656499c | -5.82769 | -44.10051 | 2025-08-28 04:06:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51a34fe4-9f54-3e30-8b69-f680bec1e11c | -7.42803 | -42.06105 | 2025-08-28 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f2a71bf6-f565-3d7f-9862-31301f41779d | -6.24115 | -43.82944 | 2025-08-28 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1db3e6b1-ef13-30ff-aa55-73a80a1d3d19 | -7.06287 | -44.36946 | 2025-08-28 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0421eefc-d848-3e7f-9672-27e05db43b4c | -6.4432 | -44.56959 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b1b0e190-2a83-3040-88bd-2141acc7edf7 | -6.46216 | -43.71985 | 2025-08-28 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45a09bed-3f05-3ec1-8457-67dbcc8cb640 | -0.7532 | -47.75331 | 2025-08-28 04:06:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f8c3e4d3-08eb-3c4a-a739-422ca713ceb2 | -6.32349 | -42.87762 | 2025-08-28 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3eb5f96-0653-3a7d-ae52-408c581558b5 | -6.2626 | -43.8288 | 2025-08-28 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ed6a996-e7e8-3331-99f1-5bd4cf2317cd | -6.16384 | -47.27478 | 2025-08-28 04:06:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a543c5a6-7039-3f8f-a458-907ad9beb334 | -7.63378 | -42.66904 | 2025-08-28 04:06:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 819dbc40-f84c-37b1-85d2-65f6e8ddca53 | -5.20493 | -44.32347 | 2025-08-28 04:06:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e22eab0-a57c-31f3-af66-3156dddc153a | -7.38872 | -39.68284 | 2025-08-28 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 14.6 |
| d82daff7-4ff6-3ffc-9668-08cb4ad0a643 | -6.15055 | -44.38767 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4ccaaaf-fb76-3cb8-bcb1-14b11776f92f | -7.43574 | -42.05517 | 2025-08-28 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 102636a9-fc6e-3ae8-9c4f-8e139828b62a | -6.15491 | -44.18295 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e30ec491-ad70-3eb7-a5a0-a9009a4f5871 | -6.51347 | -42.96312 | 2025-08-28 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d9deafa-d07a-36fd-af14-60dc39f5aef6 | -7.04992 | -45.87674 | 2025-08-28 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9a916d55-c1db-3ec5-997b-ea3d39ca4b4c | -3.49495 | -43.31174 | 2025-08-28 04:06:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 86c5add9-b69f-3f12-87c9-ee89594a5c23 | -6.57152 | -47.37806 | 2025-08-28 04:06:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b3d26427-d807-39d2-b195-f02dcef80b4b | -6.1666 | -44.06758 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7cf93e98-3030-3e02-a92d-aa7045a05cbf | -4.28728 | -40.93415 | 2025-08-28 04:06:00 | NOAA-20 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 3ab544d2-f883-358c-89a5-f34aee6bd2fc | -6.16057 | -44.39344 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56e711cb-79bb-34c0-b6e4-80e70c925756 | -6.92453 | -39.56298 | 2025-08-28 04:06:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9b6ae2b2-a19e-33e8-ba67-cdbfb4b029c1 | -6.19465 | -44.16085 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23f8a553-7ecb-3770-a7ad-f844be85a078 | -5.19514 | -46.06733 | 2025-08-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ef9f3df5-6f5d-364d-9fea-3445016092bf | -6.26035 | -43.82072 | 2025-08-28 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2544ea64-09c7-3b98-b5a6-d0277ddd70fd | -6.17966 | -44.00975 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9b0d0135-99c8-3fe3-ba67-ef7c3510e6a7 | -7.02335 | -42.02102 | 2025-08-28 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 73e8a898-122d-39ff-bcf1-ee6715cea0d7 | -6.19529 | -44.15689 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d522d6f2-3c49-30c9-8d0b-91c285fdf304 | -6.88214 | -43.61712 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 8261a773-42ce-3d1c-988f-e4dd49727765 | -5.74535 | -40.44663 | 2025-08-28 04:06:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 047f21de-d9c2-3610-8489-24a78557354b | -6.24357 | -43.37898 | 2025-08-28 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a29af5cd-fc6b-3490-8343-18df2e2b4e2e | -7.62373 | -42.71067 | 2025-08-28 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| aa3ed51e-5ef9-3eba-b90e-2e3af5b961f5 | -6.86942 | -43.63042 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 96b5e2c0-8e17-308d-9337-9b566450dc75 | -5.86094 | -42.89996 | 2025-08-28 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 332c7e27-a58a-3d72-b311-69321d0ae603 | -6.15576 | -44.04596 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d54dcb6-b23b-3d44-97a8-adf79565f03f | -5.81572 | -44.76473 | 2025-08-28 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea13956d-f5c7-3b8c-b238-a47dc3d8e7a5 | -6.87003 | -43.62669 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f47fabbf-99f3-32e3-9560-9f593cb5e530 | -6.12036 | -44.41586 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32a53626-0468-3396-9e9b-89f5bac7cd8c | -5.84172 | -45.30553 | 2025-08-28 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a942d29-a26a-3d37-b7e0-3e9a114c0c28 | -6.89077 | -44.40264 | 2025-08-28 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f0ddb48-d60e-3cb1-acd4-88fe1fcd92e6 | -5.69041 | -40.97406 | 2025-08-28 04:06:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 54452bc3-05a2-3f08-960a-007835eaed29 | -6.43746 | -37.13448 | 2025-08-28 04:06:00 | NOAA-20 | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 87a1e284-bab7-3171-af73-3cf7490787f5 | -7.5621 | -42.00715 | 2025-08-28 04:06:00 | NOAA-20 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d4b40d52-bd97-3638-a48c-d4f06489872a | -6.23393 | -43.37361 | 2025-08-28 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2541bcec-16ca-3fbe-8170-abfab4fb4e91 | -6.8697 | -43.6076 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39eeca36-8d0b-3312-bec5-a8add751a951 | -5.84547 | -45.30611 | 2025-08-28 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ebd3f28-6968-38f7-8e09-4cc5bf2a645f | -7.42196 | -42.05653 | 2025-08-28 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d47e20c0-b4b7-30f9-b547-4fe50012d5fd | -6.87148 | -43.59645 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d11be5f4-2dc1-3ecf-a4bb-aac29926f28e | -6.8685 | -43.61508 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88a7ead1-f13e-3745-896b-48b44cb81f84 | -6.87811 | -43.6203 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7ee24bcd-e9f7-3950-bc30-19ec92c4c783 | -6.15702 | -44.39284 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9f91c76-7abe-393d-9026-138c544e9fe1 | -7.39389 | -39.69522 | 2025-08-28 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 6.3 |
| f81756d2-fe0c-3b40-87b6-0f9960a551fb | -4.89748 | -45.55454 | 2025-08-28 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2893d6db-7ff7-327a-a1a0-0291fd5695bd | -5.59646 | -45.14296 | 2025-08-28 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18ed0cb3-93d0-3e86-845f-2029a965e44e | -6.92396 | -39.5667 | 2025-08-28 04:06:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9d2eaaf4-5588-3046-8a43-09b963d69541 | -6.88495 | -43.62141 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1210c5e4-b97e-3941-9304-123a8230fc50 | -5.71458 | -45.53299 | 2025-08-28 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8d6c742-befa-3f01-9e47-4206edbb3950 | -6.87193 | -43.61563 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54a832b7-cb35-33d1-8cd8-1c40f9813aad | -6.8775 | -43.62404 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7b9512f3-9622-3b5f-979c-c0c66ab105eb | -6.15411 | -44.38826 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eaf3eff6-eff3-32b8-9815-bf8a6d7b46ff | -6.32333 | -43.75186 | 2025-08-28 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 339e92fc-74c8-354a-9d42-76348e5bbf8b | -6.15437 | -44.02623 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b52899b-ac8f-3cfc-ac84-b852d94fd311 | -6.43829 | -44.57717 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 78bfd6e1-48f3-3b9f-840c-4cf811f6b214 | -6.32679 | -43.75239 | 2025-08-28 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 40764b53-85c1-3667-9dbf-612629243baa | -3.23873 | -50.80766 | 2025-08-28 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97d4b197-cab9-35ca-94a9-1adffb75cc14 | -6.87431 | -43.60057 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ab61142-de6f-3e53-ae89-d59d43be160e | -6.89141 | -44.39874 | 2025-08-28 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0874a388-8c02-3766-810c-78be98ddea81 | -6.80418 | -44.35653 | 2025-08-28 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bed31045-9ec5-3954-9831-e89be03ce338 | -6.16086 | -44.0587 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e671853-ab1d-3fdf-9d5a-a3d8ad1b1ba1 | -6.87146 | -43.50892 | 2025-08-28 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7edb5a32-efae-3425-ba57-c0ec6822271a | -6.87552 | -43.59315 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52fde20b-d86a-38c8-8779-4de8497076dd | -7.15612 | -44.15389 | 2025-08-28 04:06:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 940c00f9-2eed-3c71-8d87-f1210f855151 | -6.1599 | -44.04262 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6599d541-a8b5-3254-a47b-7b9447431037 | -6.86046 | -43.62146 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b6493ff-7d21-30ef-978a-5d7433149641 | -5.77426 | -44.92668 | 2025-08-28 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 027a2d74-14b6-34cf-8e83-ea15cbbcc6a6 | -7.15736 | -45.15133 | 2025-08-28 04:06:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 20f5c954-6229-3db3-abaf-4c0252240fa4 | -6.36884 | -44.05113 | 2025-08-28 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16f86ecb-0023-3369-8a07-d7f22978b01f | -4.79146 | -47.26096 | 2025-08-28 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| d332215b-cb83-3a1e-ac2b-489712b31f18 | -7.1652 | -39.43186 | 2025-08-28 04:06:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2983c2ce-8cee-399b-aca7-b3ef64619093 | -7.55934 | -42.00316 | 2025-08-28 04:06:00 | NOAA-20 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9b0f3859-f5e7-3c9a-b636-4a63e5690ee7 | -12.7898 | -48.14859 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bcac2943-eccd-3d88-b6c1-c091c90e4364 | -12.94911 | -46.32952 | 2025-08-28 04:08:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 91401de7-ce78-3fce-abea-82c0cae92595 | -9.45121 | -51.9529 | 2025-08-28 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 672551fb-f662-3e72-a608-1ae25a0dd885 | -8.85618 | -47.16097 | 2025-08-28 04:08:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26082460-30bc-31b8-be41-9d0573fabade | -8.4893 | -43.65375 | 2025-08-28 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0c13d38-3b92-3b47-8865-3783b9726c01 | -9.45255 | -51.94772 | 2025-08-28 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1fe779e5-60a5-31d6-a8f2-ade4ef462d83 | -10.53145 | -46.7087 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62a48b46-20a0-3f17-b067-debd2f8e4380 | -13.50733 | -46.86149 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README35.md)
