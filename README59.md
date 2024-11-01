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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f16d767-b3c6-3ba2-a451-a751d5373845 | -1.4244 | -52.2118 | 2024-11-01 13:05:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| b734e503-8006-3d5c-8477-040174afd850 | -2.2931 | -50.6668 | 2024-11-01 13:05:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 259.9 |
| 9c6c738d-ed5f-31d2-bc94-af8a6d35774d | -2.836 | -48.4501 | 2024-11-01 13:05:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 7f644a70-7e87-37ad-a8dc-ab187a97439f | -3.0353 | -49.4901 | 2024-11-01 13:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| b419dd21-6b60-3a03-85ec-59779df5411d | -3.0354 | -49.4688 | 2024-11-01 13:05:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 4fadf675-a4db-3770-977c-dede1b57031a | -3.272 | -50.3263 | 2024-11-01 13:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| b2923abb-78ca-319f-ab2f-4c04cf7b43c3 | -3.2535 | -50.3479 | 2024-11-01 13:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| bc12b385-ad5e-3517-b67c-eea8a5bfbf84 | -4.2964 | -45.8491 | 2024-11-01 13:05:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 88.3 |
| f12c9c6b-212e-3f1e-bf8f-1f9dd7e6e8de | -4.3867 | -43.4757 | 2024-11-01 13:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 291.7 |
| 3ba3b606-87cd-3f43-96c2-08ea9348f852 | -4.3866 | -43.4989 | 2024-11-01 13:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| fe226cd1-feae-37f3-8645-c935c6b264b4 | -4.4387 | -46.8624 | 2024-11-01 13:05:31 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 2b476bd6-00c4-30ab-aa9c-3711e365dfc1 | -4.4054 | -43.4746 | 2024-11-01 13:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 236.4 |
| 2571390f-afef-39e7-bbed-27e1817d931e | -4.4056 | -43.4514 | 2024-11-01 13:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 84f6d424-53ff-3f63-831e-8b17a4356d40 | -4.3869 | -43.4525 | 2024-11-01 13:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 5683db16-bba0-38d9-8a60-dd81690c2918 | -4.7373 | -44.0786 | 2024-11-01 13:05:33 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 9c882279-d4ee-381e-8243-a98e14ade613 | -5.4742 | -43.1711 | 2024-11-01 13:05:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| b60b7261-a983-36a7-a852-127477c27bb0 | -5.4546 | -43.2659 | 2024-11-01 13:05:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 6a3f3cab-117b-32f2-92ea-8ddd3c551c47 | -5.4548 | -43.2426 | 2024-11-01 13:05:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 5c6a920b-f560-3b1f-b853-9711daf319b3 | -5.455 | -43.2192 | 2024-11-01 13:05:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 0d3250f9-c45a-3c28-8490-b70bda4ee93e | -16.9008 | -57.5313 | 2024-11-01 13:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 120.5 |
| 180ae77a-64af-3e60-ab24-cd917ce57809 | -16.9012 | -57.5108 | 2024-11-01 13:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.0 |
| a61cd13a-2c42-3723-9fef-6affb018a8ff | 3.4157 | -51.2606 | 2024-11-01 13:14:46 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 65.3 |
| d0d5a2b9-1ced-359d-9ac4-0f5df32da3be | -1.4426 | -52.273 | 2024-11-01 13:15:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 8e84825e-b1c9-32df-bee0-16e18a1f2dd8 | -1.4244 | -52.1913 | 2024-11-01 13:15:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 2e28537a-f711-34f2-96f3-1ee8420f0ede | -1.4244 | -52.2118 | 2024-11-01 13:15:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 9f5d3096-17b6-3654-adb5-0c21295bcfd2 | -2.2931 | -50.6668 | 2024-11-01 13:15:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 199.1 |
| 3329aac8-8bac-3573-b104-e20f2f5563a9 | -2.8361 | -48.4286 | 2024-11-01 13:15:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| f1d8af16-83fa-307a-87a8-0dca4d3dd35a | -2.836 | -48.4501 | 2024-11-01 13:15:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 202.1 |
| 4099c92e-3284-3e29-abfb-fea9b6edb72d | -2.8175 | -48.4506 | 2024-11-01 13:15:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 989ef452-1ab2-3048-ade6-77c4cbbcc60b | -3.0354 | -49.4688 | 2024-11-01 13:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| a2db087d-ef03-387e-b9ce-f7f677d4bac1 | -3.0353 | -49.4901 | 2024-11-01 13:15:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 69252564-21bc-3e1d-a8fa-de7947d29f06 | -3.2719 | -50.3473 | 2024-11-01 13:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 6d0ee4b0-a9ee-33c0-b913-7d64dd2f45d4 | -3.2535 | -50.3479 | 2024-11-01 13:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 510d0813-18eb-3851-b666-d0acf25f67c9 | -3.272 | -50.3263 | 2024-11-01 13:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| ae6e00f0-6c76-3a89-84b6-cee813d47298 | -3.5762 | -44.8935 | 2024-11-01 13:15:26 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 78.6 |
| b77c4c8c-3c55-34c0-972f-2fb89a2f463c | -3.8413 | -44.1283 | 2024-11-01 13:15:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| d63bf03b-e988-352a-8ff3-44de42c89203 | -3.819 | -44.746 | 2024-11-01 13:15:28 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 3bd6aea1-04d0-372f-b129-7901590e9bb3 | -4.3157 | -45.7362 | 2024-11-01 13:15:31 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 70.9 |
| e2099d49-1223-3349-9ffa-d7617de67a5c | -4.4056 | -43.4514 | 2024-11-01 13:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 5dab2a3a-357b-3e00-a1e1-c20c99d2ae7d | -4.4387 | -46.8624 | 2024-11-01 13:15:31 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 174.6 |
| bfbd1614-979c-30e1-9d77-24619fb3dd24 | -4.3867 | -43.4757 | 2024-11-01 13:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 145.1 |
| d602c998-2a97-3cab-9ea5-1b5f04d72126 | -4.7373 | -44.0786 | 2024-11-01 13:15:33 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| b08412ba-73b4-3da5-8aa4-7f6c039bb678 | -5.4554 | -43.1725 | 2024-11-01 13:15:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 0b431860-9b2c-3ca2-a63d-82080ae013e6 | -5.4546 | -43.2659 | 2024-11-01 13:15:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| dea224aa-9637-3dd6-8c47-a304e6ed3399 | -5.4548 | -43.2426 | 2024-11-01 13:15:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 8c7cd5f7-2ba0-3028-813c-a5e11cb2397b | -5.4742 | -43.1711 | 2024-11-01 13:15:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 4aaed188-9167-33a7-9e86-49b993bca4cd | -5.455 | -43.2192 | 2024-11-01 13:15:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 271400b1-606d-3431-8b4a-a369de38d79a | 3.4157 | -51.2606 | 2024-11-01 13:24:46 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 0169ac68-3327-3543-8155-1e8aaced25a8 | -1.4244 | -52.1913 | 2024-11-01 13:25:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 699061e9-29c3-37f0-8cd7-33f025b9415f | -1.4244 | -52.2118 | 2024-11-01 13:25:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 970ed09a-c045-37dc-9fc5-0d9d1612c664 | -2.466 | -48.5035 | 2024-11-01 13:25:20 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| b90f3953-aa14-361a-a4ab-c8117a698b41 | -2.8175 | -48.4506 | 2024-11-01 13:25:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 83839118-5f32-34e6-9373-3d73f86842e5 | -2.8176 | -48.4291 | 2024-11-01 13:25:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 747b55da-8425-3427-9c84-3fc0166aa899 | -2.8545 | -48.4495 | 2024-11-01 13:25:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 63df4b32-d432-375b-9bb9-64eb8f20a5c5 | -2.836 | -48.4501 | 2024-11-01 13:25:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 357.9 |
| dbdeb7e0-08a6-3d97-888d-74d2cc88a187 | -2.8361 | -48.4286 | 2024-11-01 13:25:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 256.7 |
| 715900cf-db22-3b89-8c09-61836600a097 | -3.0354 | -49.4688 | 2024-11-01 13:25:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| b0242d07-5034-3e22-b6d0-7e39efb15f7b | -3.2535 | -50.3269 | 2024-11-01 13:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| d44185e8-ea33-3a6b-9f99-6689a98e90d4 | -3.272 | -50.3263 | 2024-11-01 13:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 81509d01-1dbd-3d82-9fe0-1069bb1e322a | -3.2535 | -50.3479 | 2024-11-01 13:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| ee46fc2c-441f-315f-84b0-6fb27eb17109 | -3.3891 | -41.6201 | 2024-11-01 13:25:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 79.7 |
| eb9db9a5-f26b-3312-a706-a3eae7bfb03c | -3.5762 | -44.8935 | 2024-11-01 13:25:26 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 153.0 |
| 3fad1dac-5a24-317d-8f8d-7a1a3139b153 | -3.8412 | -44.1513 | 2024-11-01 13:25:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 4917dc54-b6ab-3960-918f-e89ab480714f | -3.8413 | -44.1283 | 2024-11-01 13:25:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 41d1590c-9528-337c-901a-0ca6895cd186 | -4.4573 | -46.8615 | 2024-11-01 13:25:31 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 70.8 |
| d8112c22-3bb3-3b5f-b1ad-48f1d38f76d6 | -4.3869 | -43.4525 | 2024-11-01 13:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 6e27d446-8aa5-324e-a379-dce3b4ec9c76 | -4.3867 | -43.4757 | 2024-11-01 13:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 265.7 |
| b535b17a-faa9-3215-b7ad-d3421de43718 | -4.4387 | -46.8624 | 2024-11-01 13:25:31 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 240.0 |
| f5d56106-756b-319a-a508-ea70985bcbd7 | -4.4056 | -43.4514 | 2024-11-01 13:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 109.5 |
| d18314f1-a9f9-3036-8458-e9de050f5d71 | -4.5015 | -45.7935 | 2024-11-01 13:25:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 997036d2-4b26-3841-91d2-08a0c78b2768 | -4.6349 | -45.3594 | 2024-11-01 13:25:32 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 882da7f5-4e44-30df-a03f-6dbdf838da60 | -4.7373 | -44.0786 | 2024-11-01 13:25:33 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| ab5b37c9-99a7-38ae-9940-d6c95a3560c4 | -5.4742 | -43.1711 | 2024-11-01 13:25:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 115.7 |
| c1e028c4-6391-3548-ad73-90752ba26e23 | -5.4554 | -43.1725 | 2024-11-01 13:25:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 34f9eb88-c1f4-38bf-a57a-435ae67f89ca | 3.4342 | -51.2601 | 2024-11-01 13:34:46 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 8b559ef8-2702-3291-a517-f1554a3ca095 | -1.4244 | -52.1913 | 2024-11-01 13:35:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 8efdb7b6-6228-3c44-be6e-7fbffdd3b193 | -1.4244 | -52.2118 | 2024-11-01 13:35:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 7bb5c4b9-582b-3db6-b272-9a17fbc90f07 | -2.2685 | -46.6601 | 2024-11-01 13:35:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 282888dd-b714-386a-907f-a7fc3e491dc3 | -2.2499 | -46.6606 | 2024-11-01 13:35:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| fca93984-c73e-3d57-9889-ad2ef3cc9024 | -2.466 | -48.5035 | 2024-11-01 13:35:20 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| a890554f-d973-3bf0-9ed2-3d6f97155763 | -2.836 | -48.4501 | 2024-11-01 13:35:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 332.4 |
| 2bea9739-fa90-3e5f-84ac-6df35a005082 | -2.7961 | -49.2211 | 2024-11-01 13:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 4bbc33e4-0218-3f8b-8ce8-cf988817cd75 | -2.8361 | -48.4286 | 2024-11-01 13:35:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 155.6 |
| 8e90b51f-ef44-3b4c-9718-b27d5c55c559 | -2.8175 | -48.4506 | 2024-11-01 13:35:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 138.8 |
| b3a77f0a-1181-3388-9cfc-6c0306c1e886 | -2.8176 | -48.4291 | 2024-11-01 13:35:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 2923182d-1ecf-323a-a85f-a49412a6c1d7 | -3.0538 | -49.4895 | 2024-11-01 13:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| d2cbed06-5ad5-371b-9c11-79b494054002 | -3.2535 | -50.3479 | 2024-11-01 13:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| a9f63cd6-e7da-37a0-87f6-250c3c025885 | -3.4078 | -41.6192 | 2024-11-01 13:35:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |
| 9c6de69e-8106-3553-8d3e-ba3c3371ddf1 | -3.2535 | -50.3269 | 2024-11-01 13:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 18a7f6bb-24b2-3f60-8ea2-c60f8f0c2f8f | -3.3341 | -41.4069 | 2024-11-01 13:35:25 | GOES-16 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 7e7d9c13-c06a-3ed5-92f5-26aebf8cc42c | -3.2231 | -53.3972 | 2024-11-01 13:35:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| ebd7ce01-a70e-35a1-8cc5-ef73527c5292 | -3.4076 | -41.6432 | 2024-11-01 13:35:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 106.6 |
| a094d450-0883-39f6-9d20-87112b6e181e | -3.3891 | -41.6201 | 2024-11-01 13:35:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 95.3 |
| 23d04173-c62e-3fd0-a5b1-e3c1e0da2a16 | -3.272 | -50.3263 | 2024-11-01 13:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 0617c223-3e98-3398-a7ac-bbaedf370c43 | -3.5762 | -44.8935 | 2024-11-01 13:35:26 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 255.3 |
| 460a3312-94e7-3cce-b13f-a494d086e406 | -3.9511 | -41.5186 | 2024-11-01 13:35:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 95.9 |
| d70669be-dc36-3336-bb6f-65a6e135f0ab | -3.819 | -44.746 | 2024-11-01 13:35:28 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 67.8 |
| daf82311-eb28-34d4-a702-759ba4c7bc4c | -4.4387 | -46.8624 | 2024-11-01 13:35:31 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 1ca72d58-700c-31c7-87b2-9cd7449f5f0a | -4.3867 | -43.4757 | 2024-11-01 13:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 172.9 |
| ebcf6c6c-48a3-338a-bf39-63bc57e52b3f | -4.4056 | -43.4514 | 2024-11-01 13:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |


[Clique aqui para ver as próximas entradas](README60.md)
