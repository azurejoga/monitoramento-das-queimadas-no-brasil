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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6cf0b48-8201-33c4-bce4-b136a516c02a | -22.97229 | -46.72317 | 2025-08-16 03:49:00 | NOAA-21 | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1989f2c0-ea40-3e67-bfa4-66f4108efd26 | -7.9149 | -61.7288 | 2025-08-16 03:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 56150996-6ddc-38e4-8d2d-938ba79e4ad4 | -9.1708 | -59.6568 | 2025-08-16 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| fc690e3e-180e-38a8-b949-03e1e8c63ba3 | -7.9148 | -61.7478 | 2025-08-16 03:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 80678455-1282-36f9-b47c-31a8c6a83463 | -7.0796 | -59.2351 | 2025-08-16 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 83ddd574-676a-32ae-8db7-8903ab80641e | -6.9303 | -59.5305 | 2025-08-16 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 4e6c86a8-a861-3e8b-ae75-a06f4a615499 | -8.9893 | -61.7024 | 2025-08-16 03:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 51509240-5fac-3295-9a7c-0acc848ba2f4 | -6.9487 | -59.5297 | 2025-08-16 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 009b2b3b-0dd5-39f9-b3e6-da3ed7a9289c | -6.6327 | -60.0033 | 2025-08-16 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 80596ec6-ef8e-3ca0-b5dc-6bb6da6b30d0 | -9.1709 | -59.6374 | 2025-08-16 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 57508d2f-1df2-3c4c-8679-e712601a7679 | -6.9302 | -59.5497 | 2025-08-16 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 8a8a3f68-4c5b-3a16-84d4-59256f3f81c5 | -9.4992 | -60.547 | 2025-08-16 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| f7da1843-fe10-3511-a1c8-cd102963215a | -9.4994 | -60.5278 | 2025-08-16 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 39a86710-14c1-3c38-a226-326667ad8d95 | -8.9708 | -61.7033 | 2025-08-16 03:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 01ffc45a-c1d4-38c3-b37e-627ff5d63087 | -6.0807 | -59.9465 | 2025-08-16 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 618afb70-b614-3f40-88ef-3bd51a5a19eb | -8.9709 | -61.6842 | 2025-08-16 03:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 1f4e218d-a19b-3333-8486-1c92bcd4d6dc | -6.9486 | -59.549 | 2025-08-16 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| a95ad15f-bd4a-35d6-b15c-e76daaeff54e | -8.9709 | -61.6842 | 2025-08-16 04:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 97ee9bd6-e348-3216-878b-6e08264078ac | -9.4994 | -60.5278 | 2025-08-16 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 71385af0-1ebf-3b53-8dab-e5a4fac36e13 | -14.9435 | -54.7374 | 2025-08-16 04:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 546b9599-b715-3561-84b9-d16010f402d8 | -8.9708 | -61.7033 | 2025-08-16 04:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 47c8a2b1-068f-3ef3-adfd-f567d4b26431 | -6.0807 | -59.9465 | 2025-08-16 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 230c8b3e-2df9-32d9-a13a-fe30435017a7 | -6.9486 | -59.549 | 2025-08-16 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 2b82f9dc-0037-3ea4-bfe4-888155ff169d | -9.4992 | -60.547 | 2025-08-16 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 065aa1aa-514e-36c8-bf95-f11aecc73cf5 | -6.6327 | -60.0033 | 2025-08-16 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 91f60598-aa47-34c9-b811-1febc66217eb | -7.9148 | -61.7478 | 2025-08-16 04:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 6d25f201-9f94-3d35-82be-53f3ec417937 | -14.9438 | -54.7166 | 2025-08-16 04:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| e8d97b15-ecef-3703-a28f-c3a3698c929e | -9.1708 | -59.6568 | 2025-08-16 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 0f5876f2-fbae-3c54-94f2-df0b1e9069c9 | -7.0796 | -59.2351 | 2025-08-16 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 921dcc1d-03f4-3b57-ac48-2f4bde6f33f2 | -14.9628 | -54.7351 | 2025-08-16 04:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| bb70777c-d948-3757-90b2-0a89b4bf473c | -6.9487 | -59.5297 | 2025-08-16 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 9ecad2de-02eb-3ce4-aace-019f1d27771e | -9.1709 | -59.6374 | 2025-08-16 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| c4d3955f-b81d-32a2-89aa-620815a3a152 | -6.9303 | -59.5305 | 2025-08-16 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 038ce051-e1b8-3e50-82de-5a1c98c7aa04 | -7.9149 | -61.7288 | 2025-08-16 04:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 30e72154-4169-3b48-98c4-fed1c11eb846 | -14.9441 | -54.6959 | 2025-08-16 04:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 76563aa3-5603-3421-9730-6a96b0d09391 | -8.9893 | -61.7024 | 2025-08-16 04:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 4995d3f7-9d6e-341c-8d2e-e70d7ff34a1d | -6.9302 | -59.5497 | 2025-08-16 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 4f5316c9-3efe-395d-ba48-3077a6e56f13 | -4.92173 | -43.26788 | 2025-08-16 04:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 58ef4eb1-3d15-35a7-8729-3526106aa61e | -3.9837 | -47.88634 | 2025-08-16 04:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| aeac5f7f-6bd9-3ad1-80ff-531b67d768cf | -5.9539 | -38.63228 | 2025-08-16 04:08:00 | NPP-375D | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| b815a50c-f6e2-3e94-8435-d043c4d6c5b3 | -3.32442 | -42.78126 | 2025-08-16 04:08:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae7b6783-da99-3c54-8002-bed29880bfad | -2.04542 | -50.79583 | 2025-08-16 04:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8bd53e4c-19af-3190-b80f-6d5d0148913e | -5.75786 | -46.66693 | 2025-08-16 04:08:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f12f7fe9-e19f-3623-9183-d77c110be503 | -4.22597 | -47.21548 | 2025-08-16 04:08:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b248ef22-f513-3fe5-a258-02cc083bf4d1 | -3.8197 | -41.57956 | 2025-08-16 04:08:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 89624278-b414-36be-bfe4-c84422c96ebb | -4.29729 | -48.06013 | 2025-08-16 04:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36bb5bb3-7e35-37b4-9eac-761ad17deaca | -6.58324 | -42.23218 | 2025-08-16 04:08:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| be3acf9a-ea56-3f97-9009-edcd9bda7c47 | -2.37622 | -47.66822 | 2025-08-16 04:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69e18f73-b370-3b92-8cd1-d8fe4f20a6a5 | -4.18662 | -48.22303 | 2025-08-16 04:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d4ccf48-8205-3211-9a33-3c51bc71bfbc | -2.3864 | -47.66492 | 2025-08-16 04:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 435bced2-9015-32ef-9e9a-37e0a7100d7b | -3.32502 | -42.7775 | 2025-08-16 04:08:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 033bbde7-f67d-3273-8c3e-2978b85f67b3 | -5.75934 | -46.66766 | 2025-08-16 04:08:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1f843387-6294-3979-85af-de76deb65d1f | -3.8208 | -41.55109 | 2025-08-16 04:08:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| fb0dd1ed-9f28-312b-9cdb-aaabbc359f55 | -3.23153 | -50.80667 | 2025-08-16 04:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eab89f90-ad90-3494-a2b8-af8e1e947186 | -4.91888 | -43.26348 | 2025-08-16 04:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d421867-2674-335c-b0fc-29ff5e7924e4 | -3.4262 | -43.34164 | 2025-08-16 04:08:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ca4cc37-b5d5-3e48-8b18-32b8f5eedcca | -5.7552 | -46.66696 | 2025-08-16 04:08:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 16f70785-7fc2-3d5e-86ff-d8d3bd543840 | -2.48858 | -47.5667 | 2025-08-16 04:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4c2cdd6-6a66-398f-aa36-00969b9c2d82 | -4.92867 | -43.26903 | 2025-08-16 04:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6cd13b3f-111d-3078-acb8-b726e644be3f | -5.76285 | -46.67211 | 2025-08-16 04:08:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b1c1ed39-9dd3-3ed0-b7ea-11e5013ae86d | -4.18804 | -48.22017 | 2025-08-16 04:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dff5b8bb-072e-379e-93e3-3cc79eb0abf2 | -2.51094 | -51.82583 | 2025-08-16 04:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ef74ab5-c50e-3eb6-b7c3-5f5c9f521c74 | -6.04732 | -44.39921 | 2025-08-16 04:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7606464-dea4-3d05-83be-bcf6b0c8c522 | -2.90539 | -48.24904 | 2025-08-16 04:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1ad40ba-c958-30cb-a72e-4d3574a4b640 | -4.1928 | -48.22084 | 2025-08-16 04:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5c19562-95ed-37ed-8ecf-2c64fb05ff3a | -3.82981 | -47.74361 | 2025-08-16 04:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 01a5fbae-843b-3256-a3c7-1774d0db8855 | -3.65062 | -48.32576 | 2025-08-16 04:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 823efd5d-9a18-3551-90c3-0341866f48b5 | -3.32382 | -42.78502 | 2025-08-16 04:08:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b90e365-1c29-3539-949c-2d5304be943d | -3.43043 | -49.05077 | 2025-08-16 04:08:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bc75cb67-ce8f-3651-87b7-249a50f121f6 | -2.37704 | -47.6633 | 2025-08-16 04:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d04783b-2494-38ed-89be-d84d85daa40e | -5.75725 | -46.67066 | 2025-08-16 04:08:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 332b0b0a-d196-3469-b9e7-df3c874f5c14 | -3.82057 | -47.74222 | 2025-08-16 04:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13788f0d-e075-3283-a7ca-92990b246fa6 | -3.237 | -50.80557 | 2025-08-16 04:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9eb9061-c30b-33dc-b51d-3e1109509b18 | -5.75456 | -46.67068 | 2025-08-16 04:08:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f796c062-51ef-3616-8c99-3f8d9433db34 | -2.81961 | -49.00545 | 2025-08-16 04:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb1497bc-1cb7-3609-b96b-ad43b0ce65c6 | -3.82025 | -41.57606 | 2025-08-16 04:08:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bdc4ab64-711d-3449-97dc-4729cfffc222 | -4.22527 | -47.21974 | 2025-08-16 04:08:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5911188a-d349-3cae-8a31-470fb20c1890 | -2.47564 | -47.20734 | 2025-08-16 04:08:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bb394afc-46c4-3678-8a6d-a0c19fc0bbfa | -4.9252 | -43.26845 | 2025-08-16 04:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb726077-5b65-352b-b356-9c9e80a58491 | -5.7531 | -46.66995 | 2025-08-16 04:08:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e1478bda-7b3b-3e98-852f-0a3afb562dc4 | -5.75871 | -46.67139 | 2025-08-16 04:08:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 10ebeb83-f7e9-3fda-a8c0-7c1dcafaad9a | -3.23723 | -50.80772 | 2025-08-16 04:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91efe9f0-2b12-32ff-a4d6-2e4223798b89 | -5.70246 | -45.87162 | 2025-08-16 04:08:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2140dd1d-9e09-3a09-8592-3e80309d2021 | -3.23634 | -50.80955 | 2025-08-16 04:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ec5c30e-f428-37a6-b211-43a0caee9555 | -2.89156 | -40.10742 | 2025-08-16 04:08:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9f4a4f26-fb4b-3c31-b4a1-70b6a8baadf6 | -4.92582 | -43.26462 | 2025-08-16 04:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eaa5ccd7-3b73-31a6-9462-4e708f11f65f | -5.19913 | -46.09253 | 2025-08-16 04:08:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 80625f29-0058-395b-9e9c-cb222f805e1c | -3.83059 | -47.73882 | 2025-08-16 04:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 6fcbea9d-e49b-3bf5-a111-88b95e1d05ee | -5.76349 | -46.66837 | 2025-08-16 04:08:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2ee4b20c-6262-3412-9dda-801e5dd8e510 | -3.51332 | -43.24993 | 2025-08-16 04:08:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8dc11407-cacd-353c-ad09-a56b19000bf7 | -2.48974 | -47.57347 | 2025-08-16 04:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f85b59ec-d4d0-3d8e-9172-2711deeae785 | -3.98429 | -43.23813 | 2025-08-16 04:08:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ba70897b-552d-3905-b683-b428c9452a74 | -3.37989 | -52.71389 | 2025-08-16 04:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2134ace6-af8c-3fce-a086-6b04202252a7 | -4.91603 | -43.25911 | 2025-08-16 04:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 924fe5fa-61d2-3380-bc0f-cc7dd348f517 | -4.92235 | -43.26405 | 2025-08-16 04:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9c21c73-a27b-3b35-b0ce-ca86e3f2f3e2 | -4.91541 | -43.26292 | 2025-08-16 04:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0108681c-98dd-3534-96a7-705683f0176c | -3.65543 | -48.3265 | 2025-08-16 04:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c313ed82-81fb-3572-afae-70d7efef711b | -3.98017 | -43.24145 | 2025-08-16 04:08:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 581ea47f-e628-30ad-a8de-23bbbb3a7f63 | -6.58269 | -42.23567 | 2025-08-16 04:08:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0f51fa95-d572-33ca-800c-b9cbb3cecf7a | -5.06443 | -43.12323 | 2025-08-16 04:08:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README26.md)
