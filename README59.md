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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73921037-ee10-3413-b2f8-c75883366122 | -6.28653 | -43.56678 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dd6f67b5-a19b-3ceb-a871-305680b51c63 | -6.41719 | -43.62687 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f331ff1-c152-344e-a72b-c302181988c3 | -8.54536 | -47.4304 | 2025-09-01 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3220b7c4-192f-3b54-84b7-aeba0f2746b0 | -6.37342 | -43.5395 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd7d460f-8edb-3263-9f98-450c4c5e2ced | -7.84556 | -46.95017 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5fe520cb-5009-34bb-9e84-7eaa41da8417 | -6.18671 | -43.34324 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2709b831-b792-3508-9165-067dc0e746b1 | -6.8773 | -41.83389 | 2025-09-01 04:32:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0c62f82d-df9f-3133-af09-34e4e21fe018 | -9.6361 | -47.7963 | 2025-09-01 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2b42c010-c988-348d-bac7-108c62b2d567 | -7.27823 | -60.64885 | 2025-09-01 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2d60f547-7961-32af-a62f-b0f0fc641a45 | -6.23712 | -43.38239 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 006fbe3e-1384-3985-b9c5-734d2fea12a8 | -4.91994 | -43.18251 | 2025-09-01 04:32:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1630d95a-0aec-3065-ae47-d054a373ad22 | -6.4477 | -43.96876 | 2025-09-01 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 23680425-61f7-3cad-a464-4b3f7fea7af5 | -6.24738 | -43.39366 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65ecb094-1b17-3b27-a830-1f6b83642353 | -6.3406 | -53.43045 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 475d835e-8b2f-3012-b288-db6849f535fb | -8.89687 | -47.9642 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45be5006-98f9-3dac-b11c-e2461a7c84b7 | -10.0468 | -48.09941 | 2025-09-01 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e8a03e79-6cab-340b-a68e-c2c18033e45f | -9.67267 | -47.82011 | 2025-09-01 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac080ae6-5ea5-328b-953d-1fed5783bc7f | -9.62226 | -47.81945 | 2025-09-01 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a68c336-0f1b-333b-a859-7508d97b0bce | -6.50708 | -43.56449 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 10892b25-9f02-3bc3-90cb-ba77cc2cc316 | -8.82644 | -47.80584 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e9d86c4-fe8c-3122-a473-83263ae83b27 | -6.634 | -44.25027 | 2025-09-01 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6dbffc34-1708-366d-bfb1-bfe6925db0ad | -6.25017 | -44.86366 | 2025-09-01 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b3203c7-0366-3f5d-bb2c-18ccf4627ed6 | -10.0836 | -48.8833 | 2025-09-01 04:32:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14c59e60-eda6-36df-a6e2-c6c948c818bb | -8.82872 | -47.83492 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3e965de6-b910-3380-b16f-3d8f24047b86 | -9.23707 | -47.07885 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f9fa0ad-653f-39c0-9453-fa65a48a4321 | -7.41795 | -47.43423 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7f60c2d0-ecc2-3139-800d-93e524cbfe4a | -7.67238 | -61.08556 | 2025-09-01 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 83df9a82-b6da-3451-9dbe-c004053c2270 | -7.2772 | -60.65436 | 2025-09-01 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6b3cf523-2917-3b4a-93df-6a145b3e37b6 | -7.76057 | -50.31231 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 79c1851e-7dfe-3994-a066-94237af0e9e5 | -8.90187 | -45.12178 | 2025-09-01 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 729a8f13-fb2e-3d1b-a791-20c762877e38 | -5.04336 | -50.79229 | 2025-09-01 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 75a0c6f0-34a4-311b-b5cb-c7a007e7bef4 | -9.93202 | -51.60947 | 2025-09-01 04:32:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25c71627-6600-3278-b40f-467aa5da5737 | -7.73026 | -50.26027 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d0e8923-3061-39fa-81bc-a01d9706dbe1 | -8.84377 | -49.54108 | 2025-09-01 04:32:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 724e562f-3ca9-3fcb-a750-3e55b577d323 | -6.15087 | -43.34293 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 62e22c10-f21b-37f0-8385-11fc3f706ba3 | -7.099 | -44.56136 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2ea4114-379f-30cf-86d6-b98790f5ab39 | -7.88595 | -47.00034 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a9ff2b4-6d3e-30d9-877e-0a3e7c61c014 | -4.9107 | -43.19108 | 2025-09-01 04:32:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4abed8f1-ba51-3703-832a-d2047ca44a06 | -8.35862 | -52.53332 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d169fa71-266d-3f6b-b68e-cd6d35577f3d | -9.02402 | -50.11404 | 2025-09-01 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6008d983-da6e-3abe-9d99-0733ca9a06a0 | -9.69607 | -48.28116 | 2025-09-01 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9bf1f528-7d66-3a28-a421-6b32f63a4d8b | -5.87854 | -42.99294 | 2025-09-01 04:32:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ba181699-d2b4-308c-928b-b284a5e87313 | -6.61803 | -48.05116 | 2025-09-01 04:32:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 491ed68c-8991-3b24-af79-37f15682d489 | -11.03887 | -45.15133 | 2025-09-01 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 33f6a357-573e-3ed9-95e3-bc7a59012ccf | -6.10153 | -43.19051 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5eb6c16e-c24e-3090-825a-5fb0d984ca7c | -5.6398 | -51.08449 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ac52a7ae-74aa-3ff2-93c1-782d38844863 | -4.92381 | -43.18309 | 2025-09-01 04:32:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 92b5af6a-8690-3a6b-a5f7-ed7dc5236096 | -7.26001 | -47.44534 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b284b80c-de2f-3d80-b05f-510382bfd74a | -6.83739 | -43.33379 | 2025-09-01 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 08406770-fb26-3b85-a004-a2d307a26801 | -9.14084 | -47.94561 | 2025-09-01 04:32:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33af41ad-60f5-35e0-b6f8-0d860358a246 | -7.6355 | -42.65487 | 2025-09-01 04:32:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 44c01330-bb75-3d9a-adc9-f1f8fb6d6e09 | -7.69587 | -44.99541 | 2025-09-01 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 531f1986-4364-36b6-9e65-11cff8abbb90 | -7.08059 | -44.36371 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e678e319-f2e1-320a-b6ce-940a5233716f | -7.38586 | -47.44349 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0a0c762-6159-3057-ab86-b6d22ed5ff56 | -6.96544 | -44.30717 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ce698267-7c20-35a4-8aab-43c40899640f | -6.81697 | -43.33578 | 2025-09-01 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fefd1c55-7aae-34cd-892e-6aa27515edd3 | -4.15124 | -46.78468 | 2025-09-01 04:32:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d657d625-af23-3d35-ad6d-fa4b5ccad7d7 | -9.64166 | -47.80442 | 2025-09-01 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 87796eb3-1c6e-3632-a6d8-d809e61c81a2 | -7.67778 | -42.65671 | 2025-09-01 04:32:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7d92a938-15fa-3bf8-9ed7-297c35ece5a4 | -10.04239 | -48.1059 | 2025-09-01 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ecc5cd8d-ec86-3e60-a09a-fef4f4cd9316 | -10.08415 | -48.8798 | 2025-09-01 04:32:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ba9b4d5-16e1-3a0a-9aa7-77d3319d9dcf | -6.81744 | -52.81877 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 70270203-47ec-3c7a-8159-fe8a54351ee9 | -8.81876 | -47.83334 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 120dbc18-5c53-3315-8cca-9435bddfbf5a | -9.64221 | -47.80089 | 2025-09-01 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fd5730df-d456-32dc-8bbd-e4b9049f5e4d | -6.94176 | -45.56543 | 2025-09-01 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 154842df-2ed2-330e-baf6-3382f791dc07 | -6.2811 | -43.5635 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f60ea54d-d1b2-3ae3-9e07-a66ed333bf57 | -7.09963 | -44.55707 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 19ae08f6-f0c5-3c92-bb57-c1a4ca021ba2 | -9.27031 | -47.11 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af9e837f-b2a9-3e5b-a83d-7046828ac098 | -5.54907 | -43.74568 | 2025-09-01 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8632cb1e-27ef-3f19-9f92-39d89cc3ca78 | -6.2008 | -45.37434 | 2025-09-01 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bbe07d21-ea08-3751-99eb-56b9325bacc2 | -8.83572 | -47.50425 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2a3d839-0c0b-365e-96bf-f6b2f4b953ff | -7.07008 | -44.35775 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 43ddc726-b358-3bd5-a5bd-5aa9f999154a | -8.15809 | -43.00702 | 2025-09-01 04:32:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| eba42254-e5fa-39ac-98f9-efffd1d5887b | -6.81972 | -45.69805 | 2025-09-01 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0c86d18e-3d96-3e48-a0f0-ded5e57897f1 | -8.46342 | -43.62631 | 2025-09-01 04:32:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5908b606-a95d-3f73-a3ed-70f31ce6bb8e | -6.81153 | -43.34529 | 2025-09-01 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0e44ec22-f65d-3bc8-8b48-1b6a51557a5e | -10.04298 | -48.124 | 2025-09-01 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c459df2-9341-38c7-9d16-42f3c5084f49 | -6.07423 | -43.43165 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62fe5ea0-e929-359e-b1d9-bd4953c82a1a | -6.83498 | -43.32303 | 2025-09-01 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 132f88fa-6596-3875-866f-eeec8c6ed7f9 | -6.33311 | -53.43229 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8c2db4b-98d5-3a74-84e6-f639bce05377 | -7.9552 | -46.34744 | 2025-09-01 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7284420-7c13-36be-a44f-1c20d4bfc481 | -5.32466 | -42.86425 | 2025-09-01 04:32:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 94959d23-601d-3ce5-b204-cfd1170d84c1 | -11.08705 | -44.61715 | 2025-09-01 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df0a490f-8e36-386a-86f7-eaa9ca5fc471 | -7.71206 | -50.31208 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72acc756-eb8b-307a-8f1f-bf8c81d07460 | -8.1975 | -46.77942 | 2025-09-01 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 1f12427e-55e7-3f8a-a26c-fe68ece619dd | -7.69527 | -46.69516 | 2025-09-01 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8946f951-f812-3d98-81e8-fe43f920cbab | -5.85248 | -43.2208 | 2025-09-01 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bdd2bac1-80fb-3e69-9d81-7c4825353379 | -8.79854 | -52.08555 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61235fbe-6290-363c-b7b2-7ff6bbe55f95 | -6.18192 | -44.20944 | 2025-09-01 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e409a164-eeed-3344-89b1-72ada6a4c749 | -4.48455 | -48.11734 | 2025-09-01 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9131fee-580b-31e4-b01b-812b3d913b4e | -5.60217 | -45.27475 | 2025-09-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b255360-eae5-3477-9660-f2a998b1027a | -9.92221 | -51.62438 | 2025-09-01 04:32:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c669b92b-d00f-3678-bcb4-86786012b49a | -6.85486 | -52.81449 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a52f4d2b-61bd-395f-8f6d-7d4a9b04ea7f | -6.75674 | -43.79037 | 2025-09-01 04:32:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 516615c9-9c20-363b-a4d8-41fcbfbeb317 | -5.40576 | -43.3648 | 2025-09-01 04:32:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74d5885e-df92-365f-b512-6f27f21c37cb | -6.81262 | -52.82314 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c5bf15dd-538c-3f9c-ab78-46421c440be4 | -6.54623 | -44.61452 | 2025-09-01 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2fcb7ab-1649-3639-88a4-db5466281a37 | -6.19542 | -43.34065 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8a7c7f8-8344-3055-a6be-96894dfbd2b3 | -6.6342 | -44.37587 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f548b27-a5b7-380b-94e9-d7c410c60d99 | -8.34005 | -47.44166 | 2025-09-01 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README60.md)
