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
| 6c86b2d6-8de4-33e5-977f-41ca91d1da92 | -3.9324 | -47.6962 | 2025-11-06 01:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 0bbd7afe-ee5e-3e4f-ad88-cd94b00af4f6 | -4.6119 | -43.346 | 2025-11-06 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 3ea5100a-452f-31d2-a93b-970ecd0c3cd0 | -4.0477 | -46.9915 | 2025-11-06 01:50:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 110.0 |
| d48e3b48-2ce3-3a14-8684-a9172738c569 | -5.1533 | -41.2468 | 2025-11-06 01:50:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 75.3 |
| cd0931e1-64e4-3563-a777-c690cb1cad54 | 0.4466 | -60.4873 | 2025-11-06 01:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 77d5e882-80ea-34bc-9004-7860235afcd1 | -4.0976 | -48.0144 | 2025-11-06 01:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| c851b493-fa79-3f40-86d0-06d038267e4d | -7.2891 | -45.4589 | 2025-11-06 01:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 37941128-9ea7-3538-88f9-fab16d5721ca | -3.4898 | -43.6614 | 2025-11-06 01:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 8ca4b60b-9a35-3626-8a1a-faec58c12889 | -4.4633 | -43.2152 | 2025-11-06 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 3afbd740-1cc9-3882-abc9-477dbc876e00 | -4.5747 | -43.325 | 2025-11-06 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| a4d4c964-68ac-30e6-ab89-a2365eb493bb | -4.5932 | -43.3471 | 2025-11-06 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 9f55345d-74dd-3ab2-92fa-115dd8968ebb | -4.9855 | -48.4677 | 2025-11-06 01:50:00 | GOES-19 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| a0f98ba0-63e1-35ca-a7da-1c87f77cc604 | -3.4899 | -43.6383 | 2025-11-06 01:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| ced180d9-6476-34ec-92e6-27635ef39a50 | -4.5934 | -43.3239 | 2025-11-06 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 185.0 |
| 02382b33-990c-362a-aab1-a437302a37ed | 0.4283 | -60.4874 | 2025-11-06 01:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 64.3 |
| f17b4548-2f2f-3858-b948-35b59be11231 | -3.4712 | -43.6392 | 2025-11-06 01:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 119.7 |
| c8d60309-24a9-3106-bc6a-c032ffaf1056 | -3.4711 | -43.6623 | 2025-11-06 01:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 0d7f5c13-ef7a-30e6-9dc2-608892625b49 | -4.6121 | -43.3227 | 2025-11-06 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| cf9b69dd-7f8e-34d5-9d72-3ed5ffc8e676 | -9.52655 | -66.72961 | 2025-11-06 01:51:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| de05d102-90c8-370e-bcf7-2eae6c4df6db | -9.59423 | -64.15417 | 2025-11-06 01:51:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7d1bc1f9-56ba-38b1-9adf-5d4c6523e3d1 | -9.59609 | -64.15953 | 2025-11-06 01:51:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 39d725eb-cdce-3d89-af77-4744a0547bb8 | -4.0477 | -46.9915 | 2025-11-06 02:00:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 090ef4c1-511a-31d0-9b67-b669cacc5185 | -4.4633 | -43.2152 | 2025-11-06 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 79489950-aeb6-3987-8845-27465a8c0682 | -4.4632 | -43.2386 | 2025-11-06 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 1434c000-aef6-3c83-98de-85b2d57750d7 | -4.5934 | -43.3239 | 2025-11-06 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| adc4901d-a859-3fe8-8f69-a23003410988 | -4.1161 | -48.0136 | 2025-11-06 02:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 23816303-ef72-35d6-88ca-01d726a214d1 | -4.5747 | -43.325 | 2025-11-06 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| e4b55290-4d71-384b-9512-b68e2dc737c1 | -4.0292 | -46.9923 | 2025-11-06 02:00:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 0c2eea71-fd28-32a4-95b0-092320d181ab | -4.5932 | -43.3471 | 2025-11-06 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 07100827-d37e-3ea8-88f5-d57f63c13aa8 | -4.6121 | -43.3227 | 2025-11-06 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 5ec1ccb6-1b3c-3e46-9fc8-7f4551608891 | -5.1533 | -41.2468 | 2025-11-06 02:00:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 77.5 |
| dceebc68-1cc7-33d7-8969-fa179df19bc0 | -3.4711 | -43.6623 | 2025-11-06 02:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 9a2f7a00-0470-3ffc-9ab0-98530e0d6526 | 0.4466 | -60.4873 | 2025-11-06 02:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 68db6d97-238e-3985-b2b2-a55555bbd7ea | -3.4712 | -43.6392 | 2025-11-06 02:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 76de40d1-5fc4-32ff-85c7-fec91b0a27f8 | -2.986 | -52.8146 | 2025-11-06 02:00:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 4ca4f7b6-b1a6-3277-bce6-3dca073b7c9b | 0.4283 | -60.4874 | 2025-11-06 02:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 71.5 |
| e689b7b0-e7a1-3e79-84b7-6f36cfdb872a | -4.9855 | -48.4677 | 2025-11-06 02:10:00 | GOES-19 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| a35b3a65-7a56-3787-b3d6-2ead2d395ebf | 0.4283 | -60.4874 | 2025-11-06 02:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 66.2 |
| d5737cf7-e1a9-32f4-98e6-1707fc257267 | -4.116 | -48.0352 | 2025-11-06 02:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| ae3b2754-3091-380d-82f3-c965586123c7 | -4.4632 | -43.2386 | 2025-11-06 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 4df45bf9-c576-34cc-999c-87f0db3d291e | -4.4633 | -43.2152 | 2025-11-06 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| cd0fb9ff-5f89-34fa-b064-56018d5abb35 | -3.4711 | -43.6623 | 2025-11-06 02:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| d810eb05-7b09-3786-96cc-f6e4e7c7c7ba | -4.1161 | -48.0136 | 2025-11-06 02:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 10baa656-22c6-35ec-97fd-494b85bbcf6b | -4.0477 | -46.9915 | 2025-11-06 02:10:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 7357b0f1-0695-37d7-a28f-8e5e4d1f2cf3 | -3.9324 | -47.6962 | 2025-11-06 02:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 26885f3c-4b8e-324d-9660-c64c547bc2a5 | 0.4466 | -60.4873 | 2025-11-06 02:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 9296a492-7ad1-3f00-8812-96adb6b8cf10 | -3.4712 | -43.6392 | 2025-11-06 02:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 28e59fdb-5bbd-380c-9a65-a6d792ce9985 | -5.1533 | -41.2468 | 2025-11-06 02:20:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 73.3 |
| 0676afea-3bb6-3937-be4e-ee1ca1e81d6f | -4.1161 | -48.0136 | 2025-11-06 02:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| db37e246-547f-3bff-b193-bc2f97d139e1 | -4.0976 | -48.0144 | 2025-11-06 02:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 4b7f090d-3562-330d-965b-1500eddddfa4 | -3.9324 | -47.6962 | 2025-11-06 02:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 989cd750-e345-3bd2-871d-74c28aa31a57 | -2.986 | -52.8146 | 2025-11-06 02:20:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 96b28155-1e7b-3510-b1ac-0f9b4ceba70b | -3.4711 | -43.6623 | 2025-11-06 02:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 46.2 |
| a0eb7ba8-a116-39ff-b600-1454787f1115 | -4.9855 | -48.4677 | 2025-11-06 02:20:00 | GOES-19 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 1c724cc9-40a5-39f6-8b87-c45bfabed2ea | -3.4712 | -43.6392 | 2025-11-06 02:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 43cff7e6-7ee2-3511-95b7-679b821e5d2b | 0.4466 | -60.4873 | 2025-11-06 02:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 35dbe575-7977-3e78-8430-716fa6a22a34 | -4.9855 | -48.4677 | 2025-11-06 02:30:00 | GOES-19 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 1b9855a5-6b2d-338d-854a-f5b155e1f651 | 0.4466 | -60.4873 | 2025-11-06 02:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 1c1d2e2a-1a3d-3cdf-b390-2424ebe63b41 | -4.1161 | -48.0136 | 2025-11-06 02:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 57ca55a7-50a2-3ca1-a2d1-aea7f4e396ba | -5.1533 | -41.2468 | 2025-11-06 02:30:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 67.3 |
| 5c004326-2bfc-3779-8df9-5617e96f93f4 | -4.0477 | -46.9915 | 2025-11-06 02:30:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 2bdde4cf-4971-364a-bc4d-035a8d6345f7 | -3.9324 | -47.6962 | 2025-11-06 02:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 37a6d96c-9537-332a-8928-5dc2e3fedc04 | -4.0976 | -48.0144 | 2025-11-06 02:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 3a9eb946-e7ca-380d-9d7c-672d8deadefd | -4.0477 | -46.9915 | 2025-11-06 02:40:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 86a6bb3d-cb88-3f9a-99a0-61714700182f | -3.9324 | -47.6962 | 2025-11-06 02:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 20e60cfb-a38a-3949-81ae-8a91e1bcf7ae | 0.4466 | -60.4873 | 2025-11-06 02:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 79.2 |
| f66a51a3-53a0-3836-a547-ecfc6dbd6db7 | -4.5932 | -43.3471 | 2025-11-06 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 109.3 |
| c62d8a4d-f8f7-3344-a7ee-93f6a87f25cd | -4.5934 | -43.3239 | 2025-11-06 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| db82cde1-e2f8-3e22-a45d-c0f3256e9a0b | -4.0477 | -46.9915 | 2025-11-06 02:50:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 5fd7c4e0-844c-3f27-acbc-c81b4e15c8fd | 0.4466 | -60.4873 | 2025-11-06 02:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 76.0 |
| e7d50731-f1ec-3528-8aed-fa9e2ef0a827 | -4.5745 | -43.3483 | 2025-11-06 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| dbd0174c-0163-3493-8129-497cf85dadd2 | -4.0976 | -48.0144 | 2025-11-06 02:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| ff35818e-031f-35d2-ae8c-ef2fb386f288 | -3.9324 | -47.6962 | 2025-11-06 02:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 31a318b5-0be2-3736-a1e6-cda6cf02a28f | -4.0477 | -46.9915 | 2025-11-06 03:00:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 23da2768-3864-3fda-935a-350cbae76e25 | -4.6121 | -43.3227 | 2025-11-06 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| d9d51900-700d-394f-b520-d0ef7627384b | -4.6119 | -43.346 | 2025-11-06 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| b8dac477-3b8e-3a4b-bc91-53d2e68c6df0 | -4.5747 | -43.325 | 2025-11-06 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| dfb98801-2072-3e9b-82a6-a6d7128a63eb | 0.4466 | -60.4873 | 2025-11-06 03:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 53a13fa5-f8c7-3880-95d8-8fb1fe0a0fe5 | -4.5745 | -43.3483 | 2025-11-06 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 3badb302-4e01-3daa-aeff-a59bea40973f | -4.5932 | -43.3471 | 2025-11-06 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 140.6 |
| e048c293-3223-3e2e-bdfe-d0d77818df2f | -3.9324 | -47.6962 | 2025-11-06 03:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 0d7f2827-2471-3ab3-a70e-3b0076101a21 | -4.7014 | -46.5173 | 2025-11-06 03:00:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 297ba84e-14eb-3132-94d0-8b71aad04b23 | -4.5934 | -43.3239 | 2025-11-06 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 447fffd5-7a96-35a2-aae7-a53480528b37 | -8.89265 | -37.10765 | 2025-11-06 03:04:00 | NOAA-21 | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 60104ca9-1bae-33aa-8f6b-14bb30705879 | -8.89182 | -37.11207 | 2025-11-06 03:04:00 | NOAA-21 | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1c55b480-1000-3ce6-87a8-af7cffefd99a | -6.22907 | -37.41983 | 2025-11-06 03:04:00 | NOAA-21 | SÃO JOSÉ DO BREJO DO CRUZ | PARAÍBA | Brasil | 2514651 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 18be596d-ca57-3797-ab09-3f7f9aba8163 | -9.1242 | -37.78999 | 2025-11-06 03:04:00 | NOAA-21 | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 67f6d9f5-2172-37f9-a197-c30cc17052bb | -4.56803 | -37.95988 | 2025-11-06 03:04:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b57e763a-1929-3399-b23d-9c096614b714 | -6.22812 | -37.42503 | 2025-11-06 03:04:00 | NOAA-21 | SÃO JOSÉ DO BREJO DO CRUZ | PARAÍBA | Brasil | 2514651 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6e918f9c-b6a6-3666-8196-98940155baac | -4.5747 | -43.325 | 2025-11-06 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| cd9da4fd-2261-3c23-89ba-fe9ce982790d | -4.6121 | -43.3227 | 2025-11-06 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| accd4d1d-aee3-3c64-89ee-c2214552e8fd | -4.6119 | -43.346 | 2025-11-06 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 2058c4f4-4d48-364e-be9b-526e6efc94f4 | -3.9324 | -47.6962 | 2025-11-06 03:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 07cb8ae8-f370-3e0d-9759-0fb3b71f7458 | -4.5932 | -43.3471 | 2025-11-06 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 09aa46dd-6bb4-3ee1-8401-ca3d331bb9f3 | -4.5745 | -43.3483 | 2025-11-06 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 0ec3a737-5b2e-3018-826c-11b53ffd0bd2 | -4.5934 | -43.3239 | 2025-11-06 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 7feb8a3c-ee1f-3cec-9b8c-723559c5dbd4 | 0.4466 | -60.4873 | 2025-11-06 03:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 67.9 |
| feb9ef4d-9ed2-3bfd-9820-99d88f8f8b23 | -4.5934 | -43.3239 | 2025-11-06 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 5f0b1826-ee4c-371d-93ca-53ac94ca283e | 0.4466 | -60.4873 | 2025-11-06 03:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 68.8 |
| eb6360ce-76b2-3bc8-8597-4fa076366656 | -3.9324 | -47.6962 | 2025-11-06 03:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |


[Clique aqui para ver as próximas entradas](README10.md)
