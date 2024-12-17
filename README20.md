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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f2ec179-d841-3c0f-8186-8bea519fcc79 | -1.54005 | -53.73283 | 2024-12-17 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e59e955b-b079-3095-9225-3d2c1cd45d96 | -4.96963 | -44.9679 | 2024-12-17 04:44:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 16048f91-42a2-3c49-a89a-05621165428b | -3.23959 | -46.80073 | 2024-12-17 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f5c80187-a185-3344-bb15-e1facbbb048e | -4.90476 | -42.07886 | 2024-12-17 04:44:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 473cab5a-4960-3cf6-ab4e-03c95a6d209f | -2.08032 | -53.39038 | 2024-12-17 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe9b8df9-8d68-348e-a1d4-a329ed558faf | -4.9 | -42.075 | 2024-12-17 04:44:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 38662280-9fce-3b58-9630-2108f6b4c4da | -5.113 | -43.20532 | 2024-12-17 04:44:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f1655ff-64fb-34fa-8554-f667eb0ed12a | -2.89306 | -54.17987 | 2024-12-17 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31551f0b-336c-36b3-8318-4d648aa9f0be | -3.12312 | -53.24229 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23090b35-1a87-3b31-ada2-b889417d13c7 | -5.70374 | -46.79381 | 2024-12-17 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bf922e3f-e2be-3fdf-8bdc-734f6ec5f690 | -5.13683 | -46.18374 | 2024-12-17 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79bca705-e1d3-32c6-8516-b1c68d29d7f8 | -4.79402 | -46.3938 | 2024-12-17 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5ae14196-d717-3ecc-a8ff-ca18b8bf2214 | -1.29888 | -52.83748 | 2024-12-17 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 873a0866-4666-3699-a36f-e80e1504b9c1 | -3.75519 | -47.9999 | 2024-12-17 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf0b988c-f2f6-3f3c-8244-5e59823744cf | -1.66626 | -48.08855 | 2024-12-17 04:44:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91ffd1b4-f18d-31b0-a353-1643420411ae | -4.07252 | -47.09986 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f720c5f-4a4c-39c4-bee2-2607800d1a73 | -3.01185 | -48.03038 | 2024-12-17 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f244a53-38d6-34b1-92e9-2041a2426654 | -4.05057 | -46.92248 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 28632eff-0b87-3600-b8b2-19ce48f3bdaf | -5.0857 | -43.91373 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| c4873ee3-9ee8-3cd8-9e56-ff2e2ff5f193 | -6.09002 | -46.6673 | 2024-12-17 04:44:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60184837-7515-3c3e-888f-f9e844bd1642 | -4.04989 | -46.92696 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 13fcfcba-a26a-3f0f-8fc6-4c2de0abd07f | -5.21219 | -44.56285 | 2024-12-17 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e9f3f44a-2dfe-3c03-bec7-d4d0667b611d | -3.15434 | -53.1852 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0a06431c-bc6d-3363-879b-4c9df1deadbd | -4.01987 | -46.82252 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c456f3e6-c6d9-3e26-9e9f-72ebe11e4eaf | -1.28493 | -53.18606 | 2024-12-17 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9314aa63-2d10-37fb-8dc9-c6456a85ae4b | -3.99935 | -46.89872 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3797d37-2833-3865-a523-a8ddc3481665 | -5.13744 | -43.24097 | 2024-12-17 04:44:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 80c4a88a-09f9-3a33-ad7d-b086877f3196 | -4.04314 | -46.9213 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1612781b-a246-33fc-b207-530c98b9708c | -3.43802 | -53.98872 | 2024-12-17 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79398420-7a50-36b6-85d3-7372aa2d6ef8 | -2.68719 | -48.45752 | 2024-12-17 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce031ac3-a07f-33a8-8397-4d1732881b38 | -3.87132 | -47.02843 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3871de25-17c1-3a55-bbd7-118abf2da7b0 | -5.09627 | -43.90554 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| a8cdad47-348a-3f7a-a875-1f58137f48ee | -3.12377 | -53.23827 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 427e741e-ddfc-3fd0-9ba2-a9d2c0d2e23b | -2.49162 | -47.27357 | 2024-12-17 04:44:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62f19cd7-8fd6-3e6f-a98d-1320ef1f1b4f | -2.77622 | -48.57962 | 2024-12-17 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5da4a65d-b41a-39eb-a229-28daf1c724d2 | -5.62886 | -44.83798 | 2024-12-17 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 533ab211-be5f-3ef8-9167-6658e34002f2 | -1.29658 | -52.82883 | 2024-12-17 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcd99449-6ba7-3656-ac79-74b6f5d695af | -5.08253 | -43.90664 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1d2c03c2-c925-3f3d-b81e-ea303e25c252 | -3.16045 | -45.97296 | 2024-12-17 04:44:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d2778fb-c206-30e6-aa31-a758be2351b3 | -5.10026 | -43.91375 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c2ed3509-34ac-3712-ba0d-9c3d648c9f07 | -3.04996 | -47.96933 | 2024-12-17 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1f00a9b-c2c1-3cf2-b7f2-9be376da2f51 | -3.76294 | -47.17029 | 2024-12-17 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e953cad8-6dee-35b9-b127-ba98418c7467 | -2.57622 | -49.4148 | 2024-12-17 04:44:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0e47a17-48e4-3761-8860-515bb104dfba | -5.50893 | -36.83133 | 2024-12-17 04:44:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ea6150a9-e338-3856-9b45-b9ac111a0c15 | -5.08573 | -43.9166 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 56a25f76-bc0b-3fca-aefb-69d4e44eab53 | -3.43831 | -45.59934 | 2024-12-17 04:44:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c97cb907-c758-3c05-934e-fd02d626fa21 | -3.98454 | -48.39964 | 2024-12-17 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c80bcfd-517c-3326-9392-fb0e716930e2 | -3.9635 | -47.0316 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c45acec-fda9-391f-959d-bf771c5bde61 | -5.09098 | -43.90965 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| b964a4d8-62eb-30ba-8a8a-d82dcd40dbbe | -3.01534 | -48.03091 | 2024-12-17 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8827aba-7d46-3a93-92c8-5bc2ee16dc37 | -1.46044 | -46.81187 | 2024-12-17 04:44:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c14cb253-c1e6-3abb-b216-7da48b7c8556 | -4.88995 | -44.1699 | 2024-12-17 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d90e82f6-b7b0-3089-a85e-98d667c57e3b | -1.5438 | -53.73339 | 2024-12-17 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c508e6c1-3cb6-39ea-90ab-347beff3c123 | -3.09669 | -53.2595 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbb92901-3ad3-3e1b-97f9-8ed7ccd1eaab | -4.25224 | -47.57574 | 2024-12-17 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e3e0f7a-f1c6-3793-89d9-b231d5d76247 | -4.20381 | -44.3603 | 2024-12-17 04:44:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 13d4241e-bb3c-3b31-9055-491484b53905 | -4.07412 | -47.1032 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77ad1e01-a559-33ae-868f-155b3c5ef87d | -4.76179 | -46.70802 | 2024-12-17 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1916d9b-0899-3135-a64b-6ca742e0cd74 | -1.89553 | -46.81725 | 2024-12-17 04:44:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5a6ebe66-fd7a-3874-be87-84b8488eb8de | -4.38032 | -46.54741 | 2024-12-17 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0039ab31-0f86-30d4-a443-12b6526711f6 | -4.03954 | -47.01947 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7482ad99-3204-3644-88ca-eaab02df70aa | -4.00854 | -46.89804 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d2d3aa0-e2d5-3719-937f-79e58c73a133 | -4.03384 | -47.03197 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c54a899-5dea-3fe4-ae51-1daff341a409 | -4.09474 | -46.18336 | 2024-12-17 04:44:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1110616c-c87d-3f1e-a932-b641a9b4ce15 | -2.7768 | -54.49687 | 2024-12-17 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2f24a0e-887b-3d54-a9d6-10f2e6f1181d | -3.02894 | -47.82717 | 2024-12-17 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92b3bde6-52f5-3c2d-9902-52f1653bdd8b | -4.89955 | -42.07808 | 2024-12-17 04:44:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 17a84e45-9040-38c6-b4d1-339724f541db | -1.45889 | -53.48111 | 2024-12-17 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| faaadddb-4f46-3b9c-b221-2336b03d8eff | -1.42917 | -55.45722 | 2024-12-17 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7e259f7b-e5c7-3120-a080-573bb6dc38c1 | -6.08677 | -46.66441 | 2024-12-17 04:44:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c715dcd-7435-369a-9b83-f00d2fdb7d49 | -5.91185 | -42.89017 | 2024-12-17 04:44:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 03c692f6-beda-3a27-a2a1-006f0ccf93f7 | -5.50794 | -36.83866 | 2024-12-17 04:44:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 3.5 |
| bc45175d-d110-3ab6-9c27-6535d9021119 | -4.88929 | -44.17438 | 2024-12-17 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5064ba48-2298-3ddc-9582-9c7115ec61ec | -5.14547 | -46.18003 | 2024-12-17 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6fe80f65-5b9a-31e6-a172-26a61baa15e1 | -6.07857 | -44.1414 | 2024-12-17 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 824076cf-4c60-3efd-8234-892802a429a0 | -1.28063 | -53.18968 | 2024-12-17 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48f2b831-97d9-3bb3-be50-fa944978ada0 | -4.57288 | -46.58378 | 2024-12-17 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8359368f-51a1-3c8c-b2cb-e361b1071ec4 | -4.1005 | -46.69645 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97b73761-67eb-3b79-8823-304db8cbd8d3 | -1.54845 | -53.43184 | 2024-12-17 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c926da6-87c8-36ef-bcef-7e1b172e9306 | -5.96377 | -41.59247 | 2024-12-17 04:44:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 005a6174-5cc9-3fad-8d1d-bdff37ac78e0 | -2.08198 | -54.23532 | 2024-12-17 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cb5d282-639f-36cd-b239-49b9c0656a5d | -3.87585 | -47.03607 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3a59d6f7-b7cb-3242-ac06-d5e2c97e8e0b | -4.65627 | -44.3292 | 2024-12-17 04:44:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a50ac1ae-b786-3005-8290-89c7793f7089 | -3.2389 | -46.80513 | 2024-12-17 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| dc6e2a0e-61a7-36ce-9cf9-12c718548272 | -3.87432 | -47.03339 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f9009697-749b-3f6f-a2d0-4000759d42e5 | -5.09706 | -43.90377 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 7a2030d8-cbe9-31b3-9e82-81da34f04cdb | -4.10192 | -46.68722 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ede958b0-e46e-3a86-81b8-16de060ee23c | -5.2123 | -43.2962 | 2024-12-17 04:44:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a2fa632e-7454-3b4c-a30d-08c75c651bb8 | -4.56388 | -46.51461 | 2024-12-17 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ce4208d-8bb6-3305-b9fb-f272eaf9f02c | -3.67245 | -47.12751 | 2024-12-17 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b037a264-2e0c-362d-b1fb-11c5562860f3 | -5.09566 | -43.9131 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| d28f6eea-7823-36f5-a994-ea78d8a8dbd7 | -3.76424 | -47.16172 | 2024-12-17 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 491e6346-fef0-373d-8c3c-c198e6366f37 | -3.3791 | -53.24725 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2325112a-abf6-3007-b67f-fe5b69536f2e | -3.72047 | -50.16262 | 2024-12-17 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1871f1ec-f121-3f11-ad66-ea47b45a503c | -4.07487 | -47.10897 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ae25638-d33d-3a9d-b142-7a241d464d8e | -4.05195 | -46.91349 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8cfbec82-8e95-3f4f-a567-d87af10aa6dd | -3.72101 | -50.15916 | 2024-12-17 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 447725d0-8cf3-313a-8511-f9835c1b44cd | -2.51371 | -49.05549 | 2024-12-17 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5687f36-66f9-369d-a144-d8b94fbb75c1 | -1.46407 | -46.81242 | 2024-12-17 04:44:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9c66f10-297e-363c-8de8-d682da05f1f8 | -2.76808 | -47.39146 | 2024-12-17 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README21.md)
