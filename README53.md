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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58f91b84-aad2-33c9-bc63-7382e20a9116 | -2.29053 | -51.2766 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23402eaf-de90-324c-b750-5efa554d2a54 | -2.27979 | -51.13043 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6f1be28-e170-348d-9990-539d19f0a874 | -2.2787 | -51.13744 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 410e5e9d-dbfd-3be6-9494-6d4fa8438207 | -2.27761 | -51.14445 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4de27698-ff76-34bd-961b-b18e9e0b18f1 | -2.26229 | -51.24276 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27797652-ee91-3256-9c1e-558b3f5cd17d | -2.24204 | -51.13179 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8113943a-7d00-3c7a-b538-0be9a24696e1 | -2.23871 | -51.13128 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9a15dd14-a3e0-388f-91b8-51ae2ec7962d | -2.2305 | -50.9015 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02a5396b-1465-339f-9c51-8236cc615612 | -2.23004 | -50.81621 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a1c25221-79f5-3de8-b1ff-41c06cc239e4 | -2.22441 | -50.89701 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1cc4d9eb-b48e-39d2-8ca9-802b7e974659 | -2.22387 | -50.90048 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18719236-088d-3f87-ab0f-5bf77f6cad57 | -2.2187 | -50.88904 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c49e724-9067-3196-ac71-297bdaa0c05b | -2.21538 | -50.88853 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe8fd8bd-c88f-395f-bebe-d70a6c6d076c | -2.17213 | -51.49004 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2e611195-b519-34fd-9455-f75ed611573e | -2.8867 | -51.74807 | 2024-11-03 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cec9ede2-d789-3cb6-af15-e498e59b11dc | -2.88333 | -51.74754 | 2024-11-03 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 515b90b9-a182-3ea8-8ab4-a98f2c068882 | -2.8317 | -51.80151 | 2024-11-03 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce7376f6-8d1c-35db-94f3-2d5c228b9cd1 | -2.83113 | -51.80512 | 2024-11-03 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32978186-a91e-3410-91c8-dbc37a3add19 | -2.83057 | -51.80872 | 2024-11-03 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fd3481f-c0d7-3757-b2bd-2ad6f7b92439 | -2.80415 | -51.75668 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45b433ff-125b-3b7c-b754-8535e1fa6da1 | -2.80134 | -51.75256 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6aec1dea-276e-3aa4-ae68-7de71ef617e1 | -2.74515 | -51.73656 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1becd34-d23a-3256-97d3-a4f49c718c64 | -2.74178 | -51.73603 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf7f49bc-b9a4-33b5-ab08-b47295cd4610 | -2.74121 | -51.73961 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8479906b-eb70-3994-8a4e-ed3a05f67375 | -2.74064 | -51.7432 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f248829-4e35-391f-9ceb-156548a57201 | -2.73995 | -51.73594 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5ebc663-2b83-313c-bd07-98bea262d207 | -2.73939 | -51.73954 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae21fba7-031b-3a78-a894-d4cefff56d23 | -2.73883 | -51.74313 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81e19d43-f945-3fea-aa82-51d9ed42da18 | -2.73658 | -51.73542 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5376b3c5-75a2-3727-bb4c-6551f09d780e | -2.73602 | -51.73901 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34218414-46ef-3b78-a58e-ae829506b6ee | -2.73546 | -51.74261 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65e7b891-f082-3474-a809-4016609c5137 | -2.73473 | -51.84573 | 2024-11-03 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d969e66-c950-35d9-a81d-9d9bfa26f1b7 | -2.73376 | -51.73131 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34774b02-9bc5-336f-9042-27af0d1d6504 | -2.7332 | -51.73489 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97803142-7e69-367d-9cf3-7577fafeb13f | -2.73039 | -51.73079 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b9c18cf-dd88-3ebf-86f1-3d1c11aedc4b | -2.72645 | -51.71182 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a77d45a9-97c3-3f3a-8edf-1a45d3623fa1 | -2.72364 | -51.70771 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35d87f53-b497-3426-9c6a-31112859e898 | -2.72308 | -51.7113 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34dba655-1a8a-3bb2-9c44-b9589a08a90c | -2.70101 | -51.96376 | 2024-11-03 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5f64f912-58e8-39df-9776-c4ec520b2add | -2.65003 | -51.71474 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 168d0b02-d668-34fa-a46b-4b836151fd30 | -2.64946 | -51.71833 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca5b7dbe-8124-3b71-a705-a6f9e138cb44 | -2.64889 | -51.72192 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81f24021-6cd6-3896-a8d2-b5260d9f8676 | -2.64609 | -51.71781 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a3e2b0c-df7c-3825-9c96-5ea40a941ff6 | -2.63426 | -51.72702 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14cd3acd-4302-3540-8a25-9e07fcab0a14 | -2.62074 | -51.92136 | 2024-11-03 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9f4de40-2cc8-3c00-b31d-c4dd9ee56c45 | -2.60896 | -51.76753 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 43a953d7-4cb4-3f53-971c-8eccbb035deb | -2.60559 | -51.76701 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6e53973-4d59-33e6-95e2-b63fd4032a4e | -2.58461 | -51.92348 | 2024-11-03 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e83cb413-07c6-3dc3-9d20-cd740e825a88 | -2.58297 | -51.8673 | 2024-11-03 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4f595b9-af5c-365b-81a2-ebe411db1d7b | -2.58121 | -51.92297 | 2024-11-03 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ff77f878-1750-3d35-9150-c2cc1a75a9af | -3.37569 | -50.95362 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6baf426b-d4be-35bd-a079-3e09594d0136 | -3.28313 | -50.91397 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 316d0e5f-d4fc-3dd6-a20c-b8d66b095a84 | -3.15174 | -51.14555 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28aa6926-96d4-30d2-b487-f688ecf03aaa | -3.024 | -51.37289 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eec48473-1dbe-34b5-a2ef-ee3ca10f54bb | -2.96778 | -51.42911 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a8eacac-9684-34b1-94dc-dde0a42e6d6d | -2.91096 | -51.46372 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 590eae53-e988-379a-9dbb-8f496db08133 | -2.9104 | -51.46724 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1c5a8875-642c-3869-9389-19284561efdf | -2.90761 | -51.46321 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 72bcc4dd-c5e9-3f3c-8099-d0ce25aa12d3 | -2.90705 | -51.46673 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 24c59c39-0476-335e-b386-61dac7b22bf4 | -2.90371 | -51.46622 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8c105d6-5471-34a4-a419-49848266a514 | -2.90315 | -51.46974 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f233817c-a579-3354-8cd4-1228b8003d08 | -2.90036 | -51.4657 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02445bf3-bf64-3998-9d5f-384a29648cae | -2.89981 | -51.46923 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52db5722-d954-31a6-ba91-8c72dbc41ee0 | -2.80421 | -51.60281 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ebc63b9-e161-3fac-8ba5-99d5d7a82038 | -2.80365 | -51.60637 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 648d760d-cb2d-33a9-b680-fafb8d0225a6 | -2.80141 | -51.59874 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d08d21e-8db3-3969-8df5-d4cf7af5c0b8 | -2.80086 | -51.60229 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ad38f17-c348-3765-a45a-d2a48f196a5d | -2.80029 | -51.60585 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8cf5d46-c1d4-3cff-9ebb-357df0e3b5e2 | -2.79973 | -51.60941 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a42f568a-f1b9-3994-b0ba-60d876ab04ee | -2.79806 | -51.59821 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47ec2c0a-006b-379a-a9c3-0483c8a978d6 | -2.7975 | -51.60177 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5fcfc24b-2dc8-34d8-ba11-b9fdfea2e0c6 | -2.79694 | -51.60533 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7233370-0601-3654-8e83-3a382e51e8aa | -2.79637 | -51.6089 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb5f396f-d2c4-3fe2-9cec-305a53e8ce95 | -2.79581 | -51.61246 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3fd2cdb7-fcf6-3878-9671-5bb151658c18 | -2.7947 | -51.59769 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fb9a1de8-99be-3904-a200-eff3d710ce4a | -2.79414 | -51.60125 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| bb2828c7-318b-3926-86ab-fbd25e7b0d6f | -2.79358 | -51.60482 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b8d48609-f340-32a7-846d-90ef46172a4e | -2.79301 | -51.60838 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9367fd84-19bb-3791-b8f7-4a51775ee2e3 | -2.79245 | -51.61194 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 63c10007-174b-3158-9c3c-f65a46afbc5d | -2.79078 | -51.60073 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b0adbba2-f342-3f7a-b512-c9f641911154 | -2.79022 | -51.6043 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 80eb0b4d-42f7-3d54-abf1-cae451f0452e | -2.78965 | -51.60786 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a404c4fb-7c0a-3ae7-afe4-70afc028a540 | -2.78909 | -51.61142 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d573526b-a167-3e45-945c-e0ac1bcdd54a | -2.78742 | -51.60022 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d8677da4-85a7-3ac7-828c-5adb2b1de5d8 | -2.78686 | -51.60379 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0eb23987-6c27-33a7-8092-cdd0efb3d0dd | -2.78629 | -51.60735 | 2024-11-03 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8ed40f71-0c55-3141-b8fb-b6c72b1c3ffb | -3.84786 | -51.8676 | 2024-11-03 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f623634-8347-38b4-8ea1-b4eb84598441 | -3.8473 | -51.87117 | 2024-11-03 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebd49a02-db97-3b5d-a1d0-4906d04261c1 | -3.8445 | -51.86708 | 2024-11-03 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c492bd1-509f-31b1-8eb6-133826415b69 | -3.84328 | -51.94025 | 2024-11-03 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c5db457d-2a82-32f5-9a20-9fa774e8e15f | -3.82482 | -51.69295 | 2024-11-03 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e34aa47c-e0fb-3e92-a6a5-a1b8803768b5 | -3.79985 | -52.19284 | 2024-11-03 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 899c7dac-bfdf-3e5b-9e46-9caac93724b3 | -3.79464 | -52.22572 | 2024-11-03 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07394c25-beaf-3474-aa1a-658f3d16fce8 | -3.75845 | -51.61385 | 2024-11-03 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 320adc5b-7f04-3ba2-9375-f6689e50aa66 | -3.70468 | -52.01849 | 2024-11-03 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 012005c4-0d05-3e77-a27c-fe823282166a | -3.63976 | -51.78446 | 2024-11-03 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0626279c-284b-33ed-bb54-117a61b421ae | -3.53175 | -52.17455 | 2024-11-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 54985644-a353-349c-a558-034cddbd8077 | -3.52835 | -52.174 | 2024-11-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0c1813b2-c869-3148-8d83-da10ce3880f8 | -4.1696 | -50.90154 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7507e9d5-cdd4-30d4-936f-dbbdcbc2688e | -4.12836 | -51.07879 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README54.md)
