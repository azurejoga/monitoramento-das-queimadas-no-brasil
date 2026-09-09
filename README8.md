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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5246f94d-1fa0-3708-a3bb-3ca27bfc4327 | -2.9576 | -50.4826 | 2026-09-09 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 615f93fe-b886-3e19-89cc-dbdba48ce618 | -1.1991 | -55.7106 | 2026-09-09 01:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| cfbd6f3f-0152-369b-ad6d-86fad3d3f512 | -3.2486 | -47.2438 | 2026-09-09 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| ef9d687b-373e-3502-a6c6-ee8bdc55e616 | -6.1723 | -44.666 | 2026-09-09 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 99fe405b-2bc0-3265-9636-f40d9f4310ec | -2.9391 | -50.4832 | 2026-09-09 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| fd820cb9-aa16-391c-b882-e92a690914b6 | -6.1726 | -44.6432 | 2026-09-09 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 7bb7a1df-c68c-3e22-975c-d9e385ce961d | -5.7758 | -45.0599 | 2026-09-09 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 0b458556-b49f-3ffb-8906-aefad0514de4 | -5.7756 | -45.0826 | 2026-09-09 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 9eb6207c-6d17-338c-aa0e-75bcfcb27cc6 | -9.7695 | -43.506 | 2026-09-09 01:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 0b676514-ffed-3771-ad80-f872b60187dc | -6.1536 | -44.6675 | 2026-09-09 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 5fad1bfd-80eb-3c0b-afd2-12428a3e56b8 | -2.9392 | -50.4622 | 2026-09-09 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 9a8b77f0-2fbc-308a-841a-5c501f72e97f | -6.3703 | -43.5898 | 2026-09-09 01:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 7e7a70ed-1a6e-3cc6-be4d-fc5da8dfbd4c | -1.1991 | -55.7106 | 2026-09-09 01:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| e7d21430-c271-3f16-861d-b529986238cc | -6.1538 | -44.6446 | 2026-09-09 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| b6213f4d-b96a-3f17-81e6-3850ca868644 | -9.7885 | -43.5036 | 2026-09-09 01:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 56e4f2f5-30f6-3e25-9180-76ddb8e5d410 | -2.9576 | -50.4826 | 2026-09-09 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 373730fb-b0ac-3398-8e73-ee5a2c6c4d53 | -5.7569 | -45.084 | 2026-09-09 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 7a79f7f8-08f6-384a-ae09-b21e45b2fac6 | -5.7758 | -45.0599 | 2026-09-09 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| c940488f-afff-33ef-b210-3a1101691420 | -6.1538 | -44.6446 | 2026-09-09 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| dee423ae-e6ad-3139-bb08-f48eaebeedf9 | -3.2486 | -47.2438 | 2026-09-09 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 9b4981db-76fd-3fad-b46e-2d79995df5e5 | -6.1726 | -44.6432 | 2026-09-09 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| d09dabbe-c8cb-356a-8850-7fceb23f4937 | -2.9392 | -50.4622 | 2026-09-09 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 16c967e2-69d9-37b1-9f0c-528f688f5130 | -5.7756 | -45.0826 | 2026-09-09 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 650001d1-be9b-39bc-820d-f3d84fe82986 | -8.7253 | -62.4177 | 2026-09-09 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 21a4c498-995e-3493-807e-f195c281636f | -6.1536 | -44.6675 | 2026-09-09 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 6a0b0980-5203-3740-bfa9-6a94778a3caf | -5.7569 | -45.084 | 2026-09-09 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 3b3cf3c3-a944-3a1f-a838-393c3b931493 | -2.9391 | -50.4832 | 2026-09-09 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| b12e8372-f2e6-3d94-be1b-b52764f0b9b7 | -9.7695 | -43.506 | 2026-09-09 01:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 166.1 |
| 34bf0946-519e-34b8-bf81-b570b8cee8f4 | -9.7885 | -43.5036 | 2026-09-09 01:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 6208fdff-ee5d-3ad8-b6a2-5bb0df235de2 | -6.1723 | -44.666 | 2026-09-09 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| ddf83cc5-d794-364f-9a1c-35ebb9ed2cf1 | -9.7691 | -43.5296 | 2026-09-09 01:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| aafa4be5-785f-38f4-a529-f00904efe30f | -2.9576 | -50.4826 | 2026-09-09 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 7337608f-9cff-38f8-b9eb-7f5d0e212945 | -2.9577 | -50.4617 | 2026-09-09 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| dae1fdda-6149-3cb1-b066-3704f828c092 | -6.1536 | -44.6675 | 2026-09-09 01:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 9396edb6-7c98-3e81-b71d-8e02e0b818f2 | -2.9576 | -50.4826 | 2026-09-09 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| a77357c0-4a62-3331-808c-9d52b37d8204 | -3.2486 | -47.2438 | 2026-09-09 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 32dacacd-6bb6-3259-b2de-40143cfa80de | -6.1723 | -44.666 | 2026-09-09 01:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| a9871bff-ea3e-37d1-a1aa-3c1580b1bb6b | -5.7756 | -45.0826 | 2026-09-09 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 02113106-74ec-3cbe-8b6e-cb10af086332 | -5.7569 | -45.084 | 2026-09-09 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 61320507-9b99-3e6d-a6de-786495d561b8 | -2.9392 | -50.4622 | 2026-09-09 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 3ca14605-ae91-386d-9cc7-d572fb326e29 | -6.3703 | -43.5898 | 2026-09-09 01:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 4d6594b3-bd46-302f-83bb-cecbe04dc7c2 | -2.9391 | -50.4832 | 2026-09-09 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 141b3b80-b1ad-3bf2-9c0c-f64db67db26e | -5.7758 | -45.0599 | 2026-09-09 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| a3921d9e-a6bc-389b-b146-23eb9c445649 | -6.1726 | -44.6432 | 2026-09-09 01:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 2c313c3a-7590-3c31-afd9-bb8d9ac06aa8 | -2.9577 | -50.4617 | 2026-09-09 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 6125f177-8437-3fb3-9aa7-a680d44ee54b | -2.9391 | -50.4832 | 2026-09-09 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 897100bb-d0ae-3d2b-8537-1fffffb30422 | -10.7578 | -45.9624 | 2026-09-09 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.3 |
| a5d00931-912a-3169-a456-7a5430368d1b | -6.1538 | -44.6446 | 2026-09-09 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 980c9085-5b88-304a-99e0-764aaa34dddd | -5.7758 | -45.0599 | 2026-09-09 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 4315fdb3-5ee6-36b9-84ec-d01c72ab31e7 | -1.1991 | -55.7106 | 2026-09-09 02:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 040a9941-816d-3b67-92fa-f039d7f8bf27 | -3.2486 | -47.2438 | 2026-09-09 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 057d6c6f-41da-3086-b4d5-425dcebd3337 | -6.1726 | -44.6432 | 2026-09-09 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 787448d1-88e8-3557-bf81-230ace476eed | -5.7756 | -45.0826 | 2026-09-09 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 119.5 |
| de6ee2df-5ce9-3ec7-8959-40c6f7901625 | -5.7569 | -45.084 | 2026-09-09 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 978707c8-73e8-3834-a5e1-3a008b5a90db | -2.9392 | -50.4622 | 2026-09-09 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 3112f605-fa42-3235-b9c6-13b35eb8335f | -6.1536 | -44.6675 | 2026-09-09 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 81546e60-e7d8-3f7b-9b2e-d39bfe641e10 | -10.7582 | -45.9397 | 2026-09-09 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| bba3d461-ae07-398e-b516-9e087cb13063 | -3.2486 | -47.2438 | 2026-09-09 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| ac5781a3-f165-355a-be18-8fa67758a1bc | -2.9391 | -50.4832 | 2026-09-09 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| c0049cfc-8daf-3859-9aae-9ca4e1dd8ba8 | -6.1536 | -44.6675 | 2026-09-09 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 0c6f3f82-beef-312a-9e52-edc41c735e84 | -5.7756 | -45.0826 | 2026-09-09 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 31c01a71-05e8-3a50-bf4b-5bd98c07eb23 | -6.1726 | -44.6432 | 2026-09-09 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 507d709d-f917-3877-ae29-c804b3b1da49 | -5.7758 | -45.0599 | 2026-09-09 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 277d2c90-94ef-36c7-be42-97c49f767ac9 | -2.9392 | -50.4622 | 2026-09-09 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| ccc6c77c-69a9-33f9-88b2-73a44b754bd5 | -6.3703 | -43.5898 | 2026-09-09 02:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 469c017e-049f-3764-953a-3f242a2cae16 | -10.7578 | -45.9624 | 2026-09-09 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 7109f067-5f05-349b-a840-fe7c88e6c732 | -5.7569 | -45.084 | 2026-09-09 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 54052757-eb15-3a50-bf51-fc8df658677f | -6.1723 | -44.666 | 2026-09-09 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| baeef574-9477-3226-a592-2c20853aaff1 | -6.1538 | -44.6446 | 2026-09-09 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| a68da2d7-0fd1-3bd0-a56c-2904400d225c | -10.7578 | -45.9624 | 2026-09-09 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 71ead0ad-cab6-3056-91d9-ecb0accc0fce | -3.2486 | -47.2438 | 2026-09-09 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| e9cce2b2-2132-3949-b979-23c408794fc7 | -6.3703 | -43.5898 | 2026-09-09 02:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 9745b1bd-e4c8-3552-87a4-873346c3a639 | -6.1726 | -44.6432 | 2026-09-09 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 007e0706-4523-30ff-98cf-db5dddb937b0 | -6.1536 | -44.6675 | 2026-09-09 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| f5fe3b75-0335-30d4-9411-32584e052a45 | -2.9392 | -50.4622 | 2026-09-09 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 414f9251-c579-3837-8eda-68a7a17ee543 | -6.1723 | -44.666 | 2026-09-09 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 3385ed2a-f54f-3dbe-86cf-25ec02c91dce | -10.7582 | -45.9397 | 2026-09-09 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| e99dc767-ef40-3336-9d52-78ee3e680ed2 | -5.7756 | -45.0826 | 2026-09-09 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| d41672b2-df93-300d-8b34-8c46527273b2 | -2.9391 | -50.4832 | 2026-09-09 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 5ff59240-a8fe-3bba-abad-256289305400 | -5.7569 | -45.084 | 2026-09-09 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 66abf355-9802-3947-ba2a-4d9533e16352 | -5.7758 | -45.0599 | 2026-09-09 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 95fdf3c3-c075-3bea-bd47-c3ada76481a3 | -6.1538 | -44.6446 | 2026-09-09 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 89bca43b-deed-3f2b-968c-3479bd92b248 | -6.1726 | -44.6432 | 2026-09-09 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| a90a5bdc-6e4f-3e1f-b0fc-4d53339a86e0 | -2.9391 | -50.4832 | 2026-09-09 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| f58f2877-e13f-3a0b-ac82-635b8d8c499f | -6.1536 | -44.6675 | 2026-09-09 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| f0dba308-150e-325a-a9e5-31d1c7785fac | -6.1538 | -44.6446 | 2026-09-09 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| c8244cd8-b27f-3d92-85cc-fc5a2768078b | -5.7756 | -45.0826 | 2026-09-09 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 3a3a4cfd-2e36-3cb9-b000-2c0d5de34cea | -3.2486 | -47.2438 | 2026-09-09 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 27b8d000-4245-3d2a-b82f-ab92d000d6c0 | -2.9392 | -50.4622 | 2026-09-09 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 4b2b4c81-04d8-3a92-a5ce-c34867bbab9e | -5.7569 | -45.084 | 2026-09-09 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 8e384b69-3afe-3702-96f1-24604e67a92e | -5.7758 | -45.0599 | 2026-09-09 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| d791785b-cd00-39bd-881c-9e70a6754bb1 | -6.1723 | -44.666 | 2026-09-09 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| b46385f2-efa5-3552-8362-89ef0831b5ad | -6.1723 | -44.666 | 2026-09-09 02:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 073737f2-051c-36c5-b5fc-a6d7ff01522a | -2.9391 | -50.4832 | 2026-09-09 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 48217157-1c87-308f-bfc1-a7d0ad59f547 | -6.1538 | -44.6446 | 2026-09-09 02:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 8bec9d1f-9577-3019-b363-38412bce373f | -6.1726 | -44.6432 | 2026-09-09 02:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| d5d47dc6-e1ef-37c9-b539-4792abfd3f8e | -5.7569 | -45.084 | 2026-09-09 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| fd21f771-d1c5-3162-9705-d2d5eb96e1f6 | -5.7756 | -45.0826 | 2026-09-09 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 75dc3ef8-ffb8-33f3-9315-a608f165a0e3 | -2.9392 | -50.4622 | 2026-09-09 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| bd1a4e3d-f726-333e-94d8-701f3ffa015b | -5.7758 | -45.0599 | 2026-09-09 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |


[Clique aqui para ver as próximas entradas](README9.md)
