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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09492b64-50cb-3658-953c-325264e2044a | -12.1663 | -44.1224 | 2025-09-15 13:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| e89db246-757e-3dd1-a180-1dfc833ab41c | -14.5163 | -47.3531 | 2025-09-15 13:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 4c4c364b-5094-32fe-b7ba-4ada668e0c03 | -8.9601 | -45.7912 | 2025-09-15 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 168.9 |
| 03884ae2-eb2e-3064-9b27-e92465da6937 | -8.9784 | -45.8344 | 2025-09-15 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 047f8593-4781-3817-8f12-4a1362134808 | -6.1504 | -41.1889 | 2025-09-15 13:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 105.5 |
| 0fb0c0d7-ff36-31f8-9727-24b74824810e | -11.6626 | -46.5884 | 2025-09-15 13:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| c0685236-e187-34a6-81dd-63cb6f6ae7cc | -12.1668 | -44.0988 | 2025-09-15 13:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 195cae25-d1ec-3398-9967-590c7ea84bc9 | -11.3338 | -43.4979 | 2025-09-15 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 5a00ff17-560d-3756-89d2-4d2a4b3fdc1c | -10.9477 | -47.1976 | 2025-09-15 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 0aad078b-9f92-34dc-86ac-536a60be56ea | -12.0051 | -46.6763 | 2025-09-15 13:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| dae6bb0c-a954-36c5-9518-35d47e93f7d4 | -8.9412 | -45.7933 | 2025-09-15 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 147.2 |
| f6402035-846e-3a7f-be03-11f229d0aa41 | -8.6507 | -46.3862 | 2025-09-15 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 161.1 |
| eaa5d292-61ae-37aa-85bc-d0def26a0de6 | -11.6434 | -46.591 | 2025-09-15 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| e9f948f2-fc0b-3bec-936b-9a22231885cd | -6.1881 | -41.1855 | 2025-09-15 13:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 135.4 |
| afaba1e0-e67a-3e02-ac40-bd5362e53e8f | -6.3558 | -43.1711 | 2025-09-15 13:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 96d3de74-938d-3b2c-b971-d5514ae4fef5 | -10.0754 | -47.1686 | 2025-09-15 13:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 58b2f0b9-064f-3894-96b4-092eb0a513ed | -5.7673 | -43.9161 | 2025-09-15 13:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 11a2fcd3-ddf7-31a6-aaec-27493e2ac101 | -8.917 | -46.2015 | 2025-09-15 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 459.4 |
| 20456b0a-d20b-3c73-9fc2-4e9ab7c27a46 | -12.5975 | -45.7251 | 2025-09-15 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 007435b3-1b74-3fb3-a6d3-a3384a3d6bce | -6.1695 | -41.1629 | 2025-09-15 13:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 115.5 |
| c1c251ae-c33d-35c9-8474-8d9d65708189 | -6.356 | -43.1476 | 2025-09-15 13:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 64fbe476-4a03-3346-bf6a-b7851b4fbde7 | -10.948 | -47.1753 | 2025-09-15 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 188f582f-de87-3cb4-bc3e-ed4985ad1020 | -14.5168 | -47.3304 | 2025-09-15 13:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 9f0d066a-b194-30dc-b236-54150a8ad6d9 | -8.9734 | -46.218 | 2025-09-15 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 320.7 |
| 823914e5-e9a4-3bee-8ec9-7e14da321a7c | -10.935 | -45.5978 | 2025-09-15 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 161.1 |
| b2da6778-03f7-3115-87f7-f84a09522231 | -8.9604 | -45.7686 | 2025-09-15 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 826fe7db-4cc9-33bd-9680-d94e04064ab6 | -13.1838 | -47.2929 | 2025-09-15 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 921b5c93-a5f3-3400-9b51-e9a597825aea | -12.8404 | -47.1417 | 2025-09-15 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| d897141d-4ad3-338e-a79b-ae4e730dcf40 | -8.5947 | -46.3471 | 2025-09-15 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 5f8aaa24-c0a1-3169-95c9-5cc944d3d8b4 | -8.9545 | -46.22 | 2025-09-15 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 451.1 |
| 4b514acf-49b5-3d95-a2bb-a45603ee4f6c | -6.3372 | -43.1492 | 2025-09-15 13:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 032ecd02-df27-35db-9a1a-ec9ffa0ff3df | -10.9155 | -45.6232 | 2025-09-15 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 149.4 |
| c5cf34ba-50cd-364e-b72e-fc1fde54bce5 | -6.3989 | -42.6263 | 2025-09-15 13:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| a851d03c-8a36-3e81-9832-732f01b646d9 | -11.1306 | -45.2966 | 2025-09-15 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| f92f976c-6c64-3ed3-8ee9-30891e6e71ee | -11.1303 | -45.3196 | 2025-09-15 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 70109efe-0716-39d5-bb9d-df94a3dc467b | -7.8076 | -46.1099 | 2025-09-15 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 39991084-1eb1-36f4-a635-571456acc7af | -9.2235 | -44.5052 | 2025-09-15 13:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 143.0 |
| a5e1bc6b-8b33-34cf-a239-6e890c8b3f31 | -11.6622 | -46.611 | 2025-09-15 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 059821c1-1693-3691-bce6-60bd5c9a8f6c | -9.2691 | -51.2455 | 2025-09-15 13:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| ab77fa67-f9c3-3239-ad9f-6fba28fd611d | -9.5167 | -47.9369 | 2025-09-15 13:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 8d07ed10-92ba-346c-88f2-74a00a04b8d9 | -13.1838 | -47.2929 | 2025-09-15 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 16aa818c-a69c-3247-9a1d-d673fb503a4f | -12.8204 | -47.1896 | 2025-09-15 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 6d92eb2c-7023-3eb4-8a56-7a1d8221890d | -12.5979 | -45.7021 | 2025-09-15 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| e4f4edab-c2d4-385f-a358-1a93e854dc36 | -14.8111 | -48.1367 | 2025-09-15 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 95.2 |
| f7e1f941-04d1-3994-be07-ee76cd7ad0e2 | -16.673 | -49.7615 | 2025-09-15 13:40:00 | GOES-19 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 4ca04950-5f58-3c3f-9657-a3376fde7535 | -10.9667 | -47.1952 | 2025-09-15 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 223.0 |
| 15a78f59-5278-301f-a900-ff74b3408b23 | -12.6341 | -47.9534 | 2025-09-15 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| e8c1231d-076b-3652-a08d-681df1895731 | -9.2691 | -51.2455 | 2025-09-15 13:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| e1a7aba5-6764-369d-bb89-382abd45001f | -10.9346 | -45.6207 | 2025-09-15 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 520.6 |
| 43d42d70-7dae-3eb7-b210-fcac4d7f0a15 | -11.6622 | -46.611 | 2025-09-15 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 5680c8c5-f254-31b7-8421-5b05151c58c0 | -8.9784 | -45.8344 | 2025-09-15 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 203.8 |
| c6c27818-c111-3025-8beb-daa5d18ace0e | -12.8404 | -47.1417 | 2025-09-15 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 184.1 |
| 2251c253-42e3-3c3f-8353-7d299767f8bd | -6.4452 | -43.6067 | 2025-09-15 13:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| ee502d97-8f16-3917-ab23-d5e214db6d09 | -5.7673 | -43.9161 | 2025-09-15 13:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| cae14d16-ebc0-3397-99e9-11565953e154 | -11.1306 | -45.2966 | 2025-09-15 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 2981d015-dccc-3da6-99ea-35c236859f69 | -11.6757 | -50.5796 | 2025-09-15 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| c2f53a49-f765-3e3e-b13c-9a483548bf45 | -13.9288 | -44.8106 | 2025-09-15 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 5e01bbbd-4765-3f6f-a1dc-98f0a5b633fd | -11.638 | -50.5625 | 2025-09-15 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 156094df-c1ae-375a-aa82-49b3259df085 | -9.7393 | -46.8504 | 2025-09-15 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 46b0f3ec-a7f0-3818-8311-8e2112fc4ac8 | -8.5947 | -46.3471 | 2025-09-15 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| d7378d25-8f66-3a51-9d56-e62bfbadc695 | -11.8853 | -50.5554 | 2025-09-15 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| c4cfa7d0-7ecd-3a75-a570-e7efae1f8fb9 | -5.8399 | -44.1642 | 2025-09-15 13:40:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| a561a1eb-cd89-3937-8e92-d59cdd8ca562 | -8.9412 | -45.7933 | 2025-09-15 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 6f09820a-2e9a-3626-9b02-f60b05ebe7d7 | -6.337 | -43.1727 | 2025-09-15 13:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 141.3 |
| c205236c-a98c-3890-8ef3-d29f49ee7314 | -7.8076 | -46.1099 | 2025-09-15 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 79911b8a-69e5-3b46-858e-c77e96887431 | -10.075 | -47.1908 | 2025-09-15 13:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 0906d0b0-52f4-3ba8-8e75-a3ec051f2948 | -10.9155 | -45.6232 | 2025-09-15 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 356.0 |
| c4b1fcd0-0443-3a53-aafa-2613c3e9fe80 | -12.6533 | -47.9507 | 2025-09-15 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 9d32c434-dae3-3ad1-ae49-8dbc31524ef7 | -11.6434 | -46.591 | 2025-09-15 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| af163c55-593f-3647-bc29-7cfef7186819 | -6.3558 | -43.1711 | 2025-09-15 13:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 849aacf7-eb45-3d3f-96b0-509576987983 | -6.1881 | -41.1855 | 2025-09-15 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 249.8 |
| c088fbd2-faa7-34e9-85b7-da7ab652e0a8 | -8.6507 | -46.3862 | 2025-09-15 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| ee311ece-0da2-326d-ab70-7d7797a56f6e | -6.356 | -43.1476 | 2025-09-15 13:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 9c4f81a9-798e-3483-98e7-de757bd491af | -5.7875 | -45.8707 | 2025-09-15 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 444ba06a-0ebe-3de5-8215-f2c99013ca62 | -7.5281 | -47.642 | 2025-09-15 13:40:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 35310066-413a-33f8-a900-e0c536b8c58c | -14.5168 | -47.3304 | 2025-09-15 13:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| ecde882c-2e1d-3379-9e85-47a58c74b937 | -8.9787 | -45.8118 | 2025-09-15 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 7af67ffa-019a-35d9-8ade-a2aa7157a1db | -9.2235 | -44.5052 | 2025-09-15 13:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 167.9 |
| c8d40594-2e2a-3a33-bf8f-c10b88754109 | -14.8218 | -51.6362 | 2025-09-15 13:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 199.6 |
| f9a82f87-6bda-3dd6-a45e-6d7844fd6913 | -12.1861 | -44.0958 | 2025-09-15 13:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 0590d65b-9b40-3b36-8383-dd5669ca962a | -18.9851 | -48.5844 | 2025-09-15 13:40:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 09caf3d3-5439-35b4-9a0b-b5a08e5cb196 | -6.169 | -41.2114 | 2025-09-15 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 254.6 |
| cddf3b61-5738-3b61-9418-4dd71d9a72cd | -10.0754 | -47.1686 | 2025-09-15 13:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 639fc810-303a-3198-a63e-712247e109b2 | -8.9265 | -45.4776 | 2025-09-15 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 93f9eb12-d227-31c5-8553-65268ec5d3a2 | -14.9607 | -46.572 | 2025-09-15 13:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 67.6 |
| c8a592bb-69a0-3958-842f-f52df34ea718 | -10.935 | -45.5978 | 2025-09-15 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 366.6 |
| fda1de6c-cec6-38cc-9cef-6daabfd8505c | -6.3989 | -42.6263 | 2025-09-15 13:40:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| ec161a4a-3f5c-3d38-9c1a-a0876b977f22 | -10.9159 | -45.6004 | 2025-09-15 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 227.0 |
| 9c601fbd-6538-356a-8726-00a242e66320 | -8.9604 | -45.7686 | 2025-09-15 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| a838430d-004f-3147-b451-5a8c7066a82f | -6.1884 | -41.1612 | 2025-09-15 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 116.2 |
| 00e64324-a2db-3c16-bf3a-b59a6e7b8271 | -11.6567 | -50.5817 | 2025-09-15 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 60021a5b-e9e9-335d-b6eb-8d06c822bd90 | -6.3372 | -43.1492 | 2025-09-15 13:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 171.1 |
| 9d95be01-5ba3-31dc-b2e7-33e552c326a7 | -10.9477 | -47.1976 | 2025-09-15 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 223.0 |
| 12c3dee9-50ee-32ec-a4cd-0ec86d97b8cd | -8.5944 | -46.3695 | 2025-09-15 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 353c099f-4acf-3557-a35d-637e8473621e | -8.9601 | -45.7912 | 2025-09-15 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 120.7 |
| ddb9994a-43e1-330a-a8de-5188d5d64f27 | -7.4349 | -45.8519 | 2025-09-15 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 46d29d0f-0aaa-3aaa-b794-6073a42be951 | -6.1695 | -41.1629 | 2025-09-15 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 163.7 |
| 1c13bb36-9c09-34a7-a7b7-611379dcd2b6 | -8.651 | -46.3637 | 2025-09-15 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 929b171c-310f-3599-a970-2f41ecad8ae8 | -8.7868 | -46.0578 | 2025-09-15 13:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 5121c941-a941-39a3-8d13-a5c1bd62473c | -3.4366 | -43.1532 | 2025-09-15 13:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |


[Clique aqui para ver as próximas entradas](README74.md)
