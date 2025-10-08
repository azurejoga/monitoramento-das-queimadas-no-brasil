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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f941f125-f4ab-3172-bbc5-bb548f8016e0 | -18.0085 | -44.3043 | 2025-10-08 03:51:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| ca78f579-f1b1-31d2-9b9d-b9acca21beba | -17.28528 | -42.6573 | 2025-10-08 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| cce61678-37c8-382c-b3b3-0a16a74589f4 | -16.34488 | -47.04572 | 2025-10-08 03:51:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79e6fb59-bb05-386e-a348-8160ecaa4f44 | -19.60002 | -44.64954 | 2025-10-08 03:51:00 | NOAA-21 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6530f531-ea5f-3029-bb0e-c5ca57bb4319 | -16.18489 | -51.74587 | 2025-10-08 03:51:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2690a22-98e5-3e7b-8aac-42bfe74695b1 | -15.7737 | -46.25292 | 2025-10-08 03:51:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 581e4f52-a365-37a3-b01f-6ba1132dc7ea | -20.26666 | -43.26039 | 2025-10-08 03:51:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| d2c8572a-d862-3fce-a544-93aa31c7e910 | -20.17054 | -42.21239 | 2025-10-08 03:51:00 | NOAA-21 | CAPUTIRA | MINAS GERAIS | Brasil | 3112901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 4705a1b9-13c1-33ec-9c88-4d002a172682 | -15.35566 | -47.3257 | 2025-10-08 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31f95edb-c24f-339e-9ca3-6462acbfa8fe | -15.86461 | -44.82767 | 2025-10-08 03:51:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d2bad9c-9eed-3707-8891-95ed8a424282 | -21.04237 | -45.6759 | 2025-10-08 03:51:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c5a0f6d8-78c8-362d-8720-4c5d8f125ca1 | -17.28963 | -42.65364 | 2025-10-08 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 830ac512-3038-309f-89ac-976fc870395a | -17.99829 | -44.98665 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0fbc8eaf-113a-3fc3-a7a5-1fac3885990f | -17.90529 | -44.40411 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 312a2fbb-1988-3265-b554-eb2f333af18d | -16.29389 | -45.24245 | 2025-10-08 03:51:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4f1593ce-b3f5-3ddc-8393-325a0e7316a4 | -18.66048 | -43.90453 | 2025-10-08 03:51:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f634fb28-55be-3710-8117-415a854e293b | -21.90396 | -44.89253 | 2025-10-08 03:51:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 31b345af-0b95-3358-894c-702c724b4d1e | -20.28595 | -48.51368 | 2025-10-08 03:51:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4530e1b-8d8c-339f-bfa2-ca05c99bf890 | -18.3561 | -42.39674 | 2025-10-08 03:51:00 | NOAA-21 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 37d32f33-8b0b-3ca1-b7e3-e7239314344d | -15.70314 | -47.51133 | 2025-10-08 03:51:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 90cf122e-124b-3b4a-a9a5-59e59d6239e5 | -17.85322 | -44.31416 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb3b20ea-086d-3b03-b5e2-ac8e4c790954 | -17.1343 | -45.78436 | 2025-10-08 03:51:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c2aace4a-a452-3095-a3d5-e83d10ce5cab | -19.38857 | -44.38963 | 2025-10-08 03:51:00 | NOAA-21 | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c7bfe04-5288-3df0-93a1-57911407adde | -18.03165 | -44.9659 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43f98e29-9faf-307a-b1be-0657903d4088 | -17.28888 | -42.65799 | 2025-10-08 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2f361f54-9d36-35e7-ad7a-5fb17f8575b7 | -15.20173 | -49.7627 | 2025-10-08 03:51:00 | NOAA-21 | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 393d0ea2-be03-34df-a037-9584f3d9c9f7 | -18.2958 | -45.44061 | 2025-10-08 03:51:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c0081100-a663-3923-ba10-d9ba14a7ec75 | -20.18907 | -43.93406 | 2025-10-08 03:51:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 31998bd2-0f29-32b9-b62e-ba4edc8dc726 | -17.14169 | -43.45625 | 2025-10-08 03:51:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 257548fd-b178-30d7-900d-46ac2cbbfba7 | -19.34262 | -43.08369 | 2025-10-08 03:51:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 09f502ec-118a-3340-b831-d0ce564780ba | -17.15259 | -43.43854 | 2025-10-08 03:51:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8e9011c6-1d2b-3811-8330-fdf91d6af776 | -17.56838 | -46.06013 | 2025-10-08 03:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b61f5f8f-7f25-3ff8-8a4a-7d2aa296c455 | -16.13358 | -47.9076 | 2025-10-08 03:51:00 | NOAA-21 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 94721eca-6e0a-3400-a565-cffc14a51281 | -22.38399 | -49.96204 | 2025-10-08 03:51:00 | NOAA-21 | OCAUÇU | SÃO PAULO | Brasil | 3533700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ccdf39b9-f6d6-3264-a992-0f4811e07845 | -16.66893 | -43.93217 | 2025-10-08 03:51:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43bec59c-95a7-3ee6-8d76-c121a9b47874 | -22.38911 | -50.01223 | 2025-10-08 03:51:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ef6f65d6-9a36-38f6-9344-d705420579f1 | -17.45489 | -43.38395 | 2025-10-08 03:51:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77a9838a-e0ea-3a8b-8f34-0aa845b50918 | -17.57798 | -42.24504 | 2025-10-08 03:51:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 41c14c2c-b532-348d-9c0a-5dfcfac251a6 | -21.06905 | -46.88601 | 2025-10-08 03:51:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21e0075c-5d05-3933-81fd-e763689f1434 | -18.07904 | -44.45182 | 2025-10-08 03:51:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4fa32245-ccd4-38fd-8971-e7cb1182b04f | -21.06825 | -46.89005 | 2025-10-08 03:51:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ced70520-f0ef-38ac-9dec-568cb12a4d66 | -19.51812 | -44.08199 | 2025-10-08 03:51:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6aa751ee-885b-3ac0-a8ac-050cde05200a | -19.51238 | -44.0707 | 2025-10-08 03:51:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ff2fde7b-c032-3bde-96ed-50e75b3f8448 | -18.34575 | -42.3917 | 2025-10-08 03:51:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 729da436-b56c-3e85-9f54-c765672e5b58 | -16.02632 | -43.70467 | 2025-10-08 03:51:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abba79c8-db36-3611-ae26-641f8a6b9802 | -18.01902 | -44.94369 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 190886c3-80cc-32f3-9324-b2236ed11649 | -18.65967 | -43.90903 | 2025-10-08 03:51:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 05f0a7d9-f973-349c-b447-df1e99b71e06 | -20.27025 | -43.26096 | 2025-10-08 03:51:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| dda86f30-c933-3a61-9283-eb1d21fd4036 | -17.95824 | -42.94468 | 2025-10-08 03:51:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b25c24ea-dda2-3f14-92f8-080161ddcd00 | -18.07695 | -44.46339 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b14f48bb-cb7f-3df5-b3bb-0f7b120bcec5 | -15.19613 | -49.75935 | 2025-10-08 03:51:00 | NOAA-21 | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89098bd5-1783-3aba-9d73-be65f2b77d4c | -17.27881 | -42.65171 | 2025-10-08 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 76d36bf6-2d93-38d8-abde-60b9b6f436ea | -18.51182 | -42.09702 | 2025-10-08 03:51:00 | NOAA-21 | MARILAC | MINAS GERAIS | Brasil | 3140100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 4d5a33ff-b3ea-3217-8bc0-8fba444336ad | -18.94219 | -44.68445 | 2025-10-08 03:51:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93feb1e0-a876-3643-a7f6-71a52d4aa1e0 | -19.97473 | -43.21586 | 2025-10-08 03:51:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6331a8d4-f8c1-3339-ae9c-351907c87b88 | -18.55661 | -41.5756 | 2025-10-08 03:51:00 | NOAA-21 | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 7b55b3c7-787f-35c7-989a-194ca834ae44 | -19.33151 | -46.04099 | 2025-10-08 03:51:00 | NOAA-21 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a8f82991-748b-3fc3-b6c5-66ce4057c94b | -22.34019 | -49.88077 | 2025-10-08 03:51:00 | NOAA-21 | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 41e37053-56e3-332e-9996-caa872a13264 | -17.27085 | -42.65474 | 2025-10-08 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 32e57571-8e33-3197-8310-c66ad284b3dd | -17.57357 | -46.05673 | 2025-10-08 03:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f536ff19-b7e2-3c95-8f5d-a452aabaf7ea | -15.38594 | -47.30658 | 2025-10-08 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b9bcebe-5b54-3998-b9c1-39829ab5e580 | -15.49437 | -47.93124 | 2025-10-08 03:51:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2331459c-d31d-3aca-bca5-3bb574ab34bf | -19.83689 | -44.06813 | 2025-10-08 03:51:00 | NOAA-21 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a2adbea-42ff-3772-9f31-fb58d1aedfdc | -19.87643 | -44.30295 | 2025-10-08 03:51:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 81f81c4a-d6b0-39c5-9a11-95e8edff3169 | -21.3021 | -45.95044 | 2025-10-08 03:51:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e91aefb7-0f16-34e0-b149-728fc35fecf2 | -20.30169 | -48.51138 | 2025-10-08 03:51:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a153fb08-97a1-3c54-bdef-5203faec0721 | -19.7225 | -43.90508 | 2025-10-08 03:51:00 | NOAA-21 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea011c82-ac92-349b-ac00-12d6daecc2eb | -18.54002 | -45.07926 | 2025-10-08 03:51:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a93d4763-61a0-3425-a02b-f6782a84f12b | -19.57967 | -44.65099 | 2025-10-08 03:51:00 | NOAA-21 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7a58fa3c-8741-3b90-9730-26ce0444eab9 | -15.38744 | -48.02866 | 2025-10-08 03:51:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 331f177b-197d-3d39-84f7-b0a362faf603 | -17.45407 | -43.38858 | 2025-10-08 03:51:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 839a9de9-055c-3a79-afb3-5441d9c412b8 | -18.40981 | -45.21142 | 2025-10-08 03:51:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 227192ab-59ee-3694-bf9b-2c6f82b99a07 | -16.58355 | -46.55352 | 2025-10-08 03:51:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 25b0a918-ce08-380e-84a6-d1ff7590f1cd | -19.45237 | -44.18501 | 2025-10-08 03:51:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f360f1c0-189a-3dd7-9110-e1d65ca7bced | -18.29507 | -45.44451 | 2025-10-08 03:51:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e94a99f9-4bb5-3ab8-804b-697ae7c59f7c | -15.49504 | -47.92793 | 2025-10-08 03:51:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3e4846e9-8faa-3f4d-bd58-0465690decba | -22.33947 | -49.8841 | 2025-10-08 03:51:00 | NOAA-21 | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a7d1f20c-8b9e-37c1-8935-3cb025529935 | -18.45739 | -42.52583 | 2025-10-08 03:51:00 | NOAA-21 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 35dc709a-6fc4-3020-ad4b-61f469ba5742 | -15.36709 | -47.32363 | 2025-10-08 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76f4d070-d86b-32a6-873e-b11efe2a02bf | -15.20087 | -49.7655 | 2025-10-08 03:51:00 | NOAA-21 | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d05d53fa-ac5f-3dd8-8665-290f8f21b704 | -19.60045 | -41.89912 | 2025-10-08 03:51:00 | NOAA-21 | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 05e93924-f8fb-320b-90dd-31f2211cdbbf | -20.20869 | -43.95256 | 2025-10-08 03:51:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| dc21021a-5163-3f79-b3f0-b51c43954867 | -18.40649 | -45.20655 | 2025-10-08 03:51:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ee187703-2eac-32fb-a8b2-97ee76e8e019 | -17.38341 | -45.06376 | 2025-10-08 03:51:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 80f0e1e3-9a43-38b0-9928-631f4a382a81 | -18.19599 | -43.0475 | 2025-10-08 03:51:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 1c47ba84-1c89-3fcd-98a9-f138b0ad5d3c | -20.20132 | -43.95097 | 2025-10-08 03:51:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| c9b7f3cb-d9b4-3dea-93e0-a65f718435a9 | -19.98523 | -42.0806 | 2025-10-08 03:51:00 | NOAA-21 | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 94ec5938-b7fc-3d41-b1fa-32d3e9f778de | -18.50122 | -43.90121 | 2025-10-08 03:51:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8b0a1e16-4648-30cb-bd1f-354f9202a371 | -17.3759 | -45.05818 | 2025-10-08 03:51:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2466d309-179b-325c-a5f2-76cfd9166abf | -21.94421 | -47.32314 | 2025-10-08 03:51:00 | NOAA-21 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 254e2d3f-28ad-37b9-84c8-44b16b093ee8 | -18.1356 | -40.25497 | 2025-10-08 03:51:00 | NOAA-21 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 827eb92c-c9bd-3368-b609-41bbba5c07a2 | -18.34925 | -42.39241 | 2025-10-08 03:51:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 74b4b916-e271-39bb-a772-86f45475a2cf | -16.13552 | -47.91402 | 2025-10-08 03:51:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 320302b0-fc87-3015-8c17-c7e79c53d2ab | -19.33901 | -43.0831 | 2025-10-08 03:51:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f2865a95-d9be-3921-9e2e-d3722f4df016 | -16.78386 | -42.72863 | 2025-10-08 03:51:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24bce5d5-a236-3a05-9cb8-e3e45d94fc5f | -18.04243 | -46.43649 | 2025-10-08 03:51:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61b4ea78-df67-3f59-a8d6-b191e4ec2f6a | -18.02759 | -44.96515 | 2025-10-08 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee29a7b9-8d79-3b3f-b4d0-9b0e28e5c3df | -17.15632 | -43.4394 | 2025-10-08 03:51:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 07cb1aff-e63f-3437-ab0a-2be36765906e | -20.20501 | -43.95176 | 2025-10-08 03:51:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 84058aee-2222-3cae-876a-dfcb1d358c2e | -15.79845 | -46.24766 | 2025-10-08 03:51:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README29.md)
