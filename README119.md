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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5756d50-8568-38b1-9760-d385d27d1a58 | -18.0497 | -50.9571 | 2025-09-13 08:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 69.1 |
| de4712fe-928a-3215-8cd4-2eb6fafacf8f | -11.1429 | -50.6815 | 2025-09-13 08:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 0508eb5a-514c-37d3-b817-900fb8206f0e | -9.5137 | -54.6292 | 2025-09-13 08:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 395c6df8-187b-3572-8f19-5035e5c391d9 | -11.7575 | -46.6205 | 2025-09-13 08:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 0ddcfe94-9750-3c1f-9593-d80bce2bb0d3 | -9.5324 | -54.6277 | 2025-09-13 08:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 156.5 |
| 38eb5371-b6ae-39ac-915b-9275a47298a5 | -18.0303 | -50.9385 | 2025-09-13 08:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 10a706fb-fff2-3efe-9e03-825612d513de | -9.5324 | -54.6277 | 2025-09-13 08:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 114.1 |
| ab42d3d2-ebb5-3b62-b5de-e3f49e98f32d | -11.35 | -50.7867 | 2025-09-13 08:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 32b0fbfb-9ad8-3c95-ac31-e0670a29717a | -11.8284 | -50.5406 | 2025-09-13 08:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 525c3e3b-c619-3da0-83cd-f0a4cdef58eb | -9.2658 | -59.3997 | 2025-09-13 08:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 139.9 |
| 6c6c254e-e2a6-31bc-8027-7d6d427628f1 | -9.5137 | -54.6292 | 2025-09-13 08:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 32a9631f-b09f-3ee4-a45d-32d5220a05b2 | -11.7571 | -46.6431 | 2025-09-13 08:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 0ccef054-2e91-3bfa-9797-b0e575942960 | -9.2656 | -59.4191 | 2025-09-13 08:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 105.5 |
| ca01fe73-9e73-3917-a2ba-514ee87c3c32 | -9.5324 | -54.6277 | 2025-09-13 08:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 6b49a9ab-e1ae-33ca-8878-0f11881ce243 | -11.8094 | -50.5428 | 2025-09-13 08:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 6e63ff8e-0a68-37eb-a43d-961a57cda671 | -11.5809 | -50.569 | 2025-09-13 08:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 43a4fe42-613d-3abc-8042-24aa22abc00b | -11.8284 | -50.5406 | 2025-09-13 08:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| a2083241-324f-3aa7-a6d8-f38379b6af00 | -9.2658 | -59.3997 | 2025-09-13 08:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 5f1c4671-3b62-3a87-94c0-6aa8da083012 | -9.2656 | -59.4191 | 2025-09-13 08:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 5cb1ce60-65d8-3c93-b67c-6fc87db3270f | -16.433 | -49.0474 | 2025-09-13 08:30:00 | GOES-19 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 046e7d5a-4334-3acb-9442-f61a99a94803 | -9.5137 | -54.6292 | 2025-09-13 08:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 80a89bab-9ded-39b1-ae87-fa3cf5873111 | -9.2656 | -59.4191 | 2025-09-13 08:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 23d6ed9d-702e-3bd2-9981-78c432ec7a5a | -9.2658 | -59.3997 | 2025-09-13 08:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 3503ab49-e17e-3a8c-9246-b3b8aed6e0c1 | -9.5324 | -54.6277 | 2025-09-13 08:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 7c8184c9-f394-3ef8-8a50-e5c4a774d19d | -11.8284 | -50.5406 | 2025-09-13 08:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 12d99a3c-2aac-3cd5-97c3-0fa8a79bc57f | -9.5137 | -54.6292 | 2025-09-13 08:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 29262d84-160e-368a-aac8-c8e8362d6810 | -9.5324 | -54.6277 | 2025-09-13 08:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| baf9fd05-8c78-3aa7-b1fc-3757cde875c0 | -9.2658 | -59.3997 | 2025-09-13 08:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 117.6 |
| c1c06b50-a05a-3965-8c51-43ff65c4fa98 | -9.5137 | -54.6292 | 2025-09-13 08:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 817faf48-8c45-3fb7-88ca-ebe81ed26c2d | -9.2656 | -59.4191 | 2025-09-13 08:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 501c5593-8e03-3006-8253-eec75993b8b1 | -9.2844 | -59.3986 | 2025-09-13 08:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| ea87ef95-53e7-3fd4-b49c-6e0d22549bdc | -9.2843 | -59.418 | 2025-09-13 08:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 8728df76-e5da-3dd1-8256-4bd3492abe8e | -9.2656 | -59.4191 | 2025-09-13 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 116.1 |
| fc987017-0a2e-3bc6-92b1-538fb7aef3f9 | -9.2658 | -59.3997 | 2025-09-13 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 139.0 |
| 6d1baae1-17c3-377c-a4b9-117563e41085 | -9.2658 | -59.3997 | 2025-09-13 09:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 143.1 |
| 6e6434d9-8431-3a8e-84ac-d47bcbcd6d5f | -14.1698 | -46.2735 | 2025-09-13 09:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 0cbd1a5d-4f6b-3a90-823c-4f2b6e2a15c2 | -9.2656 | -59.4191 | 2025-09-13 09:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 102.8 |
| c98ebaaa-554c-3d33-8751-ceab091ebdea | -14.2083 | -46.2899 | 2025-09-13 09:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 124.8 |
| e10a6fee-605b-3ed4-8be1-4d13bb629bab | -14.1698 | -46.2735 | 2025-09-13 09:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 155.6 |
| a6ca3a11-7790-3545-94f5-09c0bd7efdd9 | -14.2083 | -46.2899 | 2025-09-13 09:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 29dbbc77-fcb5-38b8-94a2-57f12b0f5725 | -11.5809 | -50.569 | 2025-09-13 09:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 151.1 |
| f049262d-4404-3f5f-8551-1f79e878f5fb | -10.9283 | -47.2223 | 2025-09-13 09:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 186.7 |
| 13e8af66-74e7-37d6-99f6-954e2f05bddc | -14.2078 | -46.3129 | 2025-09-13 09:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 149.3 |
| cab05c78-f498-3b93-990f-413940fd78d4 | -11.5809 | -50.569 | 2025-09-13 09:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.6 |
| d8d2f926-b2af-3c50-9b8f-5ad27552c1ea | -14.1698 | -46.2735 | 2025-09-13 09:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 181.9 |
| ca2015b0-078d-3477-8491-fdb01a243cdb | -11.8287 | -50.5192 | 2025-09-13 09:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 9491d444-7886-3934-b70c-bd76d486c43b | -11.8284 | -50.5406 | 2025-09-13 09:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 232.5 |
| 8cce1234-c42c-3964-8e89-075583de259d | -11.8094 | -50.5428 | 2025-09-13 09:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 138.9 |
| f0c7c3a9-2e64-3af0-8775-b22b43839c67 | -14.2083 | -46.2899 | 2025-09-13 09:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 59bd54a8-c004-3a96-b32a-d482ab1d5d44 | -10.9283 | -47.2223 | 2025-09-13 09:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 127.6 |
| b0d47d24-2e9a-3cb4-b82b-d19864515663 | -11.8094 | -50.5428 | 2025-09-13 09:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 0d5687ee-930c-36cb-848e-94a571f476c7 | -11.8284 | -50.5406 | 2025-09-13 09:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 237.7 |
| 718554fe-26b4-38c4-b0ac-b684658d8c3a | -10.9283 | -47.2223 | 2025-09-13 09:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 21c82c4a-4c7e-3ad2-b6f6-ec999ed84839 | -14.1698 | -46.2735 | 2025-09-13 09:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 184.7 |
| 72cf8b42-8b37-3d21-8ed6-0a790a12edec | -11.8287 | -50.5192 | 2025-09-13 09:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 171.4 |
| 016deb93-3937-3474-b3c9-e12fa06ef618 | -11.7575 | -46.6205 | 2025-09-13 09:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 56181ae9-0d49-3938-b83e-408a26ffd6cc | -11.8094 | -50.5428 | 2025-09-13 09:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 224.1 |
| c10db3a3-22f6-30df-8251-90fd822f087f | -10.9283 | -47.2223 | 2025-09-13 09:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 410c2041-0333-3eca-af63-8d27683b9368 | -11.8287 | -50.5192 | 2025-09-13 09:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 402.3 |
| a97901a2-9739-31c4-8509-31df453b90ab | -10.9473 | -47.2199 | 2025-09-13 09:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 115.4 |
| ae03bb58-deee-39cb-8414-73abd06a8c5e | -11.8284 | -50.5406 | 2025-09-13 09:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 333.1 |
| eb30a4fb-d82a-3c43-a73a-dcbf967fa4d2 | -14.2078 | -46.3129 | 2025-09-13 09:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 5af24c94-f923-39ca-9d14-e7f839133ef9 | -11.8097 | -50.5214 | 2025-09-13 09:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 189.3 |
| 3bffe951-393c-36fe-ab9c-c21f61983829 | -14.1698 | -46.2735 | 2025-09-13 09:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 179.6 |
| e5f777b4-1894-3fbe-9cce-455586a0b10b | -11.8097 | -50.5214 | 2025-09-13 10:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| a8c1e662-80a3-3ea2-b6a5-ea9fe7b8935b | -11.7575 | -46.6205 | 2025-09-13 10:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 438cc9be-6fff-3181-b552-66fcb64409a8 | -11.8287 | -50.5192 | 2025-09-13 10:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 380.7 |
| 670fef8f-d431-3074-8164-e711aa3d9e21 | -14.1694 | -46.2965 | 2025-09-13 10:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 161.4 |
| b813df45-47b9-3e7d-a632-3d063f43c8f4 | -14.1698 | -46.2735 | 2025-09-13 10:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 404.7 |
| 49733147-8b83-37b8-ad49-55893ffb3385 | -11.8284 | -50.5406 | 2025-09-13 10:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 276.8 |
| 7636d35e-d21e-39d7-a73a-015cf543079f | -14.1893 | -46.2702 | 2025-09-13 10:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 70101ea4-efc8-3123-8555-e145f763ef76 | -14.1504 | -46.2768 | 2025-09-13 10:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 6426a2de-997d-3045-b7a6-f34e6ec90a8e | -9.2658 | -59.3997 | 2025-09-13 10:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 192a0508-5617-3968-b3d6-cdc2a7f44873 | -14.1893 | -46.2702 | 2025-09-13 10:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 56a3fc3c-5e53-3ef4-927d-97114e1d1f65 | -14.1694 | -46.2965 | 2025-09-13 10:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 560891c1-3e5b-379b-b9a1-232f47ca7316 | -11.8287 | -50.5192 | 2025-09-13 10:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.0 |
| a890f3ce-c53b-3947-9773-9b03298f8c34 | -11.7903 | -50.545 | 2025-09-13 10:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| aa1d1037-de13-3900-9677-702285c22df7 | -14.1698 | -46.2735 | 2025-09-13 10:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 314.5 |
| edbabde6-b5c2-3a27-8eae-8311f70d346f | -14.1703 | -46.2505 | 2025-09-13 10:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 9658888b-c9dd-3786-aeb9-bf7d02d45a59 | -14.1893 | -46.2702 | 2025-09-13 10:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 5e56f728-c113-35b6-bf82-d346f37eccfe | -14.1888 | -46.2932 | 2025-09-13 10:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 120.3 |
| f27f8363-2b49-383e-8024-733b94b44fd1 | -14.1694 | -46.2965 | 2025-09-13 10:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 171.4 |
| f207965d-4c59-39a2-b7ae-e89e042611f5 | -14.2083 | -46.2899 | 2025-09-13 10:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 7c0e3555-d315-38d4-9bbd-21f159eaae41 | -11.7903 | -50.545 | 2025-09-13 10:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.8 |
| c2ab6da2-9431-3fe3-822d-23a9bac4073a | -11.124 | -50.6835 | 2025-09-13 10:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.9 |
| aa41b505-406c-34dd-bb1b-5ab48476fbf6 | -11.7575 | -46.6205 | 2025-09-13 10:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| bfada793-554a-31b6-8a74-37c72dea8ff7 | -14.1698 | -46.2735 | 2025-09-13 10:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 309.4 |
| 6360c0c3-5581-3f99-9007-f46a5b1f6cb5 | -14.2078 | -46.3129 | 2025-09-13 10:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 7af00e1c-340a-3909-b1eb-0536d84d30e4 | -11.7575 | -46.6205 | 2025-09-13 10:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 127.8 |
| fe9592b2-c732-32af-ac51-8b7fa14f5c23 | -14.8708 | -49.0395 | 2025-09-13 10:30:00 | GOES-19 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 8f40cf58-0bd3-3006-936e-c4895546fb5c | -11.8475 | -50.5384 | 2025-09-13 10:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 1a9eebc8-90ec-3f0d-821d-93eeb70b5947 | -11.7903 | -50.545 | 2025-09-13 10:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| ccc7a686-8b24-39de-8b79-bfcc781346e1 | -14.29 | -46.0924 | 2025-09-13 10:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 7926d849-1b82-30a4-ad81-96f5ffd6fbb6 | -14.1888 | -46.2932 | 2025-09-13 10:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 0e655626-b17b-3cb9-9f72-a9e775724397 | -14.1893 | -46.2702 | 2025-09-13 10:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 39e71b4c-4906-33d6-b673-a3fad57a6e13 | -11.7204 | -46.5579 | 2025-09-13 10:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 114.2 |
| fdcfa42f-fa3b-3a2b-a90e-1c48698c9251 | -11.8478 | -50.517 | 2025-09-13 10:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 5d58df46-fb02-3bda-a43b-c7b04f130dc3 | -14.2078 | -46.3129 | 2025-09-13 10:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 154.8 |
| b9b8e1b8-96bf-3aff-a8ec-fa42ec3f8848 | -14.3095 | -46.089 | 2025-09-13 10:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 105.6 |
| dcd19176-17e5-30f1-8a2a-047f0a5fe654 | -11.8287 | -50.5192 | 2025-09-13 10:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |


[Clique aqui para ver as próximas entradas](README120.md)
