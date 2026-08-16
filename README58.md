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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed34e7e9-8c82-30db-b9fe-2e50b482645d | -12.0095 | -46.4271 | 2026-08-16 07:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 8718b9ec-bfcc-3f7e-8092-479ce7bbad76 | -8.9787 | -60.5156 | 2026-08-16 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 3e903be2-c682-3677-a2a6-89b945ebdbaa | -12.7017 | -48.4753 | 2026-08-16 07:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 18de3ab2-f7c9-3c43-9312-86af557dfd9f | -14.901 | -46.6283 | 2026-08-16 07:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| fadee98c-0efa-3de0-b7ec-755b8128a782 | -14.9005 | -46.6512 | 2026-08-16 07:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 8370f556-d0e0-34ed-af1b-38105b241fb3 | -6.7123 | -58.9412 | 2026-08-16 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| cf9ecca8-8224-3711-a27c-4158c6541e98 | -8.96 | -60.5358 | 2026-08-16 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 1e2898b1-f789-314a-b3bf-05de31bc0472 | -12.0091 | -46.4498 | 2026-08-16 07:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 198.1 |
| 47324866-9d0b-3972-9132-c0374670bf85 | -12.0095 | -46.4271 | 2026-08-16 07:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| b83bd745-8e22-36b4-bfd7-71f026bfa317 | -6.7123 | -58.9412 | 2026-08-16 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| c37cbcbb-3b37-31ff-8b1a-17da14f74c89 | -8.96 | -60.5358 | 2026-08-16 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 6e3dd4d4-0a4b-36c7-b10f-de40b7ded1a6 | -12.0282 | -46.4471 | 2026-08-16 07:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 0dda5889-9412-3b53-9483-75c506759574 | -8.9601 | -60.5165 | 2026-08-16 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 42796a0c-7c2d-30c4-9ec5-beb2a10189f4 | -8.9787 | -60.5156 | 2026-08-16 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| c15bee0c-ff8a-3eb6-80fc-dda56d58d545 | -6.3137 | -43.6178 | 2026-08-16 07:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 043deab5-c54a-3ad6-9558-670357cb8f7c | -7.8452 | -38.6967 | 2026-08-16 07:30:00 | GOES-19 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 65.2 |
| 8b3320fb-92dd-3cd0-bb4f-e7426e2e974f | -12.0091 | -46.4498 | 2026-08-16 07:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 155.5 |
| 4f91bd0f-ff67-3bda-b935-2ece20688541 | -12.0286 | -46.4244 | 2026-08-16 07:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 89082d32-724b-321b-b5d5-c3337c35932d | -6.1107 | -57.723 | 2026-08-16 07:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 23f328c0-4295-3338-9ee3-9022a14a20b5 | -12.7017 | -48.4753 | 2026-08-16 07:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 0c3de8d8-a3bf-3361-88d8-af0786abae4a | -12.0282 | -46.4471 | 2026-08-16 07:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| c280fb7e-6135-3b8f-8dc6-10112e9df0c8 | -6.1107 | -57.723 | 2026-08-16 07:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| f2773063-8078-38b1-a75f-5ca6645022ac | -8.9601 | -60.5165 | 2026-08-16 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| d20fbd35-d8fe-3a83-b8c1-df89480c21d7 | -12.0095 | -46.4271 | 2026-08-16 07:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| ab76d709-cc50-3585-81eb-67de81c3666e | -8.96 | -60.5358 | 2026-08-16 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 89c57de2-9a45-3092-bfbf-3b3aa366d8ff | -7.8452 | -38.6967 | 2026-08-16 07:40:00 | GOES-19 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 82.4 |
| d2f4c51d-e975-3c08-bc8f-e2ccc0c9711a | -7.8642 | -38.6942 | 2026-08-16 07:40:00 | GOES-19 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 70.8 |
| c6cafea3-b1ee-3085-a7fd-399b055e509f | -6.7123 | -58.9412 | 2026-08-16 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 345191d8-2035-3ab9-9ca2-9f8ed9d07145 | -8.9787 | -60.5156 | 2026-08-16 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| e2776f6a-41a3-3d6f-8a80-88e397222e95 | -12.0091 | -46.4498 | 2026-08-16 07:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 127.9 |
| a8ff47e1-a105-32c7-bba9-66ec4bc6bc75 | -12.0091 | -46.4498 | 2026-08-16 07:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 109.0 |
| f3a4bb12-f59a-3ff6-946a-78c56240cfe7 | -6.1107 | -57.723 | 2026-08-16 07:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 76232ec4-0ebe-3cb2-93f4-efa0646e82cf | -12.0282 | -46.4471 | 2026-08-16 07:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| ce623e45-9874-3203-b520-a73fbbd098e6 | -15.2454 | -49.7524 | 2026-08-16 07:50:00 | GOES-19 | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 61.1 |
| ea447839-7f73-3760-afa4-7922aa5f5401 | -7.8452 | -38.6967 | 2026-08-16 07:50:00 | GOES-19 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 77.5 |
| 66e96846-d7cc-3c95-93a4-7f3866d74201 | -6.7123 | -58.9412 | 2026-08-16 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| a09ba7b5-918e-3257-b7eb-d2e21b70e5d5 | -8.9787 | -60.5156 | 2026-08-16 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| da4158cd-5be5-3932-81e3-5ca91b8d8894 | -12.0095 | -46.4271 | 2026-08-16 07:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 8e5016e1-ceae-3dba-be8f-2b4fc3efd2c9 | -8.96 | -60.5358 | 2026-08-16 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 1ac2739f-c21e-3428-b891-7f6eefddc5d4 | -8.9601 | -60.5165 | 2026-08-16 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| d26d8f3e-6288-3463-aae2-d4068a1748f2 | -12.7017 | -48.4753 | 2026-08-16 07:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 5a6dda6e-2de7-32a4-a282-48dad3390481 | -8.9601 | -60.5165 | 2026-08-16 08:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| a1b750ff-16e1-398c-bc60-494a10f91e1a | -12.0282 | -46.4471 | 2026-08-16 08:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 6ddceffd-02f6-39fa-b38f-d53aa3fc466b | -15.245 | -49.7744 | 2026-08-16 08:00:00 | GOES-19 | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 61.3 |
| ae2c8e07-6d59-31c1-b139-a29f723175c0 | -12.7017 | -48.4753 | 2026-08-16 08:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 6c9eda94-bef7-3222-89ef-c12f9a06d6cf | -6.7123 | -58.9412 | 2026-08-16 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 136bf595-ccf6-3fb1-9951-1c433f57f0d0 | -8.96 | -60.5358 | 2026-08-16 08:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 474e01e7-2b36-3567-b889-d268b09b6f48 | -12.0095 | -46.4271 | 2026-08-16 08:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 92f51e9f-3828-33cd-b518-619191df0d1f | -12.0091 | -46.4498 | 2026-08-16 08:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 928bcf18-8ae9-37e4-9a5a-ee866b63b66d | -8.9787 | -60.5156 | 2026-08-16 08:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| dd9257a6-3dfb-34b4-b5aa-eb69f0fa14e7 | -15.2454 | -49.7524 | 2026-08-16 08:00:00 | GOES-19 | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 0e269d5f-968c-359a-aaa6-43897a412d96 | -6.7123 | -58.9412 | 2026-08-16 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 0cbb58a9-262a-313a-bec0-47a9769e3dd3 | -8.9787 | -60.5156 | 2026-08-16 08:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| aaeb1321-39cb-3e7e-86ba-025dcfd3faee | -12.0095 | -46.4271 | 2026-08-16 08:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| f4951e81-b3fe-38f5-8958-1534829ea777 | -12.6828 | -48.4558 | 2026-08-16 08:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 28b3214d-22d9-3f93-871e-e06b5877c5e7 | -12.7021 | -48.4532 | 2026-08-16 08:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 00b4e1a4-eff3-33e8-9175-6ee4d835f7bb | -8.96 | -60.5358 | 2026-08-16 08:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| d8905286-99a0-3478-838c-983ee74d120d | -12.7017 | -48.4753 | 2026-08-16 08:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 175b5c9f-ad67-3142-a92f-1fede3ea211f | -8.9601 | -60.5165 | 2026-08-16 08:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 1656822a-549e-3607-88c3-925fa7a30426 | -12.0091 | -46.4498 | 2026-08-16 08:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 125.8 |
| eb60fe26-ad5a-34dd-a774-fe79f9e23262 | -12.0282 | -46.4471 | 2026-08-16 08:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 2f0b2890-39b0-328c-8ffc-4811a7a7d3e7 | -12.6825 | -48.4779 | 2026-08-16 08:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 555faec9-bd1c-354c-87c5-87f9a13f8dba | -8.9601 | -60.5165 | 2026-08-16 08:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 7710ede3-30f3-370e-b050-47ddc6372370 | -12.0282 | -46.4471 | 2026-08-16 08:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 1905cc63-2194-3c2a-988b-bde84377fa66 | -6.7123 | -58.9412 | 2026-08-16 08:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| fe65bc39-8095-3c37-a768-2245f2bb78d0 | -12.0091 | -46.4498 | 2026-08-16 08:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 64ea9b9a-2a23-3b26-a9bb-0950e3e297ec | -12.7017 | -48.4753 | 2026-08-16 08:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |
| c0746d32-8365-3207-85c1-ce5c479f0cd7 | -8.96 | -60.5358 | 2026-08-16 08:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| cb1aee04-b9fb-3c0b-82d3-a474a20a4cc8 | -12.0095 | -46.4271 | 2026-08-16 08:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 705b58bf-dcdb-3739-b588-efa60a86d1e5 | -8.9787 | -60.5156 | 2026-08-16 08:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 4bfb7bc8-ac93-35eb-9ef0-fa543cad085b | -8.9787 | -60.5156 | 2026-08-16 08:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| a0068171-ef0d-313a-9d45-bef91112780d | -6.7123 | -58.9412 | 2026-08-16 08:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 8a6f2022-7a64-3cb1-8e63-564a392fcfb0 | -12.7017 | -48.4753 | 2026-08-16 08:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 1b437ba7-3fb8-3e97-9cf8-97a93538077d | -8.9601 | -60.5165 | 2026-08-16 08:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 8e48d0a7-be47-3267-ba7e-407cc181ea32 | -8.96 | -60.5358 | 2026-08-16 08:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 676b020b-9181-32c2-88ce-225cbceaa6e4 | -12.7209 | -48.4727 | 2026-08-16 08:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| ea9a63d4-7f59-359a-af25-bc6a83fd4196 | -12.0091 | -46.4498 | 2026-08-16 08:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 57439c08-4b8d-3440-ae80-f314780dcc0b | -12.0282 | -46.4471 | 2026-08-16 08:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 4626b4d0-387c-33a0-ac4b-189532cc69e5 | -12.0095 | -46.4271 | 2026-08-16 08:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 6946a696-1aa1-3bca-a7f9-f88f8f400dd8 | -12.0091 | -46.4498 | 2026-08-16 08:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| aa738be9-56a3-31df-9b8c-093f66694dfb | -12.7017 | -48.4753 | 2026-08-16 08:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| b5ec0eac-5286-3da0-bd85-c6569243e849 | -8.96 | -60.5358 | 2026-08-16 08:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 16e3f096-9d41-3ff4-8ebf-a390e7435b8d | -8.9601 | -60.5165 | 2026-08-16 08:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 8c4341f7-78a8-3d27-8c63-17f3e942f5b2 | -12.0282 | -46.4471 | 2026-08-16 08:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 5efa505d-4dcf-3ea6-a222-bd87cb8a421e | -12.0095 | -46.4271 | 2026-08-16 08:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 056d91db-8e81-3527-8cc6-485a42cbdfc7 | -8.9787 | -60.5156 | 2026-08-16 08:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| b1aa3139-7282-3987-a67b-22e361936ed3 | -8.96 | -60.5358 | 2026-08-16 08:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| c963afa0-f2f6-3433-8e5e-14ca71598f1d | -6.7123 | -58.9412 | 2026-08-16 08:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 6b4d5d0f-8789-31bd-ac74-e6258c7c02c2 | -8.9787 | -60.5156 | 2026-08-16 08:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| aa2c155a-3489-3e51-9dbc-4a61c4351669 | -8.4275 | -62.676 | 2026-08-16 08:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 00083163-217c-30a4-9218-72815a626363 | -12.7017 | -48.4753 | 2026-08-16 08:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 6dcacff0-69a9-3f18-b400-00f85614a2ae | -8.9601 | -60.5165 | 2026-08-16 08:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 32422275-a932-3609-a38f-52ae77a2b65e | -8.96 | -60.5358 | 2026-08-16 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 8566a488-16df-3b13-9cc3-db2e70e89ee6 | -8.9787 | -60.5156 | 2026-08-16 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 36b624db-6e92-3b4f-bf68-f9e9706b48b6 | -8.9601 | -60.5165 | 2026-08-16 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| f5090b97-b838-3a79-8850-d89d02007efc | -6.1107 | -57.723 | 2026-08-16 09:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 34ecfb1e-8dd1-3a03-b527-c7bc159aeb18 | -8.9787 | -60.5156 | 2026-08-16 09:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| c81dab6b-5ab3-37f3-9a97-c17825e80da9 | -8.9601 | -60.5165 | 2026-08-16 09:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| e13f56d1-e0ac-3623-afdd-42c16910dbb0 | -8.4275 | -62.676 | 2026-08-16 09:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.9 |
| a885d74d-05ce-38a4-9c3b-fdfa93b9a520 | -8.96 | -60.5358 | 2026-08-16 09:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |


[Clique aqui para ver as próximas entradas](README59.md)
