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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce47ce81-ec63-31e0-bd5f-bcadd5e5ce18 | -8.7399 | -48.3205 | 2026-05-31 00:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 29285813-e749-3aeb-92f0-e3557949a524 | -14.0494 | -58.1475 | 2026-05-31 00:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| ea23b5bf-9510-37cd-b93d-f694bf0a3d2b | -8.7396 | -48.3423 | 2026-05-31 00:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| ec8c6ee6-811b-30b4-9283-c99b3b9b11cd | -14.0302 | -58.1492 | 2026-05-31 00:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 5e371998-67ae-336f-b041-9fb62a970d3a | -10.0537 | -51.6576 | 2026-05-31 00:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 191.0 |
| 84544946-7f6d-3820-9ed7-8c3ae3b1a476 | -10.0725 | -51.6559 | 2026-05-31 00:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 566.8 |
| c727dd9e-565e-3983-b606-c93701409e43 | -10.0728 | -51.6349 | 2026-05-31 00:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 122.7 |
| ee157825-5749-34ab-868f-a8403a3fb14c | -10.0723 | -51.6769 | 2026-05-31 00:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 383.3 |
| f449c4ec-1f8b-38e4-b710-c893ba28b886 | -10.0534 | -51.6786 | 2026-05-31 00:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 168.5 |
| 751ab414-4c57-3504-8acf-3160b1d4318a | -8.7211 | -48.3222 | 2026-05-31 00:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 29cfaab6-a539-3fb0-8720-3f0265880aa2 | -8.7211 | -48.3222 | 2026-05-31 00:10:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 5c052c9d-dd73-351d-b8c1-4b397a84f1dc | -10.0537 | -51.6576 | 2026-05-31 00:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 219.5 |
| c25c551d-288d-33a0-82f5-d6d086555f6d | -10.0534 | -51.6786 | 2026-05-31 00:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 154.6 |
| b176e2b1-9d7e-3c83-8ecc-3bf5665fd0c1 | -14.0302 | -58.1492 | 2026-05-31 00:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 47.2 |
| b56837c2-4f93-303c-89e4-e8d5fe6e9f33 | -10.0723 | -51.6769 | 2026-05-31 00:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 312.3 |
| 2b6d0b4f-b256-3765-994f-62c1e0ff3237 | -8.7399 | -48.3205 | 2026-05-31 00:10:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 226e4b93-9d22-36a5-8e00-b1283456ecf9 | -10.0728 | -51.6349 | 2026-05-31 00:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 01c2bfaf-96f7-3bd9-b955-c9be3e94bfa8 | -10.0725 | -51.6559 | 2026-05-31 00:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 510.9 |
| 5c29bef8-8e8e-31c6-b9b3-3b08c2122ae2 | -7.9949 | -55.5169 | 2026-05-31 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 136.6 |
| 488bfa52-7143-39d4-a57d-70851fea9d3e | -14.0494 | -58.1475 | 2026-05-31 00:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 39a23796-2275-369a-bba2-0ef11fdf69d6 | -10.0561 | -51.662899 | 2026-05-31 00:11:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9bd56a26-1d29-3682-8ffc-be9e1bdb705d | -15.0531 | -49.457699 | 2026-05-31 00:11:00 | METOP-B | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2725cafa-fbc1-3a0a-a665-41fb96336e2b | -10.0703 | -51.633598 | 2026-05-31 00:11:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 91aa01bd-635f-3fd8-b107-2cf99591d2d3 | -12.4102 | -47.4869 | 2026-05-31 00:11:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 927a50c0-c4b9-3d6d-a216-590e73142f43 | -12.9068 | -52.518002 | 2026-05-31 00:11:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 910e5129-0342-37ca-895b-205fb3ba2f92 | -13.7101 | -52.957401 | 2026-05-31 00:11:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b807e1b1-b06f-3bc7-891c-4b0084b6c9dd | -6.838 | -47.923698 | 2026-05-31 00:11:00 | METOP-B | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9135ed07-7b6b-3102-a221-fb13710eea3e | -10.0721 | -51.641899 | 2026-05-31 00:11:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fc82bb83-6b52-397d-8a7b-3c697881cb2c | -8.73 | -48.3088 | 2026-05-31 00:11:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04bd0185-648b-32dd-aa4e-0dd559a9f6b6 | -10.0623 | -51.6441 | 2026-05-31 00:11:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 726860aa-9b8d-3782-9ac0-6df05a5bf139 | -10.0757 | -51.6586 | 2026-05-31 00:11:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fcb5ea31-5009-3fa8-a948-0517d6e4fd80 | -14.0296 | -58.122898 | 2026-05-31 00:11:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8d97c8c8-7943-339d-b7f7-d34e40190521 | -10.5106 | -42.352699 | 2026-05-31 00:11:00 | METOP-B | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 98c82b3c-c8f8-345e-a768-faf1326d90dc | -10.7922 | -46.900902 | 2026-05-31 00:11:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bf88b49e-ea23-3d31-8ad8-2b5cb0a53c80 | -10.0605 | -51.635799 | 2026-05-31 00:11:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4bef4b20-b7f6-3605-8e8b-44134319c215 | -10.7432 | -46.9123 | 2026-05-31 00:11:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9fc1aa4b-7fed-3f2b-93e3-1b4b1feb32b2 | -8.2562 | -48.219898 | 2026-05-31 00:11:00 | METOP-B | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 91743466-8531-3d87-a749-f578fa63267c | -9.4538 | -51.819401 | 2026-05-31 00:11:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee661465-d341-3ffa-a2d2-cd0ab718f1da | -6.044 | -47.879398 | 2026-05-31 00:11:00 | METOP-B | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 888aa61c-63b9-3151-b5e7-e10ca6f76a4f | -10.7449 | -46.919498 | 2026-05-31 00:11:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f4f04087-22d3-36dd-b419-41a7b185eaad | -10.0774 | -51.667 | 2026-05-31 00:11:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3991e8a0-e272-3080-a38c-0c3891093608 | -10.7465 | -46.926701 | 2026-05-31 00:11:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 30a7bded-23e8-326c-9748-b91c89bfc868 | -10.7645 | -46.914902 | 2026-05-31 00:11:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 63b0eaff-ada8-3e5e-b8d4-89b9e242b039 | -7.9965 | -55.502499 | 2026-05-31 00:11:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0cc6de6-5e71-302e-963d-8ead8f44c93b | -7.5023 | -54.997799 | 2026-05-31 00:11:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ad6dec7-1281-369d-92ed-11f86ae01479 | -12.3266 | -47.895599 | 2026-05-31 00:11:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2e008207-9a99-36c1-953d-cbd8b5e39e30 | -14.0393 | -58.121101 | 2026-05-31 00:11:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bdd23999-65f0-3d7e-ac90-8be30afab8be | -7.4997 | -54.985699 | 2026-05-31 00:11:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc26eb3f-8cd8-3b3d-b168-c82bc0c611dc | -10.0676 | -51.669201 | 2026-05-31 00:11:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 390d1172-76c5-3591-a713-1dd3b4faac9e | -10.7939 | -46.9081 | 2026-05-31 00:11:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 03cf854d-531d-3d32-b6eb-6d59e41c4eb0 | -13.7003 | -52.9594 | 2026-05-31 00:11:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cf976cd3-6074-3af5-ad6a-d56a540c5c86 | -12.9047 | -52.507801 | 2026-05-31 00:11:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 036270d2-a168-3616-bfc6-e7a7bb6256cf | -10.7628 | -46.9077 | 2026-05-31 00:11:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f65a44af-c326-3196-81c7-e0c23edfc726 | -12.3153 | -47.8908 | 2026-05-31 00:11:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| caa971a6-0d39-3a37-8a31-36564c0f3fa0 | -8.7315 | -48.3158 | 2026-05-31 00:11:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4526194b-f05b-36a2-8631-c3a5baf6d28e | -7.9937 | -55.489201 | 2026-05-31 00:11:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00782af6-d395-3663-807b-fcb9ca38b2f7 | -10.8004 | -46.891399 | 2026-05-31 00:11:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b919d8c8-354d-3204-b7bc-0758f1e7f99f | -11.9661 | -44.185799 | 2026-05-31 00:11:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f81af622-0fe6-335d-914e-8c8d5eb6608e | -10.0739 | -51.650299 | 2026-05-31 00:11:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7413a88a-30f1-3e31-9b16-6f4609d6f447 | -6.0457 | -47.8866 | 2026-05-31 00:11:00 | METOP-B | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b57a2cbf-ce9e-3aec-b4bd-89078b0350f4 | -7.9868 | -55.504501 | 2026-05-31 00:11:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51879dd2-74fb-34f6-a9f2-a62341f2fe81 | -8.2578 | -48.226799 | 2026-05-31 00:11:00 | METOP-B | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1f84a6b6-6fe6-38fe-95c5-66f32dac2e4d | -7.9993 | -55.5158 | 2026-05-31 00:11:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbcc0e35-68ec-3761-9247-b70377fc21fe | -10.0641 | -51.6525 | 2026-05-31 00:11:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e05d21d9-0d0f-3038-b3b9-489973752e47 | -6.8396 | -47.930801 | 2026-05-31 00:11:00 | METOP-B | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e9471f7c-8ada-36b6-a6c2-0b0dbf7e9684 | -15.0548 | -49.465401 | 2026-05-31 00:11:00 | METOP-B | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fc6779a8-0b85-36e7-a328-b460dad18847 | -21.2934 | -49.243198 | 2026-05-31 00:11:00 | METOP-B | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1b1b8b32-c8e4-300b-a66c-71ba1fade789 | -12.1316 | -47.211399 | 2026-05-31 00:11:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a84241c6-89cd-3eff-9c9f-0efbfec56aff | -12.3168 | -47.8978 | 2026-05-31 00:11:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7fc5e675-aff5-3dd3-9649-7e76a0128706 | -11.9639 | -44.176701 | 2026-05-31 00:11:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 833065d1-6fa4-318a-9e6a-61e0aef5050c | -8.7331 | -48.322701 | 2026-05-31 00:11:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9388b445-359e-3e03-ae43-8f79a1c54791 | -10.5135 | -42.364799 | 2026-05-31 00:11:00 | METOP-B | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2621fc21-6d3a-3bfe-ba22-25d55a67f3a4 | -10.0659 | -51.660801 | 2026-05-31 00:11:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 50b7469c-e6d8-369b-8173-7467e89c9e33 | -12.3251 | -47.888599 | 2026-05-31 00:11:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eaa816f6-5543-3627-95db-9086af21538d | -10.0543 | -51.654598 | 2026-05-31 00:11:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 903083c1-baee-3161-9e3f-f0325c5c79eb | -11.7927 | -54.004002 | 2026-05-31 00:11:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b6c187e4-c68b-37ae-b0d9-8fb0b2be0711 | -10.0725 | -51.6559 | 2026-05-31 00:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 405.0 |
| b86c4fc2-9012-3cfc-a64b-4f3cb816c7f9 | -10.0723 | -51.6769 | 2026-05-31 00:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 285.2 |
| e8b41de8-4d98-3953-9d67-b1d613772f1f | -10.0537 | -51.6576 | 2026-05-31 00:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 223.1 |
| 3d30d8d4-7bd1-328e-9b87-4e1e1ff9dc7c | -14.0494 | -58.1475 | 2026-05-31 00:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 43.8 |
| fe8f4535-fca2-39d5-9c92-a8cd76b54cb0 | -10.0728 | -51.6349 | 2026-05-31 00:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 99.5 |
| f5d0789f-d373-3dbb-84fa-623c7102f6f0 | -7.9949 | -55.5169 | 2026-05-31 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 90abe77c-4615-385d-bb03-b0415898f3fc | -8.7399 | -48.3205 | 2026-05-31 00:20:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 2ca1c631-71f9-38f4-8ce4-8b23406e4ffe | -10.0534 | -51.6786 | 2026-05-31 00:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 175.2 |
| c610e5a3-a240-3966-9793-63024ee6a6d2 | -8.7211 | -48.3222 | 2026-05-31 00:20:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| c7173427-cae3-3f9d-8c01-fded7aa3baba | -21.28643 | -49.25824 | 2026-05-31 00:24:00 | TERRA_M-M | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 24b2b8cc-d5b5-3295-9105-0840ac454139 | -19.19897 | -54.95306 | 2026-05-31 00:26:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f69934df-fd6f-38dc-b134-1d5097ed808a | -15.05334 | -49.46534 | 2026-05-31 00:26:00 | TERRA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 527e4888-22de-32ad-93c6-c7b3c36b3903 | -14.76595 | -52.69879 | 2026-05-31 00:26:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 816ff206-ff01-370e-837f-f9a1a6d01295 | -14.77108 | -52.6701 | 2026-05-31 00:26:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1fd92c82-79c6-3fa1-b130-f9410c2cd500 | -15.05494 | -49.47612 | 2026-05-31 00:26:00 | TERRA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 34.7 |
| c13c1b2e-d210-34e4-b1fd-b2153adb9509 | -10.57811 | -57.3171 | 2026-05-31 00:28:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f5ac0bbd-991a-35b2-9ec9-ef0db3bfecac | -7.50039 | -55.01257 | 2026-05-31 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 9b84f09f-ec6b-3e47-9d3c-e9dc23b39cdb | -7.99146 | -55.50993 | 2026-05-31 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 57859a33-1a13-37df-8d1d-fd429583703f | -7.99278 | -55.51972 | 2026-05-31 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 4ef44500-8872-3963-aa04-49c9d3279cc7 | -14.04041 | -58.14946 | 2026-05-31 00:28:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 48d03248-9ed6-3010-aa7d-1755808b91e5 | -6.83878 | -47.94306 | 2026-05-31 00:28:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| de4cf8e4-da99-3a5c-b4e9-009f30e63167 | -8.00056 | -55.52277 | 2026-05-31 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| fa05d04e-1512-39b8-a500-97d66d67b2c3 | -11.56565 | -54.57985 | 2026-05-31 00:28:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 982d0853-fa3e-38e9-89d3-03e29aaa18fd | -10.06662 | -51.64639 | 2026-05-31 00:28:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |


[Clique aqui para ver as próximas entradas](README2.md)
