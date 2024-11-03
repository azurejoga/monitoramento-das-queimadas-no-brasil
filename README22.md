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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0235b3d4-ea1a-3f38-a1f0-06988d3fcf49 | -2.6321 | -48.5849 | 2024-11-03 03:35:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 031a658f-794e-394c-ae53-70bfdfbd8e46 | -2.7218 | -49.3295 | 2024-11-03 03:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| d887b0ac-ff89-378e-a968-966dc89e6e9b | -2.8148 | -49.1567 | 2024-11-03 03:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 250f27a4-4b22-32e7-8d81-a4aec1888d99 | -2.7419 | -54.4353 | 2024-11-03 03:35:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| dfd3e1b2-638e-31b6-a292-87476a683b4c | -2.7419 | -54.4153 | 2024-11-03 03:35:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 1933c3ed-d86f-3bec-9830-ee95ca36de78 | -2.7602 | -54.4349 | 2024-11-03 03:35:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 112accee-8be1-34b0-8d00-32ea8338fd90 | -2.7603 | -54.4149 | 2024-11-03 03:35:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 377911bc-5623-33f2-b168-39fa110954db | -2.8333 | -49.1562 | 2024-11-03 03:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 84c398d5-3cb0-3b6c-b991-a8b1ccb53d26 | -3.055 | -54.1474 | 2024-11-03 03:35:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 2992b9cd-ab9d-3344-9a12-655ac8a88e5b | -3.1501 | -48.5689 | 2024-11-03 03:35:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| e3383d48-8837-3668-ace0-75746c07ccd2 | -3.0734 | -54.147 | 2024-11-03 03:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| c9267e1c-810d-3bcf-ad00-90ddf762914b | -3.0734 | -54.167 | 2024-11-03 03:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 2f203cb6-db74-33f6-bfe3-ddd2ed158ce5 | -3.3276 | -50.2825 | 2024-11-03 03:35:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 48eea4e8-5e11-349f-b5af-e94d1299bb55 | -3.4749 | -50.3826 | 2024-11-03 03:35:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 185f1a07-f198-359a-a3b3-59803e4a210d | -3.967 | -48.15 | 2024-11-03 03:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| f07a72dc-3916-3cb5-a578-c9ee7174a2c1 | -4.4054 | -43.4746 | 2024-11-03 03:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| dd029492-69cc-3ebe-bcdc-e4fde783ca91 | -4.4056 | -43.4514 | 2024-11-03 03:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 2e13bac8-408a-3309-a723-002ac6fbed51 | -6.5239 | -41.4929 | 2024-11-03 03:35:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 69.9 |
| d9e4b467-b952-3cd8-81c9-adb4d30982a6 | -6.5241 | -41.4688 | 2024-11-03 03:35:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 53.6 |
| 715dd6f0-4ff5-3878-8326-f7f37a8bb8a4 | -1.2755 | -53.4138 | 2024-11-03 03:45:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 126.2 |
| 43edbde1-7206-3b48-8034-27f2a127597d | -1.2755 | -53.3936 | 2024-11-03 03:45:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| b2fecbb5-4fc9-3045-bae4-20ddb786978d | -1.2939 | -53.4136 | 2024-11-03 03:45:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 286d1cc3-899e-3457-8b80-9524fd176983 | -1.2939 | -53.3934 | 2024-11-03 03:45:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| c342d936-9a31-399a-9eeb-c7e1e16cef59 | -2.1746 | -53.6834 | 2024-11-03 03:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 014908da-2823-314e-9cec-6d8bdba2e8a8 | -2.6321 | -48.5849 | 2024-11-03 03:45:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 1af5d47c-ea23-3a16-a864-0f82ab24d94d | -2.6322 | -48.5634 | 2024-11-03 03:45:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| ad3414ef-7810-3cb8-bcb7-fdcc8fd3a954 | -2.7419 | -54.4353 | 2024-11-03 03:45:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| feaaa9d2-c5a9-31a5-974d-bc06826b7137 | -2.7419 | -54.4153 | 2024-11-03 03:45:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 29a5472a-9179-34bb-b561-421b18a2d8e1 | -2.7602 | -54.4349 | 2024-11-03 03:45:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| ae6f0daf-b78e-3858-ae83-1e4c895cbf5b | -2.7603 | -54.4149 | 2024-11-03 03:45:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 274a73c7-c4b2-38e5-abce-f3abc4461cbc | -2.8148 | -49.1567 | 2024-11-03 03:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 06f80f45-f346-380e-88c6-5ed6ba530360 | -2.8333 | -49.1562 | 2024-11-03 03:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 1d04a241-828f-38af-96f8-0b1cfe32df29 | -3.055 | -54.1474 | 2024-11-03 03:45:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 3b183669-d8e6-3e82-9a09-b2da7579ead2 | -3.0734 | -54.167 | 2024-11-03 03:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| a34ba01c-152c-3859-829d-ab35f4a7c4a5 | -3.0918 | -54.1465 | 2024-11-03 03:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 307b7985-89d3-3612-b0c4-df2f08796048 | -3.106 | -50.2896 | 2024-11-03 03:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| b443e173-2d3d-335c-ac20-fc7dcf8a7240 | -3.0734 | -54.147 | 2024-11-03 03:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| f1af4c78-3f62-306c-84ef-8f05ed24ead6 | -3.4749 | -50.3826 | 2024-11-03 03:45:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| e3f0b297-342a-3376-a259-f94d4afeae33 | -3.967 | -48.15 | 2024-11-03 03:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 37bac3bc-b26d-3338-9dd8-77fe723fcc2d | -4.4054 | -43.4746 | 2024-11-03 03:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| f1863941-5c63-34fa-82d5-7355863994bf | -4.4056 | -43.4514 | 2024-11-03 03:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 9c32f1b1-b84e-3f90-9b22-422ae6afea14 | -6.5239 | -41.4929 | 2024-11-03 03:45:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 62.1 |
| 6ae80768-56fd-3516-82d5-2b278254e8e9 | -9.1058 | -43.19027 | 2024-11-03 03:53:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 948fda0d-f4d0-3f5f-a8fb-5fc8e438d26c | -9.10269 | -43.19242 | 2024-11-03 03:53:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e3947336-69a5-368d-b082-5b65e7ba40a5 | -10.25595 | -43.37395 | 2024-11-03 03:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 31429d1b-a69c-349f-95fb-b7ff9d6ab639 | -10.01263 | -43.7942 | 2024-11-03 03:53:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0eada6ea-1b72-3472-9c97-5c26455530be | -10.01005 | -43.80916 | 2024-11-03 03:53:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cf7aaa1f-8840-374b-88af-e35200bc228a | -9.79303 | -43.8768 | 2024-11-03 03:53:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6a785bc-a49c-389d-b30b-59a6af75bf9e | -9.78998 | -43.87102 | 2024-11-03 03:53:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8efc564-7c10-3f0c-9663-cb358af977d3 | -10.87755 | -44.28558 | 2024-11-03 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f004c829-45ff-3598-9861-3d21059dceea | -10.87545 | -44.2844 | 2024-11-03 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 61169031-d31b-3d3c-b883-4ca51d5bebd5 | -3.1344 | -44.17065 | 2024-11-03 03:53:00 | NOAA-20 | ROSÁRIO | MARANHÃO | Brasil | 2109601 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e3eff59-fb93-35b8-a10e-7096d8fbabe5 | -4.73568 | -43.25249 | 2024-11-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5807c1cd-41b6-36c2-8096-5d18406fdaa4 | -4.53647 | -43.29168 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25db9c22-4dc5-36d0-b11c-90ef65d27230 | -4.53585 | -43.29534 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f22caa6d-264e-3c57-8cde-fdac1088fbda | -4.41841 | -43.47696 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ef49565-0c08-3cbb-9cb2-7352ab151edd | -4.41615 | -43.46484 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 43c94bcb-3809-3a63-9ddb-4e37d88e6377 | -4.41552 | -43.46864 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2102a73c-a6b2-3e80-9638-30c145ee3499 | -4.41488 | -43.47244 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 224c1dd6-b249-3a89-84e1-c58b8d409dfb | -4.41425 | -43.47622 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 517e2fed-76d7-3387-bedb-6d02caf5810c | -4.41362 | -43.48002 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc84d838-bd5b-3890-bbe1-a9f0bbd4073a | -4.41325 | -43.45655 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 801a564b-7a20-34a8-b1b3-4d10b027ae1d | -4.41262 | -43.46033 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 960b9afb-1f20-3069-b8fe-fb5149843591 | -4.41199 | -43.46412 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 892aece6-f83e-301b-a773-d3a6fa151297 | -4.41136 | -43.46791 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e1849745-09bb-3177-a1f5-bcd03bafce36 | -4.41072 | -43.47171 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0c5aa228-ba42-37c2-b508-bfcfb5815fad | -4.41009 | -43.4755 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 27d326af-b661-3f3d-8734-1747bb98f84c | -4.40946 | -43.47932 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36cda35d-2ca6-3de1-9009-be4b987cf665 | -4.4091 | -43.45582 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| fe5a4224-9fe8-379b-8af4-f545540138e6 | -4.40846 | -43.4596 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| cb296681-0b3a-3742-bbd5-43fee191ace2 | -4.40783 | -43.46339 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2841d01f-89f4-3a4c-b2e7-c87caf8b4ff3 | -4.4072 | -43.46717 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0f88b131-0fdd-344b-824c-5e02e544319d | -4.40657 | -43.47096 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46fced07-030a-364a-b2ab-e7751a419e79 | -4.40593 | -43.47478 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a19fbb7-a032-3622-bc76-1110127dd3e9 | -4.40494 | -43.45507 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a212077b-0a10-30be-9854-960651dc371d | -4.40431 | -43.45887 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 579ab95e-3222-34d9-b93c-28a5acb3b94c | -4.40367 | -43.46268 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b1027258-f628-3d86-a2a6-b25f3b6c6816 | -4.40304 | -43.46646 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fd1a1c16-8e48-36d1-b92d-4af40128ea5c | -4.39887 | -43.46581 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8d113a1c-5bb6-36b3-add2-198c2eed94c6 | -4.3938 | -43.46133 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da8e40c7-38db-35ae-a1bc-5d5cb64b4925 | -4.3918 | -43.45691 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| acaff03d-ece0-3607-96ea-7739a2ac1bfb | -4.39117 | -43.46069 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5656d0e-7391-3ea3-a4c0-8333792adf6b | -4.39024 | -43.45687 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f186633-dac3-3dfd-8982-0493b4a4400e | -4.38963 | -43.46066 | 2024-11-03 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0edf3670-149f-33be-8cdf-07a51d6ff8a3 | -3.93316 | -44.30104 | 2024-11-03 03:53:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8bfccc3-96e9-31df-b629-1c84a81fbd92 | -5.22808 | -43.47952 | 2024-11-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0eb52d20-2671-303e-8327-1ed88b69caff | -5.15996 | -44.22963 | 2024-11-03 03:53:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cfd563ea-7b12-3464-97fd-fef113f9f350 | -5.15926 | -44.23378 | 2024-11-03 03:53:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 788e74e3-7324-33f0-b9fc-9eeb795ac2b0 | -5.06155 | -44.22273 | 2024-11-03 03:53:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 410cbb27-ee40-375e-bcf3-3e141d086d5f | -6.40696 | -43.83549 | 2024-11-03 03:53:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de8a518c-5b7e-379a-baf5-bfeda5adb4a9 | -6.40283 | -43.83472 | 2024-11-03 03:53:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7437fe05-f2f3-3f35-9da6-8e18d3522c94 | -6.18508 | -44.52549 | 2024-11-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24822dcf-e970-3773-b8c1-4e0542a87e62 | -6.18439 | -44.5295 | 2024-11-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00cda367-0f73-3854-8f0c-7197cc53cb6d | -6.10456 | -44.76066 | 2024-11-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| deae3f7a-bd94-36f1-b11d-b3d5a14b9fd0 | -6.10382 | -44.76509 | 2024-11-03 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be446ca9-1bf3-38c0-aaaf-14efb50f53e1 | -2.42378 | -45.71549 | 2024-11-03 03:53:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7e32275-c52b-35b4-a3fe-20808aed2196 | -3.27362 | -45.35836 | 2024-11-03 03:53:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb2733a0-da5d-3a07-8cbe-3bd7aae97494 | -3.07361 | -45.0238 | 2024-11-03 03:53:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad2121aa-2f40-318d-ac0f-d734d8a644f9 | -4.84216 | -45.72826 | 2024-11-03 03:53:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7718f35-31b5-3288-af31-2d39e52013d1 | -4.83737 | -45.72723 | 2024-11-03 03:53:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README23.md)
