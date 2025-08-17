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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6c4cca0-85d8-31f2-b5b0-6ff5b7f735a8 | -8.79651 | -52.0753 | 2025-08-17 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 43918935-e248-3117-99d3-5f5a6740bdb1 | -11.42825 | -52.22083 | 2025-08-17 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34097cc0-df5b-3c38-a871-8e3edef00a82 | -7.14035 | -44.63868 | 2025-08-17 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e2183084-684c-398a-9bd7-62b0c07a1a82 | -11.35949 | -55.41435 | 2025-08-17 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4153e241-972a-328b-b86d-6cbf22255c40 | -7.53135 | -50.5324 | 2025-08-17 04:14:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 422d6074-87c1-3b01-a35a-87e617638bc8 | -7.02169 | -44.27756 | 2025-08-17 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84c22f8d-18bf-372d-9f04-efe95e970f39 | -12.89088 | -46.13157 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b3b91fe-19b9-3297-99a5-0afc61496e85 | -9.76565 | -48.75038 | 2025-08-17 04:14:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eacbcb1c-084f-32fd-bb8f-dfcf6b86d3ee | -12.88871 | -46.12366 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ad0cd455-3af4-336b-9e6c-3fd8cfcba344 | -8.73159 | -44.03531 | 2025-08-17 04:14:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7affaede-28c8-3f87-9f4d-e4f688e7bdcc | -12.20582 | -47.25118 | 2025-08-17 04:14:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 786c428b-086d-37c7-b3bf-49dabc856ea2 | -12.62382 | -47.11439 | 2025-08-17 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6c850ee0-2821-3db0-9f9c-a9b1cd944369 | -12.44262 | -47.00324 | 2025-08-17 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1366ad45-5b95-38df-a583-2d34634becda | -13.57121 | -46.98645 | 2025-08-17 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8063a982-cb79-3246-b06c-905c0d113554 | -7.13618 | -44.19863 | 2025-08-17 04:14:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6de485d3-d279-39d9-8d41-88c50591a7a7 | -13.56774 | -46.98598 | 2025-08-17 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df727989-cd52-393a-a6d3-7a1a23d3fab5 | -12.13471 | -47.90714 | 2025-08-17 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8c4074a-0058-3b09-9b65-eb7597be8282 | -13.01713 | -42.3288 | 2025-08-17 04:14:00 | NOAA-20 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| f8f52733-9a83-361c-98d8-22e6bfef4968 | -6.48064 | -45.44758 | 2025-08-17 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aadf27cc-9919-3144-99d0-e4c014458f87 | -13.47506 | -44.08081 | 2025-08-17 04:14:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 533ab5b6-dcaf-381e-8b78-b4083e9163ab | -10.83858 | -45.30925 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85f8811e-25fb-3a6e-af09-2dadcce58db0 | -10.85968 | -45.32747 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72261c18-dc5e-3f33-9047-5fe0062b9348 | -13.43728 | -45.88244 | 2025-08-17 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ede9fec3-6263-3070-aa47-768ef99c13c0 | -7.13562 | -44.20217 | 2025-08-17 04:14:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2dffab4-7115-3a9f-a321-8a7de0c5498c | -12.81857 | -45.99171 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46260b06-f248-344e-843c-c1c221cf279f | -12.1376 | -47.91217 | 2025-08-17 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a3dd82f-a0eb-3ca1-9296-0cb55c489de9 | -10.84607 | -45.3694 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c08985ef-f5b0-3a09-a369-f8b1c4d020be | -7.1437 | -44.63921 | 2025-08-17 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a8b2728-ba0e-309e-a631-bcdb045765d7 | -7.19859 | -46.22598 | 2025-08-17 04:14:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10243940-105e-3204-8095-22a84d4d12e5 | -12.13106 | -47.90655 | 2025-08-17 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d356547-d7c0-3d76-850d-0db1cc4d052d | -8.0167 | -43.33425 | 2025-08-17 04:14:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7a843277-dc07-3663-b4dd-12d4cc38cb73 | -11.09545 | -44.80872 | 2025-08-17 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73dcba89-ce26-3423-83b7-008a6c47591f | -6.18757 | -45.44086 | 2025-08-17 04:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b026b49a-92d5-31d5-a2de-3f5a1ec28ee4 | -6.61879 | -43.88288 | 2025-08-17 04:14:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f36e9748-25d6-3de2-8e70-00ccae8f52c8 | -10.84446 | -45.35807 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26d1cc1d-7101-38ee-9d0d-a91decea5007 | -12.19018 | -47.23615 | 2025-08-17 04:14:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3eb8ed37-80d2-3e50-936e-2464c147ddb5 | -8.78847 | -52.03424 | 2025-08-17 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eff74c64-fdcc-3b99-8002-c1401072f751 | -10.84181 | -45.33185 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c336c18-9ffa-38f9-a210-0e4ade1402e1 | -11.35702 | -55.39531 | 2025-08-17 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7d58bd79-9185-39a3-a9c6-5a1923154752 | -12.20248 | -47.24979 | 2025-08-17 04:14:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 527c44f0-ee8f-3053-8083-d443c88cdc8c | -8.79948 | -52.03045 | 2025-08-17 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 769b588e-8477-3b80-aeea-b8304b104747 | -12.13683 | -47.91668 | 2025-08-17 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| b516f865-1b89-3cc2-bbd6-9b6b8fdf3558 | -12.13836 | -47.90773 | 2025-08-17 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d54e77b9-c95b-3a07-a4d8-677530726af4 | -6.46766 | -42.94731 | 2025-08-17 04:14:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 04323420-8417-3894-9b63-ff9d4eac60f2 | -7.14255 | -44.64639 | 2025-08-17 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3a452245-0ac7-3eca-95ab-1f8404d96cfd | -7.42172 | -42.0306 | 2025-08-17 04:14:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 53278c62-3e94-3e95-bd33-de0bcfc590ee | -8.30778 | -47.6129 | 2025-08-17 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90a69d60-29b2-3eb1-9ee4-6146da9a8eb2 | -8.03858 | -47.66708 | 2025-08-17 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 20dbe28f-a306-3532-b899-cb2a8656781c | -8.08021 | -47.69838 | 2025-08-17 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fa2a329-2ea5-3975-881c-6a43894eeaa4 | -8.51984 | -47.21138 | 2025-08-17 04:14:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5bc72514-997e-3b36-b91d-bf10b566244e | -10.8433 | -45.36526 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99be3b0e-6836-3655-a4be-5a82eda0cb52 | -7.27394 | -44.18496 | 2025-08-17 04:14:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 96c901cc-de41-39e2-9f5d-daaa781c0e07 | -6.55017 | -43.02704 | 2025-08-17 04:14:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 49f00bca-af18-31ee-a4c3-ac2307ca65ef | -10.82393 | -45.33627 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b28bc342-2697-3d08-97e1-3bc30a3cdeb5 | -8.30542 | -55.10424 | 2025-08-17 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4d74793-eaba-309a-bf69-481e62686368 | -12.57395 | -47.04803 | 2025-08-17 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 400c0854-fc64-35b3-b0a4-f91d7701342c | -10.8605 | -48.47296 | 2025-08-17 04:14:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64e8482d-59b9-3f74-8ef9-a3b11eee0990 | -11.42498 | -52.22025 | 2025-08-17 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 14992b2d-c7cd-3ead-ad9f-16fae846bed6 | -13.45936 | -47.06732 | 2025-08-17 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a750e1d0-2dcc-3696-bbfa-4bcd0a7bd181 | -10.84239 | -45.32826 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eefb5b90-efab-3173-ad81-bf47337187b7 | -6.19244 | -45.4453 | 2025-08-17 04:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1abd5b02-bf95-3f6e-b5c8-529090de893a | -10.84792 | -45.33654 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97431432-fa7e-30c1-b0c5-73bcb066956b | -12.87171 | -46.07939 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 955fc2b2-28e1-3ffe-9374-ad420ae61343 | -12.92752 | -46.1191 | 2025-08-17 04:14:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1dea28bf-b29c-37ae-91c4-c0c7710cc7b8 | -6.45808 | -55.89607 | 2025-08-17 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8396f8f4-7932-35d1-8931-3ad6776e77d8 | -7.03181 | -44.57364 | 2025-08-17 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d908f122-cc04-36b2-97d0-0d4cd917bcd1 | -10.30997 | -54.16161 | 2025-08-17 04:14:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8f800cb2-a3c6-3ffa-8f0a-390b42744ebd | -13.45871 | -47.07121 | 2025-08-17 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d73f790-d52c-37ae-8634-3a5ad300c273 | -8.80896 | -52.03503 | 2025-08-17 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff56430f-9532-3947-b126-d208f81231b8 | -13.4367 | -45.88605 | 2025-08-17 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1ad009db-7b42-380d-8772-8bcc9a8fd4ad | -11.35885 | -55.40192 | 2025-08-17 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 65379164-3e16-3518-86db-eb404ce727d9 | -8.80945 | -52.03235 | 2025-08-17 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c68562ef-d7cf-3cd4-95bd-fd0796886510 | -8.5041 | -44.73633 | 2025-08-17 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4ea745cf-336c-3b50-b77b-409a2bdeeabe | -12.87231 | -46.07576 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7faa8692-f932-3688-b04f-f22df23f9a24 | -12.69504 | -46.97593 | 2025-08-17 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e675de1d-c7e0-3248-aa3f-e9e9c88b9d6a | -12.82864 | -45.99347 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b26d3e5a-2e88-3d4e-a828-262d31a67acc | -10.83718 | -45.36056 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6445302c-a2cf-3a3a-9a2f-5c28822e1b3c | -10.83409 | -45.31585 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9272f37d-849c-3c4c-b14f-becdf9f778fc | -10.17976 | -46.83275 | 2025-08-17 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20036165-85d5-335f-a9b3-2cb3734418dc | -10.3296 | -47.73459 | 2025-08-17 04:14:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9aa60a11-40bd-3b32-8702-822db67b15db | -7.60551 | -44.93429 | 2025-08-17 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3945cd5f-c709-3536-bea2-5cbd9528f4d3 | -6.18411 | -45.44028 | 2025-08-17 04:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 95fee8df-e76a-3c05-a82e-4a860933efdd | -6.54301 | -43.02946 | 2025-08-17 04:14:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ba01b2a7-5231-3bf4-bf6e-427de3e52e05 | -12.83956 | -46.03273 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5caf49b-c2e4-3825-a63a-b456c7c44c51 | -9.94254 | -47.95787 | 2025-08-17 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de90806f-73f8-307e-9b75-488b8d7bbd24 | -8.74428 | -44.0409 | 2025-08-17 04:14:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0f193ed4-e635-39b2-b506-6d66cc249fb5 | -11.36368 | -55.42458 | 2025-08-17 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b20981da-bf87-3a5b-bd1a-11e77bc41aee | -6.91544 | -43.85522 | 2025-08-17 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d450d50-f860-3056-bb17-edfa05db45ec | -9.63602 | -50.89296 | 2025-08-17 04:14:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 526c56e4-977c-3f21-bef6-f1dcbf0f1f95 | -13.56126 | -46.96131 | 2025-08-17 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0ee0c44a-5465-36bb-aeca-3a5301f2506f | -7.23324 | -44.22842 | 2025-08-17 04:14:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae6bc759-f0a7-353e-92d8-151fe6aecc17 | -8.04159 | -47.6724 | 2025-08-17 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c3345ce9-fafd-3621-a2bf-9ca427a0dc06 | -8.07563 | -47.70243 | 2025-08-17 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f2813b1-0167-34fa-8ee1-e6b309321de4 | -10.84111 | -45.35752 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86dedb59-7fb2-3d70-af48-70e5258e844d | -12.84129 | -46.03299 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4dd0c3cd-eb6f-37a9-bf94-bcbf7490d778 | -12.89028 | -46.13523 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2edf1d62-7c0e-3dcd-9722-672242609c50 | -13.56622 | -46.97392 | 2025-08-17 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f30e4d8-2674-3de2-a65c-4eea762fdbb7 | -8.03557 | -47.66179 | 2025-08-17 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9fc631dc-ae85-3421-bc24-b1e64d63d6d4 | -12.60794 | -46.90956 | 2025-08-17 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1770cb9b-e693-3000-b2f9-eca3b1c87ca1 | -5.95379 | -46.15387 | 2025-08-17 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README18.md)
