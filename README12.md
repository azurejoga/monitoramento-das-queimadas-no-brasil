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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9788824a-2901-3b72-a0cd-dd19d4c4076c | -7.3638 | -72.8628 | 2024-10-20 01:15:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 82.0 |
| c52bd00a-06b3-3245-a88f-132b8c01a0d9 | -17.4136 | -40.2217 | 2024-10-20 01:16:42 | GOES-16 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 114.0 |
| 43300469-e2bb-3a25-87b8-40baa7462d85 | -17.4144 | -40.1957 | 2024-10-20 01:16:42 | GOES-16 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 117.4 |
| 65f516bd-8302-313b-8cba-22c0d43c4291 | -17.4338 | -40.2162 | 2024-10-20 01:16:42 | GOES-16 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 80.0 |
| 491a1878-58d1-36e7-8349-89eb05284352 | -17.4346 | -40.1903 | 2024-10-20 01:16:42 | GOES-16 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 83.7 |
| f7fea3d3-49d1-311d-88ba-836059b72435 | -2.2993 | -48.5936 | 2024-10-20 01:25:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 5e85a3b8-57d2-3c19-a7d9-0e51e3b0b5d7 | -2.2994 | -48.5722 | 2024-10-20 01:25:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| d18b19fe-77a7-3458-b27c-b96604c11e87 | -2.7773 | -49.3067 | 2024-10-20 01:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 130.3 |
| bc514dbc-b8de-32c8-83e5-7de9eb7fcd13 | -2.7774 | -49.2854 | 2024-10-20 01:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 391b4570-2c8e-33ba-a74b-09789dc5d229 | -2.7958 | -49.3062 | 2024-10-20 01:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 200.8 |
| 4f039da5-e21f-3e0d-9037-fd0d6986a259 | -2.7959 | -49.2849 | 2024-10-20 01:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 3be73e4d-c63b-39b4-881e-8d765d5df227 | -2.7981 | -48.6873 | 2024-10-20 01:25:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 279001aa-9608-3595-94c2-6031561eb781 | -3.0478 | -51.0226 | 2024-10-20 01:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 203da8fd-19f9-3c12-afa9-fe0420c9b014 | -3.1462 | -54.3658 | 2024-10-20 01:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| c453fd4e-efa4-3676-a6c7-9196553db84a | -3.1462 | -54.3457 | 2024-10-20 01:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 6bb4a9c1-3457-312e-98fe-c3d22eda116c | -3.3813 | -50.6788 | 2024-10-20 01:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 066711f3-454f-39b3-942c-1c683892f88f | -3.3814 | -50.6579 | 2024-10-20 01:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 84b25fcd-2fc7-3e3e-b296-aa9c32347cf7 | -3.3998 | -50.6573 | 2024-10-20 01:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 5c1dcd6c-ca89-37f0-bc6f-ccb4d82e2a29 | -3.586 | -54.6941 | 2024-10-20 01:25:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 17e48ae3-6f39-3bda-8d46-b84537461c4e | -3.5861 | -54.6741 | 2024-10-20 01:25:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| f1ae2f71-aba6-3159-b87d-fce572323e35 | -3.5862 | -54.6541 | 2024-10-20 01:25:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 8760206b-b2b1-37ec-bfe0-394861451db9 | -3.6045 | -54.6736 | 2024-10-20 01:25:27 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 1da2a325-a7f2-3f1f-af8c-9d08b79046d6 | -3.8686 | -45.8254 | 2024-10-20 01:25:28 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 26a6a2cd-a48a-34ac-8f99-85423991fb9f | -4.1985 | -46.6318 | 2024-10-20 01:25:30 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 0ad21774-488d-302b-8a70-7385c1ad4f6a | -4.911 | -45.8374 | 2024-10-20 01:25:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 5aeeaf0e-4149-3dfe-8671-ae0b13f3c31f | -4.9112 | -45.8151 | 2024-10-20 01:25:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 80.2 |
| f7c6a67a-213a-33af-8a6f-5f657d27ec51 | -5.226 | -46.0865 | 2024-10-20 01:25:36 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 79.4 |
| a4075b45-6771-3ce4-a122-b3a62995c4ad | -5.4476 | -46.362 | 2024-10-20 01:25:37 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 3d9df065-c74d-39ca-b2f3-63bc7c7eb027 | -5.721 | -68.6862 | 2024-10-20 01:25:39 | GOES-16 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| eb1c7c6f-9396-3284-b119-88395c46a55b | -7.3637 | -72.881 | 2024-10-20 01:25:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| b7b2b8e9-1793-36fc-9c52-cfff080fd01d | -7.3638 | -72.8628 | 2024-10-20 01:25:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 99ade17c-4075-31f6-a6d9-9ae054837f2d | -7.7679 | -73.079 | 2024-10-20 01:25:51 | GOES-16 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 656c84c1-abaa-38fa-b9a5-23021d74bf0a | -1.165 | -53.6571 | 2024-10-20 01:35:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| c940ea67-6339-3315-af10-3328450075d8 | -1.1834 | -53.6569 | 2024-10-20 01:35:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 589bc29d-3029-3d88-a0d1-a6c2bb7c7118 | -2.2993 | -48.5936 | 2024-10-20 01:35:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| b7007e8b-3abb-3fde-a772-7255cc607a1b | -2.2994 | -48.5722 | 2024-10-20 01:35:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 30c35f20-2b87-3666-a1a4-bb8fb265a565 | -2.7773 | -49.3067 | 2024-10-20 01:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 121.2 |
| a31485d0-6fe7-3f0d-88a7-4f0e13ad06ac | -2.7958 | -49.3062 | 2024-10-20 01:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 179.5 |
| a0e6d5df-002c-3dde-9f38-3d88c5a18f59 | -2.7959 | -49.2849 | 2024-10-20 01:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 81ceee70-1983-33d2-9ed7-aabbad59157a | -2.7981 | -48.6873 | 2024-10-20 01:35:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 4cbbdd41-06c3-3c71-bf44-bc57a0b53cba | -3.0293 | -51.0231 | 2024-10-20 01:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| b7011262-3d38-3540-85b9-0079e0e8a761 | -3.0478 | -51.0226 | 2024-10-20 01:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 9afe886f-3e80-38af-861f-335059b4c6d3 | -3.1462 | -54.3658 | 2024-10-20 01:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| bd85c4d9-f4ce-34c9-8173-9ea9a93ba519 | -3.1462 | -54.3457 | 2024-10-20 01:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 11305018-673b-33f6-a9e3-82a0da4e0d97 | -3.3813 | -50.6788 | 2024-10-20 01:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| d4714ca8-132c-3de8-8281-435c6595f109 | -3.3814 | -50.6579 | 2024-10-20 01:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| e32e8bfd-6dc8-37d4-b0e4-9f113dec5172 | -3.3998 | -50.6573 | 2024-10-20 01:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| caef54bb-9b7f-32f4-92a8-222ddb48bbec | -3.586 | -54.6941 | 2024-10-20 01:35:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| b137708c-a9b8-3cad-b790-dd74af7a80b8 | -3.5861 | -54.6741 | 2024-10-20 01:35:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| d2d9403a-3a01-3687-882f-08de0f316c41 | -3.8686 | -45.8254 | 2024-10-20 01:35:28 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| a2627276-1920-3e55-bf61-3a89573e48db | -3.9062 | -45.7565 | 2024-10-20 01:35:28 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 5b17e2e1-8780-38b4-a6a2-5bddceb78f50 | -3.9018 | -49.9884 | 2024-10-20 01:35:28 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 3fdce7c2-8638-39a4-a468-9e7d75f2a890 | -4.9112 | -45.8151 | 2024-10-20 01:35:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 72.3 |
| aadc26f4-3deb-3fe9-8802-1db62993c07a | -5.226 | -46.0865 | 2024-10-20 01:35:36 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 7a82e42f-e4bc-3a68-99bc-15d7044a0a35 | -7.3637 | -72.881 | 2024-10-20 01:35:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 6584aa32-8361-3dac-9496-45f795358334 | -7.3638 | -72.8628 | 2024-10-20 01:35:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 564aaf71-cae5-338f-9e85-200093519df8 | -7.7679 | -73.079 | 2024-10-20 01:35:51 | GOES-16 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 70.4 |
| c435fbe5-1f6f-3446-81f0-f2e2e2a499eb | -8.5587 | -44.7414 | 2024-10-20 01:35:54 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 25544c5e-7a12-3964-97b3-33bb1ca0e89a | -1.165 | -53.6571 | 2024-10-20 01:45:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 02bb8fa5-91a3-38b2-8a02-aa4d5e42e7ca | -2.2993 | -48.5936 | 2024-10-20 01:45:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 7a293e3e-e566-3f84-b222-002bc6e90bfb | -2.2994 | -48.5722 | 2024-10-20 01:45:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| b237d896-ecad-36a7-ac93-bbe17985bb33 | -2.7773 | -49.3067 | 2024-10-20 01:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 135.0 |
| 9e6909ac-c7e0-3eec-9965-98bda461236d | -2.7958 | -49.3062 | 2024-10-20 01:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 123.9 |
| ac360b14-58e3-30a2-8167-4a52e2bda524 | -2.7981 | -48.6873 | 2024-10-20 01:45:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| ddc3a561-e83d-38d2-9164-543de503ab88 | -3.0478 | -51.0226 | 2024-10-20 01:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| aaafb5ec-c5d0-30eb-a973-55d74c32ce2a | -3.1462 | -54.3658 | 2024-10-20 01:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| fc6e2b8b-1d60-3479-9635-bb5e84ccc607 | -3.1462 | -54.3457 | 2024-10-20 01:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| ce0d2a8c-eb81-3600-8cd1-759cd6ee8491 | -3.3813 | -50.6788 | 2024-10-20 01:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 5b81a117-9e0a-3327-9bb4-77286cf103f6 | -3.3814 | -50.6579 | 2024-10-20 01:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 6ed8976f-6696-3a5f-9d57-d217218c7e3c | -3.3997 | -50.6782 | 2024-10-20 01:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| de491f6d-9c3d-3436-8a48-bbfc8dccbb17 | -3.3998 | -50.6573 | 2024-10-20 01:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 6b611420-1fbf-38fb-81f6-87128d533b3d | -3.586 | -54.6941 | 2024-10-20 01:45:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 9c1d1603-df89-320f-93b7-a895a05c1d65 | -3.5861 | -54.6741 | 2024-10-20 01:45:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| f1154a09-c9a4-34e7-a3b1-ff15e5f4439a | -3.8334 | -48.8866 | 2024-10-20 01:45:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| b8e89b67-1108-3e52-b6b2-757914672457 | -3.8686 | -45.8254 | 2024-10-20 01:45:28 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 67.9 |
| f14d93cf-a777-3cc8-ba0f-130568c9ed7d | -3.9248 | -45.7557 | 2024-10-20 01:45:28 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 4e8d9f66-55cc-3c17-a921-6efc374dc72b | -4.1985 | -46.6318 | 2024-10-20 01:45:30 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 799d5bf1-69d5-3c44-becd-f4037ee31eba | -4.2478 | -51.0018 | 2024-10-20 01:45:30 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 6410b36d-5f7a-3bf4-a9b5-a479424a714c | -4.2479 | -50.981 | 2024-10-20 01:45:30 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 951780ed-0a6c-3594-8653-0eebef983983 | -5.2072 | -46.11 | 2024-10-20 01:45:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 60d38153-6395-3159-8720-2a2b655c50a1 | -5.2073 | -46.0876 | 2024-10-20 01:45:35 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| b249f812-3e42-342f-b759-62b40fb4981f | -5.721 | -68.6862 | 2024-10-20 01:45:39 | GOES-16 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 5a3ad039-e726-3d1b-8af5-6a1c59ab7924 | -13.0082 | -55.9699 | 2024-10-20 01:46:20 | GOES-16 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 852422fb-ebe3-381b-b852-cd70a8a6248a | -21.6518 | -57.8438 | 2024-10-20 01:50:35 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b54964ff-bc3c-330d-99aa-27b9c1f94f61 | -12.9846 | -55.9687 | 2024-10-20 01:52:47 | METOP-C | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 588fe596-547b-3175-a476-ee1960271dd3 | -12.9886 | -55.9841 | 2024-10-20 01:52:47 | METOP-C | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d8c17894-1645-3c08-86b5-52c053b650fb | -12.7348 | -62.7071 | 2024-10-20 01:53:17 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 32c330a8-5a5a-3fbf-a4ac-524b875809e6 | -1.165 | -53.6571 | 2024-10-20 01:55:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 2b92426c-0288-36b5-b6c2-95922bde8621 | -1.1834 | -53.6569 | 2024-10-20 01:55:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 09a78e25-8994-30df-8b15-a4ce26e3b61a | -7.6786 | -73.046997 | 2024-10-20 01:55:16 | METOP-C | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| a15b56d6-ba08-3d05-8e66-0e47f30eb072 | -7.5545 | -73.036499 | 2024-10-20 01:55:18 | METOP-C | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| c9c9a65a-1bf6-3ebc-b55d-f7e5f45d0fab | -7.5582 | -73.053802 | 2024-10-20 01:55:18 | METOP-C | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 17a3906d-4477-3dfe-87bd-4b09d23c073c | -2.2993 | -48.5936 | 2024-10-20 01:55:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 45db18e1-f09c-35ea-9bed-2e1711603134 | -2.2994 | -48.5722 | 2024-10-20 01:55:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 0841f863-5b97-392f-b18a-99b2e5e30008 | -3.1256 | -54.372398 | 2024-10-20 01:55:20 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4888182e-0e18-3fea-9cb3-ad48c90ed1d6 | -7.3425 | -72.8508 | 2024-10-20 01:55:21 | METOP-C | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9005c4eb-4597-3cbd-b80a-eb81cae0229d | -7.3461 | -72.867401 | 2024-10-20 01:55:21 | METOP-C | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d4ed1f0f-df2c-36f3-8f66-ba593278b35f | -7.3328 | -72.852798 | 2024-10-20 01:55:21 | METOP-C | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9767dfc3-2740-3fbd-bff3-6b4b3723c000 | -7.3364 | -72.8694 | 2024-10-20 01:55:21 | METOP-C | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8ccb8a9c-8ddc-3d7b-96ea-25aa30cb6337 | -2.7773 | -49.3067 | 2024-10-20 01:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |


[Clique aqui para ver as próximas entradas](README13.md)
