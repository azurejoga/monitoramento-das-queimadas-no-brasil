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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68867723-2e5c-3e0c-a445-39af9ca9c1a0 | -17.99765 | -57.43227 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 64e8c705-29d7-3fd5-b770-560ed7d9811e | -17.99697 | -57.43615 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7b395bac-4237-3fba-89e6-c4165bbeb465 | -17.99163 | -57.43081 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 13066add-ef4e-36c6-a91e-a2659810b0b2 | -17.99095 | -57.43464 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 809ea9f2-575f-3ebe-a59e-34ebb0d9fd9c | -17.99058 | -57.43552 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a368c8a0-8ca6-317b-9400-476b965ddf54 | -17.93334 | -57.4656 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8c4914d1-c3ff-3559-b44f-74dfb425b24c | -17.9273 | -57.46412 | 2024-10-21 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| fef11995-fff7-3609-81c6-df826b556269 | -17.69186 | -57.4359 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| cf95495e-3ed3-3b4a-a571-b29a72de2d9e | -17.8022 | -57.48195 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2f09f468-250c-316f-8025-dff58e7f65d7 | -17.80114 | -57.48676 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 01e7faa1-d023-3df1-8d59-43ad9b87895e | -17.80007 | -57.49157 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9ee4d10a-b08e-37df-b9f6-c20de28368b2 | -17.79508 | -57.48527 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b7965234-a2b1-389d-bbf7-e7eb4c661b4c | -17.78795 | -57.48859 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 277a2145-55b2-3894-ae41-1b01fab34fc1 | -17.78296 | -57.48228 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 3fb71be0-9a50-3884-92bc-086e2f460e9d | -17.78189 | -57.48709 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f8ba15c7-4b63-3f36-ae18-755a0cca3088 | -17.77084 | -57.47929 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 60fa4661-4c05-3e4a-9ebc-5d71126c23ca | -17.76977 | -57.48409 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a2618c3d-3cb4-3fa6-b37c-ef32e48b0f50 | -17.76454 | -57.56479 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| eed5e093-77f2-3096-8a8f-369cfec6190d | -17.76345 | -57.56968 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9a43c4aa-7fb1-3e7c-a688-7689af51fbca | -17.73392 | -57.47689 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ee506e7c-4aca-30e8-9d8c-69fdfc1a3089 | -17.73339 | -57.47517 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d5a0e8b4-7541-3135-91e9-46a4e8da3002 | -17.73231 | -57.47998 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b2070cde-d1b6-352b-b41e-6a25304adf3d | -17.72786 | -57.4754 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a5f2bfa6-03a8-3fdb-b408-d89225dd2787 | -17.71787 | -57.4627 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| dda5133a-10f0-3e10-92e8-0e76f0ad30bd | -17.71681 | -57.46754 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 3fc0a098-e16d-3c2e-a5a1-ebc7690b0b70 | -17.71288 | -57.45637 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| ef3816c0-35f6-37d8-8d25-4eb004336ff9 | -17.71181 | -57.46121 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 48f9fa8c-5508-352f-ad6a-b2073e537f2f | -17.71074 | -57.46603 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 639dfdb9-0eb9-3d38-83bd-d7031b7673b7 | -17.70682 | -57.45485 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 073d0958-e190-34ee-bf35-d9b5717e312a | -17.70575 | -57.45968 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 0e1dd374-3f71-3d7e-97f9-0d2b55a6f873 | -17.70469 | -57.46452 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 35ca84e2-d929-3c9c-b0ec-17441ad60f8d | -17.69293 | -57.43108 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 8313f534-5dc5-35c7-8ecd-eaf99d49eb61 | -17.68688 | -57.4296 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 590ecac6-2e52-315d-b092-65fd64466452 | -17.68083 | -57.42811 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 26e5732b-9f32-3c3f-962d-331c82424213 | -17.25078 | -57.30331 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| fa38dd38-edc0-3439-8697-921d6ed2a909 | -17.25039 | -57.30585 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b92be7ee-6380-3eef-a193-107a93469408 | -17.24971 | -57.30812 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 5c229c8b-d790-3262-a3c3-ed317c18ad96 | -17.24935 | -57.31067 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| b1ef8765-22e7-3bd3-b999-c7833f968eed | -17.24863 | -57.31294 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a75082bf-8446-3cba-8eb6-157719ba674e | -17.02312 | -57.32927 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| fbbead70-256c-3b7a-9af5-812a66705947 | -17.02206 | -57.33416 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| a243f613-633b-3fd3-b283-7e093e57c004 | -17.0219 | -57.33091 | 2024-10-21 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| a4569eb8-b98f-37db-92a1-b301ed65b12a | -29.81269 | -51.17768 | 2024-10-21 04:19:00 | NPP-375D | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 19dc69f0-3c86-35ae-9718-67e333c21f54 | -24.23724 | -50.26051 | 2024-10-21 04:19:00 | NPP-375D | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3cb7f871-8d88-35b4-930d-fa088dbcdec4 | -23.10509 | -52.09436 | 2024-10-21 04:19:00 | NPP-375D | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0d767f0a-0e14-338a-aac7-1d9e93c67acb | -23.10278 | -52.09544 | 2024-10-21 04:19:00 | NPP-375D | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 8a613121-cd48-3f84-9a49-59dc6a99bc72 | -21.37848 | -55.70639 | 2024-10-21 04:19:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 11142175-aa0e-354a-81d1-29b3041489fb | -21.37772 | -55.70998 | 2024-10-21 04:19:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d45d5835-79b9-325c-a82a-2355a593fcc1 | -21.37698 | -55.71346 | 2024-10-21 04:19:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f184c53-335e-3f25-ac8f-c7ebb6d3bbd5 | -1.1834 | -53.6368 | 2024-10-21 04:25:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| c6f72e28-5b77-33f5-aa3c-0bddb236ff04 | -1.1835 | -53.6166 | 2024-10-21 04:25:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 3ba129d5-b744-3985-b294-d6844348bc08 | -1.2018 | -53.6366 | 2024-10-21 04:25:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 763b3267-4d32-357d-8e59-bcde04fd44e5 | -2.4824 | -49.102 | 2024-10-21 04:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 7c2b7f74-afe4-3107-afbe-63a1c5b0f289 | -2.7885 | -51.3618 | 2024-10-21 04:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| acd5906d-341e-35b7-bb67-aeccf24c8854 | -2.7773 | -49.3067 | 2024-10-21 04:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| cae2932f-1416-398a-9b10-47075fa00a11 | -2.8069 | -51.3613 | 2024-10-21 04:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| ba61d23b-f580-34f3-ac9c-a7e963f364c0 | -2.8556 | -53.3256 | 2024-10-21 04:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 8c90f8ab-c0c6-313f-8c0c-8fdeb7d72d29 | -2.905 | -45.2143 | 2024-10-21 04:25:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 63.3 |
| d18afc02-487e-371c-b519-5ea9e66d28ca | -3.1138 | -53.1163 | 2024-10-21 04:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 2f1ebeb0-3d28-3571-993b-cead5eb1421a | -3.2146 | -50.8093 | 2024-10-21 04:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 06566018-90b1-3242-b354-539ce0c65b71 | -3.2147 | -50.7884 | 2024-10-21 04:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 8b7cc2ec-9582-3d84-8879-d2ad6d97c86c | -4.2544 | -43.7149 | 2024-10-21 04:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 35dc42a8-4aaf-3c21-8d0b-8536b784555f | -4.2356 | -43.7391 | 2024-10-21 04:25:30 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 5fc40b8e-aa34-368d-8d71-04c1d2a3fc6b | -4.2357 | -43.716 | 2024-10-21 04:25:30 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 0ee36614-5d2f-3759-916e-a1723dc329d7 | -5.6894 | -46.435 | 2024-10-21 04:25:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 545316e3-a182-34ba-a284-41aea4da5328 | -12.5147 | -63.3014 | 2024-10-21 04:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 36.1 |
| e93ac2a7-aaf2-32aa-9b2e-f749a45c26be | -12.5336 | -63.3003 | 2024-10-21 04:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 891116d5-fba6-32bc-8b21-b2d0659d3c7a | -18.2828 | -56.0994 | 2024-10-21 04:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.0 |
| c4ab0050-5653-3d3c-a652-ed4dbd561978 | 2.3964 | -50.94839 | 2024-10-21 04:34:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93e42908-0fd9-3589-956b-f42cf81036e3 | 2.39574 | -50.94408 | 2024-10-21 04:34:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e940104-8931-3978-9236-0f4166c97479 | 2.1047 | -50.65403 | 2024-10-21 04:34:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 93218dca-c867-38d0-986b-e056c54247c1 | 2.10407 | -50.64989 | 2024-10-21 04:34:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7f5e86f2-3b43-3052-bb3f-6d4c45341d61 | 1.83454 | -50.49106 | 2024-10-21 04:34:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 24b2b856-1888-350f-a142-4956c3178e94 | 1.83162 | -50.49565 | 2024-10-21 04:34:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 60d4b448-8217-3ed4-bfbf-c992c75f5114 | 1.83098 | -50.49162 | 2024-10-21 04:34:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 15.8 |
| edd45440-5bc7-38ca-bce0-212a74f4cd8f | 1.81549 | -50.48577 | 2024-10-21 04:34:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8ed4158-51ca-356e-b71d-9e230f171115 | 1.81193 | -50.48632 | 2024-10-21 04:34:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| becfb73d-e136-3421-ae66-4105cb33095f | 2.91657 | -51.00183 | 2024-10-21 04:34:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 14af83b2-532a-3609-a54f-e21f06925971 | -1.1835 | -53.6166 | 2024-10-21 04:35:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| a6c5f4f6-34b1-3cf4-be5a-27280f15237f | -2.4824 | -49.102 | 2024-10-21 04:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 2b425536-a12f-33fc-861e-e1ef3bd9839d | -2.7773 | -49.3067 | 2024-10-21 04:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 1a0a57f0-2d52-3590-bce5-f759f4e041cd | -2.7885 | -51.3618 | 2024-10-21 04:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 5bc01658-ebed-3296-a945-acb8dac78d50 | -3.1138 | -53.1163 | 2024-10-21 04:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| c9ea3037-2c07-3d41-b521-98b7e3077699 | -3.2146 | -50.8093 | 2024-10-21 04:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 55adbc2d-6661-33e0-8500-f44d4d2b33f3 | -3.2147 | -50.7884 | 2024-10-21 04:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| ebebee6e-df9f-31e2-821b-6efc0964784a | -5.6894 | -46.435 | 2024-10-21 04:35:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 009c7c70-22ee-30cd-ab2b-f3e8a7bd0f74 | -3.90583 | -48.36473 | 2024-10-21 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64dff600-b9aa-3277-b8d6-86a8c7739155 | -5.03395 | -40.9104 | 2024-10-21 04:36:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 09eb68e4-a28a-3c94-8a8b-3661a8d7ff4a | -5.03382 | -40.90857 | 2024-10-21 04:36:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 044f78af-0b1c-3ace-a6f1-53265e7a1f55 | -4.34172 | -42.562 | 2024-10-21 04:36:00 | NOAA-20 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 33356213-5acd-31b5-969d-8b72d184b387 | -4.3373 | -42.56132 | 2024-10-21 04:36:00 | NOAA-20 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| ee942abb-fd61-3618-b261-f44ae0a603bb | -3.63846 | -43.12389 | 2024-10-21 04:36:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23e37e69-24d1-33a6-922a-9f42e498b646 | -3.63786 | -43.1278 | 2024-10-21 04:36:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd10067a-f8c9-307b-8913-74dc85dd283a | -2.96146 | -44.30864 | 2024-10-21 04:36:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9bd4076f-6de2-31c7-83ff-36c5078b7211 | -3.65431 | -43.7229 | 2024-10-21 04:36:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb6e096a-6716-35a5-80fe-f88abbb5acc3 | -3.65378 | -43.72252 | 2024-10-21 04:36:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ebea1173-021f-3a8c-8e18-9f8a4fcc7c03 | -3.65027 | -43.72227 | 2024-10-21 04:36:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b825a379-5cbc-3871-83ab-dd1687fc8723 | -3.64973 | -43.7219 | 2024-10-21 04:36:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f76cdff5-03f5-3fce-a72b-7574b998f564 | -4.24433 | -43.72517 | 2024-10-21 04:36:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d9399aa8-6443-3672-ac09-f1f86c90e41b | -4.24377 | -43.72889 | 2024-10-21 04:36:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README34.md)
