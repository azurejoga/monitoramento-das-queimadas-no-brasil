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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 854f23e5-a116-3b44-a386-02a001c6b849 | -2.53696 | -46.39726 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f86cb16-a38c-31ff-9107-f96285e23333 | -1.13288 | -54.17336 | 2024-11-25 04:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0fa356a-dca8-395c-8f24-4150140f9eff | -5.57097 | -50.94797 | 2024-11-25 04:33:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bca9818b-8bda-3670-95ab-0675d295d6a9 | -6.05602 | -44.04227 | 2024-11-25 04:33:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 51d73d08-4355-367c-8a68-5eb36819251f | -3.78911 | -49.85117 | 2024-11-25 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 023abde8-56a9-3896-9515-60fe3fa0fc80 | -4.2464 | -47.99912 | 2024-11-25 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82473800-fe82-3b8f-ad4a-28568754ae09 | -2.6645 | -46.60563 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8c4734a-2a86-38d6-b945-a158f75b9bbf | -3.25147 | -53.27309 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7506a93-b4d7-3ee6-91e0-d260df6c30d8 | -1.78444 | -52.73966 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 39045aac-321e-3c8f-a65a-db61c5b42ddd | -4.29834 | -46.90225 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| caeaf7ce-36db-37e1-b416-3629ee37518d | -2.62369 | -46.21013 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c8fa2fb-b242-3900-81b3-3fb5712a4f09 | -4.09352 | -46.84174 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c5feab9-7bcd-31a9-a703-b62a9d8937fa | -2.14194 | -52.08873 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 425781e3-e96f-3787-a6d6-90d0dd0b3c44 | -3.53998 | -50.45613 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 556f4798-97ae-3bec-a78f-57232346ebd1 | -3.19187 | -46.36262 | 2024-11-25 04:33:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9fb71ab-9b6a-359f-b7aa-837540d8e5eb | -4.20324 | -48.1232 | 2024-11-25 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a453e56d-a70c-3484-820a-fbfa11392deb | -4.29394 | -46.90872 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d480745d-cf99-3cfd-bb8e-86f8f5cce1c4 | -3.53514 | -54.49432 | 2024-11-25 04:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 455159dc-6bff-31dd-b9cf-1946fadbcf72 | -4.24898 | -49.19197 | 2024-11-25 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0981f907-a277-3cbf-8f95-97b7fcde629d | -2.71073 | -46.11186 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16c00674-92fe-3d25-bfaa-0e95c0d05808 | -3.25453 | -46.4187 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 257556b4-e0a0-38f1-a980-f2e824f4d2d8 | -2.07755 | -47.88154 | 2024-11-25 04:33:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c5c97c9b-43e7-3f1e-8259-b76297eac9f3 | -4.33555 | -46.00141 | 2024-11-25 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df15da14-0f2c-30ac-921c-2a4dae0f7f76 | -3.18865 | -46.55878 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a984692-507a-3504-a1e9-6efe978b5c0b | -4.63111 | -42.91634 | 2024-11-25 04:33:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 51982b98-3ed1-34a4-9dda-d5ed85cb37f3 | -3.61433 | -54.21675 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca836495-a45e-3028-adec-71b40e635d46 | -2.58578 | -46.5433 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c56ca81a-18fc-35a3-b07d-527f1e94be38 | -3.15171 | -44.26836 | 2024-11-25 04:33:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc37784d-7515-3244-884b-b987eb5ef527 | -3.12302 | -53.10356 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e613889-4b13-3db4-a6a0-064414945895 | -4.57942 | -40.77318 | 2024-11-25 04:33:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a93967a6-0412-3e0e-bba0-7582c8e1ddba | -1.4376 | -52.44411 | 2024-11-25 04:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e591b67d-4801-31da-8fb0-090ef08dc975 | -2.62703 | -46.21065 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 17ed36c8-a734-3f0f-8090-c248f76c9ee1 | -3.26883 | -53.82551 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ca7ec8e-426f-3489-bb5d-380e23e5e9dd | -2.58039 | -53.96316 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5dbcd755-84a7-3681-88c4-ece0ce9ff5c2 | -3.23023 | -46.44362 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24c3785a-85dc-329b-be78-344a5b01d9c7 | -5.66157 | -49.95783 | 2024-11-25 04:33:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| deab1400-d5ef-3d9d-9246-2b71c4d54f99 | -3.96429 | -46.90725 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 514f40e2-93b8-3bba-af46-8c3c21b43c61 | -3.40887 | -50.32032 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3f7abbce-2aac-3b9f-a721-22ec5a5d8dfb | -3.42377 | -53.28339 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0c88626e-6a12-3bd1-a697-b1edc442e654 | -3.94576 | -46.71944 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a008b98-5f4b-3574-bbaf-a2e053b3ce1b | -2.7349 | -46.10516 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bf2abdf-6194-36d4-8df6-284d97ed82dd | -1.61425 | -52.36086 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 60f9056d-deb6-351a-bfbb-21d88c06819d | -4.24353 | -48.66837 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0e877804-ee78-3918-89b5-4dcd14aa3c2d | -3.70951 | -52.41703 | 2024-11-25 04:33:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4df8ed44-dfd7-38fa-b224-da08ada2c0cc | -3.12365 | -53.0996 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3cbfab6-2e2d-3ea7-86f1-183d1e590a9d | -2.80589 | -46.81128 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eed99281-8172-3395-83b2-583790a56f81 | -3.70662 | -54.39384 | 2024-11-25 04:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee338b1c-7585-3271-a3d3-3c85e2f080c2 | -5.98517 | -46.34014 | 2024-11-25 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02d1e9a3-e875-32b8-baf0-2330ff7995f7 | -4.05593 | -46.84313 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2583c02e-aad2-3997-8e8a-f771fe770753 | -2.9289 | -53.0699 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ef0e60b-e3b7-374a-8460-0cc106d88ca2 | -4.21536 | -50.40414 | 2024-11-25 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a31f43ec-7ebf-3e0b-8d0f-1c31663f7363 | -6.64902 | -43.59011 | 2024-11-25 04:33:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f02d82d7-1bb4-3bb6-9e07-cd2da4dfe26a | -3.77256 | -46.67443 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a2db705-a04f-3f29-8614-929e142b1ccb | -3.5126 | -53.82677 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 829b5aec-9b24-3e42-9d70-49ed2762af8e | -4.19829 | -50.68734 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3dd82c77-34c9-398c-a415-c8dcaf1e6ebf | -1.62853 | -54.46418 | 2024-11-25 04:33:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b944fcd9-7e97-34cd-964d-e8567ea526ac | -4.01716 | -46.19585 | 2024-11-25 04:33:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f2a8249-a794-3f5f-9dfc-3e1ea4c40d3a | -3.10083 | -54.00491 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e1710b0-1e20-38a0-8975-d2f082b71d63 | -2.13668 | -52.27585 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eae5c996-b8b9-3f42-9a94-29c5c9cf0272 | -4.56849 | -46.29477 | 2024-11-25 04:33:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 646639f9-e501-31ca-b8be-d8c25daac2b9 | -3.93399 | -49.89288 | 2024-11-25 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98f55fa9-48e2-3e2a-9d6b-b274fe5c7a94 | -2.65108 | -46.2538 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5e4699b-a104-3bed-b8e8-72f11f17ed04 | -4.01616 | -48.07931 | 2024-11-25 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9edff43c-f5cc-3597-844e-13f6b85b4580 | -2.32846 | -53.86661 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a0dfd00c-ba03-3382-aeff-b50d7c607d3d | -3.23928 | -54.22998 | 2024-11-25 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75158242-5687-34fe-8560-2b6fbc25509a | -2.59054 | -54.05272 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 13ea954d-f116-3969-959b-f7992981edee | -1.97798 | -56.14125 | 2024-11-25 04:33:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f8f31381-4093-3371-b84b-6422fef35c68 | -4.30991 | -45.89691 | 2024-11-25 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 63869a9d-5602-3939-a2b3-a2aa25ea5c13 | -1.92072 | -53.00178 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d0ef7321-0473-33b1-8d8f-bee72000ea2c | -4.69899 | -45.8505 | 2024-11-25 04:33:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 848cfd8c-d526-3c7e-8114-739bab97a3c4 | -3.70963 | -51.77761 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a409f7f1-31fd-370c-8dbe-55ffc38428a3 | -3.26236 | -46.43422 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7a53da0-84bf-39ed-8be8-c42ba0106948 | -2.54639 | -46.40228 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| adadcb00-47a3-3412-a581-c4f063924bde | -2.58392 | -45.3261 | 2024-11-25 04:33:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b860cabf-e80e-3a37-b508-c1b6c530806b | -3.34873 | -50.51143 | 2024-11-25 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc1b58ab-dc58-3213-bef4-e8dee6904d18 | -2.45924 | -46.28536 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ac91997e-242b-362a-8588-002ffdee53a7 | -2.58641 | -46.56113 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 775649e0-4ccb-3590-9513-45bf628019bd | -2.71379 | -46.24237 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 957ac2d2-7db0-3e38-b512-2f778a482b92 | -1.18725 | -53.88371 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 09e49e07-c512-3cb0-b905-31fda8bac92f | -2.17567 | -52.08334 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d0c38cc-1322-3924-aef5-cc5a16fdaa9f | -3.87255 | -52.20967 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 404f2248-a35c-3b3c-9e8f-e9c98819b01b | -4.25861 | -48.72484 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9aa8b23a-2e1f-39fe-8d14-ee3da2304414 | -4.20171 | -50.23953 | 2024-11-25 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eeb58964-0275-3eb1-b32f-096594edbc7d | -2.733 | -46.10083 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 890031e2-ad0f-3437-b347-08ca4ba4209c | -4.64301 | -47.26789 | 2024-11-25 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3b531f1-ea8e-3774-afb5-601d768f0620 | -2.90055 | -51.77304 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9005abef-3e5a-38b0-9932-5a5bdd4efd12 | -4.26414 | -48.68958 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a51b4b1-4b7f-3073-8ab8-ea588da913c5 | -2.17622 | -52.07987 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1c99a20-638a-3d93-9ae2-03c069b983af | -1.56885 | -52.01142 | 2024-11-25 04:33:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32a732b3-9d9a-3e98-a641-b2d80a6c0330 | -4.03916 | -46.66597 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5620b88c-2997-3756-a0d5-625c9e61b7f5 | -2.85692 | -53.97446 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 260f4d62-caa1-3b5d-94d6-c4c9fd9f0e01 | -3.23063 | -46.31104 | 2024-11-25 04:33:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e26414e-402b-32d6-a234-de35f343d5ec | -2.6637 | -46.54464 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4099570-24b9-37c1-b38a-6d54ac66ed24 | -3.47238 | -47.68712 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9ffcc1c2-fd63-3897-b74b-1f9629c6b31d | -3.71731 | -51.77885 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 193a5d33-6b31-3649-9533-fe3739dc991d | -4.25688 | -48.67045 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 63effa71-a452-3de9-847d-0d9b7275b396 | -1.77283 | -53.62389 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fa157c19-36cb-3360-a0eb-9ab47cc0486d | -2.80274 | -53.01802 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97fb4d00-4d78-30f0-bcf1-d69b9fe17a1c | -2.69758 | -46.19631 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0f0cc87-e15d-3524-a69c-2c11d5bdfe84 | -2.9067 | -51.70915 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README29.md)
