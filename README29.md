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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ebed0ed-1de0-3cd7-8e60-13048ab3308f | -3.967 | -48.15 | 2024-11-03 04:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 2ee44c9a-4fc3-3aa0-9114-d427b75bb37b | -4.4054 | -43.4746 | 2024-11-03 04:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 9ee05c95-3d3a-3751-8a31-d4f8c8e729c5 | -6.5239 | -41.4929 | 2024-11-03 04:05:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| 08de70a6-1fca-3c1e-aaa3-f0334eccb43c | -6.5241 | -41.4688 | 2024-11-03 04:05:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 62.1 |
| 56e00009-15f8-3ae9-b2db-8a5dae1c26cf | -2.5796 | -53.3927 | 2024-11-03 04:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 7f9b1f61-5ce1-3a72-a9e4-7b75b8fb9fe6 | -2.5797 | -53.3724 | 2024-11-03 04:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| f213e52e-5420-3c21-b4ae-2650ee493995 | -2.7876 | -51.6099 | 2024-11-03 04:15:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 1d6d19fc-12b5-3dbc-95be-0f480cc3725e | -2.7603 | -54.4149 | 2024-11-03 04:15:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 4dd071c0-6853-3ac0-a714-86d83bb289b0 | -2.7419 | -54.4153 | 2024-11-03 04:15:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| e4c4a6c7-dfe9-3c66-98ca-460adf878a71 | -2.7602 | -54.4349 | 2024-11-03 04:15:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| ff4d1478-1a2d-343d-8ed4-da84413122a1 | -2.7419 | -54.4353 | 2024-11-03 04:15:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 8242f35f-f747-3787-b752-d88e2ac18fcf | -3.055 | -54.1474 | 2024-11-03 04:15:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| cc88698b-3a42-3ded-98e8-6e999fe892db | -3.0734 | -54.147 | 2024-11-03 04:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 5ee5a81e-a78f-3d14-bebb-cea17f5503c8 | -3.2415 | -53.3967 | 2024-11-03 04:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 448819f2-37e0-320f-ae6f-1a5b73f22ce7 | -3.1501 | -48.5689 | 2024-11-03 04:15:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 72cd6287-7ca1-3439-9c3e-d8bc493ba5ed | -3.1061 | -50.2686 | 2024-11-03 04:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| a0e400cb-314d-331b-ad7a-e3067ad9441b | -3.106 | -50.2896 | 2024-11-03 04:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 170.4 |
| fcb77d46-b726-3722-834f-b7d0cc7c7870 | -3.1059 | -50.3105 | 2024-11-03 04:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| d4b01430-6f9c-3fe9-89ed-6140f466b998 | -3.0734 | -54.167 | 2024-11-03 04:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 699ff27b-780d-3023-8058-3fa0d89d4f98 | -3.0918 | -54.1465 | 2024-11-03 04:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 3ee7f51b-0faa-3c63-af08-fb713c3b72bc | -3.4749 | -50.3826 | 2024-11-03 04:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 49b7688e-157e-3b95-a7b2-54e8bcda170d | -4.4054 | -43.4746 | 2024-11-03 04:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 4c4119b7-ee74-384d-b1ff-d4e738f372fa | -4.4056 | -43.4514 | 2024-11-03 04:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 0d7a61e3-71f6-3af4-9098-f556f3bcda20 | -6.5239 | -41.4929 | 2024-11-03 04:15:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| bd54b4cb-7c47-3cfc-bdf5-73b4cabf1308 | -15.2117 | -43.2825 | 2024-11-03 04:16:31 | GOES-16 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 82.2 |
| 78a0c7f0-6f6d-31fb-840b-d4fdffaef6f4 | -2.5797 | -53.3724 | 2024-11-03 04:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| f9d6e2ea-c6fd-3841-9982-07f2e1e58591 | -2.7876 | -51.6099 | 2024-11-03 04:25:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 06f20b7c-e605-341b-a456-52e79a32d71d | -2.7603 | -54.4149 | 2024-11-03 04:25:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| c22647e5-8fb1-395d-b2e2-f19eb3c9c176 | -2.7602 | -54.4349 | 2024-11-03 04:25:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| d30588f2-6dd3-3e94-860a-25277f7b8f1f | -2.7419 | -54.4153 | 2024-11-03 04:25:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 18814633-f57e-3ee5-a6a7-d55c9cf23df8 | -2.7419 | -54.4353 | 2024-11-03 04:25:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 8c2457f1-c118-3f3e-9e43-5a2f121128c2 | -3.055 | -54.1474 | 2024-11-03 04:25:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 78f8941e-c4cb-3e71-a498-3842a4076afd | -3.0734 | -54.167 | 2024-11-03 04:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| a35e340d-99bc-3159-b757-988cc817096c | -3.1501 | -48.5689 | 2024-11-03 04:25:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 4463517a-52ff-324a-ad23-914c79be293a | -3.2415 | -53.3967 | 2024-11-03 04:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| ec824335-b335-314e-b9be-231c4831090d | -3.1282 | -54.2459 | 2024-11-03 04:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 173a4818-4ecb-3678-a5b7-31745c2c43dc | -3.1061 | -50.2686 | 2024-11-03 04:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| c5b9846e-7875-3e36-b6bd-32c5a2767705 | -3.106 | -50.2896 | 2024-11-03 04:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 172.7 |
| a6b45896-c0b6-3beb-8f7a-0105ff665f4c | -3.1059 | -50.3105 | 2024-11-03 04:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| b5da667a-a687-3071-9761-8b041b640140 | -3.0918 | -54.1465 | 2024-11-03 04:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 1e7a772b-72df-3361-8f77-d270db93685f | -3.0734 | -54.147 | 2024-11-03 04:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 58b3ce63-4ef6-3b4d-a7f7-e8459b466176 | -4.4056 | -43.4514 | 2024-11-03 04:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 9c3f1c6d-b427-3296-b6e5-3dc1f0bb9c15 | -4.4054 | -43.4746 | 2024-11-03 04:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 71ac8627-6baf-3248-9a52-fb0cb66085b4 | -6.5241 | -41.4688 | 2024-11-03 04:25:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 73.4 |
| d9b877da-d3f0-3a1e-9309-ff55433e2897 | -6.5239 | -41.4929 | 2024-11-03 04:25:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 93.2 |
| 4c6f6e24-4e9f-3e4e-be06-85f2fd27efbf | -15.2117 | -43.2825 | 2024-11-03 04:26:31 | GOES-16 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 78.1 |
| 5dff94c7-3ea9-397a-8e9a-858b8c9a8e73 | -1.2755 | -53.3936 | 2024-11-03 04:35:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 75d499f6-67d8-3d59-8708-430158579b9c | -1.2756 | -53.3734 | 2024-11-03 04:35:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 217a79c1-14ce-3aef-8e4e-d3249cf56309 | -2.5796 | -53.3927 | 2024-11-03 04:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 83d343b5-e42d-3111-84d8-cd918028d7aa | -2.5797 | -53.3724 | 2024-11-03 04:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 697d6a1e-d19a-3492-a78d-a6a5f2ca5f29 | -2.7876 | -51.6099 | 2024-11-03 04:35:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 8a6ff58a-98d9-304e-a718-034fb1cb74af | -2.7419 | -54.4353 | 2024-11-03 04:35:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 5bfbe3eb-27d5-3869-b73f-79f8eb407508 | -2.7419 | -54.4153 | 2024-11-03 04:35:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| e9a6582f-470a-3d50-bfff-7c4e20d5f04d | -2.7602 | -54.4349 | 2024-11-03 04:35:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| d93ba5c4-bd47-331b-a6c4-4a80355b4888 | -3.055 | -54.1675 | 2024-11-03 04:35:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 49598d46-6751-38fc-9b3a-f8e9adda37c5 | -3.055 | -54.1474 | 2024-11-03 04:35:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 3a411b06-8705-3c9c-91fd-1931481fd9bd | -3.0734 | -54.167 | 2024-11-03 04:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 9fe3c7b6-e52b-3bc1-995a-4df2a4a95dce | -3.0734 | -54.147 | 2024-11-03 04:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 1a580623-1dcc-3ce2-a86c-2b5821316441 | -3.1059 | -50.3105 | 2024-11-03 04:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 93004a2b-4811-3704-a9d3-d4d9b970bffb | -3.106 | -50.2896 | 2024-11-03 04:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 175.3 |
| 28f9eb69-8032-3de8-9481-76433d8eaedb | -3.1061 | -50.2686 | 2024-11-03 04:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 159379dc-2346-3cc7-af17-2a51130c3387 | -3.1245 | -50.289 | 2024-11-03 04:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| d9fcce65-fea0-34c2-a134-9c4c355c1623 | -3.1501 | -48.5689 | 2024-11-03 04:35:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 1f2477ac-fe27-3193-82c5-1281047ef6dc | -3.2415 | -53.3967 | 2024-11-03 04:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 4e6c93ee-483d-39fb-ba7b-700f5466fa42 | -3.4749 | -50.3826 | 2024-11-03 04:35:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 04775cbb-3b8c-3871-aae4-af2d50b78771 | -4.4054 | -43.4746 | 2024-11-03 04:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 4e6345da-0be1-35bb-ba61-bd6741b03436 | -6.5239 | -41.4929 | 2024-11-03 04:35:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 101.0 |
| 01e7c466-c7c1-3697-865c-d54b411d6067 | -6.5241 | -41.4688 | 2024-11-03 04:35:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 63.3 |
| b6aeaea2-46e4-3117-95b8-4e12c073553e | -15.2117 | -43.2825 | 2024-11-03 04:36:31 | GOES-16 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 73.6 |
| 3f4e295c-3302-33da-b525-d8effdcb85f4 | -0.63457 | -47.67918 | 2024-11-03 04:44:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6bc49141-9470-34af-8320-be57f4229a08 | -0.63398 | -47.68291 | 2024-11-03 04:44:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 838c9a3c-f135-3630-95be-34ceaa4475ce | -1.65855 | -47.3703 | 2024-11-03 04:44:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26e77de9-6fef-3434-a075-1913893b965b | -1.48674 | -47.21946 | 2024-11-03 04:44:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3250b879-3d72-3b43-a899-ee11c9a8498e | -1.48667 | -47.21666 | 2024-11-03 04:44:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8db69854-1072-3989-a2ff-56e663975db5 | -1.48605 | -47.22062 | 2024-11-03 04:44:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec56f9ac-b1d8-32c8-95ac-5083edc7b5a8 | -1.48542 | -47.22459 | 2024-11-03 04:44:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1fb2f962-9f37-3bec-9151-441ece7a9961 | -2.03953 | -48.01091 | 2024-11-03 04:44:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74a350aa-3af0-3fcb-bfc3-fc2822e55017 | -2.03553 | -48.01412 | 2024-11-03 04:44:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80377f0f-258e-36eb-8808-d8eeef021793 | -1.99424 | -48.28329 | 2024-11-03 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93322516-55f8-34ad-a700-42d6012d70b5 | -1.99061 | -48.12169 | 2024-11-03 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b8c06ead-846a-3da7-a228-71c37aef5ccc | -1.99003 | -48.12538 | 2024-11-03 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0c02e19e-4e02-349e-9e27-b98ec1b6e3ed | -1.98661 | -48.12487 | 2024-11-03 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 85aba12b-f3ee-3d5b-8b05-bbe3b60e9fa4 | -1.96461 | -47.95037 | 2024-11-03 04:44:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bb838b0-3795-33c3-ac84-b12f1e9cbfcd | -1.96404 | -47.95411 | 2024-11-03 04:44:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64b91f92-7caa-3b2c-9b64-1e1866008021 | -1.77908 | -47.83433 | 2024-11-03 04:44:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33b5e9e2-f44b-372d-adad-e03d38ead44c | -1.7785 | -47.83811 | 2024-11-03 04:44:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45df9b60-4e08-3720-a0ef-f3393d26fdea | -1.77505 | -47.83758 | 2024-11-03 04:44:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e19d2fb-a96e-36a7-9713-61dc910305e9 | -1.61844 | -48.5145 | 2024-11-03 04:44:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50900153-79b7-31d7-a958-516c1e1c62ea | -1.54463 | -47.73808 | 2024-11-03 04:44:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a61554c-6d17-3bd8-8245-d25a4a17473d | -1.54405 | -47.74187 | 2024-11-03 04:44:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb887cfd-970a-3212-9e37-e87ca4652975 | -1.28052 | -48.13071 | 2024-11-03 04:44:00 | NOAA-21 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8ee1a0f-8872-30e0-9d62-e518fcc410ce | -1.27713 | -48.13019 | 2024-11-03 04:44:00 | NOAA-21 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a393b3ab-1bb3-352d-9f85-a0c86684b152 | -1.13167 | -48.36718 | 2024-11-03 04:44:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3d4cf7f-f342-30be-99e8-58a1720081fc | -1.13111 | -48.37076 | 2024-11-03 04:44:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 077f3a54-47a9-31ef-b478-d21cca9c79e7 | -1.13056 | -48.37434 | 2024-11-03 04:44:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c8a6908-1f8c-3faf-a368-27cf16e9d727 | -1.12945 | -48.3815 | 2024-11-03 04:44:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a7597b6-8d88-30a6-9d19-27dad11d5886 | -1.12889 | -48.38508 | 2024-11-03 04:44:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4e24e07-69c1-3f79-aae0-47701093a6f3 | -1.1283 | -48.36666 | 2024-11-03 04:44:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca7f22a1-6725-374d-a5c9-6c1ba1695a01 | -1.05415 | -47.91613 | 2024-11-03 04:44:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 3ec6449d-a07b-3bfb-8416-8ca46bda0775 | -1.05359 | -47.91982 | 2024-11-03 04:44:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |


[Clique aqui para ver as próximas entradas](README30.md)
