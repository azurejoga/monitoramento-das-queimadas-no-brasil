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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b09dae87-e6a1-3b16-9d7a-73160963b343 | -20.42525 | -46.50562 | 2025-08-22 04:21:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cdd1dcd6-533f-385c-b560-54f241befddf | -15.00121 | -54.86824 | 2025-08-22 04:21:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b3ba77b0-ad77-34e8-a5db-f05a6b33234b | -20.33179 | -46.5687 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef2ceeaf-a345-3d71-b510-16f31cbd221d | -20.33513 | -46.5694 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e624f1bd-dfdc-3482-a51c-89c6becce449 | -12.95189 | -46.29082 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 761e9078-dc26-3a0e-9564-f3fc8c9bcd42 | -14.86339 | -47.97095 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 90132513-ae64-371f-8f63-0109294f1233 | -14.60468 | -54.83993 | 2025-08-22 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6606fed7-df02-32e3-b42d-639f01bafc8f | -17.34967 | -48.1712 | 2025-08-22 04:21:00 | NOAA-20 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b8d17e18-62c7-3295-b9eb-434a64011bd7 | -20.26933 | -46.68668 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1bf51f8-7ba3-3588-afe5-d7bca2667af4 | -12.99611 | -56.88182 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a05557e3-c585-30f4-b7a4-0129a1c3205c | -14.88159 | -48.04956 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 24d98359-74d1-396e-9bea-142a719cf15c | -17.67682 | -54.05196 | 2025-08-22 04:21:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8b82952-4aa8-3e9f-ada3-c689ddc4256f | -14.62105 | -54.86007 | 2025-08-22 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 27ccae0a-2ec3-3f3f-b5dd-47553cef2177 | -14.83447 | -47.92439 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e5c15f9-88c2-33f5-9154-785b693a4877 | -14.76554 | -45.4058 | 2025-08-22 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e9f3fb0f-a6f2-39cf-b591-a7b923a326d0 | -20.43938 | -46.50374 | 2025-08-22 04:21:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 687803c1-9656-3991-8527-1cb3dc661b34 | -15.49995 | -48.04884 | 2025-08-22 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f86391dc-97ae-3c81-836c-ac27ea2d3f5f | -13.00131 | -45.22863 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0f5185ba-deac-3d8a-a8e7-8fba5163fef8 | -13.14026 | -46.90181 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49529fa2-92b8-302b-a6f0-2671eef6ff93 | -15.66451 | -52.69739 | 2025-08-22 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dcec65b6-70cf-3f85-80aa-f20f8726b8aa | -14.647 | -54.88353 | 2025-08-22 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e3a0f0c8-1f11-34aa-970f-ac684a155666 | -13.02964 | -46.31439 | 2025-08-22 04:21:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0458a5af-aa27-35f3-ae27-6a6c6b5a7049 | -16.50401 | -46.73931 | 2025-08-22 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce1290bd-5ae7-3765-84dd-79a1723a2c74 | -13.37773 | -47.49689 | 2025-08-22 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f4838ece-4b97-3745-8fd5-e7dbd3e7dc1e | -13.63311 | -46.87768 | 2025-08-22 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d76e67e4-223b-3d27-b20e-f368b39290b7 | -14.75388 | -56.02806 | 2025-08-22 04:21:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a9c980d-9cc1-3790-b5b1-8ada70575484 | -15.02528 | -54.86157 | 2025-08-22 04:21:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f4a4f0dd-7c9f-3094-91ea-ae23a64e253c | -13.14907 | -46.91069 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3da526e1-33ff-3d6c-9203-8acf0cb06ec9 | -15.19569 | -48.69954 | 2025-08-22 04:21:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c966516a-2f9d-3cca-8f9b-5135ab113c81 | -13.02962 | -46.33609 | 2025-08-22 04:21:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9cb42b99-3bed-3b5d-ab4d-d9bdcd0f00a2 | -14.76331 | -45.42044 | 2025-08-22 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8f9ec5d4-5ca2-346a-a50f-7a2231434324 | -16.78309 | -47.65967 | 2025-08-22 04:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dd88e375-688a-32c8-abe8-6d4c004f0ddd | -14.76242 | -56.04024 | 2025-08-22 04:21:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78a76aa3-acb6-3abf-bec7-7b3933b9c3b3 | -12.92324 | -46.17019 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 210d6ef0-f05d-395b-8ec5-6eb96eaeb9d3 | -20.7537 | -41.88575 | 2025-08-22 04:21:00 | NOAA-20 | CAIANA | MINAS GERAIS | Brasil | 3110103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dcd54e3c-7d47-336d-9367-45fd6b2bcbbe | -13.05881 | -46.83712 | 2025-08-22 04:21:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c0e90f96-faae-37d4-bec4-e514c822ad51 | -13.62592 | -46.88012 | 2025-08-22 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1009bda5-d168-35ab-85ce-08d31c1598ea | -11.33589 | -55.42513 | 2025-08-22 04:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 700a773e-adc9-3ceb-be7b-e7f333f9eef5 | -19.46021 | -44.73267 | 2025-08-22 04:21:00 | NOAA-20 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b8515327-a365-3fef-a19a-33c4d4f9240c | -14.73149 | -46.65509 | 2025-08-22 04:21:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f0caedd0-15e4-3fc0-923e-cf01bcb6d28e | -15.19327 | -48.11778 | 2025-08-22 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6c08bc48-ee68-3bdd-a66d-4981d6580e60 | -17.50667 | -48.00004 | 2025-08-22 04:21:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 353cace4-a3c5-36fe-8f69-de0c357de27d | -14.7592 | -56.00124 | 2025-08-22 04:21:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e1d10ac-04b8-31df-9b66-892dc4e8b588 | -15.9074 | -48.40718 | 2025-08-22 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a65473fc-a149-350f-81bd-6c2777f3df42 | -18.28531 | -45.53829 | 2025-08-22 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f67acd38-db1c-34fa-9c5c-9c12f1370402 | -16.52233 | -42.5136 | 2025-08-22 04:21:00 | NOAA-20 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5274f58-d153-36ff-9d08-28f2d43520f8 | -13.45912 | -47.05381 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b8c4ded0-1b0c-3d98-b404-bd2e236a89b4 | -12.99298 | -45.23837 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 78a5a6ac-822c-3f04-9a52-867093b7368e | -12.94914 | -46.28675 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20e8197f-219f-3a5e-8af7-853a99209db0 | -17.67165 | -54.05519 | 2025-08-22 04:21:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0cba4b62-4511-3063-98a3-79a166542de8 | -20.36157 | -46.55437 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99a137c7-0015-3cdc-89ac-0a487df9ddca | -12.99683 | -45.21315 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 850c89f0-2db5-3e67-be5e-a6e5491ee151 | -14.3452 | -53.12732 | 2025-08-22 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63ef52c5-1129-33eb-8caf-36a86ee79140 | -14.76778 | -45.41367 | 2025-08-22 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5d3d922c-47e4-3b81-a858-401a5e6bd0e7 | -14.45026 | -48.47413 | 2025-08-22 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0cc1e84c-539d-313b-8e80-7b276078a7a1 | -13.48496 | -47.03934 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e507cf7e-f641-39ee-abe9-bee5b608a15a | -15.56253 | -50.31579 | 2025-08-22 04:21:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1403b2a0-bd77-3440-93bc-b97b96207c48 | -15.1489 | -47.95566 | 2025-08-22 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 394bd785-b5a6-33ee-8c8c-79fd64feb938 | -13.02795 | -45.16637 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 137f127f-e538-3b53-9d8a-47c1cae32fa4 | -15.19291 | -48.69516 | 2025-08-22 04:21:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d45b50f9-149d-3c25-b69b-f77724752e83 | -13.4971 | -47.04873 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0a68a4d-35d7-34a3-96fb-d177146a1f8f | -18.29874 | -49.56437 | 2025-08-22 04:21:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| f11ceb6e-bb0a-36ed-87b6-2c9fe9c4b6ad | -18.28588 | -45.53438 | 2025-08-22 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8e06407-9972-3eea-bd80-bb1054d95850 | -18.74609 | -44.47923 | 2025-08-22 04:21:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bbcabea6-6a71-38af-a5e4-525e2ea6588a | -14.76446 | -56.00229 | 2025-08-22 04:21:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63c31234-1ced-34f9-9aed-419f9ae6abab | -12.99019 | -45.23423 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 11d3a1f5-3ea2-3b6a-8918-9a979b193396 | -13.03128 | -46.32551 | 2025-08-22 04:21:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6ecfb3f4-3607-3979-8f38-def710ecca19 | -13.03073 | -46.32903 | 2025-08-22 04:21:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 53aee119-b150-3b87-b1fb-04649abeab23 | -13.14143 | -54.9202 | 2025-08-22 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5bc709a4-d162-336f-8714-3ca5c754798d | -13.02519 | -45.18442 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b266cc55-e7fc-31e6-acf2-83cf2234b03e | -12.99742 | -45.2317 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| bc8fd7e0-bbbd-345d-be8a-d38415545b61 | -14.62723 | -54.85444 | 2025-08-22 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b874faef-bc26-3583-acaa-827bc58eac29 | -16.74644 | -49.31517 | 2025-08-22 04:21:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09e1857a-5f35-3084-9193-c710fa725f20 | -14.64808 | -54.87792 | 2025-08-22 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eaedb86d-05dd-3f12-8348-093065cae352 | -14.62225 | -54.80206 | 2025-08-22 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c55395bc-b791-3e52-94e9-8ee5eec0f7e5 | -14.99743 | -54.8616 | 2025-08-22 04:21:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1afd256-df52-3140-ace0-06d879051e1f | -13.03464 | -45.16743 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 120a68fa-eca9-37de-82eb-dec170ad60cb | -13.64141 | -45.70152 | 2025-08-22 04:21:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 76684956-f070-3425-8db3-e28da89115a9 | -18.29046 | -45.50303 | 2025-08-22 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b24353cf-e41d-3ab6-9841-1eb518f9bf10 | -14.32112 | -52.01442 | 2025-08-22 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8023819-e827-3f34-8770-c5aaca606c0e | -12.94199 | -46.18046 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6cdedf42-08ee-3c9a-a9d2-5f499c76ed62 | -12.65506 | -47.80174 | 2025-08-22 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 193d1b7c-a9a7-3728-9076-0426e03e2907 | -13.03247 | -45.20406 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f5c1244-3417-39e2-907d-a4523458c926 | -19.29212 | -48.43379 | 2025-08-22 04:21:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e56d4ac-9ed9-3ce8-a04a-3009ec104709 | -20.35533 | -46.57294 | 2025-08-22 04:21:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9d8a3b3a-2f43-345d-afae-3bbd04342082 | -14.59516 | -54.78537 | 2025-08-22 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b3485f5-e126-3335-8e78-11a95ec2b94a | -13.0224 | -45.18027 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a8058f6-25aa-3407-a2c5-2ff0e3d0a314 | -13.02685 | -45.17359 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23f66f49-27a7-314f-a22b-1e762aafc62f | -12.92599 | -46.17425 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 113d33b4-677d-3bee-8e66-b8ab7987d752 | -13.6464 | -45.71331 | 2025-08-22 04:21:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1b78e44f-4249-3bb1-97a8-fa8e3e766aa4 | -20.23413 | -46.61144 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 459a5836-2a81-3f10-a274-5774ada08554 | -12.49644 | -53.81294 | 2025-08-22 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b7d9fe6-fcc7-3ab5-ab08-1d991a600843 | -19.45786 | -44.73361 | 2025-08-22 04:21:00 | NOAA-20 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6d2127a8-7b39-3662-8a7b-242fb9b5cfee | -14.64751 | -54.90723 | 2025-08-22 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36d1d8d7-0859-33b7-88c0-bc56053b0d45 | -14.26369 | -53.31976 | 2025-08-22 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eca3f86c-4dba-3a6c-987f-3edebbf8aa61 | -12.96408 | -46.25663 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 40d240b5-9754-3901-b161-92ff9ae9b17b | -13.46605 | -47.05084 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 24d65295-82cf-38a4-b696-8ae26178c9b2 | -13.13636 | -46.90489 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1948f63c-4b29-3bc8-9b01-fd6336d684c7 | -13.50088 | -47.06768 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| efc1f1b4-5d30-32c2-b3ce-d7b90cf5216d | -14.75649 | -56.04251 | 2025-08-22 04:21:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README36.md)
