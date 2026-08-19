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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 404f2a9d-6a42-3347-a29b-9fd7efd7aad5 | -3.10073 | -61.20287 | 2026-08-19 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0e3da79d-d207-38d7-a2c2-6f6108669682 | -8.22159 | -55.02805 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4a68df1-4e92-3ea9-89b3-e0ed326fb2a5 | -8.57324 | -54.69233 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 22cb668c-b926-38dd-b262-a002d703b8dc | -6.86296 | -59.03846 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 16a47075-e426-39dd-932c-bd2989d8207b | -9.28577 | -56.89249 | 2026-08-19 05:23:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d9e9b657-e79f-3925-a871-74a85ca7928d | -7.46185 | -59.99555 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a9b743e-08ff-331d-8bc4-bca68c44cd9a | -8.57818 | -54.75266 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 49f5e93b-1411-3d5c-8a65-20f39ce29942 | -8.54452 | -54.7679 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5edf51dd-68df-3340-a79b-ab8f1e580d19 | -6.84433 | -58.99495 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fba5fc8f-ba8e-3ccc-acd2-0b91a5e16cb5 | -8.58793 | -54.71392 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8935094f-0f56-396b-ba5c-3ff98ed6235d | -7.05025 | -56.52258 | 2026-08-19 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 928b9408-cc31-34d4-94b9-d7f6c492c59a | -8.57733 | -54.72571 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c0b51149-6457-3b5d-88f7-cb06fbb221f0 | -9.4237 | -60.45203 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43f5fbb1-be23-33db-8341-626b446a0d53 | -6.70074 | -58.95033 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea4dc007-38eb-335b-8234-e06b2e34ad50 | -11.16749 | -49.61716 | 2026-08-19 05:23:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ad71b7e3-fd4f-385e-94b2-76b86eb71a22 | -6.95526 | -59.04886 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0126a088-207b-3277-9907-1fcfbf7de198 | -8.57675 | -54.73 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b766309e-a978-329a-ac4a-ff51fcfb06a3 | -8.96492 | -60.49598 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 593aed90-74d4-36f6-923d-ade1f4cbcf78 | -11.16216 | -49.62137 | 2026-08-19 05:23:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01a504ee-f354-34a4-8165-d4b265ea3379 | -8.56439 | -54.69106 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05d88ade-f12f-3f51-8b89-1fc0632e4d15 | -7.90861 | -61.73091 | 2026-08-19 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e50cfda-493c-38a2-94e6-278d91f89f5c | -8.54072 | -54.76305 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 968dd18c-1bb0-3552-a38e-1a7bbaed69c2 | -8.21786 | -55.0233 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c41db6ad-0c4a-3d5f-937e-95e448a760a6 | -9.41578 | -60.57001 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3cd58823-9ad7-367b-b042-e35343f0f646 | -6.88391 | -59.03788 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf672e69-8b5a-33b4-98bf-52464d4daa84 | -8.53314 | -54.75307 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7655cba6-f761-30e9-9a43-4cf32d8e91c9 | -7.53953 | -55.57679 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6424b7ef-243a-33e4-96a4-792afc8d643f | -8.57069 | -54.67847 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9d39e0a-cbcd-3b25-b621-d2bed8274695 | -6.70527 | -58.94347 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f70368e9-5405-3f0e-8b92-aec7f5800ec4 | -6.74476 | -59.17015 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 468508f1-42cc-302c-b7b5-9149e6b6e5e7 | -7.55343 | -55.56761 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fde2cd41-5140-3332-beab-a2fcbc7b54c8 | -6.76144 | -59.46727 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 066f6c20-38d8-36a6-9440-0ca4432ccbce | -8.57967 | -54.77477 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a004a6e4-9a5b-363f-b5a1-084241661b3c | -8.57791 | -54.72144 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 16197c1f-6e5f-3049-b128-2b4470083cc3 | -6.74704 | -59.17796 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d8de005-9847-375b-909f-0286aeddaf2a | -7.45797 | -59.99855 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d097d89-ac0a-31e3-b5cb-f41c1890a916 | -4.71325 | -47.15133 | 2026-08-19 05:23:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b9a1c1a3-66e9-38e1-97be-5be9172f566d | -8.57262 | -54.69672 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| df3f8aff-c492-3c04-88d8-6c0966874e71 | -8.57145 | -54.76917 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 34fec45b-a65e-3008-ad17-0b0170fef189 | -8.56074 | -54.74852 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6f80c6e1-0d8b-32cd-9fe2-b59e5f3e3f19 | -7.43666 | -59.78185 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7fe4fd4-e868-3465-8bd4-cc73ae228b2d | -6.5948 | -59.11388 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67cd894c-1c43-34ec-b985-faea29a4ef00 | -8.55392 | -54.7649 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ac61ca9a-bc46-3acf-9d20-ce34d7aa1fd3 | -6.85227 | -59.01122 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7488317-941b-3b4b-b1a3-5035e64fd79d | -6.76699 | -59.45354 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4239ae1f-0840-3aab-a334-131c4044fc3a | -6.88793 | -59.05723 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a01345ef-952d-3e39-bb54-5cd3e4337c35 | -7.10582 | -59.76706 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 987b3e0f-5554-3eba-8db0-b32e457e3558 | -8.57377 | -54.75202 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4d61f7ca-aa67-31a5-bd2a-c437665db6ba | -8.57291 | -54.72512 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 667b75b8-ceb6-3241-933f-d9e02ace3502 | -8.56264 | -54.76793 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8d54dfe0-2009-30e5-b30a-62bf205b064d | -4.71242 | -47.15745 | 2026-08-19 05:23:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bc40df6d-ddc3-3a44-9766-948baa152fb8 | -9.39969 | -60.56389 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 771ebdc8-be62-3e2a-ae44-8298d810fc78 | -3.10465 | -61.2217 | 2026-08-19 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66897b57-d8e1-3202-9c1c-474a1bb4c08d | -9.42579 | -60.41616 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6aeedbdc-5323-3ef2-9133-89d80896b22c | -7.61623 | -60.9714 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f5243cab-4952-391f-8998-3baec74c2cb2 | -8.53192 | -54.76177 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a05b0fb0-f4aa-3946-9565-fff659a306f6 | -10.8159 | -50.30221 | 2026-08-19 05:23:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4ef0a004-e4b3-390f-80dc-01b5ac3b6977 | -8.58558 | -54.73124 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f60312c7-994b-37b2-b658-2a55d0f14bed | -8.54011 | -54.76733 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a8bf7ec7-3b92-30ee-8331-30813ead7cc3 | -8.57997 | -54.73943 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6c1423d7-9cbb-343c-a40d-094f69f5a948 | -8.56936 | -54.75142 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7fe9a9cd-7d71-3427-88a4-50866df8909c | -8.5538 | -54.73402 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0762f2b0-c115-39f0-8401-4522eda1d4f3 | -8.90442 | -60.55849 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05b86e30-fa15-3c24-a9b3-85f3f342f4a2 | -9.42695 | -60.43082 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 713c6c8f-79e9-37c8-aba0-a9f2dfa5e43c | -7.53635 | -55.59888 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f39ab142-1bef-36be-b7b9-607b8ebd5f51 | -3.27104 | -49.52264 | 2026-08-19 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0f11a27e-564f-38d5-bcab-5dd1c2fe3792 | -6.79605 | -59.4434 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 472683af-fcc1-3d63-9322-f106cca58111 | -7.61954 | -60.97192 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9efada4d-735e-3941-bad0-1115fcef4e3e | -9.42478 | -60.44496 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26248ea0-65b9-3645-bd7c-89d686fc708f | -9.423 | -60.41209 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 75458d8f-0568-361e-9332-3acd534804cc | -3.27044 | -49.5267 | 2026-08-19 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8f315a1d-03be-30e7-9cac-7d683caa4575 | -8.57212 | -54.76326 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b9b6068f-31a8-3f7c-a364-a2f0fb8c5693 | -8.90008 | -60.58651 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27140e2c-a141-3601-83fc-8f98421b3ced | 0.24326 | -60.51673 | 2026-08-19 05:23:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f3ba31c-a6de-3a5a-8b8e-4c34dc2f930a | -8.56322 | -54.73108 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aa15d90d-9a6f-309d-bdd9-14457b34c9b1 | -10.10964 | -54.28675 | 2026-08-19 05:23:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 234f8a0a-69d3-3370-aaac-a6f751cae994 | -9.98631 | -53.93733 | 2026-08-19 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9eaab090-2e7f-3f74-93aa-23296c3f9ac5 | -8.57269 | -54.72782 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2ae6d986-b172-3c12-ab0d-c45ec04dd466 | -8.58142 | -54.76186 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a991dd71-eb96-3fbe-b978-0144d3c22159 | -10.11029 | -54.28193 | 2026-08-19 05:23:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 19f046ba-df7a-33a7-a60d-a045747d494f | -8.55635 | -54.74779 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f5fc350-2636-37c2-aed2-cba41ef4f07e | -7.56631 | -55.56559 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7651c478-ca8a-3cce-b389-2e7c40bb529c | -6.75152 | -59.17128 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b34883e-de6e-3187-aa71-0b1623406256 | -8.52814 | -54.75673 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d3e8641-82a2-3e27-9626-a8a6cce4bde4 | -9.4058 | -60.56845 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08ea6068-faae-3f00-9243-f1d96d00002d | -8.90123 | -60.60104 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09333302-2ae6-3612-93e8-453f3542ad64 | -6.87885 | -59.04834 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bf7764a-6fda-3070-a804-ea00f1e08c49 | -8.58201 | -54.75756 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c5ddb8a2-2af5-3ed7-8480-db0409898a7d | -6.79495 | -59.45053 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6ea53fcc-c237-3f77-8072-cad89725801a | -7.61677 | -60.96793 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f096b5e-bb66-3d17-9f21-a89878c2341e | -6.76925 | -59.46121 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c136a77-fbfd-3026-9998-caa5ce7b9257 | -9.42812 | -60.44548 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 575e3aac-b89b-3352-b2ff-55c12285bcc1 | -8.09795 | -51.66185 | 2026-08-19 05:23:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 910bf125-4e5e-3d5c-9564-1ef38f6d7c7f | -7.55754 | -55.56818 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69b0c368-44e5-3df9-b638-7e50617d251a | -3.69193 | -47.65391 | 2026-08-19 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 88b80234-4727-34e2-9764-a43ad22ae00c | -6.76049 | -59.15775 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 235e61d9-0ec4-3ca2-af06-b5da6afa7b60 | -9.40696 | -60.58304 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0eea7629-0b7b-315b-9480-389951e26798 | -8.50001 | -54.86201 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5b573aa7-8bb6-3ffe-b84d-a7fb66541cc4 | -7.56988 | -55.56989 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a12246e1-4a79-38a0-924f-cd51dd611932 | -7.57521 | -60.88693 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README56.md)
