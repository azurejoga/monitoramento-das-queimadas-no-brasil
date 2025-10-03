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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd94ab2f-843f-33da-9bf4-c6e9073b2ca2 | -14.9846 | -49.96371 | 2025-10-03 04:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 399d4ea1-0d72-3b2a-9871-48bd8c66677e | -22.59019 | -42.09875 | 2025-10-03 04:14:00 | NPP-375D | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| af6b0a4d-36a8-30a5-8631-47826ff1651b | -15.339 | -46.29695 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfee6c9c-7380-33fc-867e-aaa012f9d4e0 | -16.01208 | -50.85876 | 2025-10-03 04:14:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a8d7a5ce-31b1-37ba-8924-29e8a020aca8 | -14.93173 | -47.0158 | 2025-10-03 04:14:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5218f4a4-53fb-333c-9b36-ab5da2c51a07 | -15.33198 | -46.29541 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fccb635f-044a-365a-9242-0b642cf05016 | -14.87543 | -48.3026 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3d94253a-e023-3862-94c9-f37bd98ebaa5 | -19.23114 | -43.72282 | 2025-10-03 04:14:00 | NPP-375D | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 188b46f8-3f50-3852-aa45-bc732c4c41cd | -17.86482 | -57.61393 | 2025-10-03 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| c844eba5-10e1-368d-95d8-8943a974f9a5 | -17.85974 | -57.62234 | 2025-10-03 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 423e8536-6371-3579-9d67-f3d6b952a144 | -15.57324 | -48.19315 | 2025-10-03 04:14:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c84a4d4b-2740-3d29-a46f-31b82544cfde | -14.74812 | -48.11301 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bbaba231-73ea-3559-85e7-34fe611d187f | -17.83255 | -44.30264 | 2025-10-03 04:14:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d2c7df3b-5d87-32ef-b4fd-53f7479cff98 | -16.1582 | -45.1129 | 2025-10-03 04:14:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 008f3439-6636-32df-b36c-9430fe0c83a6 | -14.72866 | -48.11404 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ff3d896-4e17-361c-a1da-f841d34fbdc0 | -14.67567 | -48.07152 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 28c0ee92-2187-30bd-8f6a-a3c85d9f0f41 | -14.9401 | -46.90925 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 86e6dfd3-560d-3778-982a-ba65f0b6e441 | -14.91647 | -48.30081 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ecc15c1-6510-3665-9d6b-17ecbd8e48cf | -14.74004 | -48.09073 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 017555f9-78a3-3ad9-9a96-4e09b1b6c35f | -16.03689 | -50.92728 | 2025-10-03 04:14:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e38e90b6-6b9a-335c-ad29-c63795b2fa95 | -18.45686 | -45.07375 | 2025-10-03 04:14:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ec1069f-3690-3f96-a392-7a1287413004 | -15.2115 | -47.18916 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25065444-37dc-3ada-9f0a-5787826e0a5a | -15.93269 | -43.07043 | 2025-10-03 04:14:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95c36be9-60d1-3baa-af42-308c25f0a015 | -15.82819 | -46.24615 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5dc8d4b3-d426-3ddf-8a3a-01787afc9bfc | -15.31289 | -46.2793 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7210a65-cb67-33b9-8f6c-05a0d8bc8670 | -15.27325 | -49.31971 | 2025-10-03 04:14:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11ecc682-9c6e-3b21-9d97-8dc4731a9d1a | -18.51373 | -44.03336 | 2025-10-03 04:14:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc333611-e406-301c-bc34-e987bd758119 | -19.71935 | -45.88121 | 2025-10-03 04:14:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7269e152-e324-3ebc-8bc7-0032b386bb9b | -14.89357 | -46.98311 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa2adff4-9389-3855-9c2e-890d158ee158 | -14.92806 | -47.01512 | 2025-10-03 04:14:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 281d06a6-e90e-3050-9af1-9641751886b2 | -19.96804 | -41.65973 | 2025-10-03 04:14:00 | NPP-375D | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 610309f4-46c9-32e8-bdd5-66a0a8a958df | -14.90857 | -48.31189 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8975ffdc-49a2-3274-bf04-e00fdc379563 | -14.65533 | -48.25378 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b6c752f9-f5df-3f3d-aac5-d31de1e333aa | -15.30944 | -46.29958 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| beb4c0ab-23b7-36ce-baa6-60702be9614c | -14.94997 | -47.52665 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5a40076e-e6cb-38f7-8a7f-09a6a353d1f7 | -15.98992 | -50.90031 | 2025-10-03 04:14:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ea812bd-ec41-36f6-865b-57a52ce8ce9f | -19.8709 | -43.64473 | 2025-10-03 04:14:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 8c41b12d-cb7b-3348-b2f4-006179c49cc9 | -16.63013 | -49.41551 | 2025-10-03 04:14:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57669a11-ef38-3f20-9911-b27e024568f6 | -18.64998 | -43.87626 | 2025-10-03 04:14:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d1fc10f-b095-3c30-99b0-f5a247fd09c0 | -18.45312 | -43.81678 | 2025-10-03 04:14:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1043f357-a4ee-3555-b4e4-0c2c05944d56 | -18.16352 | -53.34449 | 2025-10-03 04:14:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19a57032-368f-3360-8375-ba8637764689 | -15.58019 | -46.9443 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03a6fb9b-3915-398c-ba45-47367d0f18da | -15.92879 | -43.0735 | 2025-10-03 04:14:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21ebf2be-7fab-3c9d-8dbe-0fbfa089a144 | -15.19053 | -46.4056 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe5a5b9a-210f-342a-8ae0-81be408c0832 | -17.84857 | -46.83951 | 2025-10-03 04:14:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 716e70ff-7b15-38c1-88ea-2a322cb5bcd8 | -15.20869 | -47.64201 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ffb9838-c097-3f49-ba27-6713bca98878 | -14.85354 | -48.28839 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4427c953-d822-3c3b-865e-3894f4c18d87 | -14.66886 | -48.08709 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 23b8f09d-21c1-35ef-8653-478ec7782786 | -19.72597 | -46.55645 | 2025-10-03 04:14:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36a0370c-e7d2-37a8-b04f-141860f8d528 | -15.21245 | -47.64282 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da99316b-09ee-365c-9ab5-695df501eff2 | -15.21968 | -47.18593 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dcdd459a-8603-3423-a61f-c5f975baed46 | -14.90755 | -46.96768 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f672b409-836c-3c88-b5c6-187aee614a78 | -15.27299 | -47.91425 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 129835f4-b27b-3de2-8663-9200265fac31 | -14.93859 | -46.89609 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 76cc9220-c876-3acd-a843-d1dcc2afcb72 | -15.29668 | -46.28909 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa07e192-983c-3445-861f-ca79f7c20f2f | -14.91576 | -48.33962 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6f6c1164-bdc5-3213-9edb-f973bf6d12c0 | -15.36073 | -47.06427 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f1cb72b4-982c-39e3-a4fe-e43981885344 | -19.69287 | -47.62965 | 2025-10-03 04:14:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4601b17d-d036-3c4d-a709-db4b909cab93 | -15.58963 | -46.91079 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73bee43d-edcb-3f7a-bbf4-f90cefd459fa | -14.89657 | -46.96565 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60e5bc93-714c-3487-aaf8-d64781e47bf5 | -19.72272 | -45.88182 | 2025-10-03 04:14:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 43f8a25c-6468-3b46-a6aa-5a2f74a65449 | -18.44954 | -43.70723 | 2025-10-03 04:14:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ae41d06-530c-3888-884d-e39d7e5e1163 | -14.67287 | -48.08723 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 393156b8-12a6-32bf-8726-76f53d83db2d | -19.8375 | -42.29419 | 2025-10-03 04:14:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 27b3098d-495d-3397-b82e-38a3c3f8fa9e | -14.89995 | -48.30217 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7eaa4161-4983-3a2e-acf1-c501166b0f66 | -14.88468 | -48.34246 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1e7b3c9-2f79-30b5-991d-fded2515ef23 | -15.58615 | -46.90913 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa461b9f-1bac-37e4-b36f-464497ffa34d | -15.5896 | -46.93289 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2423333-95ec-3887-a3a1-b7c0e3f48c6b | -19.86697 | -43.6479 | 2025-10-03 04:14:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| da3db1b8-fb9a-38d3-9bba-f67891bedfb8 | -19.84799 | -46.16052 | 2025-10-03 04:14:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9883d9d2-1b8c-31c4-9dfc-513e54b2f804 | -20.27606 | -42.16682 | 2025-10-03 04:14:00 | NPP-375D | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f9e6712e-2ce1-39c9-b493-66d38f8a3fd2 | -14.9039 | -46.96696 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6a5128f3-36f4-33f2-b45f-4ef39dd23bd0 | -14.66924 | -48.26726 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 63eb62cb-492d-3cce-826d-18f946bcf264 | -18.18407 | -53.34864 | 2025-10-03 04:14:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02306fa6-0b45-3e36-80e4-bd29eb64a57e | -20.13322 | -44.00615 | 2025-10-03 04:14:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e0c26eb0-263f-3037-8878-627aaf908298 | -18.31657 | -44.04125 | 2025-10-03 04:14:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4736845b-025f-3efa-82b4-dafb79a9e15c | -14.89279 | -46.98763 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e1ecfd58-a02e-3113-b068-4b7c1b0feed3 | -14.80539 | -51.42183 | 2025-10-03 04:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50d3ac1f-7fba-36b9-a0c6-f029a6b10bd9 | -15.25511 | -47.92584 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c823f9dc-9ba2-3f9d-9652-a90c7ae920c0 | -17.18947 | -47.01958 | 2025-10-03 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2914535-55e7-3d34-bb4e-e3a2df0549f6 | -14.90392 | -48.33739 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37160dbd-f56f-3eb1-b99b-097b3528b3aa | -15.3545 | -46.29128 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d23ba9c4-e6f2-3fcc-886e-c3fda7406aa6 | -14.89811 | -48.34683 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0451d1db-38fa-3bca-a024-7f61db08871b | -16.2688 | -47.09266 | 2025-10-03 04:14:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2bcdecba-c630-38c6-a881-471dc85de1b0 | -15.21055 | -47.18243 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 372d7cc0-b1d7-3beb-8c44-1c623b9efb3b | -19.84143 | -44.08279 | 2025-10-03 04:14:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9632f2ef-5b96-3bf9-933c-0c1c6851308e | -14.67091 | -48.09823 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 37a473a4-2af1-347d-b78a-d864fbbfed95 | -15.22097 | -47.18805 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1c90028-823f-3df5-9f62-ceb8993245f9 | -19.88877 | -44.18908 | 2025-10-03 04:14:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fb134bfc-c903-3846-9107-c1830db41c88 | -14.9417 | -46.8777 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 38cd1508-44bc-3ff2-aa76-08561531243e | -14.74018 | -48.09416 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6173a3f1-5e61-3fcb-804d-7c9c64b9977b | -17.211 | -46.99164 | 2025-10-03 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be1f5d45-8eda-3fd8-be47-539c38336cce | -15.49118 | -45.93112 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6eb4f786-3323-3993-a949-11be6dfb79ac | -19.90288 | -44.50568 | 2025-10-03 04:14:00 | NPP-375D | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 91b51dff-ddc6-3991-9f1c-eb84bc748786 | -15.49052 | -45.93504 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d89a2cd-934d-324f-b890-47a6e2473790 | -16.3611 | -47.01505 | 2025-10-03 04:14:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a75987d-18f6-3291-aedf-4e2cd2272ff3 | -14.97406 | -49.97164 | 2025-10-03 04:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1fa2da48-8518-3201-8590-cace299da483 | -18.97594 | -46.97103 | 2025-10-03 04:14:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3eeca507-227a-321a-924e-0332a1ea468e | -15.58451 | -46.94088 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29097112-b9d6-3b24-8d0c-8ba2a83ba796 | -14.94446 | -49.9843 | 2025-10-03 04:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README76.md)
