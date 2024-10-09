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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c481a2c-cc66-3232-a417-483c38b8a028 | -17.1563 | -56.824001 | 2024-10-09 01:24:51 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 420bed77-e40a-3ad7-ac9d-87ee255395bb | -16.8967 | -55.761299 | 2024-10-09 01:24:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 85bfd33e-a47f-35c3-926b-3707b543fd4d | -16.8988 | -55.77 | 2024-10-09 01:24:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| df5a35ef-78de-3c95-9b11-5cabb304b6be | -16.9009 | -55.778801 | 2024-10-09 01:24:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f35d05e0-72fc-3508-9c3b-bfbbdf4f030a | -16.902901 | -55.787498 | 2024-10-09 01:24:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c2513c15-8289-3d5e-880f-1b2ec5706bb9 | -16.905001 | -55.7962 | 2024-10-09 01:24:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 88f8ca39-e85e-3e60-97ef-302b5bde52de | -16.907101 | -55.804901 | 2024-10-09 01:24:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 26846702-9910-356d-8774-75cee11c7f1a | -16.9091 | -55.813499 | 2024-10-09 01:24:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9f2ecace-a62e-321b-97fe-ce7eb8c5c997 | -17.1429 | -56.810799 | 2024-10-09 01:24:51 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2189bff7-7576-35be-88a6-4ef25ec5ce2d | -17.144699 | -56.8186 | 2024-10-09 01:24:51 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ef2cf4da-ddf4-336e-9b21-8920978a349a | -17.1465 | -56.8265 | 2024-10-09 01:24:51 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5585ca4b-5b78-3a71-93de-25cec8ff43a3 | -17.1483 | -56.834301 | 2024-10-09 01:24:51 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2a13ac92-cb29-30dd-b433-fe9aa52644a6 | -16.8869 | -55.763802 | 2024-10-09 01:24:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d95aee54-a00a-3c30-8622-87fafaa25e98 | -16.889 | -55.772499 | 2024-10-09 01:24:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4c87210d-4813-3b8c-8d2d-c6876c17bb3d | -16.8911 | -55.7813 | 2024-10-09 01:24:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0dca9d29-595e-30ea-8564-3149e6a94b40 | -16.893101 | -55.790001 | 2024-10-09 01:24:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f7471e46-2fe9-3ef4-ae34-175aa0d2bc4c | -16.895201 | -55.798698 | 2024-10-09 01:24:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e2e25c36-5fc3-322e-990e-659d8e36bfbe | -16.9799 | -56.1567 | 2024-10-09 01:24:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6823ab65-f63b-3141-9342-6847ce79c859 | -16.9818 | -56.1651 | 2024-10-09 01:24:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bbb769fb-0cde-3314-b111-f7347c045956 | -17.136801 | -56.828899 | 2024-10-09 01:24:51 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dfd7757d-54a9-3a12-902d-73da061c6551 | -17.138599 | -56.8368 | 2024-10-09 01:24:51 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bdb4a7c7-56db-3aa0-8cfd-2a3f5a132dbf | -17.140499 | -56.8447 | 2024-10-09 01:24:51 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 26a609b9-960b-3095-8a7e-978142416154 | -16.879299 | -55.775002 | 2024-10-09 01:24:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 26907cbf-bd18-31ba-b8ec-a15555b6ce6f | -16.8813 | -55.783798 | 2024-10-09 01:24:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| beb6619e-50c3-3a3d-87fb-4393157a64e8 | -16.8834 | -55.7925 | 2024-10-09 01:24:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1143eb6a-e157-31ac-8142-673cffa2bc92 | -16.8855 | -55.801201 | 2024-10-09 01:24:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 731577c5-e27c-363f-822d-132cec00d170 | -16.887501 | -55.809898 | 2024-10-09 01:24:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3369def0-de2c-359d-a99c-2baac02b6566 | -16.899799 | -55.861801 | 2024-10-09 01:24:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a4326106-19d1-3f34-b3d7-57ac3c88f6c6 | -17.127001 | -56.831402 | 2024-10-09 01:24:51 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 174ba392-431b-3cf3-ab03-d3b7155d926f | -17.128799 | -56.839199 | 2024-10-09 01:24:51 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dedf6210-63fa-369e-ad38-6cfc61485f87 | -17.130699 | -56.847099 | 2024-10-09 01:24:51 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5c93e5d7-d6f5-3573-980b-180dedfa2b34 | -17.117201 | -56.833801 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 22a61062-5fc2-37dc-894f-8ce7e310055a | -17.118999 | -56.841599 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 95ed6251-db80-3c83-858b-087b47785787 | -17.1075 | -56.8363 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 98c058f8-42a6-3891-bd83-05069ddebadf | -17.109301 | -56.844101 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 51a1cdea-2068-32b0-a328-35437f24247e | -17.1112 | -56.852001 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 00b6b9d2-9ec4-3df2-80da-eeaae17b2d88 | -17.2176 | -57.314499 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b86f873f-f3df-3542-8620-5e1409bf98fe | -17.2194 | -57.322102 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0b14ac02-e888-3c10-969e-6f0688ab98c2 | -16.874701 | -55.886501 | 2024-10-09 01:24:52 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ba942b2a-f1e8-31ce-ae55-4db7f66e23cf | -17.0959 | -56.830799 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 786f9605-5f1f-37b3-bb02-c5aa0f9c22cb | -17.0977 | -56.838699 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 58a92a4a-6a23-3a16-bf27-91488395c265 | -17.099501 | -56.8465 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 220fd234-4cc6-3ab6-9357-682d052cb959 | -17.1014 | -56.854401 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0b4457bc-20a6-37bd-8d1f-53121f94eea7 | -17.2061 | -57.309299 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e5c55cd5-2733-3528-8c48-60ca3796a516 | -17.2078 | -57.316898 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2217e65b-ee70-3384-bde6-8e57b1ed7c7d | -17.2096 | -57.324501 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ff9b7cf2-6ec8-3d36-8537-9fa8ea4a84ab | -17.2113 | -57.3321 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e0290e1f-b794-396f-83ad-03e81f819f45 | -16.8547 | -55.845798 | 2024-10-09 01:24:52 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 72d54b2e-fe33-368f-9117-1a029df040bf | -16.856701 | -55.8545 | 2024-10-09 01:24:52 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bdc1d12c-bc27-399b-8cd9-f3b5fbce91fb | -16.858801 | -55.863098 | 2024-10-09 01:24:52 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d4bbb4f1-7939-30a3-9a2f-69afca7831e3 | -16.8608 | -55.871799 | 2024-10-09 01:24:52 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a06fdbbb-b34d-3a01-ae55-bb86b569c35d | -17.0861 | -56.833302 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 706ddc69-923d-3419-b168-eb4d11cda995 | -17.0879 | -56.841099 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 82f1d1c7-1fb0-3196-8100-7413cb3fb3ce | -17.089701 | -56.848999 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3e8e0617-b574-32b7-95ae-868be13e0718 | -17.0916 | -56.8568 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 48088a20-8a40-31d2-9163-237ebb0142e5 | -17.196301 | -57.311699 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 557ad171-52a2-379d-a5c8-76d55dc54d91 | -17.198 | -57.319302 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3cbcdadf-2235-3388-a55a-fae87e0dbec3 | -17.076401 | -56.835701 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 85c48515-55f0-3662-8313-383bc8ee59cb | -17.078199 | -56.843601 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fe5b5564-1b19-322c-9bc8-4b90702089ba | -17.08 | -56.851398 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a96740a2-654e-3572-966a-6976827347ed | -17.0819 | -56.859299 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 48f84e11-3e1e-39e1-9fe5-1db7a2b6d08a | -17.1831 | -57.299 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7404be35-22b1-3868-83e9-b66dc017a9d6 | -17.1849 | -57.306599 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 72417cd3-5b2a-3a99-9c99-30a7cac2fd4c | -17.1866 | -57.314201 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cbc720e1-e4d8-3a37-a8cb-515e021c9af4 | -17.191799 | -57.337002 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f1b057ce-b919-3276-95f1-bc4b321925e5 | -17.063 | -56.822399 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 47119828-f43a-3715-b853-0e3ed2becca6 | -17.0648 | -56.830299 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1ecf74a4-d65c-328f-b8cb-9ba4a2c58d76 | -17.066601 | -56.8382 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 93264f4f-1841-390c-ae23-6dfe6941aac6 | -17.068399 | -56.846001 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6329b3b8-6767-33c2-a9d4-45e6ba34c617 | -17.1733 | -57.301399 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a978daeb-3912-34e9-a2ff-cae16dba0314 | -17.1751 | -57.308998 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5ac908c9-8c5b-337a-bef4-1695c18e77e6 | -17.1768 | -57.316601 | 2024-10-09 01:24:52 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 74d2870c-42e7-3504-aab0-515096758fd3 | -17.0532 | -56.824799 | 2024-10-09 01:24:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e491a68a-7e6d-35bb-b829-0c7a1cfb79ef | -17.055 | -56.832699 | 2024-10-09 01:24:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8814c113-e098-3782-8e6d-d7c6f7f7264b | -17.056801 | -56.840599 | 2024-10-09 01:24:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 420b62b2-8386-30f4-93ed-b4f34388094f | -17.1635 | -57.303799 | 2024-10-09 01:24:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c20a3fc7-1276-37c3-aee9-089a7b9ff8f4 | -17.152 | -57.298599 | 2024-10-09 01:24:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 84e5b5f7-a4af-3d2f-90b4-0d4fedc7e98a | -17.1537 | -57.306198 | 2024-10-09 01:24:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a6c1fa2e-bda7-3d2f-aee3-8275425848df | -17.1555 | -57.313801 | 2024-10-09 01:24:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d02d5ecd-17f8-3ea1-a900-6fd87c4874ab | -17.1572 | -57.3214 | 2024-10-09 01:24:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 76972654-027d-31b9-b39d-fa371f47985a | -17.1458 | -57.3162 | 2024-10-09 01:24:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 34fe2f1c-9d45-3a6d-b0f0-7fc30d91813d | -17.164801 | -57.399502 | 2024-10-09 01:24:53 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5550235f-6722-3321-99c4-d32e41424a45 | -17.1665 | -57.407001 | 2024-10-09 01:24:53 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d2081416-449c-3be3-891b-fe60bb094c28 | -17.134199 | -57.311001 | 2024-10-09 01:24:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3308d8eb-e198-39e0-a213-a405838ee9e1 | -17.136 | -57.3186 | 2024-10-09 01:24:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2f2c08d1-6246-32aa-a971-a23839d2ccbc | -17.141199 | -57.3414 | 2024-10-09 01:24:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ae4cccda-1415-3dcd-ac65-1226383b8be3 | -17.1429 | -57.348999 | 2024-10-09 01:24:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9feeb74a-a8df-3270-b290-1a5978f9fe06 | -17.155001 | -57.401901 | 2024-10-09 01:24:53 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4e924265-bbe2-3a51-8945-585db163d151 | -17.1567 | -57.409401 | 2024-10-09 01:24:53 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 45cd4ea1-807b-3459-9eef-104ee9eb866c | -17.1584 | -57.417 | 2024-10-09 01:24:53 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d516fda7-7456-32fb-9afb-1f530a4b6688 | -17.1602 | -57.4245 | 2024-10-09 01:24:53 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 247df0c1-4d5e-3153-ade7-feefd37bf650 | -16.9625 | -56.612099 | 2024-10-09 01:24:53 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6b670481-9c8c-3d16-a7a0-2ac2da7a6e5e | -16.9643 | -56.620201 | 2024-10-09 01:24:53 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 45af2ff6-bf44-3d25-b8d8-1928a1770422 | -17.0142 | -56.834599 | 2024-10-09 01:24:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 07b5e58b-f343-3ab5-a887-a3a761c94deb | -17.127899 | -57.328701 | 2024-10-09 01:24:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4d7be0bd-d745-32f4-90a8-909536c39f55 | -17.129601 | -57.3363 | 2024-10-09 01:24:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c968bc2c-2046-3676-86d6-09708c9eabf0 | -17.131399 | -57.343899 | 2024-10-09 01:24:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 45df1456-9bcd-3c8b-a55c-c7b64fa63ce8 | -17.133101 | -57.351398 | 2024-10-09 01:24:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 110861c3-e8f0-3063-8354-fc068306a461 | -17.134899 | -57.359001 | 2024-10-09 01:24:53 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e0e651bf-e487-393e-9496-005ea51dfd12 | -17.145201 | -57.404301 | 2024-10-09 01:24:53 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README37.md)
