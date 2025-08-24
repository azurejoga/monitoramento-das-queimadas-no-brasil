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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fafeb44f-218a-3ac4-bcdc-7707977dc3d4 | -9.25562 | -59.63685 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 474e1d02-e1cc-3fc2-a523-926a5d519e58 | -8.84203 | -49.89267 | 2025-08-24 04:59:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc3bd197-6530-37b4-b51a-cf4753b1dcda | -8.75486 | -46.75362 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c529bd17-6fec-3335-b591-b7b5e0f1d799 | -7.54473 | -63.84504 | 2025-08-24 04:59:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3704313-3bd8-3955-8f39-c5d0da67af37 | -9.15694 | -59.46301 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 608edbf4-9543-3e0a-b2b4-ca406efe7326 | -9.20502 | -60.79159 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 6e1070b8-3523-3a40-a2d6-410cba08612a | -8.60951 | -62.64601 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2de4a588-c96b-3e43-99c4-3a93e67eba93 | -9.15208 | -59.46743 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 17f32b38-acd3-31d9-8734-1547d50043e2 | -11.10744 | -44.76377 | 2025-08-24 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5100025-0e86-38b2-8ef6-531764b45ddd | -8.85979 | -52.04271 | 2025-08-24 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 239c76f1-706f-3db0-b9ac-d7d2339337d6 | -9.18625 | -59.62548 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b6bdedc-2894-3fb6-8a15-d08bc955bd73 | -9.16219 | -59.47977 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2f5bc960-6831-3a29-a589-1ee9a82bab3a | -10.63331 | -51.61555 | 2025-08-24 04:59:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f707005e-c55e-3a69-9c80-06a15c2f4088 | -9.1674 | -59.46248 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ca5cfaa5-e88b-360a-8563-885a8deda2be | -10.64371 | -51.62146 | 2025-08-24 04:59:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3297810-7255-393e-a853-3f186ac9f7b6 | -7.81033 | -46.62299 | 2025-08-24 04:59:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 80c623fa-d2f5-3597-84f0-5da82a7af5f1 | -8.18751 | -45.0813 | 2025-08-24 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 234b8111-05db-3433-9cfa-c1551fc2bd9b | -11.13426 | -46.334 | 2025-08-24 04:59:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| faa489e3-6342-369f-a83e-340173cf16ee | -8.71493 | -51.1409 | 2025-08-24 04:59:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e66ae00d-53c7-3fec-b4e9-d1ccb4be4bd9 | -8.68005 | -62.88076 | 2025-08-24 04:59:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 62a26257-f0a5-38fa-a002-d956ab8d0295 | -7.60919 | -60.8353 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ade10394-88bc-346c-ae41-34f66407e1b8 | -8.91731 | -62.41853 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fd6e9a22-2479-3ac0-a6af-a295c0730768 | -9.15822 | -59.47908 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 279d0529-f7dc-3588-b1e7-f41e7ebfeeb3 | -9.16168 | -59.50618 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6c84830-97a7-3173-a114-733776462937 | -8.62937 | -62.6228 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9bcd4f02-89aa-33a3-96b6-a013f19ce56c | -10.57922 | -47.14548 | 2025-08-24 04:59:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5045f8e-352a-38be-8d6d-0752853b0b9d | -9.14116 | -60.76861 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 96f69882-445e-3b58-96c6-74ee1f68752a | -7.75514 | -47.35326 | 2025-08-24 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 208a37b8-1442-39e1-9ee2-dbce889525ae | -7.43309 | -60.62836 | 2025-08-24 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a428fc38-f745-3cab-a0cb-518b5b1d619f | -9.22218 | -59.75512 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f63c1fc4-2684-333b-a58f-1238cec7bd0c | -9.10732 | -61.42789 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5dd2a9fa-d277-310e-a63a-498a4b98dd84 | -9.15783 | -59.45791 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 6da70b00-f145-3120-b006-b9fdf74652fd | -7.75448 | -47.35793 | 2025-08-24 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f5dfde71-2201-383f-899b-79851c1e1694 | -8.74404 | -46.724 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 71887a2a-e936-34bc-b2a4-c53d1835213d | -6.87776 | -59.8214 | 2025-08-24 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf989ca6-4283-377b-907a-64f0cc1ca82e | -10.60923 | -44.32434 | 2025-08-24 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| f60744af-a9cb-35a6-904a-d6e307c0935d | -9.14983 | -59.46994 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9bc6829d-1a11-33e0-acd9-dc983139c9e1 | -11.13412 | -46.33591 | 2025-08-24 04:59:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c4a19b0-d4a7-3ec4-9e15-d3b021eb2e62 | -9.17116 | -60.80676 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 102f2c24-ef34-336e-acd5-ba1aaa49a87d | -10.60869 | -44.32862 | 2025-08-24 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| fa3d83bd-6c8e-30b0-ad3e-641776a037fc | -6.68404 | -58.85373 | 2025-08-24 04:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e161ffdd-62f8-3cbc-b611-c135ab219bd7 | -9.03002 | -59.01585 | 2025-08-24 04:59:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c487e17-37a1-3b2e-b785-efea63161174 | -7.92959 | -45.91887 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9f7d444-53c1-3ad1-8913-676fbaa70ece | -9.15257 | -59.50226 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d74d656b-4025-3628-98f6-68d5726b2273 | -6.57465 | -59.87622 | 2025-08-24 04:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78e3c4c5-a5e5-330b-8ade-5c922f35d8ba | -9.1618 | -59.45859 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1304058f-7320-3902-b48b-cc5ab237ae2f | -8.89795 | -62.41494 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 600f1571-99f9-3402-b845-62e031c9962f | -9.023 | -47.64542 | 2025-08-24 04:59:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5b5182b1-e03d-30fe-a417-49406cbf0f87 | -10.41329 | -47.17667 | 2025-08-24 04:59:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dc482ae3-2855-3e26-a0f8-72578aeba9bc | -10.63488 | -51.61341 | 2025-08-24 04:59:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 851b22d8-3aa1-3c05-8897-7182b987ad72 | -10.57851 | -47.15073 | 2025-08-24 04:59:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 691221c2-43a4-3678-8ea1-ce231dde0afc | -9.22254 | -59.75508 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9611150-b9a4-3932-b55c-a46abf03ee6f | -9.19855 | -60.77771 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6354e266-7684-3f94-b105-fe28fed45f93 | -9.16224 | -59.49337 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 58e4da5d-bc16-309d-a1e1-6fff874cf5cb | -9.16258 | -59.4669 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0adede9a-e26a-3918-a1fe-a4675584a11d | -9.03293 | -47.64194 | 2025-08-24 04:59:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eed76d81-651a-36ef-b480-7164a8b52a56 | -9.15988 | -59.51649 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4a2be112-feae-396f-ac26-4d98ddc13723 | -11.10594 | -44.77569 | 2025-08-24 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aee4edec-1db4-3fd4-ae3f-04e70e99b09b | -9.25252 | -59.63096 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a476ee5-0409-3e0c-8441-e3fe3ae75f1c | -10.53378 | -47.14967 | 2025-08-24 04:59:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 533cf5c7-b843-3be6-b1cf-c49cac0a0847 | -7.43822 | -60.62482 | 2025-08-24 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d887970-d3fa-3660-ba15-f9f72aca21ff | -9.19711 | -60.78595 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e8a4090c-36fe-30e8-bb9a-d42e334d14a3 | -8.83917 | -49.89495 | 2025-08-24 04:59:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 135bc25b-adba-3c4a-9d66-3f38187b4839 | -8.88633 | -62.39624 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0bef777f-6375-3ee3-abed-1db1f0486dd7 | -6.63104 | -58.41191 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59e3652b-8a63-31d2-97d7-33cddb0da9d0 | -6.38557 | -62.91395 | 2025-08-24 04:59:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| c6128a5c-17cf-36c2-973a-2c9337cc945c | -8.15243 | -47.30346 | 2025-08-24 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad73a773-c3e5-3b53-9f73-dc6029994928 | -9.15515 | -59.47323 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a6e70cd0-f467-35da-ae35-a43a534753a6 | -9.15065 | -59.49898 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 332c889c-057a-3e0c-8bfc-8dcb7f6d666f | -8.74588 | -46.72097 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fa8f1b99-02f7-385a-bd45-8576bcc142e6 | -9.23184 | -60.92389 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 85c35d83-5799-39d9-8bd2-e5968a42de87 | -9.16569 | -59.47272 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 623ddd21-cc69-341b-b547-9486afa4528c | -6.92662 | -62.8913 | 2025-08-24 04:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 97162212-681a-3282-b1a5-ac975d555158 | -8.68507 | -62.88168 | 2025-08-24 04:59:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fbecf380-5d33-3e52-a6b4-1ffdc4b6d53c | -7.57223 | -63.43765 | 2025-08-24 04:59:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c72c7c56-0c89-3e55-96ba-bb465f9508db | -8.61145 | -62.60582 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4f034505-7728-3817-a10d-2f2b4a52c605 | -8.84381 | -49.90861 | 2025-08-24 04:59:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88688741-de4d-30df-9914-2178c4ed20cf | -6.92388 | -52.85508 | 2025-08-24 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cd72508-1c05-32a2-9932-a79ef91e5f65 | -9.1486 | -59.50156 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ebcf7f65-2fdd-30bb-b5bd-709ca6b95b2a | -10.76143 | -48.26701 | 2025-08-24 04:59:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ec275247-eed3-3fb5-8f8c-58feeec5e1b3 | -8.84057 | -49.90294 | 2025-08-24 04:59:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe8e35ab-0216-386d-899f-0c09fd946136 | -9.16078 | -59.51133 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 18eea0ca-8524-3803-a583-35e7141c5c42 | -9.10281 | -61.42706 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 589142a7-9910-30f8-b785-6c4f5f3d9ee8 | -9.16039 | -59.4901 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e29ce103-1052-3fd5-97b2-3c59041f4a1d | -8.77159 | -46.75295 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 980da0c9-305c-3ab3-8af4-fdeb38d131ce | -5.61485 | -60.23543 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ec8cd7c6-26ec-3f1b-beed-0a4b83b0b229 | -8.06431 | -49.65422 | 2025-08-24 04:59:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ed9536e-1cdf-347e-88b4-8acb98db59dc | -9.17029 | -59.59855 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5eb4da8a-3bde-360e-bf8e-669c7bde2296 | -9.18162 | -59.462 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2449738d-be46-31db-9435-6737ce17fb53 | -8.03691 | -44.99964 | 2025-08-24 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe808ae1-6c5c-3820-a12f-b0f1ef336556 | -9.81508 | -46.44226 | 2025-08-24 04:59:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d999f63-9a00-3acf-b453-55a8a0edf38a | -9.22049 | -59.618 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94eaa4e2-22e5-393e-a422-6335e82deda7 | -10.65309 | -50.12307 | 2025-08-24 04:59:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4340284a-ea11-350f-be4f-8ffa400cf4da | -9.23611 | -60.92204 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 467f0416-2f81-3502-823f-56a1546f05aa | -7.07514 | -60.05994 | 2025-08-24 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb791c49-4050-3591-b01c-f7043ee72e57 | -8.91347 | -62.44001 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7dd740bc-094f-3cef-a0d4-3863b022a2fd | -9.20358 | -60.79986 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 65d01ac8-76f0-3e38-b4b6-40eaaf39c74d | -8.61662 | -62.60887 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bcff87ec-14e1-3b46-b5b2-610cba757686 | -9.15429 | -59.492 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bfe3ec0a-edcf-394d-a75f-c24b0bb0e392 | -7.81276 | -46.62589 | 2025-08-24 04:59:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |


[Clique aqui para ver as próximas entradas](README55.md)
