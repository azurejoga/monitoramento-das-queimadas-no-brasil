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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c08a90c-c42e-3883-aa98-09b4171defaf | -7.3888 | -59.97409 | 2026-08-10 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee144b7e-f2dd-33cf-ad1e-8c6f0a039781 | -8.95638 | -60.60255 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d2736e50-8e1a-3021-a2f1-d86f2143f29d | -6.84965 | -56.40854 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abdc045f-a904-311c-8fc8-f051d3da49c3 | -7.69201 | -55.16793 | 2026-08-10 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e048f7e-bc8e-3ea1-b29c-f7914bdf1ede | -7.15025 | -59.62487 | 2026-08-10 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a98cc747-a1b6-38bf-80b3-eacfff0cded6 | -6.81459 | -56.42374 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b2c084e-ba4f-3d08-b443-34b669497cf1 | -8.16628 | -61.51993 | 2026-08-10 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 511bce7e-6361-324e-b761-79f7f88665f2 | -2.90718 | -54.14846 | 2026-08-10 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d65a5e9-9e82-3338-aa74-def1b6a7faa4 | -6.84193 | -56.41145 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a6d51c8-0f75-3bfb-8496-09014b6e46f6 | -6.84609 | -56.40799 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b726ba7-23b6-33be-b032-e56d3d22a373 | -6.84131 | -56.41551 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3313565c-0bf7-3586-8658-d4e52f3b7457 | -6.81397 | -56.4278 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cd1e88f-07fa-3d75-93c6-886b2e6b0725 | -8.89507 | -60.56746 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 66088520-fde0-3b34-bd0a-7bf4524634d7 | -10.48172 | -46.62533 | 2026-08-10 05:27:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f21233bb-b884-34a6-8ef8-d9ab691fe3b2 | -8.96162 | -60.54892 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 625282f6-84b8-3a15-b655-f1bca9be0dc8 | -6.83775 | -56.41496 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 171c5dfe-4aac-33b0-a74a-0b41a5e822fe | -6.1451 | -57.71796 | 2026-08-10 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a70607e7-410b-3410-8705-61cb60b3fcfd | -7.54848 | -55.56209 | 2026-08-10 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 566f3a05-1622-3a44-aee9-217b66e8de71 | -7.5546 | -55.5723 | 2026-08-10 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 066c2ee4-cee7-3299-a656-fc1edd71d986 | -8.17034 | -61.51674 | 2026-08-10 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 787a673a-5b7c-3e76-b753-d00b5cb12613 | -4.3001 | -59.47176 | 2026-08-10 05:27:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b2b7458-1a61-3dc1-9aae-62ad1f8f1ddb | -2.74548 | -54.59514 | 2026-08-10 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb8de843-5d09-3a12-85b7-4cac798240df | -2.61612 | -59.90345 | 2026-08-10 05:27:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd095158-a8c7-3d29-81e1-7a1a80273f5e | -6.84425 | -56.42011 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b88c4b35-2341-3ae4-ad1c-c70a96a6411d | -8.89621 | -60.56039 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 068917eb-3efa-3420-9175-17cbe140a4e7 | -10.47712 | -46.62125 | 2026-08-10 05:27:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b223aa59-4a52-3edf-9a1f-36cd98d31fd7 | -8.89222 | -60.58516 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a215b1e7-9923-3e3f-9dbf-a5e603b1ac6b | -6.13611 | -57.70922 | 2026-08-10 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3865b0f0-dfec-33a9-b03b-cf0c64ec780d | -6.16712 | -57.91488 | 2026-08-10 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b130622-3f97-3eb8-800d-bbd3931fe831 | -6.8092 | -56.4353 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3b4e6bd-cac7-3717-910a-08df60fedf99 | -8.98003 | -60.54102 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c348c0ef-306b-3199-ba23-66d1624b2b6a | -8.89393 | -60.57454 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ff450e36-daad-3185-9f62-3afa7f7593d9 | -8.02342 | -55.11605 | 2026-08-10 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4e5660e3-6eae-3f7a-89dd-eca595096a08 | -8.89556 | -60.5857 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6e1e3566-1967-3387-96e9-63f4c2bb4125 | -6.84732 | -56.39994 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a720b6e-7ad0-3db8-93b6-3a211d1fa133 | -7.6997 | -55.1691 | 2026-08-10 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 013b87e8-29fb-364b-8569-28380b5b7093 | -8.95143 | -60.53668 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea0c8fbe-8794-3304-bcdf-69399caaa459 | -8.1669 | -61.51617 | 2026-08-10 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cda06d17-a2cb-36c5-85a6-71ceb43d872b | -8.94532 | -60.53205 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4ce049da-e42f-3a0a-86c8-a4396b27f0b2 | -5.72863 | -49.13559 | 2026-08-10 05:27:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0247cbdb-fd6f-3d9c-b2f8-540bba57dd43 | -6.84548 | -56.412 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72ddd408-d5b8-35f8-b065-088ffebd2d1b | -2.36054 | -67.21508 | 2026-08-10 05:27:00 | NPP-375D | TONANTINS | AMAZONAS | Brasil | 1304237 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d5ac3b6-2341-3b46-beca-fb6ae077fc58 | -6.83114 | -56.43452 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1117d8f3-a6a6-3c74-8047-e89ee0960b33 | -8.89499 | -60.58924 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4001efae-6e7a-3fce-b806-fc19843ac165 | -7.38936 | -59.97059 | 2026-08-10 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec94d946-1415-3dca-b93d-29571b39938d | -4.45516 | -47.9137 | 2026-08-10 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e386d63f-b7a5-3299-9a9e-abd0ae5c1a57 | -7.69657 | -55.16376 | 2026-08-10 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ed0f8c5-0d54-32ac-ae55-d255716a4145 | -6.85321 | -56.40908 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 379567b4-a28b-38e4-b96a-ce1ff3245c8e | -6.8526 | -56.4131 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f85f677-1e1c-392e-8a1a-81accdf32cda | -6.72088 | -58.9377 | 2026-08-10 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92d26988-1555-389e-b623-974fe85d59c9 | -7.5703 | -55.56994 | 2026-08-10 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38d479a5-8d01-34ec-b9e3-241131ee7a5d | -4.44919 | -47.91283 | 2026-08-10 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a571b8f9-8197-3203-af71-e32d3581400e | -6.46048 | -47.85031 | 2026-08-10 05:27:00 | NPP-375D | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 734ebc8a-9ec3-3c70-8bc5-bbcff756fcb0 | -5.02674 | -56.12698 | 2026-08-10 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cae0436b-e7e3-300d-ae81-4578004c0883 | -6.70817 | -58.95347 | 2026-08-10 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1064634c-64d1-3eb9-b84d-340e2cf1ca00 | -7.65923 | -62.54702 | 2026-08-10 05:27:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c00c962e-d7ee-31a2-94c7-7c19ece65ce3 | -6.72474 | -58.93476 | 2026-08-10 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 667b823e-1c9f-3add-8b70-b0a8f36d12f1 | -8.95752 | -60.59547 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc1c5db0-00f5-3724-8fad-9599174db1d6 | -8.89165 | -60.58869 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6bfb9b00-ce81-314e-a99d-620e032ac3a5 | -6.83713 | -56.41902 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fbeffa9c-b7a1-325e-918b-e629ef2197f0 | -8.9767 | -60.54047 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a337985-61a8-326a-988b-627d44d0f68e | -5.03089 | -56.12352 | 2026-08-10 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9204f4ab-5bc4-3678-ba08-5a73aac558dc | -4.45454 | -47.91804 | 2026-08-10 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b4b13be0-31b4-3bd4-9eff-48c686c30b61 | -6.14229 | -57.71386 | 2026-08-10 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| aa40081f-90b9-3ac5-980e-26484ac87ee5 | -6.84376 | -56.39938 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e018735-7643-39d5-b47c-30b77139dd47 | -6.14116 | -57.72104 | 2026-08-10 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b87d0c18-f755-327a-95f3-def25f8a3290 | -6.70872 | -58.95 | 2026-08-10 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e839127-dc0d-3362-8291-23835da1e934 | -8.95636 | -60.57015 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ad9070e2-29d9-3790-9ba5-40edab38cb2a | -10.47644 | -46.62687 | 2026-08-10 05:27:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5ce3f073-61c3-3eaa-8dc3-db911c25dc13 | -8.95182 | -60.59849 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4340772-ebbe-3954-b854-4a7c6e90bbdf | -6.83003 | -56.41787 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01b1cd21-8dfc-349d-9563-b19dfc3033ff | -3.02974 | -54.52458 | 2026-08-10 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 582dd609-b650-303d-9d72-1f44e6457ce5 | -7.69515 | -55.17329 | 2026-08-10 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6304159c-656f-3af9-93c5-5498eee473aa | -5.03505 | -56.12001 | 2026-08-10 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 090fcb56-7e11-3c05-a555-4581787820ac | -5.79576 | -51.88488 | 2026-08-10 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d427b38d-0a25-3b01-9f63-8c944c2368fd | -2.65612 | -54.62449 | 2026-08-10 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1baf3ed-82b4-33e1-9340-dfede65d23c7 | -6.89001 | -58.93651 | 2026-08-10 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e04f8255-faa0-39d4-be5d-6817cc08ec5f | -6.88724 | -58.93251 | 2026-08-10 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96c1f86c-2f0e-374d-84e4-177790b51daf | -4.44857 | -47.91718 | 2026-08-10 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fd97af12-193e-39c0-b15b-988373a9683c | -2.90645 | -54.15316 | 2026-08-10 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44d6b867-7b32-336a-b074-bbd40af22ee9 | -8.94254 | -60.52798 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e47b6cc0-2867-363f-8470-6bc4c015a2a7 | -7.39046 | -59.98513 | 2026-08-10 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 211ec3f2-2bc4-3d6a-8000-da98398038ce | -6.43342 | -60.06642 | 2026-08-10 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 210bfd08-2788-3d42-be05-a0d05b4f0c27 | -6.8358 | -58.93502 | 2026-08-10 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e3ffa7b3-9c99-35e6-830b-33ce15180d11 | -6.15704 | -57.91331 | 2026-08-10 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6c23ae6-46e8-3ffa-bc88-f1628f788c4a | -7.6582 | -62.54822 | 2026-08-10 05:27:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 355d8d43-6a01-33f9-b085-0e0cdc2991ec | -8.90118 | -60.57209 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| b73ba308-80a8-3b72-a144-725717da88de | -6.82343 | -56.43743 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d138118b-dc22-302c-be1e-e7f164f994ae | -7.48371 | -61.38102 | 2026-08-10 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3698b3bd-85d6-3b91-8c57-376f6b75e91f | -6.46603 | -47.85561 | 2026-08-10 05:27:00 | NPP-375D | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49dc1193-2687-3d16-b5c8-0f6c208eaa70 | -8.94418 | -60.53913 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 5cf45cf8-43ad-31ff-a852-6595aa52ca67 | -8.8967 | -60.57861 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c7dfa536-06d0-34b7-a3a5-df127b34b4a0 | -7.38713 | -59.98458 | 2026-08-10 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14aff064-5467-3047-9fd1-03448bbd547b | -10.4753 | -46.61956 | 2026-08-10 05:27:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 49548f7f-dcb9-36cc-8d46-127223ebd7a6 | -6.81042 | -56.42726 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b88fa221-cde3-36e9-b733-f4afafaaa6ed | -3.93071 | -59.13449 | 2026-08-10 05:27:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d50c6a3c-11dc-3189-a956-f79928f586b8 | -6.85383 | -56.40506 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78cc3b62-7428-32f6-81da-66e26fe73264 | -8.95584 | -60.55192 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 4d2773cd-41df-3cb0-9c73-906cf8c56cf1 | -2.36109 | -67.2118 | 2026-08-10 05:27:00 | NPP-375D | TONANTINS | AMAZONAS | Brasil | 1304237 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa960105-8391-3dd1-be62-c749ae25f878 | -6.84487 | -56.41605 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README16.md)
