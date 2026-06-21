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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82678438-2e20-3575-8e6c-66d02eec9c87 | -11.1168 | -54.1294 | 2026-06-21 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 39d867cc-8d1a-331c-ae03-c11b186acf8f | -11.1168 | -54.1294 | 2026-06-21 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 0ab88a8a-fb54-3dcf-8ae3-3798d64e899a | -11.0976 | -54.1516 | 2026-06-21 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 140.0 |
| 2c26ea3c-efb2-3743-bb9b-20958d211ccf | -11.0979 | -54.1311 | 2026-06-21 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 132.7 |
| e1a125c7-32ed-3b1d-b2e8-3af3aaab78a1 | -11.1165 | -54.1499 | 2026-06-21 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| d9bc2295-1739-30ea-9373-5229a43d290f | -11.0976 | -54.1516 | 2026-06-21 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 206.7 |
| 840a7707-7b40-3639-af8e-17e5cc82c140 | -11.0979 | -54.1311 | 2026-06-21 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 173.9 |
| 9f844c6d-bc6c-3c31-b6ce-f8492da0646f | -11.1165 | -54.1499 | 2026-06-21 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 827ba41a-f62a-3a4e-9901-9b42bb3613e7 | -11.1168 | -54.1294 | 2026-06-21 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 106.7 |
| ec3a4fee-39b4-3afb-a7d9-95df7097293c | -11.1165 | -54.1499 | 2026-06-21 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 126.0 |
| fe124b02-1d9f-33da-9099-f3f509fe84ae | -11.0976 | -54.1516 | 2026-06-21 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 197.3 |
| 10e34e5d-d534-355c-91c4-f275b0dd9117 | -11.1168 | -54.1294 | 2026-06-21 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 6a9ded9c-994e-32f6-82fc-e7ccc3eab55d | -11.0979 | -54.1311 | 2026-06-21 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 158.0 |
| cc635ffd-0da6-3233-89cc-a5bfb6b4213a | -5.82105 | -45.07683 | 2026-06-21 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 236709e4-1fd4-3248-b3a8-164b32c3c425 | -5.81704 | -45.06963 | 2026-06-21 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff81d90a-1ebf-3170-be36-fefac9c4f1ba | -6.50932 | -42.21667 | 2026-06-21 03:47:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 15b924b2-70a0-33ca-a137-e17175cc610c | -5.81946 | -45.086 | 2026-06-21 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 28283822-af60-3c2a-bcfc-0310b4d4de54 | -6.08513 | -44.00363 | 2026-06-21 03:47:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6299798-dcf7-33e9-96a3-e4f12fb1b3f5 | -6.99618 | -42.88763 | 2026-06-21 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| c263e906-f7dd-39bc-a77c-fe765a6b4a5e | -5.81651 | -45.07269 | 2026-06-21 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84be96d5-5074-3162-ae29-dbee7a71b5cd | -6.95735 | -42.06556 | 2026-06-21 03:47:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 723a2c33-54e5-331e-97b3-115fd7e0e0e9 | -6.50517 | -42.21592 | 2026-06-21 03:47:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 34f9e43a-28b1-322b-889f-0dafaab37f29 | -6.96143 | -42.06628 | 2026-06-21 03:47:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d6257965-be8c-307a-893c-1ed4c6e2c3e0 | -6.17267 | -43.35321 | 2026-06-21 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9742e1eb-1da9-30eb-803f-157fa2f0f708 | -6.04453 | -39.82055 | 2026-06-21 03:47:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6c70c935-452e-3c16-8be4-7ab093fcdf15 | -6.17466 | -43.35154 | 2026-06-21 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6337c2d4-b30d-3f42-b2c2-ace6a15d7e82 | -5.2018 | -38.83881 | 2026-06-21 03:47:00 | NOAA-21 | BANABUIÚ | CEARÁ | Brasil | 2301851 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 99cadfd2-055d-36f8-8add-ed658dccb8e9 | -7.00049 | -42.8884 | 2026-06-21 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 39ce55e1-81aa-3625-ab64-9ff1cd240269 | -5.81544 | -45.07881 | 2026-06-21 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9d9c8888-e03f-3cef-8096-e1ad81800da0 | -6.9998 | -42.89253 | 2026-06-21 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| fb2ac61a-85ff-3a27-a91c-6f44bac062db | -5.82052 | -45.0799 | 2026-06-21 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 62a804ba-5136-3db3-b590-5eed3eba7b9a | -5.81999 | -45.08295 | 2026-06-21 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ba1cd26-0d09-3a90-a130-994c0c880a32 | -5.96115 | -43.49278 | 2026-06-21 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5902691a-f853-389e-93f3-68c163b032b7 | -5.81438 | -45.08492 | 2026-06-21 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e56ab13-7802-31df-a71b-67e4bb7f6b44 | -5.89403 | -39.25037 | 2026-06-21 03:47:00 | NOAA-21 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3ae7db55-a978-342e-bd02-bcc918248268 | -5.73576 | -39.71033 | 2026-06-21 03:47:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6a3302e2-1e38-3f46-b136-a04eb22ced0d | -5.81598 | -45.07575 | 2026-06-21 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 55bdfa7f-6afe-3218-a036-2f8495c735d4 | -6.08038 | -44.00297 | 2026-06-21 03:47:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77e93953-f122-3df8-a9c9-440af347d1c3 | -6.51627 | -37.15096 | 2026-06-21 03:47:00 | NOAA-21 | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b8598ffe-14d3-378a-bc81-9b622ece26a8 | -6.99549 | -42.89177 | 2026-06-21 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 01a6e41f-e0ab-3f3e-81c5-d45b6e8c7467 | -5.81491 | -45.08187 | 2026-06-21 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8a330d51-eb90-31ff-a46d-40998662ac05 | -4.06494 | -43.24781 | 2026-06-21 03:47:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd489f8c-4a16-3bdf-a140-f3fb30d8b4db | -5.82158 | -45.07376 | 2026-06-21 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf5c4236-36c5-3307-827c-4f828284533b | -6.83872 | -47.91891 | 2026-06-21 03:49:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb202cbf-8c3f-3100-9ab8-586ba565f1f0 | -12.23649 | -43.20983 | 2026-06-21 03:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1586b31a-2fde-3418-aeea-c2039fcb77db | -10.5367 | -47.72992 | 2026-06-21 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7c306ef-64ca-3712-a46a-c10b5864ab9c | -10.58515 | -44.33149 | 2026-06-21 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c35b1d08-274a-31de-919d-5ee3b63898e7 | -6.85156 | -47.91691 | 2026-06-21 03:49:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c709b755-3ff8-3d6b-8df7-64559c903739 | -8.39204 | -45.55696 | 2026-06-21 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea60197d-9d24-3e2e-b25c-cccfff269b25 | -10.25083 | -47.34581 | 2026-06-21 03:49:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d9e8677-7b53-371b-9117-156e47cf2f53 | -11.94918 | -43.96676 | 2026-06-21 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5e9c0f7e-8866-3f78-a9b1-f74e4b81c97a | -11.63867 | -48.52716 | 2026-06-21 03:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1e6f0543-1745-30f7-86ad-7baa0381150a | -9.68964 | -47.69676 | 2026-06-21 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c678339-6f07-322f-ac56-c6e9181ca7ed | -10.69023 | -47.70456 | 2026-06-21 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6e704b9-ebe2-3424-bb05-b9fc75a45007 | -7.7223 | -44.56474 | 2026-06-21 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14a5ed6b-b58c-32af-9755-b04a8e74904b | -9.31086 | -47.6315 | 2026-06-21 03:49:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 191c41a5-910e-3854-bd08-b35054e6c18e | -8.65071 | -47.7674 | 2026-06-21 03:49:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e554f33-6b49-3492-bfc8-9e6d91b091fd | -13.86098 | -45.89292 | 2026-06-21 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3387c7b4-1198-3753-88a0-8046f8eac5ba | -10.87681 | -46.33384 | 2026-06-21 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b70625bb-727e-361a-93e6-9bb2c40a0165 | -11.95025 | -43.96777 | 2026-06-21 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9e1c575d-4556-3348-a9d0-7b19a51fc51f | -8.65146 | -47.76328 | 2026-06-21 03:49:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc700997-2286-3d68-a2d1-8a3209b97c1c | -11.63856 | -48.52802 | 2026-06-21 03:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| dcbf052c-1b11-3e8d-a5b5-78004e4139b5 | -9.23182 | -40.5586 | 2026-06-21 03:49:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 07433717-9ad6-361b-b529-d2d96084174c | -13.56653 | -43.51139 | 2026-06-21 03:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e9a1939-dc9c-35b6-a9b2-930042d42642 | -13.56316 | -43.50702 | 2026-06-21 03:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c97ee92c-203b-3308-8137-8788ca20493c | -9.6904 | -47.69275 | 2026-06-21 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 13aecaa9-6702-3dbe-b8bd-3bc1a901e2bb | -9.03943 | -42.68843 | 2026-06-21 03:49:00 | NOAA-21 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fb35ebbf-b084-3864-a0c1-f701e422cbd3 | -8.25881 | -43.9305 | 2026-06-21 03:49:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1719d0f-2ec1-3730-8c04-e1a011ef9ab7 | -11.89104 | -43.83126 | 2026-06-21 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4d3ed937-a441-3fb4-b7f6-53a1d9478d2f | -11.64368 | -48.53236 | 2026-06-21 03:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6e74d44-92be-3e07-9094-d5c2e45191e4 | -10.54158 | -47.73478 | 2026-06-21 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b36d9c15-9d97-37a7-816c-fce3bf3e2fa6 | -8.35622 | -50.50411 | 2026-06-21 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0fadfb32-7582-3fd5-ad2c-c16f4339d758 | -11.63693 | -48.5362 | 2026-06-21 03:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b51638f7-f2ba-3236-9d2c-4c125254cdac | -11.94993 | -43.96266 | 2026-06-21 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a19df605-f7a6-33ff-991a-79926bb99b44 | -11.55141 | -48.26416 | 2026-06-21 03:49:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d78030d7-f683-3e86-99bb-ee41602ef0a9 | -11.63709 | -48.53537 | 2026-06-21 03:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 81bb7041-cdf4-3b7d-84e5-cf3a2614e7b4 | -11.9467 | -43.9629 | 2026-06-21 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fed4b336-69e0-38d7-aefe-78971cc10d04 | -7.54473 | -43.444 | 2026-06-21 03:49:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 748541b4-6e8e-3c34-95c6-19803c41ac9d | -10.53744 | -47.72605 | 2026-06-21 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d5a17fe9-79cb-368a-bf0b-b0fe683f046e | -11.08522 | -43.18375 | 2026-06-21 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc9870fc-9548-3111-a8b8-4da587999c49 | -11.64447 | -48.52822 | 2026-06-21 03:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fee7a85f-62e7-33d7-a20f-a0912e173de7 | -8.00708 | -46.45015 | 2026-06-21 03:49:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3d9acf0b-6a05-3d0a-86d9-44595e2e0ae7 | -11.64437 | -48.52906 | 2026-06-21 03:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cc699dc5-369b-3748-b466-9606773dfaf6 | -10.58068 | -44.33067 | 2026-06-21 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c3cc1517-7af0-3b6b-b5e9-a32e6fec30a4 | -9.35977 | -40.50972 | 2026-06-21 03:49:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3d458c5d-09b6-37f9-9469-648e378e52f2 | -2.98917 | -40.03998 | 2026-06-21 03:49:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| abb9accf-fa86-3d4e-9a1a-c30f3f0ec806 | -11.94598 | -43.96702 | 2026-06-21 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 20ea80d3-0e35-3fc3-889e-9193416b9045 | -12.83224 | -49.79726 | 2026-06-21 03:49:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 29a6d883-000c-38d5-9864-a5fdc05a0029 | -8.65122 | -47.76263 | 2026-06-21 03:49:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7810c1c-f192-36a8-81d7-7448dd57d52d | -10.58328 | -44.32815 | 2026-06-21 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| d67076be-34cc-333e-921f-7e7e985ab973 | -13.5625 | -43.51065 | 2026-06-21 03:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60d33eef-111c-3ec7-9e79-d9e523e87773 | -9.3128 | -47.63154 | 2026-06-21 03:49:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3d4026f5-bc64-32e8-ba1e-bbeeac2ab7f2 | -7.18554 | -44.87695 | 2026-06-21 03:49:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0a999b9-2ca0-3789-8f79-a668824d1306 | -10.58598 | -44.32691 | 2026-06-21 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b57f9b9f-e8f7-3b93-bbff-d8c4da0640b4 | -8.35742 | -50.4985 | 2026-06-21 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1faaa5dc-0a93-324b-bcf4-9da085e95221 | -11.79577 | -42.63663 | 2026-06-21 03:49:00 | NOAA-21 | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c33022f3-171d-351d-98a1-5bb716463de1 | -10.59045 | -44.32772 | 2026-06-21 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 64f1964f-e4f8-314f-bc7f-b13d17b6ced5 | -10.59409 | -44.33311 | 2026-06-21 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 6c3a1768-fc16-371d-87f7-bea789892370 | -6.84559 | -47.91547 | 2026-06-21 03:49:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8dd10da-76b7-312a-98d8-503b6914e67e | -11.63775 | -48.53212 | 2026-06-21 03:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |


[Clique aqui para ver as próximas entradas](README3.md)
