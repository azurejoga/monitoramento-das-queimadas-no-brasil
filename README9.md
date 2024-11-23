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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdee3d7a-8307-3651-9d3a-12c3176ae584 | -2.3283 | -47.0909 | 2024-11-23 00:45:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a85dde2-5c4c-3eb2-9cd6-14e8029cb152 | -6.1463 | -46.6861 | 2024-11-23 00:45:00 | METOP-B | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 34a81ab5-32a3-311b-bdd1-e3a30fadc6f9 | -3.3003 | -50.3587 | 2024-11-23 00:45:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1de7052-98bf-3802-9658-a86fc0dcd87a | -4.6585 | -45.665798 | 2024-11-23 00:45:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 26ddb848-dc38-35b4-a8ad-9fceda2b8ff6 | -1.6297 | -52.609798 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb3b1501-c198-3eb3-9e16-bf0294f1d60a | 0.0991 | -51.204899 | 2024-11-23 00:45:00 | METOP-B | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 9c4b9dfa-e62e-339a-8657-a563658d764f | -3.8096 | -51.998699 | 2024-11-23 00:45:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22432f5a-318f-34c2-bca6-f120b66522f1 | -4.7023 | -45.848801 | 2024-11-23 00:45:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3984471d-fdf1-3c17-9823-a6fa76f7282b | -2.9614 | -53.712299 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2daf8ee-ffa6-3ae2-88cb-dd8d6051cdd8 | -0.9527 | -51.7141 | 2024-11-23 00:45:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 42ba335d-c6c6-33e8-b07c-40d5fafe51d2 | -3.2284 | -53.617001 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07c35d54-76f0-3acb-85d9-b17d5984e739 | -1.7362 | -52.7155 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b35ac53-ccbd-3053-8c1b-9d6735347cfd | -2.7725 | -54.062199 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d5be9cb-da24-306e-b10a-1cc5f35ccb12 | -1.19 | -51.761398 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3309a142-e1e3-31ff-8cf4-f1d81126e544 | -3.8242 | -48.9716 | 2024-11-23 00:45:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20fbb0f5-ad82-31cc-b2e7-1999be067d52 | -1.2978 | -51.737301 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f0d2b94-5fa8-30a2-9f3b-c6f65d807b3a | -4.0858 | -47.014099 | 2024-11-23 00:45:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 66908969-fa17-3878-bdd7-9cecdf671c97 | -2.4527 | -53.6959 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4744b19a-a0ca-3254-b7ed-f8a9bfcf2a03 | -2.5495 | -54.033001 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f2b7410-e22b-39ed-a732-b1080a6ecb6d | -1.6338 | -52.4006 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb2a8469-511a-3295-a6d7-206c29ca247a | -1.4662 | -52.6614 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffbf0bff-ccd9-321d-85ec-6caa65cebb3c | -4.5317 | -42.903999 | 2024-11-23 00:45:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 05e0d2f0-7401-3378-9cda-d93c2a0c9620 | -3.4675 | -54.632 | 2024-11-23 00:45:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0491c968-b885-384c-bd43-615e12930b79 | -1.6243 | -53.313999 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79019c95-bb5e-303c-bd04-14a5ff8b7394 | -2.1717 | -54.4599 | 2024-11-23 00:45:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 051bb8bc-0606-3956-9e3d-86638b10f4e8 | -3.8367 | -52.2533 | 2024-11-23 00:45:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6430e55e-e732-3bf4-9d9b-957a59effe52 | -3.7566 | -52.399799 | 2024-11-23 00:45:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5853584b-adf2-37ad-ac3b-060f2c9a1c0d | -3.2464 | -50.617298 | 2024-11-23 00:45:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ab2e98d-d59c-3b63-9131-5d105866cc87 | -1.6192 | -52.4272 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a3b9f3c-42a9-34a3-874a-9443b554c253 | -5.5394 | -45.785599 | 2024-11-23 00:45:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c31c0af0-3dfc-3d0d-b36f-2fd1924c1695 | -1.3552 | -52.807899 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8825ac40-099d-3cb8-97ec-cab0fbd35946 | -1.6992 | -55.152599 | 2024-11-23 00:45:00 | METOP-B | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 587ca811-3d25-3cea-abdc-43d3de322194 | -4.5469 | -45.8857 | 2024-11-23 00:45:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 36788a58-74b9-3334-969d-e65b6fc4394a | -0.8921 | -51.7192 | 2024-11-23 00:45:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 40b2d88c-ba00-3b6b-8f81-1d2d318f2a0c | -1.6395 | -52.607601 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9226d431-985f-3ede-a62e-527f1f7d112f | -1.7833 | -53.606499 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c1f34cd-ce3f-300c-bc58-f15ad75f775b | -4.0891 | -47.028 | 2024-11-23 00:45:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cead259e-b248-3ce5-b710-91da9e41eb14 | -1.6264 | -52.5952 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bd92b6e-2ea7-3603-8dfe-d8c484bc06aa | -2.6342 | -54.271599 | 2024-11-23 00:45:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7044437e-3dd2-34ca-8479-7883f7959763 | -1.2956 | -52.272301 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ede1903-db03-3cd6-9ecf-e82413b6a843 | -2.0674 | -53.222801 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15badbb3-27e4-3efa-99f6-95f1d6c4c690 | -4.1053 | -42.4538 | 2024-11-23 00:45:00 | METOP-B | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c59b15c3-b817-3dff-9c27-32af4f9cd967 | -2.9565 | -54.7882 | 2024-11-23 00:45:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c94fbdfa-6679-3222-a031-25338e5b1c7f | -2.2384 | -53.6138 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89ed4ba3-b957-3524-a91f-28519830fa77 | -3.5249 | -53.515099 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f991e475-6593-3c42-842e-c34190faaf15 | -3.2378 | -54.2523 | 2024-11-23 00:45:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5dcc1e66-75d1-375c-a5e5-a0476a97d754 | -1.2803 | -54.528599 | 2024-11-23 00:45:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e36f903b-d86d-3b45-aa5c-b697cce827cf | -2.7581 | -54.043999 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb5c3cb8-17ab-384a-92f8-eacc03fd41ef | -1.6017 | -52.259201 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ad1fafd-1612-398e-8539-aa66b9575ca7 | -2.413 | -50.305901 | 2024-11-23 00:45:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8825d303-aa2e-3a23-8d86-41a849e3c05c | -2.6824 | -52.072498 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1da644a7-bc04-33a4-b674-f970a2548736 | -1.2051 | -51.9636 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c258d872-9e92-3ffe-8219-e831b6735b0b | -1.2266 | -51.7864 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 833022ad-854d-38bb-916b-6dc983c8b60d | -1.3856 | -55.1786 | 2024-11-23 00:45:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fae87a38-0f23-3f7e-a2d6-d55c71c1426c | -4.6626 | -45.682701 | 2024-11-23 00:45:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d2b567ca-7e5f-33b9-8171-5393e8b162d6 | -1.6362 | -52.093102 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97d113b0-ba23-3364-854a-886dcb297543 | -2.4496 | -53.682201 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33da73e9-9c4a-37c3-81bd-fbcf43cd68c0 | -3.2373 | -53.930401 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 374bb5c8-ee15-3d4b-bdb6-a10bc14c8471 | -2.6145 | -54.047199 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44f63070-691e-3ef7-9b70-53843f1a741e | -2.1265 | -46.400799 | 2024-11-23 00:45:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc33844e-7416-38c0-b575-d50fa1b85a25 | -3.5086 | -50.458302 | 2024-11-23 00:45:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9323a4d5-4e45-3ef5-9dc9-a925c0b81035 | -1.397 | -55.1833 | 2024-11-23 00:45:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 325cb699-5779-3ec0-aa70-5791607d5070 | -4.5381 | -42.930302 | 2024-11-23 00:45:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dca5da10-70f2-389e-8d5e-3791efee8ef9 | -2.8939 | -54.006699 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 459da895-8d15-3934-91ea-7e900158dae3 | -4.5285 | -42.932701 | 2024-11-23 00:45:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1479e42c-3bf6-3f27-bc14-c10548f76c05 | -2.7859 | -54.030701 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6af85b44-61dd-3db1-9e25-a1f0e3081447 | -0.8425 | -52.545799 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef997a71-c449-3f6b-af83-77bf044e7914 | -1.6133 | -52.582699 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60251f1a-b387-3389-ace5-f4aab3b48d48 | -3.2528 | -54.227402 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58e56934-f119-30c7-b108-c923a66d2faf | -3.2399 | -54.216 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db54d11b-db58-3631-9f23-15e1553709ac | -3.2618 | -53.2631 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ef4b021-e59d-3c33-b287-d703f23367b6 | -2.61 | -54.255501 | 2024-11-23 00:45:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 556f0521-536b-36a9-88b0-2434fbb3ad84 | -1.4676 | -51.125 | 2024-11-23 00:45:00 | METOP-B | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb53224b-4106-3ba8-a701-ca34d8deafaf | -2.5469 | -53.976299 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eef90af6-6329-3254-9e7f-10c56a5c135d | -4.5592 | -48.020599 | 2024-11-23 00:45:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9eaeb33-2c2e-31bc-8eee-5a6b9e18fa34 | -4.4455 | -48.193901 | 2024-11-23 00:45:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73009411-6718-3887-bd9b-91651ac0c618 | -4.247 | -49.684898 | 2024-11-23 00:45:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a97afd6a-213a-373d-901c-7dcc5a16d71a | -3.5421 | -50.514198 | 2024-11-23 00:45:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03b69140-26a9-332e-a06f-488b439fba73 | -3.469 | -54.638802 | 2024-11-23 00:45:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cc52f13-046b-3a45-a93c-dd5aad01f10e | -1.9628 | -46.841999 | 2024-11-23 00:45:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9d25780-1a15-3796-84a7-e41207a7d47f | -2.7657 | -54.077999 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94dc21a7-748a-3299-aaed-a701d8907a82 | -3.0407 | -54.841801 | 2024-11-23 00:45:00 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99fcdffa-dcca-3ec2-be19-d029af961993 | -2.8154 | -54.024101 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aaf1ecfe-e87f-3df0-9445-f6f45cfd1aa5 | -2.6062 | -54.056198 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b256683c-4a26-33f2-9b08-786d78007981 | -3.8326 | -43.9333 | 2024-11-23 00:45:00 | METOP-B | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 14f38670-9577-3948-bf31-1157d9f53159 | -4.3677 | -48.565201 | 2024-11-23 00:45:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5979d980-b6e9-37d3-a403-10386b66b0b6 | -1.6052 | -52.592201 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2d0b18e-78e4-3cf1-8ad9-20158b8ad10f | -3.7987 | -51.183601 | 2024-11-23 00:45:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fc076d5-63ab-315e-ae5a-360f7eb16f0d | -2.5767 | -54.062698 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb8ecf67-e200-3d55-9cab-d32538ec6047 | -3.23 | -53.623798 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d49925bd-f9ae-366a-b50b-ca9d5a1a98fc | -3.7024 | -47.611599 | 2024-11-23 00:45:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc889f21-7682-3c2a-ae04-13c315279d9a | -0.7701 | -51.7715 | 2024-11-23 00:45:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e2ebed87-5ba5-31b9-9795-7e8d08f4dfb9 | -5.7514 | -46.240101 | 2024-11-23 00:45:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f2f6516-917a-35df-91e7-64b1fff1bac6 | -1.6183 | -52.604599 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04095e43-9417-3f1b-9af2-3bbb249d5f2b | -1.1864 | -51.926998 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a77e1f3-9904-3882-b320-da140972e4c6 | -3.2922 | -53.853802 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6756a6d-4b95-3a91-a216-22b0d110d821 | -1.2819 | -54.5354 | 2024-11-23 00:45:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07d30c4d-80ed-308c-8003-c5e3423ec276 | -2.6115 | -54.262299 | 2024-11-23 00:45:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3a1f60a-e29b-3530-988d-48a5c5e85b94 | -3.4871 | -49.9174 | 2024-11-23 00:45:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 215efdbb-3618-3044-b918-a91a6be7dd23 | -3.286 | -53.8265 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
