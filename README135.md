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
| 3709a7cc-3d6e-3299-9fd3-35911d6fd12e | -6.3281 | -42.2056 | 2025-09-12 14:10:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 79.5 |
| ec98c959-d42c-30ea-831f-1c35df326db6 | -7.5641 | -44.4068 | 2025-09-12 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 1ca5f892-3c2b-31cf-8e2b-61e292ce84cc | -10.0943 | -47.1664 | 2025-09-12 14:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 260.1 |
| d3ed2fc8-df91-3f7c-9c35-ab759b4cf5ac | -12.9294 | -54.7333 | 2025-09-12 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 85287e25-1fba-35e9-95fa-1313ecf49db6 | -9.0376 | -47.0819 | 2025-09-12 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 08b4940e-0094-3969-af5b-268af107ac46 | -11.4208 | -48.5756 | 2025-09-12 14:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 1cd3cdbf-2e0e-3bde-923b-a71c6e8c712c | -8.9938 | -46.1034 | 2025-09-12 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 6b5e9337-1f91-3f72-943d-cb2205039b01 | -9.5324 | -54.6277 | 2025-09-12 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 7e5d12f2-31d7-3c19-8598-47d59a009724 | -9.0759 | -47.0335 | 2025-09-12 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| a195bb19-da0e-34bb-a38c-aec338024a2a | -10.6979 | -48.6612 | 2025-09-12 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| dd2a42f0-f599-359d-9566-8f86c2804078 | -9.0166 | -45.8077 | 2025-09-12 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| b1e69667-6841-3a21-a31f-d9bc08c05510 | -9.0373 | -47.1041 | 2025-09-12 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 1862a5b0-9fb6-3ec5-a9bf-f439f57b1f21 | -6.3278 | -42.2294 | 2025-09-12 14:10:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 112.3 |
| 029c35fd-f22d-301f-a00a-a7bce63f60d5 | -6.1894 | -41.0641 | 2025-09-12 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 111.5 |
| c0913a6a-4c1a-3943-a6bd-46b6fee4a6c7 | -9.9574 | -50.3139 | 2025-09-12 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| e788c061-2bb1-3b50-bc1b-8f9e84fe6f01 | -10.2979 | -48.8365 | 2025-09-12 14:10:00 | GOES-19 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| de59ee40-9be1-357c-bccc-4a3d3558db16 | -10.9089 | -47.247 | 2025-09-12 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| fab62322-3cfd-3fb5-a9b1-f0a250456473 | -8.4705 | -47.2712 | 2025-09-12 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 2a52aff3-a316-3510-a7d4-801acdf8c5fc | -8.9368 | -46.132 | 2025-09-12 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 150.5 |
| eb5396e1-9332-317a-89bf-a08c2949f9ea | -14.3937 | -52.9456 | 2025-09-12 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 24635ab0-07f7-3081-a889-868c33d1df87 | -11.4398 | -48.5733 | 2025-09-12 14:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 219.3 |
| 612ab25a-ce90-3f1f-aa8e-a850342963d1 | -10.3504 | -50.5516 | 2025-09-12 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 66b541bc-d3b0-30c5-95be-9e14a5caa2c9 | -11.377 | -50.2281 | 2025-09-12 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| f98b9551-27b0-352b-ad3a-5a1652f2dfd5 | -12.8649 | -62.1268 | 2025-09-12 14:10:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 75fba2e8-c578-3ba8-b466-549e2d63a32b | -10.8972 | -45.58 | 2025-09-12 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| a4711e89-88cd-3fcd-a1d1-a22f8fa99cbd | -16.3623 | -51.4969 | 2025-09-12 14:10:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 113.1 |
| f5a4ccd9-7453-3fc0-846a-868fd96dcba9 | -8.8768 | -51.111 | 2025-09-12 14:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 8728fc7a-88d3-3975-af11-1ac2240623b1 | -8.4331 | -47.2527 | 2025-09-12 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 1d391a44-e37d-375a-bc32-82eb773b24c4 | -15.1058 | -47.9983 | 2025-09-12 14:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 70.8 |
| a214e829-9275-33e1-b82f-547fcc0f68a7 | -9.72 | -46.8749 | 2025-09-12 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 41fb51dd-8500-3d59-bf9c-e59e15431382 | -10.0947 | -47.1441 | 2025-09-12 14:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 523707e7-a62b-3d14-b474-a1a0a7e510bb | -12.9098 | -54.7763 | 2025-09-12 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| ef5abf78-2108-3cf6-8240-8f501c367af3 | -11.429 | -43.5307 | 2025-09-12 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 334.1 |
| c48d01d5-6e40-3b62-8d53-1d88e8fcf70e | -8.9563 | -46.0849 | 2025-09-12 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 34cca369-53bf-353c-aa65-4e2fc911eef8 | -9.0379 | -47.0597 | 2025-09-12 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| e7b54f2e-ea3e-3ac6-b999-2edcf73481ce | -6.1923 | -42.6205 | 2025-09-12 14:10:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 103.7 |
| 0d2463ad-ea95-3ac6-a385-587379dbc8d5 | -12.9289 | -54.7744 | 2025-09-12 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 6eb1d246-13ed-31fd-a488-582081007593 | -11.1949 | -48.4277 | 2025-09-12 14:10:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| d68cfb55-9b59-38e0-a33c-a5697093c7b3 | -9.0382 | -47.0375 | 2025-09-12 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| f133829c-f34e-334c-ab2c-c26a7aff837f | -10.679 | -48.6633 | 2025-09-12 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 281d0a19-7283-3457-8dcc-ce3903b4ff06 | -7.4508 | -44.4407 | 2025-09-12 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.3 |
| f20a83af-a144-30bb-a6a4-d4370f2575a0 | -14.1907 | -46.2012 | 2025-09-12 14:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 895ed15b-c5f1-3891-9d13-003fe7eccf70 | -14.4588 | -47.3174 | 2025-09-12 14:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 4c0d97c9-354c-3a1a-a6d1-7b756f21b3eb | -8.9749 | -46.1054 | 2025-09-12 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 207.2 |
| 7631129c-a70e-398f-9250-192d4d2e85bb | -10.3171 | -48.8127 | 2025-09-12 14:10:00 | GOES-19 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| f9478ee5-bbf4-3edc-a992-fdfcbddd9309 | -11.5425 | -50.5947 | 2025-09-12 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 3b77dc6d-2c13-380a-ad31-b53b39920a98 | -9.6473 | -48.0548 | 2025-09-12 14:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 9409de23-b732-3c67-bbec-53726bb5b755 | -6.1891 | -41.0884 | 2025-09-12 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 860.0 |
| 41750245-0408-3566-8b97-130f7760eaec | -8.956 | -46.1074 | 2025-09-12 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 78e3b1b0-8998-3ac3-bedc-afb75fb06a4e | -9.3433 | -45.4082 | 2025-09-12 14:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 77577fde-f32b-3c82-8777-4f7333e045bf | -9.1162 | -49.8604 | 2025-09-12 14:10:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| d1846f5b-4bcf-3808-8a3e-35baa7997739 | -11.9523 | -51.1661 | 2025-09-12 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 12f3c849-412b-3c48-ac21-cd6d5efed97a | -6.1698 | -41.1387 | 2025-09-12 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 318.8 |
| 94f03119-e552-3e7e-9042-d5c548fbeec2 | -8.4893 | -47.2694 | 2025-09-12 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 4ea48b1d-6914-3e66-8e78-69611b5934bd | -9.3436 | -45.3853 | 2025-09-12 14:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 9b0dfe0c-96ec-3783-8b37-62e716ec4f38 | -9.0172 | -45.7624 | 2025-09-12 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 634eb91b-a970-35ec-840f-8ac826f53148 | -9.7197 | -46.8972 | 2025-09-12 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 04f28513-e4d7-3dac-ab3a-f8f0023c6e30 | -6.2588 | -43.4828 | 2025-09-12 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 5e4016dd-d52e-3d5b-9c16-16baa383d755 | -6.8184 | -45.6349 | 2025-09-12 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 2ef5ceef-0846-3ce0-b4ac-073a30624fc4 | -8.0817 | -50.1836 | 2025-09-12 14:10:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| f261aaa8-4461-3ca6-81c0-4022eaedb1fb | -11.972 | -51.1214 | 2025-09-12 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 132.8 |
| fea5faff-fa7c-383b-b220-6356dc3c7fa1 | -7.5455 | -44.3856 | 2025-09-12 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 22d3b99f-4b92-3100-8233-c8cabd9e8e0c | -10.8968 | -45.6029 | 2025-09-12 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| ee5c2608-5f57-3213-a52e-aaa6c930df3d | -7.5232 | -44.6862 | 2025-09-12 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 689d749c-3f85-3503-ad7e-e4ceacd5ab87 | -10.4252 | -50.6078 | 2025-09-12 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 25b90cb0-5526-3a96-a918-d971bcc7976d | -15.5822 | -54.7429 | 2025-09-12 14:10:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| ef2cfc56-f638-3f4e-adf3-5f6198659aaf | -10.0754 | -47.1686 | 2025-09-12 14:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 67380291-1e22-33f7-95b8-15129501ea68 | -6.1732 | -42.6458 | 2025-09-12 14:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 75.5 |
| 739f4270-a621-3313-a22a-142b2c9ccf2a | -10.4249 | -50.6291 | 2025-09-12 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 6889f106-d440-3944-888a-e41a4319b337 | -15.1402 | -50.1628 | 2025-09-12 14:20:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 209.5 |
| cde68ac8-a9f9-3309-9d40-563fcb3ae52e | -11.5232 | -50.6182 | 2025-09-12 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| eeae7d08-52f2-37a6-ad20-b67c61359147 | -7.5232 | -44.6862 | 2025-09-12 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 5ffa4407-05e7-3325-8a2c-bb38e0ef9840 | -10.4438 | -50.6272 | 2025-09-12 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 124.6 |
| b977ddd1-daaa-384e-89b1-672ca7e3deb7 | -11.3718 | -43.5157 | 2025-09-12 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 866e7eac-b93d-362b-a8a2-891b0bc5d553 | -7.542 | -44.6844 | 2025-09-12 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 1827d3b7-6907-38ff-b2b3-70d56d0ac189 | -15.0246 | -50.1148 | 2025-09-12 14:20:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 9eb871f4-dfea-3ec9-aa65-6a9b1badaa01 | -9.0172 | -45.7624 | 2025-09-12 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| aaad9391-2c84-3ffb-8f36-6fc6d470d799 | -10.1133 | -47.1642 | 2025-09-12 14:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 319.1 |
| 411bfbfa-93a6-3456-ae18-ee63d0dca693 | -6.1705 | -41.0658 | 2025-09-12 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 109.3 |
| 2b1884e1-d305-3667-be4e-d25dc6735b6b | -11.1061 | -51.9958 | 2025-09-12 14:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 104.7 |
| db1edb72-1fea-3b3f-9102-246252c2a325 | -14.4394 | -47.3206 | 2025-09-12 14:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 6a1676f6-ec82-33ac-9b34-6ec242b71c8a | -10.6979 | -48.6612 | 2025-09-12 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 7eb60392-ed54-3ca9-b4c5-a29d7493ffef | -11.4281 | -43.578 | 2025-09-12 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 4f8c1e70-99dd-3406-a781-1e80d74453cd | -10.3171 | -48.8127 | 2025-09-12 14:20:00 | GOES-19 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| b87992a8-b24d-324b-a43d-4b53f2dd7afe | -11.429 | -43.5307 | 2025-09-12 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 319.4 |
| 323d6797-5a86-3194-a58e-edb7e87f3c4c | -15.1169 | -52.4705 | 2025-09-12 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| dea03e72-1131-38d4-a02d-3577f842ce4e | -9.9385 | -50.3158 | 2025-09-12 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 22274f9a-c959-3f11-9537-8338687da658 | -6.3044 | -53.4156 | 2025-09-12 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 700af5da-e60a-3037-9149-480098900083 | -12.9294 | -54.7333 | 2025-09-12 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| f8189ffa-98f5-3a78-8ea0-ae4faac6059a | -16.5309 | -55.0599 | 2025-09-12 14:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 96.3 |
| 018b2248-17b5-3939-a267-43a2dc58a394 | -6.1923 | -42.6205 | 2025-09-12 14:20:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 105.4 |
| 663ed0ff-8068-3ac0-b63f-6e557657304d | -9.1164 | -49.839 | 2025-09-12 14:20:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| e2211fab-6973-3d4e-a303-58ac74b53de1 | -6.3042 | -53.4359 | 2025-09-12 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| dc7a5727-5ce2-314a-ba13-6c7a10c5776a | -7.5643 | -44.3838 | 2025-09-12 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 234081d6-05df-3ae6-986a-d4d882169bf4 | -11.377 | -50.2281 | 2025-09-12 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| af3a7625-66dc-380e-9d4d-3e2bf98a7623 | -7.5452 | -44.4086 | 2025-09-12 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.4 |
| a03bc38e-93d7-37a6-94c2-7a15b61dfd05 | -11.526 | -50.4255 | 2025-09-12 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 63c1553d-c92c-3acb-99eb-5a65b680247b | -9.5137 | -54.6292 | 2025-09-12 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 143.2 |
| 08f67cf7-2d11-33a6-9435-99969481e179 | -11.1064 | -51.9748 | 2025-09-12 14:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 590df1da-841b-3efe-8f41-b0f412d566ed | -9.72 | -46.8749 | 2025-09-12 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |


[Clique aqui para ver as próximas entradas](README136.md)
