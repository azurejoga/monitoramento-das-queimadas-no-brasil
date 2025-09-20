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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e660ec6-8247-3c94-8a70-8c439d0e76bb | -7.7336 | -44.3902 | 2025-09-20 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 315.3 |
| cb65908f-5006-3800-a1da-187bf7cc746d | -7.3366 | -44.5663 | 2025-09-20 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.9 |
| a00cb335-cdbb-388b-b6d2-497ddddcc74b | -7.3551 | -44.5875 | 2025-09-20 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.2 |
| f6f3302c-9974-34b6-a99f-3ed62dc34d51 | -7.3739 | -44.5857 | 2025-09-20 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 110.0 |
| ea29c2cb-cdee-3fef-98db-7636043e2b7a | -4.0707 | -40.4698 | 2025-09-20 12:50:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 80.4 |
| f31d3610-970f-32ad-8c5f-778fe0504318 | -6.077 | -41.0013 | 2025-09-20 12:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 299.7 |
| 09861733-d994-32e1-9e9c-4f28b5f8348e | -2.42908 | -49.34346 | 2025-09-20 12:53:00 | TERRA_M-T | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 3c0cecdf-fba1-3668-b69d-a65947957f0d | -1.80706 | -54.46862 | 2025-09-20 12:53:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 85e20f44-d373-301d-b71c-3bdf8dcbdeb3 | -2.4318 | -49.32419 | 2025-09-20 12:53:00 | TERRA_M-T | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 3272756b-1410-3220-b68e-9c1aef14e7a7 | -5.60549 | -52.15676 | 2025-09-20 12:55:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 36bb0fa0-38a2-34d9-b331-88b1ac77d0bd | -3.7996 | -55.69058 | 2025-09-20 12:55:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 12331080-79c4-37d5-8ec1-20e368897263 | -3.46185 | -51.21349 | 2025-09-20 12:55:00 | TERRA_M-T | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 68f3231a-0054-31d7-9fba-bc7ced206c01 | -5.6073 | -52.14357 | 2025-09-20 12:55:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 37abffa9-f9c1-391c-8d29-f41147e568d4 | -4.23099 | -55.70959 | 2025-09-20 12:55:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6a065f51-3ae9-3baf-95df-2e83d36b31a1 | -2.51424 | -51.90552 | 2025-09-20 12:55:00 | TERRA_M-T | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3618facf-8a50-3873-8713-8c6eecc529e6 | -10.24043 | -48.0667 | 2025-09-20 12:57:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 87011f6f-93ec-37ef-bf44-da0d91f217f6 | -9.40646 | -54.68116 | 2025-09-20 12:57:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 86d391b1-120e-380e-90e2-75a1449e7d38 | -9.35966 | -54.52613 | 2025-09-20 12:57:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 86c029ec-5d02-31e8-b4fb-257b5d64fa2d | -12.46748 | -58.56069 | 2025-09-20 12:57:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 69eb4aed-3b6d-31d6-ad1e-605de51f30f8 | -10.23733 | -48.03801 | 2025-09-20 12:57:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 2ce4d272-9eb1-362d-8e0b-6fea22a2e869 | -6.21514 | -55.30512 | 2025-09-20 12:57:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9d45ec6e-7470-3a2a-a785-cfcb287b486f | -10.24453 | -48.03166 | 2025-09-20 12:57:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 43.4 |
| f2ac9da2-6cd9-31f2-84ca-ab86031979db | -9.35471 | -54.53017 | 2025-09-20 12:57:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5cd4c8aa-3817-325a-9260-8eb5a8a4507d | -6.3381 | -56.18293 | 2025-09-20 12:57:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 95544bad-8f1d-3df4-a90a-79b46d9868d8 | -9.40503 | -54.69148 | 2025-09-20 12:57:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 7f05a544-f17c-38b7-8f65-d6c10b053088 | -9.35616 | -54.51977 | 2025-09-20 12:57:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 11256171-abd6-3654-a7d5-93f5d381f83c | -9.71117 | -61.28912 | 2025-09-20 12:57:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 2dd072c6-2278-397c-a095-e0cf0209165d | -10.23345 | -48.07352 | 2025-09-20 12:57:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 518aa15c-ff56-3670-943e-c58e0021d222 | -8.9844 | -65.4198 | 2025-09-20 12:57:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 84641111-51df-3ee7-9ed0-f8b1f449494e | -16.48168 | -55.13675 | 2025-09-20 12:59:00 | TERRA_M-T | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 23.8 |
| 81e795b8-d134-314b-a88f-2c9ca4805fd9 | -15.29043 | -56.85964 | 2025-09-20 12:59:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 43.7 |
| f32666d0-e963-3c8f-be1e-af1e4178598d | -15.31374 | -56.81994 | 2025-09-20 12:59:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6b8e38a2-8fe9-3517-b731-5fa4d5250bb6 | -15.69518 | -53.62382 | 2025-09-20 12:59:00 | TERRA_M-T | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 72b3a7fc-fb99-3bf8-9adc-45dd46bcc057 | -16.48012 | -55.14911 | 2025-09-20 12:59:00 | TERRA_M-T | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 19.1 |
| f10bd98b-c7bf-3976-83d5-9922da94965b | -15.76886 | -59.38423 | 2025-09-20 12:59:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e21344c8-bd22-34ec-a7ce-630a31e971ed | -14.81813 | -60.23678 | 2025-09-20 12:59:00 | TERRA_M-T | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 841c3967-63dc-32db-8dd0-8fe8d913a2d0 | -16.96916 | -49.73904 | 2025-09-20 12:59:00 | TERRA_M-T | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 543516b5-13c8-30ae-88bc-08608b59463e | -15.91812 | -59.43213 | 2025-09-20 12:59:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 7e7d40d0-28ab-381b-93e8-e21ed4659ce5 | -19.61206 | -57.74539 | 2025-09-20 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.3 |
| 06b8f8db-1c79-3a6f-a614-4c27dd553097 | -15.28133 | -56.85842 | 2025-09-20 12:59:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| a05bc9e5-8480-3b92-94dc-2738c793c0c2 | -15.28665 | -56.8199 | 2025-09-20 12:59:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5d8510de-92ec-3e0e-9290-64e150817814 | -15.28002 | -56.86794 | 2025-09-20 12:59:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f12cfd92-04a9-3fe9-a12c-7f7753b99fd6 | -15.90437 | -59.40141 | 2025-09-20 12:59:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 1a3bc468-f761-3fd6-a053-34bdfdf30bb1 | -15.69701 | -53.60898 | 2025-09-20 12:59:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 0c6b64f3-70af-3b73-adf3-c3a70552fa65 | -15.28911 | -56.86923 | 2025-09-20 12:59:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| fe888d2e-49a5-3fc2-ba9d-35f278b41742 | -16.10716 | -53.81125 | 2025-09-20 12:59:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 29.2 |
| e1e915f5-0d04-34d2-9e54-0bc4eef302fe | -15.9195 | -59.42282 | 2025-09-20 12:59:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 934269be-762a-3bd6-960d-14701ec26868 | -16.9685 | -49.71461 | 2025-09-20 12:59:00 | TERRA_M-T | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 5091dbdd-2f77-3138-9d4f-ede410397a6f | -16.10889 | -53.79702 | 2025-09-20 12:59:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 89be2bf0-1466-3ced-9da1-e4e1aa2c27db | -15.27359 | -56.84736 | 2025-09-20 12:59:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 4505110e-8dce-3ea9-84d1-0ea7ba94213f | -15.30595 | -56.80891 | 2025-09-20 12:59:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 36e19590-9eb0-3583-aa3a-d6b956d8321d | -16.47156 | -55.13554 | 2025-09-20 12:59:00 | TERRA_M-T | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| d4673265-4e07-3528-bb82-5ed158d1a2bf | -16.97232 | -49.70853 | 2025-09-20 12:59:00 | TERRA_M-T | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 30.6 |
| ef3ea5df-7ac4-3367-93e7-9f9572a46d6c | -15.77707 | -56.59937 | 2025-09-20 12:59:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6d8832db-7cf9-373c-a50d-0d8480a726b1 | -4.0707 | -40.4698 | 2025-09-20 13:00:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 112.2 |
| 2c50d7ce-2293-3e1f-92d2-0184cc0aadba | -7.3368 | -44.5433 | 2025-09-20 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 629739f4-fc1e-3be9-b565-0d5d3ad80864 | -6.077 | -41.0013 | 2025-09-20 13:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 254.5 |
| bf794041-9803-31c3-b3b2-2ad258a80652 | -15.2783 | -56.8555 | 2025-09-20 13:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 57e0704d-57d4-37d2-b330-46702e93bda8 | -7.3554 | -44.5645 | 2025-09-20 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 123.4 |
| f6a89e95-efe3-3044-a31c-98842fa2c689 | -15.2976 | -56.8535 | 2025-09-20 13:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 05877410-32db-3762-a910-78231ceef966 | -19.6073 | -57.7531 | 2025-09-20 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.5 |
| 4563fa20-13d2-3376-83e7-f4562769dcaa | -6.077 | -41.0013 | 2025-09-20 13:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 839.1 |
| 640fec5a-cf78-3fd8-a229-cdd25fd60050 | -19.6274 | -57.7504 | 2025-09-20 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.9 |
| fe92195f-dd1d-3d9f-b2eb-db82e4e416fc | -15.2783 | -56.8555 | 2025-09-20 13:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 14277d7b-54f6-354c-8439-b5fef08d5d82 | -7.6079 | -45.4977 | 2025-09-20 13:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 903cfe94-9885-3546-8905-4ac011b7bd27 | -15.2783 | -56.8555 | 2025-09-20 13:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 401c1d30-6b8d-397a-9b36-e67875c66033 | -5.79 | -43.4738 | 2025-09-20 13:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 33468063-fe02-3bbc-be25-7ecece15a5d7 | -6.077 | -41.0013 | 2025-09-20 13:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 758.6 |
| 9d2431f3-466c-32a1-ae00-d93c69cc823e | -8.4837 | -44.7036 | 2025-09-20 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 4165f62b-c1e3-3f4f-b1ef-0f54c092797b | -6.3261 | -42.3959 | 2025-09-20 13:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 76.1 |
| 0559323a-a9a4-3fe3-8787-bc7909cc0b54 | -5.0635 | -43.0131 | 2025-09-20 13:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 8ac9af9f-817b-3e2f-97d4-90133dab54b3 | -19.6073 | -57.7531 | 2025-09-20 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.5 |
| d261c0a1-40aa-3dba-8eaf-5366f8f5efbc | -15.2976 | -56.8535 | 2025-09-20 13:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 64.1 |
| cd458a20-e6ce-3d0a-8ee4-2583f8ed7f96 | -9.6287 | -46.6394 | 2025-09-20 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| ac6117b6-6edc-3c01-a776-dee5840653d4 | -6.077 | -41.0013 | 2025-09-20 13:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 517.0 |
| 613df559-14d5-38b6-9761-1c3fab4873c7 | -9.0286 | -46.3243 | 2025-09-20 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 169.3 |
| a6b2491d-fe00-3daf-a653-4f802316f2e4 | -9.0097 | -46.3264 | 2025-09-20 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 314600bd-1357-3a78-92f8-5405be8c546a | -5.8088 | -43.4724 | 2025-09-20 13:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 2684c9f5-3a12-354a-b0b9-e4afd8f1f1b4 | -8.6502 | -46.431 | 2025-09-20 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 17015c3c-29ef-3fbc-a61e-783ed499bfcf | -15.2783 | -56.8555 | 2025-09-20 13:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 53fc76ca-3e6c-3e27-8ed7-c9623f91a9bb | -8.4837 | -44.7036 | 2025-09-20 13:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 107.4 |
| bd37ff5a-d5e6-321f-9b64-25710910696d | -19.6073 | -57.7531 | 2025-09-20 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.6 |
| b176c679-fa79-3722-ad2e-09d8d0c81691 | -8.6502 | -46.431 | 2025-09-20 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 652d558b-2b1d-333e-bbe8-f685305b48a2 | -9.0286 | -46.3243 | 2025-09-20 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 7f20014c-6319-38e1-bc30-3fd9e4ebdef7 | -16.4711 | -55.1301 | 2025-09-20 13:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 76.1 |
| bbd746a8-ef4d-375a-96e8-1d5c83d3560f | -8.6687 | -46.4515 | 2025-09-20 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 3344818e-f355-35d1-9df7-a2bc325d45d2 | -6.077 | -41.0013 | 2025-09-20 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 494.3 |
| 2215a949-6aaa-3729-800b-1234bc0f7ab4 | -8.4834 | -44.7266 | 2025-09-20 13:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 8b3d46c6-71ad-399c-88c3-8007d4c4a15e | -5.8088 | -43.4724 | 2025-09-20 13:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 1bbccd49-6ad8-31ce-9296-8ed05f3e23f9 | -6.077 | -41.0013 | 2025-09-20 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 323.0 |
| 6e947812-48fa-3f4d-afd3-4fbfe63e3d84 | -17.445 | -44.7922 | 2025-09-20 13:50:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 99.8 |
| b90ef9d6-cf09-3535-aeef-43effdc2c0c3 | -8.5759 | -46.349 | 2025-09-20 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| a1ca0033-42af-34a2-81a6-d7082a0d50c0 | -8.6885 | -46.3823 | 2025-09-20 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 29cb80ae-af78-3476-9525-44b69e1670d1 | -9.0286 | -46.3243 | 2025-09-20 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 200.5 |
| fc261005-2258-3e14-81a6-60df361b12e4 | -5.7885 | -43.6366 | 2025-09-20 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| d144f94e-149a-3119-bdd3-8c6639f0ba4e | -5.79 | -43.4738 | 2025-09-20 13:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 9d1e6544-eaa9-3370-972e-0e59b81fa8cc | -8.6502 | -46.431 | 2025-09-20 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 4f662265-229f-3c87-9236-1870045c9d86 | -8.6499 | -46.4534 | 2025-09-20 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| dd0c5b07-8885-34d9-a5a9-2385f81489d2 | -19.6274 | -57.7504 | 2025-09-20 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.4 |
| 53597c9f-8353-31b5-a6f0-c3d8a7579b55 | -19.6073 | -57.7531 | 2025-09-20 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.7 |


[Clique aqui para ver as próximas entradas](README31.md)
