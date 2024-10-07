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

## Dados Diários - Página 141

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa5c256a-64d4-34cc-8c71-8dda52115502 | -17.00885 | -56.6937 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 80b95f21-520a-3a0f-aeae-71e2fd36d8c3 | -17.00384 | -56.68417 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e50b4cb7-ab6a-3e7a-9219-779fdc414110 | -17.00339 | -56.68861 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3ed2951f-d83a-3bd3-83d4-4d13de2b0810 | -17.00294 | -56.69303 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5b0d8be7-5067-3daf-a290-b89dbc4c5436 | -16.99703 | -56.69236 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 75fafdd5-1a7f-3756-82e7-fc3c75cf5422 | -16.9754 | -56.60891 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 12e24eff-60ee-36d5-9c76-49f368a32171 | -16.97177 | -56.61094 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f30714cd-a851-3021-873a-19d7a49d8f82 | -16.9713 | -56.61541 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5739db3c-8fee-3b51-8fe3-a1a3c1ad8b19 | -16.96947 | -56.60824 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| fa7f6ae5-ae28-3abc-b66e-a28e466f1c0e | -16.96903 | -56.61271 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 70cb32fe-0825-3951-975f-10a0f86bbf17 | -16.96858 | -56.6172 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1b1a52e4-dbef-3f6e-855d-ae3a580eaec1 | -16.94116 | -56.61655 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 009afb58-792e-3e40-90fa-4d1711eb9d06 | -17.15073 | -56.14787 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 46cabf7e-6292-3b0f-b6cc-d0251bb3422c | -17.15058 | -56.1449 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 6468f7cf-d2ff-330d-b1aa-16a68db7e2cd | -17.15026 | -56.15268 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 82b436e4-ba29-3e05-bacc-cff23a527214 | -17.15008 | -56.1497 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1d81e1f9-e98a-353a-b6c6-5014c5ff2fef | -17.14908 | -56.15931 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 63c58030-d462-3c2e-be77-bba386f92880 | -17.14858 | -56.1641 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 4f01afa7-e558-35ac-90c5-ef9c171094a5 | -17.14367 | -56.15678 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 3396a7a5-f1aa-34b9-95d8-3b4faa9ab416 | -17.14296 | -56.15862 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3453f3e1-42b9-38d8-a647-d85cda0c2c30 | -17.05464 | -56.05424 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5705e232-cc23-3cb5-8aed-04652158bb80 | -17.05413 | -56.0591 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 72dffca2-1f68-372f-a2f4-b3f1977151dd | -17.05407 | -56.05588 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e9a25da2-283f-3fc9-931d-e4188cee9b9a | -17.04798 | -56.05844 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 543d82f4-2a02-3333-864b-c59f210de60f | -17.04792 | -56.0552 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9427bb6f-d2be-311e-9d52-a94f1cf6fabd | -17.04745 | -56.06007 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| a81aabee-877e-32e3-b591-8260e986ddc7 | -16.96552 | -56.13758 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a6c99d3a-9aa9-31df-80b3-7f6204087ff2 | -16.96504 | -56.14237 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| d40d1469-0dc4-3543-ae2e-b9557f1b6485 | -16.91765 | -55.872 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 06585414-9111-394b-8e7e-5302cd915bee | -16.86087 | -55.81011 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 00763f7c-e886-36df-9146-7046f4cbf170 | -16.85664 | -55.80806 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 75278695-4aae-3997-8992-e97dcd348612 | -16.69202 | -55.95551 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| aae71f24-50f4-3591-863b-70efbb37946c | -16.69152 | -55.9604 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 6edebfe1-e8ee-325e-b11b-daace19f7b51 | -16.67425 | -55.8839 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d8230c11-0598-32df-9e67-33603336787c | -16.67375 | -55.88885 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2171ec10-2bea-386b-8011-8d945379809e | -16.66806 | -55.88322 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4da51338-dee9-329b-8018-0e839bca4044 | -16.66756 | -55.88817 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 41d4c16e-17c1-3295-9380-95e4e1f32223 | -16.66707 | -55.89314 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 99b584c0-6d93-3ef8-802e-af5bb3229a5c | -16.66658 | -55.89808 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 8bd0be84-4c09-3679-b99b-cc4237bfce09 | -16.65372 | -55.90166 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 03876f19-fed6-3b25-9576-4e545006fc16 | -16.64865 | -55.8996 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 18e55a7b-b149-3fab-886d-8652eadd8a80 | -16.64813 | -55.9045 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 469a288c-9575-33ef-85b5-e7a9a22d39b5 | -16.64754 | -55.90096 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| cefa4ca9-91f7-38ca-92f3-fd6934367187 | -16.64706 | -55.90586 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| c008e8f5-b4b2-3629-a6bf-08dd8b2e6394 | -16.64195 | -55.90382 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9f7432ac-7643-31ec-b17c-8ce172c943b2 | -16.64136 | -55.90026 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| f849cf0c-8bad-38ab-b167-d9bbf62e32d3 | -16.64088 | -55.90518 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 2e659ff3-8bb9-3cbb-87d9-1bfb4dfd815e | -16.63526 | -55.90807 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 16735e9a-5462-3671-b239-bdf7379c6340 | -16.62908 | -55.90739 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 128ac8da-5a75-383a-8458-3182c95eaf11 | -16.62857 | -55.9123 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 232a74dc-3353-32f0-a9fe-ff809dc43cbd | -16.62804 | -55.90871 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 51470f61-131f-34b1-800c-7a30ba6d0610 | -16.62756 | -55.91364 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 13d79b6f-a6b8-3887-b246-4bbe0bf64d0f | -16.62342 | -55.90176 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 0b444de9-802f-36c3-8b81-f63183ffea73 | -16.62291 | -55.9067 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5c063f1c-87eb-3a97-b3a4-3f507f538140 | -16.62234 | -55.90306 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| cebb13e8-bed6-3b2b-b68e-c35c7e1e1b0a | -16.61673 | -55.90601 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| dc1ca041-ecb2-3caf-b617-d1c0f9ad790a | -16.61617 | -55.90235 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 4ac4a5cc-08d5-3cf2-8c6e-39725b1f270d | -16.61569 | -55.90729 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 4122ef4a-a22f-3d21-a801-acc8dee89ff0 | -16.61474 | -55.91715 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 274661e5-879f-3804-aaeb-4d778bdebb80 | -19.6405 | -56.49516 | 2024-10-07 05:44:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1d562fba-65c1-3138-883f-890d70b47ed5 | -19.5871 | -56.53465 | 2024-10-07 05:44:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f6a89b56-979e-32c8-bcb2-4efd6eb11274 | -19.58096 | -56.534 | 2024-10-07 05:44:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4a0c01fb-4597-318e-9ffa-578ee043df14 | -21.41199 | -57.25353 | 2024-10-07 05:44:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e50eb65c-e079-36bb-8b2e-457ebffc9652 | -21.41162 | -57.2577 | 2024-10-07 05:44:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e9cbbafb-89b0-3a10-8482-ab7eba89fa7c | -21.40554 | -57.25804 | 2024-10-07 05:44:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| eb8e41ac-c9c9-3150-a5ea-428b0142371d | -21.40087 | -57.24236 | 2024-10-07 05:44:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8fff3a36-cf6c-3fc9-8128-517de3f1ad80 | -21.4005 | -57.24662 | 2024-10-07 05:44:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0fe460d9-cb48-39e3-b92b-8d6b14167933 | -21.40013 | -57.25078 | 2024-10-07 05:44:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f78d81a6-ae1e-354d-b7a4-2b05239ac99b | -21.39977 | -57.25489 | 2024-10-07 05:44:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a29faec6-2924-3f02-82bd-2ba6b0b23b71 | -21.39486 | -57.24194 | 2024-10-07 05:44:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 360189cb-93c7-3894-bcde-436fb65d6208 | -16.53564 | -57.7437 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| afe3df1c-a3cd-34db-92e6-27cd1f0a16bb | -16.53138 | -57.73212 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 57b1fc96-1658-3a3c-8c72-6f9500f5dc64 | -16.53098 | -57.73567 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ecc061c7-ab93-3ef7-8bc4-4c39ea0085b8 | -16.52631 | -57.72768 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 41b054d9-691f-324a-adde-11a75c1e1d0c | -16.5259 | -57.73128 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e43c3962-d52e-304e-968f-c5a259bbaebe | -16.5255 | -57.73488 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0fa6acb3-2f63-388c-b111-d6f349a09056 | -16.5251 | -57.73848 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 5b8172a6-b2a0-3503-854b-24091dafcb5f | -16.52469 | -57.74209 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c37a727e-09cd-3f49-8924-315bb052db29 | -16.52429 | -57.74572 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| a7f24720-fd3a-3bb2-8f40-aad5e7a52bb5 | -16.52388 | -57.74939 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 3b44264f-82cd-338c-8336-92c827eae0da | -16.52083 | -57.72684 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 494422fc-9895-375d-b44b-fd2760ec0826 | -16.52043 | -57.73045 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9e8305cc-1d3b-329f-b4f1-32ce74ae6fe2 | -16.52002 | -57.73411 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ae08af57-0446-3fe4-adce-82103a87e585 | -16.51961 | -57.73775 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 90c688ff-d6a5-3ee0-aac5-8daf17d692af | -16.51921 | -57.74137 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 6e8b023c-7cb0-3382-aaf5-4053aeee8da7 | -16.5188 | -57.74503 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| cfab8fec-95fc-3622-83df-c7a388f8ea3d | -16.51571 | -57.7228 | 2024-10-07 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3fa75cee-4f8e-37ad-9b94-d86090f2d4cd | -20.34 | -48.84 | 2024-10-07 06:03:28 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ceb843df-a1e0-3f6a-8003-eacc12bd5b6a | -20.34 | -48.78 | 2024-10-07 06:03:28 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7508c129-fb12-3f15-836f-c85626154a26 | -10.8754 | -63.9169 | 2024-10-07 06:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 57563b59-7a8f-3fb2-ac52-10cbecc40013 | -10.8755 | -63.8979 | 2024-10-07 06:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.4 |
| aa0567da-5d84-38c7-92f0-bb82ba364713 | -18.6391 | -57.2578 | 2024-10-07 06:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.8 |
| 8489f17f-8e41-3454-9807-9968659d4865 | -3.55361 | -65.02142 | 2024-10-07 06:29:00 | AQUA_M-M | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2e9b2c97-7787-3e4b-962e-a9d743c4e50e | -10.83939 | -68.35641 | 2024-10-07 06:31:00 | AQUA_M-M | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 37f2ba2d-a3d1-3e01-94e5-ba7756bb7f45 | -10.40063 | -67.88409 | 2024-10-07 06:31:00 | AQUA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a865fc90-9302-3dda-b7f6-c1feb138f23e | -17.0342 | -56.67834 | 2024-10-07 06:31:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.9 |
| 4d69aaaf-fed4-3baf-94b0-3ef8066dab5c | -16.66132 | -55.8907 | 2024-10-07 06:31:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 30.6 |
| ca3e0d90-1c72-315d-b874-25530fa31989 | -16.65557 | -55.88568 | 2024-10-07 06:31:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 31.9 |
| 3137ffc0-90a4-3586-bb62-058c8507e50e | -16.64278 | -57.12585 | 2024-10-07 06:31:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.0 |
| 51fe5b29-e0e5-31d7-82f0-d96046f9d838 | -16.53415 | -57.71825 | 2024-10-07 06:31:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 32.8 |


[Clique aqui para ver as próximas entradas](README142.md)
