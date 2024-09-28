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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 203bfc2c-df15-3fdb-9a83-5e7f10d84cc5 | -2.87614 | -51.68134 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 07c1aef2-c4ce-3e44-ab13-ca6b1a0d66f5 | -2.87606 | -51.6633 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 831ae4b9-aadb-3d72-8242-333604894548 | -2.87526 | -51.66841 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1216f7e1-02e2-3d63-ad97-ee64d8a92798 | -2.87522 | -51.66032 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24907503-deb2-38c0-bc7e-f5765cb380ee | -2.87456 | -51.3817 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5ea0ad2-01af-3133-b525-e844f31526ce | -2.87446 | -51.6735 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 768929c5-8623-304c-811e-aae5fbd33b1b | -2.87446 | -51.66545 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9e034a5-e5bd-3487-a231-8bfb96e39e18 | -2.8737 | -51.67054 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c611319f-aee7-3056-8807-b5fe5994259c | -2.87366 | -51.67859 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 030ebc75-45f2-3bd2-8f7e-e8f46737a89a | -2.87294 | -51.67565 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 73ba91dd-de17-394c-9938-5c52a5fd154a | -2.87218 | -51.68076 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 49f5733f-da18-392f-b85f-edb5ecd27c2e | -2.87129 | -51.66782 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc110dbb-6467-379b-b7e3-748604b4bbfd | -2.87049 | -51.67289 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 98724e38-bebb-3753-9228-6c0819350a35 | -2.87048 | -51.66487 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13655a31-1c9a-34f3-8502-3a34f044f08c | -2.86973 | -51.66993 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4db1ee20-7b44-397d-9f38-88c4194c3b25 | -2.8697 | -51.678 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 5ef8493e-6c01-3af5-8e67-b00004a86bbd | -2.86897 | -51.67504 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83bed04e-8fb8-395e-91eb-15827746b032 | -2.86821 | -51.68014 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5560738c-d530-3b70-9816-fa547e41b075 | -2.86732 | -51.66721 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a297e12-d1f8-3cc9-9682-1b81a44cf4e9 | -2.86653 | -51.67228 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53825462-dc16-308c-917b-ef864793e924 | -2.86576 | -51.66933 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35051edf-60cd-3925-91c2-9984f6619173 | -2.86018 | -51.6609 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 076bd81a-8b6a-331d-af84-88241f6b6543 | -2.85939 | -51.66599 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8dd0fef3-5c4f-30d5-8c4b-5db8eadf2aba | -2.82625 | -51.34538 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 84282963-4539-3322-bb1c-1d40d0547c62 | -2.8222 | -51.34477 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5279616b-c42c-35ed-afa4-4c1e61b2ec75 | -2.82167 | -51.34832 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 27fcc9f8-41cd-3224-9a5d-c0de18dc1d37 | -4.60406 | -50.9573 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1bb819dc-9dc1-31c8-88f7-5b4f744cd318 | -4.60304 | -50.95601 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46b9b171-e014-3084-bbfd-e3d07428dbfc | -4.15181 | -51.05923 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9494531e-d09a-33cb-be2a-fc24c0947a7b | -4.14757 | -51.05876 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c5c4055-894c-34c5-8564-782c1bb868e2 | -3.8814 | -51.90213 | 2024-09-28 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84e5e39b-0b76-39b3-8537-fffe002eb3c7 | -3.87829 | -51.92255 | 2024-09-28 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6cb837b-3efd-32db-80be-5badddfa12aa | -3.8775 | -51.92778 | 2024-09-28 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c68b6e45-b8a2-3162-8125-969f4a6b83b9 | -3.87731 | -52.08692 | 2024-09-28 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93e13557-00f3-3e97-b410-d95bf7078887 | -3.87644 | -51.1669 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 397c025b-a39d-3dd0-b178-6aaae3b10e0d | -3.81326 | -52.19268 | 2024-09-28 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75881ca2-716b-3f4e-994d-4c91805e2b74 | -3.7759 | -51.85825 | 2024-09-28 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfb6a73f-c6bf-355b-82eb-932ea8119f6e | -3.76816 | -51.80189 | 2024-09-28 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 868ebcdc-746d-3cb2-99e3-511ea53ab717 | -3.76366 | -51.8047 | 2024-09-28 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 54578397-e76d-38fd-94bd-5b47573ac387 | -3.75163 | -51.30466 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a13e6f1d-db1f-368d-a0cc-f72854d4209b | -3.73425 | -51.81076 | 2024-09-28 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74d8b91f-84cb-33d0-8b27-6657a28cfdda | -3.63845 | -51.78181 | 2024-09-28 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af8951e3-bc0f-36d1-8df8-c228e1d32392 | -3.63794 | -51.78522 | 2024-09-28 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75b2d871-02a7-3ddd-a0f4-914ce00b7bd6 | -3.63447 | -51.78119 | 2024-09-28 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b339727a-2cf7-3de0-a465-f9a5dbccc0ac | -3.6094 | -51.79736 | 2024-09-28 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fffb931-b42a-38a6-a5da-14371447f616 | -6.14494 | -51.24994 | 2024-09-28 05:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07079193-770e-3ee3-a30c-5acf5d145b26 | -6.14009 | -51.25321 | 2024-09-28 05:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 239d47ab-b252-3808-ba15-d5cdd4002b72 | -6.1352 | -51.25676 | 2024-09-28 05:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aaea0470-6f23-38f6-bd95-9c54392afd3e | -6.13152 | -51.25203 | 2024-09-28 05:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 812fbfc3-a0e8-31a8-9226-8c690a2aa261 | -6.13089 | -51.25631 | 2024-09-28 05:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a75e62c0-c650-3f25-aa11-68381dec80aa | -5.41189 | -51.15688 | 2024-09-28 05:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22358b91-09fb-3c76-a658-46373a8f8c50 | -5.30395 | -51.45106 | 2024-09-28 05:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bbf86c6-2a5b-3bb2-ae12-b8fbba365217 | -5.30339 | -51.45487 | 2024-09-28 05:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85d9608b-4d83-3fff-8f0b-6d6359cf9bc3 | -5.29978 | -51.45043 | 2024-09-28 05:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c796a8d8-1591-3a7d-bdfd-79e8bd19506c | -8.55205 | -51.79007 | 2024-09-28 05:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3af204f5-e12f-3691-9f52-5366e68f01f9 | -8.55143 | -51.79434 | 2024-09-28 05:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08bf629f-fec9-3d38-acad-32ba0efb919b | -8.39598 | -51.76043 | 2024-09-28 05:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61fa855b-638a-3dab-9d53-40373a02218f | -8.34799 | -51.73959 | 2024-09-28 05:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d19a72a-2c76-37b4-91be-70a6c101e5b4 | -8.34315 | -51.74294 | 2024-09-28 05:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ad61920-a069-36e4-9b8a-097c988d023c | -8.33833 | -51.74608 | 2024-09-28 05:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 685e1b91-7d4d-302f-bb36-044270b9bd36 | -8.33034 | -51.74092 | 2024-09-28 05:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e2590e3-0815-3a89-b3d1-80a3d4e36b7a | -8.32607 | -51.74028 | 2024-09-28 05:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38c0475d-e804-3c07-96c5-e0e8801a9f54 | -4.0678 | -54.10623 | 2024-09-28 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fa8a4596-abc2-3b9f-bfcc-71aa8f91cc74 | -2.07141 | -52.02059 | 2024-09-28 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aa2f91e4-0289-3433-a183-f2819dbe79a1 | -2.0696 | -52.01805 | 2024-09-28 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 36b2a16f-584c-3131-a711-6d7e50afab34 | -1.18384 | -53.17532 | 2024-09-28 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05bbde4a-96fe-3511-894f-be02a7075150 | -3.21138 | -53.39618 | 2024-09-28 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 68e6add3-2ca8-3248-9930-48d16857eee5 | -3.20841 | -53.39148 | 2024-09-28 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 4592c456-3416-3306-be6e-b6ad8d052ab3 | -3.20777 | -53.39565 | 2024-09-28 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 68712704-deb8-3776-9f95-d8a05de019cc | -3.20713 | -53.39981 | 2024-09-28 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c3647d22-063d-327d-bb6d-8b80b8043067 | -3.2048 | -53.39096 | 2024-09-28 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9fadb41-0b37-3e42-a5b4-a3c56da866ac | -3.20416 | -53.39512 | 2024-09-28 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24960045-108b-3407-ac27-cf6f9370d0fc | -3.20183 | -53.38631 | 2024-09-28 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b96c3dba-4c25-31c5-8e32-6c93c71276cb | -3.2012 | -53.39043 | 2024-09-28 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 714c6871-cc46-364b-bc69-987b6debf09a | -3.20056 | -53.39458 | 2024-09-28 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 86267ecf-7099-3e78-a9c0-b9852ea4c693 | -3.19822 | -53.38579 | 2024-09-28 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a04e173-d119-36dc-a6c4-914e32145c17 | -2.86136 | -53.31704 | 2024-09-28 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8a3f4f4-c977-3692-842c-c5fa32f0cf88 | -2.85839 | -53.31237 | 2024-09-28 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5dfcae41-ba08-3745-b417-801c3814e2c8 | -2.85776 | -53.3165 | 2024-09-28 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7e558b1-d322-3509-96c9-89c00d3777d8 | -2.85415 | -53.31596 | 2024-09-28 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 697683a9-01fb-39e3-9225-cf69027713e5 | -2.85352 | -53.32009 | 2024-09-28 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0ef1503c-46b3-34fb-bb11-10629d68955d | -3.51588 | -53.62759 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3713644b-c80e-3b88-98a5-f30f709bddbd | -3.3905 | -53.71235 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bca9ea7b-dd0b-3316-80b6-8bddb3b06c0a | -3.38987 | -53.71643 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba5e14c5-9df0-3b07-923f-d40bb8e75eac | -3.31263 | -53.37171 | 2024-09-28 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 541aab0a-b47d-3478-b8f9-9ed4a6e980ab | -3.30901 | -53.37119 | 2024-09-28 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3ee725d1-9baf-36c8-87d0-b2e41f2f12f3 | -3.30336 | -53.69244 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0112566b-cb42-3a0d-850e-03d0b18317b8 | -3.30273 | -53.69645 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0cf145f9-bbed-344b-b079-1a93cdb60637 | -3.30211 | -53.70043 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 478595c4-731f-3848-a5f6-524c52747ed4 | -3.30149 | -53.70441 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2095e670-d705-3283-9553-c14130391888 | -3.29918 | -53.69591 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a37190e-c973-3c8d-b9d1-f267a914e0ad | -3.29856 | -53.6999 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bdc060b6-438a-3d65-91a0-adec5823486e | -3.29794 | -53.7039 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 01504b28-803b-3c19-a3ee-37d94d646fc0 | -3.29438 | -53.70337 | 2024-09-28 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15b57ad0-ae14-3414-9ac6-e674b0fb06ca | -3.88698 | -52.36993 | 2024-09-28 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 268b200e-faa9-3e9e-9533-22ffb25dbf92 | -3.84779 | -52.3687 | 2024-09-28 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e19a4206-4f74-3d7d-8c86-88dceed225b2 | -3.84614 | -52.36583 | 2024-09-28 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6f9ddde-4169-31cf-8f38-f9c5c4f92442 | -3.84541 | -52.37054 | 2024-09-28 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d0d02f2-e7a4-3239-aeca-6ddd64dfcec9 | -3.84465 | -52.36335 | 2024-09-28 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69a469bb-86ec-3779-ae3e-904bdc5ec892 | -3.84395 | -52.36807 | 2024-09-28 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README73.md)
