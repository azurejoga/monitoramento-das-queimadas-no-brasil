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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6c0fba5-b8fb-380a-829f-061b853d5700 | -11.14277 | -49.9063 | 2026-08-01 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 4b23d22c-8858-386a-8ca5-f44efb68faf2 | -14.06648 | -46.27252 | 2026-08-01 12:19:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 60.5 |
| fdd91661-b721-37eb-906e-b2d6ab1c10b6 | -7.90003 | -48.27496 | 2026-08-01 12:19:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 3d30d008-e96f-37ec-bf3d-e5c4ce59ca0d | -13.52813 | -51.50806 | 2026-08-01 12:19:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 26805be2-8379-31d8-ad76-e023be6ccd88 | -11.54694 | -50.14106 | 2026-08-01 12:19:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 0e3cebdf-379d-3603-b0f7-f26c3bf8dc25 | -11.76999 | -50.16974 | 2026-08-01 12:19:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 37.5 |
| c168df5f-0ba7-3bad-913d-2b7c04ee6673 | -13.33652 | -48.66077 | 2026-08-01 12:19:00 | TERRA_M-T | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 60.4 |
| d1ac7765-072e-3172-8883-a52f26d7505a | -11.25607 | -54.86071 | 2026-08-01 12:19:00 | TERRA_M-T | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 35b9b635-93b1-32b3-a1ab-d1150513e171 | -14.07602 | -46.24243 | 2026-08-01 12:19:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 03aa519e-cfe6-38ab-af07-a09f4383ebf7 | -11.77492 | -50.16462 | 2026-08-01 12:19:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| c693f487-720f-34f7-b3b3-da8a88bc5e77 | -11.94787 | -50.87455 | 2026-08-01 12:19:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 15.2 |
| a72d9dd0-852b-39f2-8bcb-128c9744bb15 | -11.76103 | -50.17982 | 2026-08-01 12:19:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 9b9fb8fe-71dc-386c-9d8c-3bad79275f92 | -11.77281 | -50.18127 | 2026-08-01 12:19:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| e263c6a4-e640-33f9-8f68-7083cb0c6722 | -11.24644 | -54.85285 | 2026-08-01 12:19:00 | TERRA_M-T | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| ef63d9ec-c5e5-3203-90fe-72017d5b3576 | -14.09804 | -46.25252 | 2026-08-01 12:19:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| fae84bb6-041f-3670-8a52-632d5cb3abbc | -11.24516 | -54.86188 | 2026-08-01 12:19:00 | TERRA_M-T | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 7c904bd5-a168-3fcc-8622-3c49fbb9f4c4 | -14.21749 | -57.40927 | 2026-08-01 12:19:00 | TERRA_M-T | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 961f5e59-7eef-3966-beb2-ad7039e76352 | -6.56363 | -55.15936 | 2026-08-01 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a881eb8b-55d0-33b3-9ecb-62306b96c67e | -20.60609 | -57.30435 | 2026-08-01 12:21:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 40408a90-dee0-300b-a9aa-23e5a9f19390 | -15.32795 | -50.8274 | 2026-08-01 12:21:00 | TERRA_M-T | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 2871c346-8b8b-378b-a297-0a5ce162ac1c | -18.49968 | -51.61963 | 2026-08-01 12:21:00 | TERRA_M-T | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 55775b96-bcc9-3321-b326-f1a1bd3cf602 | -19.43222 | -57.0706 | 2026-08-01 12:21:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 862ebae6-96e4-3c00-a5b8-3eb128bba9d6 | -22.28293 | -56.0014 | 2026-08-01 12:21:00 | TERRA_M-T | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4696096f-b0d1-34ae-be45-a92d79029b1e | -18.49779 | -51.63642 | 2026-08-01 12:21:00 | TERRA_M-T | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 1bc9b978-2be8-3684-87bc-c99c5837cf7a | -20.55831 | -57.31012 | 2026-08-01 12:21:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 77577225-19ed-38a6-8f59-974916c6e00f | -25.30559 | -53.18077 | 2026-08-01 12:23:00 | TERRA_M-T | CATANDUVAS | PARANÁ | Brasil | 4105003 | 41 | 33 | nan | nan | nan | Mata Atlântica | 20.1 |
| f1fe88fe-934e-3adf-a28e-89647092991e | -30.49947 | -52.63007 | 2026-08-01 12:25:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 13.6 |
| 4544ce11-cfc3-3685-b3e7-39ef6264967b | -30.49754 | -52.65237 | 2026-08-01 12:25:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 33.5 |
| d1c342c3-7c2a-307c-ad29-4b172700a12e | -14.0925 | -46.2637 | 2026-08-01 12:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 9ffd62a8-1f02-3300-9ddc-8f2745762892 | -14.0735 | -46.2439 | 2026-08-01 12:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 79aecb00-fba4-3777-98a3-469b3b3b8ab8 | -14.0925 | -46.2637 | 2026-08-01 12:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 9e36d49b-a19a-313e-b1d6-0a682e05d2b4 | -14.0925 | -46.2637 | 2026-08-01 13:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 0df35241-9af6-3693-ac54-fef846ab1f70 | -11.1539 | -49.9096 | 2026-08-01 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 9bf8845a-05f6-3707-a382-24f2c1dc5a22 | -14.0735 | -46.2439 | 2026-08-01 13:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 465899aa-6611-3317-82af-fddc413e41da | -11.1349 | -49.9117 | 2026-08-01 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 2575591e-054d-3f09-8081-7f9a3ff5ba9e | -14.073 | -46.2669 | 2026-08-01 13:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 4d3599ec-1b78-3f09-a5b0-22e54a9597ad | -11.1349 | -49.9117 | 2026-08-01 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 6866de3c-12aa-3bf9-9589-96f7f8cabdda | -14.0925 | -46.2637 | 2026-08-01 13:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 93351174-d175-3d9c-8af6-d2ce79641f69 | -14.0929 | -46.2407 | 2026-08-01 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| f4941540-482b-3831-99b0-eabf387f5dee | -14.0925 | -46.2637 | 2026-08-01 13:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 85.1 |
| a5ebc353-4525-3b47-8123-9b0bdfcf755d | -8.2 | -55.4443 | 2026-08-01 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| c46b8f55-953f-3073-ad8c-04fbe531e64b | -14.0929 | -46.2407 | 2026-08-01 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 1008505d-0c4d-3827-a589-6bf5d4e6b611 | -8.2002 | -55.4243 | 2026-08-01 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 514447bf-d81d-323d-ad39-0bb3fadf7b96 | -14.0735 | -46.2439 | 2026-08-01 13:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 8b58e052-0003-3d40-a8b6-d7bcc22a2cce | -11.1539 | -49.9096 | 2026-08-01 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| a173012a-c96b-33dd-83d0-f1460e4097cc | -14.0929 | -46.2407 | 2026-08-01 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 69eefdfb-561b-3c6b-ba9f-46197366b025 | -14.0925 | -46.2637 | 2026-08-01 13:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 0ab8a709-3253-3f69-be30-1791da3a6f1a | -11.1349 | -49.9117 | 2026-08-01 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| e5088b49-9050-3134-963e-c898d72f88c9 | -14.0735 | -46.2439 | 2026-08-01 13:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 135.5 |
| b333c383-4ce4-32da-bca6-e880c6811fdc | -14.0925 | -46.2637 | 2026-08-01 13:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 43866ebe-77ec-339c-b75d-4b684f6c7601 | -8.9681 | -45.1999 | 2026-08-01 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 57c9a4bb-14dd-34df-ad76-6b409c21bd2d | -14.0929 | -46.2407 | 2026-08-01 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 4cb397ec-b256-3c4a-9580-a604e1d4b56a | -11.1349 | -49.9117 | 2026-08-01 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| a19d55f2-85aa-33eb-9b61-1d9ebb04987a | -8.2 | -55.4443 | 2026-08-01 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| f1eeaa2f-d843-35ef-a635-b9d251dc6a39 | -8.1814 | -55.4455 | 2026-08-01 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 9acdfb71-e4b2-3cda-a978-a31deab4b8d4 | -11.1539 | -49.9096 | 2026-08-01 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 8a3be67d-fdce-3525-acb5-599d36440328 | -8.1814 | -55.4455 | 2026-08-01 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| f7e95162-e81c-3b02-ac3c-dd4219cd2418 | -11.1349 | -49.9117 | 2026-08-01 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 183.0 |
| df55eef4-47e4-3f2e-85fa-4e1002f96a6c | -8.2002 | -55.4243 | 2026-08-01 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| aa395b69-8375-3afa-8f99-8bff5d3e98f4 | -8.9681 | -45.1999 | 2026-08-01 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 191.5 |
| d5516c3b-d2c4-3e4e-b57e-b47c44ac5ddb | -14.073 | -46.2669 | 2026-08-01 13:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 1426a670-718b-345d-9689-5efd3249501d | -14.0536 | -46.2702 | 2026-08-01 13:50:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 72.3 |
| f499b0d6-ef89-3c35-a25b-9ecee17f25c7 | -14.0735 | -46.2439 | 2026-08-01 13:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 4b925482-b2fa-38b7-b262-f12e26146a6a | -11.1539 | -49.9096 | 2026-08-01 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 155.9 |
| 670282b7-b1fd-38b7-8611-c0f99ca94c24 | -8.1816 | -55.4255 | 2026-08-01 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| c1ac9660-9b8d-3eb6-b117-ba164199fac5 | -8.2 | -55.4443 | 2026-08-01 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| c6e95c12-3973-3d22-8b12-b9b40618cd8a | -14.0929 | -46.2407 | 2026-08-01 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 27b261da-15af-3c6d-8f90-ec5d17ebdc75 | -8.2002 | -55.4243 | 2026-08-01 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 142.6 |
| 09239f27-8c10-3e0e-9371-12da8c5a20a0 | -8.1816 | -55.4255 | 2026-08-01 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| d747ce54-f11d-3bf3-a996-990310848e6a | -11.9567 | -50.8676 | 2026-08-01 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 8466d171-19fc-348e-9d05-1808b41dd839 | -11.1349 | -49.9117 | 2026-08-01 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 6e637fac-5111-33dd-9008-13ba07fbdb3d | -8.2 | -55.4443 | 2026-08-01 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 211.8 |
| 904544fb-dccb-39e3-a719-51b6b980a205 | -8.9677 | -45.2227 | 2026-08-01 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 87cd965d-bc62-3999-8fa0-aaceb039b207 | -11.2402 | -54.8534 | 2026-08-01 14:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 714c59f6-0e6d-3c01-9cfd-82eb4fb5ebc7 | -14.0735 | -46.2439 | 2026-08-01 14:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 89.3 |
| b05d01e9-5cce-3bee-8506-bfde95bd30cf | -8.1814 | -55.4455 | 2026-08-01 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 62f30dae-87a8-34ab-965f-28530305ffa8 | -8.9681 | -45.1999 | 2026-08-01 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 172.4 |
| b70a3212-4178-3ad5-9154-30f93039879f | -11.1539 | -49.9096 | 2026-08-01 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 168.2 |
| e5f50219-2cae-3e16-9d4e-df1356c30b8d | -14.073 | -46.2669 | 2026-08-01 14:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 85e220ec-9781-3b9e-bc3f-26ef64f8b851 | -11.2402 | -54.8534 | 2026-08-01 14:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 7d0890d0-5f5b-3689-bdb5-928a5a5847b4 | -8.1816 | -55.4255 | 2026-08-01 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| a59f8810-1191-3224-bd44-de33471271ec | -11.1349 | -49.9117 | 2026-08-01 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| c876b94a-e66e-3349-b5d1-0d32f7c0e362 | -14.0735 | -46.2439 | 2026-08-01 14:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 77188a24-f555-397c-a8f2-df18aa40d246 | -8.9681 | -45.1999 | 2026-08-01 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 76964522-e149-3e0e-89ba-2ddae6f86941 | -11.2591 | -54.8517 | 2026-08-01 14:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 6f37c6c8-5349-37ce-994a-e83d137dea7c | -8.2002 | -55.4243 | 2026-08-01 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 145.1 |
| 6fd37fdb-a07b-3fc2-8652-7a3a75e4dc10 | -14.0929 | -46.2407 | 2026-08-01 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 1f03affc-57bc-3428-9ac1-20086e932885 | -8.1814 | -55.4455 | 2026-08-01 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 149.3 |
| 74d0a8eb-34ca-3024-bdd9-aca963dbf1f4 | -11.1539 | -49.9096 | 2026-08-01 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| ec67f036-a10d-3165-9c22-de70ab35de56 | -13.53 | -51.53 | 2026-08-01 14:15:00 | MSG-03 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 628f414c-6eeb-3ef5-9004-c138b0977d94 | -11.2402 | -54.8534 | 2026-08-01 14:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 158.2 |
| 3c567a2e-2e8c-3418-976c-2acf663b6793 | -11.2399 | -54.8737 | 2026-08-01 14:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| dc416748-c4e7-3f5f-97ab-d53b6402d96c | -14.0929 | -46.2407 | 2026-08-01 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| c66a6021-91ce-332d-85be-408e75a3e2b1 | -14.0925 | -46.2637 | 2026-08-01 14:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 5255bc65-b89c-3a0a-a570-45aa3507292f | -8.2002 | -55.4243 | 2026-08-01 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 211e18d9-ca2d-30b7-b403-b95ff9b6b519 | -14.0536 | -46.2702 | 2026-08-01 14:20:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 0e4c1a1c-6201-3009-8da4-80fda6a63596 | -14.0735 | -46.2439 | 2026-08-01 14:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 00889e29-c73b-34c5-bb7d-c19221326659 | -11.2588 | -54.8721 | 2026-08-01 14:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 7d87ed72-3dba-393b-a4aa-91c7b81c1f40 | -14.073 | -46.2669 | 2026-08-01 14:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 01e187ab-ea93-3ed3-a689-528a8cdf9957 | -8.9681 | -45.1999 | 2026-08-01 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 209.3 |


[Clique aqui para ver as próximas entradas](README27.md)
