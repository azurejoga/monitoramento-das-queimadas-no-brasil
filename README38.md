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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d486b4c-deb2-3d20-af0b-e888a52691b9 | -2.31586 | -48.14584 | 2024-11-28 03:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b91acbc3-b1d9-344d-ae57-3321734260c1 | -2.27493 | -46.37432 | 2024-11-28 03:59:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17244200-b955-3023-9673-25c94f3cc0e6 | -3.68072 | -50.87933 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e99e17d9-60c4-3b63-b7cd-3de84f36049b | -3.57759 | -50.33658 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8577bbd1-5030-39e5-9d4a-884ac7a90c30 | -2.9146 | -51.71195 | 2024-11-28 03:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b50bf419-12bb-3a50-b3f5-a2e7decefea1 | -6.48044 | -47.498 | 2024-11-28 03:59:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c70fc0e-5266-3b45-868d-730a3d02b51d | -2.93528 | -49.43867 | 2024-11-28 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac2b316c-9086-34a8-9a79-18f4ae20043e | -3.2918 | -39.2609 | 2024-11-28 03:59:00 | NPP-375D | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d6803605-8d1e-3f95-87fa-3ede40e3d36e | -7.69075 | -42.98285 | 2024-11-28 03:59:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 50d5f818-69c1-36c4-ad59-cfbfb1dddb3c | -3.17289 | -48.58182 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02d55a20-3eff-3151-ab8d-4f6d1d121fe2 | -3.09233 | -53.25448 | 2024-11-28 03:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85258465-f485-36ee-95ac-616d8234bf26 | -2.51239 | -45.1898 | 2024-11-28 03:59:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 572b63bc-b30a-3d3a-b43c-e45a1fdb61b8 | -6.17587 | -42.61729 | 2024-11-28 03:59:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| c8fd54db-266f-3cfe-889a-944c33ba4b99 | -3.20181 | -46.59284 | 2024-11-28 03:59:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| f3996586-6397-32ab-8fd1-cdd6ef8bfdbf | -2.88908 | -51.58242 | 2024-11-28 03:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 720f4922-42af-3989-b7de-a68add332a5c | -3.77872 | -46.68621 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df3a4494-9a59-311b-bbd5-87d4075191c8 | -4.74106 | -46.51063 | 2024-11-28 03:59:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a4ad1281-d36e-3a62-bf47-ddaa4cdbb21b | -3.08246 | -49.20765 | 2024-11-28 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ff5c0391-f11c-322c-bfb0-8bdbf9a1ad5e | -2.85981 | -46.80999 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df3abb5a-e1d3-315e-988b-710c73a73e49 | -3.08111 | -49.21547 | 2024-11-28 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bcf68aec-180c-32f5-885d-99897dd262a9 | -3.77391 | -46.68568 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d018580a-cbf8-38e8-97fc-7492bc886900 | -2.85553 | -46.8368 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 586aa03d-3b4f-3824-b093-d125eb6925a2 | -5.57788 | -43.14838 | 2024-11-28 03:59:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f6da7b19-dddf-306d-9a99-7c98ed35c1cd | -3.22095 | -45.38678 | 2024-11-28 03:59:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36228639-bf4b-387a-ae6b-8ca27a1336e1 | -3.24143 | -50.76827 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 24561976-433c-3208-8e67-f8bece172c51 | -2.51822 | -47.4086 | 2024-11-28 03:59:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 931fd715-fcf7-3318-a32e-33b1881e97b3 | -8.85388 | -39.8791 | 2024-11-28 03:59:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3d52cb9d-b91f-3a9a-9318-1f5032a43d3c | -4.21485 | -50.89007 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6c68e35-581a-3f1d-8143-4cf2d8ac9213 | -3.2776 | -50.61688 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a2c47ce-5da9-3ce1-ae7f-c771b43019ed | -5.38266 | -35.61301 | 2024-11-28 03:59:00 | NPP-375D | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 761bd6ed-3397-3188-9883-f8fc86694fd9 | -3.04338 | -48.51539 | 2024-11-28 03:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47f66eeb-0ce9-355c-9769-314218c595e2 | -3.60436 | -52.54637 | 2024-11-28 03:59:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d1d9dfeb-bbf8-3748-a84e-fa60e66c1e50 | -3.48781 | -50.08498 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f16e658-4658-3313-88ee-74fd29c7fdd9 | -3.24241 | -50.20468 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 154b4321-607e-3744-869d-126f665d5aa1 | -6.1694 | -42.61213 | 2024-11-28 03:59:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a139b46e-3963-3ce7-87ec-8b73e87121bb | -4.31762 | -48.08155 | 2024-11-28 03:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04eec248-d1b8-33a9-bab6-d19170c295a5 | -4.92567 | -47.14172 | 2024-11-28 03:59:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58939f19-c5b1-3f18-b87a-ac5b651fd1a6 | -7.68784 | -42.97821 | 2024-11-28 03:59:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 4dd39cf8-4e83-3434-9f06-97077d490472 | -6.71172 | -47.26295 | 2024-11-28 03:59:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 24693719-d3f4-3c60-99f6-8e8e85be5f89 | -4.21753 | -50.89215 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b3d4c3d-e1a8-323f-84bc-c35985a72ed6 | -1.66619 | -52.73644 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 09b243f7-cdec-3551-96f9-543721ce756b | -2.86854 | -46.86285 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1b169230-a24e-3352-a3a3-ba3a1c0a3903 | -3.5458 | -50.18891 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb948655-f9c0-34e0-a2bf-ae14c48e2246 | -4.72703 | -43.25337 | 2024-11-28 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b89fd17d-3949-37b5-9cbf-12fe48bcf3f0 | -3.07005 | -49.20247 | 2024-11-28 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca86b11d-5bce-3046-87ea-701c1a631c04 | -1.44622 | -52.60118 | 2024-11-28 03:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1055339c-7224-33f8-99a7-883c59705642 | -6.43999 | -47.04387 | 2024-11-28 03:59:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| acc33bc3-cbde-3b65-9e54-2d1d935465d7 | -2.87615 | -46.84732 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 425c2b6a-3b61-3130-b330-2c3e9c413ea4 | -5.95149 | -39.66778 | 2024-11-28 03:59:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| ef67d3bf-ddf0-3540-888a-8632e2ab06be | -4.5175 | -45.72884 | 2024-11-28 03:59:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a948266e-37eb-3ddc-9d25-79b33e434888 | -3.85907 | -40.44607 | 2024-11-28 03:59:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a166b28a-6f95-3272-b831-2c9cfe0f207c | -5.97957 | -45.36766 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 24ad0d86-a5c2-336a-bd11-e20ecadd9217 | -3.17431 | -48.43849 | 2024-11-28 03:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce113db4-3428-3d2f-8c4c-3c8543f9135a | -5.49528 | -47.65878 | 2024-11-28 03:59:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc50f725-d664-3f00-9044-a470c79f9c97 | -3.80513 | -52.36255 | 2024-11-28 03:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e15ec20c-da8c-3d87-8d82-24f230f9e3e2 | -3.29848 | -45.51652 | 2024-11-28 03:59:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2d313a2d-94df-3130-b75f-617c5ea841c9 | -6.95839 | -40.36054 | 2024-11-28 03:59:00 | NPP-375D | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cd141a17-2943-3e5f-afc3-809a7018f669 | -2.60058 | -46.83655 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 42df809f-fb64-3e8d-96fa-b5699898454b | -3.81751 | -46.59937 | 2024-11-28 03:59:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99e2467d-1b7b-3f1a-b0a0-a1b371c6448f | -4.67435 | -44.61287 | 2024-11-28 03:59:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35915adb-d9f6-391a-912b-b51540977eca | -4.66388 | -44.04336 | 2024-11-28 03:59:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fdd3cd50-bbc3-3488-be4c-2c1325511810 | -4.73725 | -46.50485 | 2024-11-28 03:59:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b1c9cfd-ba35-33b7-bbaa-5030a0c64c32 | -3.68855 | -50.23437 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a29393f2-be91-38e2-bdef-9d45509c1a5f | -3.11052 | -53.10722 | 2024-11-28 03:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2bab3890-01fe-3a2c-88cb-1ce820655ffa | -1.71313 | -52.48303 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00c8ad30-32a0-3c95-b3b0-e771ef9cb7c4 | -2.86274 | -46.86746 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e72f7bbd-c826-3bf0-bd02-808b50b77855 | -4.18342 | -44.26343 | 2024-11-28 03:59:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b298be7f-8b9b-37af-b9c3-de8a2c811184 | -6.17165 | -42.62076 | 2024-11-28 03:59:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0c4c7a7b-bf12-323e-9fe9-9d190915591f | -6.16162 | -42.61504 | 2024-11-28 03:59:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a6fb9dd5-b096-3018-8a3a-bdcb124b8481 | -2.83794 | -46.83556 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac8f2a95-dfb1-36a2-ad08-4befab815b12 | -1.67528 | -52.49071 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4eee671e-c3d3-318d-9de1-a97a2c82de70 | -3.39081 | -50.10972 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b13c24ac-dc3e-3e04-b6af-3da7a530cf16 | -3.17489 | -48.43504 | 2024-11-28 03:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96479e44-140f-36e1-a837-42d70b8039d5 | -3.55649 | -51.03463 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ea1afb8b-b413-326f-8b1c-2b253d3b2bbf | -2.83703 | -46.84097 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d87a4aaa-5b82-38b2-8bee-8d38b742c157 | -3.38401 | -50.11318 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9635c643-67cc-3c39-9b3c-6406806a40fe | -5.55159 | -41.42537 | 2024-11-28 03:59:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0e77548b-94e2-377a-8109-ddd2fadb7022 | -2.73039 | -48.89835 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| ebc8ac70-aa20-3be5-b1e8-c76ba7ad584f | -5.67471 | -46.49657 | 2024-11-28 03:59:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5dae37f9-cfdc-3290-82a8-48a5d068bde5 | -3.28382 | -50.61793 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e34841a1-3cd9-3136-90a2-b13c3160ec77 | -3.29405 | -45.51581 | 2024-11-28 03:59:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 732c9f28-dcb7-3465-94f3-5012d5825e73 | -3.56414 | -41.96307 | 2024-11-28 03:59:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4637ac7a-0d7f-3ae5-9b2c-adaba1945436 | -3.2501 | -50.77427 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bf705e0b-b4fd-3e2e-ab74-204822ee64b1 | -5.97305 | -45.35489 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 933e67ed-4e8f-3f1b-94fc-ecb1a534b31b | -5.82638 | -44.10719 | 2024-11-28 03:59:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3ab7ccf3-d262-3893-a00f-1e7558d5cc68 | -3.91227 | -42.41924 | 2024-11-28 03:59:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 523eeff7-b46d-32f1-95fb-6f6550fd819e | -3.67982 | -49.5693 | 2024-11-28 03:59:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea079543-846e-3461-9475-9547d470efaa | -2.72786 | -48.89467 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5ad678d1-1743-3731-8a31-6da47f545b9d | -3.06022 | -51.05793 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a8d1cd15-02cd-390d-9311-d3d8f1b75ce0 | -3.27169 | -50.62643 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec805ef0-776d-3e32-806f-713e14f00119 | -3.78613 | -50.13841 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e6e6095-1a50-36ec-ba20-d451399cff74 | -3.10193 | -50.36746 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4749978b-7a76-3164-ab3f-ba2819738a08 | -3.68972 | -50.23135 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ef667a0-9216-31bb-a4c7-2a2b966bcb74 | -2.84499 | -46.85336 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 647ad875-0734-34d3-93d2-0e21451afa45 | -5.31121 | -43.08529 | 2024-11-28 03:59:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9a0d7b5-ae28-3bb2-8cf3-81e64b40b7bb | -3.13261 | -50.2599 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0accabb5-fe83-3466-94de-6a251f28ecb0 | -2.86728 | -46.84027 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| eefc39b8-1b66-3e7e-bec1-5d856df84b73 | -3.25298 | -50.62326 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 75db5666-c64e-3c2d-ba66-4d0c90cfbb28 | -2.8454 | -46.86875 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8b38bbfb-016e-36e1-8062-091ec1be95d9 | -4.22025 | -50.89597 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README39.md)
