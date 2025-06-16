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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6784237d-6dfd-3807-ac1e-a39ef2e62b77 | -11.1379 | -53.9429 | 2025-06-16 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 17a5fc81-7841-361f-8f93-23c84300d11f | -7.1169 | -44.0339 | 2025-06-16 02:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 229.9 |
| f9e21872-62d8-36b9-ad68-b1683453dea8 | -11.0115 | -55.0561 | 2025-06-16 02:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 114.3 |
| a1c00558-f68f-363d-b27a-05a696f09c6c | -7.1169 | -44.0339 | 2025-06-16 02:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 7f7c40c7-2f02-32f8-a70d-2124fd7df219 | -11.0115 | -55.0561 | 2025-06-16 02:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 815b728e-8a61-3723-967f-04b824f36bf6 | -11.1379 | -53.9429 | 2025-06-16 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 65844a7a-20a5-34cd-8320-35f3e368a031 | -11.0115 | -55.0561 | 2025-06-16 02:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 87.0 |
| b83d5f47-cfc7-3246-a345-22390fa931d3 | -11.1379 | -53.9429 | 2025-06-16 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| a54616b2-1307-3f39-852f-833021a1120b | -7.1169 | -44.0339 | 2025-06-16 03:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 1ffee357-2fe5-397a-8113-7c0ba36d21e9 | -11.1379 | -53.9429 | 2025-06-16 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| d7dccd2f-4630-3393-be18-b3b7de7c88bc | -11.0115 | -55.0561 | 2025-06-16 03:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 93f3c2b8-210d-3d38-bfe6-3cee96c1c95d | -11.1379 | -53.9429 | 2025-06-16 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 0fe6dbef-3902-33e3-a09c-4853d28092e3 | -11.0115 | -55.0561 | 2025-06-16 03:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 690dd021-d330-322e-8002-4c848b910003 | -8.07599 | -34.97782 | 2025-06-16 03:13:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 316df763-41be-3abd-bcda-8bcdd0fd92c7 | -22.9015 | -43.75473 | 2025-06-16 03:17:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f4e78a6b-0c9e-33df-8340-222f52c161b0 | -11.1379 | -53.9429 | 2025-06-16 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 32fa65ca-2d25-3f98-86d9-f44c438bce4b | -11.0115 | -55.0561 | 2025-06-16 03:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| b7ec2ba1-8121-3d65-9974-5133bc7138bc | -11.0115 | -55.0561 | 2025-06-16 03:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 2570c760-9873-30f9-a0d0-49766ab048e3 | -7.1169 | -44.0339 | 2025-06-16 03:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 414356ed-d166-3930-af64-ca829563498d | -11.1379 | -53.9429 | 2025-06-16 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| ee2dc860-21ab-3294-9da9-314356bf6486 | -7.11508 | -44.03768 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18eb746a-dc75-381b-a9b9-9001aabb4fdb | -7.11714 | -44.05844 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb4ec62b-8462-3064-afb0-f609d7f0d67b | -7.11023 | -44.05712 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbdddb11-1298-399b-8059-6ae44b2d61a1 | -7.11145 | -44.05724 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11185b0d-3af3-3f1e-9d7b-23e4f06f77a7 | -7.11667 | -44.05417 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6d996e1-f199-356a-b5d8-24f0af536da4 | -7.1091 | -44.06988 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9f6d858-4e99-3853-9698-bebfc96b6e26 | -7.10376 | -44.06021 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71566d73-071b-3ce7-aa45-96d997c07b98 | -7.11094 | -44.05315 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 563a9b19-bad0-3d89-83c1-797b444e68b8 | -7.11289 | -44.04947 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b46759c-4ba7-32b0-ac1b-f940a8778f4e | -7.11637 | -44.06261 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 166d57ea-0c9a-306b-a0f7-7b56d8ea7884 | -3.77542 | -41.66983 | 2025-06-16 03:34:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 915389f1-f423-3d4f-8fa9-d11fe03ec358 | -7.11521 | -44.06241 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d84600b-119a-3268-9a6a-95504c66ce48 | -7.11372 | -44.03759 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb44bd9e-0d31-30d8-a156-5ef51b2e8276 | -7.10951 | -44.0612 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a20e873a-c60f-3c1a-86f3-90a00ba3d606 | -7.11162 | -44.04934 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2cca6d2-6169-3741-a6c4-4e90a96381b6 | -7.12124 | -44.06832 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a72b93f-f577-3d41-abee-227c5634a990 | -8.0739 | -34.97734 | 2025-06-16 03:34:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 90faf7b6-fc76-3df0-8cd4-bb2dd65b0e7f | -7.11069 | -44.06129 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 892ca1cb-61bc-3d8f-b81f-d28b7bf280a3 | -7.11361 | -44.04562 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c6c95b1-af56-3477-8f49-b19da2c0c7bc | -7.12046 | -44.07254 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9dd73d2a-214a-370c-b283-92da032d8ce6 | -7.23859 | -35.58866 | 2025-06-16 03:34:00 | NOAA-20 | INGÁ | PARAÍBA | Brasil | 2506806 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e1703321-abea-3c24-bcba-6634fcef650f | -7.1148 | -44.07106 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8711847f-e3eb-3c84-9b07-3e928d792fa6 | -7.11792 | -44.05428 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8812e2f7-478d-3e9f-837a-85cd54a18ce2 | -7.92391 | -47.80972 | 2025-06-16 03:34:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1230d62a-71a5-316b-baf9-fcdb785f4cf7 | -7.10828 | -44.07428 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 021e423e-6831-31f0-9fad-ff77296549c0 | -7.12204 | -44.06399 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14f65ba3-89ee-356a-a08a-a040db247f17 | -7.11218 | -44.05329 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad4e8870-ec1a-3f1a-a942-f991ee489b56 | -7.12021 | -44.0343 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 86f9fbee-1b6d-34ac-a576-48bbb4815125 | -7.11301 | -44.04157 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4f23ed7-4a5a-376f-9811-bc3cc2eb0f2f | -7.11594 | -44.05828 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d520085e-3a0b-3965-8fe8-5b501e3df47a | -7.11738 | -44.0502 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9627a55a-5902-3ff6-a047-6268f27fc19e | -7.11866 | -44.05029 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e6ebab8-f6b9-3783-9a3a-f3e1832ae1e1 | -7.92749 | -47.81199 | 2025-06-16 03:34:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1c8f40ca-dd23-32f2-85b1-525ccf77f75b | -7.10451 | -44.05605 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4125d235-3296-3d83-bfb2-c95592deb963 | -7.93098 | -47.81113 | 2025-06-16 03:34:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab11f7b0-5924-34ee-8dbf-748a067c73d3 | -7.11434 | -44.04166 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6e367f8f-a8a0-30ce-b8bd-f77222c41251 | -7.12159 | -44.03447 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 25a603d8-a15a-3072-bc46-6eacc8fff189 | -7.10299 | -44.06453 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82e004bc-8a9b-3676-b7ad-915b2b60e32e | -7.10522 | -44.05205 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf3502ce-308c-3439-9702-ca9714b22b3d | -7.11402 | -44.07527 | 2025-06-16 03:34:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f34b6373-5b32-3864-8427-8f3f6add373d | -11.02858 | -44.64467 | 2025-06-16 03:36:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7154a1c2-2356-397e-b3c2-8e97aa267320 | -12.97796 | -48.63979 | 2025-06-16 03:36:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0bbcc6b1-110a-38fa-8a39-5a05fd02da84 | -10.82573 | -46.95462 | 2025-06-16 03:36:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 47.2 |
| f1639500-48b9-304d-b5b5-11af9d5d69b2 | -12.0495 | -48.07795 | 2025-06-16 03:36:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f0592900-7874-3a72-9806-a09deb3773aa | -12.97659 | -48.64626 | 2025-06-16 03:36:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8829a9e-fb11-3928-bfde-e57cc968adde | -10.82463 | -46.96012 | 2025-06-16 03:36:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 31.3 |
| bebbf82a-f5b4-31dd-ae33-3ce464a1ceee | -14.09197 | -45.09172 | 2025-06-16 03:36:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2aae337-d60f-3854-aba3-7f3216f8ebe3 | -9.41199 | -48.43373 | 2025-06-16 03:36:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 979810bf-b35f-3274-9345-62412453f611 | -12.05217 | -48.07556 | 2025-06-16 03:36:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3df20379-a32b-3768-8bf2-59ce87b30066 | -9.40486 | -48.43219 | 2025-06-16 03:36:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fc6e4132-967e-3ed1-842c-32c2d26841cd | -9.41052 | -48.4409 | 2025-06-16 03:36:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54ed3da3-63ae-3557-9683-f1e392d3834b | -14.40106 | -40.35162 | 2025-06-16 03:36:00 | NOAA-20 | BOA NOVA | BAHIA | Brasil | 2903706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e91ae2db-64d6-3d0d-8080-b6ac6d1e730b | -9.40231 | -48.43264 | 2025-06-16 03:36:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6ff8b88-3f07-3be2-92a2-c025d95efc33 | -11.02301 | -44.64364 | 2025-06-16 03:36:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21cfaf23-f814-3a46-b2fe-97fe4fd7e188 | -9.40945 | -48.43415 | 2025-06-16 03:36:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bdf6add9-2562-3cb4-8b8a-47bad6b37916 | -12.05092 | -48.08148 | 2025-06-16 03:36:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d2399aa6-6f33-3f91-aee7-1f91eb28d1f0 | -12.05616 | -48.07965 | 2025-06-16 03:36:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e949af29-4de2-303a-9dc1-264d2597ab93 | -14.3991 | -40.34957 | 2025-06-16 03:36:00 | NOAA-20 | BOA NOVA | BAHIA | Brasil | 2903706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 366019fe-5356-3114-aaae-a952145f8832 | -9.41517 | -48.44286 | 2025-06-16 03:36:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7d2db43-9ec5-37c3-b3f3-7b7cc95ff740 | -14.08657 | -45.09055 | 2025-06-16 03:36:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dd2ff4e8-d988-3174-8bbd-ef8978608af7 | -19.71906 | -40.35369 | 2025-06-16 03:38:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4cb9a7fe-986f-36e7-b229-8a51695f5d0f | -20.34938 | -40.36013 | 2025-06-16 03:38:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 58ba9bf5-64d1-36c7-952d-c70d018283be | -18.03953 | -39.92522 | 2025-06-16 03:38:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 963e6049-f1bd-3197-947a-bf670fa2de0d | -22.67607 | -42.85566 | 2025-06-16 03:38:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 729aa8a8-798b-3ad8-9d4d-3f077d49317e | -14.64182 | -48.06128 | 2025-06-16 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb6876b6-e5f8-37a3-9258-acd335b5de66 | -16.67929 | -43.88467 | 2025-06-16 03:38:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa56128a-4dab-3f20-84ba-60f36feda200 | -14.64807 | -48.06348 | 2025-06-16 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ad21e63c-d52d-3df6-823a-92ac16bb6d25 | -22.78656 | -43.75757 | 2025-06-16 03:38:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 64fb40ea-95cc-390d-bfc6-ac6c408cd7ce | -16.68005 | -43.88271 | 2025-06-16 03:38:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6314dd07-b2f1-35ec-bb06-05b2a8e4d60b | -14.64259 | -48.05945 | 2025-06-16 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| efe99c19-7068-35e7-8d94-67269f3b0d39 | -19.25807 | -40.71368 | 2025-06-16 03:38:00 | NOAA-20 | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1be212bb-3ad0-3454-a5bb-2b214ba4d598 | -14.64137 | -48.06504 | 2025-06-16 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ccd14ef4-d3c2-31ab-bfb3-f43359b889c1 | -22.90132 | -43.75256 | 2025-06-16 03:38:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| fadce9c7-5cf7-373f-9da7-40b4a6642cc6 | -7.1169 | -44.0339 | 2025-06-16 03:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 61.3 |
| c4c898dd-f604-39c9-b27e-04305d72981c | -11.0115 | -55.0561 | 2025-06-16 03:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 436a51fb-ad5f-3986-b69d-b0fc6a79e38f | -28.58421 | -49.4407 | 2025-06-16 03:40:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d4a4500d-6f47-3cbf-a25d-a230be839a52 | -11.0115 | -55.0561 | 2025-06-16 03:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 69e70fb5-8e50-3ada-8359-0a5ef80b5944 | -11.0115 | -55.0561 | 2025-06-16 04:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 6021f93d-997f-3f72-83f4-ed34b3e78235 | -11.0115 | -55.0561 | 2025-06-16 04:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| c3f4eeca-d2c9-34d2-82d6-f9a958268459 | -11.0115 | -55.0561 | 2025-06-16 04:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |


[Clique aqui para ver as próximas entradas](README5.md)
