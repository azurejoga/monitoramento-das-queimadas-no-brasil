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
| 27f7d530-8390-3ccb-8ae3-ada36921da35 | -3.26876 | -50.60463 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fbf43ef-2935-3e0b-a0ff-d1af9c07008d | -3.341 | -48.38265 | 2025-11-13 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8257be13-4fa4-3a67-bc55-b0c01098d2d0 | -3.59323 | -50.16753 | 2025-11-13 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a47d18a-d8d4-31f0-bb58-29b628b0f14b | -2.89464 | -48.07841 | 2025-11-13 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55770895-32a3-3952-bb7c-6f196d9b8b6f | -5.68319 | -46.01225 | 2025-11-13 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f14e39a-da11-3835-8dfd-3eb763558ff4 | -4.81349 | -47.34803 | 2025-11-13 04:42:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49d127e5-b0d0-3c08-9969-99816fa3115f | -5.64481 | -41.06788 | 2025-11-13 04:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4f20acdb-c192-3fd6-937a-d18719a07293 | -4.75248 | -42.78052 | 2025-11-13 04:42:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef91efd2-0366-3def-92df-fc07cdffa0cc | -3.1539 | -45.81504 | 2025-11-13 04:42:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5f23615-0344-3dfd-b4e9-6906d9a3416e | -3.75608 | -50.94418 | 2025-11-13 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 25c00e93-6de8-332e-ac16-8a45ee6c8226 | -4.30638 | -48.24532 | 2025-11-13 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e92be6e-7015-36bb-8758-f6b08f539b98 | -4.7551 | -48.83484 | 2025-11-13 04:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9f3c955-e599-382f-89a2-6917d32c7a46 | -5.36135 | -45.40855 | 2025-11-13 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c76eab90-4e57-3cb8-9285-c98b7f563cf7 | -2.0028 | -54.45014 | 2025-11-13 04:42:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4e70b4dc-5c5e-39b4-910d-7227d7ef7332 | -3.40037 | -50.17788 | 2025-11-13 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 353e0822-c59d-3b0d-b807-c4edf8d3d20f | -6.07798 | -41.56385 | 2025-11-13 04:42:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 006ec8fb-fa0b-3aa8-8b64-331c51ee678a | -3.14767 | -50.26773 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6a1cd5b4-557e-3562-a26f-7fb4e1ca952f | -3.25957 | -50.02739 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 64513261-a3ec-373e-b69d-66f6f1f3a2fd | -4.53128 | -46.43719 | 2025-11-13 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4a449188-348c-36a7-a759-12e082c50e01 | -3.89571 | -52.11749 | 2025-11-13 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2592b393-b8c4-3f74-abec-c9613ba850b7 | -5.84372 | -38.3503 | 2025-11-13 04:42:00 | NPP-375D | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 9.7 |
| dd9c0458-0a16-3dc2-b313-9c84b453012b | -2.6402 | -49.21716 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b9f63aa-7e8c-33d8-8692-4c1c8190ce60 | -4.10975 | -48.01014 | 2025-11-13 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee0bd0e9-912d-332d-abef-302e90f0eb85 | -3.77998 | -52.16565 | 2025-11-13 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 422c6311-5bb7-3866-b46f-ca7dad279925 | -2.44981 | -49.26173 | 2025-11-13 04:42:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c6445da6-a3c1-3b26-9547-6c8c5083bdde | -4.63627 | -48.74891 | 2025-11-13 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8c2fcbb-9abe-39cb-815b-a840c8d936eb | -3.27638 | -50.80063 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6b954cf-cfd4-341c-adc3-889dbda023f1 | -6.87893 | -42.85087 | 2025-11-13 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| d9488ee7-4808-3be8-9944-771eb98ca643 | -2.26826 | -49.08399 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4cd32352-d2ee-362b-aacc-e66106c9bff9 | -3.40375 | -50.17841 | 2025-11-13 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1b7f495-94c4-3330-bc96-10fc9859dceb | -4.95003 | -47.03426 | 2025-11-13 04:42:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ad25253-f6c1-309f-afc2-1d102b99cfa7 | -4.51987 | -46.42043 | 2025-11-13 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 85499be8-d84e-325a-b404-b43f89061a80 | -3.72566 | -49.821 | 2025-11-13 04:42:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d49e82ae-6790-30c1-9bac-f1088ea41d6c | -5.64905 | -41.07421 | 2025-11-13 04:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 17f280c5-b371-3809-a26b-1411318e69db | -5.64804 | -41.08144 | 2025-11-13 04:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b19cc472-9ad9-31d3-8b1b-ce7fcab54518 | -5.35795 | -46.75718 | 2025-11-13 04:42:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 77031159-04fe-32b7-8738-ecc2c16a7f34 | -4.12873 | -46.84256 | 2025-11-13 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce45b5dc-ffdb-3f9f-a8f2-1f19e9af7879 | -4.72084 | -46.44915 | 2025-11-13 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d2a728f8-946b-3e93-85ee-d9c0c8e2c6c1 | -5.88882 | -46.44395 | 2025-11-13 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3e78ad7-afea-34df-8fb7-5cac60dd95ed | -3.46364 | -43.18299 | 2025-11-13 04:42:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b926688-a752-3ad8-b859-8b426b9e36e8 | -3.29318 | -52.1082 | 2025-11-13 04:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc8f2dee-8c1a-34b4-9b60-4ed94ab25008 | -4.25125 | -46.29182 | 2025-11-13 04:42:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 066ba1c1-4999-3c86-9c4c-5e9b5521e1c3 | -5.76494 | -51.42177 | 2025-11-13 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85d5d94a-32da-322a-a57e-ca06630f2dfd | -3.14829 | -49.47206 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2ac41fa-634c-3a95-9f32-4210b18ec7fd | -4.75787 | -48.83882 | 2025-11-13 04:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 481c9d51-7d32-3aa6-b364-753f52ecce78 | -2.85432 | -51.28017 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03ed1caf-2ab3-3c6f-8fba-6cbb08a981fd | -3.36959 | -48.41171 | 2025-11-13 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 032d366f-d4c5-376f-ab73-54b7a784df3b | -4.33473 | -50.8198 | 2025-11-13 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd5e18b4-397f-3ebb-b6a8-023052982aa5 | -4.82014 | -49.72813 | 2025-11-13 04:42:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aae1e448-e4ca-3351-ada9-bf5fa83a027b | -3.33768 | -48.38213 | 2025-11-13 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f037f551-0a94-3aa8-86b5-90fabbc765ae | -4.89601 | -48.97005 | 2025-11-13 04:42:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b46dc539-c874-3366-898b-fe5902457780 | -7.11557 | -42.7255 | 2025-11-13 04:42:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e01bc999-c141-3bfa-979d-7da517789e15 | -3.1613 | -50.62254 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b356c56c-a514-38b7-ae85-8d79a9638d46 | -5.85181 | -46.44674 | 2025-11-13 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c020d0dd-a264-315a-87de-2bc58efdc6f1 | -3.34737 | -48.3799 | 2025-11-13 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfdaf1d2-cb17-3a00-9326-3670616044f7 | -4.7211 | -49.24373 | 2025-11-13 04:42:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbdbea48-f145-3e36-8c7c-aefe78a9a18a | -2.8199 | -45.44447 | 2025-11-13 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fd95e8c-ba3d-359b-9d79-baffac655e46 | -5.72713 | -44.83585 | 2025-11-13 04:42:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 25fa309b-c2d8-3e47-8745-e9f6f61f542b | -7.1158 | -42.72241 | 2025-11-13 04:42:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| af92474c-8dcf-3ba8-ac13-60a9e122a17b | -4.24213 | -49.67619 | 2025-11-13 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 912605dc-2239-316f-8cc3-a05b64f2b4c3 | -4.45853 | -38.39244 | 2025-11-13 04:42:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 5c962348-b57e-362f-8c0a-300245253760 | -4.01552 | -48.80305 | 2025-11-13 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a4d0e74-8ffb-3ba8-ba7e-b0cd05112270 | -7.18104 | -44.98721 | 2025-11-13 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8fad53cc-3aff-3aaa-a4d4-305cdc13b782 | -3.03361 | -50.28374 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e69403ac-acdd-37f9-b106-417eea05b3ae | -4.04277 | -46.12333 | 2025-11-13 04:42:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d724f19-1fd7-3440-aa7a-b54c5e53a249 | -5.585 | -51.40528 | 2025-11-13 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40e1481d-3bc1-3f61-9918-a73b044ff780 | -1.37723 | -55.39357 | 2025-11-13 04:42:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1aca95f4-649e-3969-bc5a-6de29e6c778f | -2.43671 | -48.62209 | 2025-11-13 04:42:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 116b9a5a-c779-350d-9f58-a360f13b1874 | -3.20246 | -50.75428 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b7ca2a93-43fc-3df5-a1d8-b18c2a61266b | -4.37678 | -47.26372 | 2025-11-13 04:42:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 871ddcb2-bdd0-3757-a83c-4828121740f7 | -2.97158 | -51.04203 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6fe8f25e-9871-3843-9846-424fc8e6c784 | -4.51925 | -46.42437 | 2025-11-13 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 66e8db4f-8e60-3ddc-8bb7-67612d07045f | -5.6444 | -41.07076 | 2025-11-13 04:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4cc6d9a4-396f-3600-b4c6-6914b543f685 | -7.24471 | -41.63109 | 2025-11-13 04:42:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f137e6d5-7b51-3a7a-a828-43dfbc9ff0f6 | -3.75263 | -50.94364 | 2025-11-13 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| aa237eda-bc91-3335-ade4-33b5c2e27c3a | -7.14423 | -49.12881 | 2025-11-13 04:42:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9cb48c7f-b962-3fe5-8a00-512a3323cde2 | -1.48477 | -47.14213 | 2025-11-13 04:42:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fc70bee-d196-3d13-8fd3-9d67564c6b5f | -4.66285 | -48.1536 | 2025-11-13 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68a65ff7-9534-3e63-ae7d-1e212e9b1b00 | -2.43197 | -48.04874 | 2025-11-13 04:42:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 407e3b6b-9329-35de-8ec1-761af62445d6 | -2.15809 | -45.57355 | 2025-11-13 04:42:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aebec311-7cba-3087-b55e-77bb0363af9c | -4.52776 | -46.43663 | 2025-11-13 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 26061d46-3beb-3823-9d54-01d97f34255e | -3.10937 | -45.77084 | 2025-11-13 04:42:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d9987da-f965-3cbb-a65f-3282552fff89 | -7.55558 | -47.25056 | 2025-11-13 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a6938dcf-8fa5-3aa0-a5fe-8b87f08c65a5 | -5.02488 | -46.83868 | 2025-11-13 04:42:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb34063f-c7f2-3690-80a4-ce4008c07b09 | -2.71899 | -47.41199 | 2025-11-13 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71b4b191-f929-3e29-8944-667d1c2ef789 | -3.28244 | -50.21424 | 2025-11-13 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c4ec04c-b4ce-3b1a-92e5-afb9b25a5c3a | -5.84309 | -38.35482 | 2025-11-13 04:42:00 | NPP-375D | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 06f5e20a-5642-30f8-8af8-53c449075569 | -2.86527 | -51.47665 | 2025-11-13 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 21c51866-558c-35e5-bcaf-19674482a24c | -3.09608 | -49.26776 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 244abce0-a2db-3bef-9bb3-5d01e9a9349c | -3.10778 | -45.77141 | 2025-11-13 04:42:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d405da9b-578c-3ddb-ab71-86f20292045a | -2.55119 | -49.11749 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e4fc520-0205-324e-8877-1f52c7617be6 | -5.62835 | -45.04144 | 2025-11-13 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 670b709e-9a98-37a1-8899-aee1f7cbf5f0 | -1.69564 | -46.57204 | 2025-11-13 04:42:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21700d7d-0078-3923-a81a-bae7195436f4 | -3.40432 | -50.17483 | 2025-11-13 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| df374daf-8b39-336c-841b-1888764d7967 | -6.28583 | -41.74339 | 2025-11-13 04:42:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 39eeed35-5043-322d-b867-a1c53c0b735a | -3.06059 | -40.08383 | 2025-11-13 04:42:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| c17b6473-8f2e-30dc-a58d-9fa8be563499 | -6.2539 | -44.83748 | 2025-11-13 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa02a69f-de14-3284-b7c0-a8614970b7ee | -3.80561 | -49.12391 | 2025-11-13 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ef1a5d58-2931-3f55-baa4-c6cbaaab7e6e | -3.75354 | -52.14396 | 2025-11-13 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f306757-2fcb-3341-bcee-691d89b4eb8d | -2.63632 | -49.22011 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README27.md)
