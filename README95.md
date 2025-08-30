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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 806d555f-cb68-3f57-a0ae-052ff9cfd34c | -6.17623 | -43.34155 | 2025-08-30 12:14:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 625.8 |
| cd6f39ec-460c-31a0-be26-e9aa054de663 | -6.18518 | -43.99984 | 2025-08-30 12:14:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 99d3a1f3-2751-31bf-a492-c759d0112879 | -7.24959 | -45.46259 | 2025-08-30 12:14:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 6be286bf-1d9d-3e40-b022-981d484cffee | -6.17603 | -43.99861 | 2025-08-30 12:14:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| d97c6761-1193-3dac-a27c-9a0ba1decab4 | -3.48349 | -39.10897 | 2025-08-30 12:14:00 | TERRA_M-T | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 88.0 |
| 3b31c67c-a0c4-35a1-b2a2-9327062b858a | -7.65281 | -42.64864 | 2025-08-30 12:14:00 | TERRA_M-T | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| ce0195a1-f537-39fc-a7ca-9b25ca7b845e | -5.76384 | -45.21857 | 2025-08-30 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 938ce4a3-35b3-37ea-a55e-286e9724651f | -4.27007 | -40.93672 | 2025-08-30 12:14:00 | TERRA_M-T | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 19.7 |
| 062b7d50-f503-3677-9b10-5d05ac9a5660 | -8.86864 | -45.74731 | 2025-08-30 12:14:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| c972414f-5330-3e23-8e18-e72fafe9f701 | -7.96347 | -46.39618 | 2025-08-30 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5b40e627-9afb-3a0f-9c3c-a2191b0cd5ee | -7.60164 | -42.72486 | 2025-08-30 12:14:00 | TERRA_M-T | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 572e1673-312a-3f5d-aa0c-9950fc68d80a | -6.17467 | -44.00818 | 2025-08-30 12:14:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 56cd96bc-ccc0-3918-ad88-f836b009dd1b | -7.0995 | -44.30923 | 2025-08-30 12:14:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 9764b056-85d9-3a94-88cf-bf504ea0b1cb | -9.13606 | -49.63051 | 2025-08-30 12:14:00 | TERRA_M-T | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 268ce782-e63a-3576-ba31-d7e9da9e6a33 | -6.2181 | -42.75517 | 2025-08-30 12:14:00 | TERRA_M-T | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| b6a69130-d6c1-3d4a-8373-479b8d713791 | -8.83023 | -47.47607 | 2025-08-30 12:14:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d34a3ca6-3b12-3b22-bfc9-9a262a448798 | -7.39419 | -45.92862 | 2025-08-30 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bdd9138b-da93-3dc1-986c-d2a4ec9c446c | -8.08027 | -48.41863 | 2025-08-30 12:14:00 | TERRA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 816629c7-e04e-3198-99f7-e8e2e9c696c5 | -6.76723 | -44.6427 | 2025-08-30 12:14:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 20a25c78-81f9-322c-9f4c-c6ae67c78ac1 | -6.19432 | -44.00115 | 2025-08-30 12:14:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 254a0449-8b2d-3328-a3aa-60e82b9d02be | -6.20682 | -42.76483 | 2025-08-30 12:14:00 | TERRA_M-T | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 27.0 |
| 78842bd9-f1a3-311a-b349-1582f5a3b115 | -8.84567 | -47.81031 | 2025-08-30 12:14:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b1e263fb-cd89-3164-a695-6f51f1d00bd3 | -6.42596 | -45.60666 | 2025-08-30 12:14:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 90da2788-f7fc-3f59-b852-599af3ad2d0b | -8.84707 | -47.80083 | 2025-08-30 12:14:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| df4be866-698c-3418-b0bf-9c8d14c3f416 | -11.00962 | -46.95477 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 57204596-7d3f-33cf-bba9-76c59b03b35d | -13.56871 | -46.923 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 647c2388-92aa-3a34-9fe2-c2066cefd90d | -10.02843 | -46.01934 | 2025-08-30 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| dc19204b-a300-3515-88c5-3128819dd4fc | -13.3554 | -46.99947 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 7c8b8db8-f33f-3855-9bdd-1d781be2eb4f | -12.66625 | -48.17995 | 2025-08-30 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 40.1 |
| c8a4033b-23a4-35e6-b6d3-8dd71bf8385e | -14.0242 | -44.55484 | 2025-08-30 12:17:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 1bde3ee2-068d-3479-b01d-ac727ac2f311 | -11.89089 | -46.4705 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| ff7eaf6b-227d-34da-9012-1a164e70821a | -11.01113 | -46.88187 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 891dc6fb-3039-3187-a6fe-ef3b246f71e1 | -11.88724 | -46.36899 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 9f05bf2c-d248-33f7-b10a-fd5ebb74c2d3 | -10.14029 | -46.77588 | 2025-08-30 12:17:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| ca43c8ce-3f2c-3cf0-8658-32883f6454f3 | -11.87837 | -46.36777 | 2025-08-30 12:17:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7f68b3a1-54f8-3fa5-bdff-f9a4536e1f67 | -14.852 | -46.7774 | 2025-08-30 12:17:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 14672c92-1a6c-376e-945c-7d6110af040d | -11.89986 | -46.40743 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 4c8c772d-b9b3-31c0-b028-0659cbdba52a | -11.07268 | -44.61617 | 2025-08-30 12:17:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 76c5c64d-e5a5-314e-b30e-3bba91716e27 | -11.85036 | -46.50143 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 2839497d-fd77-3f5e-94ad-c66836af8cf6 | -11.85604 | -46.38569 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e6ec0ec4-20b3-33e9-9685-fc13dcc903a7 | -13.37806 | -47.03043 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 866d8420-c1bd-3311-b56c-07e3db1eb5a8 | -13.36792 | -47.03817 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 18916b3a-e894-36f0-9d90-d3f61475e9ef | -14.55605 | -51.99276 | 2025-08-30 12:17:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 2d7583d7-66df-37fb-bd38-775c4882b1e8 | -10.98802 | -50.78183 | 2025-08-30 12:17:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 00567524-9fc9-3fec-92a5-b30ce810795c | -11.87583 | -46.38563 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 742b06d3-3df4-3def-be33-37d3693e95f0 | -14.45799 | -52.02792 | 2025-08-30 12:17:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| c2aa1dc5-b658-327d-a218-1372c2ddb820 | -14.61992 | -48.06824 | 2025-08-30 12:17:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 03b41d2d-c68c-367c-af63-32129cf3774f | -11.34449 | -43.60004 | 2025-08-30 12:17:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 214362b0-4265-3189-984a-55ca1eaddb52 | -13.2833 | -43.67355 | 2025-08-30 12:17:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 77c0d849-4efd-33bc-99a0-a88b96feca5f | -9.70392 | -47.05386 | 2025-08-30 12:17:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 3539b008-b7b2-3a10-bf7c-d926e97e9e7a | -11.89484 | -46.37917 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 125.2 |
| ba1dbb75-6a22-3518-a684-973beb5795d6 | -10.04358 | -46.03975 | 2025-08-30 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 9ed8e721-f111-3e32-8b83-940159c170f9 | -14.61856 | -48.07753 | 2025-08-30 12:17:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 28ce8a0c-3723-300c-b9ce-9abd48860a11 | -14.37595 | -47.8446 | 2025-08-30 12:17:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d767e17c-7c8a-37cb-989c-e3f95ceb149b | -13.35344 | -46.87328 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 117894dd-2756-39c7-a7cf-8be68139b39a | -15.31466 | -46.09062 | 2025-08-30 12:17:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| cb2a4b4d-7870-3f98-a60a-ea61a6212bee | -14.01161 | -44.57544 | 2025-08-30 12:17:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 41f69548-2fe7-3cbc-9fb1-94066aedb9ad | -11.00077 | -46.95349 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 02e9b3b6-3a69-3006-a829-c69232ab9249 | -15.17871 | -48.03119 | 2025-08-30 12:17:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 7bcdc2ee-d631-3590-8f49-1bb5cf76a602 | -13.38949 | -47.01366 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 0b9940a0-cb39-3df7-b43b-5ecd5e7e8ca3 | -10.70009 | -47.05612 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 0c91a7c1-8e99-34f5-a108-6d9c95c4cb55 | -12.65448 | -48.19732 | 2025-08-30 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f056063f-fc30-3efc-b62c-bfe5a2f5de42 | -11.3301 | -43.63288 | 2025-08-30 12:17:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 218.8 |
| 0f19d08d-4e3e-37bb-b39a-e93b39fde710 | -12.65726 | -48.1786 | 2025-08-30 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| daaa0fff-81c5-32c3-94b5-1d60ac58aefc | -14.83506 | -46.7595 | 2025-08-30 12:17:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 20ea5d60-8891-372b-a1b5-5be8a6f79fb0 | -13.36682 | -46.98271 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 50d7649c-51d5-300b-a0da-f1d5aca51941 | -14.01451 | -44.55357 | 2025-08-30 12:17:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 01d1da2a-1beb-38ff-abbe-094895764bfc | -10.01817 | -48.05498 | 2025-08-30 12:17:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7940b298-ea99-3379-ba51-52dda3aa4d27 | -11.3316 | -43.62138 | 2025-08-30 12:17:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 33.8 |
| beac8869-0e0a-32b9-b7ca-b8bdbaf093d8 | -12.84631 | -48.08629 | 2025-08-30 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 524932f6-43e2-37bd-92fd-0bb24907c776 | -13.35281 | -47.01754 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b7057389-9d47-3b84-9abf-db8a51455386 | -13.37935 | -47.0214 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 28.2 |
| f3d9da60-a728-30e3-906b-8b64e9383e67 | -13.50811 | -46.95454 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 33.8 |
| e8dfda9c-18f4-3af7-89e0-59b95232cdd5 | -10.94314 | -46.83862 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b7cf2729-df88-3692-8c74-e687f5c1f012 | -13.67722 | -46.87133 | 2025-08-30 12:17:00 | TERRA_M-T | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fc61fc8b-11cc-3504-bf10-de897a4c671a | -11.82679 | -46.46408 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| ac2b3079-9b3f-3741-aa1c-bff58ac1fbdd | -13.68475 | -46.88188 | 2025-08-30 12:17:00 | TERRA_M-T | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 4dc16ad5-08d9-344a-9100-095d08742c10 | -11.82808 | -46.45507 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 1bca6d67-8fdf-3d4f-b685-fbc8bacd1088 | -11.86432 | -46.46672 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 02e3eb8c-2218-3b0f-8172-6d549eec404f | -17.85734 | -44.72916 | 2025-08-30 12:17:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 39.2 |
| a7a6bb4f-8d3b-37dc-83a9-fd4e8bdb5fa3 | -10.72562 | -47.00482 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| de04c3b9-f243-3a88-a8ba-abfe30549623 | -12.83183 | -48.1222 | 2025-08-30 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| ebdd3a8d-5aeb-3709-8eda-4cb0e60803ee | -9.69511 | -48.30353 | 2025-08-30 12:17:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 4df5a598-9738-3975-a03a-8baac924c43c | -11.88852 | -46.35992 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 5a674dbb-89be-3b6c-9326-3ae03f81a556 | -11.77137 | -44.75085 | 2025-08-30 12:17:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 127.2 |
| b1f73c4c-d553-30d9-9021-34a0faeeff8b | -9.85836 | -48.07737 | 2025-08-30 12:17:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 58a86094-992f-3b1a-88b7-95cd20c49240 | -14.62881 | -48.06941 | 2025-08-30 12:17:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 42c69c18-4ceb-36be-8b22-66741f508bc6 | -14.98347 | -48.16699 | 2025-08-30 12:17:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 361c0c3c-e9a8-3134-8019-18e64c9411ba | -14.98212 | -48.17622 | 2025-08-30 12:17:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b02ca303-e68a-301f-a8a9-89468acbe485 | -10.99863 | -46.84355 | 2025-08-30 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| e11b7fd8-7c2c-3c1c-93b9-1b5cd956d054 | -11.35595 | -43.58973 | 2025-08-30 12:17:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 47be9e11-2596-3b1e-a83a-a0bd0784c4ce | -11.84707 | -46.44861 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 42.5 |
| e232de67-2162-3994-8698-32bc98d44f2d | -9.69367 | -48.31322 | 2025-08-30 12:17:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ec88608d-0248-3bcb-86f2-0638b4cc3d44 | -9.77448 | -49.88163 | 2025-08-30 12:17:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 37049e17-d743-34c2-9909-67eaaff6fc65 | -11.87965 | -46.35875 | 2025-08-30 12:17:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 4ec2682e-c869-3d0e-9b77-73f04a6aa50a | -12.64495 | -45.29689 | 2025-08-30 12:17:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f2047580-3aee-3150-886c-8953f935b193 | -13.34784 | -46.98915 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| fe6ef57b-080d-3d18-abe9-82d66f520730 | -12.85318 | -48.16363 | 2025-08-30 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b22abff7-2717-3bf6-bde3-b2dc9cb6177f | -14.46033 | -52.01359 | 2025-08-30 12:17:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| e9aefade-f6b8-3a74-a75c-3c8895bd16e9 | -13.39078 | -47.00463 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |


[Clique aqui para ver as próximas entradas](README96.md)
