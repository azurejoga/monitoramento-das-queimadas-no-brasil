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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07e4e5ce-33e1-34f7-8d40-5f56ab8720c2 | -11.9715 | -52.4715 | 2025-05-28 00:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 3fdcd1e9-ac54-38a2-ae03-93d02701489a | -17.2847 | -42.623 | 2025-05-28 00:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 3903b802-ad1c-35a0-9207-b47cb4ecc445 | -7.2025 | -43.1171 | 2025-05-28 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 109.1 |
| a6386051-950c-3579-83e9-1c723cc94493 | -10.8213 | -56.9604 | 2025-05-28 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| d5510dee-a112-3264-bd3b-fca6d5a96616 | -17.3041 | -42.643 | 2025-05-28 00:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 8a632423-6bd8-3ae5-a1f8-e59f1e436ad6 | -11.4058 | -44.8432 | 2025-05-28 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| faec90e7-2df3-3bdd-9a49-77066de4feed | -7.6762 | -46.0995 | 2025-05-28 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 4a6edf0f-d68e-3f8a-8c86-4674c1d6297c | -10.235 | -52.2263 | 2025-05-28 00:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 1504f81c-83ab-33d3-9ac0-2df60fde7d04 | -7.0766 | -46.0402 | 2025-05-28 00:00:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| e580cf50-bbc0-3eb3-9101-0fa067698a06 | -7.0764 | -46.0626 | 2025-05-28 00:00:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 0c6ccc90-eb2d-34a0-b3a6-21a8873360cd | -10.2539 | -52.2246 | 2025-05-28 00:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 76175876-2207-38cd-a362-bc4a513fab93 | -11.4062 | -44.82 | 2025-05-28 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 53a4d6aa-1f8b-35d0-9281-00f46e57e18a | -7.1837 | -43.1189 | 2025-05-28 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.1 |
| ecb40e10-f79e-3e70-84b5-01fcde8d725b | -7.6236 | -45.7672 | 2025-05-28 00:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 27d6ac16-c851-32f4-a2c5-10b6442d03ef | -11.818 | -44.2703 | 2025-05-28 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 210.4 |
| 33fbbefd-9f7f-3b0e-942f-028264bbaacc | -11.387 | -44.8227 | 2025-05-28 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| c9a529eb-53ff-32e2-8caa-db408a8a497f | -11.8176 | -44.2938 | 2025-05-28 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| d1219776-5573-3968-a2e4-0cda27d584eb | -17.284 | -42.6479 | 2025-05-28 00:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 1c557b16-5a42-3510-9469-03b3a29a90d5 | -17.2639 | -42.6527 | 2025-05-28 00:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 2f99dbe2-8b9f-3f36-9b1a-382a9beb74e7 | -7.2025 | -43.1171 | 2025-05-28 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.4 |
| 63dc03f8-36d2-39a8-a767-09875144afbf | -11.387 | -44.8227 | 2025-05-28 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 464f80a0-f221-3903-9754-e5dad1e7c221 | -9.048 | -47.7434 | 2025-05-28 00:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 2fff4488-b233-372b-bc5d-1d5bf6a6bce1 | -11.4062 | -44.82 | 2025-05-28 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 5d9d3ac1-ba36-3eb0-806a-89f809aac975 | -10.2348 | -52.2472 | 2025-05-28 00:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 6d5595f4-5e83-38c6-9898-43774a89f620 | -10.235 | -52.2263 | 2025-05-28 00:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 178.6 |
| 8b575ebd-f3cf-3c06-963d-14488d1ccaca | -17.284 | -42.6479 | 2025-05-28 00:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 228.1 |
| e6cd7920-4298-36d6-ab46-d9e6f4001ed2 | -7.1837 | -43.1189 | 2025-05-28 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.2 |
| 6e6fb49e-1d72-3af1-b99d-43423ece1439 | -10.2539 | -52.2246 | 2025-05-28 00:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 1f2a1b65-767f-3a20-93ae-4820cf0baab5 | -7.6762 | -46.0995 | 2025-05-28 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| c4a50ce6-224f-3d07-9c7d-43745b0185dc | -11.818 | -44.2703 | 2025-05-28 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 8e23dc30-2554-3bfb-8b34-dabab3541cd2 | -11.8373 | -44.2674 | 2025-05-28 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| c259ecc3-5d13-3d42-93b2-5d286cc69322 | -17.27634 | -42.65278 | 2025-05-28 00:16:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 153.7 |
| a2665525-798b-3f54-9595-75eb800b64e6 | -17.27765 | -42.66303 | 2025-05-28 00:16:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 128972e5-0ba9-37a8-9886-00f5db7e124d | -17.28697 | -42.66171 | 2025-05-28 00:16:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 19.1 |
| b094adef-6574-37fc-8b4b-e0faafd6075c | -15.91972 | -41.37018 | 2025-05-28 00:16:00 | TERRA_M-M | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| 4d9df564-96df-33cc-8909-b11c4e9f0fa7 | -16.74887 | -42.47574 | 2025-05-28 00:16:00 | TERRA_M-M | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 9cee700c-f667-30cd-aff5-e5aa18fbfb91 | -16.04494 | -43.80426 | 2025-05-28 00:16:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 3a43def1-75b2-34c2-8910-1cb41435f8b1 | -17.28564 | -42.65142 | 2025-05-28 00:16:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 131.3 |
| dc8c3c18-5158-30e4-8b16-d50834069a52 | -11.39085 | -44.82982 | 2025-05-28 00:18:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| f6b873c3-5564-37cf-8b60-f9746734393b | -8.73224 | -47.98991 | 2025-05-28 00:18:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 5034ab41-965e-3643-94e8-d56e0626dff2 | -9.84253 | -44.71155 | 2025-05-28 00:18:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9048dc1e-1732-35ca-b750-838d54a786d1 | -11.81926 | -44.28666 | 2025-05-28 00:18:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 7777863f-b02b-3538-8850-09faf2067ead | -11.4021 | -44.83963 | 2025-05-28 00:18:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 7da795b4-55c7-3344-9d5e-e3b248a96b37 | -9.0442 | -47.75428 | 2025-05-28 00:18:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 8147bddd-0f4a-3e9c-ad6e-d73da551c5f7 | -10.4652 | -47.94061 | 2025-05-28 00:18:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| c4dcd925-8778-3ca8-966e-0f64302a8d9f | -9.20345 | -49.46936 | 2025-05-28 00:18:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 63a4153b-fc31-3a44-934b-83dff0a8d72d | -11.03343 | -44.19867 | 2025-05-28 00:18:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 263da958-8dde-3d1f-8837-8251290f513d | -10.46746 | -47.95861 | 2025-05-28 00:18:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| d76150ca-38a5-3e16-9b1b-573edd191981 | -12.46263 | -44.28598 | 2025-05-28 00:18:00 | TERRA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d691f394-6a17-3aca-9a15-ac35273a5404 | -11.80833 | -44.27738 | 2025-05-28 00:18:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| eb14c056-856b-38b2-ab0e-f5ef0bfe6a54 | -10.4585 | -47.95417 | 2025-05-28 00:18:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 413967b8-cc59-38c5-9e36-90164b0aa1d6 | -10.66492 | -49.4397 | 2025-05-28 00:18:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 50fd3e97-57b9-34f8-aa2b-411eeb6b3525 | -8.72576 | -47.98439 | 2025-05-28 00:18:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| fb56f8f2-3c3f-3d43-82d5-247c0220827e | -8.16529 | -43.39865 | 2025-05-28 00:18:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 94d91a0c-bcc7-326a-aee1-3bcd4569d252 | -11.82038 | -46.14456 | 2025-05-28 00:18:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| a863f188-b8ef-324d-81d9-47ddfa9e5beb | -11.81647 | -44.26549 | 2025-05-28 00:18:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 7f06835d-67cf-3964-8e84-198d02a3b353 | -10.24086 | -52.21817 | 2025-05-28 00:18:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 146.3 |
| cb966f37-046d-3298-ba69-2819ecdf0a2d | -9.19606 | -49.47562 | 2025-05-28 00:18:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 9c087d14-0401-3dbb-b9f3-48dbd72f0850 | -11.39228 | -44.841 | 2025-05-28 00:18:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f01be262-45cb-3f5e-9300-1d2e529b86c6 | -10.45294 | -47.94225 | 2025-05-28 00:18:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f445ca92-7442-386d-8f52-b73275339ce1 | -10.47077 | -47.95243 | 2025-05-28 00:18:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| ca2295d6-933c-3d47-8177-97c67067477a | -9.17892 | -40.31543 | 2025-05-28 00:18:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 470d68d5-a110-3045-b5e4-8788cbb43ff4 | -10.6643 | -44.40956 | 2025-05-28 00:18:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b8409703-6b3f-34c4-9651-ab324bf53387 | -10.95051 | -48.1491 | 2025-05-28 00:18:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 9413c0d0-e204-318a-ab1e-800457f14f28 | -10.24226 | -52.26279 | 2025-05-28 00:18:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| f8056aa4-54b2-3ea2-afbc-fb0d881563f3 | -12.27047 | -44.60371 | 2025-05-28 00:18:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 4856d9ef-fb36-3d75-8c8a-daf611cb277f | -11.40066 | -44.82846 | 2025-05-28 00:18:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| b672d423-e3e8-33f6-b1e6-25c2882c7de4 | -12.2719 | -44.61499 | 2025-05-28 00:18:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 258ed9bb-a62b-37e2-b910-eebf42038746 | -11.03478 | -44.20895 | 2025-05-28 00:18:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| c8a170b7-d2df-3c62-8721-9f2e8df13014 | -11.81787 | -44.27605 | 2025-05-28 00:18:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 264.4 |
| ca1bbec4-7eb7-34bd-bef8-06a145703186 | -9.03031 | -47.73938 | 2025-05-28 00:18:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| f4bdbda7-36e8-3786-a02a-1cdb0c5c73cb | -9.18817 | -40.31403 | 2025-05-28 00:18:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 7b93e951-922c-3e12-b707-cdc3e594f2b2 | -10.98765 | -44.62876 | 2025-05-28 00:18:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9d4f4e91-66e4-3a1b-8182-467c805d7a1a | -11.82741 | -44.27475 | 2025-05-28 00:18:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 28c49bdd-d06d-3419-986f-bd5918a4516f | -9.0421 | -47.73783 | 2025-05-28 00:18:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 4045d82f-3652-34e7-aa81-3aaffef06d6f | -11.82601 | -44.26418 | 2025-05-28 00:18:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a51585d5-69d5-3fa5-a733-1b63258c5677 | -10.24513 | -52.2577 | 2025-05-28 00:18:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 131.1 |
| ce2ac7d5-4a3a-3a87-b60f-197311a83619 | -10.23772 | -52.22316 | 2025-05-28 00:18:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 195.6 |
| da7fb3ed-bf67-331f-b253-fbd66915c008 | -17.3041 | -42.643 | 2025-05-28 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 250226a0-7ae5-3e76-98df-c22700c0d890 | -6.2226 | -43.3459 | 2025-05-28 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 52b48aa3-b25b-3c0f-b00a-377f62441c71 | -11.4062 | -44.82 | 2025-05-28 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 422a23ea-9e17-3243-9cf7-3c1f8eee0ced | -6.2038 | -43.3475 | 2025-05-28 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| ee10e613-2211-39d3-9146-a9c950e03fc0 | -10.2539 | -52.2246 | 2025-05-28 00:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 00affa95-9965-3776-ad86-50844b2e84ef | -7.6762 | -46.0995 | 2025-05-28 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| f8b9a877-2e19-3a79-a5b5-a9a1c6f05057 | -11.8176 | -44.2938 | 2025-05-28 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 6c674651-a921-356c-b3d9-fd775784f6f0 | -17.2639 | -42.6527 | 2025-05-28 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 2d6042b8-b20a-3625-94cf-52eb0afa8ea7 | -11.4058 | -44.8432 | 2025-05-28 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 42.8 |
| d66c2c5d-fe56-3be5-914d-6f103adc0a5c | -7.2025 | -43.1171 | 2025-05-28 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.8 |
| 6b168e89-32b0-3192-b251-899c5e05ae8a | -17.284 | -42.6479 | 2025-05-28 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 195.1 |
| 6c768ee6-8963-3fa7-a0c7-2840cbd498db | -10.235 | -52.2263 | 2025-05-28 00:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 128.2 |
| b1c071eb-147e-37a7-8a74-fe62e18f2d13 | -11.818 | -44.2703 | 2025-05-28 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 167.6 |
| 9c6d1cfa-7521-3450-b915-c257fc46bf24 | -7.1837 | -43.1189 | 2025-05-28 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 60.5 |
| ea3f3f1c-9578-3436-aa74-fff0364c30c2 | -7.67664 | -46.10221 | 2025-05-28 00:20:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 31efe79b-b333-361f-8120-06199fe7e8a2 | -7.08874 | -46.05459 | 2025-05-28 00:20:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| a90b8e3a-09d3-3382-94bc-c57ffd00d68b | -8.14764 | -46.49495 | 2025-05-28 00:20:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 75f987fb-d744-347e-89ac-0840dd36cc87 | -7.08718 | -46.04295 | 2025-05-28 00:20:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 374813bf-a446-3d0f-8662-548840fcae46 | -7.63139 | -45.75239 | 2025-05-28 00:20:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 13ca3e87-2795-3331-80bd-d912e0c2495a | -7.19708 | -43.12248 | 2025-05-28 00:20:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 9006b8b2-57bd-370b-ac8e-7a3505d21bf5 | -6.33626 | -43.36834 | 2025-05-28 00:20:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9cdebf66-092a-3639-87ef-fa0753252aa5 | -7.2059 | -43.12123 | 2025-05-28 00:20:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 35.2 |


[Clique aqui para ver as próximas entradas](README2.md)
