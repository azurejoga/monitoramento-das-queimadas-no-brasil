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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebc0ebf9-e91c-3d17-94a7-de6c796fe8db | -3.2299 | -43.4414 | 2025-11-05 13:00:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| a84c55d8-2d6a-3966-b59f-fa97eca3225a | -5.9234 | -41.3056 | 2025-11-05 13:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 116.6 |
| 205d1b32-7d07-3b9c-82c3-1259ae8edc34 | -4.4632 | -43.2386 | 2025-11-05 13:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 64f09d6b-dc03-3006-b481-ffdb9768bf8e | -19.0519 | -57.5356 | 2025-11-05 13:00:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 120.8 |
| bf37b9c5-60c3-38bd-9538-94c4702be97a | -6.3635 | -42.4163 | 2025-11-05 13:00:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 74.8 |
| b855899e-1c26-3f13-a891-83440002abe3 | -6.0735 | -43.2414 | 2025-11-05 13:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 124.0 |
| 76934342-ad5e-32ff-9c61-a36cd12d1309 | -6.1271 | -41.6253 | 2025-11-05 13:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |
| 32b9a75c-a22b-3342-af06-5e21aaf9c298 | -6.456 | -39.1091 | 2025-11-05 13:10:00 | GOES-19 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 106.1 |
| d45ad875-06f8-32a5-86bf-27f3deff8d8e | -6.0733 | -43.2648 | 2025-11-05 13:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 168.5 |
| 2ddefe64-ffa0-392d-a8f9-f64bce8db0ad | -19.0519 | -57.5356 | 2025-11-05 13:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 125.9 |
| f6a89c14-b860-3838-973a-4f3bf2f6505c | -4.4445 | -43.2397 | 2025-11-05 13:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| e8dfeda8-9a80-34c3-8d52-aabc51211db9 | -4.4632 | -43.2386 | 2025-11-05 13:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 8496fcbe-840b-3e50-87f0-165724445984 | -6.0735 | -43.2414 | 2025-11-05 13:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 143.3 |
| 9486e441-cbe5-3e90-b550-c14552697531 | -4.5934 | -43.3239 | 2025-11-05 13:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| cf483664-2b3f-3417-9996-86e02d376754 | -6.456 | -39.1091 | 2025-11-05 13:20:00 | GOES-19 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 152.4 |
| dfd345ab-3343-3798-b8e8-f44501b98f64 | -6.0735 | -43.2414 | 2025-11-05 13:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 155.9 |
| dfd1807f-f9f6-3531-aef7-1826f6b29931 | -4.2913 | -43.7822 | 2025-11-05 13:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 322515c2-4e42-39d9-86b8-6d99ef4015e2 | -19.0519 | -57.5356 | 2025-11-05 13:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 128.8 |
| 9587c945-846d-3aca-aad4-7b9b1e4e4292 | -4.3099 | -43.7811 | 2025-11-05 13:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| ad543fda-52c8-361c-aeee-c2201f998b52 | -6.0733 | -43.2648 | 2025-11-05 13:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 149.2 |
| 6b6eda91-f18d-311f-b183-1258954d2d69 | -7.1692 | -42.7435 | 2025-11-05 13:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 75.1 |
| 0ccff5cc-679e-3b6e-94d6-95c5eb7dab65 | -7.1695 | -42.7198 | 2025-11-05 13:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 70.8 |
| 8eb0af60-2c11-36ff-9981-e1b078f2f5b0 | -6.1271 | -41.6253 | 2025-11-05 13:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |
| 302ed973-8306-32bc-aa73-dde90d94adf8 | -6.0461 | -44.1484 | 2025-11-05 13:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 775e0a96-e215-3cec-a581-9665224f0d2a | -4.4445 | -43.2397 | 2025-11-05 13:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 89bda814-7a4a-3dd7-8ba6-1011d4ac0b27 | -5.0143 | -49.706 | 2025-11-05 13:20:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| b423f008-296f-3859-b408-1e296d7fe996 | -3.3135 | -53.839 | 2025-11-05 13:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| a7b9da2c-e197-3e8f-b8ef-1a0c5f7d3411 | -5.9236 | -41.2814 | 2025-11-05 13:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 113.4 |
| f4d6fb29-2a3e-348e-bff6-81a4397cdb1f | -6.0735 | -43.2414 | 2025-11-05 13:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 137.4 |
| ecbd15e9-5ac1-315a-8c4c-58f0890890ae | -19.0519 | -57.5356 | 2025-11-05 13:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 127.5 |
| 9b45acea-4c00-301a-8b13-4956c8e74a0e | -1.2084 | -49.1689 | 2025-11-05 13:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| c4930cbb-da29-3bea-866e-c376a2922b22 | -4.2911 | -43.8053 | 2025-11-05 13:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| e6498e95-9d11-3c80-8f27-e25b9b049942 | -6.0733 | -43.2648 | 2025-11-05 13:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 154.8 |
| 559b2c2d-6ede-3466-9da5-944899292d44 | -6.456 | -39.1091 | 2025-11-05 13:30:00 | GOES-19 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 135.2 |
| fa461781-15ff-335a-a3ee-de78cfe030ac | -4.2913 | -43.7822 | 2025-11-05 13:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 200.3 |
| 1ec1074d-6408-3588-9406-bb07953baa9e | -6.1271 | -41.6253 | 2025-11-05 13:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| 785800af-a783-384b-b12c-a5c6d96e9271 | -4.4445 | -43.2397 | 2025-11-05 13:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 72f28803-d681-3f0d-b546-0a6e70f16478 | -5.9234 | -41.3056 | 2025-11-05 13:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 139.8 |
| 5120006b-07fe-39e7-9739-bf69b51d845d | -4.3872 | -43.406 | 2025-11-05 13:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 9762fa85-d75b-3fd0-a7a5-533351bb77f5 | -4.5934 | -43.3239 | 2025-11-05 13:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 7c7d5ec0-6623-3f68-ade4-79300f6da742 | -4.482 | -43.2141 | 2025-11-05 13:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 70309be3-f056-3263-90d3-616050eab4df | -4.3098 | -43.8042 | 2025-11-05 13:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 9fe5125f-448b-36c1-bf2a-be40be9db9a0 | -19.0323 | -57.5174 | 2025-11-05 13:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 123.3 |
| 491999bc-9db9-376c-bb01-e96817800cf8 | -6.1083 | -41.627 | 2025-11-05 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 97.6 |
| b33c4346-9e75-3e79-994d-4668c028c3c2 | -3.3135 | -53.839 | 2025-11-05 13:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 7c5135ed-b267-3fa7-9313-b196ba511d2a | -19.0323 | -57.5174 | 2025-11-05 13:40:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 118.8 |
| 79ff98c5-0053-3b82-84f9-c796aabdfed9 | -4.4445 | -43.2397 | 2025-11-05 13:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 11097844-57ea-38c3-a042-544c8ec084a1 | -6.1834 | -41.6444 | 2025-11-05 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 82.7 |
| ee9e9ec6-9449-3fbe-b74b-3142f88ab6dd | -3.2299 | -43.4414 | 2025-11-05 13:40:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 67c2ab7d-3a68-3adc-a4db-e4dd9c18d712 | -6.0735 | -43.2414 | 2025-11-05 13:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 169.9 |
| 616d0cbb-aace-3afd-b44d-9d93c88f49ea | -6.1271 | -41.6253 | 2025-11-05 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 104.1 |
| e44c77ce-3c4c-31d8-a969-ddeef45bbd7f | -7.9507 | -45.1244 | 2025-11-05 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 42f0f753-07cd-3cd2-8cbd-e956a9c6708d | -1.2084 | -49.1476 | 2025-11-05 13:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 0c2cb3c9-c706-352a-b6ab-b61a8857306e | -4.3872 | -43.406 | 2025-11-05 13:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| d9051504-14e3-3edd-91d0-55aca941bb59 | -8.5908 | -43.7431 | 2025-11-05 13:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| d001e6d7-3dc2-30be-8b35-f6a9dff8785c | -4.2913 | -43.7822 | 2025-11-05 13:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 172.5 |
| 62eb00b0-08e6-3545-99aa-70b1f5a5c484 | -6.108 | -41.651 | 2025-11-05 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 91.5 |
| eb30314b-b4f3-3efa-a474-b577e084461e | -6.0461 | -44.1484 | 2025-11-05 13:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 121.0 |
| ebb60bfe-1120-3ab7-96f6-4d7b6a617e1b | -8.8556 | -41.1107 | 2025-11-05 13:40:00 | GOES-19 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 88.7 |
| 0a496570-c457-3266-8a88-2f461c925c97 | -4.482 | -43.2141 | 2025-11-05 13:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 0a6ab73c-bb06-325b-add7-c6a72da05381 | -6.1269 | -41.6494 | 2025-11-05 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 97.3 |
| 5535db3c-b4e2-3452-9363-8f52cbb2eb78 | -6.0733 | -43.2648 | 2025-11-05 13:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 169.1 |
| a0b4f732-98b0-3216-9f7d-512c0e022369 | -1.1899 | -49.1691 | 2025-11-05 13:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 80a3f4bc-c748-33a2-929f-233ce10fb911 | -6.6567 | -44.9462 | 2025-11-05 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 06b3efa0-9703-3d6c-ad73-822523d77d8b | -3.3135 | -53.839 | 2025-11-05 13:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 69e8500c-38bb-38fa-bf76-4adf4635ed7d | -4.5745 | -43.3483 | 2025-11-05 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 4c977700-78ca-3146-84a5-887b9c572acf | -4.2911 | -43.8053 | 2025-11-05 13:50:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 05eab011-7ca9-3ac2-a8e5-22af0d5642ae | -6.0733 | -43.2648 | 2025-11-05 13:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 181.9 |
| 9155b0a3-d3e0-3b22-aa34-b977a69211f4 | -6.1834 | -41.6444 | 2025-11-05 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 82.6 |
| 62f7912c-673a-3493-8511-0fca7ebedf21 | -19.0519 | -57.5356 | 2025-11-05 13:50:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 126.8 |
| 083954a7-291d-3605-994e-4dfa028009e6 | -6.701 | -40.8206 | 2025-11-05 13:50:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 81.9 |
| 649e73d9-4b2f-34d7-9bce-6f80f2262612 | -6.0735 | -43.2414 | 2025-11-05 13:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 161.1 |
| 452f1a47-b441-3245-925b-5c0cb6971326 | -6.1269 | -41.6494 | 2025-11-05 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 96.1 |
| 98b6f966-1e23-3047-b1d3-4e2cc0e7c1ea | -4.3872 | -43.406 | 2025-11-05 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| c9319919-2329-3ca7-885b-73035c7c2e5a | -6.0461 | -44.1484 | 2025-11-05 13:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 1332073e-e035-3c4c-b6eb-35ef33266f7e | -7.3134 | -44.9572 | 2025-11-05 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 9ffcad5a-7cf4-312d-ba48-c7cdd7cfde6e | -6.108 | -41.651 | 2025-11-05 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| 95815eca-d68b-308b-9395-44edaa24c073 | -5.9234 | -41.3056 | 2025-11-05 13:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 141.3 |
| 2f94ebc3-102a-34bf-854b-fb98ad56103e | -8.1386 | -42.2128 | 2025-11-05 13:50:00 | GOES-19 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 68.6 |
| c28d07e4-36b4-3ef8-98a4-9e7609788727 | -7.0695 | -44.9335 | 2025-11-05 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 06267205-cedf-35e0-b143-cdc278ed4e62 | -4.2913 | -43.7822 | 2025-11-05 13:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 221.6 |
| e67b1a88-f876-36c8-b18e-2fa8fc2105ef | -3.2299 | -43.4414 | 2025-11-05 13:50:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 02779d9a-5217-30f9-a10d-00bb6fb4bee5 | -6.1083 | -41.627 | 2025-11-05 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 75.5 |
| bd4b0e21-3ca2-3c72-bf95-11808ba8515e | -4.5934 | -43.3239 | 2025-11-05 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 8a9be353-bbed-300f-8dfe-4d7cd3729144 | -4.482 | -43.2141 | 2025-11-05 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 8d4308f7-fcc7-315b-9225-cf8f6342c8f1 | -6.1271 | -41.6253 | 2025-11-05 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 95.6 |
| 7fbeee96-bc2a-395f-b0d5-7d0b6523cbfc | -4.3098 | -43.8042 | 2025-11-05 13:50:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 7876845c-6c4a-33e9-8860-cc11e15dd4b4 | -4.4633 | -43.2152 | 2025-11-05 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 3f2025c8-73e0-3b91-8ebe-3034d8d3407d | -6.6567 | -44.9462 | 2025-11-05 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 87814b30-53da-30ec-a698-4effdddd949b | -4.0949 | -42.4152 | 2025-11-05 13:50:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 85.0 |
| 52a86c8e-d6f0-37f0-9dc4-b1e0350d999f | -7.9507 | -45.1244 | 2025-11-05 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 8e3a68e7-e28a-3fd5-87c1-c34e4f7561fa | -3.29 | -42.6448 | 2025-11-05 13:50:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| c2301947-98c8-32a4-b828-0dc88d6db954 | -19.0323 | -57.5174 | 2025-11-05 13:50:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 122.5 |
| 127c4e58-2dbf-35d9-a37b-87f1bba404c2 | -4.4054 | -43.4746 | 2025-11-05 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| d046e957-094f-3a49-af85-cdde10877c83 | -19.0519 | -57.5356 | 2025-11-05 14:00:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 122.2 |
| a63d27c2-a6e8-3f3e-a4bd-8da0d9efd2ff | -3.3135 | -53.839 | 2025-11-05 14:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| fb9ee368-f13b-398a-9922-93d8c042b1f3 | -7.1079 | -44.8617 | 2025-11-05 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| cb842efb-c147-3349-9e23-0bd22ed2b794 | -5.9043 | -43.2784 | 2025-11-05 14:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 81734c30-e8cb-32ee-b126-cb581637a923 | -4.4054 | -43.4746 | 2025-11-05 14:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| a7778bfb-0853-30dc-a311-6a7fbabca3d9 | -6.1269 | -41.6494 | 2025-11-05 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 93.7 |


[Clique aqui para ver as próximas entradas](README42.md)
