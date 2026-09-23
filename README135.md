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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1768b86-c40e-308c-a7d0-47b20fd76236 | -8.0921 | -44.3538 | 2026-09-23 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 4d521d3a-9cb9-3b50-a280-ce191ee27771 | -6.6129 | -43.7317 | 2026-09-23 13:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 338.6 |
| 360f0674-1602-3034-84aa-4165709066e5 | -7.1581 | -42.0792 | 2026-09-23 13:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| 109806e4-fcb5-31f8-b0ea-83581cff9412 | -6.5941 | -43.7333 | 2026-09-23 13:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| f034e090-68ea-3d50-89ae-4dde6569df52 | -6.1846 | -52.049 | 2026-09-23 13:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 82de9cb8-e711-3462-80b0-f8d52bfcd284 | -6.6127 | -43.7549 | 2026-09-23 13:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 7d90a83f-bf28-3b1d-aa78-88b9980c5089 | -7.4288 | -44.718 | 2026-09-23 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 1e9f9ba3-db2e-380a-9dd1-7f20c8757de1 | -9.5854 | -48.4549 | 2026-09-23 13:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 261.0 |
| 3a4f4eaa-9e30-3ec3-86fb-14c2eca33b27 | -7.0164 | -44.6413 | 2026-09-23 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |
| f6934521-0534-3202-bf2e-97821751f626 | -8.0923 | -44.3307 | 2026-09-23 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 133.2 |
| b9f07d28-33b9-349d-b217-8643a780ff46 | -11.3054 | -44.0198 | 2026-09-23 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 281a352d-6d2b-39db-8dcb-fd70b0259d6f | -11.3058 | -43.9963 | 2026-09-23 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 180.4 |
| ef3fdcb8-1129-37ec-9a12-d1530721d59e | -7.1395 | -42.0572 | 2026-09-23 13:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 85.5 |
| 7bc4f22b-dac4-3a59-800b-38c5929f4d89 | -6.6631 | -55.0512 | 2026-09-23 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| e9ebcfca-0306-3d9d-a9e5-d1f879540914 | -9.6043 | -48.4529 | 2026-09-23 13:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| f4952f9f-1925-34ac-8790-fc74fa62529a | -9.6111 | -43.9243 | 2026-09-23 13:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 98.6 |
| 9088bd87-e08b-3082-abf8-29f7efc6f91a | -11.4782 | -47.3529 | 2026-09-23 13:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 92b424eb-9cfb-3bd3-b88c-f24da8a0d324 | -7.1392 | -42.0811 | 2026-09-23 13:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 103.9 |
| b79b203d-8249-3d9d-960a-1a7827a4f777 | -8.9016 | -45.933 | 2026-09-23 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 286.0 |
| 8818b839-1db6-3142-a1b6-d68aff595cb5 | -6.2394 | -41.6875 | 2026-09-23 13:10:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 77.4 |
| 2a8abd69-3236-3b8f-9877-98528084c41a | -7.41 | -44.7198 | 2026-09-23 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 64.9 |
| ca047347-de4a-3248-ba3c-0d2e32821759 | -7.1277 | -43.0774 | 2026-09-23 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.9 |
| 8f8f222c-3004-3c7f-b608-91c7e623599f | -7.0349 | -44.6625 | 2026-09-23 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| f0b1f0b7-5502-3cc9-aacc-6ce9a0c5411d | -6.2205 | -41.6891 | 2026-09-23 13:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 108.1 |
| d028faaa-c318-36e2-8b55-a9ed37ca3dc5 | -9.6108 | -43.9477 | 2026-09-23 13:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 101.1 |
| bd231047-f0a3-3688-88b7-162f9a962407 | -8.9013 | -45.9556 | 2026-09-23 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 65d6f5e3-4cd6-379c-898b-45ea8cf93003 | -11.699 | -43.4416 | 2026-09-23 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 02331717-f9d1-311a-a793-d28c7fd3e5c9 | -6.9416 | -42.8834 | 2026-09-23 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.0 |
| 53c4b46b-7c5e-3ff2-be24-d77c5598c6c6 | -7.4153 | -42.6479 | 2026-09-23 13:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 136.7 |
| b6b15a06-4a71-3d4a-8a8d-15b5f5265002 | -8.9202 | -45.9536 | 2026-09-23 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 205.9 |
| e6234fb2-f2b6-3c77-b606-e53524c28d78 | -8.92 | -45.9 | 2026-09-23 13:15:00 | MSG-03 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e6627dcd-8f05-3e10-90c1-e03b3e1ed477 | -6.61 | -43.74 | 2026-09-23 13:15:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 954d5c68-ffb0-33be-b4f2-4e15b3aa2207 | -8.92 | -45.95 | 2026-09-23 13:15:00 | MSG-03 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cc795f48-2a8b-3f07-8018-401332d142c8 | -9.5921 | -43.9267 | 2026-09-23 13:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 90.1 |
| cac338d8-b1b8-38f9-87e7-3f641859eae7 | -9.5332 | -45.3633 | 2026-09-23 13:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 543da786-bb65-3db8-8983-366baf571b22 | -9.9163 | -45.0885 | 2026-09-23 13:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 0384d19e-0eac-3e05-8ad1-7f27f2d50e09 | -7.0349 | -44.6625 | 2026-09-23 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 64b361ed-8d36-329b-97b3-09af48971751 | -8.7735 | -45.6303 | 2026-09-23 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 0a9f440a-cf96-30a7-bb12-f699f52f2069 | -9.5518 | -45.3839 | 2026-09-23 13:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 116.1 |
| b9300ba2-4c3c-3684-a533-1af0b20b85c7 | -8.378 | -45.6036 | 2026-09-23 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| a2a84727-b059-36d2-8ffd-36b5b94c1da8 | -10.5561 | -46.7095 | 2026-09-23 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 120.6 |
| b6dde86b-1522-3fde-a756-6bec7e327635 | -7.4153 | -42.6479 | 2026-09-23 13:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 107.5 |
| 68556142-b858-3891-825e-81cac1f2aa11 | -6.2394 | -41.6875 | 2026-09-23 13:20:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 76.6 |
| 80773ef0-fb29-3e8d-8a66-c07ef67335f7 | -6.2205 | -41.6891 | 2026-09-23 13:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| a67945a6-5ed3-3324-aa64-9c1999c76509 | -6.2396 | -41.6634 | 2026-09-23 13:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 120.5 |
| 98996efa-f1f7-35f6-9290-0d6ac99af3c1 | -12.3573 | -42.2307 | 2026-09-23 13:20:00 | GOES-19 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 93.4 |
| 09746ad3-b236-3ce0-863e-4111518b8039 | -6.9416 | -42.8834 | 2026-09-23 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.2 |
| 33b99f23-f182-3f9f-9110-d1f7b5168987 | -6.6317 | -43.73 | 2026-09-23 13:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 1a02070f-a4c7-32e6-ab72-27db83cd47b5 | -6.2399 | -41.6394 | 2026-09-23 13:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 83.7 |
| c34ea572-29e1-3d8f-bc04-4439bb5ac3a9 | -6.6148 | -59.908 | 2026-09-23 13:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 90089099-fab2-3b98-9cab-5821a803a1fa | -7.0164 | -44.6413 | 2026-09-23 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 938b6023-692f-3685-a3a2-2894b38be1ed | -8.4985 | -57.6075 | 2026-09-23 13:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 748aa9ed-3cb1-3866-adaa-4d4fa87005d9 | -9.5329 | -45.3861 | 2026-09-23 13:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 99.6 |
| f05b5f25-5844-30a4-9e1f-3e497550d93d | -8.8108 | -44.2525 | 2026-09-23 13:20:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 43abeec2-c729-34e3-a8bf-63bd4bad6999 | -11.1541 | -42.8364 | 2026-09-23 13:20:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 100.2 |
| 102d4087-033c-3609-9ce2-da08b5a905f9 | -6.8985 | -41.6976 | 2026-09-23 13:20:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 128.7 |
| 2b45d437-008b-3805-9729-5ee4326d17fb | -6.9174 | -41.6957 | 2026-09-23 13:20:00 | GOES-19 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 155.2 |
| acb4424d-a0eb-3fd7-8681-e1750bce64b3 | -8.0923 | -44.3307 | 2026-09-23 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 794bc576-c40c-3235-a88f-f1e7b56d72de | -8.0921 | -44.3538 | 2026-09-23 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 106.1 |
| ca88487e-6eee-327f-bbf5-b29458f0428f | -9.5854 | -48.4549 | 2026-09-23 13:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| acbb0c46-baf3-368e-b8b5-b2657c27af6e | -6.166 | -52.05 | 2026-09-23 13:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 9b9dec15-7a70-3f1d-9393-693b200ad25f | -11.4005 | -44.0525 | 2026-09-23 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 308.0 |
| ea73ca98-a61f-3232-b638-8f9ea0c87f68 | -11.4782 | -47.3529 | 2026-09-23 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 188faedf-bbc8-39db-8925-88a164d3f118 | -9.6111 | -43.9243 | 2026-09-23 13:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 134.5 |
| 493fd511-4c22-374c-a8a3-22d58a97cfe4 | -9.5918 | -43.9501 | 2026-09-23 13:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 71.7 |
| d824842d-991e-3c0d-b841-62c2cca85f51 | -6.2208 | -41.6651 | 2026-09-23 13:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 129.2 |
| 968ded16-7e94-311d-b4bc-95c264841d06 | -7.1392 | -42.0811 | 2026-09-23 13:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 101.4 |
| 45f71036-44cf-39f2-8237-42fc1c48fe45 | -9.6043 | -48.4529 | 2026-09-23 13:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| ded3f20d-c56c-348d-b62d-211af9b1e074 | -7.1274 | -43.1009 | 2026-09-23 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.3 |
| e4c53945-b159-3469-99e1-3ed9f6f373af | -7.0885 | -52.7575 | 2026-09-23 13:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| eb0adb6e-8af4-3c1f-ba65-0f85a3198f56 | -9.5735 | -46.5337 | 2026-09-23 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 154.9 |
| b4b85283-beb6-31ea-9dba-021e012827b8 | -6.6129 | -43.7317 | 2026-09-23 13:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 360.6 |
| 1a47896a-b326-39ce-8426-e4a42077a33f | -6.6127 | -43.7549 | 2026-09-23 13:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| be387c35-c0db-356e-a1eb-74c8df709090 | -8.3591 | -45.6056 | 2026-09-23 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 117.3 |
| de7b61cb-5928-3645-8aaa-b9bf333b344a | -7.1277 | -43.0774 | 2026-09-23 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.0 |
| 2e3aab47-1022-34c0-900d-aa568cf2ef13 | -9.5857 | -48.433 | 2026-09-23 13:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 3c0145fd-c550-3375-97ef-8904c953cf07 | -7.4288 | -44.718 | 2026-09-23 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 176f1ebf-5982-38a0-b7a9-cb5817f391ef | -8.8105 | -44.2757 | 2026-09-23 13:20:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 145.5 |
| db9d2c91-80d5-3481-8bff-86d6585cd353 | -11.305 | -44.0432 | 2026-09-23 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 47e2e862-2e9f-3ce4-b496-b41383d5626d | -6.6331 | -59.9265 | 2026-09-23 13:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 138.1 |
| 3f26fc19-051f-3122-af7a-d0e806584f7d | -6.8988 | -41.6735 | 2026-09-23 13:20:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 95.2 |
| db97da70-c2c7-3073-b681-759a74728c6f | -8.9202 | -45.9536 | 2026-09-23 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 962f4917-be24-35b0-8003-d207b7e85e6c | -11.4009 | -44.029 | 2026-09-23 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 270.6 |
| 0076f3d2-076b-3436-9e03-e8b37d4f9245 | -7.41 | -44.7198 | 2026-09-23 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| e07b899d-35c5-376d-ae33-e6e0c327813c | -9.6108 | -43.9477 | 2026-09-23 13:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 94.3 |
| f0600a37-298d-3072-9735-770143957613 | -7.0352 | -44.6396 | 2026-09-23 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 179.3 |
| 88684fd8-d317-30e7-b3e0-beb8c7c01460 | -6.6127 | -43.7549 | 2026-09-23 13:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| efe68f98-30b3-3f6d-b233-5f4e52170cbc | -7.0352 | -44.6396 | 2026-09-23 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 161.1 |
| 6a5c5229-f6be-37f6-a18d-fee45495f0e5 | -9.5731 | -47.9529 | 2026-09-23 13:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 8a49d158-b588-3dd7-959a-b9b95224a089 | -7.0349 | -44.6625 | 2026-09-23 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 64c71e23-b10a-3540-84f3-1b7156903093 | -8.0923 | -44.3307 | 2026-09-23 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 174.3 |
| c3c8f5a5-12db-3f3e-8df2-9b1b8888066d | -6.9414 | -42.907 | 2026-09-23 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.6 |
| 44d0628b-dd2e-34c8-ac06-1d22f64b0f2f | -7.1277 | -43.0774 | 2026-09-23 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.1 |
| 6b7604ba-0415-3b6e-aa3d-085501dc09bc | -8.8261 | -45.9411 | 2026-09-23 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 7749e7a6-93c9-3ad7-a502-498dbb5b5f16 | -11.3976 | -44.2167 | 2026-09-23 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 236.5 |
| 4a4ab3c5-ca92-32a9-8488-befda50b3b0d | -11.4005 | -44.0525 | 2026-09-23 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 248.4 |
| 3c3f5144-911c-364e-8ebf-34a213b512a8 | -8.8108 | -44.2525 | 2026-09-23 13:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 72eda2ec-d309-33d2-883c-01fac843e8c2 | -8.4985 | -57.6075 | 2026-09-23 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 147.1 |
| 5b6a5659-affa-325f-ae0d-14073772fe59 | -9.6111 | -43.9243 | 2026-09-23 13:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 165.3 |
| ee7f4657-50c1-3120-980a-012812b60489 | -9.5735 | -46.5337 | 2026-09-23 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 141.3 |


[Clique aqui para ver as próximas entradas](README136.md)
