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
| 95e475b1-3683-3ea3-988c-914d994d3129 | -8.71686 | -47.85736 | 2025-06-25 04:57:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 19568c2e-2520-3e99-bad2-38886ee100c0 | -8.43026 | -48.30474 | 2025-06-25 04:57:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dec40347-4f28-318f-aabf-76cc0e77314c | -7.09824 | -49.17465 | 2025-06-25 04:57:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 58d846d2-8a64-32d3-9c4f-f4bc1da02542 | -8.67542 | -51.46873 | 2025-06-25 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2f037df-e796-317e-b663-bd71e503fba7 | -11.11746 | -44.5234 | 2025-06-25 04:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f020b52-6a88-354a-9fe5-fdae4db27187 | -7.02997 | -44.57238 | 2025-06-25 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1235cf1e-410a-3156-9e29-c40e3ae54ac1 | -6.18147 | -48.0563 | 2025-06-25 04:57:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1cd4e9c9-07d4-3cb4-8fe2-bb965fe9a7be | -7.86564 | -50.66614 | 2025-06-25 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3dc7befa-a6bf-3c8a-a1eb-13a9036b6c0b | -9.92462 | -52.43219 | 2025-06-25 04:57:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7c21ad1-98d5-3b52-bee3-be29dbcef543 | -10.51472 | -47.57625 | 2025-06-25 04:57:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66b67a52-42ad-3330-afb7-2ea1c604450d | -3.49643 | -51.17885 | 2025-06-25 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 133eea6b-b6ed-3a4d-9265-e0fc96c7d6a7 | -6.92535 | -46.40788 | 2025-06-25 04:57:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b02c0b30-f6a9-3c57-8323-15e42a69c7c8 | -9.50565 | -56.09363 | 2025-06-25 04:57:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8984c430-3d1a-3f2f-b95b-920ed0c4c511 | -4.54222 | -48.00367 | 2025-06-25 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31178610-4e03-3b39-b7ac-59fa31c41040 | -8.42584 | -48.30406 | 2025-06-25 04:57:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9f2003a-c011-3556-8c62-2365533f9d4a | -5.92059 | -43.48031 | 2025-06-25 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c778878e-e8d0-3950-a186-2d019d9fe9f3 | -9.48169 | -56.07513 | 2025-06-25 04:57:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eace6e9b-ae28-398b-913c-430cd61497ca | -10.454 | -47.9552 | 2025-06-25 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 3a5daed1-88e7-3fea-8d63-77c4134a9cfe | -8.67242 | -51.46393 | 2025-06-25 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8e52d18-736c-3f02-a418-a6dde7820765 | -11.11153 | -44.52259 | 2025-06-25 04:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f7f2e46b-2a69-39e9-b118-3cb803ba8b92 | -6.17962 | -48.06934 | 2025-06-25 04:57:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 6acfa23d-4d3d-3f93-ba1a-ccc66598a8e4 | -4.37688 | -48.07133 | 2025-06-25 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2cecd9ad-16c2-31fe-a507-529eb017cfdb | -6.12195 | -44.22125 | 2025-06-25 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01d9d8f5-7f28-3b1b-9e54-1334764dd0cf | -9.57024 | -49.10518 | 2025-06-25 04:57:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| de1440a1-16ac-30d4-b437-d6edf6ba34f7 | -6.34233 | -43.78564 | 2025-06-25 04:57:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb8dccd7-5279-30a2-84a1-ac7ad7a3d3f7 | -4.18759 | -48.14846 | 2025-06-25 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f330e02-16b5-3630-9b2b-3224039058fe | -8.34094 | -48.52295 | 2025-06-25 04:57:00 | NOAA-21 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e10195e6-26a5-35b0-b33f-3db02b0cfb46 | -9.92581 | -52.4242 | 2025-06-25 04:57:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5dad5cd5-4bc0-3fd7-a512-aa21178c06f4 | -6.18084 | -48.06079 | 2025-06-25 04:57:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 3bc10b39-8e6c-38a9-8872-f661a74d3a74 | -6.11629 | -44.22049 | 2025-06-25 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d319e16-f92f-3a4c-8fb3-b611cd203cfc | -7.01982 | -44.56307 | 2025-06-25 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 82ba1227-4e7c-3344-b688-9454963f7033 | -4.53866 | -48.0047 | 2025-06-25 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6561ded4-4957-3157-ba7f-ab0218b0df8f | -8.67606 | -51.46448 | 2025-06-25 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d98815c2-63b3-3888-b874-af616565b8bd | -7.48182 | -49.60402 | 2025-06-25 04:57:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8281f2a1-f076-35c4-9fd9-0a195cf4d2ff | -10.44934 | -47.95448 | 2025-06-25 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 0929d19b-9647-3702-a8bd-cc70ab075205 | -9.51394 | -56.1059 | 2025-06-25 04:57:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3215dd1d-5630-3613-9196-4b760170eee1 | -9.5745 | -49.10582 | 2025-06-25 04:57:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c03b186-baaf-3322-886a-3e70c88ed187 | -4.53442 | -48.00391 | 2025-06-25 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ca83a8b-2b4c-3af3-a7f6-68b1c6fe3756 | -6.17648 | -48.06017 | 2025-06-25 04:57:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 14f86dce-29aa-36c2-bd33-88d91f7c1297 | -6.2929 | -44.23887 | 2025-06-25 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3882aaf3-8be0-3828-96c4-4788c6a023bd | -6.77696 | -55.48751 | 2025-06-25 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 83d18d72-c15b-34db-811d-5c88ed3013e7 | -11.11098 | -44.52702 | 2025-06-25 04:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd49391f-5525-3b6e-8362-7b720d8e9972 | -13.61102 | -43.97136 | 2025-06-25 04:59:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c60c68b5-5f7d-37f7-a841-ad46374f35bc | -10.8756 | -53.77919 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7083d0ae-6a66-31dc-a102-e34fa4801fd2 | -10.8182 | -54.04545 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad73b306-ee29-3829-9282-9bd6ae90da49 | -13.64496 | -53.93694 | 2025-06-25 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4e6000d-30bf-3f8a-b370-6401a7ac6e9e | -11.79687 | -47.55132 | 2025-06-25 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 006e4098-33d9-35aa-b214-819ff3093c59 | -13.0506 | -48.8264 | 2025-06-25 04:59:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 902d92eb-818b-3552-9acb-d87288d24510 | -14.71494 | -48.40892 | 2025-06-25 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a480c474-93cd-35dc-a458-d6dfe3d6edc8 | -14.80716 | -48.29662 | 2025-06-25 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1b2a4ea0-d20c-3c14-ad93-5314013edc1d | -11.93892 | -48.42178 | 2025-06-25 04:59:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c20f7307-84e6-3115-895b-381bde7a71a1 | -11.84043 | -57.85693 | 2025-06-25 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd12604b-d726-3a07-a459-c00a2bac1455 | -11.61693 | -46.49473 | 2025-06-25 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4258fae3-c9b5-3068-9961-9e022ca2bdef | -11.09108 | -46.6417 | 2025-06-25 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbebd848-55c9-376b-8b6e-d34641fc1555 | -12.49881 | -55.74039 | 2025-06-25 04:59:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 57f1ed54-a696-3ffb-82fc-c939965dd407 | -14.71913 | -48.41483 | 2025-06-25 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f071fd8c-6379-3d6f-bbba-c09e6ffef2b6 | -13.07289 | -48.83421 | 2025-06-25 04:59:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 869de0de-65e0-369b-8ab4-d7fe5ab1b889 | -11.37088 | -54.56733 | 2025-06-25 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32ddba90-f77e-3c09-8889-97b7421fa88c | -11.14194 | -53.92436 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 77d90cd4-c42c-34a7-989c-d587d03a4b81 | -12.28465 | -57.27229 | 2025-06-25 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 82ae5b33-05fe-3fa0-b1a7-a7de334cce67 | -9.38262 | -57.55862 | 2025-06-25 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 32197663-674c-3144-b693-2f6b92f68884 | -10.06417 | -55.55638 | 2025-06-25 04:59:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 366eb88e-1dd1-32d5-ba7a-12b4d455c46d | -14.3834 | -50.33097 | 2025-06-25 04:59:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d477db1-3a86-34b6-b2f4-8884b76b0592 | -10.06472 | -55.55289 | 2025-06-25 04:59:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08dafaf0-43f5-3767-b08f-5cb01e1f6424 | -11.6161 | -46.50119 | 2025-06-25 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f19da8ab-832b-3310-9fae-beed5605adb3 | -10.29994 | -57.13249 | 2025-06-25 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 130d63af-13eb-35f7-99f3-81214fb05aea | -10.82701 | -54.00991 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e175c082-0d1f-3eef-ad02-5b207ac45628 | -10.87222 | -53.77868 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9270f7c8-3fd2-3116-9734-1f02e06ae52e | -13.2931 | -57.08038 | 2025-06-25 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0747336-bfc4-3e25-bdd1-19d9d348f469 | -11.13811 | -51.02258 | 2025-06-25 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f603ef0d-51b1-319a-b384-8cb6fe7184eb | -11.56895 | -52.09179 | 2025-06-25 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f87f1a68-2060-326a-8773-1a16ae39d920 | -12.2157 | -51.46029 | 2025-06-25 04:59:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6cba911-1e70-38d1-b30e-2263a2d808a7 | -11.88505 | -54.67353 | 2025-06-25 04:59:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 56625c82-a114-3ae4-b6b0-35e84915c815 | -12.58246 | -56.99157 | 2025-06-25 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89fff44c-bf1d-38a4-90a2-0ed00ce5e421 | -10.83886 | -54.04494 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e1d614d-75bd-3a22-bed3-fbcda9d36f57 | -10.3638 | -57.25924 | 2025-06-25 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| daf250da-ddc3-323c-bd4e-097f6ca488d3 | -10.87277 | -53.77502 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 8301a442-6082-3295-b245-dc591bc176a3 | -12.8048 | -48.73817 | 2025-06-25 04:59:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d74da64b-19fb-39f2-97a5-a00a06e9861f | -11.18401 | -48.61726 | 2025-06-25 04:59:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 505738a8-5f48-3f81-91b6-cbd4a2db872d | -10.86872 | -54.31704 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ef6e7a4-a4fd-3237-a998-1fcb38340440 | -11.61627 | -46.50005 | 2025-06-25 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e902bf8-8ee2-3d78-8a88-cf16275d077d | -11.95791 | -47.014 | 2025-06-25 04:59:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e715a265-8dbd-3481-8024-089023e11aa7 | -11.08555 | -46.64393 | 2025-06-25 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8a2e4ae-25d5-3d21-89d6-6f7dd821efb0 | -10.83036 | -54.01044 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da55793e-7d90-363f-b7d9-578be2c6d722 | -10.83091 | -54.00684 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a4e37a4-0b19-3232-ada9-eac2b36e9ba9 | -15.08174 | -48.9432 | 2025-06-25 04:59:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e2e7eba-5a46-3f1c-9f7a-c033192f8162 | -12.58639 | -56.98851 | 2025-06-25 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eda1e672-289a-35f1-80e0-04d2607f4d44 | -10.82935 | -54.03978 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8ac7a82-ab34-37f9-85db-5ee4a3c6e56a | -10.87152 | -54.32113 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 174e16b1-e5bb-32e4-a0bd-082353742a43 | -11.14011 | -53.92397 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 930d23d0-2405-3dd6-b3ae-c4c07d9fb0a5 | -11.33576 | -51.42218 | 2025-06-25 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2983608-34f6-3a92-ad68-25b25cdb284e | -13.05517 | -48.82707 | 2025-06-25 04:59:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d96c7143-e160-33d5-a38e-d2ec2927777b | -11.91358 | -54.81974 | 2025-06-25 04:59:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1ffa55ef-099b-389c-b983-ea32bbb2942b | -10.86176 | -54.29818 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1fdb1c1-59b4-3af3-9da7-1a91b128e4d7 | -10.83161 | -54.04752 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6bb5717d-f3c8-3a0b-acc1-981d616d24df | -10.60651 | -52.83668 | 2025-06-25 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 874aad41-60e4-3afa-980e-c6a3c72c7fa7 | -11.59428 | -47.61081 | 2025-06-25 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3255e871-a13a-33a7-8000-50b2cf7d0cff | -12.79563 | -48.73689 | 2025-06-25 04:59:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb477482-e4ba-333c-a3ac-67998bacd859 | -10.82155 | -54.04597 | 2025-06-25 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6be5dd91-46f1-33eb-b030-ba7f67deda79 | -10.29593 | -57.13566 | 2025-06-25 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README15.md)
