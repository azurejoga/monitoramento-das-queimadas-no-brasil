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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 333cdce3-c1c1-3724-9b29-c8bc0abbe873 | -3.01314 | -50.48082 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| b172d5b6-dc86-3e1f-bda4-2ae4bff6c907 | -3.01232 | -50.48655 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| df6363f6-bd93-326f-991b-28984e38b74f | -3.00756 | -50.4838 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| e4cef59b-56f3-3d00-b340-e81c69c7377b | -3.00656 | -50.47972 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 8e89fae7-dad8-3a60-be76-05a9063afef6 | -3.00574 | -50.48549 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 719ebb56-7506-319d-b508-3a0b3b482297 | -3.00099 | -50.48273 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 1f9e4da7-4357-3227-8428-d68742091c29 | -3.00013 | -50.48846 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| d4940085-4991-3000-b9a0-1b3e8f00db13 | -2.99917 | -50.48438 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 5bcf90f0-8e6f-3d21-bae8-c2a4fc9ede5b | -2.99836 | -50.49012 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 7d51156a-8527-3001-8ad2-4fe4d0b2b4f4 | -2.99442 | -50.48157 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| e5f89ca0-25b5-3369-9450-4018d17ded10 | -2.99357 | -50.48735 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| ace4cc23-749b-394c-844b-090ba1625dd5 | -2.99261 | -50.48314 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| c9b384dc-f798-3b54-881f-0b13306883cf | -2.98791 | -50.48002 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2015c740-b16e-3f7f-92a7-775a4f940b45 | -3.25517 | -50.202 | 2024-10-26 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ff6996db-c729-3111-ab3e-f95b55b3620b | -3.25435 | -50.20753 | 2024-10-26 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2ffc157e-311d-367d-8898-635dabbf9e94 | -3.23592 | -50.19271 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 985e59ed-d850-3826-9178-880bb96f35e6 | -3.2301 | -50.18545 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ffd3225a-e0f6-3b34-8078-826a11d10303 | -3.22924 | -50.19139 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3ca60f3b-f4bf-3302-9ec1-07e115262770 | -2.96238 | -50.42424 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d5de7c79-3a7d-3f0f-ba66-b19ceacf0afe | -2.96155 | -50.42996 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0e0bfbe9-d8e8-3008-9c28-eb34c7172a26 | -2.95579 | -50.42313 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d1d22052-65a0-3fcc-be74-ed0eac1764d6 | -2.95495 | -50.42887 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 925518c8-f4bd-3c2e-86b3-b291874c075f | -2.8296 | -49.25316 | 2024-10-26 05:36:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| add6ee19-7a3a-3441-996c-8db7caeae037 | -2.82255 | -49.25203 | 2024-10-26 05:36:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f9c74574-8d8b-3694-be0f-188a8b756535 | -2.82154 | -49.2589 | 2024-10-26 05:36:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 60c50e5d-fd1d-3090-a145-933b796f2798 | -2.81549 | -49.25089 | 2024-10-26 05:36:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2ad5e348-7863-335a-8983-a89f2b433fc5 | -3.918 | -49.38713 | 2024-10-26 05:36:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1515cc6b-7536-31e0-8122-87cdc49e0610 | -3.66268 | -50.1277 | 2024-10-26 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 48aee042-caba-3196-8740-deeb7b3a1efd | -3.65684 | -50.12012 | 2024-10-26 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ce1805bd-92d4-30bb-937e-bf8b2e8d31f3 | -3.65593 | -50.12646 | 2024-10-26 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6a9f4286-4460-3870-836e-d56f45acedf2 | -3.65505 | -50.13258 | 2024-10-26 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 87c5532c-3de2-3c1f-936e-f21a1dd1610d | -4.39551 | -50.52579 | 2024-10-26 05:36:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4f905dd9-fad8-39e2-acd9-7ef4baddbdee | -4.29761 | -50.73644 | 2024-10-26 05:36:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b40fd076-c1e8-3773-8dcc-a20d8f11c945 | -4.29102 | -50.73542 | 2024-10-26 05:36:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b78bafea-d84e-3bab-85d5-5ff57c8ce60a | -3.51399 | -51.01977 | 2024-10-26 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 212742c7-f639-31c9-b397-b0808666c3ec | -2.84119 | -51.81078 | 2024-10-26 05:36:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b883bbb-4c8b-3d03-891e-5bf4972b790d | -2.84053 | -51.81528 | 2024-10-26 05:36:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58db5c02-ded2-3479-9453-c5addb45704a | -2.83513 | -51.80982 | 2024-10-26 05:36:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2f770d7-2a80-3a24-9b8e-338e4947a13e | -2.83447 | -51.8144 | 2024-10-26 05:36:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ea93cb6-90b7-340c-aa6f-5f4ad0d7955d | -3.12957 | -50.60288 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c92ef0cb-b5a9-3ded-be19-a34c28f76fc4 | -3.12905 | -50.60196 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c4e5baf7-bf70-3666-949d-edb7fe4fddbe | -3.12878 | -50.60807 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 44f86d10-de0f-3399-a17a-1c6bbf528c23 | -3.12829 | -50.60725 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1804b58d-bdb0-38cb-bfeb-d705aad7d8dc | -3.12304 | -50.60174 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fee9a555-9cb6-34c4-a028-8338c0098a85 | -3.12252 | -50.6008 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6eed2c6f-3f11-3c22-831e-aec92c022219 | -3.12176 | -50.60609 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 948773f1-bbb5-37d0-b0c8-b9c5b19cdaed | -2.55724 | -50.6941 | 2024-10-26 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f56fa08f-4fb0-388b-b28c-4b00f6413134 | -3.94829 | -52.25632 | 2024-10-26 05:36:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a19df286-1fae-3646-9dde-aed5624cf63b | -3.94515 | -52.25674 | 2024-10-26 05:36:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2eb5b6a-6339-3cf1-bdef-b613d462d69e | -3.94231 | -52.25541 | 2024-10-26 05:36:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1011668-20f5-39f2-9397-e24c7971f9f0 | -2.97877 | -53.26465 | 2024-10-26 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6e4e7342-a6d5-3947-b782-f72ff941ed9a | -2.97825 | -53.26817 | 2024-10-26 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 56d82ccd-b9ec-3b80-a574-10a5c9472066 | -2.97323 | -53.26396 | 2024-10-26 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7e30b8ac-6262-3254-b74d-0a180f3e8111 | -2.97271 | -53.26748 | 2024-10-26 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5ea0a2cb-7826-371d-949f-04c1d7317a8c | -2.97219 | -53.271 | 2024-10-26 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 64e27b07-3da1-37b9-875e-d66d004b3008 | -2.96718 | -53.26677 | 2024-10-26 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a4266eb5-fa46-3d63-8332-5981b1c8fcff | -2.95096 | -52.56657 | 2024-10-26 05:36:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 7fbbc5f8-3ba1-3b1d-b899-28e7cb27903d | -2.95036 | -52.57072 | 2024-10-26 05:36:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 2781247a-ad8d-31ca-9a3d-cc8c2af8d693 | -2.94583 | -52.56123 | 2024-10-26 05:36:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e58398b3-f6df-3060-84f6-cc967eb0686c | -2.94521 | -52.5655 | 2024-10-26 05:36:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 8451bc82-1485-3d4e-bafe-67831a508816 | -2.9446 | -52.56973 | 2024-10-26 05:36:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 8f9b77db-a076-319e-b295-0a1d43e56bcf | -2.94216 | -52.98095 | 2024-10-26 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9229a27-037d-3fdb-80e4-ddd3a3cbd0cb | -2.94155 | -52.98503 | 2024-10-26 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 86b2f518-df53-3009-abd0-ba7bf4778578 | -2.88562 | -53.32055 | 2024-10-26 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 322b9b6e-7022-3cbf-986f-629299762fc2 | -2.88462 | -53.32724 | 2024-10-26 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bf1f9639-ce57-3a9a-b07c-1e55b73978d9 | -2.8817 | -53.30921 | 2024-10-26 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5c970ab4-f80a-36f3-a572-459cad6c01de | -2.88063 | -53.31638 | 2024-10-26 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| aa7e5a4f-5bc3-31e2-9bc1-ebe9f2d8efd0 | -2.8801 | -53.31993 | 2024-10-26 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 03f90ef1-54a5-36eb-9a58-8dcd0c26236f | -2.87567 | -53.31195 | 2024-10-26 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a9f2a4b-6f1b-3da7-816a-163fd82f0874 | -2.74023 | -53.19868 | 2024-10-26 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b2f59a3-2980-376b-b87c-192f49bafc9d | -2.7344 | -53.19926 | 2024-10-26 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cd046d36-167b-323f-ae04-983174c56556 | -2.73423 | -53.20111 | 2024-10-26 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b3b684f-6d4e-31e5-a0cc-14cee4daf0f5 | -2.73387 | -53.20277 | 2024-10-26 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4553ad8d-a2c2-3e1c-9761-56c68f64bc90 | -2.62352 | -52.44939 | 2024-10-26 05:36:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 09a69d29-7511-3001-855b-7df51f867d7c | -2.62321 | -52.44843 | 2024-10-26 05:36:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f3939ffb-d986-3180-9fa7-3b6444601557 | -2.89618 | -53.32503 | 2024-10-26 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2ffca18f-08fd-3b75-9652-0c1171e199d9 | -2.89566 | -53.32848 | 2024-10-26 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ee7ea5f0-5246-3023-af0f-7b7a9d3b66eb | -2.88962 | -53.33133 | 2024-10-26 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6f330e60-8abe-3e4f-ada2-3d6a49edc813 | -2.88666 | -53.31364 | 2024-10-26 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 683c5455-db33-349c-9508-06516873870a | -2.88614 | -53.3171 | 2024-10-26 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c38767d8-538e-395b-8bfe-25431486f069 | -2.88512 | -53.32391 | 2024-10-26 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c3ca636b-ecf0-3afa-a031-a4923c8dfad8 | -2.88411 | -53.33064 | 2024-10-26 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52d1b8a3-5bb6-3073-9ad7-b68cdad59148 | -2.88116 | -53.31282 | 2024-10-26 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 87617f47-76cc-3f23-b38e-8376cd60db0d | -2.87621 | -53.30835 | 2024-10-26 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8a12138-1a21-3bb8-b9b6-a3d519b8e4f9 | -3.28837 | -53.68349 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f3feb8b-e3f6-3d17-bae2-f9a231a1f41a | -3.28576 | -53.68196 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a088ab41-bf78-3c9f-9e6a-fd7829061ffa | -3.28297 | -53.6827 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f54cd48-9fe7-35c9-b88b-fc7e6cb5c5d1 | -3.98912 | -53.80266 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b359d94a-94f5-37eb-9663-06446f10877f | -3.98861 | -53.80611 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c6e6dee5-c08f-34bf-ab75-44967b394c37 | -3.74219 | -53.40754 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4a3c48d9-5d37-3f19-972a-df6f7141a69f | -3.74166 | -53.41114 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c2cee5c8-5167-36a7-bfa0-4e8124314b4b | -3.84269 | -52.39667 | 2024-10-26 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4bd39a5c-cf69-39c6-8a41-ccb2760fbf05 | -3.84205 | -52.40112 | 2024-10-26 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 98558f4c-8eda-38a7-824b-e2365c5a0632 | -2.09942 | -54.59419 | 2024-10-26 05:36:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 386e936b-7afa-3162-8ae0-e3bc851637bd | -2.09486 | -54.59057 | 2024-10-26 05:36:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91cbdb51-0e63-32dc-acdf-ecab9578b352 | -2.09444 | -54.59341 | 2024-10-26 05:36:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2349940c-310d-30ec-8c3d-282df00e791d | -2.19562 | -53.72976 | 2024-10-26 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea09066a-6c47-3c0c-8ab5-3ce9f1194904 | -2.19085 | -53.72552 | 2024-10-26 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5132545b-5ad9-3af6-8283-727e9ac5cc69 | -2.19035 | -53.72882 | 2024-10-26 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6ab4dcb6-5ded-3013-9174-1744cfe4173c | -3.12232 | -53.70911 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README94.md)
