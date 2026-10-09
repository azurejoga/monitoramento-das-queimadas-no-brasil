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

## Dados Diários - Página 164

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab8e0a1a-d990-37bb-ac2e-6f98855bbcd9 | -3.01934 | -54.04623 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8a8346e-d1e6-391c-8122-cdd5513de8ae | -3.10219 | -53.77606 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a42a7912-9431-3b36-bf70-0a030e6352cb | -3.11304 | -54.1591 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b003aa16-0030-3daf-ab21-bc66c2f3ff74 | -3.08611 | -54.30221 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5d9d034-bd90-389b-9b3f-91b1cc67e5e7 | -10.04577 | -48.21694 | 2026-10-09 05:04:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| df3e5b71-0f64-3953-835d-d67bc102e555 | -3.09514 | -53.95272 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb029859-6a0e-3f8c-9fc4-9c7b826ee506 | -3.28682 | -54.04021 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2114d7d9-ca59-30bb-8ce2-f4c8e4795b05 | -4.74502 | -55.65503 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 771c55b2-2af0-3640-92cd-202eda230b2f | -3.1033 | -53.9462 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 68b26072-8141-3d84-994b-f835cf35cebf | -8.70584 | -62.42057 | 2026-10-09 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8dc76d5a-6989-3500-b3b5-5293ae7895b6 | -3.30665 | -54.02781 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5014810e-a9fb-3a84-b7d3-e35c6580bf86 | -6.11017 | -53.50769 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cef7f804-30d5-3378-a48c-e938e2eb30eb | -4.30765 | -54.79956 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 875e019c-b1cf-3229-865b-47971139b59b | -7.47828 | -42.84524 | 2026-10-09 05:04:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d0f99d0d-cf24-397f-b497-6d01779316d9 | -3.47322 | -59.50179 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86a6d919-6b6c-353a-828c-250fcbe16d8e | -10.74661 | -46.59367 | 2026-10-09 05:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 45b3537e-b040-3010-afc4-fa1e430fe5bb | -9.84338 | -47.4774 | 2026-10-09 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 16ff87cc-bc0a-3923-9e1c-26ecb087e97f | -3.2056 | -57.86612 | 2026-10-09 05:04:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32ed65cc-a3cc-35fb-bedc-0943f70ea6de | -6.11282 | -57.85378 | 2026-10-09 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5638d8ba-8ada-3dc6-88c8-fe56495ff623 | -8.98642 | -45.90477 | 2026-10-09 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 986d34f1-a9f8-3c2e-a027-61262d1b38fe | -6.22305 | -44.14726 | 2026-10-09 05:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2d42179-46d6-3d15-9e7c-cc138db85dd6 | -3.41611 | -59.57414 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 14301e95-5d19-34e5-b200-bb5bd757b5d0 | -6.47304 | -55.47503 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e8a35d3b-63cf-3c73-8896-fa6ff81a2a28 | -3.03922 | -53.89408 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09eff095-b0a9-31e0-b88b-a6cb7b480334 | -3.31526 | -54.04086 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a6b1455-8b45-39b3-b681-e6d706c5cdb0 | -4.1578 | -55.14109 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5983bf2-269f-34fa-9c62-8aed9e26012b | -6.48725 | -62.8638 | 2026-10-09 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b6f58d3f-1449-3d16-8fe9-ac739dbed7e0 | -3.98184 | -59.35497 | 2026-10-09 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ce9e06cc-99bc-37ee-a16b-3ef8e9c7cfc2 | -6.48856 | -55.30336 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a7ed8b8-eebb-39a3-8fe8-cff14a75df41 | -3.52253 | -50.3422 | 2026-10-09 05:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a74869d1-2ae7-3586-8a4b-7615483678e5 | -4.93698 | -49.21596 | 2026-10-09 05:04:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 27f4ffcf-0087-359b-8280-0168121b1c48 | -2.99913 | -54.07933 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f93c308-b4e0-3971-b597-c3ea0e3c750d | -7.28752 | -46.15378 | 2026-10-09 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ccea8763-9ecc-3507-b946-c95b41df1822 | -3.15699 | -54.0871 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e91e76a4-e720-36a1-bef7-1cbf6cb1a809 | -10.87991 | -44.79232 | 2026-10-09 05:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b0a1914-22cc-3aac-a337-586920f6d3a5 | -3.79701 | -50.6161 | 2026-10-09 05:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32a9012e-e6ac-38da-9dd1-5be3d2815a01 | -6.51473 | -47.38763 | 2026-10-09 05:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62f2027d-ff7e-3015-bfc5-ad9adc71547b | -6.02328 | -51.72977 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de50558e-ca4e-3025-b5d4-b6675c017882 | -3.90269 | -55.89532 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 4b9e7387-8542-360e-8c93-aef4f3d066bf | -11.7664 | -43.53049 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 343fb258-a4b5-3710-b662-b1920c765c10 | -3.09636 | -53.94511 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbd35aa8-0e95-3364-8ad3-2e9f810a9cde | -3.29829 | -54.05769 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5a1e24a-c042-32de-b21f-ba0ef6090ddb | -4.41203 | -55.43302 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0bb41952-a40f-31da-a16a-57106bfdd2c7 | -2.93437 | -54.08084 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c1e195e2-4add-35e2-b474-d1cbf69ce411 | -9.25361 | -60.88786 | 2026-10-09 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0d640e1a-7df4-39bd-91ba-07ce4bc2122a | -3.20454 | -53.88024 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b52f51e9-3c14-37ff-b259-06551c018b3b | -9.91023 | -44.78804 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e193738-3f68-39ca-bf74-263aa663b2dc | -3.07594 | -53.9613 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65e38897-846d-301a-baf1-9d9511241263 | -3.09091 | -54.29494 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c96577a4-c631-32a2-af2d-d333d82edd26 | -3.26885 | -54.28643 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 163238ee-623c-300f-abef-55b19f8e6301 | -3.325 | -58.15336 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e819b1bc-818c-3f76-b06a-35e9703bbdd5 | -3.74641 | -49.38908 | 2026-10-09 05:04:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac3be2f1-e010-396b-90d8-2b07ec1030d2 | -2.57031 | -56.14716 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 022d7513-2cfc-3252-84bb-11018c02933b | -3.17882 | -53.8417 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5480430a-6871-3231-b90b-32fa436dcf56 | -5.88158 | -53.51824 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4dade879-5546-354e-9e65-1d237c3d3242 | -6.01672 | -40.97868 | 2026-10-09 05:04:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 59b377e3-bee6-3f34-bb50-93b08c5b5eb0 | -9.89954 | -44.7897 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 473c67ac-2861-3be9-9e1c-6f67c4fee037 | -4.12569 | -59.88915 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 985a0aa2-0b2e-337c-9de3-1e91dc99bde5 | -11.00756 | -45.41645 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 50fb3c67-24dc-31f6-8a9b-064a0c0ad61b | -8.32152 | -45.44701 | 2026-10-09 05:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31d0b8ed-792e-35f6-aebc-4e47351aa105 | -3.91464 | -55.74834 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f02897a5-e9d1-382a-a29b-b40d6a833158 | -3.73979 | -59.45493 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92905e90-a936-3569-b7ec-b421d9f79bec | -7.1792 | -52.61287 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5c95687-373b-382c-901c-314213765cdf | -3.0573 | -54.03272 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c2f7734-4303-3322-8e8f-0a72434917a4 | -3.0157 | -54.04259 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d746bc17-70b9-3c4f-b437-bb648848e53f | -4.10863 | -54.62651 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d051f416-9e47-37ad-bb06-9a5cc56154d6 | -3.54497 | -54.68162 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d75a3087-01a6-38d3-ba31-a89e94e2b1fd | -3.00602 | -54.7918 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7bd64032-518b-369e-a0b8-a11c255c50a0 | -6.09063 | -53.47914 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34f8d85f-c692-3b2a-aa6e-f94c0fdfdd44 | -9.89362 | -44.79481 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b46945be-4c39-39c5-aa61-9a7bdae9b8d3 | -8.56323 | -46.89724 | 2026-10-09 05:04:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b78b7643-dc05-3832-9604-30e382d0928e | -8.32484 | -49.11844 | 2026-10-09 05:04:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 609c8bad-7bce-3684-ac1b-262e289f1d96 | -5.96949 | -55.35941 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c138670-c95d-334e-9b09-5c8b8f392bf5 | -3.92071 | -55.85409 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0892ea7f-9eef-3fb5-8bd2-8df81ec41119 | -3.39906 | -60.84826 | 2026-10-09 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62464b42-82c8-3fbc-8937-7ec67b0b75c9 | -3.305 | -54.01585 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2edea74a-9a36-3f25-bef3-38562989403e | -5.26579 | -50.14292 | 2026-10-09 05:04:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb685c6b-1a1b-3fac-a8ea-d6af410b1275 | -6.43655 | -52.66919 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bc215d5f-a65e-3065-9795-6296a2f6b715 | -6.82812 | -39.56135 | 2026-10-09 05:04:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a927356d-49ff-3cc6-85af-dcff72acb648 | -6.24255 | -52.67765 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a178e20-5eca-3e0d-bc21-1db966d18c87 | -6.01215 | -53.52853 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50bb84cf-3f78-33dd-b0af-305da3122eda | -8.40794 | -49.5445 | 2026-10-09 05:04:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 390c4677-18ee-322c-971e-ea72c71a6bd1 | -3.57196 | -54.48989 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae58d987-9767-3e00-b136-0133bc05c444 | -6.03795 | -53.48529 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88b07e01-24ce-36cf-9d64-b9ea56b80f72 | -2.91538 | -54.10944 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7708a60-bcdc-3524-928f-910f0127e369 | -3.25773 | -54.0435 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e1ec842-cf97-38e9-aa63-d066722f9468 | -3.19648 | -53.95263 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a69d9c9-2937-3792-bd98-ffdf51637633 | -5.69347 | -53.49227 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0621f1e1-a3a7-375e-b605-fa340f9cc39a | -6.09787 | -53.49845 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2cfb0c9-a4bd-3674-a9f9-1702b0cac722 | -4.13287 | -51.02862 | 2026-10-09 05:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f59cee8d-86df-31d5-a614-0ae2d4561d86 | -10.29389 | -46.60649 | 2026-10-09 05:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de1d41be-ff57-3c5a-9b8a-fbb17e8893e7 | -3.00151 | -53.90747 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f6b174b8-b9d1-3eba-88db-5b5113a0682f | -7.18476 | -52.62089 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad476419-f2ec-37c9-8c9b-16ce1bbfcfb1 | -7.25008 | -48.06477 | 2026-10-09 05:04:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e158950-56c5-3840-bb10-c71b5710df74 | -4.96333 | -55.11942 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3ef65b2-dc6c-3d7e-9193-9086e1574167 | -4.32687 | -55.0191 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a9e61df4-25ed-3d00-9b55-104a9133d1d6 | -7.08659 | -52.6875 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 798c5fe2-c6a1-3093-915a-8a6538269897 | -3.10158 | -53.77984 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 72f9145c-dfbd-3ddd-9286-4932671eaf88 | -2.99683 | -53.91452 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 7d41a58b-19a9-3479-a602-8c5bc29baa5e | -6.03738 | -53.48882 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README165.md)
