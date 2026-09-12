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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 054b7936-a450-3cf2-9cc1-a6071fa1d397 | -8.94752 | -68.68991 | 2026-09-12 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7ff5f19-cf68-3646-b630-5c4095c4d549 | -6.16753 | -57.71281 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ef4b641-a5a8-3a34-a8ea-44a513ae5e98 | -11.23812 | -54.14075 | 2026-09-12 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 107af6bc-c9e3-3448-8355-c944f00ae443 | -9.14763 | -68.20454 | 2026-09-12 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18b6fb30-0e44-36b7-8e07-b02d964d8ca1 | -6.3679 | -57.86996 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72f3d8d9-07d7-3189-a112-54926384910a | -9.18755 | -68.21616 | 2026-09-12 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 325ea786-5d26-3e44-ab56-af43957f49a6 | -6.84477 | -55.80359 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3c33d99-b525-3195-9ea3-edcb76c4cdaa | -6.24244 | -51.69434 | 2026-09-12 05:29:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45b59bfa-d335-3ba8-9c0e-9a1f1f3c4436 | -6.34004 | -55.31039 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24cf6060-9d68-35fa-bbfa-672f777902af | -6.09258 | -57.68608 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 53179053-18f0-30ec-bf3a-f02d670d1db9 | -8.11836 | -54.79044 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f79ac2b-ce20-389f-b9f5-d01c409a4a5d | -9.15899 | -49.98664 | 2026-09-12 05:29:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f8f84b3-badd-3b6d-b78d-ace6322ad10c | -12.205 | -49.3977 | 2026-09-12 05:29:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6c8641ca-6838-3c0c-80db-f4dc23f8107b | -10.54884 | -51.37777 | 2026-09-12 05:29:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 384a8118-83ce-3722-b79f-db5fb54902dc | -6.13242 | -57.71292 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23ba9140-8f35-31c3-8ddf-9e04f1111044 | -5.97558 | -57.76547 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c16808ff-4d0a-3065-85cc-36e682ab176f | -9.15674 | -71.84819 | 2026-09-12 05:29:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7c11f48-ef38-3d2e-9445-e8066361ff0a | -8.11335 | -54.79414 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28ccbe5e-01d5-3dcb-bf5e-a51b2171cd7d | -11.24363 | -54.13617 | 2026-09-12 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4ed01eb-75e4-3f73-a779-ec87e930fed2 | -6.08822 | -57.90477 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3dba2eca-5c30-38b3-af4e-bd9ce9cbd7d8 | -8.53533 | -54.70339 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 518fe59d-32ef-3f52-a996-3942d16abe8e | -6.11107 | -55.64875 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81d0108a-9d08-3bd8-95e3-e0c34130ebdc | -6.11004 | -55.65559 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb28939f-50a4-3399-ac4c-1353910f0abf | -6.40601 | -54.97895 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b67e86b-c4e8-3ea0-a476-4365d42d7d8e | -9.18597 | -59.45053 | 2026-09-12 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53be6ed9-434b-3bb9-9e3d-cf026793a528 | -8.07178 | -54.86486 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 405609af-f28c-3975-9cf3-fd68d22deab9 | -12.2024 | -49.39828 | 2026-09-12 05:29:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f9a87598-3d06-3cb3-ac98-5a409e7e0944 | -6.11158 | -55.64535 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8379976-6d59-3bc0-a10a-8575a0608783 | -6.84423 | -55.80714 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1eb9d96b-54e6-3782-9f1f-0111ff493219 | -7.84627 | -56.58162 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a3697df-5f69-38ed-b8f7-b10ae1364dd8 | -8.53275 | -54.72114 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9816de56-5031-3038-ba7e-47b6f749d09e | -6.11056 | -55.65215 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16091bd6-279c-3f71-a04d-f23c24c30b8c | -9.18303 | -68.21537 | 2026-09-12 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f6f8a6f6-4acd-3206-bdc2-fce8f8d09172 | -9.44157 | -67.03245 | 2026-09-12 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cdf3c96-e5d7-3328-93dd-7f3d6eaef45f | -6.81974 | -58.99274 | 2026-09-12 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed6cf464-e945-3110-8729-4ed48a46ea6f | -6.20338 | -55.27608 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa1410a2-7954-3ec8-8e58-d854faa303d9 | -6.28474 | -56.03394 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dca94f39-9511-3db2-90c5-02dd0f304239 | -9.16453 | -68.2409 | 2026-09-12 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 005d6065-4537-3504-84f6-b76bdb5b6b44 | -9.70383 | -54.34549 | 2026-09-12 05:29:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97c3beda-8553-38fd-a726-ea0742dabc92 | -6.77286 | -59.43375 | 2026-09-12 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 451deed1-e3ac-32e0-af4d-39e9eee820f7 | -9.44505 | -67.03703 | 2026-09-12 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb9864c9-2d95-3462-8abf-78da7fadf77d | -9.90596 | -67.82946 | 2026-09-12 05:29:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d4d634d-6de1-397e-bbe4-9d112eba05d6 | -6.79984 | -58.89515 | 2026-09-12 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f271adb6-a9f1-3985-b7f7-65cfb8052a30 | -8.11274 | -54.79848 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 734e6e40-4ac2-38e7-a204-a505844f1737 | -6.8363 | -55.28817 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a78deac4-5fe2-39e2-9916-f03ce85b66f4 | -6.40659 | -54.975 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0382e04a-0f06-3eb6-a2a7-867ddfcba09d | -6.77005 | -59.42963 | 2026-09-12 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72d0e58c-b196-38d9-9c38-8bb5e613bdfd | -10.55233 | -51.3503 | 2026-09-12 05:29:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0099950b-dc87-3101-afaa-884fc3e0efb6 | -6.88689 | -55.65853 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f181eff7-3271-34f9-b0ad-27a190c29262 | -6.28785 | -56.0176 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 346d31cc-4bbb-325c-803d-87a9c44da7e1 | -8.95309 | -68.68578 | 2026-09-12 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 20469e03-12c3-3e8c-947c-28ad70582f86 | -6.13495 | -57.69651 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a65b220-3153-3cd6-8cd7-165f46edb8d9 | -10.49601 | -51.37139 | 2026-09-12 05:29:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 083a757d-45e4-3920-9460-54e930081746 | -12.44487 | -49.5923 | 2026-09-12 05:29:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 68c4ceea-0c7c-33fe-8cba-055139585cdc | -10.55385 | -51.33837 | 2026-09-12 05:29:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60a1f47d-28ad-347f-b7fd-2a5a0e43dc53 | -9.44225 | -67.02862 | 2026-09-12 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08018309-3316-3791-8273-5014c38e3ff5 | -6.28831 | -59.93146 | 2026-09-12 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44145c92-8e0a-3e4d-99a1-ee3e8286bf4f | -9.49637 | -68.49692 | 2026-09-12 05:29:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c728e9e7-f741-32f1-9aee-aee7f04d89d2 | -9.53148 | -67.16358 | 2026-09-12 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09840148-1ea5-3d64-87ff-f57cfdd4c17b | -10.5557 | -51.36984 | 2026-09-12 05:29:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2e6d9e01-53e3-3db0-af98-ccc816f326af | -6.28546 | -56.02896 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9771b138-0751-33e2-829b-442f32a8cdad | -9.41466 | -68.90935 | 2026-09-12 05:29:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a394fe75-1f08-3613-88b9-df50e77eb58b | -9.47381 | -67.09369 | 2026-09-12 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 794a7025-61ac-3db7-856e-0ccdacfc6913 | -6.61335 | -58.85578 | 2026-09-12 05:29:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9a48fa98-e51e-3df1-8f17-084c0c45abbd | -6.10001 | -59.89876 | 2026-09-12 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9286061a-06f5-3c7d-ad6f-d026aae0573d | -10.54934 | -51.37391 | 2026-09-12 05:29:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1049a968-e020-3b77-a6c9-55c264a1682e | -7.70467 | -55.3691 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 205b3a89-16d7-396c-94b5-72d71c473816 | -10.6892 | -54.16567 | 2026-09-12 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 5c50fed4-d87e-3141-bb11-0ddfce44e5d9 | -9.48192 | -68.84029 | 2026-09-12 05:29:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9cb046aa-11bf-3d0f-828a-af5ad828005a | -9.9067 | -67.82521 | 2026-09-12 05:29:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 079e01a9-1ead-3e8e-94cd-7065887b346a | -10.55184 | -51.35418 | 2026-09-12 05:29:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db35a353-b6b0-3b46-9203-b38f7b960a3b | -9.15836 | -68.24933 | 2026-09-12 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6d3544c5-2666-34d7-96d2-9c8444e7c83f | -6.84428 | -55.58286 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 665747f7-bdc1-3c5c-af05-32f4cc4d13c8 | -9.14276 | -64.38995 | 2026-09-12 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95a2b0c6-d588-3e62-aa08-4fe0481ac57e | -10.50469 | -51.30505 | 2026-09-12 05:29:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb0e37b3-7be8-3561-8391-538a55df6ebd | -6.10805 | -55.64138 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a58c915f-79ab-33a9-9ce0-f530fb85a4bc | -6.88764 | -55.65622 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27690f3d-8899-3c4a-8ddb-7d8e63033a16 | -6.84653 | -55.24644 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4fef1da-28d4-3cc3-a2df-bc152ace92ee | -9.70448 | -54.34075 | 2026-09-12 05:29:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9fee287-6513-3f6c-9102-74ec6e5e783a | -6.34059 | -55.30663 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d82357d0-89ea-36c9-aca4-45d6cfb3028f | -12.1293 | -48.96441 | 2026-09-12 05:29:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 172f9f75-3a73-38c2-864a-7fff61066f2b | -8.49712 | -54.6523 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78309991-e301-3b04-a175-0533e1e03b9a | -10.50547 | -51.30343 | 2026-09-12 05:29:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e4b88031-4b72-398c-86ec-0519afcd357c | -8.25533 | -55.4685 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14d5cbec-0aed-31b0-847a-6b13b24f3c8e | -6.23572 | -51.70354 | 2026-09-12 05:29:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02fb720a-b480-3dd7-9679-71f4bcc5894f | -6.84539 | -55.24663 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 096eb202-de62-3a4d-b36c-cd59a312754c | -10.48502 | -51.36611 | 2026-09-12 05:29:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05192569-e55d-38d8-aac1-45f779c8eccd | -10.23418 | -56.25896 | 2026-09-12 05:29:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c76a7a6-dc03-3bed-b1b1-fd2d23210cf0 | -6.33296 | -55.72071 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 009db9db-4750-3f7e-bb31-282ca016b31e | -6.76668 | -59.42909 | 2026-09-12 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0edde44-ced8-35a4-8f62-39d9f1090843 | -9.3684 | -48.41924 | 2026-09-12 05:29:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7de02839-f71e-3247-8f78-6b1926cdefad | -9.16824 | -68.24636 | 2026-09-12 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a2936af-b078-3192-b0af-7a9a8fc44b2a | -6.10402 | -55.64077 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f37114b-117a-37d4-a6b9-8d084ee99fb5 | -9.73841 | -64.95153 | 2026-09-12 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04581414-da77-3109-8643-59317fcc14e2 | -10.69398 | -54.16627 | 2026-09-12 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 7c5e902c-0877-3706-a504-f0f6ecf9f509 | -12.13164 | -48.9601 | 2026-09-12 05:29:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a243cb6c-dea6-38f0-92d4-4ec356eda904 | -6.88574 | -55.64118 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c030ae7-e571-3ae0-bb0c-7d5950a22e95 | -6.2045 | -55.26838 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91937e79-82e5-3379-9f90-73d857208681 | -11.24432 | -54.13092 | 2026-09-12 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b9888ad-998e-32fd-8a54-d784cb6ef53c | -6.28886 | -59.92795 | 2026-09-12 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README51.md)
