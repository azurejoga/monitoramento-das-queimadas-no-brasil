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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4cdd6527-6f9e-3917-8703-3bf63e253a2c | -9.88904 | -64.83195 | 2025-09-23 05:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91890227-2708-3389-ae8b-946b892a4cde | -8.0726 | -70.33098 | 2025-09-23 05:40:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e637961-9317-308f-9cb1-36cbed7f10d0 | -7.98836 | -70.90901 | 2025-09-23 05:40:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 890b1461-056c-35cd-85ec-69b6144b8e5c | -14.42306 | -60.31206 | 2025-09-23 05:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 864e69bd-2afb-389b-afc3-210f3564b7d8 | -9.28345 | -67.32575 | 2025-09-23 05:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67e31141-eacf-370d-a143-df2d356399e0 | -9.28961 | -67.2888 | 2025-09-23 05:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d11c62a-ccf9-3e59-bbeb-20a65eb8cfcf | -8.89407 | -71.33312 | 2025-09-23 05:40:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c93dd62-2f1d-3eb2-bd57-2981e1afc371 | -10.81843 | -61.42614 | 2025-09-23 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 00503013-5790-3a24-8ed3-2f12f8d4d5fb | -9.11634 | -68.32058 | 2025-09-23 05:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e731b20d-1682-395c-b936-a3b1786c7da2 | -9.47817 | -67.13622 | 2025-09-23 05:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3624b66-cc00-3707-a308-7067593d4371 | -9.00473 | -69.41295 | 2025-09-23 05:40:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d097227-70d5-347b-a809-6909238f9391 | -9.19454 | -67.56853 | 2025-09-23 05:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a34fc76-b4be-3c51-bc45-d060b8d7e06b | -8.4284 | -70.19451 | 2025-09-23 05:40:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2c024df-cebd-34bd-b41a-7313c30822bc | -9.2229 | -67.57671 | 2025-09-23 05:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74d0c295-3ef6-359f-8e75-7c9afd49eea4 | -8.86427 | -71.37469 | 2025-09-23 05:40:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9ed380c-a383-3d8e-840c-0a4178d64e83 | -10.82283 | -61.41592 | 2025-09-23 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c8db13fc-01b2-31aa-9f22-82cbd90245f0 | -9.44888 | -68.88711 | 2025-09-23 05:40:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e521318-627b-3822-9c35-f3d620a759e9 | -9.88515 | -64.83493 | 2025-09-23 05:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 42ce2877-3268-371f-bd2c-f6b187db86a3 | -9.46885 | -67.1264 | 2025-09-23 05:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51e4179d-2290-37f5-90ab-7ae8f95a873e | -8.30595 | -70.56738 | 2025-09-23 05:40:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71f8b2a6-123b-3b96-b68e-4ffadc567e0b | -9.19457 | -67.56762 | 2025-09-23 05:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7425000-42ba-3472-8819-5a532776a64e | -15.36377 | -59.17744 | 2025-09-23 05:40:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8b96735-18f8-3529-be33-c481715a3d7e | -9.942 | -67.22978 | 2025-09-23 05:40:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 311403f5-c731-3985-9c9e-30067c19604b | -9.47108 | -67.13501 | 2025-09-23 05:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf148f66-2992-3f51-9d2f-17b9cb64d972 | -15.31494 | -59.41879 | 2025-09-23 05:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 17dcd564-e455-3a4f-954a-2390cd3018a9 | -7.99321 | -70.85487 | 2025-09-23 05:40:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7962332-a3cc-35eb-aa49-ac889a0313f3 | -8.8611 | -69.15971 | 2025-09-23 05:40:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c23ad1c-12db-34bf-a2c7-ad217497c527 | -15.28336 | -59.42126 | 2025-09-23 05:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e02a3a8b-e576-3efd-ba74-58f6b3251cf2 | -9.37789 | -68.78725 | 2025-09-23 05:40:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b79b477-2124-38d8-8be0-b8b7b96c0b18 | -10.10538 | -65.09042 | 2025-09-23 05:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ea124ee-f918-319d-9611-6bfadc3cf3f9 | -9.13284 | -68.17741 | 2025-09-23 05:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9219933c-fc86-37cb-ae31-ba3611b734d0 | -8.42974 | -70.1976 | 2025-09-23 05:40:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d4e832b-ba6a-3749-b5da-5c6e5fd3c269 | -9.55986 | -68.55946 | 2025-09-23 05:40:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9632b0c5-719a-38d3-8278-b285c5fce1b6 | -7.39603 | -70.10619 | 2025-09-23 05:40:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 253bca4a-43e2-3b0a-8e80-d2ecb8b32680 | -8.23868 | -70.81985 | 2025-09-23 05:40:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9617013-b5e5-31e8-8f6d-1c8e215b2479 | -10.05975 | -68.45869 | 2025-09-23 05:40:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b943ae63-2fef-3298-89ae-d0c09c222f7f | -8.42771 | -70.19857 | 2025-09-23 05:40:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c667ed3e-7a70-375e-bf82-5d974ec4b3eb | -15.31441 | -59.42291 | 2025-09-23 05:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50415a72-4317-3c7c-9b1c-5a8622ecbb49 | -15.35931 | -59.17678 | 2025-09-23 05:40:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a9b8a29-7475-3d69-a5a6-18290c87a93a | -15.35874 | -59.18125 | 2025-09-23 05:40:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abf9a962-ebd0-35fb-9609-22eb7bc66da4 | -9.88736 | -64.84249 | 2025-09-23 05:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bc80f86-cdfd-39be-886e-534d207b42d8 | -8.53162 | -67.06901 | 2025-09-23 05:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 958e8a01-4f73-3f4f-964c-ef84a8483ca5 | -8.43046 | -70.19355 | 2025-09-23 05:40:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 083ad013-f1a5-3b12-9b26-b2ff7812f676 | -9.14268 | -67.81509 | 2025-09-23 05:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50ea3c36-6738-3c6f-90a9-f7eec5befeda | -9.89181 | -64.83599 | 2025-09-23 05:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9bba92e2-07f2-37f1-b214-e3324b22b422 | -9.11255 | -68.31995 | 2025-09-23 05:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7601163-dee6-3220-8335-ccd55c5416cd | -7.25642 | -69.97321 | 2025-09-23 05:40:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3ef36a2-472b-376f-acb7-e3f5f2d02bd8 | -9.43736 | -68.93088 | 2025-09-23 05:40:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8cce8461-b665-3c98-a2dd-79465c9c3ece | -15.34754 | -59.19791 | 2025-09-23 05:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 212863cd-3d68-3608-a7c2-0ef3dc91bbed | -7.37717 | -70.13731 | 2025-09-23 05:40:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a020f120-a593-3d5d-8676-0d087fa830ee | -10.82159 | -61.42451 | 2025-09-23 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e9da620-f863-36ea-9527-4b5dbb5c3687 | -11.74403 | -62.51748 | 2025-09-23 05:40:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bc870d2d-9044-3b6d-924b-2edbc8a8e5a8 | -9.45136 | -67.14411 | 2025-09-23 05:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb8ce9f6-60d5-3de2-a248-f654c9e5d5e2 | -8.06899 | -70.47924 | 2025-09-23 05:40:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7deeb598-7ab4-39c4-8312-9a243fad384d | -7.98915 | -70.90437 | 2025-09-23 05:40:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f542d983-0489-313c-9415-e62f972e238a | -8.973 | -68.02376 | 2025-09-23 05:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25576467-9ec0-3fac-8814-22cac841f4db | -9.1434 | -67.81075 | 2025-09-23 05:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 619d8b87-1904-3a82-b56d-3da1a0b769f1 | -9.44336 | -67.42206 | 2025-09-23 05:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 450abb5e-743c-330c-8ec3-0fe46ed4ab22 | -8.0674 | -70.33611 | 2025-09-23 05:40:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13a4499c-cefa-3cc0-939b-c531761e231b | -15.34308 | -59.19724 | 2025-09-23 05:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9e6245d-705a-3923-925b-d964f6a49d63 | -9.65014 | -68.71517 | 2025-09-23 05:40:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f313e429-13d5-3516-9dbe-9bcec2bab6be | -9.52345 | -67.16322 | 2025-09-23 05:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0d4acf0-e0d5-310a-8de3-841ecabd1be3 | -8.3716 | -70.75835 | 2025-09-23 05:40:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03e7083a-5014-3404-8411-cf556a47b11e | -9.8704 | -66.69923 | 2025-09-23 05:40:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a8db8c2-6b1a-34e3-a5b9-4a2880dc75e6 | -6.42556 | -67.91744 | 2025-09-23 05:40:00 | NPP-375D | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7980a06b-7fbb-3622-9be2-44843c778607 | -6.39472 | -67.96106 | 2025-09-23 05:40:00 | NPP-375D | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0afecb2-eabc-3b80-8268-692a9ed38283 | -7.39676 | -70.10199 | 2025-09-23 05:40:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c594ba0-d326-3b56-a44e-75c4f6eda34d | -8.31804 | -70.93027 | 2025-09-23 05:40:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce40e518-9542-3018-91df-8dc51dcbe36c | -7.55621 | -70.00891 | 2025-09-23 05:40:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa36872c-8883-3d58-974e-ecaeadebdc65 | -9.92627 | -64.74804 | 2025-09-23 05:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ad98dd6-9575-3fcf-861f-a95e158eb04d | -9.92238 | -64.75101 | 2025-09-23 05:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1bf8628c-97b4-3ced-afbe-75ffdf790cc5 | -7.99327 | -70.90718 | 2025-09-23 05:40:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5c705e4-cc29-3aa9-baa6-a09849f14634 | -8.88596 | -69.23135 | 2025-09-23 05:40:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 945b4594-a527-3a36-aec3-10bb6a15bb96 | -7.98873 | -70.90638 | 2025-09-23 05:40:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 445981af-35f1-300e-b5d1-f85d82ada218 | -8.30079 | -71.13372 | 2025-09-23 05:40:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a29533f2-c394-33f4-a659-e914d7c08241 | -10.81793 | -61.42399 | 2025-09-23 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7516f04b-042f-31e3-a78a-f85e00d88111 | -10.8167 | -61.41272 | 2025-09-23 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 913d1109-60e8-3908-872a-27d789620394 | -9.79906 | -68.87936 | 2025-09-23 05:40:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed72b870-f7cf-317e-be71-0dc7adb9337a | -10.82221 | -61.42022 | 2025-09-23 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39355e16-a474-333e-bbd7-dbc7495bd29c | -8.02739 | -70.07693 | 2025-09-23 05:40:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f75be2fb-867e-3c07-bd6f-f5e5f2cb7876 | -9.9296 | -64.74858 | 2025-09-23 05:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2b327c61-ee01-3925-a05b-d780c007ceb0 | -10.70394 | -69.05296 | 2025-09-23 05:40:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1ad2693-030c-31e9-907b-616cf921fa22 | -9.44327 | -67.7552 | 2025-09-23 05:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da202586-52c4-3c7d-9416-ed51e75dbf97 | -9.55605 | -68.55879 | 2025-09-23 05:40:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 476d414d-c85f-3007-ab1b-5a5369f6ea11 | -8.88838 | -71.29026 | 2025-09-23 05:40:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39e85aee-eecf-3f04-8fbb-c34a481595ce | -15.31 | -59.42249 | 2025-09-23 05:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed8142b8-7b31-3e22-8216-63544d0c79fd | -7.77218 | -67.1409 | 2025-09-23 05:40:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2349962d-50a7-30e7-ae07-aab4c3c68d56 | -9.37679 | -68.81725 | 2025-09-23 05:40:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 047a4905-efcc-30dc-abc5-12d03026d0bb | -10.81606 | -61.41702 | 2025-09-23 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd3b1a50-8569-37c9-be71-e0a5bfdaecb4 | -9.47543 | -68.52546 | 2025-09-23 05:40:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89b0a24e-2bd0-3d8e-9143-2b26ebcaefaf | -8.4327 | -70.19527 | 2025-09-23 05:40:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33bb3384-6452-36f8-b3a1-fced3ad593a4 | -8.30462 | -70.84089 | 2025-09-23 05:40:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d940fae9-8bd0-3a61-b36c-c6db802b4dc6 | -9.88848 | -64.83546 | 2025-09-23 05:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2cbdce92-4610-3e96-ad1e-4aaef108db55 | -7.89222 | -70.17495 | 2025-09-23 05:40:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3a8555c-be8b-3a87-9408-b79f22a1956f | -9.19385 | -67.57277 | 2025-09-23 05:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6da2bb98-6559-3c56-bc7a-831fc9b388dd | -9.35292 | -66.50988 | 2025-09-23 05:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b5fd1d8-43e7-3a63-aaf5-17e6176298be | -9.28414 | -67.32164 | 2025-09-23 05:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc4d6f42-e589-32ce-9840-32c8d8ab951c | -9.44973 | -68.88218 | 2025-09-23 05:40:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e055775-71f1-38e1-a04e-b42519e4666a | -7.99324 | -70.85279 | 2025-09-23 05:40:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6966185d-e35e-36fe-85f6-b740f4a4696e | -9.28522 | -68.12249 | 2025-09-23 05:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README24.md)
