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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6add3e4d-62c4-38fa-8a68-d0ee2a097a10 | -2.90063 | -50.41609 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 46af20c0-a6c4-3166-a827-2227b378a086 | -7.16616 | -43.52091 | 2026-09-15 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 97f0e528-d6c4-3793-b1ae-df5432215fe8 | -7.24185 | -46.15898 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| afb523db-db9a-3f0c-aab4-07f66cc7d610 | -4.57016 | -54.9101 | 2026-09-15 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 112d34f1-30e0-3701-8502-7cadbd8ef27f | -6.15477 | -55.71713 | 2026-09-15 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0a097347-3b64-34f1-8b45-c478b5bbb3be | -3.3591 | -50.7422 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abc18943-250b-3457-8ea3-e5c7aed157a0 | -6.16523 | -52.7415 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74c59484-4bfd-34cc-bee8-35bb064d9c37 | -6.43043 | -43.07096 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24e6bef3-6af5-31b3-b352-873a0059e909 | -4.13475 | -54.02182 | 2026-09-15 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5326466-efbd-37be-8d09-948efabe61f0 | -2.91582 | -50.39775 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0cd11773-ea5b-3e89-a568-83923d22071e | -3.07148 | -51.0797 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acc68767-1c12-350f-ac4c-5dd8a082d463 | -7.25015 | -46.17098 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f77406e-3b45-3670-a1ad-3f60b6f8e6ca | -6.15669 | -52.7925 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91b37e3c-53a8-35c3-a9ac-26f51481e7ee | -7.01929 | -44.62478 | 2026-09-15 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36ced7dd-f0f3-31e6-9166-1f5e0a19ad92 | -7.96795 | -43.97808 | 2026-09-15 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa58de29-3c3f-3fe2-b2a4-020d7444c72a | -7.23467 | -46.16142 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| efc1eea2-51eb-3326-ad18-28bd9d604e0c | -7.23025 | -46.16787 | 2026-09-15 04:32:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a550481-e31e-371e-a9c0-933252bfc722 | -4.51735 | -54.96636 | 2026-09-15 04:32:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b1822eec-5831-3790-86e3-a5c4bd33bcbb | -2.90542 | -50.41167 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 053ce700-ae9f-326d-9b5a-d215a2a322b9 | -4.18316 | -49.40397 | 2026-09-15 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4714b8f6-6487-3bf7-9d5c-df626d371293 | -5.60943 | -43.56258 | 2026-09-15 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1660d955-940b-307b-b1c1-ffb68654923c | -5.13494 | -55.94069 | 2026-09-15 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c3f23c9f-52ad-37af-90bf-f7a723ff410c | -7.08836 | -42.10434 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9d1a191b-2a6a-3b15-a925-5e24b935ca9d | -2.89188 | -50.41988 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 862c27f6-3af2-3f4c-92a2-408ee7817ad7 | -4.66994 | -42.08985 | 2026-09-15 04:32:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 7e99a576-07ce-3b53-9201-91716389da9f | -2.89501 | -50.42559 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ad95a50b-3f67-378d-a1db-adaa2e8873d8 | -7.22584 | -46.1743 | 2026-09-15 04:32:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 170f1203-6fda-349b-b4be-a2798a098510 | -2.95614 | -50.39912 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77d5c395-6ac8-3f5e-9041-d821ee528a5a | -5.35491 | -47.70731 | 2026-09-15 04:32:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9e257fa4-d9cd-3a02-a528-6225cdb9cb5f | -2.77824 | -49.45758 | 2026-09-15 04:32:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac0692bd-6d4d-3fa8-b568-2a2fe8bce10f | -5.35433 | -47.71092 | 2026-09-15 04:32:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a0ff99d-7715-3840-acbc-4f18cb61d869 | -7.22916 | -46.17482 | 2026-09-15 04:32:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4374fe65-596c-31b4-a7ca-c861676ce505 | -2.88793 | -50.41924 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f34890ad-f56c-3302-9a41-7d15dd205a60 | -5.12874 | -55.9435 | 2026-09-15 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3f286fb1-ef54-32e2-85d3-ff8931f08147 | -5.12934 | -55.94008 | 2026-09-15 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1db8202f-5f68-3340-83c6-2b335c86e6ec | -3.92888 | -42.99504 | 2026-09-15 04:32:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6d598dd-fca3-3abf-bbdc-f598c4171fe8 | -7.08999 | -41.82164 | 2026-09-15 04:32:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b6632900-41d6-308b-a14f-b3a38258c243 | -7.16423 | -45.04656 | 2026-09-15 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3117d5cb-b1d0-33ab-b1e2-1958d17c5a97 | -3.58166 | -58.55335 | 2026-09-15 04:32:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 436c33cb-bf60-38ce-9da5-ac72ac666897 | -6.05363 | -52.18981 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 23c8cb45-1dbd-3785-a86a-74b17627a5b3 | -2.66274 | -57.57004 | 2026-09-15 04:32:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 185a4a93-78f0-36a2-8d07-ae178fb399bc | -6.5544 | -51.19462 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 570e8fdd-899d-3a19-b071-1e152b2626b9 | -2.92455 | -50.39398 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a3e9c89e-276c-3360-ac59-94ac69137dfa | -2.90521 | -50.43773 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6571d890-dd8e-3e11-835c-dacebdbdb4c8 | -6.95286 | -42.56754 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| becd09d4-1b62-3da4-bd9a-290689ccd9c2 | -5.92519 | -53.5442 | 2026-09-15 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a1bae5bb-5073-3c65-9511-e3fe4822fc91 | -2.88625 | -50.42938 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 47762ee3-3ba3-3cb5-8c16-5251d471a14a | -4.66376 | -42.0795 | 2026-09-15 04:32:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 67b52512-3dc5-323d-be46-37bd64415f45 | -4.53319 | -55.62282 | 2026-09-15 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45cffce9-24c5-3807-96c6-a57d6863f495 | -2.90396 | -50.39586 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| da3307ff-4fc2-3c08-aa11-8514403a2801 | -2.91167 | -50.42309 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| afce2c52-140b-3408-b53c-892d6a83f971 | -4.9525 | -45.14531 | 2026-09-15 04:32:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a10dbab3-1a3a-3291-89d9-660cc3a631ce | -2.48004 | -49.40591 | 2026-09-15 04:32:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 713bfc03-720b-365e-b708-9ec06c73f338 | -4.80396 | -42.87801 | 2026-09-15 04:32:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae281ea2-5696-3ff0-9f31-da0d27fedaa6 | -7.40466 | -47.78577 | 2026-09-15 04:32:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf24ba2f-c6c4-31a5-bdd7-23f658d8d54c | -2.93162 | -50.40033 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8721154f-0860-332d-aae8-fcb40d57c294 | -6.95855 | -44.54255 | 2026-09-15 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0566c600-a95b-3b01-b886-31a246c60cba | -4.1795 | -49.40338 | 2026-09-15 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ee2893a-b585-3710-9e37-f2762b2a4f44 | -2.90209 | -50.43196 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8141f898-f322-3d5c-8b00-0f87b5fca468 | -3.96078 | -43.11388 | 2026-09-15 04:32:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1c47630-fc06-3a1a-889b-eae8377b5022 | -6.82095 | -50.99979 | 2026-09-15 04:32:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5f91491-9b40-3ae4-ab02-2a1bf94b7aa4 | -4.67133 | -42.08067 | 2026-09-15 04:32:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 078a04f9-5e4d-35b4-b740-ada54f989003 | -2.9127 | -50.39207 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 601dd16f-2906-3ed3-89cb-aba6b0b406fc | -6.94839 | -42.57162 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 848f1686-8bf7-39e8-a373-7124e3de1148 | -5.4114 | -48.53283 | 2026-09-15 04:32:00 | NOAA-20 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3a1e6068-eb50-3a1e-a8fc-6cd8d362972e | -2.89033 | -50.4126 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 80277eec-f06e-3f50-93c8-cbbb5422f954 | -6.72327 | -48.11803 | 2026-09-15 04:32:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c49e755c-a47f-37f3-8e7f-e1cbab1edfbb | -2.90792 | -50.39649 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 04e1fd88-b5e3-37eb-988b-b3e9b2e45c96 | -7.56441 | -46.3103 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a1998ab-e1b2-3ae4-ae6c-616742fb8f9e | -5.93102 | -53.54864 | 2026-09-15 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b61afbaf-a816-33a2-91d2-60ac2761af96 | -3.53958 | -48.18475 | 2026-09-15 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e405c273-fc44-32a2-a86f-7971d13854b9 | -7.24355 | -39.28198 | 2026-09-15 04:32:00 | NOAA-20 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| ba306b24-3ad3-3607-bd30-b02a0a6fca02 | -3.4034 | -50.757 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cca093a9-dc54-393d-947a-991cda419af1 | -7.13042 | -42.09288 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9ed03cc9-eb51-3af9-8d4a-3a388f3261c9 | -5.73718 | -43.27596 | 2026-09-15 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 88b2fb1c-83e8-305b-add9-50feb5a9be21 | -1.22821 | -54.12454 | 2026-09-15 04:32:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 134d49af-ff2e-3b0f-898c-6d0c93dd137c | -2.92767 | -50.39969 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6adec0ca-4c5b-30de-93e8-97f2d539534f | -4.30251 | -49.11127 | 2026-09-15 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46a470cd-dd40-3a1c-9c47-3c18d7543074 | -4.37142 | -55.0347 | 2026-09-15 04:32:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebb57326-e95a-3c90-a30a-15d472a024ea | -4.51569 | -54.97592 | 2026-09-15 04:32:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 949a2263-444c-302e-b17d-e0140eddf45a | -5.91993 | -47.38074 | 2026-09-15 04:32:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6367e517-edfa-34ca-bddd-ae071d9bf8dc | -5.80985 | -53.80535 | 2026-09-15 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f676569f-ac44-3322-a4ea-1ac46d319a8d | -6.05071 | -46.34659 | 2026-09-15 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f117ad8-884a-3e81-b58b-82e008a04c81 | -2.90605 | -50.43261 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 990e5577-7c32-38e9-bfca-055aadbbbffe | -7.21365 | -46.14384 | 2026-09-15 04:32:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f31e0855-f4d4-3988-a0a0-bf2357783a73 | -7.29659 | -42.35566 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ef241e61-ca76-3c6e-8b74-4b119e9c999a | -7.10546 | -42.09681 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 16d170ce-c443-33f0-8c9c-c28b5e8d8f81 | -5.92326 | -47.38128 | 2026-09-15 04:32:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1aaaf47a-a8b8-35aa-aac4-27b03d5261ae | -6.79114 | -47.87699 | 2026-09-15 04:32:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9fabe78c-2810-3ec2-addd-ef7046006676 | -2.98184 | -50.51844 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d6fca79-9286-3372-8e0d-22b746b31cf9 | -6.78733 | -46.45664 | 2026-09-15 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 890bf6aa-7360-398c-93ac-bdb1eb95b153 | -6.7221 | -48.12531 | 2026-09-15 04:32:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9ab7dd5b-8b87-33f3-a01c-d7116ccd4ad7 | -7.48261 | -42.12011 | 2026-09-15 04:32:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dacde5e3-8e66-316a-9a6c-b1480f2b151a | -2.90688 | -50.42752 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7c3bb8e7-df09-38cb-9bf3-22134b0015b4 | -6.83059 | -43.51622 | 2026-09-15 04:32:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86529fee-41f8-37fb-8a9f-74b61ca34f83 | -3.41806 | -58.2212 | 2026-09-15 04:32:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e028b23-5b1d-39f0-8680-ce22e574d6d7 | -3.64589 | -58.61671 | 2026-09-15 04:32:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 059c66e7-0d0e-3d14-a1b6-c35d30c79292 | -5.93019 | -53.55363 | 2026-09-15 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c747cea-0388-3da9-9ebd-5c92ac70b5da | -8.39331 | -42.21865 | 2026-09-15 04:32:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7628dec9-421d-3c3a-b198-80eace4d311d | -3.78205 | -51.34918 | 2026-09-15 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README39.md)
