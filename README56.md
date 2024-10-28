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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 878d4750-dc3b-368b-9516-f1820f58bb1d | -3.20725 | -50.21522 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 724630c5-25b1-346f-b0e6-44d0a8e665a4 | -3.17651 | -50.39256 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c8dd5c99-b2b6-3ada-8d80-83e910195ce0 | -3.17589 | -50.39664 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fe4222e6-5e3a-30cd-8ad1-bce520901a61 | -3.17356 | -50.38791 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb6a6904-6b62-3b26-a41d-8caece27af97 | -3.17293 | -50.392 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12a3565c-9c3e-3644-bbed-68f720e6b55f | -3.17159 | -49.1499 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b18b9a60-6eae-3352-a01a-89ab5f40d64e | -3.16998 | -50.38736 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 599f1e2c-3e4a-3fc4-b0b2-1cb427f1056e | -3.16935 | -50.39145 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10429c6b-02fc-3485-9875-f3ee86b27cc9 | -3.1664 | -50.3868 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e8426461-cde3-31e3-aba5-005497aef635 | -3.16577 | -50.39089 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d008caca-fa50-346d-9485-c679a9682b91 | -3.15462 | -50.46423 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18bb6fc3-1e06-3a48-828e-b98cb7c28996 | -3.15167 | -50.45961 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9f53784c-61e5-3de1-8c94-f389d22ae63a | -3.15105 | -50.46367 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3f62412-d637-32ee-80a6-8fb551726446 | -3.14872 | -50.455 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7f05e952-8942-3ced-b1a1-7bc04b699e1c | -3.13972 | -49.17897 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 26cb58bc-0686-380d-9349-7333f25e3a91 | -3.1346 | -50.31612 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 609405a3-3afb-3959-92d8-8904c390604c | -3.13276 | -49.17311 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb3399cd-47bf-3eee-ad93-b64a15c4ba3b | -3.12893 | -49.17253 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56dde87f-e38a-336b-83b7-69e2b9cfba65 | -3.12527 | -50.3525 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e952b25-9ec6-3fd4-bf7f-9a98ae027c8e | -3.12232 | -50.34786 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0372a17a-f212-387b-8231-902d9f3e3e23 | -3.12169 | -50.35194 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92d1cb55-0adb-33bc-84b5-ea1c0ce5365c | -3.11873 | -50.34732 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f70fd03b-1b4f-311a-9916-b3dd2d341095 | -3.1181 | -50.35139 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ed63494-6be5-34c9-9d89-cf2aa01a9aa6 | -3.11747 | -50.35549 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dfd138fb-5474-3b93-b9ef-048439ed5bfa | -3.11515 | -50.34678 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10a1f8c4-582c-324c-8f09-1902f8ce8a6f | -3.11451 | -50.35086 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc3ed40a-c2f8-365b-af46-35f80a8cc2ed | -3.09931 | -49.47203 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 872f11b2-007d-3b51-a2c7-5fefd7b24958 | -3.09008 | -49.3032 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33c469c8-bb4e-3b15-8e7c-ff0b8a71a3b3 | -3.08628 | -49.30264 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1838dd84-d055-36f7-afeb-d5a510020b89 | -3.08571 | -49.30508 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2816d85a-3984-3eb9-82cf-b0f90889082b | -3.07332 | -50.42805 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f174dbac-9105-32d8-895d-b53573f4c4a2 | -2.82825 | -49.23986 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 5e7931f9-d6c7-3285-95d4-7531f3756828 | -2.82754 | -49.24452 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6490f2b0-d639-3698-b278-8edfcf4bafca | -2.82691 | -49.39976 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e14fc91-a8fa-3032-b367-c03304c5dd00 | -2.82446 | -49.23927 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 786c370b-99c4-33af-b386-4949d41344ad | -2.82374 | -49.24393 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ab3f54d2-06b3-3fd5-a381-648fbcd7091e | -2.81827 | -49.2288 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bf8732a6-6cd7-3ba2-8e06-e58e96894a36 | -2.81615 | -49.24276 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dc8e5603-2fa4-38f4-bf36-be3cc3c3984f | -2.81447 | -49.22821 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 370f31f9-6baa-37d9-87dd-f415dc583a00 | -2.81376 | -49.23288 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c07b7b20-52df-344f-a625-1bfa13ee9fd0 | -2.81067 | -49.22762 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1c43427d-ff2f-3e55-b4e3-408b9690bff5 | -2.80996 | -49.23228 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bf3d2d34-2947-3c97-807e-2083bf954e21 | -2.80926 | -49.23693 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c767bb1e-518c-3110-aa29-052aac0fc296 | -2.80867 | -49.31735 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2e8750b-d11c-3b41-be38-d3f3c7cbde3e | -2.80616 | -49.23169 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e6a11111-509f-3cb2-b53e-0f24d114aa16 | -2.80546 | -49.23634 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ef818733-3eea-3b8d-bcbd-eacd313db334 | -2.79105 | -50.33405 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7c5c74c0-01ba-3eba-a659-64ac3203dbcc | -2.77303 | -49.57579 | 2024-10-28 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd1cc6d9-dd6b-367d-8907-9b4613ab37a6 | -2.77084 | -49.363 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 40459240-5586-3ff2-b693-72cf3bfe4387 | -2.75278 | -49.17748 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c13de43c-d08d-39d6-8b94-c70bcae1641b | -2.74785 | -49.30964 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f05bd689-d463-3482-bf9f-41af95552640 | -2.71102 | -49.32279 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a638bd7-d1bb-3d22-a6bb-8c64ab1f5be0 | -2.70956 | -49.05018 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ea0a30c-2ad2-362d-9648-b2d8e5e42bf3 | -2.70864 | -49.31306 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1da3ed5a-485a-3af6-8007-dd3232f6ba35 | -2.70794 | -49.31764 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7834ede5-daca-3960-a32f-3baacd82c7ed | -2.70724 | -49.32221 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0aeaa1f2-c47c-300c-955e-fccd54ae5cd9 | -2.70572 | -49.04958 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 394c75f3-2c96-3f12-bce7-066a67f1405b | -2.70486 | -49.31248 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3bb98210-7137-35c1-b2c0-fd542ae8dba4 | -2.70429 | -49.05912 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 19a5af48-766f-374a-a873-8da609217638 | -2.70416 | -49.31706 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 90f192e5-fbff-3d08-a25b-93b13fca44f3 | -2.70344 | -49.04751 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bad0f686-bc9e-37d1-9dc1-7cd142864e7b | -2.70269 | -49.0523 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a537d41c-692b-30dd-9554-8dc97d2187b8 | -2.70195 | -49.05705 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8752c70b-174a-3e0a-8821-64d3a6da33bc | -2.70188 | -49.04898 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c0193d8f-3dd4-3ec3-be0b-2c62d02236c8 | -2.70117 | -49.05377 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a098065b-c4ff-3f2a-b71e-9b47c6d83869 | -2.70112 | -49.82462 | 2024-10-28 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4e11d069-9e5b-3c33-8298-b698b7fc6b17 | -2.70039 | -49.31649 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12fb4e07-53b9-3c0c-ad06-8d5d6a7dfcee | -2.69969 | -49.32106 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89c87af9-3267-3951-8370-a96a488e30e4 | -2.6996 | -49.04693 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de51484b-c902-3ead-9649-6dc4445b1a16 | -2.69886 | -49.0517 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 810d916f-3515-3daf-b9fd-bd9879097f1b | -2.69284 | -49.31531 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b6763bd-f972-3de8-b6e4-73ed2087a925 | -2.67874 | -49.33185 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb453c5f-0584-3b48-b896-ac9116be9515 | -2.66951 | -49.31628 | 2024-10-28 04:57:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfdf603a-f6f1-38bd-b116-4b4be1d07e27 | -2.66599 | -49.81151 | 2024-10-28 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13d8d933-8f0c-3d75-9096-7433a5bd4b97 | -3.05763 | -49.49352 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8af457d-4990-34cb-b435-b574c32450c5 | -3.05698 | -49.49072 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 304f2230-25a2-3042-be02-278757513d1e | -3.05394 | -49.4856 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 46ba9331-cf09-354f-a345-813f4551264d | -3.05323 | -49.49014 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 01d60d40-476a-3b6d-a3ad-20909ca9694e | -3.05252 | -49.4947 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 63108ff1-9461-3670-a07e-2d0f803354dd | -3.04948 | -49.48957 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| da6e3dfc-4104-3c6d-af63-982b624a3e9f | -3.04896 | -50.42006 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c401988-74df-3f98-bec1-90f4c59624ce | -3.04877 | -49.49413 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 5e46d735-853b-3dc1-9cb8-c86dcacec097 | -3.04807 | -49.49863 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 12b26711-aca7-3894-979c-ea2a75d38636 | -3.046 | -50.41552 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 53f82190-5dee-3afe-a4eb-d43a7cf156d0 | -3.04538 | -50.41956 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 85b0e86a-2b7a-3388-88c7-8f3b8ec11071 | -3.04502 | -49.49355 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b9852051-e4d6-3da9-970a-a55a47ec7a48 | -3.04477 | -50.42359 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 517ecb27-9fa1-3f7a-b4d5-38cb2e7c7c79 | -3.04432 | -49.49806 | 2024-10-28 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| fb218380-521f-3241-b070-9d6d14abefd0 | -3.04243 | -50.41497 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9c131bff-26d0-3bd0-8415-43bf3e2e8aae | -3.04181 | -50.41901 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c2ef50af-b75e-3361-b91a-30ae64e85a48 | -3.0412 | -50.42302 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| df21d753-f942-3ddb-931e-56edbbda3270 | -3.04059 | -50.42702 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bf2fafa9-bf87-313f-92dd-268d25fff009 | -3.03886 | -50.41441 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2d6e698-54f2-33ee-b13b-ba9517d4ae71 | -3.03824 | -50.41845 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac2eca74-58ee-3e50-8f48-fc93e70d1bd4 | -3.03763 | -50.42249 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4bdb60e9-4a2c-39ce-a681-33d20e1ee812 | -3.03702 | -50.42648 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a02f1dc-184e-3c31-aaaa-d62055d9e8c3 | -3.0359 | -50.40981 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a54a797c-b78c-387e-85c2-2260e0c4b2b3 | -3.03528 | -50.41386 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abaf9870-c7ca-3c7d-9412-df0edfda009e | -3.03467 | -50.41792 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d42435b8-d52c-3e45-8413-b83315a24074 | -3.03405 | -50.42198 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README57.md)
