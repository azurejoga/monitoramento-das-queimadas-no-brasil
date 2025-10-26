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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 063a2935-c26b-3086-a709-34931d2b9d27 | -3.10526 | -50.20707 | 2025-10-26 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97c2edde-b8ff-302e-a6df-5a24e93aab27 | -3.31512 | -50.11366 | 2025-10-26 04:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8ce16268-fd2b-3031-ac24-2bd5dae71ccd | -1.57411 | -53.45226 | 2025-10-26 04:49:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee89fec5-0a00-38a3-a334-16fd012efef7 | -1.37628 | -55.43373 | 2025-10-26 04:49:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9df8052-cabb-30ab-bca3-794f5e4c8a46 | -5.79073 | -48.6231 | 2025-10-26 04:49:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7733d062-cab6-3177-8890-8c01a8a0d30c | -3.52132 | -49.71315 | 2025-10-26 04:49:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c48ee7bf-6460-3f07-817a-e73d9ce281eb | -3.96242 | -45.41798 | 2025-10-26 04:49:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| ce2f92e8-4010-3ac1-a011-60222ecffdba | -3.85036 | -50.0141 | 2025-10-26 04:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d63d0b2-2e2b-3f43-bd7d-b2112116c918 | -6.58762 | -48.76804 | 2025-10-26 04:49:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 37b6dfa1-b823-338e-923b-ad337f3aaa8e | -5.11452 | -43.20293 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ceab3cb2-d6a9-3137-a101-58e386ab07d7 | -3.37424 | -52.80148 | 2025-10-26 04:49:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0bed38a-caca-38f5-b77e-376d58423a41 | -1.74983 | -55.74812 | 2025-10-26 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 187ba894-ddb1-3fa8-b41b-b496714f68c3 | -3.1022 | -51.28093 | 2025-10-26 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f2afb99e-7b5a-3e25-a012-27a810304631 | -0.01603 | -51.07689 | 2025-10-26 04:49:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 154b536a-b99b-395d-a5ec-6ce7ad2564e3 | -3.27275 | -50.05124 | 2025-10-26 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 234d333d-66ca-3d99-a71c-62767d98663f | -3.1102 | -51.20806 | 2025-10-26 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67032ee2-3598-31b1-a039-6df0d492ceaa | -3.83948 | -50.19638 | 2025-10-26 04:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 753ffcba-f8f7-377e-9e3d-0f24031a6036 | -4.25642 | -48.64323 | 2025-10-26 04:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5f1d995-3b78-34cd-b751-26a03d0f413c | -2.06246 | -56.8833 | 2025-10-26 04:49:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8c7aefa-16d5-3fa9-8da0-8f04f174dd5e | -1.18796 | -53.38499 | 2025-10-26 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9357c0cf-b24c-367c-a6b9-8fbadd531825 | -4.12483 | -46.88215 | 2025-10-26 04:49:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54185e4f-65bb-379a-b80b-483a90dc81ff | -3.10349 | -49.46175 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f8b7144-dfe5-312e-b5b1-2334cbc20200 | -3.46764 | -47.6842 | 2025-10-26 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7dafdd56-4c24-3e8f-8cd7-e75eb8095f0c | -3.23732 | -45.93628 | 2025-10-26 04:49:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 201ba46c-2c8e-3a97-a0e5-2e63a369bf2f | -4.15081 | -50.77335 | 2025-10-26 04:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96ee9d80-53f5-38a8-bfc0-ace2ec5ef677 | -5.92019 | -45.40823 | 2025-10-26 04:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fae75010-32ca-3778-9049-c05f72c64ae2 | -3.23021 | -52.91561 | 2025-10-26 04:49:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f2d83cb9-8b69-3495-bceb-21ae51dff1f8 | -3.6099 | -49.34338 | 2025-10-26 04:49:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1661e5cf-c776-3be3-9c25-f31c84010e55 | -4.78421 | -42.77219 | 2025-10-26 04:49:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 27.6 |
| ffcc1c9f-f4d9-3354-a9b9-6e194770cad5 | 1.62464 | -55.72811 | 2025-10-26 04:49:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e56ac4c-86de-3a01-9064-f2882559ae7c | -4.8006 | -47.88694 | 2025-10-26 04:49:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32267081-b752-3a8c-b6ab-1f0563ef8534 | -6.17772 | -49.87133 | 2025-10-26 04:49:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1ad4a8b1-3c70-3102-8d31-add0328f6fa6 | -3.10207 | -49.45464 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2b534463-31a6-3509-968c-2a89a111d48f | -7.05243 | -43.88135 | 2025-10-26 04:49:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38dde3f4-bac0-36cd-8507-4adee853a6cf | -4.29558 | -49.29029 | 2025-10-26 04:49:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8705fed-37d9-35b1-8032-06fe66a8f3a2 | -5.11496 | -43.19972 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdf64f6d-e6e8-38e1-be47-b561107eeaab | -5.2323 | -48.52615 | 2025-10-26 04:49:00 | NOAA-21 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ef172466-6498-3b1b-b949-761722805070 | -4.22085 | -48.36164 | 2025-10-26 04:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93635532-c976-3529-9e14-d756044b2024 | -2.77392 | -45.0913 | 2025-10-26 04:49:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb3ea81b-0f1a-3077-95f1-f0774c4a0994 | 1.38273 | -50.64357 | 2025-10-26 04:49:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c295ce8-19c1-316b-aea8-bffa510ce805 | -2.31109 | -48.55003 | 2025-10-26 04:49:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aea9500d-2b45-35a3-b5b2-f00ec945fcd5 | -3.10147 | -49.45844 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 44caa870-68b3-38c9-bf49-732ac7788ca4 | -6.0376 | -46.57265 | 2025-10-26 04:49:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad7c3419-7336-3347-8be9-482d1e5cb655 | -3.83609 | -50.19586 | 2025-10-26 04:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de3ced16-1389-31fe-927c-522be77445b2 | -3.81543 | -50.76485 | 2025-10-26 04:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41676269-7fb0-3dec-835a-04ef88f6554b | 1.13893 | -51.00087 | 2025-10-26 04:49:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f3bbca9-0264-303d-b971-ebc415f1f649 | -3.08626 | -49.51047 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5db537e-4a41-31cd-abf1-61677ad72829 | -6.66784 | -45.94049 | 2025-10-26 04:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 275fd260-7831-3d91-8cac-2ad34cdce614 | -3.26936 | -50.05071 | 2025-10-26 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bd976893-a452-366b-be66-5b3769644da3 | -5.11155 | -43.19025 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ed37e56-6f1a-3907-9cae-88537b0700e9 | -4.71329 | -46.43038 | 2025-10-26 04:49:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fefe7c07-2c34-38da-9afa-726199431659 | -6.73719 | -44.15086 | 2025-10-26 04:49:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7536b0d-36e4-352f-8b28-134101c29b01 | -3.64948 | -52.02432 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6709d9c6-aff8-3588-88a4-00c76b385fb4 | -3.09456 | -49.45736 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2cf5f810-dd22-3b8b-86ff-cb2d733bc284 | -4.03142 | -46.06927 | 2025-10-26 04:49:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e34ff221-c285-3724-a17c-dd12b4bd9da3 | -3.04695 | -51.22298 | 2025-10-26 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 159c3fc8-7dcc-3186-a3d6-aac6f9e7aa8a | -3.23247 | -45.93961 | 2025-10-26 04:49:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d4c7e07-1c2c-3ba0-aafe-32eb6d11daad | -5.50566 | -49.57676 | 2025-10-26 04:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3276fb5e-843b-3a11-b6dc-c8a83d8c5c67 | -3.4827 | -50.07874 | 2025-10-26 04:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef4f12cc-7b8b-3e6b-8fa8-edf6e94a7530 | -4.47587 | -45.33405 | 2025-10-26 04:49:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 045e5ddf-0ec2-3220-afa1-e48794abc3c9 | -5.39577 | -47.6111 | 2025-10-26 04:49:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4187d66-08e3-363c-8186-6c0b4cca9cf7 | 0.37238 | -50.91092 | 2025-10-26 04:49:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 237eaa47-7cfb-3243-b82d-2e00178fa8e7 | -2.9781 | -49.11565 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61698c5f-20d4-368f-96d7-0f897a6fef6d | -5.11108 | -43.19349 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6bfdb00-fd50-36dd-b40f-d64cbba491dc | -2.98657 | -52.62635 | 2025-10-26 04:49:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b5aa9a54-4646-3115-a8a7-f37203da330e | -3.76021 | -47.56554 | 2025-10-26 04:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 047e8b66-1399-3c69-9b8a-13bc3c9e73bc | -3.87133 | -52.19248 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5fc85ea-c3aa-3aa9-b074-4e258e7e38f1 | -4.58037 | -46.50962 | 2025-10-26 04:49:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2ffebf88-4b52-3618-9b38-17e2dd0e681b | -6.12559 | -47.01116 | 2025-10-26 04:49:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9bd24ae2-73e3-3018-9752-c4f6db2d4a01 | 0.42322 | -51.07809 | 2025-10-26 04:49:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65e75e6f-bc9b-3790-869d-dd1441580ca7 | -6.70259 | -42.04154 | 2025-10-26 04:49:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 84f56905-0d1e-3b79-a121-3c66d4e171cb | -4.61988 | -46.03354 | 2025-10-26 04:49:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22f7d814-8675-3315-9aeb-7d8d32b45e0a | -3.41782 | -52.67619 | 2025-10-26 04:49:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f768c91-8450-3510-909c-adacd030a1cd | -5.11541 | -43.19651 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed3ed779-9458-3a1c-b04d-3ea3caa6e4ba | -4.80497 | -43.306 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a1ed224-b427-32df-a4e3-fa717edbfe8c | -6.22503 | -41.38734 | 2025-10-26 04:49:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c334e564-b37e-31fd-9753-d9f2cb3de858 | -6.22463 | -42.54454 | 2025-10-26 04:49:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7e09177b-7972-3f34-a096-81addb9c6b0e | -6.83137 | -41.55264 | 2025-10-26 04:49:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7f6e1e26-f7df-35c9-a67e-d322a51b09ac | -4.00266 | -48.31814 | 2025-10-26 04:49:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33443c9b-8a94-398f-9ecb-9dbbd3a7e855 | -1.75367 | -55.74868 | 2025-10-26 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d83a8d7-0c41-3971-a17e-73eb256119f0 | -3.6087 | -49.3512 | 2025-10-26 04:49:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6d92c4b-1dfb-3b81-8e3e-3ea124d4b2cf | -4.88799 | -43.24989 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0888080b-e0e3-35d1-9679-a2306c75d1ba | -3.76646 | -47.57633 | 2025-10-26 04:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a28daf85-892e-3681-beee-1d6065340eaf | -4.8985 | -43.25141 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 52213554-18a5-3b2d-8621-800473feb82e | -5.77887 | -51.3961 | 2025-10-26 04:49:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6ff35895-4d2d-36dd-b7dc-9b2a21ee823b | -6.10313 | -47.04972 | 2025-10-26 04:49:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 939a1227-0017-3165-a641-b29ee84b4f6f | -4.02412 | -46.0016 | 2025-10-26 04:49:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ffa92cd-f70c-343d-acb3-6cd24d359f28 | -6.15412 | -43.13391 | 2025-10-26 04:49:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4ff9ae83-69bb-3ab2-aca8-3818ddd9b9cf | -6.44056 | -45.73445 | 2025-10-26 04:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f245b3e1-9fb0-3c59-a3db-e5cdd8717e91 | -2.64425 | -48.5045 | 2025-10-26 04:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89f50f37-37be-3537-9793-13f04bec45a0 | -4.30959 | -50.33839 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0bf1efbb-dcf8-3e7e-87c3-95e911d0dc51 | -2.9033 | -53.13261 | 2025-10-26 04:49:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1bd120a-84b4-3281-8aa6-a4dd716c1c9f | -6.60077 | -48.75631 | 2025-10-26 04:49:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85e7651f-900f-3f0e-8cff-0f8c8a866e07 | -3.72093 | -49.3043 | 2025-10-26 04:49:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ffa75730-60c7-3db4-b991-6a7d4c01c7b8 | -2.98132 | -51.33563 | 2025-10-26 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e7231e4-e953-3a56-bd2f-1794ea618f8e | -6.78713 | -45.40825 | 2025-10-26 04:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d25e7662-72da-34e9-87b3-558c622d0b76 | -4.20236 | -48.35884 | 2025-10-26 04:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0db0eb3c-efea-3cbd-9a46-efc8d03fc2d5 | -5.4148 | -46.33282 | 2025-10-26 04:49:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d32a9795-a9b7-3b5a-af09-6b3c02cc210e | -4.20196 | -54.93993 | 2025-10-26 04:49:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23cbc898-f43f-3c6f-a813-cf34cc749d9d | -3.31462 | -50.7915 | 2025-10-26 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README37.md)
