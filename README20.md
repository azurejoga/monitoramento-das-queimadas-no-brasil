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
| d1b9dca1-6e38-366a-a74b-4b69e49837dd | -7.88351 | -35.22546 | 2024-12-02 02:47:00 | NPP-375D | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 9a855a13-acf5-3a99-bd5a-06bfb5f4198f | -7.88553 | -35.2243 | 2024-12-02 02:47:00 | NPP-375D | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| d6769be8-6a6f-3061-afca-7d92e1403dab | -7.84222 | -34.96256 | 2024-12-02 02:47:00 | NPP-375D | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 6439cc93-9ce4-36a2-8ef5-013a9bd2b231 | -7.89202 | -35.21983 | 2024-12-02 02:47:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8066d238-0462-3922-af6b-f1539a785889 | -7.89064 | -35.227 | 2024-12-02 02:47:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| edcdb996-1e7b-3bf9-9648-99392ef6f9cd | -7.80634 | -35.30643 | 2024-12-02 02:47:00 | NPP-375D | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 82a5ac01-9383-3f2a-a211-9ce2f6b61935 | -7.88694 | -35.21725 | 2024-12-02 02:47:00 | NPP-375D | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 02c1ca2a-abaf-3aa7-8c7a-09203f9e966c | -7.88486 | -35.21846 | 2024-12-02 02:47:00 | NPP-375D | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 890391aa-96fe-3c9d-a880-4ae9c7a02a84 | -2.8196 | -53.0629 | 2024-12-02 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 1ebf6097-5119-3fbc-aac4-5a8bfa9cec60 | -2.5428 | -53.4137 | 2024-12-02 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 1b6202d5-cb72-330a-830c-062f0d8246b7 | -6.086 | -48.0557 | 2024-12-02 02:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 50517434-3666-393b-9522-e435f36cdc9d | -12.4169 | -63.7465 | 2024-12-02 02:50:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 125.7 |
| 12fd9cc2-e416-35ce-a7f3-3f77529d01a6 | -2.6348 | -53.3712 | 2024-12-02 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 61f35e5a-1c3d-378b-b49e-19d436cf1029 | -20.7217 | -54.4341 | 2024-12-02 02:50:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 114e2676-1cde-3db3-9f50-76f46bea657d | -5.118 | -43.2198 | 2024-12-02 02:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 90f8b461-ca67-302c-bfc0-93ad4b80883c | -12.4358 | -63.7455 | 2024-12-02 02:50:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 92.3 |
| d15ae655-672b-3153-a2da-a62016c970a6 | -3.4017 | -50.2381 | 2024-12-02 02:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 2a32472b-e157-3a5a-93d1-034020d126ca | -2.5612 | -53.4133 | 2024-12-02 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 4ddc2df4-7f1e-3ac2-8d56-ed609d456d15 | -5.5882 | -45.1412 | 2024-12-02 02:50:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 2d302975-a790-349e-8908-ef8c75688eaf | -3.2591 | -53.6186 | 2024-12-02 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| b5af0431-8e2c-32f0-a128-7364cafba99a | -2.5612 | -53.3931 | 2024-12-02 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 75726abc-a01b-340b-a3ca-fc311a093b57 | -12.4171 | -63.7274 | 2024-12-02 02:50:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 375bf9b9-8d1d-31c5-81f4-a2bdf1a7fb19 | 3.3657 | -60.5329 | 2024-12-02 02:50:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 5c943aee-ca8a-3738-b483-457cc30d06ab | -3.259 | -53.6388 | 2024-12-02 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 6e9a8938-e926-3b47-b9a1-69eef7df68b2 | -5.1369 | -43.1951 | 2024-12-02 02:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 6daddd40-9c4c-337f-b67b-82f42f7cdf0c | -4.5745 | -43.3483 | 2024-12-02 02:50:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 1799ee5c-1ae1-30ba-b1c3-6923b35d5cdb | -5.1181 | -43.1964 | 2024-12-02 02:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 1db0432f-b541-3aaa-9875-1c572041c6fe | -2.6349 | -53.351 | 2024-12-02 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 708c0da9-cee9-3aa7-a1cf-0bfc9353dd32 | -12.4359 | -63.7264 | 2024-12-02 02:50:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 67ba82c2-1f63-3fb1-a84b-fc58b25005fd | -2.8013 | -53.043 | 2024-12-02 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 36f6d623-7722-36f3-ad7f-e06c61b468f8 | -2.7759 | -55.3509 | 2024-12-02 02:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 31279774-3be5-3272-8e3f-67d8c680757d | -4.267 | -50.8551 | 2024-12-02 02:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| f5ac8f12-62bc-3c08-9bec-acfef36e9293 | -2.8012 | -53.0633 | 2024-12-02 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 4e0e9e15-ed02-33e4-afcd-0e795441adf7 | -2.8197 | -53.0425 | 2024-12-02 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 4af1df6f-db09-30d1-b332-f1054735f7ae | -5.1181 | -43.1964 | 2024-12-02 03:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 6288d2db-77b1-3edd-8f19-645bc56bbe55 | -2.8196 | -53.0629 | 2024-12-02 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 5dbf792a-ec5b-3068-8c5b-c2ac0b54a20a | 1.1072 | -56.007 | 2024-12-02 03:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| b3ba7216-7683-3f52-870e-d972f84f5b2c | -5.1369 | -43.1951 | 2024-12-02 03:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 379c8c4f-e912-368a-a27f-a88a659a8c6c | -6.086 | -48.0557 | 2024-12-02 03:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 440b762a-a98f-3579-bf6a-82f289d74cc8 | 1.1255 | -56.0069 | 2024-12-02 03:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 51537b17-6434-3241-a645-cdcb669bb290 | -12.4169 | -63.7465 | 2024-12-02 03:00:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 09c4bfc0-6e2f-37d9-ac48-acce6b33abfb | -1.0735 | -53.4562 | 2024-12-02 03:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| db75d08e-5d92-309f-b88a-94de4b01e4ec | -12.4359 | -63.7264 | 2024-12-02 03:00:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 7556a7b8-30f1-399d-8771-50cbe8bb115e | -3.259 | -53.6388 | 2024-12-02 03:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 8903aaa6-2ea6-391b-bc5d-8979a00eb33e | -2.7759 | -55.3509 | 2024-12-02 03:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 17604f2b-79bc-30c8-8c23-55f7af9a98b1 | -12.4171 | -63.7274 | 2024-12-02 03:00:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 4b17bba6-34e4-3409-bdf4-7f72c004ae92 | -3.2591 | -53.6186 | 2024-12-02 03:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 0ef779aa-e72a-3bd7-8db5-06820afe0c4a | -2.6349 | -53.351 | 2024-12-02 03:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| b2711cd8-11bd-36ef-a6d1-ecc5ad5e6f95 | -4.5745 | -43.3483 | 2024-12-02 03:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 8ee82575-2fe7-3fca-b939-be5b596c414e | -5.5882 | -45.1412 | 2024-12-02 03:00:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 5b38b52d-5e5e-3901-92ec-834aff3bc76d | -2.5612 | -53.3931 | 2024-12-02 03:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| bd7c2add-f1d6-3b48-b46b-bbe8a5ba07c2 | -12.4358 | -63.7455 | 2024-12-02 03:00:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 4b52c534-bfb5-316f-b7ba-e95baea10dc1 | -2.8012 | -53.0633 | 2024-12-02 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 06e3d734-6e73-3945-b587-4653443f71e3 | 1.1256 | -55.9872 | 2024-12-02 03:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 8bc244a1-11e2-3da6-8e41-8ca82d7a3e85 | -2.8197 | -53.0425 | 2024-12-02 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 2cf9a8ee-d590-34f4-9b3c-9678db86ad16 | -2.5428 | -53.4137 | 2024-12-02 03:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| f01fa39c-17a0-3857-ada5-56c4b74f97de | -2.8013 | -53.043 | 2024-12-02 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 55cc2945-06f5-35ae-9e5a-e73c1d1583a7 | 1.1072 | -55.9874 | 2024-12-02 03:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 1fdba59f-8d31-3ad9-98af-d8f8f422d410 | -2.6348 | -53.3712 | 2024-12-02 03:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 3291de0e-d631-35d5-8228-0a5d01752481 | -5.118 | -43.2198 | 2024-12-02 03:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 3deef7a0-56a1-3344-8f01-9f7e6a37331d | -2.5612 | -53.4133 | 2024-12-02 03:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 298a11c2-1fb5-3168-a89c-73fc69166478 | -8.15583 | -35.12184 | 2024-12-02 03:08:00 | NOAA-20 | MORENO | PERNAMBUCO | Brasil | 2609402 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a574b8dd-bb56-3712-a581-86c72f3a2217 | -5.19693 | -37.69474 | 2024-12-02 03:08:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 6.5 |
| e4044f01-01e8-3fb1-92a4-45df40f46e91 | -5.19447 | -37.69207 | 2024-12-02 03:08:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 90f20447-17c8-30f9-97ef-3be1623638d1 | -6.73004 | -35.00121 | 2024-12-02 03:08:00 | NOAA-20 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6c8e0ee8-66a6-3e84-bd87-4177ab9d786c | -4.75308 | -38.47173 | 2024-12-02 03:08:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 452d7e60-307c-3720-919c-6919be395c34 | -5.88868 | -35.42584 | 2024-12-02 03:08:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0eb10f81-fcf6-357b-a9ae-d0f3d61390f9 | -6.73192 | -35.0001 | 2024-12-02 03:08:00 | NOAA-20 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 130f2e36-bcb3-3379-9012-8f07639fc545 | -5.19767 | -37.69041 | 2024-12-02 03:08:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 152c9e9b-8529-362d-a511-a2abcaac679a | -2.9531 | -39.97026 | 2024-12-02 03:08:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 569fa99f-2395-3f5c-bad4-12f31106eed3 | -4.75222 | -38.47658 | 2024-12-02 03:08:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8d929dc0-6f00-3207-b382-b5c2ef6550a2 | -8.2611 | -35.36297 | 2024-12-02 03:08:00 | NOAA-20 | POMBOS | PERNAMBUCO | Brasil | 2611309 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| c3cb9066-064a-36d7-8dc8-1e16179d0801 | -8.26018 | -35.36822 | 2024-12-02 03:08:00 | NOAA-20 | POMBOS | PERNAMBUCO | Brasil | 2611309 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 55f8b4b1-ff28-3986-94a8-1784d9157014 | -2.8013 | -53.043 | 2024-12-02 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 3b1704d2-c7e5-3c09-b459-0d62dff17362 | -6.086 | -48.0557 | 2024-12-02 03:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 156d686a-3cc4-3866-bff4-1d10117ec111 | -2.5612 | -53.3931 | 2024-12-02 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 9e86ebd3-4a26-38a4-a4b6-db23fb89d96b | -2.8196 | -53.0629 | 2024-12-02 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| ea9b1827-dc9a-32b2-907a-f854beb64a84 | -5.1369 | -43.1951 | 2024-12-02 03:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 25cca7da-5ee5-3a94-a923-c9b2fc31ca33 | -2.7759 | -55.3509 | 2024-12-02 03:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 6fbd8c64-60f8-3cfc-b652-df53d9989bea | -3.259 | -53.6388 | 2024-12-02 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 6f2bd516-e7b3-3e78-9554-2425f93c4355 | -4.5745 | -43.3483 | 2024-12-02 03:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 8cb917dd-a60b-362b-a2d6-eb4d7acb2131 | -2.8197 | -53.0425 | 2024-12-02 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| f5dea3ac-fce7-3a8d-b810-a9933a88da01 | -5.1367 | -43.2185 | 2024-12-02 03:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 2c34c482-0c93-309d-9b1d-e6c0443bd13d | -2.8012 | -53.0633 | 2024-12-02 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 214cbd96-cb56-379b-9ef9-687439501575 | -3.2591 | -53.6186 | 2024-12-02 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| dc8d9c46-381b-3f73-9ceb-0dd9740bf37c | -5.1181 | -43.1964 | 2024-12-02 03:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 90df8cec-d242-3643-986b-c44988d74bbf | -12.4169 | -63.7465 | 2024-12-02 03:10:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 90d70bae-2df7-38bd-ad53-eddd32d41818 | -5.5882 | -45.1412 | 2024-12-02 03:10:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 6ba8c430-d77a-3a18-8ada-73264c7462cc | -12.4358 | -63.7455 | 2024-12-02 03:10:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 191ccb0d-4c04-3620-b314-8f5b1d6bdb3e | -5.118 | -43.2198 | 2024-12-02 03:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 8a214501-3ae1-3b1a-ba7a-1e915cf08249 | -12.4359 | -63.7264 | 2024-12-02 03:10:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 20ffc8b3-d1d7-389e-96f2-5282ea9571b6 | -2.6348 | -53.3712 | 2024-12-02 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 71a57b3c-cfe7-3d4c-b1d1-d6a4d4860f7a | -2.6349 | -53.351 | 2024-12-02 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 2dd34152-c49b-3765-84b5-17f08685832b | -2.5612 | -53.4133 | 2024-12-02 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| f4be777b-2b57-3294-8a49-1a7724616902 | -2.5428 | -53.4137 | 2024-12-02 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| be921a9e-2c26-3063-b67f-cc859055a9de | -9.78095 | -36.14659 | 2024-12-02 03:10:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 75c1a515-8b20-3542-8562-25b749bcc7f0 | -11.27602 | -41.73467 | 2024-12-02 03:10:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 4fc722d7-86da-3781-bec7-841eba961a86 | -9.83972 | -36.16417 | 2024-12-02 03:10:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9e57fa6f-88d4-33bf-bdfe-1da61285e5df | -10.05134 | -36.5556 | 2024-12-02 03:10:00 | NOAA-20 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4a4575a9-81ec-3b47-826c-ee07438749a0 | -10.05192 | -36.55248 | 2024-12-02 03:10:00 | NOAA-20 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |


[Clique aqui para ver as próximas entradas](README21.md)
