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
| 349f4d1a-46ef-39ea-b428-0c7dc4fe559e | -9.65634 | -48.27625 | 2026-09-01 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3de22c40-cc08-37ca-ab6c-e30ff2805be4 | -6.59048 | -58.5987 | 2026-09-01 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57eff82c-63b1-399c-8101-02b1b4d10c8a | -9.2065 | -59.41452 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b837fbe-783c-38a9-9264-39037b617cae | -9.9417 | -53.99514 | 2026-09-01 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ecd57b54-e032-392c-b681-d04f11bd2ab1 | -6.91864 | -55.70064 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d6d6692-deef-3fb2-89bf-677b45c34413 | -11.35293 | -45.42388 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 79f723c3-2f26-339b-822e-52db30a0138a | -6.88395 | -59.45111 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e752edb-5c79-346b-bf4a-b97767058f3b | -10.53794 | -50.77583 | 2026-09-01 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b1dbf73-7ed2-3efb-ad44-d11c81de2dfc | -11.31696 | -45.20228 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 32b8d914-b8fb-35a2-8d40-cd31949eaeb2 | -10.68874 | -46.25523 | 2026-09-01 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cf5b59b9-3d1a-37c1-a970-0515b24bb8d2 | -10.32613 | -49.10938 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d70e5032-29d8-3090-b40a-0746adeef810 | -9.4043 | -51.6857 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 71551e02-ab25-3d1b-afcb-3b72d8a349b1 | -6.10477 | -57.8646 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23fd11bd-5a30-347b-aad9-9f7e6714737e | -7.56493 | -60.46586 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd2bbce2-90ea-3cbd-94cc-bc7830fab644 | -10.75167 | -47.98265 | 2026-09-01 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 718dd49c-d001-3294-9da4-d0b91612866f | -11.35751 | -45.42082 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f8b19755-738e-3e1f-b8bb-a252e8ce19a6 | -9.52948 | -51.66947 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69a0ab5e-8fe3-386a-94bd-ed1a10e8661c | -8.23847 | -54.93936 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c52a8d87-2227-3ab0-99ec-397204df8ab2 | -5.48696 | -57.15062 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b1d6ca56-537a-3771-8aa8-fd300c094586 | -10.86187 | -45.31108 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0e397dd7-9912-37e0-91f6-fde5feccea45 | -6.9306 | -55.62808 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86b4b950-7466-3c7b-9300-3d3feb1f8714 | -6.12785 | -53.55117 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d338e57d-10c1-34ab-abaa-31a0fed85ce4 | -11.25232 | -50.57944 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 850d42f6-0eac-3186-a41f-4c8b025bbb64 | -11.51411 | -50.29372 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1cc3ed91-8caf-3a80-8067-086d876b1ff6 | -11.92275 | -45.09621 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17988dc7-0375-36d7-b1ee-f71f25cbba26 | -7.19137 | -60.67913 | 2026-09-01 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6c9bbe41-6ff3-367f-be78-2d20ff43e244 | -6.3463 | -44.09317 | 2026-09-01 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b1957e43-0d7c-33d4-b698-212056a5335f | -5.98155 | -53.61391 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49747c2d-2234-34a9-8b28-963799fc7598 | -6.60571 | -58.6044 | 2026-09-01 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 352e4f8e-38f5-378e-a87c-10e510179d1e | -5.24868 | -55.91507 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c578a356-5f02-3ca4-a77c-ffc6fc7eefdb | -4.79693 | -55.97213 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ff0ac74e-69cc-346a-84e3-11e75dbec2c8 | -11.32646 | -45.16367 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7901e331-2317-30ae-a768-a6a552f410ed | -6.0891 | -57.71783 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12536421-e1f5-3b33-bb44-751d047b48eb | -11.24584 | -54.01303 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64d921e9-68c0-3385-804b-e02efca26995 | -8.79814 | -62.51376 | 2026-09-01 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be7409f4-dfdf-3c2a-854b-7b9667336299 | -5.9452 | -57.68781 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 940f03e0-0209-3b51-9e04-14f1f723884a | -6.2474 | -55.42587 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 32e1ed9e-6589-3f99-9219-07a8dad4436c | -7.34528 | -60.59106 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eef22ff9-523b-3f37-96db-3c38c7e412d6 | -10.32277 | -49.10886 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f880b195-f610-35e9-8148-eb48af2e220d | -11.80921 | -46.03975 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63d21aa4-c4f1-3ba5-b9a8-1caf0feb6f25 | -5.85513 | -57.55318 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fd295714-3c74-31ca-a06d-2f0b2d874f6b | -6.80262 | -59.45967 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d295195c-fcaf-3114-8641-3ebeb0839e1d | -11.24737 | -50.58942 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 96b7fa82-d3f4-3a4a-93da-f13e2615858f | -9.16281 | -60.28884 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af7d5e12-4ce5-346c-81a1-d28e5db6c7bb | -7.54658 | -47.32489 | 2026-09-01 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8aba4aa6-c075-3fd6-835e-a2cd17384e6d | -11.10319 | -51.54709 | 2026-09-01 04:40:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8431d844-d057-3775-b79b-de4970ba41a8 | -11.93426 | -45.10648 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 009eb9d2-bbbf-349a-871a-92d421506491 | -10.75645 | -54.06484 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 77622887-42f5-3191-9721-7d90fd578090 | -5.24716 | -55.91307 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 657acc1e-4278-3232-9380-cd09fd5e0fe2 | -5.86006 | -57.55412 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c461dbd9-f636-3843-aa16-a27388332e8c | -5.2583 | -55.91238 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6bdb5356-a0a9-3f53-8f85-641be6d6f4de | -6.95198 | -55.65129 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bcbcebbb-9af3-3809-8c58-4efacbc3c930 | -3.62114 | -60.55849 | 2026-09-01 04:40:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7b3bb0a8-f1ad-3067-8979-84baa95d0fd4 | -7.34173 | -60.57695 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| bd20f355-55b9-3d4a-90b3-22b8e796ade2 | -7.08567 | -45.65509 | 2026-09-01 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6d5f4ac5-f74e-3048-aa32-2a80ac63174e | -6.60269 | -58.59064 | 2026-09-01 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dd53a672-b562-3c63-ba3b-5c026307d001 | -9.71982 | -48.13428 | 2026-09-01 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4726eee0-ce61-3418-82b7-248138dbf74b | -6.95046 | -55.63454 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8dfe7dfd-6667-382c-aa14-d802e1264160 | -7.53682 | -61.38158 | 2026-09-01 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2fabf1a8-b67c-3800-b294-6d75e1446b5c | -10.0425 | -48.69227 | 2026-09-01 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 97da1307-7fe8-3c38-8811-defb67307a33 | -10.02301 | -44.69213 | 2026-09-01 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 918cc888-bc06-3c43-9652-ac587f904842 | -11.21448 | -46.14231 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0a7881cb-d2fd-35d1-b091-d6140b98918a | -9.18309 | -59.46098 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 562681a1-0f29-3ebf-ac2c-05407cea7b69 | -7.02747 | -55.63964 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ede1a50-3a2f-3ae7-ac4c-b73a7353ebca | -7.1145 | -49.92222 | 2026-09-01 04:40:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 289d29e1-6a71-38eb-8120-4951db37677d | -10.75396 | -47.99129 | 2026-09-01 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| df13966d-339a-3e61-96a3-29b7dcce9c2c | -9.39697 | -60.57788 | 2026-09-01 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee892f1f-8f04-301a-9be3-c4d1b812f07c | -10.76736 | -54.04433 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c8bf61d-653c-34f6-ab4f-41c607585be6 | -9.46246 | -45.6179 | 2026-09-01 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| adbda1c7-d8db-386a-92f7-bf4db02eb1d7 | -10.51432 | -57.42938 | 2026-09-01 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3038a5e2-4b40-3061-ad6a-ea9c41e7d57e | -6.8805 | -56.50921 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f256a114-fa79-3ce7-9c26-3e12c7dd6728 | -9.22311 | -47.99067 | 2026-09-01 04:40:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a653fbe8-35e4-3ef7-880b-bad5bb58a474 | -10.23939 | -54.34864 | 2026-09-01 04:40:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ceff741-ad39-3e72-9670-ffd8b80de71b | -9.39203 | -60.57291 | 2026-09-01 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d579fa6f-0001-3aeb-8195-7456f8e26879 | -11.29868 | -50.60837 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ec2ef94c-1a11-3691-a684-5dc1f606bd2d | -9.45315 | -45.62684 | 2026-09-01 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 26.9 |
| fbf4566d-dd1a-37aa-a9a0-20afd4ba02b9 | -9.46172 | -45.62299 | 2026-09-01 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e76dc017-b3a9-3a9f-91c6-3fc566b3fac1 | -11.47998 | -45.07997 | 2026-09-01 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2fb69ced-7464-32fa-9279-a55e70ffe20a | -11.25395 | -50.56894 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 409f3935-9c9a-3911-9749-babbe765982c | -7.19734 | -60.68002 | 2026-09-01 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 723fcb2c-8575-3c01-9b2f-86d3e4dc96e5 | -6.75584 | -44.57435 | 2026-09-01 04:40:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d99a2504-9bf8-362f-af6c-365ecce9fb25 | -11.67314 | -47.59718 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8fd389a6-4cff-3e5b-8966-2172228740a1 | -7.03284 | -59.21898 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 85966186-38f4-3dd9-8753-452d6755bfca | -10.74758 | -47.98603 | 2026-09-01 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c0cef67-220e-3cf6-b104-a596b212cc74 | -10.77537 | -54.0413 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c26db776-e3cc-38f4-8dd8-7df36f5bfca7 | -11.25562 | -50.57996 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ecd42892-9a62-3f7f-bb2c-bfb75d8bd1cc | -11.29697 | -50.57579 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 35.9 |
| d913c607-63ba-3d52-b343-6823a2cc9a10 | -9.39573 | -60.57415 | 2026-09-01 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e48dc5a9-969e-32f6-802f-4b273cf90121 | -10.06208 | -46.65281 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57164fe5-4c53-38f6-b7c4-581d3333a2ac | -6.56479 | -58.56054 | 2026-09-01 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d2021b2c-7636-334e-b9b2-cb75247bd88f | -11.25019 | -54.0094 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f142627b-c6c8-318c-a501-79bbd3176b42 | -10.74347 | -47.98954 | 2026-09-01 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 165ad3ef-5b57-31d7-a1bb-b9a0b1834a2a | -5.61494 | -57.35777 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98d2b1f8-73c1-31ca-bd55-541577c61e87 | -11.29588 | -50.5828 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 2dd39c0c-306b-3028-b7a1-37366fd7c48c | -6.29316 | -53.58536 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28d3c851-e064-3b7c-9fb1-b936764b295d | -11.21114 | -46.08157 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b5915bd3-9917-32ad-8c05-74fb66129460 | -6.81701 | -59.44324 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7538c15a-895b-359c-84be-1930d16a22c2 | -3.34301 | -59.4301 | 2026-09-01 04:40:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d1172dbe-0366-3270-b008-9d93190dbc13 | -6.94756 | -55.62584 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c666bed-45eb-3198-937f-4761e27ab638 | -11.48617 | -45.09676 | 2026-09-01 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README39.md)
