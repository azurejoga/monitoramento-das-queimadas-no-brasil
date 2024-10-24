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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a36f563-7c63-3973-864b-40cf02a42ef4 | -3.81566 | -49.91544 | 2024-10-24 04:32:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 758a98eb-ddc7-3f8c-aad4-c33eede9d0a4 | -3.81214 | -49.9149 | 2024-10-24 04:32:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fa06c03b-9b01-3e73-8872-2f83d2a8b42f | -3.80415 | -50.16729 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80d3c4bd-023b-33d3-87b9-d8318275aab6 | -3.80062 | -50.03097 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c5d6aae-c3c3-3945-9a89-a1504323b9c9 | -3.80059 | -50.16674 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 410ff16c-f609-323d-947c-b2f2412b214a | -3.79709 | -50.03042 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68e89333-8d69-3216-bf03-970cbfd3965c | -3.79703 | -50.16618 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6c63a231-bc4e-3ac8-856b-131f4841a1aa | -3.7764 | -49.95395 | 2024-10-24 04:32:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e5d21db-99ef-3db0-8853-10700451a2de | -3.76219 | -50.38279 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9252f36e-7e4f-312b-afe0-0f5560589302 | -3.76152 | -50.38696 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2960d49b-099c-3188-977a-e10b33be2401 | -3.7601 | -49.8747 | 2024-10-24 04:32:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b1f2321-8dbd-3c97-a6bb-54e6d8b0a6a1 | 2.63529 | -50.8807 | 2024-10-24 04:32:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e51c196-84e0-3516-92b8-8e40c7281b56 | 2.63179 | -50.88486 | 2024-10-24 04:32:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d88c3a0f-5f53-31cf-ba82-438a7f3c6773 | 2.63125 | -50.88131 | 2024-10-24 04:32:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1177e6cc-5818-332d-abe4-d5c2633756bf | 1.812 | -50.47049 | 2024-10-24 04:32:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 154a9df9-bc9a-3f37-86a8-08340172ec5b | 1.79644 | -50.47282 | 2024-10-24 04:32:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 596bb154-bc79-3e38-8515-96b03bc9957f | 1.79331 | -50.47831 | 2024-10-24 04:32:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8dbb8fb2-a6b5-3aa2-8043-fbe1190b81c4 | 1.79255 | -50.47341 | 2024-10-24 04:32:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 814aa91d-9c0e-3fea-996b-53d713e50b69 | 1.78942 | -50.47889 | 2024-10-24 04:32:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b6690077-a51b-3a23-ac1e-2f4a4272cc10 | 0.83699 | -51.15112 | 2024-10-24 04:32:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69b7fece-6944-3379-a1e5-fb9638a429f2 | 0.00432 | -51.22325 | 2024-10-24 04:32:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3f0370f-9d3b-3ce9-bb96-e9884bacd044 | 0.00377 | -51.21983 | 2024-10-24 04:32:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7004afd5-6b0f-37ab-a0be-23df3d573480 | -2.22794 | -50.71526 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2bd9d398-1794-3ca6-9fe8-902863c06123 | -2.2057 | -50.63859 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b092f35-b4aa-32ee-a56e-67c138807152 | -2.19502 | -50.70557 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed3e65fe-ad80-3f23-9e39-b549cce94d4b | -2.17093 | -50.53094 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0bf4836e-dc86-3d85-8949-81b913b7dc51 | -2.17008 | -50.52908 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 181767f3-805f-3cd7-8c73-1976de29579e | -2.16212 | -50.69584 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da7e5f50-ee3c-30ab-8d25-e043f683321d | -2.1614 | -50.70032 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7639183-de2a-3224-9cf4-1ab4753b1b15 | -1.8392 | -50.65041 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 443c8508-c171-3901-8073-3c11ea2b611d | -3.59647 | -51.38453 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6997932b-46ab-3e7c-a0dd-e44cf7e1c5d7 | -3.56876 | -51.24345 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42f54f39-0eb2-3640-b004-cdb98f5615f3 | -3.56835 | -51.2468 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d4ac639-dcf5-31a9-8224-a2a288da4561 | -3.56044 | -51.24694 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9d0b48df-23e1-392c-82e0-294f0e0519d7 | -3.49843 | -52.08791 | 2024-10-24 04:32:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50cfb0d4-623b-3daa-a640-48e65a74c1c8 | -3.49318 | -51.59506 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b624958e-7d46-3e79-bfca-393230a6030b | -3.4924 | -51.5999 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04e9af06-779a-378a-a87e-1a91e37fcae5 | -3.47334 | -51.20961 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 415b3fd5-d4a4-3997-b991-d9fbaeda52de | -3.47298 | -51.21144 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6e2ab312-70f8-32bb-b10f-a519d64c51e2 | -3.47259 | -51.21419 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 90f9a4ef-ec7b-3ddb-abff-3f74b96af4fa | -3.47113 | -52.10452 | 2024-10-24 04:32:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c75b3666-2a73-3ffd-86e3-e61ac3f36f1d | -3.47056 | -52.10799 | 2024-10-24 04:32:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1930cca-f1ca-392f-ba01-79e9c4999df6 | -3.46368 | -51.63026 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 388530c7-110d-32e8-b28b-f8b1260101d4 | -3.45448 | -51.58886 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 116b45f3-48d0-3940-a798-5c73a605ee6e | -3.45061 | -51.58826 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 40783db7-f534-3cbf-a573-4392f6ba53bd | -3.44674 | -51.58765 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f99c1d94-f77d-34a2-942b-aa8c502b7af7 | -3.38296 | -51.2399 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6406507b-4aed-312b-8777-e3550f717db0 | -3.34796 | -51.64954 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3325bc7e-979d-3b3d-b01f-9e20da899061 | -3.34407 | -51.64894 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5bf48428-c1f9-315d-9d73-d5dc476a05c7 | -2.41089 | -50.47924 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f593d04-f2af-30e7-a0ed-7e6d3da50ddf | -3.26816 | -50.77192 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 94fbd166-8590-3dc8-b0a3-2864af339d33 | -3.26745 | -50.77631 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c5a0ebda-212d-3912-859c-6e3fd1bc1ccd | -3.24423 | -50.84964 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9169bd3f-2e2e-3130-8bd8-e047ac3943f6 | -3.24052 | -50.84904 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 56570985-7d74-3d30-98f7-26b90eb64b3f | -3.19556 | -51.27131 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b083717-9472-3e3b-9cc5-598f49633695 | -3.17573 | -51.24898 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df574bd4-2af4-32c3-9a25-a2dc913e94bd | -2.95685 | -51.45303 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 16a8f49b-e2f1-3e74-8cd8-4b11991ef885 | -2.95298 | -51.45247 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a8931b60-bb58-32b0-8e5c-4b6378a6aee0 | -2.87432 | -51.31395 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f5cd3b36-3592-3f22-b9ba-32f62ee17457 | -2.86624 | -51.59389 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1eb5c341-77f3-3d1a-8dcc-6939f306e2eb | -2.86543 | -51.59883 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3aa86d6b-f159-363f-afc9-0b1518d637c2 | -2.86535 | -51.59572 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f16a9fd9-2772-34ad-8993-b03739482fc0 | -2.86457 | -51.60067 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f2f9516f-1993-3789-8c00-5f81e9f080c9 | -2.86233 | -51.59328 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8e597334-9fc5-3c53-b74f-f008747fba32 | -2.86152 | -51.59822 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 989c2517-f908-3793-9fc0-920f9e7dff23 | -2.86144 | -51.5951 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9394c182-796e-3e27-935e-321f6de374cd | -2.8607 | -51.60318 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 17022e7c-a0ba-3109-8761-0ef359fb08fd | -2.86066 | -51.60007 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 74b12031-207d-3b80-9843-1b7cd62020a3 | -2.85987 | -51.60504 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f80e52c-d808-34a9-994b-b09685246a4e | -2.85761 | -51.59761 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7365cd67-722c-3bfc-8bff-b0f06974d66c | -2.85753 | -51.59449 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7685097a-eb91-32c8-b513-1ea022e01724 | -2.85679 | -51.60257 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 627d3330-28e6-304d-963c-b21e3bfaee18 | -2.85675 | -51.59945 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f8c56d47-e491-3a20-85a9-72370f540751 | -2.8128 | -51.3532 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fdd5a33f-4138-3575-9e50-97da4541d90c | -2.80122 | -51.59592 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4413113-1080-3034-ad97-13c748040920 | -2.80043 | -51.60081 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32695c83-1a66-33fa-a79f-67f37a45a10a | -2.79734 | -51.36311 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| da828a2a-dc73-3935-9559-5b2707450a04 | -2.79504 | -51.36517 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43e30d1b-27fc-370a-832b-c449051a3bad | -2.79348 | -51.36251 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2706028d-037f-389f-b51b-298e86c791ce | -2.79273 | -51.36731 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a4b9835-b9d9-312a-9779-c14a60e82443 | -2.79118 | -51.36457 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e57df03a-4a5e-3524-b245-c90d31dde331 | -2.60821 | -51.77249 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b635ce23-bd27-34be-ba51-6af2edcd855a | -2.60343 | -51.77699 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a89f3b2f-2d6d-34a8-b847-f9abb9dad21a | -2.58466 | -51.92148 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6384b31b-feb6-3829-a843-f8a2906f51f4 | -2.22114 | -51.67299 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cafc9db4-0bd3-3d0b-b1ff-1e490ba2f91f | -2.21678 | -51.07823 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e52fed63-d271-3c1e-9e64-270f74ee79c5 | -3.97636 | -52.16292 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a6bad4e-fac3-393a-9431-765dea2abdf0 | -3.89048 | -52.12399 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd7984a2-6f35-3fdd-ae82-104cf20fc1b6 | -3.88992 | -52.1274 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 106f8ccc-3ea0-3cba-a4a9-bfa4605657c9 | -3.88989 | -50.98747 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5c5605cc-0e2c-3172-b431-3e6cfad2dc4b | -3.86831 | -52.13454 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f2b0c028-5238-3386-b538-cc52c86a4b3f | -3.86774 | -52.13798 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 005ef387-4e9f-338e-a2cd-d34151fa5a6e | -3.86537 | -52.13721 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 897328dc-b427-3181-b4ed-c8f4a7f28862 | -3.86378 | -52.13724 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3d8b2e50-04b3-3bee-a2ce-2e9bb752d390 | -3.84934 | -51.88418 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b08daea3-ed99-3697-9f4f-bccb8f636a14 | -3.84542 | -51.88357 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55ab23bb-46a3-3331-88e2-b02928d9c4dd | -3.82977 | -51.35956 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 64bc8d9c-ce3c-3914-983f-cf07de3d14f1 | -3.82926 | -52.23491 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e596f45b-90ce-3fa7-9f38-89fe12677975 | -3.82901 | -51.36424 | 2024-10-24 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 30d98d59-b53f-3a98-a077-1f7a3c0bbbd7 | -3.82727 | -51.2079 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README36.md)
