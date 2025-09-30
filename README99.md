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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5d23de5-8a66-3007-ad4e-61a67424b2f8 | -14.55202 | -48.25388 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4892d8eb-59ae-3f73-9549-378b3136cb90 | -14.80872 | -48.75375 | 2025-09-30 05:10:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b198b877-7830-3952-958a-2066922dc425 | -14.7346 | -45.66613 | 2025-09-30 05:10:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6721646-0923-36c8-a15e-ff090639f268 | -15.93238 | -48.1254 | 2025-09-30 05:10:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed0462d3-bc71-3825-b0e4-95ef7ae66d2e | -15.80503 | -59.52211 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6368d77a-c231-3337-9b72-e7f13eb7890f | -14.69365 | -48.24473 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c3d3386-b0e2-3b61-a475-4ff7a2d41e34 | -15.93377 | -46.20871 | 2025-09-30 05:10:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9aa0d2f-2b80-3b92-b9f1-ca4ae2df0c37 | -15.53967 | -47.86904 | 2025-09-30 05:10:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1d3649b-516b-3dc3-b51a-331c3d40e601 | -17.39696 | -47.13652 | 2025-09-30 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 80091fff-1607-3e57-95bb-90abc2d3ea7b | -17.75682 | -51.3456 | 2025-09-30 05:10:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a4d7c7e5-6726-324b-92d4-8fecf22f881d | -15.92685 | -46.21446 | 2025-09-30 05:10:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 10a9fc41-4ac4-318e-b15f-e212d44efaef | -15.27092 | -49.25269 | 2025-09-30 05:10:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| df58b995-cde0-3ba3-bd4b-0c59bd650e7f | -13.81985 | -47.46481 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65dabd07-9d71-37c8-987b-1b0ffc5c18a5 | -15.59887 | -47.83043 | 2025-09-30 05:10:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d0c24260-5fc8-3920-9326-06045026c214 | -14.53646 | -48.38118 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f009f963-11e0-36f4-b3cc-7511d9c2f3d3 | -15.20004 | -50.18626 | 2025-09-30 05:10:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 67092fa5-18ee-31eb-8522-26a30c5c7470 | -15.29995 | -56.79084 | 2025-09-30 05:10:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c750211-e26a-3722-8d08-309b2ececf34 | -13.73607 | -47.89873 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc320926-dfe7-3454-8c14-353400ac1c78 | -15.84352 | -54.97614 | 2025-09-30 05:10:00 | NPP-375D | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4fc9a784-5cca-38c0-9aca-0e17979958d6 | -14.58285 | -48.28345 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8c2fba2-cbd6-345a-baff-9ea7ad0c8e7f | -17.40299 | -47.14908 | 2025-09-30 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f86c7a3b-a0a7-3ea0-9775-98d44938563c | -15.9174 | -59.49878 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c56d4af6-93c7-3818-81a1-7d27106cb3ec | -14.39646 | -47.1475 | 2025-09-30 05:10:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e7d7cb76-0cd0-3789-84ef-8693eca8a44f | -14.27143 | -52.93903 | 2025-09-30 05:10:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1253593-afb4-3c04-bd45-80a4cd2615b5 | -14.51335 | -48.39215 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c2c911a-04b2-3d2d-975d-9e35711fb95e | -15.24608 | -56.80491 | 2025-09-30 05:10:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 908df8e1-3f0a-3367-b76e-9475012422cc | -15.92355 | -46.20753 | 2025-09-30 05:10:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dcb672d4-7c89-3ec4-a1a4-c758423a4c52 | -15.26195 | -49.71811 | 2025-09-30 05:10:00 | NPP-375D | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5bb4b5ad-98f0-3dd2-ae4d-eeaf1faaacbf | -15.06852 | -45.05564 | 2025-09-30 05:10:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b9ca02c3-392a-3290-bfa5-22a2bf417b13 | -13.63698 | -48.03224 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| caa4af52-691e-35ec-8539-abd1d789a52f | -15.2569 | -49.71832 | 2025-09-30 05:10:00 | NPP-375D | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 99b08518-acb5-3280-8293-d9c747b4b206 | -15.54985 | -44.35494 | 2025-09-30 05:10:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cb96ebf7-187a-3e98-b430-bc83ee8d9941 | -14.57987 | -48.2146 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1efcd3ba-83d2-3137-bce6-78a0fa31bb79 | -14.53312 | -48.23867 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a5a46f3-4842-3a20-b846-ccd14329f611 | -15.29507 | -46.41202 | 2025-09-30 05:10:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| de4d9392-eb85-3ce1-a411-a57c9b256b9f | -15.26785 | -49.49914 | 2025-09-30 05:10:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0374332e-b1a3-3684-87ba-f3caf38b66c5 | -15.27777 | -47.86133 | 2025-09-30 05:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 615ebc8c-524d-3bc6-90d0-a8cbd44ea6b0 | -13.78984 | -47.95957 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 710f0991-9825-3b83-a549-b24c5b2a3c81 | -15.25255 | -49.71267 | 2025-09-30 05:10:00 | NPP-375D | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f238115a-1067-3c0a-9b96-016e57958f0e | -15.71886 | -47.59408 | 2025-09-30 05:10:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5f1a0cf4-1e1b-3c0d-b228-6404126592a2 | -15.71897 | -59.51532 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c2fc4e3-e3ec-378b-8f4f-e5f6cbff9b5a | -15.89377 | -57.48952 | 2025-09-30 05:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acdf4401-88f8-332c-9d99-157d2228f7a3 | -15.80101 | -59.52531 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48b637f2-d054-3660-ad48-f76faab4e214 | -15.29321 | -56.78981 | 2025-09-30 05:10:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3c72a0f-0d24-3c84-b27e-b60c68d93c45 | -13.79926 | -47.88063 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aec56dc7-fe1d-3424-9be4-da29331ce1f4 | -14.66653 | -48.14436 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0a3a290-a1b9-35b7-9d07-29ef0526cf36 | -14.51619 | -48.45812 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9209ddf7-fddf-36fd-a961-1f3bd2b5fb46 | -15.2695 | -49.26495 | 2025-09-30 05:10:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df396fe6-d2f1-3c70-84d4-13d704d82f83 | -18.4748 | -44.0252 | 2025-09-30 05:10:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d040e93-2a29-3924-a967-d8b22b294b65 | -14.50805 | -48.45935 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11feff47-4ad4-3eb0-aaa7-749679faedbf | -15.91997 | -46.24109 | 2025-09-30 05:10:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4492954a-6cf2-35ef-baad-12ded52c4d77 | -14.51716 | -48.42708 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ca04c36-6e00-361c-bb66-a6544dcc9317 | -13.7988 | -47.88459 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b52923ff-e98a-34d0-916b-c60e9ff4c01d | -14.64574 | -46.96604 | 2025-09-30 05:10:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d05a40f9-f924-3d7d-ae92-136f062b24ae | -15.9027 | -46.22476 | 2025-09-30 05:10:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34c1109a-be29-328f-b17a-fa991ff15c6e | -15.1172 | -46.45732 | 2025-09-30 05:10:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2eaf3748-0d1a-3c86-a5b9-35ed3800b195 | -13.22834 | -50.93468 | 2025-09-30 05:10:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| db4892c2-50cd-36fc-a244-31d1529d2008 | -15.26261 | -49.71263 | 2025-09-30 05:10:00 | NPP-375D | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dae9d047-99f2-3fea-9f4c-43b5de2f64c5 | -14.70969 | -48.2487 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 389185ae-26c2-3881-9528-db9825afc004 | -15.38948 | -47.07434 | 2025-09-30 05:10:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 83bba4ed-3cdf-345b-b270-b86df0196ef6 | -15.97428 | -57.23528 | 2025-09-30 05:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f73d785-98ce-3cb4-a78b-ae910203f4f3 | -14.72351 | -45.66625 | 2025-09-30 05:10:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8165d9b-e6eb-376d-884b-57c13b956420 | -14.19143 | -46.60623 | 2025-09-30 05:10:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5bfb9e1e-c637-3b62-9b2c-a8a688585393 | -14.51317 | -48.4384 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 957fc2d2-b1a8-345b-bc61-861065e67f72 | -15.92632 | -59.50818 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20e675f6-0eed-3a9d-a3b9-b66008c7350c | -14.55079 | -48.26392 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1a642dff-1511-36fc-aba6-f3986df91d0c | -14.66525 | -48.14649 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81b72cc2-f934-3f02-9a0b-33f07385d4ce | -15.47451 | -47.94201 | 2025-09-30 05:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5558716a-8ecd-3791-bc26-b0459df8b782 | -16.3931 | -47.03495 | 2025-09-30 05:10:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 638033d7-8146-3e30-8717-db13290642b8 | -15.71975 | -47.58592 | 2025-09-30 05:10:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.5 |
| af24dc5b-f0c3-3145-bfe1-62834133c52a | -17.92153 | -57.59178 | 2025-09-30 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 59ddce53-e909-32ab-8129-3e1279c09b6c | -13.73337 | -48.68731 | 2025-09-30 05:10:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 57155b2e-a633-33fb-9792-37420261451d | -15.91782 | -46.24155 | 2025-09-30 05:10:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 867764fc-e8d7-3440-8afe-3ba8aed2d936 | -15.82172 | -48.16781 | 2025-09-30 05:10:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 319afda5-e8a2-3d9d-9500-07f3a3583b42 | -17.88741 | -57.62434 | 2025-09-30 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 37449df9-0698-319b-b53e-73417af6e373 | -15.84145 | -59.59835 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e531860-89e1-30d5-b3ed-ba711a72c81e | -15.3294 | -46.26368 | 2025-09-30 05:10:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0ca8929e-c292-38c6-8a91-0ecde52748d4 | -15.27286 | -49.26146 | 2025-09-30 05:10:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7807484c-3465-37f2-a688-92efdb0209e7 | -15.51697 | -50.04892 | 2025-09-30 05:10:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a6aa6d45-cea9-3c74-8db2-b94ae779c718 | -15.25227 | -56.83202 | 2025-09-30 05:10:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f139f15c-dd8f-3f80-b6fc-b9089f35b321 | -17.8835 | -57.62743 | 2025-09-30 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 12816afc-ba0b-3e7a-891f-9fcf68de75a8 | -14.79048 | -48.31986 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2498fbb6-4ac5-33e8-8656-be7efc93de28 | -20.62254 | -46.17555 | 2025-09-30 05:10:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e4d6bca8-924f-3303-bdc0-8ea567888f2b | -15.27177 | -49.27036 | 2025-09-30 05:10:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1944751-4656-3a61-9241-dbe1d1a54c7a | -15.2838 | -47.85822 | 2025-09-30 05:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 609a3a0c-9caa-3e9b-b4cb-ccb48e5ff6f9 | -16.52768 | -49.43269 | 2025-09-30 05:10:00 | NPP-375D | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4193de06-24cf-3937-91a1-dcbd6b1914db | -15.71495 | -59.51856 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0c8884b-2438-32f4-9a9a-b1b527f8b469 | -14.54934 | -48.47675 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| da373120-f05c-3a17-9f82-032c959461fa | -13.81144 | -47.48811 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b716d664-7fa9-3f1a-9414-90351fea2e56 | -15.17097 | -46.41946 | 2025-09-30 05:10:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ae5b00f-7262-3842-a0a4-e615621c3369 | -14.51574 | -48.39186 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff1fd161-9ec8-3541-a37c-41bd08460b54 | -13.76055 | -47.9257 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4fc78a0c-3c2e-3c6a-922b-e05a9913d1fa | -14.68143 | -59.84787 | 2025-09-30 05:10:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c78637df-734a-3b40-beaf-9d18656cbc4e | -14.72121 | -45.67021 | 2025-09-30 05:10:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3522ad05-b450-3432-b848-e9cbd0912712 | -15.80441 | -59.52591 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ecd9b8d5-5060-363c-be2a-b9da6aea97fa | -14.53768 | -48.24689 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 20d474ee-3fbb-304b-b8a0-3de05e695aec | -14.71439 | -48.25557 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ba76c42-71c9-3410-bb79-90cb60557a5d | -15.72174 | -59.51972 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6b99234-9018-3f92-a3d5-7ad5ba7f0768 | -16.42545 | -47.01558 | 2025-09-30 05:10:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eba91553-6203-38c0-aa85-bc30565ef291 | -13.26257 | -57.32804 | 2025-09-30 05:10:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |


[Clique aqui para ver as próximas entradas](README100.md)
