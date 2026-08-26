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
| daaf3f4d-1516-3c3b-b0f3-90cee467f745 | -6.12748 | -57.81386 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3e856cf-c6bd-35ec-94b6-a1a24da30da2 | -8.60024 | -54.86329 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 147b856c-3bd2-3590-ba34-4fbd2bbb316d | -5.34145 | -45.16693 | 2026-08-26 05:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 04b860e4-7c1c-3408-88f2-a3b0c63fe3fa | -8.07922 | -45.90277 | 2026-08-26 05:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2cd0c3e-d2f4-3008-b40e-8a07b59f4b55 | -7.38994 | -55.16737 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75f80cf3-d660-341f-88c4-6fba54c88e49 | -7.49573 | -55.36594 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf91234e-b8d4-3515-8502-54875526514a | -6.30632 | -53.56934 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92186211-8eb0-3aef-88c4-4453ec20ba8f | -5.56122 | -50.48864 | 2026-08-26 05:27:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a0089aea-76da-3ebc-91e4-34aa463f775a | -6.6368 | -58.51384 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d5d96219-a962-3f22-91dd-1a57e3340a0d | -5.7765 | -57.55453 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c76e2be8-75a4-38dc-8d1a-70ab363e5693 | -7.02543 | -59.22748 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe81b747-84f5-3657-9514-f0985f03804e | -8.52586 | -55.31721 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23f4e930-cc36-33bc-add5-5a560c895452 | -6.14984 | -53.6892 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f153279e-a9b6-399f-982c-ecb2f1ce7e48 | -6.14456 | -59.91307 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7beb5c23-24c6-350e-8e28-538376d9f9bb | -5.94461 | -57.73112 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16e390cb-465b-373c-940f-8adf17afdc02 | -8.1351 | -47.50135 | 2026-08-26 05:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f92e6e60-ed87-3230-bd7f-fc9f0e228e26 | -6.64177 | -58.50389 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 70ad5564-c2b9-3907-b654-beefe7ff53c9 | -8.27072 | -55.53854 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2740fb3-1ea8-3571-89a7-730478e38901 | -7.03097 | -59.23548 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e21c36d-e0f0-36c9-8da4-717ab4d97e17 | -6.41195 | -60.05661 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b0be4aa-dd6b-32ff-b90d-f3b89e20d4b0 | -6.64898 | -58.50145 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 34153460-5cb7-3de8-86c1-b9474a4ef68c | -7.37565 | -55.18488 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44b6358d-3658-38d6-a282-d1a3a3b706f8 | -8.62631 | -54.70019 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ab436a9-0c31-35ba-8694-bb5c818e0581 | -8.01324 | -51.79192 | 2026-08-26 05:27:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e0d1ea6-9968-30a1-8531-7f1bc496b296 | -6.63347 | -58.51332 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6fad59c0-586b-3758-95e0-dffef8bd1271 | -8.62157 | -54.70477 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45103e46-dfe4-32e5-837f-8965ed773052 | -8.01347 | -51.82536 | 2026-08-26 05:27:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f809aa53-4a0b-3fd1-a334-9320963acaec | -6.95303 | -59.08816 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1653a0a-0e07-31cb-b7ab-58e8f5569f6e | -8.52815 | -55.31563 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9bd6ee63-919f-35f2-8877-fcaeaeb76ccb | -6.26366 | -55.41149 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54c23cc4-123b-3498-8070-d2c6cb890ae7 | -7.06255 | -59.22691 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f41ad3a6-7131-3de3-bd9f-d0a5e2cf0050 | -7.55535 | -61.41302 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcb737ca-3016-3ed9-9208-617924a03b17 | -5.94405 | -57.73471 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6c1312a-6300-39d0-a8bc-5764187812b8 | -7.47495 | -61.37339 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ee0d89d-3d15-33a6-b180-de0fcaf573bf | -3.13023 | -61.19306 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 46c4a6de-41c7-354d-b027-7d7cbb3b8a2d | -6.61445 | -58.3814 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec7dd7f5-1ade-3690-983b-42e3c3253b80 | -6.12301 | -57.82043 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f081b2aa-13b4-3453-ba61-54bbf6db1e6b | -7.54324 | -61.3567 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70f320d7-432c-3cf3-a0bc-c413088b6954 | -2.78776 | -49.58176 | 2026-08-26 05:27:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7fa99ea9-e5de-3fa9-84d2-b9ed1eef4d7e | -6.85699 | -59.41442 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a73a423-fd9c-3679-b205-96c56c9b210a | -6.33468 | -54.74112 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17efbff9-cf3c-36a3-9a57-7d8a7ce443f8 | -7.48533 | -55.27938 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bad9487d-2550-3711-bd8a-a247278531df | -6.85754 | -59.41095 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ddf8c19-3c22-31be-b971-b2f052eac143 | -7.1424 | -55.83601 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49702acd-fec1-3f46-909c-5a474488c1d5 | -6.33081 | -54.74055 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c7dd5cb3-f320-3d5a-b167-65e5f7386334 | -6.22513 | -55.61881 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cd90f6d8-4d80-36a5-8136-2d46a207454a | -6.62348 | -58.49755 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 779d06cd-1545-337d-9bce-b1386f8933d8 | -8.95339 | -50.77636 | 2026-08-26 05:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 686335d2-3678-32a5-b2be-7a1b34fbaf53 | -6.11518 | -57.82649 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d2722d9-3061-3e0e-a551-198ce5a0e48a | -6.34241 | -54.74226 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f24b124-79ca-38fa-8cfb-d5100ec45c8e | -6.78769 | -59.65656 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33568825-49f7-3459-9fbc-b434fdbdfbc2 | -6.99838 | -59.31213 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0d6c2db-af67-3651-b75a-601d0b911d02 | -8.59627 | -54.86279 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a273504a-4a19-363e-8e18-8be21f1e25b4 | -7.38053 | -55.15161 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| da892fa1-ad7c-34f2-9eb5-4c0eac4ca880 | -6.14956 | -59.92472 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a7e3c483-2cb7-3026-aed8-70c0ceb08296 | -3.13088 | -61.18901 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de5533c5-1416-3254-a35e-370310e5291f | -6.271 | -53.36938 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 20b26901-396a-3030-b6e6-78429ac2ee5f | -6.63675 | -58.49237 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c637c2a3-b69b-3966-b639-862b8666853c | -6.99835 | -59.26942 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fac552c7-1a63-3da9-9baf-22b34f206d76 | -2.98466 | -49.27568 | 2026-08-26 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50752bc2-4135-3dc4-9392-7cbdb29ab6ea | -6.30949 | -53.57106 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f0f8d430-2d7a-3e39-b2c5-bf6b2ce7b00f | -6.13254 | -57.82559 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5e37063-2f22-359c-8782-660db29faddd | -3.09678 | -61.19599 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a667dc7-b032-3c58-ae3b-a3e0511e5051 | -6.77554 | -59.43694 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4bf3b0e3-9cdf-34ed-8700-4e561cea03f2 | -5.7883 | -57.61151 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a979c12-dfce-32c4-95f4-8a9fb6baafac | -7.39583 | -55.15395 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fceff3e4-756f-3a8e-9143-197f4b61ef8b | -6.81656 | -59.58258 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f56f1c31-7d63-3fdc-82c5-eb266a73e0aa | -6.63402 | -58.49564 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2b3c5b5-c8be-3bd7-a566-cc40997d566f | -3.09321 | -61.19542 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ed8dc5c-5525-3f9d-8297-fa3fa660be47 | -7.38471 | -55.1764 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b49edec0-5cc3-3523-921b-33f48f70763f | -6.44121 | -54.97056 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38cc8800-06b5-3700-ab4e-fe3398e0e6cb | -6.63069 | -58.49511 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed2f5e57-2753-3536-8da3-08ffd1a8150b | -6.16054 | -57.80075 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b6e4fd3-dd70-332c-a4dd-4af3f4f68ce7 | -6.30003 | -53.5773 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fd8d366-91d0-3f8d-bc67-ba46613df854 | -6.1337 | -57.86224 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 912bef12-597e-3d90-a8f8-bbfa725d3510 | -3.20289 | -58.9977 | 2026-08-26 05:27:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d840cf4c-dccf-3946-b9f7-4974b8c28710 | -5.76918 | -57.55706 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c928a07c-2638-314d-8e87-0bc0a1a44014 | -6.14755 | -57.70712 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c475e372-5489-3755-9b59-b75e462ac18a | -6.99448 | -59.27237 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0855bac-6987-367c-8e27-40dbcb1baa60 | -2.79295 | -49.58261 | 2026-08-26 05:27:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0c32d1a4-f8e1-3a64-bc2e-d101885ab1f4 | -7.09126 | -56.54197 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5551786a-8a72-3168-a55a-291cfd50add9 | -7.52391 | -61.38841 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 0db54742-e513-3d1b-a753-2c8994e9a0b5 | -7.48603 | -55.27467 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b949049d-d3a7-383c-ba8b-516ac3cb96cd | -4.92793 | -55.77673 | 2026-08-26 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ef5897e-3c7a-3ec3-9111-266cfaaaca93 | -7.52798 | -61.3852 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 49ecb70c-fe66-3ef8-92d4-903fecb11339 | -7.0293 | -59.22454 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9fd1c37-e846-315e-8c26-7c1f1fd3e950 | -7.47555 | -61.36962 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c46c5196-d2a5-3ad6-9c62-e9e192a4bac4 | -6.99338 | -59.27931 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40589ff5-582b-3e34-84bb-9dbf197e2c54 | -6.12582 | -57.82453 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 050050c1-057d-3b27-bae4-df93480f9ec7 | -8.5891 | -54.71984 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 10c95159-c32e-3b9d-ae2e-e67d38313e33 | -8.13375 | -47.51188 | 2026-08-26 05:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 67711f8a-83d1-3caf-8bbf-b416f7d462e0 | -6.68981 | -58.71865 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff9b7bbd-bb91-329e-bda3-a261f5d1a191 | -6.82774 | -58.65501 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 55225fa1-8eaa-3428-98d2-a3589af58fef | -7.37948 | -55.18541 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0664c51e-078a-32e9-bdae-0037d08acc7e | -2.79342 | -49.57951 | 2026-08-26 05:27:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2b5476df-bcf1-3161-bae0-252e537e68f6 | -8.6164 | -54.74107 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ab7ca78-69cc-3df1-8e1f-79203b21f478 | -7.5398 | -61.35613 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f45cdda-8069-3949-a757-18aa3fcf3294 | -3.62536 | -49.70251 | 2026-08-26 05:27:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 015c27b0-c7dd-3b8a-97b1-549775267dda | -6.90644 | -58.99538 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1bd0871e-f791-300e-93d1-1667557d438f | -7.45839 | -59.99666 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README59.md)
