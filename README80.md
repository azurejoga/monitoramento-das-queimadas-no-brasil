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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2808b6e2-4c86-3144-95f8-91667802db4c | -2.29594 | -48.48943 | 2024-10-08 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05ff54ee-6de4-3947-8c9d-d2588755953b | -4.39666 | -48.69239 | 2024-10-08 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d9d7f714-abea-3abf-a3cc-312b4e63c2c0 | -4.39612 | -48.69599 | 2024-10-08 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b449a49b-e6a0-3391-a7ab-eec971f8c520 | -4.39264 | -48.69178 | 2024-10-08 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 773e3437-a7cf-3e1d-95c2-f9230f430fee | -4.3921 | -48.69536 | 2024-10-08 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f0167687-d57c-313d-acaa-28eb1e93e9d5 | -4.38301 | -48.70112 | 2024-10-08 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 93a5b3fd-1b1b-3f80-9c6c-2e04428aac88 | -4.37899 | -48.70053 | 2024-10-08 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fdc8cfd4-6d70-3f9b-bda8-fbc188ca767c | -4.37548 | -48.69646 | 2024-10-08 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4ec103ff-5985-3b9a-9e30-2b65e9d2244b | -4.37497 | -48.69989 | 2024-10-08 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8aca9ce3-5e45-3a9d-91d7-4cec697e800e | -4.36065 | -48.21529 | 2024-10-08 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9490daa7-c93d-3ccc-9254-48965fbe1028 | -4.36008 | -48.21908 | 2024-10-08 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4fa41102-f6f6-30cf-98fe-cac6837eebc9 | -4.21655 | -48.87449 | 2024-10-08 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c423bf1e-3fd8-3305-9869-ced824c2970c | -4.19138 | -48.57104 | 2024-10-08 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c6631c8-bc93-3b4e-975f-e9b02e082d55 | -4.18735 | -48.57033 | 2024-10-08 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7f855222-c4bc-3d11-b777-261204726418 | -4.09763 | -48.25232 | 2024-10-08 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c162504b-362f-326a-9eea-7a782d8aceb4 | -4.09709 | -48.25602 | 2024-10-08 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 99ef9a68-e32e-3b8a-b9c4-12da81540da9 | -4.09655 | -48.25967 | 2024-10-08 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e3baff6c-4384-31bb-9d0b-2499276e398b | -4.09601 | -48.26332 | 2024-10-08 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6726a8ef-7a21-3d73-b059-1ee36d29fd8c | -4.09546 | -48.26699 | 2024-10-08 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 991f4b01-8473-3b33-aed9-aba6bcaed1a2 | -4.09242 | -48.25907 | 2024-10-08 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e99d3f59-c2a4-3fb3-ae75-12b683cdd9f9 | -3.91397 | -48.34822 | 2024-10-08 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28903bc6-a22b-3e61-9860-d564e71b5f73 | -3.90987 | -48.34768 | 2024-10-08 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 14c67f37-81a2-3dd1-88c0-834bc1f3fba9 | -3.90933 | -48.35123 | 2024-10-08 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 84827ab1-31c2-3066-9ad8-0b17511bfa6a | -3.90631 | -48.34357 | 2024-10-08 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 143ea13d-d617-32e0-82a9-c83c859f63a8 | -3.90577 | -48.34716 | 2024-10-08 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4fd4e620-a20d-3296-83d3-de984eb95067 | -3.90222 | -48.34298 | 2024-10-08 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd62b8fd-c7dc-3f69-a1ff-298a47b13219 | -3.90061 | -48.35363 | 2024-10-08 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e2874cc-fe0c-3a7c-9ef3-277091e5b037 | -6.22814 | -48.16039 | 2024-10-08 04:55:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97adec2c-5f4d-3220-b2c1-7fe3df8aaf21 | -6.22754 | -48.16441 | 2024-10-08 04:55:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98e3e78b-a9d5-34be-b728-e113516e9bb4 | -5.7529 | -49.25466 | 2024-10-08 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c691d944-485d-3d15-b0e0-08962f8d9b39 | -5.75228 | -49.2509 | 2024-10-08 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d1a1129c-6ee1-3e2b-a9de-3cf5c0aca9f9 | -5.74895 | -49.25404 | 2024-10-08 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd72a399-f7fc-3e75-a172-fbecfbb81fc2 | -5.745 | -49.25342 | 2024-10-08 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2851fcb8-3086-3ca6-bb0f-500991ea7a15 | -5.71144 | -49.31534 | 2024-10-08 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f162778b-083c-3eb3-a83a-823a3e89541a | -5.706 | -49.32478 | 2024-10-08 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 650d91a9-0953-3694-8e9a-e020685f7cd2 | -5.46176 | -48.91024 | 2024-10-08 04:55:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a2f75ba-0bfd-3997-9f7d-d5ee5f1650d3 | -7.49492 | -49.44427 | 2024-10-08 04:55:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 328953f3-bc2f-3c2e-b988-39876150db2f | -1.44788 | -48.8787 | 2024-10-08 04:55:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9074ddd5-1000-39cb-81f3-27cb5cf5d4cf | -1.44716 | -48.88332 | 2024-10-08 04:55:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72a71781-026a-35d6-bff3-6477c0dd0e7c | -1.44406 | -48.87811 | 2024-10-08 04:55:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 686f1e36-c70f-3238-a915-166f7c98d2c1 | -3.50865 | -50.26934 | 2024-10-08 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f59ccc73-ab40-3365-a199-b3ca1bd7e719 | -3.508 | -50.27351 | 2024-10-08 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73bcb658-e836-3531-8ce8-4a6d27899f25 | -3.50438 | -50.27296 | 2024-10-08 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe8dc09a-5a01-3af0-b613-b5e0737e000b | -3.50076 | -50.27241 | 2024-10-08 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07ca195e-3bbb-3166-a3e2-cb8320e86f6d | -3.48812 | -50.49746 | 2024-10-08 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e12a1384-901f-339b-a030-ce6953844147 | -3.14653 | -50.22625 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 281bf5f1-851d-3fa2-8d86-ba34f1a9f4e5 | -3.14589 | -50.23041 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e348cd8d-cab9-3269-bf2c-e2cae9d3b81f | -3.10656 | -50.39231 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ea78cba-4d6c-39fa-ad38-36a0d8089ec3 | -3.10559 | -50.38952 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b34c046-d235-3567-bc01-c7a323f24fd2 | -3.10497 | -50.39351 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c556bd45-257d-3504-9d69-8ff82a36de36 | -3.10419 | -50.38375 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 62b1337a-de23-31d9-b6ed-99fbd1f4879e | -3.10357 | -50.38779 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0bc73e13-16a0-3352-a8b0-e076cec83b2d | -3.10263 | -50.38497 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ce8aa5b-4425-3dea-8856-1de8945e3ce9 | -3.10261 | -50.46653 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fea92d5b-3393-32a8-9c49-3b9af28c5d06 | -3.09903 | -50.46598 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8f003db-4838-38b6-b02f-1c0e018d6bba | -3.0977 | -50.46301 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9c7b572f-3133-3a7c-a83b-b3d667243b28 | -3.09706 | -50.46706 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8d6d2773-1fea-3661-b4be-5ef80e356da5 | -3.09608 | -50.46139 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef81a16f-90b3-3cdd-84d5-40e427e7d9a8 | -3.09412 | -50.46247 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b011198e-d7c2-3e73-8a6d-e742df7ed9e6 | -3.06472 | -50.48684 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1c97e1d-940e-3d5f-824b-d98cfc86ef2b | -3.03948 | -50.43742 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d197524f-a8f9-3103-af7d-73ccbe206af4 | -3.03591 | -50.43685 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38236b69-9396-324c-aa4a-9dc7bc799a09 | -3.03527 | -50.44097 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d3427d0c-f26c-3ed6-a5ea-7ceba5c55c7e | -2.89384 | -50.39505 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29eca361-cf10-370d-9451-9956bb8a01b0 | -2.89323 | -50.39909 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc42fcd3-fd05-3422-b1ef-a6eb90d13b46 | -2.89206 | -50.39622 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe407e8f-1555-3d7e-8868-a324637a6f36 | -2.89143 | -50.40024 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66510fa4-fb6d-30c1-9a2e-fea2b5024ad0 | -2.88965 | -50.39854 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e5a73d8-bd9a-3550-8e0d-37c7fa7a5581 | -2.45586 | -50.25521 | 2024-10-08 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42731763-da8a-3062-a0b6-bf9ccaf9015c | -2.45523 | -50.25927 | 2024-10-08 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6551c125-2ef5-3ea9-a40f-397493cef271 | -2.45228 | -50.25466 | 2024-10-08 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 751b928f-563f-3cbd-8c0a-1a460d546997 | -2.45164 | -50.25872 | 2024-10-08 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31572b60-67e4-366b-8766-4d650b49c068 | -3.32654 | -49.13973 | 2024-10-08 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72af2c3b-9bbe-3b24-9c23-af1e0f6f2d8c | -3.32582 | -49.14449 | 2024-10-08 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79ff8c82-c413-326a-bc7b-2aca52ff3e38 | -3.25923 | -49.10801 | 2024-10-08 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 821afbf5-3ab1-3532-9ec1-9759a032116d | -3.16028 | -49.7509 | 2024-10-08 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e2dbb1f-34b2-305f-b8d7-f65150463244 | -3.06396 | -49.57481 | 2024-10-08 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24a31357-7b99-38ce-9307-52aafd23bf32 | -2.98639 | -49.52874 | 2024-10-08 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86345685-d88a-3765-975d-1b3c76b91378 | -2.98334 | -49.52365 | 2024-10-08 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35b61986-0d79-392d-9422-9617991b5645 | -2.98264 | -49.52815 | 2024-10-08 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 49a24de1-3cd4-3de5-b962-f2565a335738 | -2.98195 | -49.53262 | 2024-10-08 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 2cb2cffd-4ece-376e-9f60-020ae9f99d5a | -2.97959 | -49.52306 | 2024-10-08 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b02a810-ec95-350f-bfb1-6ae96b16a250 | -2.9789 | -49.52756 | 2024-10-08 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9d3b3ef2-f2f9-36c9-96e7-930bb216792e | -2.87906 | -49.47322 | 2024-10-08 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47e757f3-2ce4-373b-8623-855b78370af7 | -2.87425 | -49.14868 | 2024-10-08 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dabc5471-fe6e-35b1-944d-31ea321900d5 | -2.75116 | -49.52913 | 2024-10-08 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a1a9a8e2-e6a1-3a43-afa7-0e535ffbaceb | -2.72364 | -49.53403 | 2024-10-08 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2da00ca-ffcc-31ce-b92d-43d3943a6889 | -2.72297 | -49.53847 | 2024-10-08 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 580d79c0-6569-3798-9620-7d3a7b5ba4e2 | -2.64024 | -49.26897 | 2024-10-08 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9a6f2eb6-8e44-3b2a-a5f2-6488e3d7bac2 | -2.60754 | -49.2851 | 2024-10-08 04:55:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed2a1cdb-08e7-3fc6-b328-e666f37d2e5e | -2.53281 | -49.01997 | 2024-10-08 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b2828e4-d775-3d9d-b621-593499ab4ce6 | -2.53207 | -49.02467 | 2024-10-08 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37716222-2be5-34f3-b805-8970e8fdff8e | -2.40653 | -49.18907 | 2024-10-08 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a824cfa1-2370-32c0-8b21-3cd061280cb7 | -2.34868 | -48.99244 | 2024-10-08 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c67ec18-a320-3fb5-be81-f39383c458f4 | -2.34731 | -48.98959 | 2024-10-08 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 492dce7a-7ab0-342d-a5bf-2e151a9c353d | -3.68301 | -50.2501 | 2024-10-08 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d63498a-bde6-3a60-847f-9cee4d6a29bf | -3.5783 | -50.39694 | 2024-10-08 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f70f4560-941b-3fb5-ace5-01729625a818 | -4.85378 | -50.7725 | 2024-10-08 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9655ce5d-6a0f-3e0b-9149-35c077271e12 | -4.85082 | -50.76788 | 2024-10-08 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76408a7d-a0ee-334b-a14d-c382d8ec218b | -4.82416 | -50.82209 | 2024-10-08 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README81.md)
