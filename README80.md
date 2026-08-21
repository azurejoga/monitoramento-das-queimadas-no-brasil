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
| bc75694e-fa49-3d45-ac06-c5202d8aa64e | -6.22949 | -55.61707 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 7c4be0b9-7989-38f6-8fdc-1c6745b264db | -6.8591 | -59.43636 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 902169d1-0cac-3618-a486-913aac3bdc3c | -8.26327 | -63.99406 | 2026-08-21 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bed5c07-5687-3d98-a5a2-3285b0ea31e0 | -6.87388 | -59.44609 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 888b14ec-70e8-3476-999f-0658e9a36b6d | -6.88464 | -59.42728 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f7929961-00cc-38b6-a85f-2b78d709e563 | -8.89999 | -60.54274 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| af3d27cf-5b98-3f1c-a8c1-932b59cf0435 | -9.24643 | -59.81291 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 503b979a-2d64-3172-8f60-349673d1e6f1 | -6.4295 | -52.74867 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 341570b7-ca59-342a-a9c6-7a7b7ff7dfac | -11.18191 | -54.00908 | 2026-08-21 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20bbecd5-f7d5-3f9b-9376-be7a252ccc20 | -9.24718 | -59.80779 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b52f6f8-0c14-3c29-8d38-48dac6fe4788 | -9.53903 | -63.56531 | 2026-08-21 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c3145a7b-8a09-3716-9f5c-2949935da579 | -7.61071 | -60.94974 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f83fa938-dec7-38b4-aeca-39a7b8f03464 | -10.38726 | -61.2118 | 2026-08-21 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 407e574a-0a49-3996-893d-96611eb895a9 | -7.06835 | -59.96657 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72a1cab3-00b5-3eac-aed6-909362c596ac | -6.6936 | -59.10115 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ea65d2f-d8a5-31ba-acd0-067a05f272fe | -8.58528 | -54.78892 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 573a1347-c9cb-3fa6-b76d-12f0dcd7f1f8 | -9.15606 | -59.66239 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c7d300f-48c1-30f2-957d-bd3fc08cb647 | -11.20772 | -55.06472 | 2026-08-21 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c7c75bc5-5d96-38cb-ac25-1e630a7e33f2 | -7.33799 | -55.68324 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12335b12-7f3e-3044-9962-58051526bf62 | -9.16005 | -59.66298 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b5901ab5-e8e4-3b01-91ae-c9fbaebf3f2e | -6.75154 | -59.46076 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 40008016-5bb2-316a-9863-70f72776e28e | -6.36401 | -58.33739 | 2026-08-21 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58857d63-14da-306a-8a4f-ca1078d7de92 | -6.37966 | -54.953 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70ee5b0a-a230-33d3-a4ec-8af09f058d70 | -6.20175 | -55.48843 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 033b23ae-37a7-39bb-a591-05ec3d2ec070 | -6.8736 | -59.42055 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fc70d8f3-eb54-3520-9dd5-534920770088 | -6.24846 | -55.41646 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d20cf2b5-3346-3ebe-a6c5-430a6f6c44ee | -6.17208 | -55.44185 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0302617b-c255-3533-bad6-d34ba49902fb | -6.22931 | -55.40495 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5ef4de6-2796-3f92-8c52-71d1b9aa51cb | -8.40119 | -62.69889 | 2026-08-21 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61889206-ec5d-32f2-90ef-6013d56966df | -9.41385 | -60.41404 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| c8ad098e-fb11-37ca-ad4b-893cd40c3192 | -6.3604 | -58.33297 | 2026-08-21 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3615f30f-21ac-3dea-856b-c276638e5104 | -11.17972 | -54.02706 | 2026-08-21 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1b1bbf28-3021-3353-8d4c-19eff8236fa2 | -9.42078 | -60.41995 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f8d9481d-0bee-3f49-bf1a-e279966c687b | -6.70075 | -58.94534 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91054de3-c832-3b96-9071-3556e869a7cc | -6.57904 | -55.44821 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 85827ad1-766d-3c81-b346-3f3a4331ede4 | -6.42604 | -52.73147 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3522e3a-4979-30c7-b536-c67138cb649e | -6.68918 | -58.94003 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 17051901-6e2d-358e-8dfb-0689773443fa | -6.87074 | -59.41259 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5fb5e738-80c6-3ed8-8901-140d04dad682 | -6.83226 | -59.40181 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.9 |
| d2d42b39-5217-3cdd-adb4-a16724fc2b35 | -9.40491 | -60.5517 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb88a53b-9fd6-31f1-802b-a40d29829fb8 | -6.22411 | -55.61438 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ce13a5cf-69db-3ac9-a195-e77944a906c3 | -6.88783 | -59.43287 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fa3c8501-0fdb-3077-93e7-a332e96a25b9 | -6.39206 | -54.94143 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d4ade72-bf3c-3d1d-ae05-36229936b31a | -6.8906 | -56.4386 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 623fe6c5-9c3f-3de3-ab8d-6e43c413e5ca | -6.93797 | -52.78204 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e9262e4-d4c3-3dc5-9527-79cd86baab3e | -10.2402 | -54.37253 | 2026-08-21 05:42:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0da4cf42-3384-3127-8fe0-5ddb51e3f97f | -9.40964 | -60.43493 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8589de91-773f-39c0-b2a9-07dcc6369647 | -7.76929 | -61.13759 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 44510c53-8a68-3097-9136-d96a99e985ee | -6.75473 | -59.46628 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f1d9ebf-3abf-34b5-9f0d-abfc9c5f2328 | -6.01569 | -57.82683 | 2026-08-21 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 36b5f96e-8844-375c-82f2-98b713fdf0c9 | -8.17031 | -54.99613 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1d344ea-fb3e-3df4-aaff-da1122588d5d | -9.42148 | -60.4152 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 60b5a4d5-fcd5-3e4f-89f7-886d4b7149a5 | -7.60619 | -60.96046 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa6f9231-cc2d-3caa-a515-8021cb19c7b1 | -6.86328 | -59.0294 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0be9d46d-0ff8-3e3b-9ae8-10db350fbebe | -5.80622 | -55.71693 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ccf697b7-64e8-37fc-ba27-93f58367c9cc | -7.05673 | -59.8352 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e2f7733e-fb42-3113-87f4-631143cd2c2a | -6.87853 | -59.44165 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54a33e05-e7bd-390a-ab59-833ed3d091ec | -7.3541 | -55.67939 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1d45326-0e28-3f98-9db0-4ad3c83198e3 | -6.11753 | -59.91006 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa6e35ab-ec8d-352a-b621-522e77b949d4 | -8.15689 | -55.37435 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ade773c-17ab-3d57-8fa8-92a2034cd21e | -8.58057 | -54.78504 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9fbdfccc-50cf-3568-a499-360e33afb398 | -6.70427 | -59.09865 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5781b85a-65a1-3c61-862b-3a008dbdd08d | -6.87729 | -56.63626 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 43b49ff6-20b8-30b6-9600-7d1a90350241 | -11.20582 | -55.05001 | 2026-08-21 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 17e7c611-566b-3967-9c50-8a09ddafa32f | -7.60218 | -60.95702 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0246aaff-db22-3261-bf6e-f747f83ef228 | -8.58626 | -54.78174 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c59555de-b5f6-378c-b7c7-fe2890519d7b | -6.72578 | -59.0911 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 294880e4-31cb-3b63-b928-cff474435114 | -9.4094 | -60.54518 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a99e39d-00ce-36b9-bf05-d5c2ac803dc6 | -6.97686 | -59.58931 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79ccf775-3778-3bbb-9748-fa4d75c73254 | -6.69578 | -59.10096 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d99c24a0-b374-389f-b582-706366e2539f | -7.44574 | -59.99939 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a15e18d-6ed8-3ed4-a0ea-863e145645bd | -9.41185 | -60.55508 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfcc8039-f602-37fb-a311-3c0572b6b1e2 | -7.87093 | -63.76781 | 2026-08-21 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 047b0bdb-1370-3cde-bdb7-2877dbb02179 | -6.43404 | -52.71825 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06f9931f-6afe-3cd7-b93c-98ffa7a56dab | -7.44125 | -60.00342 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f29172e-39f2-38fd-affd-6e9c3c72f727 | -9.21127 | -59.77639 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e19a3a1-e308-3be0-b4cb-9446e4fe91f5 | -6.87534 | -59.4361 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5a786a68-65b6-39c6-a883-81ec293ae4f2 | -6.66383 | -56.34899 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ebb3bf46-9d03-3de1-ab0b-67d8cb1f97f4 | -8.52085 | -55.3352 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7c9f05c1-d34f-3f49-b894-87df508548d5 | -6.80635 | -59.01756 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f83d80ff-621c-3c34-bda6-48d669dfa2ef | -6.79889 | -59.43758 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ee5cc20-427a-3b9a-957f-055450a707c5 | -6.81583 | -59.40438 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68f2f10a-fb02-3ef0-bb5e-9dca7b438ca9 | -6.08597 | -57.91584 | 2026-08-21 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d46b3d7-aa5b-38bc-ab5a-699c6ee7ea0f | -6.69928 | -59.10496 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b91765b-5ef0-3505-8f43-c2e4484d32ba | -6.89959 | -59.43456 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0963eb43-a6f8-3b59-8868-74c6a3bf795b | -8.08739 | -51.66735 | 2026-08-21 05:42:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 40479ca7-1028-3f51-8de8-c1aeab84ad07 | -6.70877 | -59.09575 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe22742b-4b0b-3133-857b-0567ae6cb771 | -6.69776 | -58.93776 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1335b6f-0ad0-32c0-91b9-2c27647ba365 | -6.43637 | -52.74715 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b52ca5dc-d5aa-3d63-9c82-c0223afd3947 | -8.40574 | -62.6695 | 2026-08-21 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33529159-6936-3bb4-adc6-f88912a55f94 | -11.16121 | -54.0293 | 2026-08-21 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8e9bd695-4a7a-3fe4-9799-265b795c9c45 | -6.71728 | -59.09336 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77fd3b1b-5342-3d74-ae88-928744884210 | -8.37291 | -62.70198 | 2026-08-21 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7eeeda5e-85da-37c9-871b-6268d43e0992 | -7.34777 | -55.68752 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c2e41ed3-6111-3d1c-bbf8-d30a310ba4d2 | -6.22461 | -55.40142 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3756ee36-03b9-3e06-9bb1-68990e624ee1 | -9.11954 | -61.59867 | 2026-08-21 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24c66cf5-021a-3b71-9c49-774ccd141d1f | -9.41937 | -60.42937 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3b67712-d880-3878-9b49-afa6d5cd5fb9 | -7.3384 | -55.68032 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01ef016b-e69a-3516-a867-ec7da2614706 | -6.22333 | -55.62004 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| befc2604-17ff-3d61-a6d0-1264dd851cab | -10.81293 | -50.99914 | 2026-08-21 05:42:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |


[Clique aqui para ver as próximas entradas](README81.md)
