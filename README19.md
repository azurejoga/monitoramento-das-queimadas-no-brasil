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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34dfd0f4-d859-388d-8094-2a1897255b51 | -4.57787 | -43.33924 | 2025-11-06 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 23e9ee9f-33fa-31cf-96f3-b59d04af93b9 | -3.03942 | -51.13118 | 2025-11-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cec67bf5-e6f6-36df-8de1-9e4a6aedf723 | -3.93204 | -40.92957 | 2025-11-06 04:44:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7f280b99-9816-3185-9e3b-db0be31bb2f5 | -3.50047 | -49.55729 | 2025-11-06 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75f3b3a0-54a9-35fb-8151-8f22b83847c0 | -3.77678 | -51.67525 | 2025-11-06 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 33482ed5-e435-3969-9629-2616850835cc | -4.04507 | -46.99247 | 2025-11-06 04:44:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e835572f-c1b4-3f34-b094-c2270343ca4f | -1.63508 | -55.17101 | 2025-11-06 04:44:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1defbecc-1b02-3729-ae61-f79cebb4aeb7 | -3.92313 | -47.70013 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 54fe6c4a-93de-380e-b67a-3bf539dad35f | -1.62336 | -54.71231 | 2025-11-06 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9800a8a4-a892-3836-bcbb-502533b73bdd | -3.41135 | -50.84346 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe0f408d-8d0a-33fc-a26f-f2ccd51dc579 | -3.77957 | -51.67935 | 2025-11-06 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4c2e4442-8cad-31f2-a1d6-f050ab479b94 | 0.44997 | -60.48736 | 2025-11-06 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a026d3e7-0049-3d9a-931a-ecb16a1e9e84 | -4.49202 | -45.92424 | 2025-11-06 04:44:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 750e1bdf-3aa6-3d59-b725-f9f92a1650c6 | -3.58455 | -55.5061 | 2025-11-06 04:44:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3793e83b-726c-3835-a3fd-99f4a6f209c8 | -3.78235 | -49.43079 | 2025-11-06 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 04e35492-10be-3e73-b1f1-e4561d9a4244 | -4.38842 | -49.77769 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75c8a58b-8f0e-32b8-94a2-1c158eae1b8a | -3.69692 | -49.56349 | 2025-11-06 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7f27ef55-dda4-325c-b8c5-806a2ee3cbe0 | -5.52805 | -46.50087 | 2025-11-06 04:44:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 878ba253-0d46-39e4-82c3-8a0aab2135fe | -6.07195 | -43.25726 | 2025-11-06 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| eee6831e-b5b4-3db1-8f7f-754fc6e7eb65 | -6.12071 | -41.62616 | 2025-11-06 04:44:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 65e1b00b-1993-3706-8e13-244cd72b7e3a | -5.15252 | -41.27557 | 2025-11-06 04:44:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 04f6eacb-79e4-3632-be3f-a5a42634d9df | -3.41688 | -52.76806 | 2025-11-06 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 207aff1b-98e8-362d-b917-2e698a3d4586 | -3.33396 | -52.09433 | 2025-11-06 04:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 09fc2271-c329-38e1-8a41-9b0e77f0058b | -4.58006 | -43.33189 | 2025-11-06 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5ce9dc12-17f0-3f89-81c0-7afc05afbeae | -3.77478 | -51.81841 | 2025-11-06 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba1a417a-c02b-3064-b5b8-76739bff47e5 | -3.45026 | -51.58731 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3a5e592-40d1-3be5-8da0-1059f04b5baa | -3.79846 | -51.38768 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0cf398e4-8d7e-33cd-9de5-e0c5d679c8a3 | -4.714 | -50.82652 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b403e6b5-3294-3e8a-b8c3-1aa8b4385a5e | -3.92949 | -47.68885 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2387baeb-010f-38ab-ab73-e4f40e53b073 | -2.98764 | -52.82073 | 2025-11-06 04:44:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 1e161bc2-1949-35c0-94cc-067082e3e204 | -4.57933 | -43.33671 | 2025-11-06 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 122e2188-6b6f-39e5-93f5-8dd5b33a0525 | -4.5825 | -43.33999 | 2025-11-06 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 986a8cf9-0b08-3252-b6e0-bdbbbcb408cf | -3.90255 | -42.55157 | 2025-11-06 04:44:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 753b8308-6620-3449-a9b8-e541ffed3753 | -2.62292 | -49.22942 | 2025-11-06 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48f2f6a7-c8b4-3440-b0bb-c3b5b7f27975 | -3.475 | -53.20275 | 2025-11-06 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd58734b-9ea5-38f3-854d-387c3c054e8f | -4.87642 | -56.09346 | 2025-11-06 04:44:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49186d58-d862-3306-b394-7de1b8cafe73 | -1.63053 | -53.72118 | 2025-11-06 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b132ac7-b07f-3045-a5e9-0bfdcd7fc787 | -3.9254 | -47.69221 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7dd1b5a8-c395-3bb8-bd37-10b145aa21d3 | 0.44387 | -60.48835 | 2025-11-06 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 74e2b981-bbf9-3b70-bf59-fba5a1aa4440 | -4.63896 | -42.18045 | 2025-11-06 04:44:00 | NOAA-21 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0d1c608c-1894-388f-b119-bcefefb558ca | -3.518 | -51.66024 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0d8650c-78ca-3863-8bdd-27a520e29a26 | -3.92599 | -47.68831 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7067422e-8eef-3468-ab2c-22146257f2cd | -2.98347 | -52.8242 | 2025-11-06 04:44:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 86ba2bf7-8449-36a2-a233-cf15e72f386f | -3.92784 | -47.69292 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8ac5c6f5-42bc-30da-9e95-d7830c17553c | -3.60038 | -51.3707 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c99fa59-cc30-3ac2-9c89-022ce302e0a1 | -3.70854 | -50.87981 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a866a876-9864-3771-98f9-3e3d034a15cc | -6.12025 | -41.6295 | 2025-11-06 04:44:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c784f7ea-d19d-3871-907b-d0401a68dd0e | -4.14726 | -50.68799 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c64e29f2-9b82-3a47-8a63-742faeefd2bf | -5.15539 | -41.25542 | 2025-11-06 04:44:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f20ab96f-02b5-3d8d-b603-fc2a918bfd61 | -2.21546 | -51.08881 | 2025-11-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec0f5e36-9b55-33bf-b236-cda3869d9ddb | -3.59316 | -49.44386 | 2025-11-06 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0ef3f38c-8746-36d5-a3a2-d45ea47bc60a | -3.70523 | -50.87929 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f06b498-f954-352b-ad68-948e4ededcba | -3.47877 | -49.91728 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e00952ae-5943-33b3-a471-18730e9068a5 | -1.64276 | -55.17601 | 2025-11-06 04:44:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bb373fe-23ae-3346-a7d6-17248e848bb6 | -3.47404 | -53.23203 | 2025-11-06 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec64399b-f522-33c3-b763-120cc5d92929 | -3.58045 | -55.50549 | 2025-11-06 04:44:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d95e520f-4e27-3540-9628-c8c5b9d8ad47 | -3.42039 | -52.76859 | 2025-11-06 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2de60f45-0b7e-3e83-9500-1d373dad0a97 | -5.52737 | -46.5055 | 2025-11-06 04:44:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9f5ae154-db3c-3441-af67-9e3bc8a965c7 | -4.7154 | -47.23624 | 2025-11-06 04:44:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3f7beaa-507d-3896-9106-8676cc7bba22 | -2.96328 | -49.53313 | 2025-11-06 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61b95002-380d-3792-9efd-bd1a40a13421 | -3.58865 | -55.50673 | 2025-11-06 04:44:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ee4556a-077b-3b88-ac4e-a588804d39cf | -3.58804 | -55.51041 | 2025-11-06 04:44:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4a1acaff-3068-3bcf-b9dd-903a3ed6d852 | -2.98387 | -51.35373 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1d06b4e2-9d46-348a-b65e-394739601604 | -3.88615 | -49.11341 | 2025-11-06 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce15e9af-0a96-3e68-806b-d6269b1dd1c1 | -2.92976 | -51.30545 | 2025-11-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2160c34a-265a-3d78-90f0-5f40c62934c8 | -5.9483 | -44.2655 | 2025-11-06 04:44:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea4c6595-1bbe-3bb4-80e3-1c920f6cc8f3 | -2.7907 | -50.31141 | 2025-11-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f50e7b8-021c-30bc-85f9-e26716d2f952 | -5.75893 | -40.81384 | 2025-11-06 04:44:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 52d4b695-76ab-31da-b152-dd9885fd9269 | -3.47383 | -43.64257 | 2025-11-06 04:44:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 959ef92b-0a66-3e5e-bc7a-5ea6952000d3 | -3.8985 | -42.5455 | 2025-11-06 04:44:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 04933e15-ee80-378e-b4d7-d327aad5773c | -4.40715 | -50.37662 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0745c913-899c-3c8b-9c3f-46f4b77ddb52 | -4.6054 | -50.9969 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21447ff4-e5d5-3b3e-8a08-c2a14d583968 | -2.89376 | -49.78299 | 2025-11-06 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aecc3921-6bc7-321a-a4ca-1f1ed5b7cd09 | -5.76838 | -40.82795 | 2025-11-06 04:44:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 71ab3139-8859-3902-8861-014bf69bf39e | 0.44852 | -60.47823 | 2025-11-06 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0e8ae34a-069f-3e65-95d8-79fdc96c26e8 | -3.82882 | -49.81015 | 2025-11-06 04:44:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e22a20f7-e8bc-3185-be00-3af27f9f6ba7 | -4.75076 | -50.61378 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d0a3357-7cb7-32cb-84d7-2a711b045467 | -4.36079 | -50.88733 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4db36e1f-9c48-3b11-9baf-ee3ede5f8e9b | -4.21045 | -48.40281 | 2025-11-06 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 555467b1-b1d9-36b5-a520-36af6420c526 | -5.15051 | -41.25101 | 2025-11-06 04:44:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3e3c1446-7ed7-3658-873b-87c10287078f | -6.20217 | -43.27385 | 2025-11-06 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1a02c963-ff32-3fe2-939e-6839a3d5280f | -1.63781 | -54.0634 | 2025-11-06 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f4f9897-3a01-36d0-8993-56e7db0e12ec | -3.95953 | -53.5069 | 2025-11-06 04:44:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e924c19f-8947-3277-8703-049919a34e78 | -2.89728 | -50.47652 | 2025-11-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b432726b-16b2-31b0-a9a9-b257d7963c66 | -2.794 | -50.31192 | 2025-11-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95575918-cccc-3c59-94cf-59933d8683cd | -3.70267 | -49.89981 | 2025-11-06 04:44:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82a74b7a-d2ea-3367-8788-8e04d7eb8585 | -1.42063 | -52.91373 | 2025-11-06 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5395123d-f922-3246-b883-f639761133e5 | -4.4706 | -49.42332 | 2025-11-06 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00a7193c-bfeb-3e68-a017-0e9daaf4a931 | 0.44315 | -60.48376 | 2025-11-06 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 29b73a96-95cd-379e-88cd-dbefdd560b72 | -3.40526 | -50.83898 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d525e10-7e58-315e-9fb9-2f5f7686639a | -5.56624 | -45.09377 | 2025-11-06 04:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9295629-fc73-3e5a-8d01-1b45a2930f43 | -4.57856 | -43.33438 | 2025-11-06 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 73aa71ed-945b-3eed-82de-6c7e72ce9bcd | -4.9262 | -42.88453 | 2025-11-06 04:44:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 966b1255-6778-3a58-96cb-85bca70cd7af | -3.61421 | -52.12245 | 2025-11-06 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7d5c102-174a-34f7-9e86-f0c8b4dda859 | -3.69638 | -49.56696 | 2025-11-06 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00a09978-ce38-334c-b563-6ca529ca71bb | -3.58729 | -55.41341 | 2025-11-06 04:44:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86187f30-e1e5-3171-94ea-7d5db0766ec6 | -5.8831 | -45.34681 | 2025-11-06 04:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25101910-1e5a-39a5-8e1f-d0d69433c9da | -4.18457 | -52.09048 | 2025-11-06 04:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79f5201d-44a2-36d0-8cbc-461f1f420b4f | -3.98475 | -47.29694 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb39e53d-0c61-3db1-9bc5-42a9f57499fa | -6.26764 | -43.68163 | 2025-11-06 04:44:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README20.md)
