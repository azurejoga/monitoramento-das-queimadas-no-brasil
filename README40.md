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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c851e68-2d72-3a4e-b61c-02af33ae3d81 | -11.62909 | -46.51863 | 2026-08-22 05:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c72f0110-287f-3f36-b91c-7b55eb3c7de5 | -8.53973 | -54.81312 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 608e7a1a-ee97-33a6-9ccb-027be66b23e3 | -8.52596 | -54.83339 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 434984a2-2504-36b6-a238-8a7994b24d28 | -12.8247 | -48.45573 | 2026-08-22 05:04:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1cf4340d-dff1-3796-bfaf-924186d685ba | -8.02866 | -54.01859 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37a56cad-76d5-3670-93b6-1d1c1af5a5e8 | -8.68359 | -54.74644 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 847a3a29-7dbf-3076-a989-277bcd4be14c | -9.14937 | -59.55854 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe021ea4-a54a-3d0c-b55b-57dbecbb8d32 | -9.21306 | -60.77053 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3f9971bf-d006-3556-a99f-0c2bd13660b4 | -9.0534 | -50.87932 | 2026-08-22 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b38196d2-6831-37de-bebc-873f5076341c | -9.24237 | -60.79681 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c615a2c7-646b-3cbd-a03e-093563b4cd83 | -6.11435 | -57.69237 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48e730b1-0628-353e-a8d2-dc911c90e817 | -6.80917 | -59.39728 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dac7ef4e-07fd-3c9a-98bc-a556010f248e | -7.87262 | -63.74463 | 2026-08-22 05:04:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6ff1ce0-365d-3034-a93f-45516b3667ca | -6.65875 | -56.3397 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e9c1b37-7dbc-3ff3-9808-26c1e9dacd2b | -8.03089 | -51.79729 | 2026-08-22 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6b5cf47-6133-3e7b-a4dd-2a46f258aea3 | -10.51581 | -50.82613 | 2026-08-22 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 681de32d-3268-32b4-96d4-d1f2e7fa1dad | -8.53109 | -55.32038 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdc17764-c17c-341e-aa8f-c7029baccfa2 | -8.60158 | -54.71095 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 599fb993-5384-3930-9196-70a5da0e8e26 | -9.12165 | -61.59903 | 2026-08-22 05:04:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c1dfa3be-9144-37ba-adfd-a8cc2f399fa8 | -10.75636 | -50.26046 | 2026-08-22 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc8363dd-cc7f-3484-9637-6a50d572ad18 | -8.52436 | -54.82184 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d247d87c-8543-363d-af92-b1e331788c58 | -8.58125 | -54.79362 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de741346-20de-3670-8a7a-ef824b9e6cf8 | -11.211 | -55.04664 | 2026-08-22 05:04:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0d0a4fb-ce8b-3b78-98f6-14d169470be9 | -8.52496 | -54.81818 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f815dd30-5925-361d-8744-01dc59823195 | -6.74244 | -58.57861 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 521479b0-90e0-36af-bdfd-190056e034d3 | -9.39909 | -60.5831 | 2026-08-22 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecd60da2-e32e-3b64-acb8-82a5a6c07cc2 | -12.25663 | -43.17943 | 2026-08-22 05:04:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d43c27cb-c47a-3ece-81b3-9f8c219d33cb | -7.60214 | -60.83175 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be578359-0eb8-3389-acea-7855b9e32683 | -6.57433 | -58.98273 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59bd8f01-2c5a-3462-ae74-f4d7146c3322 | -6.79818 | -59.596 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5bd6b856-3372-3f50-a0c2-785fc3f58a30 | -13.4359 | -51.82691 | 2026-08-22 05:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08347d27-589c-341e-bfbc-ce5576fde73d | -8.80805 | -48.5434 | 2026-08-22 05:04:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2d2d8633-66b8-3a05-8e7a-354987b772bf | -6.56775 | -58.96862 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6eb591c2-2999-3822-9e2d-8565a8e2d1a2 | -9.21448 | -59.77459 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7d78a46-424c-31a0-b6d2-d98e75f86081 | -8.99544 | -50.71309 | 2026-08-22 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1553ff21-eb61-39db-8896-a494bf3d9cf0 | -5.7943 | -57.5447 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 779dfe91-9ffc-3a53-8711-6957fe766dd1 | -8.54621 | -55.30674 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f898d134-3902-3a2d-a495-0f0b6aff72e8 | -6.11512 | -53.07349 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a82293d-1211-35c6-9db9-029a6c621eb2 | -11.13814 | -49.04095 | 2026-08-22 05:04:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac95aaec-df0e-3bce-82dc-c20a69a22ddc | -11.44849 | -44.53873 | 2026-08-22 05:04:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27961f5e-8437-3ac5-ac28-430f8de0a0af | -6.89315 | -55.71272 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45ddc396-08c8-30ff-951d-6043896e5436 | -9.17853 | -59.46912 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f0ef1cd8-b9a7-3820-91ad-9b18835124f8 | -6.80262 | -58.98909 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c7595dd-b4e8-31ae-a7dd-9f9e45ff265e | -6.84861 | -59.43623 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ec36550-3360-3479-92da-7675544b53c8 | -6.55924 | -58.51304 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3642843f-9115-398f-bf92-d5712984ad57 | -8.61219 | -54.73138 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd4e09ff-3456-30ba-a4d8-992101030b25 | -6.1566 | -53.70445 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ece2d7f-acf2-32f3-a2fa-2b8d4b375b8a | -6.76754 | -58.68917 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5b5c7e5e-b1f1-37e7-826a-40b989657e6f | -12.72226 | -48.41801 | 2026-08-22 05:04:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5a6c8aa1-d86e-304f-8224-54bc74830450 | -8.38902 | -62.69201 | 2026-08-22 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| cef23d0c-a25f-328d-9424-e4ceb512714d | -5.74536 | -53.58808 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8136bf2-426b-3163-91db-1adbe0376e30 | -8.52955 | -54.81142 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 21536cb4-9387-346b-9fc9-b19e0d19ba9f | -6.93239 | -59.30752 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49aa0a8d-5212-38c2-a71d-ab73113494d3 | -9.21601 | -59.76596 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 264cf34f-f8a5-396c-8521-70d40b3b7a8d | -8.10797 | -51.65722 | 2026-08-22 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89aee632-55eb-3cd5-9d6f-c6e514757fc9 | -6.85203 | -58.96682 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d224baa1-1b57-33f6-a0ce-5b6ccb6fcaeb | -8.52316 | -54.82917 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 7b192852-3326-346d-843b-c58bb46da9a0 | -9.17425 | -59.44287 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21a79a61-ba67-3752-993c-0f796ff48f4d | -7.04299 | -56.60939 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c0e1d01-93ad-34ba-aefe-b2ba2a5a6717 | -11.20705 | -55.04969 | 2026-08-22 05:04:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0c3a819-c936-33e6-a30c-ab5c74b723a8 | -9.15011 | -59.55433 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19b09fab-d329-34f2-a758-2fc54b1e6fa7 | -5.96375 | -51.95398 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f845b36f-7af2-3261-b848-f8aaa2444655 | -8.52695 | -54.84864 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 07b00b48-5e2a-3942-ab64-7849516c596b | -7.07834 | -44.99714 | 2026-08-22 05:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fdda0d2f-78cb-3baa-8933-fa385bc5caa0 | -11.16897 | -54.00488 | 2026-08-22 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fac838c-6874-39c2-9b2f-163d7ec281c6 | -6.81583 | -59.41214 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 48f182a3-350b-3f34-9c1c-05721bd68ffb | -6.76103 | -58.67567 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9ed68dd7-1a20-3944-b9e4-45e254bb9dbe | -8.58243 | -54.78632 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8ba03ff-ec68-369c-a033-732ffc5cdf6b | -12.27769 | -43.15554 | 2026-08-22 05:04:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 874fc38c-3815-3181-9379-45cc9420c035 | -6.72136 | -48.11407 | 2026-08-22 05:04:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e5f6a379-57aa-3724-aabc-5ba0874db324 | -6.93683 | -59.30827 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98d56481-47d7-376d-ab09-6a1b4dbe9659 | -10.80259 | -50.97834 | 2026-08-22 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b762cceb-d5de-33f9-82f9-f8c3c3e59fa6 | -9.42914 | -51.64342 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ca6a0d4-5d56-37b7-a071-4f275f983fbf | -5.90187 | -61.29489 | 2026-08-22 05:04:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2af68286-20a6-3350-bb0e-322341ead469 | -6.72531 | -48.11472 | 2026-08-22 05:04:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2007b41c-73a9-391f-8c37-84cb01a0e5de | -8.58496 | -54.74921 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20c112f0-904a-3aa4-a909-496d46110ad8 | -8.57759 | -54.75175 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1183eba-f0f7-3a70-96fa-6029b26407cd | -9.43769 | -51.61079 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35054610-d264-3190-9db8-3be430d6cff3 | -9.40668 | -60.4356 | 2026-08-22 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60a82b78-74c9-3279-b2ac-7d9f7d9bd02f | -6.85998 | -59.02428 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6051fcd3-f626-33f4-8d32-0e752b12d5c1 | -6.37144 | -54.95021 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f9609b7-8739-3898-a243-cf4a09ae42a9 | -6.75768 | -58.69563 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 148b22e7-4726-3737-bc48-bba79851e85d | -6.38755 | -54.96069 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9c250cb-39ab-3ee4-af07-5b99a0433d3f | -6.76709 | -59.77721 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea4e5bb5-3e84-352a-b3af-fac505c7283e | -6.43284 | -52.71565 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ce6ac43-b93a-358a-95e9-df0b7ecb41d7 | -6.76888 | -58.68115 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9c3f9a13-60ca-31a4-837f-8c378d38675d | -8.95506 | -60.59425 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 534ea7be-7597-31bc-b892-e86f5499095e | -6.12639 | -59.91009 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25ed2fd8-68c1-3e1d-a23b-a6c772eb4a38 | -10.52356 | -50.8231 | 2026-08-22 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e769c6f-200d-390b-9042-b959c3421106 | -6.36344 | -62.90263 | 2026-08-22 05:04:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e040bec-33c0-3be8-9e41-6221e8eb5188 | -7.33303 | -46.23852 | 2026-08-22 05:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ffaebce-489b-3185-9a32-10a5d0e299d9 | -11.83536 | -51.95856 | 2026-08-22 05:04:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7846f74-3496-3ebb-970b-3580598ee354 | -6.53413 | -58.53268 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b7b10a95-3e95-38b7-af0b-35f9cb3bc0ba | -9.16344 | -59.4537 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 22fa99dd-5c85-3b27-8b13-60e257a6f823 | -9.04589 | -50.8338 | 2026-08-22 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43ddd61e-e304-36cb-850f-6f4fe9958bf0 | -6.78799 | -59.43963 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cf1fd812-6464-3928-9eb0-96f61e72c2f0 | -6.15979 | -57.74375 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e1f5c6d-440e-3050-9050-3f68caea999c | -6.66982 | -56.34163 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d90fb16e-7692-3768-83ea-dc8cba3b48db | -6.91769 | -60.07138 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d3d6d7a6-a7d9-3f96-9393-4897efc34244 | -10.38565 | -61.20692 | 2026-08-22 05:04:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README41.md)
