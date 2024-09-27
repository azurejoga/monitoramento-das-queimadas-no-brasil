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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1eb0eb7-5eff-3ed2-9b29-dd9933ef666e | -7.78254 | -61.18772 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 0b3ee51f-2ca3-3cee-a1c6-ddedf5e76dc4 | -7.78198 | -61.19128 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9f2d6b4d-c764-35e1-9a52-53edaef3224f | -7.78143 | -61.19483 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3e89dd1f-ae10-3864-9f28-6d0562dcad6b | -7.77974 | -61.18365 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 23841599-50c9-3fb9-8478-4f7cde13ce4e | -7.77919 | -61.18721 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 27.8 |
| bc01dad0-7d78-329d-82e6-6f47500b9129 | -7.77864 | -61.19076 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 34787bc6-774a-3730-98f6-6ab083738472 | -7.77809 | -61.19431 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 15e28e9f-cfb5-3f6e-a3fd-135f4b454830 | -7.77639 | -61.18313 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 02fd7ad6-c6d7-3541-ac72-f9d3a383fd70 | -7.77584 | -61.18669 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 86da423c-353d-3c29-aa3c-0e1c15dfddea | -7.77529 | -61.19024 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| dc04cd2f-42f4-3454-88c9-2c25dcfef05b | -7.77474 | -61.19379 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d79f3350-1fe6-3ecf-a94b-819727168473 | -7.7725 | -61.18616 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1622aaa1-98a7-3f5c-abfe-80d1b93c57bf | -7.77195 | -61.18972 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 4b661a13-12e8-3e59-8d92-2fefbf1e6f9a | -7.7714 | -61.19327 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f7d464fb-05aa-3dc5-99b9-12af373cb7de | -7.77085 | -61.19682 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2e2d4c06-07e0-319d-90b4-a8b8c7f6865b | -7.76805 | -61.19275 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 67b8fab9-95d1-343f-b8ac-1a12508d3c79 | -7.7464 | -61.22208 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03f22cd0-21a5-3fe7-8bfc-057aa05c7340 | -7.74585 | -61.22562 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2099039c-e3c3-3708-9532-2ab3e25b133a | -7.74305 | -61.22157 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2ffa01ff-726c-3223-b782-20727b39e2a1 | -7.72695 | -61.2372 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d12a09b-2471-37d7-bc2b-0b79f4f63061 | -7.60806 | -60.97831 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 134c5b4b-cf10-3e03-b0a8-e7a6762ee797 | -7.60526 | -60.97421 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c23cb951-e649-3566-9c81-9eb7db735e13 | -7.60471 | -60.97779 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bf861c05-fcee-3b40-8676-9841eba01143 | -7.59629 | -60.96548 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3ec593e-8217-369d-8015-702f593ddddd | -7.56852 | -61.32103 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4401cb39-8560-34ee-b92d-901e88eebd24 | -7.56518 | -61.32051 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ddd13f2-da64-34ad-90a1-4f57e72bc019 | -7.55915 | -61.35925 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 55a92d93-27ff-3947-9eea-da83d08b542c | -7.55637 | -61.35521 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 592289d9-42f8-323a-be09-01a5b6159e64 | -7.55582 | -61.35872 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| da5d75d0-20bd-3dcf-9e90-592f635c4674 | -7.53298 | -61.32998 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10079182-7345-3689-864f-dbda708a7962 | -7.47803 | -61.33222 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ece4c279-4424-3d26-b04b-e2bc6e7f82c4 | -7.47469 | -61.3317 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53917641-7042-3ecd-95a7-4cb46f202b8a | -7.47415 | -61.33523 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c63d814-e219-3920-8332-2353d0e6f132 | -7.92542 | -61.557 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1522ce5b-cf95-30b9-82d3-9889ba3f53e3 | -7.91822 | -61.55946 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96f13d13-a026-3db8-a479-ca907367b8a6 | -7.87757 | -61.66792 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c8956d2-1518-3b92-ad6a-05bbb52ad9b2 | -7.87479 | -61.6639 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88c55440-1946-3c67-a9e1-54dadcb6e805 | -7.87425 | -61.66739 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b52afc84-84f1-341f-8e02-592bac4acb4a | -7.82309 | -61.67017 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6b55c82-a08d-3834-aa15-12904768ed58 | -7.82254 | -61.67366 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d61e0906-e8ad-3256-bb64-5dd2921e4268 | -7.82031 | -61.66615 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 930f9e3d-daba-3db2-aee8-b8696c6c7dec | -7.81977 | -61.66965 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28930500-ae03-36fd-9eef-8dc25dfedb54 | -7.81922 | -61.67314 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d40c8f79-9511-3576-bb5b-05fc39bbb775 | -7.81699 | -61.66563 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 19177ae7-3b53-3108-816f-854372932c1c | -7.81645 | -61.66913 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 66b7d8dc-401f-37b9-9d31-62537d33778d | -7.6401 | -61.53748 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 701cd5f5-721d-38b6-8112-1f2a7b9f49ac | -7.5976 | -61.59178 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9203109-0750-3610-97d3-e639ff802d09 | -7.56935 | -61.57661 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95d4565b-e647-3b63-bb65-f7f243183860 | -7.56711 | -61.56911 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5774e237-3403-36e3-bfa2-b33b2b873420 | -7.53478 | -61.38428 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d068df6c-e698-3cd2-abf7-3439dbc80c0d | -7.53424 | -61.38779 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cb5b30c2-1a08-3f67-a616-649ecccbad2a | -7.53255 | -61.37673 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 758224eb-8f82-3060-ad65-0f62d73e0be5 | -7.532 | -61.38024 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e499cedc-4d50-3b45-9534-0259dab8ad4d | -7.53145 | -61.38376 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d09cf51e-8556-3860-adbd-7012bd79f58b | -7.53091 | -61.38728 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ddbfda29-4598-396d-8b75-a928615c6d6f | -7.52922 | -61.37621 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7f8a6991-05c1-32d3-b333-dea02222f3c5 | -7.52867 | -61.37972 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a1430968-0396-3129-a861-9e72c225ab6c | -7.52812 | -61.38324 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6772849f-da3e-3ab4-9880-2e3e60d0e6ab | -7.52589 | -61.37569 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e6ab9485-267b-31fd-8d24-80eea6551bf9 | -7.52565 | -61.50861 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92d5686c-808a-3854-ac3e-f51cfebd5569 | -7.52534 | -61.37921 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 501c50dc-151b-3b66-87bf-b0d29f046d5a | -7.52287 | -61.50459 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aa490cbd-73fc-3274-99fd-1e8f44dc4291 | -7.52233 | -61.50809 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ef8d98a0-7c85-3aa6-9701-1782778a47d3 | -7.519 | -61.50757 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 745fdb91-80a3-3987-bf9e-7d91c1eab4d5 | -7.51737 | -61.51806 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da3a7104-7c70-33ae-b6d5-bd2f608fbdb4 | -7.51459 | -61.51404 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 99b759e0-3436-31fe-995c-3255b3cfade3 | -7.42547 | -61.41109 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68342031-0437-3ed0-99fd-f0fc61b4260f | -8.0058 | -61.21507 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61cf8e00-530d-3237-a746-fdbd6d774406 | -8.00525 | -61.21862 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f800f60c-5cff-3091-8f3c-9805d32bc6eb | -8.0047 | -61.22218 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d0ca44a-f8bb-3fe3-a8e7-50e23ee75a9b | -8.0019 | -61.21811 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dafa2796-61e4-3af5-b906-5dbf9c0430db | -8.00135 | -61.22166 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54d64cc2-cd92-3a45-aaeb-1c8dac37cfd3 | -7.99855 | -61.21759 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4307c6d5-a2f9-33b8-a67d-47822dfe5104 | -7.998 | -61.22115 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71c08813-1ddb-3f07-aa22-1058acaa45ef | -7.99745 | -61.2247 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 847e8bb2-9d00-3970-8482-fd60fa5a2b31 | -7.9952 | -61.21708 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7659069e-f075-3312-8a48-8ab4f15b78cf | -7.99466 | -61.22064 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| adf1cfd6-4a13-3262-be8c-e8dc8f61ca30 | -7.9941 | -61.22418 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc808e40-0972-3153-be91-11a6f03ce1a7 | -7.99356 | -61.22773 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8c38e9f-2cd3-3eb6-a687-346e9454f48a | -7.99186 | -61.21658 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a4962b1-9532-33bd-ab1f-f681004aedc6 | -7.99131 | -61.22013 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e64c622d-8596-3e17-8015-88f82224b3a5 | -7.99076 | -61.22367 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87d8c68e-6080-3f1e-b439-823e7804bc41 | -7.99021 | -61.22722 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f253779e-a829-3752-8edc-f60eae63580d | -7.30515 | -61.08886 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45104d69-15f4-3ceb-a768-45b5d912fb00 | -7.3046 | -61.0924 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75c7a009-3bdf-31ef-8602-ec6f2b32e10e | -7.30406 | -61.09595 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6922ee0-17c8-37ef-b6f3-666632aef9d0 | -7.30235 | -61.08479 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e0e29e50-5f70-3b6e-b0c9-540116b859fe | -7.3018 | -61.08834 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10c72a01-67c4-315f-8189-657cff9f21a2 | -7.30126 | -61.09188 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b57fee3d-ce60-39a0-aa2d-6e8f39d1d25d | -7.30071 | -61.09543 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1a239de-47f2-3b74-bcf7-b184c70206a8 | -7.29846 | -61.08782 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1fd0e57-70be-319c-85ba-da8239ed529f | -7.29791 | -61.09136 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38db4622-5d56-322b-b4ad-d084fa52154e | -7.29457 | -61.09084 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d1521c2-7340-3fc9-90c4-bba556442041 | -7.29068 | -61.09387 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b3a115fb-5ea2-35cc-8a3c-13580467c3d8 | -7.28733 | -61.09335 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e64417b-23b0-37e5-bc94-023e12bbda97 | -7.28399 | -61.09283 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c49cffb-2e9c-3f7b-9664-2418acca72ad | -7.28167 | -61.09259 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea4d0cd4-5459-334f-ae8d-4ac881e113e7 | -7.28112 | -61.09613 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| faa9fbe3-8443-3883-8540-048ebe87d9cf | -7.00763 | -60.6923 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4426c965-d5dd-30a3-ba6e-624db20df704 | -7.00594 | -60.68097 | 2024-09-27 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README123.md)
