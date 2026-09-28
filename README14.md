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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef89c891-47b1-32eb-9bb8-a36cf4e2e07a | -14.901 | -49.4761 | 2026-09-28 02:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 179.0 |
| bbbcfc9f-478c-3f0b-a3ff-12997d837d5a | -14.9201 | -49.4951 | 2026-09-28 02:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 268.1 |
| fa39d64a-6124-3bb3-8bb3-2d0c2712f582 | -3.2137 | -51.0384 | 2026-09-28 02:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 70e8845a-0665-34fa-9b65-1052b53377b2 | -11.1958 | -44.8269 | 2026-09-28 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 233.7 |
| f1b77de0-129f-371f-933f-2cd24aa75c57 | -11.1771 | -44.8064 | 2026-09-28 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 237.7 |
| 297b7364-653e-35b3-9d21-4295fe2d4a38 | -11.1966 | -44.7805 | 2026-09-28 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 4a01ecd6-9e6b-3a08-91e3-096d9aa37df2 | -11.1962 | -44.8037 | 2026-09-28 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 369.5 |
| 78608669-4513-3b53-8a4c-b4962da7a2fd | -6.7251 | -45.5975 | 2026-09-28 02:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 7ed531cd-82b2-3beb-a2b1-b33ed2785880 | -9.177 | -61.4073 | 2026-09-28 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 1fb3b3e9-5120-3d41-991d-057d5a07c234 | -3.1471 | -54.0849 | 2026-09-28 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 7bfb5327-101a-3152-b95e-f83da823400c | -11.2154 | -44.801 | 2026-09-28 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| a97268df-721c-3bef-81f8-2742f2447a6b | -11.1767 | -44.8296 | 2026-09-28 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 9c33c24d-016f-39f1-b277-42355eed4af2 | -9.177 | -61.4073 | 2026-09-28 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 19179f84-767d-32e8-aa7b-59c7374aab99 | -3.2137 | -51.0384 | 2026-09-28 02:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| bcfc72a8-d122-380a-be46-709a5dc06550 | -11.1966 | -44.7805 | 2026-09-28 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| d3823cf5-cb00-31a0-bc9f-3fbf59b80ac5 | -11.1962 | -44.8037 | 2026-09-28 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 347.2 |
| 823fdf45-4d04-337d-a626-f0def816d092 | -11.1958 | -44.8269 | 2026-09-28 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 43e56042-2c28-3a64-89d6-58b2f7f6c311 | -11.1771 | -44.8064 | 2026-09-28 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 156.3 |
| ac99a2aa-219a-33f7-bd87-056d65404a94 | -10.8238 | -60.744 | 2026-09-28 02:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| f5db6ed8-5c0c-3c4e-95fb-aca2c7884036 | -11.1767 | -44.8296 | 2026-09-28 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| e19e52bd-9314-338b-99da-f1a42d188bba | -6.0734 | -57.8025 | 2026-09-28 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| a34407dd-75b5-368a-9fe4-264f68cd470c | -8.2293 | -45.4375 | 2026-09-28 03:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 16ba47eb-b3de-3254-86f5-94d0082fc12c | -9.1584 | -61.4082 | 2026-09-28 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 7691f268-3151-3574-9eb9-d7be723595cd | -15.1748 | -49.3893 | 2026-09-28 03:00:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 161.9 |
| c57e5a50-012f-39c5-9f58-49982522d854 | -6.7064 | -45.599 | 2026-09-28 03:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| bfafaf3e-7497-3791-a5fc-0c4003109570 | -10.8238 | -60.744 | 2026-09-28 03:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| c8bdac68-8da3-3aec-9cae-5199ed566f1c | -15.1943 | -49.3862 | 2026-09-28 03:00:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 75.6 |
| aea5d317-fbd6-31d5-8329-2a98a6760d50 | -6.6627 | -55.1112 | 2026-09-28 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| ea3600cf-a1dc-36a6-832e-9b5fd512e2f9 | -6.0919 | -57.8018 | 2026-09-28 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 157dceb3-b258-3d5a-bada-6add98fd99b1 | -3.2137 | -51.0384 | 2026-09-28 03:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| cc416958-ad05-3c57-a277-66ed1feec6de | -6.7251 | -45.5975 | 2026-09-28 03:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 89deed6a-b385-3671-8c39-71873272e91a | -6.7064 | -45.599 | 2026-09-28 03:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 9679ac6c-8690-3330-9690-cae3e31c1ea5 | -9.9973 | -50.1393 | 2026-09-28 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 4b1116e2-d963-3799-957d-e690bb3ec76e | -9.177 | -61.4073 | 2026-09-28 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 551a5ffe-a193-3192-b84d-e5bd44b0240e | -6.7251 | -45.5975 | 2026-09-28 03:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| b13ca07e-9153-3799-b51e-399174f38c53 | -11.4425 | -44.9303 | 2026-09-28 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.8 |
| cf22ee0f-2e97-3910-8e11-7b3348a8c622 | -7.4591 | -64.3453 | 2026-09-28 03:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| a3920aba-3cab-354e-8f4a-d2bf5c32b101 | -6.6627 | -55.1112 | 2026-09-28 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| b37f7b2f-f5c3-3040-a621-7b8714ce7b76 | -9.1584 | -61.4082 | 2026-09-28 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 9bb37913-e353-3b86-96a9-71d672108d22 | -2.998 | -54.7492 | 2026-09-28 03:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 1d6a9501-2d04-3367-b477-c5a3a1eaf85f | -6.0919 | -57.8018 | 2026-09-28 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| d8dfbd1a-ed86-3f8e-a234-eb7ad3c6d105 | -3.2137 | -51.0384 | 2026-09-28 03:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 847ca822-d3b5-3044-b51d-39bced3b4ee0 | -11.19 | -44.8 | 2026-09-28 03:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 11607bfc-98b8-39a8-9a62-87c838c7bbcc | -11.19 | -44.85 | 2026-09-28 03:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b80f39c7-8948-3a55-89d0-dbba2466dd1d | -11.16 | -44.8 | 2026-09-28 03:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 505a764c-9fb3-3eae-9b98-389ed86d7353 | -15.19 | -49.4 | 2026-09-28 03:15:00 | MSG-03 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5373fd39-96b4-394a-b1f7-033d3877d9f4 | -15.16 | -49.39 | 2026-09-28 03:15:00 | MSG-03 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ec81ad36-edda-38e1-af48-b7d11a0b3806 | -11.1962 | -44.8037 | 2026-09-28 03:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 914.8 |
| 35ddcf52-e883-3758-961e-a34ede6a7811 | -11.1958 | -44.8269 | 2026-09-28 03:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 190.9 |
| 1903420b-79e9-317d-b6e9-c5a6bd5bb52f | -3.2137 | -51.0384 | 2026-09-28 03:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 5299a6c4-e811-3391-a4b5-182f16ed85d1 | -6.7066 | -45.5765 | 2026-09-28 03:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 70ed6305-7a34-31c1-a937-c5dc07717086 | -11.1775 | -44.7832 | 2026-09-28 03:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 181.4 |
| 856d66aa-18ad-3856-89eb-a800bfc7026d | -10.9156 | -50.6845 | 2026-09-28 03:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| f73ad446-e0e3-37a3-b79b-c04c7ed0d823 | -11.1767 | -44.8296 | 2026-09-28 03:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 5776ba44-7796-35fe-86ef-7cdb2c241b4b | -18.1151 | -44.3745 | 2026-09-28 03:20:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 57b8411c-6e8a-3261-a0b4-e178a51fafd7 | -2.998 | -54.7492 | 2026-09-28 03:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 520216b1-c3e1-3da0-bd8e-a39798c4986c | -11.1771 | -44.8064 | 2026-09-28 03:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 478.9 |
| 4061f60c-0823-3c18-a5a2-83fafee0c2a5 | -11.1966 | -44.7805 | 2026-09-28 03:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 330.8 |
| fed09f6e-222d-3d33-aa31-83c37c9ff8c6 | -9.177 | -61.4073 | 2026-09-28 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| f4c1282c-db92-3d5a-820f-a306020fb9da | -6.7064 | -45.599 | 2026-09-28 03:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 62e1bd89-c263-33bd-b2e5-da199b4f25b5 | -5.89335 | -42.43871 | 2026-09-28 03:28:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c1568fb4-d608-39eb-8a67-140a8529508e | -6.19158 | -35.24854 | 2026-09-28 03:28:00 | NPP-375D | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| d7f185f7-8ff0-3c63-893c-5cf3b94e9bde | -2.998 | -54.7492 | 2026-09-28 03:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| c93df151-2d70-348c-814d-35370bbc6dc8 | -11.7135 | -50.5966 | 2026-09-28 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| c594cfcc-d1da-3624-a4b8-ff08b5de5a87 | -9.177 | -61.4073 | 2026-09-28 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| f7084e27-58c3-393d-8cfa-17840508b500 | -11.1767 | -44.8296 | 2026-09-28 03:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 20cdde20-e7f1-3b68-965f-f3e1f099869f | 1.8396 | -55.9795 | 2026-09-28 03:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| f5a17274-e5bd-34f0-aef7-6932b16735cb | -11.1966 | -44.7805 | 2026-09-28 03:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 231.8 |
| f99afd27-b7eb-3a98-911a-23394cdd79c2 | -11.1775 | -44.7832 | 2026-09-28 03:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 112fa145-625d-364b-9f39-980fa2c3792c | -10.9346 | -50.6825 | 2026-09-28 03:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 5dac6ba0-6d85-3448-a79b-aa2c75b77e03 | -6.0554 | -47.2715 | 2026-09-28 03:30:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| ca16cbbd-8db9-3b19-93a6-a7b615b73a12 | -9.1584 | -61.4082 | 2026-09-28 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 6e801d66-9092-3c39-8c6b-f17759e4b1a9 | -11.6945 | -50.5988 | 2026-09-28 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| aec351d8-f837-32e0-9883-87047cc5674f | -18.1151 | -44.3745 | 2026-09-28 03:30:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 185.0 |
| 474b9bf3-f973-3e87-80f0-e77195d7ff2b | -3.1471 | -54.0849 | 2026-09-28 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 6e4e661a-a703-35a4-99c5-89bde2d50e07 | -2.9081 | -54.1309 | 2026-09-28 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 73cbc637-cba7-3e58-8f57-21e814365e5f | -10.9156 | -50.6845 | 2026-09-28 03:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| dabceb56-8c1d-3f97-a993-9c1f7965875b | -3.4102 | -48.3448 | 2026-09-28 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 31730f2e-035a-3c74-a4e5-d2b5d2e26407 | -11.1958 | -44.8269 | 2026-09-28 03:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 9f29997f-fb5f-3514-8d35-6ed2d401086e | -6.0739 | -47.2922 | 2026-09-28 03:30:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| e75f1929-a77c-33a5-a4f8-413343375c3f | -18.6832 | -41.4612 | 2026-09-28 03:30:00 | GOES-19 | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 90.9 |
| 568d9a15-5ddf-3ef0-acf6-293459802a01 | -6.0741 | -47.2703 | 2026-09-28 03:30:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| db2993e4-5824-3d48-9ed0-6874064cabbc | -11.1962 | -44.8037 | 2026-09-28 03:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 635.8 |
| 5107d8cf-6abd-3e85-b1f2-8c6b8c041a08 | -11.1771 | -44.8064 | 2026-09-28 03:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 323.6 |
| 3195eaa4-f564-39e6-a9b8-a9ca73d2524c | -7.1578 | -39.31532 | 2026-09-28 03:30:00 | NPP-375D | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0b6ef961-12ed-3b71-a656-10066e234fa1 | -7.38024 | -42.10406 | 2026-09-28 03:30:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2046a319-6ff3-3851-a4db-4f033a8994fe | -6.95005 | -41.60727 | 2026-09-28 03:30:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d9216745-0712-3a56-9328-f3771aa4741e | -11.70481 | -44.53646 | 2026-09-28 03:30:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| badadd1c-849c-3182-b594-5a970855c555 | -11.68153 | -44.53892 | 2026-09-28 03:30:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdb62cba-280c-3589-9e9d-0f9aff4220b7 | -7.71032 | -39.35202 | 2026-09-28 03:30:00 | NPP-375D | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a6e650bc-b1c9-3361-946e-a0976078243d | -11.37564 | -43.41576 | 2026-09-28 03:30:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 13533759-e901-346e-841a-500754345ea0 | -10.88584 | -43.68509 | 2026-09-28 03:30:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 256dc4d9-93ea-34b4-9619-df6c8e92da09 | -10.88173 | -43.69116 | 2026-09-28 03:30:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 28a3a743-173e-3599-9112-1a3a166d5b2b | -11.70639 | -44.52895 | 2026-09-28 03:30:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7dac4e5f-e773-3168-83f9-f951e11fbff8 | -10.89016 | -43.68601 | 2026-09-28 03:30:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ec88a1be-f0b9-3bb3-8368-ceeb0c8f0a60 | -7.3327 | -42.08893 | 2026-09-28 03:30:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3fa8ad95-4cae-3b39-9967-0349f381ad71 | -6.94786 | -41.61872 | 2026-09-28 03:30:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 41ddfacd-10b9-3737-81c2-cb791e578ca6 | -11.37525 | -43.41597 | 2026-09-28 03:30:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b5a86d6c-663a-33f7-9980-6890ca0f300d | -11.70796 | -44.52147 | 2026-09-28 03:30:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64fab4ee-345b-31ff-8aea-f1fa5263fbcd | -6.94897 | -41.61289 | 2026-09-28 03:30:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |


[Clique aqui para ver as próximas entradas](README15.md)
