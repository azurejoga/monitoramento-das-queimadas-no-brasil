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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06cf41a3-f732-3c05-a851-84ca76f39cbf | -12.9294 | -54.7333 | 2025-09-13 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| c5c03269-de0f-31b2-af0f-37ca60854211 | -10.7474 | -50.5319 | 2025-09-13 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 7f5bdce0-08b0-3717-a1b8-e0464e12896f | -15.1169 | -52.4705 | 2025-09-13 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 38fc4250-9738-37d7-9578-ed22214b36a1 | -16.0796 | -49.993 | 2025-09-13 13:50:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 61b5249d-fc7f-3f09-a06e-6dec6cb84780 | -14.4364 | -48.4421 | 2025-09-13 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 99.4 |
| ededea8a-cc36-3a57-8e32-2bf34c09cfb6 | -9.2503 | -51.2472 | 2025-09-13 13:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 393bf91c-49c2-3dcb-b5a1-b86bb4a5170d | -13.9366 | -48.2745 | 2025-09-13 13:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 42.1 |
| d2e454bb-b061-3e50-932a-e96ce93a007a | -10.3701 | -50.4857 | 2025-09-13 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 6ab5669f-a298-30c5-b70a-093af1dbf4c2 | -10.5484 | -47.2242 | 2025-09-13 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| e93491d3-f9bb-368e-83aa-fb4fb2cfe5d3 | -12.8456 | -47.9236 | 2025-09-13 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 175.6 |
| 58ac4473-f06e-35dc-aac5-b2e7cd5cce5a | -11.8698 | -46.7627 | 2025-09-13 13:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 8e58f3f9-2698-397e-8719-66245928ca07 | -8.9176 | -46.1565 | 2025-09-13 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 3277025a-7ff8-3fae-92f7-68e93816ad63 | -12.1236 | -47.579 | 2025-09-13 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 166.2 |
| edd1fe66-7945-3216-8a42-70dc5aab095c | -11.2882 | -51.1334 | 2025-09-13 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| d7594644-d68c-3bca-8c0c-9dd6bb4f755d | -11.7826 | -47.402 | 2025-09-13 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 120.9 |
| bf772532-7003-36cf-ae97-69084e3d3f97 | -14.2088 | -46.2669 | 2025-09-13 13:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 127.4 |
| a38e1845-5772-3994-a7ef-bc28c3bde313 | -13.9379 | -48.2076 | 2025-09-13 13:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 84.2 |
| f81f98df-a353-35b0-8af6-d11a5e21c153 | -13.2341 | -43.7554 | 2025-09-13 14:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 442.0 |
| f9f1b80d-bd27-310d-b058-324e4dcd2f47 | -11.2882 | -51.1334 | 2025-09-13 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 114.3 |
| cd1d0c06-da9a-30ca-bc0d-9e4b0fc73f79 | -9.9948 | -50.3316 | 2025-09-13 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 646cd343-32e2-3398-bb33-78f82c104738 | -12.8456 | -47.9236 | 2025-09-13 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 306.5 |
| c4891e37-e40a-3fd5-87e7-63c9a6505aaa | -14.4133 | -52.9221 | 2025-09-13 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 389becb3-2d5c-3018-9f54-2d613a2d01e8 | -13.9172 | -48.2775 | 2025-09-13 14:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 29e97c57-73b6-3235-943b-8013a207dc1d | -8.497 | -45.1369 | 2025-09-13 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 138.5 |
| cdcc1395-a9d1-351f-8aaf-afbffa314ab5 | -13.9185 | -48.2105 | 2025-09-13 14:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 07d12341-2849-32a6-8892-1574de2adbdd | -11.8468 | -50.5813 | 2025-09-13 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 4c80e1ee-e0fb-3468-8949-fd1f7b99f2a6 | -10.8785 | -45.5597 | 2025-09-13 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 3e3bf61c-82d1-3d2c-b420-32f3fdad9309 | -14.4584 | -47.34 | 2025-09-13 14:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 58.6 |
| c2594850-5079-3ab5-b078-35aac99cb7db | -14.4588 | -47.3174 | 2025-09-13 14:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 79.2 |
| af6cf776-f59b-36a2-a49f-499f439d52ab | -14.0072 | -44.7733 | 2025-09-13 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 204.7 |
| 31702e04-952b-33fc-bd35-f0970d088778 | -15.8648 | -47.2322 | 2025-09-13 14:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 92.6 |
| e5184db1-c8c6-3305-a439-b5d714c3e1d3 | -11.4512 | -50.3483 | 2025-09-13 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 44d34e01-11ea-3f09-bc49-1706d9d04fd3 | -10.3699 | -50.507 | 2025-09-13 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 6d7afcaa-0374-3429-930a-9504190ca1d9 | -13.2336 | -43.7792 | 2025-09-13 14:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 0ef5fae9-ce3b-354f-8915-113af0c83579 | -8.9179 | -46.134 | 2025-09-13 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 2e2cd3ef-27b9-3e99-ab98-cbc7f1b2fbe4 | -15.1748 | -52.4839 | 2025-09-13 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 759308a6-0248-30ba-a5a0-a0dc44aaa64e | -15.4713 | -47.3256 | 2025-09-13 14:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 111.0 |
| e44632cb-13c6-3e64-b0c8-fe47666452b2 | -18.0667 | -45.4134 | 2025-09-13 14:00:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 3319fbb9-5e21-3415-984b-f54d3ee6fbb4 | -16.1399 | -49.9171 | 2025-09-13 14:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 4ad1f089-bb0b-3c3e-a227-58d09bb810df | -13.8979 | -48.2804 | 2025-09-13 14:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 2346a267-1dc7-38f6-b9c1-9e20ea9d9b0c | -19.3508 | -44.798 | 2025-09-13 14:00:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 98.3 |
| e93ccdab-cedc-39e9-a5fe-741d126c4081 | -15.0436 | -50.1337 | 2025-09-13 14:00:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 79.5 |
| bba9fb88-b674-3c03-9802-b84638d9f8d7 | -7.4513 | -44.3946 | 2025-09-13 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| b49137a7-cd11-3403-8405-e832e01631a3 | -12.9591 | -48.0186 | 2025-09-13 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| cd5231eb-5877-38fd-95ff-3c53c4288466 | -10.3696 | -50.5283 | 2025-09-13 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| d90222fc-0d32-3a1f-b4fb-e5a079bdabf4 | -12.8452 | -47.9459 | 2025-09-13 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 242.1 |
| af7f1468-52f8-31f4-a2b7-ba65652df612 | -11.7204 | -46.5579 | 2025-09-13 14:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 125.6 |
| dcb9261a-8813-3d42-a1d2-c523c9c2d93f | -15.1169 | -52.4705 | 2025-09-13 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 67f95e40-a247-3c05-8cf7-865e90a9b874 | -11.8465 | -50.6027 | 2025-09-13 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 58a178ae-5fee-31db-bb10-c1b0d732d6fc | -10.3509 | -50.5089 | 2025-09-13 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 3dd1635f-a3e3-3b83-984a-3cc2a927ece6 | -11.1237 | -50.7049 | 2025-09-13 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 2fad67d7-ef7f-36bf-bca2-feea76692226 | -12.8649 | -62.1268 | 2025-09-13 14:00:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 05804a2e-85e5-3036-8a8c-6cdfa70c3e27 | -11.7579 | -46.5979 | 2025-09-13 14:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 297.3 |
| 3a750a7a-d197-3dbb-a780-410fcc043ccd | -11.7826 | -47.402 | 2025-09-13 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 9b2ce089-aa64-3865-82ff-701b7caf9afd | -7.4633 | -44.9889 | 2025-09-13 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 4f40228f-cb69-32f6-a278-6a4d7514f37a | -11.9863 | -46.6564 | 2025-09-13 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| ed4d479d-0ab3-34ae-8cea-7594550c450b | -9.2844 | -59.3986 | 2025-09-13 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 732115a6-2f87-38b5-9d21-9592f8651b0c | -16.6532 | -49.7649 | 2025-09-13 14:00:00 | GOES-19 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 167.9 |
| 73ef383d-db97-3ede-9e8e-443b5f022af4 | -15.8845 | -47.2286 | 2025-09-13 14:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 10d29529-01e1-3ef8-bbb8-8387383f0041 | -16.4903 | -55.1484 | 2025-09-13 14:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 108.7 |
| 98f25774-4d76-3900-8dab-cd71035c05c2 | -9.2503 | -51.2472 | 2025-09-13 14:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 14ca94ee-b7ae-3fc0-b7f9-9f1959a27dad | -9.976 | -50.3334 | 2025-09-13 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 466b0e22-a270-386f-9465-2132668c740c | -8.956 | -46.1074 | 2025-09-13 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 281c7d2f-ba49-3c79-8c56-cc6931348404 | -12.8647 | -62.1461 | 2025-09-13 14:00:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 87.2 |
| d4d8d4bf-2406-38b9-8f85-f91afa0f8926 | -9.9754 | -50.3761 | 2025-09-13 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 18df887e-5658-31b5-82d2-ea65e9cf9cda | -10.8781 | -45.5826 | 2025-09-13 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 172.6 |
| 41fa6249-f2a0-3c09-a50a-1afac4b29fa1 | -16.3422 | -51.5217 | 2025-09-13 14:00:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 5b704558-81b1-3c5a-b003-25b04d49d524 | -15.0241 | -50.1367 | 2025-09-13 14:00:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 1dc73f3d-d1ce-3f6f-a8e6-781b088573b4 | -16.4906 | -55.1276 | 2025-09-13 14:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 170.6 |
| 1e38cb3e-23c9-3d81-9153-65ddb6864175 | -10.1319 | -47.1843 | 2025-09-13 14:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| d367ba91-8c29-3f1b-9067-dc6be9be5c23 | -11.885 | -50.5768 | 2025-09-13 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 90780943-444f-356c-9593-509e50275095 | -13.9877 | -44.7767 | 2025-09-13 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 149.5 |
| f728fb49-2876-3325-8f9f-cb3f517c7871 | -8.5159 | -45.1349 | 2025-09-13 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 115.6 |
| deb1c465-94e4-3fed-9a99-cfd241088be8 | -15.6013 | -54.7613 | 2025-09-13 14:00:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 03f04bfc-4e91-3f67-86b2-6ac78d0c8602 | -15.4517 | -47.3291 | 2025-09-13 14:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 113.0 |
| e5335159-a0a9-3430-805c-30f5f4604275 | -11.8659 | -50.5791 | 2025-09-13 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 167.1 |
| cb36fc29-1803-37f7-8f7a-57e36947bce7 | -9.7108 | -47.5418 | 2025-09-13 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 2b8b3f55-435c-32ad-9d00-5628321b4538 | -8.9595 | -44.4436 | 2025-09-13 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 195.4 |
| d646a946-4478-342c-a6d9-29d6c95f3c58 | -10.7104 | -50.4718 | 2025-09-13 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 55c1c696-b240-3829-9d97-b121962530c9 | -9.2843 | -59.418 | 2025-09-13 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 8e94fa70-a611-3d7e-b3a5-c5c09cc084f3 | -15.2454 | -52.8773 | 2025-09-13 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 71551373-3776-37d5-b49e-a2a027b0a939 | -15.1605 | -50.116 | 2025-09-13 14:00:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 226.3 |
| 45fe629a-621e-3fb9-834e-0b4c2b0a0ce5 | -9.9757 | -50.3548 | 2025-09-13 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 592407f8-e1b8-3916-ae3e-71a0d27cfa7c | -9.2656 | -59.4191 | 2025-09-13 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.1 |
| ec10020e-220e-3b2f-9038-13d3a2e0d454 | -10.1316 | -47.2065 | 2025-09-13 14:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| b7aca3e6-39cf-3dec-9575-adeeae78ce0d | -9.2505 | -51.2261 | 2025-09-13 14:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| f693821e-01c4-38f1-b644-e784f8f20754 | -18.0466 | -45.418 | 2025-09-13 14:00:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 146.3 |
| e139b270-ae9a-30e9-b03e-ada64ff5d99d | -10.6575 | -46.292 | 2025-09-13 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 9c19d12d-2f3c-38ef-a45b-c45fc31f4d7e | -9.5004 | -55.9788 | 2025-09-13 14:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 249.6 |
| 043132ec-0ac8-3a03-a9fb-aa5e17515406 | -8.9405 | -44.4457 | 2025-09-13 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 138.2 |
| e3ced501-8f74-3746-bac3-3395dcc0df61 | -16.1394 | -49.9392 | 2025-09-13 14:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 79ded895-de02-30df-8c67-679da427892d | -12.9294 | -54.7333 | 2025-09-13 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 5b3ec91e-42ed-3442-a662-6f0627405edb | -11.1896 | -51.419 | 2025-09-13 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 111.6 |
| ad8871a4-d5cc-3e8a-bd61-0c1564061ee7 | -18.0065 | -46.9499 | 2025-09-13 14:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 91243fc0-03f5-3327-85cd-93b2e33ec615 | -13.9379 | -48.2076 | 2025-09-13 14:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 4fb04356-729a-30d7-b6bc-1fceb46dc277 | -17.4142 | -49.2519 | 2025-09-13 14:00:00 | GOES-19 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 82df9d93-7bc1-3a0a-acb5-f0b65c0d38c6 | -12.8263 | -47.9263 | 2025-09-13 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 60e3d314-5841-34c8-8814-ba62596984e5 | -8.9365 | -46.1545 | 2025-09-13 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 4066688e-59f3-3702-acc4-9fb38eabf552 | -14.4199 | -47.3238 | 2025-09-13 14:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 7d33eb56-bb83-3128-a2b9-4d72c100ea86 | -10.3397 | -49.9333 | 2025-09-13 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |


[Clique aqui para ver as próximas entradas](README131.md)
