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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c19cd9f-2175-333e-89c1-380907d03a63 | -3.1459 | -45.3854 | 2024-12-01 05:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 38f5690b-fdb8-3bb3-ac6b-ebabd4b645e7 | 1.1622 | -55.9869 | 2024-12-01 05:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 66c74370-8125-37fa-bb3b-334b6a633424 | -2.8197 | -53.0425 | 2024-12-01 05:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 4ccf110d-8b1c-35ce-a586-ea32308275fe | 1.1438 | -56.0067 | 2024-12-01 05:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 5dc38f6e-fca0-3a65-9cfd-ac60f5b4e8c5 | -4.5562 | -43.3028 | 2024-12-01 05:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 117.2 |
| ecfc1109-0343-3512-b6c8-d3b3a19a8742 | -3.259 | -53.6388 | 2024-12-01 05:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 857b82c4-1861-3fb4-be6c-2955e97d4afa | -3.146 | -45.3629 | 2024-12-01 05:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 144.2 |
| 45db4128-0f08-3aeb-a797-e447f07ea71e | -3.2591 | -53.6186 | 2024-12-01 05:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 16c00356-dab9-3014-8f29-165d6edc18f5 | -4.5375 | -43.304 | 2024-12-01 05:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 28cfe5a0-0d2a-30ea-8f55-a8e12b0fc50f | -3.1645 | -45.3622 | 2024-12-01 05:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 6205b2b6-759f-38e1-88f5-b65aec71f1a0 | -6.2747 | -35.1412 | 2024-12-01 05:30:00 | GOES-16 | TIBAU DO SUL | RIO GRANDE DO NORTE | Brasil | 2414209 | 24 | 33 | nan | nan | nan | Mata Atlântica | 72.4 |
| 48bfbb45-7915-33a5-822b-173e4b7faaf6 | -2.8013 | -53.043 | 2024-12-01 05:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 8e21e07d-21b7-3539-bbca-b44a88b70d92 | -4.5578 | -45.7232 | 2024-12-01 05:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 74.3 |
| d1f2c1a4-c8c7-33d3-8ba5-92f0c2692be1 | 1.1439 | -55.9871 | 2024-12-01 05:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 134.9 |
| 311ccb08-566c-3e5e-ad22-59b1206a4014 | -6.2744 | -35.1686 | 2024-12-01 05:30:00 | GOES-16 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 77.5 |
| bfdb8f26-0368-3214-9dc3-004668f2e0d4 | -3.1273 | -54.5264 | 2024-12-01 05:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| f5e732e3-fc20-3ae9-a064-f54ab1853180 | -3.4974 | -53.8339 | 2024-12-01 05:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 789c6f41-4ba5-3928-8e3f-b99cae2bdf22 | -6.2747 | -35.1412 | 2024-12-01 05:40:00 | GOES-16 | TIBAU DO SUL | RIO GRANDE DO NORTE | Brasil | 2414209 | 24 | 33 | nan | nan | nan | Mata Atlântica | 148.7 |
| 0ecab3c7-9a7d-3278-a2df-096fb93cc24c | 1.1438 | -56.0067 | 2024-12-01 05:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 3f3232c0-2bb8-3dd2-86f1-ce7da2cc94ae | 1.1439 | -55.9871 | 2024-12-01 05:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| e77cd0bc-fa3b-3e6a-aabf-dbf494f34201 | -4.5375 | -43.304 | 2024-12-01 05:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 1c8cc223-3896-3294-b724-22abf7eddaae | -3.1274 | -45.3637 | 2024-12-01 05:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 9a8cea76-9cea-3961-8e49-d6db4a0b4b03 | -3.2591 | -53.6186 | 2024-12-01 05:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| f43fe832-ab59-3556-b9c7-d53b7da60b79 | -3.146 | -45.3629 | 2024-12-01 05:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 185.6 |
| 96261c1a-04bc-3194-8dbe-9e9b11dec907 | -4.5562 | -43.3028 | 2024-12-01 05:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |
| e47f046c-b73d-3aa4-9a78-6cb63c3e82b8 | -3.259 | -53.6388 | 2024-12-01 05:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 27ee0010-1b9f-3971-884f-b914037d7ca5 | -4.5578 | -45.7232 | 2024-12-01 05:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 0ba024f4-73b5-30ee-92e0-51c6123302e4 | -3.1273 | -54.5264 | 2024-12-01 05:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 432fb290-087f-3432-b181-514d1623749e | -3.4974 | -53.8339 | 2024-12-01 05:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| a9c019d9-0078-3406-af9e-d4d80e984651 | -3.1459 | -45.3854 | 2024-12-01 05:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 91fa1696-c9a8-34b1-af67-2fe4473bf8d1 | -6.2744 | -35.1686 | 2024-12-01 05:40:00 | GOES-16 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 150.5 |
| 91cf3bf5-1560-396c-9f1f-e21119871d06 | -4.5375 | -43.304 | 2024-12-01 05:50:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 95c063f2-ecaf-3d46-9e48-93d6884d39bb | 1.1439 | -55.9871 | 2024-12-01 05:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 8607ef0e-e9e5-31a3-aa13-205f5c84d748 | -3.259 | -53.6388 | 2024-12-01 05:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| adbc4225-150e-38d5-b41e-35ff4f280d5b | -3.1459 | -45.3854 | 2024-12-01 05:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 42715e0a-ab92-3e75-8455-ef94806bf21f | -3.146 | -45.3629 | 2024-12-01 05:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 176.8 |
| 653fce88-d7d0-31c2-9296-ac782bea4fa7 | -3.1273 | -54.5264 | 2024-12-01 05:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| e5b7960e-3918-3f9d-a9c7-40c5b15b34d8 | -6.2553 | -35.1708 | 2024-12-01 05:50:00 | GOES-16 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 70.5 |
| 23052712-02d6-3cfd-b267-73c5edbe20f6 | -6.2744 | -35.1686 | 2024-12-01 05:50:00 | GOES-16 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 122.2 |
| 856560a2-455b-3bee-9164-b476fd909097 | -3.1645 | -45.3622 | 2024-12-01 05:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 93.7 |
| cbf1a88a-1616-3efa-a139-09f0378cfd64 | -3.2774 | -53.6383 | 2024-12-01 05:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 6c2b0011-c04e-3786-8076-4b0a27662711 | -3.2591 | -53.6186 | 2024-12-01 05:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 871750d5-b8b8-32c1-b33f-7ad38c125b71 | -6.2747 | -35.1412 | 2024-12-01 05:50:00 | GOES-16 | TIBAU DO SUL | RIO GRANDE DO NORTE | Brasil | 2414209 | 24 | 33 | nan | nan | nan | Mata Atlântica | 91.2 |
| ae300bba-e3a4-34e6-9821-850698edb4f6 | -4.5562 | -43.3028 | 2024-12-01 05:50:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 113.0 |
| e40609fd-bf62-3a96-9deb-df0c745f3b45 | 1.1747 | -55.95814 | 2024-12-01 05:59:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 56b32c38-84e5-33ba-9cc4-bf32d98e71a0 | 2.73678 | -60.38503 | 2024-12-01 05:59:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9ecb3e49-2599-33ad-8bf4-1aa07e0bdb2a | 1.52796 | -55.70317 | 2024-12-01 05:59:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae5c17f7-896d-3d44-9153-357770668992 | 1.14425 | -56.00487 | 2024-12-01 05:59:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e5851f97-9574-32ee-abfc-e09903bbe09b | 2.73278 | -60.39126 | 2024-12-01 05:59:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f5d15d9d-f4cc-322e-987d-5c50ce5be3fd | 1.15467 | -55.98497 | 2024-12-01 05:59:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4f9da5ad-5301-3e62-9311-a201d9c7d063 | 1.15944 | -55.97221 | 2024-12-01 05:59:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 67b6e7c3-437a-3355-bb21-50594fda2a1e | 3.28103 | -60.06669 | 2024-12-01 05:59:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e80c985-d4af-3ac6-91b4-420ff57b1d62 | 1.15563 | -55.9909 | 2024-12-01 05:59:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 625617b8-1b6e-3882-bfbc-5c00649dbc09 | 0.07847 | -60.46734 | 2024-12-01 05:59:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0800e1ac-4a41-3566-9cc0-a2cc209f66f2 | 0.88891 | -59.54751 | 2024-12-01 05:59:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc20989f-ff9e-3db5-9729-acac0358b9bf | 0.64741 | -60.53006 | 2024-12-01 05:59:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8633ac53-6c3a-3ea5-8beb-ee4849a12f35 | 1.16609 | -55.97107 | 2024-12-01 05:59:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2aee56d8-df77-3450-be06-fe8ad8c6d7fd | 1.14803 | -55.98611 | 2024-12-01 05:59:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 14f770a7-6585-3bf7-9c4c-c01d7684a600 | 1.16039 | -55.97805 | 2024-12-01 05:59:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f8d02e85-6461-3d18-bf1c-c335fc039606 | 0.89371 | -59.54333 | 2024-12-01 05:59:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4c86a7e-4338-3f0f-a1ec-1381fdc81f94 | 0.64789 | -60.53248 | 2024-12-01 05:59:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06895bd4-bb19-34d8-ad95-af2f856327f7 | 1.14234 | -55.99309 | 2024-12-01 05:59:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5e0124ac-6fdf-3bde-8e3a-bd056af5fcfd | 1.14329 | -55.99895 | 2024-12-01 05:59:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 35ed85a5-cb3b-3eba-a245-d759b0549829 | 0.08354 | -60.46651 | 2024-12-01 05:59:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4f7c92d-37bc-3f48-ac73-3b4513d3db42 | 1.15089 | -56.00377 | 2024-12-01 05:59:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 57c56838-6d60-3e8b-9527-62c6dba7338a | 1.53465 | -55.70182 | 2024-12-01 05:59:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3efa738-f819-3a92-b3e5-2061b008ec1e | 0.64785 | -60.53296 | 2024-12-01 05:59:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 247e9cfd-fbc4-3e37-b317-c0ac5baf304b | 1.14898 | -55.99197 | 2024-12-01 05:59:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0d09e1f1-c3ad-3ea4-9c70-f840c3e26584 | 2.73765 | -60.39046 | 2024-12-01 05:59:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5a4e0599-d17b-3077-9734-916dbd0ea08b | 1.15372 | -55.97909 | 2024-12-01 05:59:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b036d394-8e2c-346b-b8ea-7d160103b736 | 3.27699 | -60.07315 | 2024-12-01 05:59:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 737baf5f-db0e-3478-b245-908b461abe4d | -6.9344 | -43.5401 | 2024-12-01 06:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 7381a240-8956-358b-9b07-7742de12cbe6 | -3.259 | -53.6388 | 2024-12-01 06:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 4724fd7a-6855-3cd9-beb6-acd0789f5f4a | -3.1273 | -54.5264 | 2024-12-01 06:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| f45270b1-3d6f-3c3f-abfd-21e109c250b5 | 1.1439 | -55.9871 | 2024-12-01 06:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 6ffb419a-8c59-3cfa-883d-a2016e34694d | -3.1459 | -45.3854 | 2024-12-01 06:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 68c45cb7-2b14-33cd-a7d7-69c5dfd4e0c8 | -3.146 | -45.3629 | 2024-12-01 06:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 210.0 |
| 0dc742e8-337f-34ee-b66f-ea87b04aed5d | -3.1645 | -45.3622 | 2024-12-01 06:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 84.1 |
| f8a5af1a-28ba-331d-bc46-2d068dc41793 | -4.5562 | -43.3028 | 2024-12-01 06:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 48e8ca08-8015-352b-bf71-1a8c97783929 | -3.2591 | -53.6186 | 2024-12-01 06:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 27b79677-8f8d-373a-a63f-544b128841fe | -3.79498 | -58.97198 | 2024-12-01 06:01:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec5a9d65-342f-3561-b93b-3ef5c44224de | -1.33213 | -55.84598 | 2024-12-01 06:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1acfe982-1cfe-360f-b837-898e8e70e9fc | -3.79207 | -58.97678 | 2024-12-01 06:01:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ae0d8ee4-70fc-36c8-a1b4-7bdac25d585e | -3.51635 | -62.7562 | 2024-12-01 06:01:00 | NOAA-21 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b6a7bb1-e222-3a2d-bf5d-7ea3d78616eb | -3.53253 | -62.773 | 2024-12-01 06:01:00 | NOAA-21 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b06ac23c-75fe-3fd6-806c-1b81e2bbc6c3 | -1.2608 | -60.29018 | 2024-12-01 06:01:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e8720b7-9b63-3d57-bea9-14f2cfba5b54 | -3.79861 | -58.97334 | 2024-12-01 06:01:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6777c067-3eb6-3ecd-85cd-30a474f6081b | -2.96111 | -64.99806 | 2024-12-01 06:01:00 | NOAA-21 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14425712-d6f5-34d2-91b1-87f950339eb6 | -3.52588 | -62.84787 | 2024-12-01 06:01:00 | NOAA-21 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 015ada38-d9ac-307a-817c-2103934978b8 | -5.43023 | -60.1848 | 2024-12-01 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c06e297a-69d7-3f57-8dea-39eb1ad692be | -2.85201 | -65.20776 | 2024-12-01 06:01:00 | NOAA-21 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d8760003-2ec8-32d3-9aff-b8ddeb7e530f | -2.85084 | -65.20438 | 2024-12-01 06:01:00 | NOAA-21 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0916c461-b42d-3348-af3f-c52690690a7d | -2.85013 | -65.20917 | 2024-12-01 06:01:00 | NOAA-21 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86dc0d13-6b3c-37c9-8597-553cc32ba6ac | -6.61358 | -60.09108 | 2024-12-01 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 01b9745d-e436-3316-82eb-49bf09d5504e | -3.50789 | -62.75013 | 2024-12-01 06:01:00 | NOAA-21 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2c177db-13cb-31fa-b9f4-f28537759c27 | -1.33112 | -55.85258 | 2024-12-01 06:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d93e5962-1e2b-3fac-97a7-8d96d556cfbe | -3.51177 | -62.7555 | 2024-12-01 06:01:00 | NOAA-21 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a01bb84d-61c5-3acf-a822-b15ada0c22db | -3.51565 | -62.76086 | 2024-12-01 06:01:00 | NOAA-21 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0f8b1ea-cf64-3a1c-85d2-98dd30473b2d | -0.18711 | -60.67635 | 2024-12-01 06:01:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8900bf8c-7283-390c-a575-ddb58742df18 | -3.52022 | -62.76155 | 2024-12-01 06:01:00 | NOAA-21 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README100.md)
