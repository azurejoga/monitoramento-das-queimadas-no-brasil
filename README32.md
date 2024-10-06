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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e76ffb7-7ed2-307c-bf77-317393e0f205 | -9.3633 | -64.325798 | 2024-10-06 01:43:26 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| deaa0fdb-8e1a-3035-a94c-353c898fce64 | -10.0528 | -68.355698 | 2024-10-06 01:43:29 | METOP-C | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 63296430-8856-30c6-893f-e695316bb168 | -8.2142 | -61.194302 | 2024-10-06 01:43:33 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 896607b0-630a-3b09-961c-e8ffe8322e25 | -8.2158 | -61.201302 | 2024-10-06 01:43:33 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4a19dfe2-7385-3d24-a75f-fdb87879c447 | -8.2174 | -61.208302 | 2024-10-06 01:43:33 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ac55e53c-3cca-30c9-9032-ca517676ad77 | -8.2044 | -61.196602 | 2024-10-06 01:43:33 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a92c7568-7fb5-3851-a946-8fe837fc0627 | -8.206 | -61.203602 | 2024-10-06 01:43:33 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 98ea0c53-31d1-31d6-9a63-82a7c7d14e45 | -8.1487 | -61.268101 | 2024-10-06 01:43:34 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 73e0fa99-1011-35ca-9bec-cb064f790a95 | -7.9719 | -61.3964 | 2024-10-06 01:43:38 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 786813d2-be2d-338c-a355-46b96f03d799 | -7.9218 | -61.2686 | 2024-10-06 01:43:38 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ad67d6da-6f18-3013-b56e-276f484d4475 | -8.3173 | -64.012497 | 2024-10-06 01:43:42 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e5d61591-b053-3088-a2b5-236bbf287a67 | -8.319 | -64.019897 | 2024-10-06 01:43:42 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ad034a5-ec23-336a-b0b7-586349eda6b6 | -7.15 | -59.285 | 2024-10-06 01:43:43 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9ef8fcf2-44fa-3400-ab1d-bbe6b3c210c1 | -7.1519 | -59.293201 | 2024-10-06 01:43:43 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 20f96fa1-4f1d-31aa-b3de-56c7136ae82d | -7.1402 | -59.2873 | 2024-10-06 01:43:43 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 761f087f-2016-37e2-a0c0-ed4861f9ebeb | -7.1421 | -59.295502 | 2024-10-06 01:43:43 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 785a69de-bdfe-36ca-b785-c74e12a27f82 | -7.1495 | -59.370602 | 2024-10-06 01:43:43 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a0f2e817-584e-3278-ae3c-b0692ce837a3 | -7.1514 | -59.3787 | 2024-10-06 01:43:43 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a70502eb-3be0-3668-b60d-e3f357d8336d | -6.9605 | -59.050301 | 2024-10-06 01:43:45 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ed997463-8828-3fae-a899-f2cda3d05f63 | -6.9624 | -59.058701 | 2024-10-06 01:43:45 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 571f8d95-3263-3a56-85a4-e8f1c6920037 | -6.9487 | -59.044201 | 2024-10-06 01:43:45 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 61888df3-202e-3394-88ee-a5a0a3ad27ec | -6.9507 | -59.052601 | 2024-10-06 01:43:45 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 71145fd8-a921-31c2-b599-dcd8b11d7dd1 | -6.9526 | -59.061001 | 2024-10-06 01:43:45 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 701adecb-b86e-3144-bac7-eb0a373da424 | -6.9546 | -59.069302 | 2024-10-06 01:43:45 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bb98d45e-4e63-394c-973a-67af86a824ea | -7.0302 | -59.389999 | 2024-10-06 01:43:45 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c77f10e9-3dd4-3e21-bdda-2dbabd4235d4 | -7.0321 | -59.398102 | 2024-10-06 01:43:45 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| da169006-4ede-3ea9-99ca-f5ec8d35cce6 | -6.9409 | -59.054798 | 2024-10-06 01:43:45 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8fd27a39-92ca-3fc0-9181-62f683a109c3 | -7.0109 | -59.3517 | 2024-10-06 01:43:45 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0ff05e3a-049e-3d9c-a17f-2d731d8285d5 | -7.0204 | -59.3922 | 2024-10-06 01:43:45 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ef3a0b28-f5b9-35d2-88f6-76916d903393 | -7.0223 | -59.400299 | 2024-10-06 01:43:45 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ec852c1-21bf-3338-85a6-0644275f6b5a | -7.0107 | -59.394501 | 2024-10-06 01:43:46 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d2ac8308-db49-3a4d-a4b1-13171958d2ea | -6.9933 | -59.364399 | 2024-10-06 01:43:46 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 40ceee25-4057-38b5-82c2-3ccdd2565778 | -6.9952 | -59.372501 | 2024-10-06 01:43:46 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6b3efae1-94ee-3614-abe1-826618e5cb61 | -6.9971 | -59.3806 | 2024-10-06 01:43:46 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9c6e3a88-7dff-3dbe-b228-ad8af303c517 | -7.2709 | -61.084999 | 2024-10-06 01:43:48 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b88a0e56-ece1-3cba-ab06-3525af463c50 | -7.2725 | -61.092098 | 2024-10-06 01:43:48 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4cb0c6bd-760d-3c6a-881a-03db5250bcaa | -6.7178 | -59.071602 | 2024-10-06 01:43:49 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 91ca4f95-f221-3895-87e7-08ad13f46e7e | -6.7818 | -60.0909 | 2024-10-06 01:43:52 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 419201ca-942a-3978-9ebb-83824bafc656 | -6.7836 | -60.098499 | 2024-10-06 01:43:52 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ce5b0f2-f910-344c-bfc1-be5bc526707c | -6.7853 | -60.106098 | 2024-10-06 01:43:52 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9be00b07-625e-3f1b-b566-1f2917d40d98 | -6.772 | -60.093201 | 2024-10-06 01:43:52 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ec056d76-4b26-3755-a612-c7ccb2a6d866 | -6.7738 | -60.1008 | 2024-10-06 01:43:52 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 66c0943a-1926-33e2-b979-ff359d6bfa7a | -7.3712 | -64.6576 | 2024-10-06 01:43:59 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 318c07cb-0230-3072-9cc8-bb9765e21596 | -7.3729 | -64.665298 | 2024-10-06 01:43:59 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 314552a8-60ee-3c8e-929c-ad5a35d30061 | -6.811 | -64.314102 | 2024-10-06 01:44:07 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c3c9c249-0f5f-3ffa-b9b6-2bf86e8d0cb7 | -6.4403 | -62.8577 | 2024-10-06 01:44:08 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0129d9d3-cfd4-34da-9cf9-c30564139f0a | -4.2765 | -60.009102 | 2024-10-06 01:44:32 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8e651246-5ac5-3389-9847-4f250bf990df | -4.2783 | -60.017101 | 2024-10-06 01:44:32 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f4aa1cc7-1beb-3279-854c-df07f3b45945 | -2.5955 | -54.521099 | 2024-10-06 01:44:38 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3682fd7-b86f-3810-a278-aec95b2d2f38 | -2.6 | -54.539902 | 2024-10-06 01:44:38 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 028bd64c-05cc-37c3-a682-5aada82ea028 | -1.7668 | -47.1984 | 2024-10-06 01:45:16 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 3cb706d2-0f86-3e50-851d-ac06ebe4a0bd | -2.6858 | -49.0752 | 2024-10-06 01:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 42d21cb5-a8d9-367a-92d9-804363400f50 | -2.6859 | -49.0539 | 2024-10-06 01:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| dc165b70-a494-3533-a147-5ea809fa9cc9 | -2.7981 | -48.6873 | 2024-10-06 01:45:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 89dea235-9277-3f21-8c4c-65dbd0d079a6 | -2.8165 | -48.7082 | 2024-10-06 01:45:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 3c797742-7987-3d1f-a86c-53ada917e795 | -2.8166 | -48.6867 | 2024-10-06 01:45:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 196.7 |
| 2170d247-384d-37c2-aa72-42f598dee897 | -2.8167 | -48.6653 | 2024-10-06 01:45:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 25980cc6-1a6f-3214-90c0-87fd769c8019 | -2.8169 | -48.601 | 2024-10-06 01:45:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 00309030-d595-3e0e-8358-5d81cb77a19b | -3.1129 | -48.6131 | 2024-10-06 01:45:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 53e6adeb-556d-37d7-bea1-6de79cd42eb7 | -3.113 | -48.5916 | 2024-10-06 01:45:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| dea845cf-3d24-3300-9592-3e1221be4213 | -3.1314 | -48.6125 | 2024-10-06 01:45:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 8597f024-e046-3270-aed6-e0bb3a23c634 | -3.2223 | -48.9733 | 2024-10-06 01:45:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 192b19b6-07d2-3f81-836a-058ecd756184 | -3.7068 | -41.6758 | 2024-10-06 01:45:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 66.4 |
| 4f3d385d-8b55-3fd0-b7e6-d54b063c71eb | -3.7255 | -41.6748 | 2024-10-06 01:45:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 95.7 |
| 7f908d08-fde8-36a6-bdd1-6b1241a0f728 | -3.8008 | -41.5989 | 2024-10-06 01:45:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 147.2 |
| 32b8ec4c-8bf7-3261-9882-767251c30648 | -3.801 | -41.575 | 2024-10-06 01:45:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 90.6 |
| e60627bd-3a35-330d-a7db-4185874e5685 | -3.775 | -49.4643 | 2024-10-06 01:45:27 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 1e906d38-4081-3380-a342-82ebd2ee8dff | -3.7934 | -49.4849 | 2024-10-06 01:45:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 84cdaeff-5867-35bc-9fd8-27d86b8cf979 | -3.7935 | -49.4636 | 2024-10-06 01:45:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| eeee04f3-4f3f-369c-ae46-3eac131428c9 | -5.5716 | -44.8927 | 2024-10-06 01:45:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| f6adf1ff-99c1-3468-bd9d-195412a0f458 | -5.5718 | -44.87 | 2024-10-06 01:45:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 8e94106d-bb5b-3c97-81c8-583214afdd1a | -5.8214 | -44.1426 | 2024-10-06 01:45:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| e091a276-7996-3d60-b6e6-ea3fec08630a | -5.8216 | -44.1196 | 2024-10-06 01:45:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| b6acd08f-5f3f-39f0-a296-910b795816ac | -6.9514 | -59.0666 | 2024-10-06 01:45:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| cf467705-93f9-3a19-ac54-8810597ea59b | -6.9699 | -59.0658 | 2024-10-06 01:45:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 892a2b80-8768-3fa4-bced-21bdb092c096 | -7.1532 | -59.2898 | 2024-10-06 01:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 7a0371fb-b49c-3af7-b876-019790c7597e | -7.87 | -54.8828 | 2024-10-06 01:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| e5d8ad28-494a-31c5-bac5-69450a9b5fdd | -7.964 | -54.7562 | 2024-10-06 01:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 8e652c57-033f-3d4a-bead-383936c3b250 | -7.9825 | -54.7752 | 2024-10-06 01:45:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| e5ce79d3-d817-3852-b3fa-d36fa6170a58 | -8.2139 | -61.2022 | 2024-10-06 01:45:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 9cf54000-c6ae-308e-b1cf-8bca3b0ba85a | -9.1449 | -60.6612 | 2024-10-06 01:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 2eb476f5-5e3a-3b8d-b484-949e332b6274 | -9.3275 | -46.5609 | 2024-10-06 01:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| d452853c-cf17-37be-9ad4-e4c43952a625 | -9.3278 | -46.5385 | 2024-10-06 01:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 195.3 |
| 7247433c-9aaa-3a42-96c6-8543db33688d | -9.3464 | -46.5589 | 2024-10-06 01:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 20a52e76-9e9c-312d-b62e-19cfdfef754c | -9.3467 | -46.5365 | 2024-10-06 01:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 316.3 |
| 1ae7a714-1fa5-3a0d-a540-6ded90dfb7c3 | -9.3656 | -46.5344 | 2024-10-06 01:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 4156fb77-636e-3584-bf40-38dc480e92bf | -9.3647 | -51.0898 | 2024-10-06 01:45:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 2a70b6e0-034c-3605-b9e3-c752ab724805 | -9.365 | -51.0687 | 2024-10-06 01:45:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 5471894a-cd90-3f6d-996a-024c62e22842 | -9.3835 | -51.0881 | 2024-10-06 01:45:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| f86d7597-ef4e-3ec4-83a6-15e7e716b73c | -9.6779 | -64.6269 | 2024-10-06 01:46:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 98a87f8b-ac44-3256-8622-4f90091468b0 | -9.6965 | -64.6262 | 2024-10-06 01:46:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.7 |
| aaeff46f-797e-3d32-a7f8-d99338b546e5 | -9.8552 | -60.2966 | 2024-10-06 01:46:02 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| d75e65b5-50af-328f-8632-b50e8ed0e661 | -9.8737 | -60.3149 | 2024-10-06 01:46:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 2e33d2be-ec30-346d-93d9-ff1fa9bf3104 | -11.0966 | -54.2336 | 2024-10-06 01:46:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 5678e9ab-967c-34e7-b1f1-81535007a146 | -11.1155 | -54.2319 | 2024-10-06 01:46:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 716ca1d5-bca1-3b00-b124-792441fa01ba | -12.0211 | -63.7478 | 2024-10-06 01:46:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 80.3 |
| c7cae3fd-8d8a-34f0-ae7a-ebbf6f5d4f9e | -12.7089 | -40.2155 | 2024-10-06 01:46:17 | GOES-16 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 78.4 |
| 0daef36a-dc78-315e-b6e4-0b3d468bbb56 | -12.6089 | -53.1338 | 2024-10-06 01:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 582ccc17-cfbe-3f36-ad39-67018cfb8da1 | -12.6092 | -53.1129 | 2024-10-06 01:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 619143a1-c5f7-3f25-bd06-d125a07eb4d6 | -12.628 | -53.1317 | 2024-10-06 01:46:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |


[Clique aqui para ver as próximas entradas](README33.md)
