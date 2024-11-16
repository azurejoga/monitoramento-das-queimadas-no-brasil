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
| 66619bb7-e074-3f89-9716-1b8cd1af6a05 | -2.6282 | -51.9175 | 2024-11-16 00:47:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5c5dc88-1304-3c7d-933b-81107d0e0c4e | -3.5411 | -51.490002 | 2024-11-16 00:47:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8c0b950-024b-3244-80d0-f04e2f1413cb | -5.9022 | -46.235401 | 2024-11-16 00:47:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af29d921-587b-3647-99ef-3ed315ce6b1c | -3.7231 | -45.6549 | 2024-11-16 00:47:00 | METOP-C | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1d9051db-7a59-319c-b6c5-89fb1d2bbba8 | -3.7458 | -54.709801 | 2024-11-16 00:47:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aefdca94-e886-3e31-82f8-f8ca79fbaab9 | -1.8588 | -54.282299 | 2024-11-16 00:47:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43c4076c-da58-3e4d-bff0-65d3be62ab8f | -3.1909 | -45.102299 | 2024-11-16 00:47:00 | METOP-C | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e09e616f-cb26-3545-a766-0b28a259a564 | -3.6255 | -53.9912 | 2024-11-16 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 5eb1a800-37f2-3566-bb4b-ce300389511a | -2.9674 | -47.9931 | 2024-11-16 00:50:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| e3f9b013-b425-3ddf-b1a9-d0d27457f9b7 | -2.7615 | -48.5812 | 2024-11-16 00:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| cf035308-200d-343a-8c86-7676da3ba391 | -3.7685 | -50.7908 | 2024-11-16 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| b7089df8-35f6-324d-a57d-be8ac02c869e | -3.1272 | -54.5464 | 2024-11-16 00:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 6d246f13-a318-307f-840e-b1e64e52a7a1 | -3.1456 | -54.5459 | 2024-11-16 00:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 5b1cec3a-d886-3f4e-968f-b3d2691694ed | -2.1378 | -53.7244 | 2024-11-16 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 3f1d6c82-77c8-3ce2-a65a-72ccb8982cce | -3.5083 | -47.212 | 2024-11-16 00:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 6e6a9f83-c7a9-3af0-91fc-2a04d8c83cda | -2.651 | -48.477 | 2024-11-16 00:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 8a9a2af4-46c2-3364-9ac8-bf73c5cc5f8a | -2.78 | -48.5806 | 2024-11-16 00:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 161.4 |
| 9422106e-9d36-3f05-b203-ded3e8c5677c | -3.5851 | -50.5255 | 2024-11-16 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 68930867-112c-3687-ac77-b6bc7dca2f1b | -2.1576 | -46.5527 | 2024-11-16 00:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 6a918a96-126e-331e-944d-f503a6815aa7 | -2.7985 | -48.5801 | 2024-11-16 00:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| cd2abfe9-2c6d-3cc4-a19b-0469cfbd083e | -2.9859 | -47.9925 | 2024-11-16 00:50:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 991473ca-feb5-3479-953b-66d1d9ddce9b | -3.1273 | -54.5264 | 2024-11-16 00:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| ec8cd17e-7c45-3774-b974-28f22131eb0a | -3.0356 | -45.1193 | 2024-11-16 00:50:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 57.9 |
| aeb94117-be54-3e3e-b36a-29c5cb28fae4 | -3.3211 | -43.8306 | 2024-11-16 00:50:00 | GOES-16 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 89c8ad08-685e-3fbd-a090-1346f3ecb4aa | -2.1562 | -53.7039 | 2024-11-16 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 248.4 |
| 39ee7226-22cf-38da-a98a-986cffa82023 | -17.5882 | -57.4711 | 2024-11-16 00:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.6 |
| 66d83684-17bd-322a-b41a-3d4447b39c8e | -2.6325 | -48.4775 | 2024-11-16 00:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| faa8e63f-b731-3e31-882c-79f562716451 | -2.1379 | -53.7043 | 2024-11-16 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 145.1 |
| 50d1f7da-e18e-3593-a776-d523e5b35015 | -3.1501 | -53.2371 | 2024-11-16 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| c75562bb-0ff4-3362-a228-3103a5ddf6b9 | -2.1562 | -53.7241 | 2024-11-16 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 183.8 |
| 3d06d738-86aa-3b03-a32d-60f06de30ce8 | -3.5439 | -51.4844 | 2024-11-16 00:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| ef8a66df-cb7b-3381-ae30-d6bb4ba58b21 | -2.7986 | -48.5586 | 2024-11-16 00:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 946dbf2b-c96e-3c4a-836f-2fbbb20d8992 | -2.5767 | -54.4188 | 2024-11-16 00:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| ca0a43a4-979f-3a4c-a023-55c1a37b84da | -3.0357 | -45.0967 | 2024-11-16 00:50:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 97f2c951-dcee-3d4f-84c0-e536d46bde27 | -3.3688 | -45.4215 | 2024-11-16 00:50:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 15a62577-6c0d-36d2-9d84-d8b0de8137e0 | -3.1456 | -54.5259 | 2024-11-16 00:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| fc177815-a180-381f-b2fa-4d9501d91059 | -2.1563 | -53.6838 | 2024-11-16 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| ca4e6731-9246-3fac-ac69-092f2ee22016 | -17.5885 | -57.4506 | 2024-11-16 00:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.6 |
| d2295767-efe6-3b69-b2a7-178843efc093 | -2.7801 | -48.5592 | 2024-11-16 00:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 2174f257-1254-3d5e-ad57-76b9ce1fb0fb | -3.3024 | -43.8314 | 2024-11-16 00:50:00 | GOES-16 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 1eaad696-de56-3022-a165-3f6b2dbb1f2a | -2.78 | -48.5806 | 2024-11-16 01:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 141.4 |
| cc938247-ae68-3773-8a0e-805863b5b5d4 | -2.1576 | -46.5527 | 2024-11-16 01:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 16799a73-fee4-322d-8518-ea631183e61e | -2.651 | -48.477 | 2024-11-16 01:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| e2e61f66-4a74-3a8e-bc7b-713ba212b5cd | -2.6131 | -54.5381 | 2024-11-16 01:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| ba24aec8-e8cf-343c-8559-fb7392292146 | -2.1391 | -46.5531 | 2024-11-16 01:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 6cc7bc29-3359-3c21-8da1-bf7fd4a3ac0d | -3.7208 | -45.6531 | 2024-11-16 01:00:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 94066981-3a4f-390c-8b08-a34f2c8a1788 | -16.958 | -57.6269 | 2024-11-16 01:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.3 |
| d189051d-a3c9-3161-89a2-5eb0296689c0 | -3.1456 | -54.5259 | 2024-11-16 01:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 49670e65-bdac-30e9-95c0-d0cff9a85c33 | -2.6509 | -48.4985 | 2024-11-16 01:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 86ee0b6d-b8f7-31ae-a38e-3e7d45208f64 | -2.1575 | -46.5747 | 2024-11-16 01:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| f9581068-7298-31b5-a585-279a1e654991 | -3.5851 | -50.5255 | 2024-11-16 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| f6c4e29a-1556-3d31-9b73-9fb6e20af74e | -2.9674 | -47.9931 | 2024-11-16 01:00:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 5aaffc3b-f6db-3da3-9f6c-7c25ce828c22 | -3.1501 | -53.2371 | 2024-11-16 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| dad28078-f556-3d06-afa4-26dcc80875d9 | -3.7685 | -50.7908 | 2024-11-16 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 4a591d4d-610b-3eb6-8f1f-76b30b3b7f49 | -3.6255 | -53.9912 | 2024-11-16 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 84d24c23-379c-3954-9afe-4416629681b5 | -3.1273 | -54.5264 | 2024-11-16 01:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| fd05c683-340d-35ad-a446-c64a67b7609e | -2.1562 | -53.7241 | 2024-11-16 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 1f2556f7-c745-3024-bc80-0d952c46a033 | -3.0357 | -45.0967 | 2024-11-16 01:00:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 156.7 |
| 5180d732-7e28-3e09-8bc4-30dbf781d5d7 | -17.5688 | -57.4529 | 2024-11-16 01:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.7 |
| 56769151-2c28-3879-9214-5d55c2bc563e | -17.5685 | -57.4735 | 2024-11-16 01:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.3 |
| 02709a5a-b32b-38a8-b64b-3d61a4917d7b | -3.1272 | -54.5464 | 2024-11-16 01:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| d503ead2-1819-3998-84a6-e3b18789ca21 | -2.1562 | -53.7039 | 2024-11-16 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 192.5 |
| 7031a878-076b-3afb-a3c7-8d6c8fdb2acf | -2.5767 | -54.4188 | 2024-11-16 01:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 5dc5b054-6c06-3495-b9f8-20ab5a646e3b | -2.1746 | -53.7036 | 2024-11-16 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 79443b5a-75c2-3520-b566-b43448f67caf | -17.5882 | -57.4711 | 2024-11-16 01:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.0 |
| 18bedf55-9ae1-3e5a-8f51-559fe7ff02a4 | -3.0356 | -45.1193 | 2024-11-16 01:00:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 62.5 |
| c6672335-51b2-3e4a-b279-e4fcbd690311 | -16.9384 | -57.6291 | 2024-11-16 01:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.3 |
| 1074010f-b4ce-3d22-84bc-1167449cafff | -2.1379 | -53.7043 | 2024-11-16 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 167.1 |
| 32969765-9d71-3d93-b834-dc214ceeddb9 | -2.7801 | -48.5592 | 2024-11-16 01:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 55de355d-2c29-3133-96fc-383b990e7e78 | -3.7394 | -45.6523 | 2024-11-16 01:00:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 61375e3e-1d6e-3f0f-800a-8af0f9c09251 | -2.1378 | -53.7244 | 2024-11-16 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 2d10ad89-b2df-3179-b53b-0f503d3604c9 | -16.958 | -57.6269 | 2024-11-16 01:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 114.6 |
| a2dccf27-765a-390c-9380-cd8b7943e366 | -2.1378 | -53.7244 | 2024-11-16 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 4ea9bf55-5f58-31ec-859c-4be3fb6d9c34 | -3.7208 | -45.6531 | 2024-11-16 01:10:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 56.5 |
| b59e2c32-41fa-3090-abb3-5e8018dc8afc | -2.7986 | -48.5586 | 2024-11-16 01:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 09d0576d-27ce-3652-8356-4f64d949a6eb | -3.1456 | -54.5259 | 2024-11-16 01:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 5281e10c-1de5-3108-825e-ef5d2e04aabf | -2.1576 | -46.5527 | 2024-11-16 01:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 167.5 |
| 646e7caa-69d0-3176-ba36-5000fdada0c4 | -6.3007 | -39.4763 | 2024-11-16 01:10:00 | GOES-16 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 81.1 |
| dce403e2-a9eb-386b-b580-645c317ac367 | -16.9577 | -57.6473 | 2024-11-16 01:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 126.1 |
| 238e5c00-3490-3a22-b04e-be95e8b128f0 | -2.7801 | -48.5592 | 2024-11-16 01:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 3e0ce14d-277d-346d-a462-1acc6e62cfdd | -2.1391 | -46.5531 | 2024-11-16 01:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 47aa4d23-1334-3fc6-8fed-87878553b516 | -2.1379 | -53.7043 | 2024-11-16 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 126.6 |
| 22e0809b-acf8-363d-9c40-a72b7d72df37 | -3.1501 | -53.2371 | 2024-11-16 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 3b64a2f8-1ce4-30ae-ac0e-310f9cf578e2 | -3.7394 | -45.6523 | 2024-11-16 01:10:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 13260c9e-3db0-3685-bd3d-0df89ac53035 | -2.5642 | -46.8938 | 2024-11-16 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 1c6920b9-a901-3a9d-bc81-d188dd1090f2 | -2.1746 | -53.7036 | 2024-11-16 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 67c109f0-30be-39c5-8d40-8407278c82f5 | -17.3126 | -57.5039 | 2024-11-16 01:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.4 |
| 7f28c556-5ec8-389f-96a6-8761a073544a | -2.78 | -48.5806 | 2024-11-16 01:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 648b75b5-040c-32d2-91c4-004f450769f0 | -17.5882 | -57.4711 | 2024-11-16 01:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.2 |
| 0435de98-549b-3b48-8281-6310348ab076 | -3.7685 | -50.7908 | 2024-11-16 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| ebcebbf8-b9f3-306a-8d9a-78b339f17d3a | -2.1575 | -46.5747 | 2024-11-16 01:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| aaaa113b-e6be-3367-aec0-772113b5fcf0 | -3.1273 | -54.5264 | 2024-11-16 01:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| e30c63c7-b9c7-30bc-965c-d8068fd91f4d | -2.1562 | -53.7241 | 2024-11-16 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 9c864928-5d40-367e-9ae9-d7693a34eae8 | -16.9384 | -57.6291 | 2024-11-16 01:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.4 |
| a4f68edc-a4e3-3d56-b1fa-abda755c83cc | -2.7985 | -48.5801 | 2024-11-16 01:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 5c53059b-695c-3318-8d59-f6a62f36b858 | -2.5766 | -54.4388 | 2024-11-16 01:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 5ba72c24-eaed-3a65-9d12-e594d0fa6c4a | -2.5767 | -54.4188 | 2024-11-16 01:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| d3500733-e6d8-32a6-af43-046a576861c0 | -3.5851 | -50.5255 | 2024-11-16 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| abc05a91-e564-3d94-b023-db22da148254 | -3.0357 | -45.0967 | 2024-11-16 01:10:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 100.0 |
| e501b402-f1b6-38a4-8782-cb37bc6cd3cc | -2.9674 | -47.9931 | 2024-11-16 01:10:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |


[Clique aqui para ver as próximas entradas](README10.md)
