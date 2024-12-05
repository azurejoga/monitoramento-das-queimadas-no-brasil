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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ada83ef2-29f3-3e8f-8308-4cf1b1a1b124 | -6.9346 | -43.5168 | 2024-12-05 04:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 3f468243-81fa-39d0-a123-fb09995117e2 | 1.40753 | -56.08031 | 2024-12-05 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 119f46a6-06de-3b5a-bd71-12deb3a99091 | 1.09768 | -55.96619 | 2024-12-05 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 29e2be39-d565-364d-9cb9-78485e4ec36b | 1.08951 | -55.97187 | 2024-12-05 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2be4e028-189e-391c-b150-df6446123e99 | 1.08509 | -55.97255 | 2024-12-05 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6e06f97d-543d-36f9-9544-ead2e4e715e3 | 1.08574 | -55.97684 | 2024-12-05 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d7bb1aa-e1a6-3dd2-bfd1-5edf56e68de5 | 2.48136 | -60.69581 | 2024-12-05 04:44:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4b95e547-7f29-3c0c-8398-04fa758ce696 | 1.09392 | -55.97119 | 2024-12-05 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6b89fb4f-ab9d-37a3-8a6a-76413173d3b4 | 1.41134 | -56.07522 | 2024-12-05 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c61d10ac-f022-32bb-99d0-222016fa48b3 | 2.57539 | -60.69527 | 2024-12-05 04:44:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9c6008cf-ee6b-3319-be45-526335b7a9a8 | 1.1021 | -55.96553 | 2024-12-05 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d3e97b34-0730-3894-a50b-d41ceada9761 | 1.08724 | -56.01642 | 2024-12-05 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7e8f941-a6ae-3ea1-8aae-72b2d9b29553 | 2.5761 | -60.70006 | 2024-12-05 04:44:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0c090a17-2253-3f02-af8d-6a6f4dae72fb | -6.83825 | -35.21867 | 2024-12-05 04:46:00 | AQUA_M-M | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 6.7 |
| bc65e7af-b1e8-385a-8ac9-ae209277785b | -6.93439 | -43.53108 | 2024-12-05 04:46:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 26.2 |
| aa151dd0-c072-3f07-85cd-7b1f1144ece1 | -6.93111 | -43.53778 | 2024-12-05 04:46:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 18aa47a2-c597-34e2-af89-4fec7dc58942 | -6.82909 | -35.21738 | 2024-12-05 04:46:00 | AQUA_M-M | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 59f3c6a9-bd03-3c83-aa81-61022acde9bd | -7.42824 | -39.8896 | 2024-12-05 04:46:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a30e7160-2f86-38ad-90df-25735734a845 | -2.82594 | -53.05762 | 2024-12-05 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b0e610e5-2428-3847-8779-12a3c9d8d67a | -5.58435 | -45.21294 | 2024-12-05 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8b3a2a87-6413-319e-8eee-4d2bcd47e0dc | -3.1832 | -53.85801 | 2024-12-05 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d7fa9e1-0ca3-3dbc-816a-f10cff843d95 | -1.62075 | -53.8276 | 2024-12-05 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a843a284-731b-3137-bc5f-28e74c9a8559 | -3.63847 | -54.43988 | 2024-12-05 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7405f6d-22c5-3a6c-a390-bfda1b9fba79 | -1.70826 | -52.60097 | 2024-12-05 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0ca6cf7a-296a-3c84-ae7d-b586d9d2518f | -2.07854 | -45.60773 | 2024-12-05 04:46:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 452ad424-20ba-3b19-af9a-0832d8e8c376 | -3.63474 | -54.4393 | 2024-12-05 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fbee66c-255a-3047-8ce0-a238b5ccb49b | 0.8968 | -59.39 | 2024-12-05 04:46:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ad87670-8d87-3104-b295-63bde127216a | -1.64732 | -53.82733 | 2024-12-05 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 89a40c33-d04c-30bc-8e7d-9c3582195a52 | -1.68503 | -54.44977 | 2024-12-05 04:46:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b32ece47-e36a-31c3-8526-e3a33b51f67b | -2.17065 | -54.62383 | 2024-12-05 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 18f20e2d-4a08-3769-90dc-83d03ee30d61 | -1.72914 | -52.60419 | 2024-12-05 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9edcc6d0-0317-313e-adec-42025ef975da | -2.982 | -51.44039 | 2024-12-05 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab8ae29c-6e63-356c-8f3a-ab61cc8ea09a | -2.82656 | -53.05371 | 2024-12-05 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b1dbbaed-29f1-32bb-872a-f5a469e0a163 | -3.18994 | -54.50867 | 2024-12-05 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 42f08f60-cafd-318b-831f-78eb765ca5f2 | -1.68843 | -52.7962 | 2024-12-05 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a876e607-3773-3c1e-85c4-84f1e53d26e7 | -5.58377 | -45.21691 | 2024-12-05 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b8633874-453f-3950-8dde-086a1117fc19 | -2.56802 | -53.97536 | 2024-12-05 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b524dcdd-85dc-3271-95db-80fce0bacaa2 | -2.81066 | -53.06328 | 2024-12-05 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 03584515-1ea7-3522-99b2-0dba0cf44a91 | -1.50042 | -51.93365 | 2024-12-05 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 34b757b5-d90e-3d5a-a96b-54dbb9bf81fa | -5.57926 | -45.1589 | 2024-12-05 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f930aa1-75c7-3cce-9d0c-14dee47a7e29 | -3.04885 | -51.40425 | 2024-12-05 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9caffc33-cf6e-3406-808a-3abf03077270 | -3.17956 | -53.85746 | 2024-12-05 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e53a2725-d1ca-3f61-89a8-852821cdab8f | 1.03017 | -59.48428 | 2024-12-05 04:46:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f3a07fac-1055-371a-aa5d-2444d1e15a51 | -3.18979 | -54.50607 | 2024-12-05 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bee06659-3593-33ce-a87c-ba2b6d48784c | 0.16892 | -60.58996 | 2024-12-05 04:46:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a4cfa7d4-969d-3a47-b70e-61407ac360e9 | -2.82884 | -53.06208 | 2024-12-05 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| da3080e0-2e7e-3be5-951d-8b9866089c85 | -1.54804 | -45.52899 | 2024-12-05 04:46:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b9fc7ec0-3aa6-394a-9656-da7398f113ca | -1.69405 | -52.64603 | 2024-12-05 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42cb2b58-f6e2-3d5e-9f34-5518082c71bd | -6.94527 | -43.53118 | 2024-12-05 04:46:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b72b712-6c78-3e38-ba4f-dc99a55e455d | -1.70766 | -52.60481 | 2024-12-05 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4bd598ca-4810-39c1-8653-abd14e49e40f | -2.156 | -54.61665 | 2024-12-05 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a07ea84e-c643-3d33-a08a-e2fce0381758 | -2.45153 | -53.9772 | 2024-12-05 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8626f754-abc5-300e-96f3-b1366b3c341b | 0.75311 | -59.65981 | 2024-12-05 04:46:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4522bf84-5e6f-3313-9bf9-f5b30a31a69b | 0.70548 | -59.87879 | 2024-12-05 04:46:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7b35c35-f0b0-3271-b443-72422603cc75 | -1.63039 | -52.35917 | 2024-12-05 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b54f9dd-f9d3-3abd-860d-1bf137f7e05e | -3.18908 | -54.5106 | 2024-12-05 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b66f0bb7-4616-373b-ae20-ddbdc32fc84c | -7.42761 | -39.89457 | 2024-12-05 04:46:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a0c88087-2215-3829-a909-e74bbe3037a9 | -2.16755 | -54.61845 | 2024-12-05 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 111e5b61-4778-3357-a3a1-54e4ec930e00 | -1.0865 | -53.45965 | 2024-12-05 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 526d66bc-64c3-390c-a321-be71fbf12c31 | -1.68904 | -52.79229 | 2024-12-05 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2cc46959-94ee-36e5-9a60-ed16cdbcf638 | -5.57985 | -45.15487 | 2024-12-05 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58c4743d-7254-3a1e-9b7e-3bd9ea4fb418 | -4.66905 | -47.92037 | 2024-12-05 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d18273e6-1edf-30a8-b4c4-3d4fb8d51b01 | -1.62635 | -52.3624 | 2024-12-05 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8ad18dc-da4f-3788-8921-1dbcfc7f8a7e | -2.82946 | -53.05817 | 2024-12-05 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| db14eb1f-3144-3ac2-827e-a309499f1fce | -1.17038 | -53.42478 | 2024-12-05 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2601fbf-1cc1-3d6f-9947-2be6f583ea69 | -1.47064 | -52.68357 | 2024-12-05 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eca3c84b-ba20-339a-803f-d8f4d7d2ea36 | -1.22648 | -53.7638 | 2024-12-05 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88b5532f-962f-3a55-9848-5cd3a1a83548 | -2.83297 | -53.05871 | 2024-12-05 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e6e5e97d-46a2-37d7-a149-68a73a00cdcf | -1.03867 | -53.54988 | 2024-12-05 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a50b25d9-b968-3d79-a250-7ecc54e38039 | -2.81768 | -53.06436 | 2024-12-05 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a3e46292-1b98-3846-971a-1474c13ea9a2 | -3.44972 | -54.34348 | 2024-12-05 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab2d6a6a-0c39-32dc-b784-1f63f47b73fc | -1.49424 | -52.53317 | 2024-12-05 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 882db0a4-eed5-3def-8061-e82710b86b22 | -1.62305 | -53.83706 | 2024-12-05 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52931ad3-b5c8-3052-b7bf-17a0e32dbdcc | -2.97521 | -51.37496 | 2024-12-05 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4026644-51a3-3423-bea5-3e55061bdab4 | -2.98588 | -51.43742 | 2024-12-05 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b0b8c1f-b97c-3468-a9b3-194daff6f3f5 | -1.87671 | -53.30236 | 2024-12-05 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f3666f1-88b1-39a0-8f6f-1bb6913005c1 | -6.15613 | -46.68006 | 2024-12-05 04:46:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1e4d0c0e-d189-37c8-9b94-ac25a8ee7753 | -1.47414 | -52.68411 | 2024-12-05 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6790577d-825b-3a40-8057-cd3c396b37ec | -1.49077 | -52.53263 | 2024-12-05 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f886bab1-3a95-3d13-aff9-525dafd7575b | -2.37475 | -46.16479 | 2024-12-05 04:46:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| adec6fa8-64db-3d48-b5be-3574c638d615 | -1.87692 | -46.38012 | 2024-12-05 04:46:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c0f5f47f-8cd6-3513-af8f-c5f16028f9be | -1.87867 | -53.2901 | 2024-12-05 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2616e60-bfa9-3d14-855d-44eb780345e5 | -1.08352 | -53.4549 | 2024-12-05 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7f3e3ff-2495-3fe2-8079-1a583421f489 | -1.03066 | -53.55303 | 2024-12-05 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10f9556d-3bd1-3740-8501-6a29d4083195 | -1.15649 | -53.41825 | 2024-12-05 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82230cde-662b-3ed8-b542-73da381d3ec4 | -2.82471 | -53.06545 | 2024-12-05 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 281977a8-5b59-3bc7-af40-ec977eef1e82 | -3.18836 | -54.51518 | 2024-12-05 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 71ae610d-266e-3f00-83d2-e54a4d6f8201 | -6.94188 | -43.51954 | 2024-12-05 04:46:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4325d141-ceda-3be0-8387-b61d17fcdeec | -5.57866 | -45.16293 | 2024-12-05 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 01da42c1-7e18-30cf-b0c7-a19d927a6f5f | -2.00381 | -53.27921 | 2024-12-05 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9d0ea82-8abe-373b-af53-a07254cfdfd0 | -3.18531 | -54.50998 | 2024-12-05 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ddfd0cbe-fce9-324c-9487-895ca4e505a2 | -1.68225 | -54.45093 | 2024-12-05 04:46:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 509c3c6f-bdd5-308c-9991-e54c1e73ec7d | -2.15427 | -52.83692 | 2024-12-05 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2c3c7edb-297a-3446-a3bc-668d0efb2a79 | -3.17942 | -53.8544 | 2024-12-05 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb025faa-e86b-38d4-86f9-cdbfd800706f | -1.03 | -53.5573 | 2024-12-05 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c604d554-af32-3bca-aa86-eaa4fc05a2bd | -1.6118 | -53.26279 | 2024-12-05 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcdd0ca2-c929-39fe-9b40-151bc42dbedb | -0.85752 | -52.70829 | 2024-12-05 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| acbb2797-16ec-34a3-bac2-898b5d4b05e2 | -1.5737 | -46.03296 | 2024-12-05 04:46:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf87f85c-28b5-32d6-bff9-5b2cfea2c5d8 | -4.34592 | -46.80857 | 2024-12-05 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b7924cd-cc35-36d0-8e09-591629072fab | -2.93867 | -51.41224 | 2024-12-05 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README9.md)
