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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca053e68-9033-3281-a478-fa3eabbe95cc | -5.00813 | -44.49888 | 2025-10-15 04:55:00 | NOAA-21 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3cb6405c-46e9-3e46-b67f-d94a0d7d8403 | -4.9065 | -43.45564 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 0f66fde7-1f49-30ee-a93e-12473cf8a831 | -2.86354 | -49.16457 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 492f21ba-55db-3783-956d-0e721ed123d9 | -4.11243 | -48.72596 | 2025-10-15 04:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90113aa5-8885-3b17-91ad-fe78dc08bed6 | -3.97455 | -43.24471 | 2025-10-15 04:55:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 701bc8af-d863-3f42-9bc5-e62b0cdfc2dc | -3.73947 | -44.1402 | 2025-10-15 04:55:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d9cc757-048a-3335-af24-667431787b56 | 1.33685 | -50.73598 | 2025-10-15 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| adaf9859-16ad-381f-86b0-6109827b8777 | -4.27839 | -48.58606 | 2025-10-15 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f81705a1-e612-33a1-a4ec-361f6c92dd9b | 1.85352 | -55.72165 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e32a23f8-abcd-332e-b0d2-dc7f360a4265 | 1.86134 | -55.69516 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 831c6499-3858-3a69-b1aa-70d2b89a8644 | -4.64995 | -43.12844 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 384831ee-d253-3d56-904d-acd61ccb873b | -3.12474 | -50.20909 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d3d59f8-f665-3f97-993b-26651fa09b49 | -4.25842 | -45.58604 | 2025-10-15 04:55:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c8168aaf-aaca-3d73-bc90-cc0898d67fba | -3.56459 | -51.11821 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 5eaa5b9c-0022-3f72-bd72-dfa07c805084 | -3.57419 | -49.44016 | 2025-10-15 04:55:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e0955b57-e218-3736-a55d-78c5b1e4b3d1 | -3.61938 | -48.91513 | 2025-10-15 04:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f87fff4e-bc61-3a84-a261-c06eef2a262f | -4.11191 | -48.72951 | 2025-10-15 04:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de3c8dbd-9052-3f1a-bbfa-fb058107408c | -3.05799 | -44.47358 | 2025-10-15 04:55:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ce5beea4-501a-3dbc-b26b-7290c449d204 | -3.13006 | -50.20813 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f3c3524-ce45-3121-8c01-1f829c40bf2e | 1.33289 | -50.73288 | 2025-10-15 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7051537f-c001-3972-bc50-b486fddd115e | -3.42595 | -50.25111 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2642d08f-77f7-3126-8677-ed1d76534097 | -3.06777 | -49.40482 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3872a86-830f-3c06-93aa-42bd981ef980 | 1.80462 | -55.86492 | 2025-10-15 04:55:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d1842ef4-655d-3aeb-8637-8986fe7cdda7 | -4.35662 | -48.19993 | 2025-10-15 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e4bf83c-8c51-3ee9-9613-716dc31718c8 | -3.56807 | -51.11869 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f3bd097c-1279-3494-b22a-a53e19e8a588 | -3.38615 | -50.17179 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ec3decc-7039-351f-8713-eede1829f1c1 | -4.36441 | -46.77926 | 2025-10-15 04:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b9f4997f-e72c-3faa-af7c-04b2a8c17ba8 | 1.85881 | -55.70784 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e92d9b13-13e8-3203-b9a5-f6283290f014 | 1.86733 | -55.68556 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b9cefb7-dc3b-3a26-af30-13df5d32f1b1 | -2.87644 | -50.73497 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ffc39c1c-6b09-3a93-bd4b-296bd6cefa7c | -2.88346 | -50.73606 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2dfc666-ee26-3072-9620-98d60fddfbe2 | 1.7469 | -55.80632 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1dfa0c6f-13d4-31e8-b0f2-4ed865900e8a | -5.02747 | -44.73438 | 2025-10-15 04:55:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 908fa200-da7a-30f8-8b3c-27c44ff81eff | 1.89615 | -55.65513 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0ad0242-f786-34dd-8ff0-00a691d0442f | -4.1461 | -42.20936 | 2025-10-15 04:55:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 809e9c44-c063-3fc4-ab10-d115af5c3f1f | 1.77793 | -55.7636 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a9a5c3b-98ec-3209-9089-eefccd5571ca | -4.52541 | -48.05248 | 2025-10-15 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0cc2f8d8-fd3e-3b18-8160-9b315a9ea2f9 | -2.94687 | -49.33222 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ed5612a9-91bb-3cca-9246-4f752a8f8489 | 1.85553 | -55.73441 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e3bc834-cc3a-3f49-8618-18a2827401ad | -2.88056 | -50.73158 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| baf8a52b-f122-39df-b54a-e190575d7fd5 | 1.00826 | -51.08827 | 2025-10-15 04:55:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 565bfa0f-2371-326d-ab36-983054c50ae6 | -4.15183 | -43.12703 | 2025-10-15 04:55:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89977b32-1b79-3b35-b8e3-72d45acda157 | -3.73723 | -48.35846 | 2025-10-15 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 81e1669f-af3d-3437-9db2-5bd1d14891a6 | -4.87551 | -45.77496 | 2025-10-15 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e39e504-bf29-3032-9b7d-932b42399e07 | -2.9286 | -48.30367 | 2025-10-15 04:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 3e783573-06c1-35df-8d4c-12ad5926e56d | -4.66234 | -43.12601 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 166.3 |
| 86e83f31-9c18-3e71-9c99-6d9eb1efc175 | -4.25424 | -48.55313 | 2025-10-15 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5f16205-e540-366e-8343-cef1e7631278 | -4.11047 | -48.72616 | 2025-10-15 04:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd89e19a-f04e-3a6c-8361-7923324b9de2 | 1.81496 | -55.85889 | 2025-10-15 04:55:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4c78f57-a76a-38c7-8330-051014f8d614 | 1.07536 | -51.04145 | 2025-10-15 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d2a7b58-8899-35b8-b861-d1615e5e86b5 | -4.87695 | -45.77509 | 2025-10-15 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2696aef-2b06-3321-855a-e8c1368fee50 | -3.94557 | -47.56279 | 2025-10-15 04:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ce72610-b99b-357b-94f9-d521aa049a72 | 1.43601 | -50.84969 | 2025-10-15 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cdcfb62-f6c6-3a70-b79d-6860a6110ec7 | -3.17075 | -48.61149 | 2025-10-15 04:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d56d82a9-7b62-314f-9afa-97331270901b | -4.65645 | -43.12507 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| bdf7945f-5ad8-3d61-b536-0fa9ded8b8c0 | -3.56577 | -51.11042 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51a143b7-5ad1-3b19-b140-6c445ed884b9 | -3.78436 | -49.43114 | 2025-10-15 04:55:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0fbf4a48-64d6-3520-af7a-09d4fe2d7acb | -3.45059 | -51.60879 | 2025-10-15 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3eb4dc22-fbae-3b40-aabe-492e7489d2f1 | -4.89381 | -43.46191 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c722984e-418e-3a61-b5a7-4dff6f2234c2 | 1.81563 | -55.8632 | 2025-10-15 04:55:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbc715a1-95d0-38d7-9720-130202d780c8 | -1.756 | -54.52061 | 2025-10-15 04:55:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 439b4b8d-e184-31c6-8ac9-93f004a4307b | -3.42234 | -50.25055 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0fb1e7d5-9636-3de8-869f-0f51c11feaeb | 1.31087 | -50.72516 | 2025-10-15 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b5215a6-68c1-3ce0-be1c-3338e8fea1bc | -3.14528 | -50.44706 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6d284d2-d65a-3028-bf12-5b9292cca52d | -3.60959 | -50.58798 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2227d184-d266-3d26-b23e-755d8835cf26 | -3.29594 | -50.17202 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51131807-523d-3208-bf15-1100298978b0 | -1.89705 | -51.01136 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c0229f9-083c-398b-8e55-c0f891709db4 | -3.39558 | -50.13413 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94ac4ba4-e03e-393d-ae61-81f014d87534 | 1.07816 | -51.03736 | 2025-10-15 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95c6e6aa-c6dc-338f-af40-ea3e47a61748 | -4.80289 | -45.71684 | 2025-10-15 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de007bea-65f1-3c51-9924-9a9c0ceec8c6 | -4.87022 | -45.67308 | 2025-10-15 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 027c15c2-1e85-313d-a823-3c7fecbbc2ac | -2.44356 | -49.00167 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df0ca8a1-9d74-3b2a-83ea-5e16fe339837 | -4.8937 | -43.46041 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 83d2a350-86f7-3c9d-b893-2513483ff1f3 | -5.03279 | -44.73528 | 2025-10-15 04:55:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 546cc117-629c-3b33-bfde-06349e6b96d5 | -1.27251 | -54.21923 | 2025-10-15 04:55:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39fc7d91-64e7-3e7f-9fa1-27b33c2c4f04 | 2.04807 | -55.79069 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e874eb03-4a19-3008-ba22-7b2b0d297952 | 1.0776 | -51.03379 | 2025-10-15 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b53b8eb-ed5f-32af-b464-adedee726b21 | -3.56698 | -43.50737 | 2025-10-15 04:55:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40fc1afe-4ebd-396f-9201-b68899045da4 | -3.56986 | -49.44146 | 2025-10-15 04:55:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2ae18ec2-e291-3e92-9b9b-1c5a35e26172 | -2.94617 | -49.33688 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4532e2bb-a484-3909-9215-1b38d501c6ae | -5.43343 | -40.9857 | 2025-10-15 04:55:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 9dba4218-0ece-36c8-b79f-527dfcb25cb8 | -4.3591 | -46.78353 | 2025-10-15 04:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4331ccd3-db5c-34d5-8aa3-3e46d528975f | -4.8985 | -43.4707 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| ecae2635-4428-3ce9-8b56-f47b01793f7f | -3.53625 | -44.02365 | 2025-10-15 04:55:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| bf9511bb-405a-3153-ae06-7f21cecb2b2b | -4.7747 | -45.73699 | 2025-10-15 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a375c140-3f3e-372e-96cd-3ea560668563 | 1.8143 | -55.85458 | 2025-10-15 04:55:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 180d1b06-25c0-30f8-b399-49dad012a1f9 | -4.77053 | -45.73064 | 2025-10-15 04:55:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6bc54ca4-8e32-3b9c-8d55-c386175641e2 | -2.24392 | -47.87191 | 2025-10-15 04:55:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4138ed19-4b66-3c66-9177-995e8b52ba56 | -4.91172 | -43.46057 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6da22913-4b4c-3641-b9f2-ae9e5838f2b1 | 1.31029 | -50.72153 | 2025-10-15 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 49c56a13-c569-378c-bc46-0febebb56f1b | -2.05077 | -48.79723 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a4d69c89-f27f-39da-821c-9283161d883a | -4.17879 | -48.14025 | 2025-10-15 04:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52d485a0-f38d-3c67-a08f-d04374b4be9b | -3.08525 | -47.72671 | 2025-10-15 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2c719cd3-bf46-3f4b-87fe-8b4be31cf78b | 1.31323 | -50.7619 | 2025-10-15 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c15f0f3-d6bc-30ac-b98c-db4ae155e2ba | -2.8103 | -49.21132 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 8f0c815a-1dde-3d9a-a0e5-8b9a12baebd0 | -5.25468 | -43.4707 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c43b95e-f1dc-376d-806b-adf25be7c0d5 | -3.07818 | -49.51386 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 881545d8-53f1-3c99-bb45-032615aa6280 | -2.95065 | -49.33282 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e8b97ef4-ad6f-309e-ac2c-06f64e553408 | -4.11117 | -48.02013 | 2025-10-15 04:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fefd0d42-8d61-325e-966d-b69a4a8a370e | -2.81102 | -49.20668 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |


[Clique aqui para ver as próximas entradas](README43.md)
