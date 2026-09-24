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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22c09b36-d23d-321a-badc-8fe0cf2662a9 | -1.27912 | -57.03733 | 2026-09-24 05:48:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 15df69bc-eb42-35af-9f6b-5567f213f463 | -3.81515 | -58.8844 | 2026-09-24 05:48:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8c707c90-992f-3667-84de-638c5823a5d6 | -3.68171 | -60.59406 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd644152-6ddd-371e-b877-8f6df2eb104d | -3.83553 | -59.3544 | 2026-09-24 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02ef39bb-e1fa-3886-9a37-28f4d5f117c9 | -3.4486 | -60.56074 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d29c8bb-0477-3c29-b420-305dc2696fdd | -3.68289 | -60.58607 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 665afff1-803b-3259-9c8f-2fae88e2e674 | -5.22204 | -60.05194 | 2026-09-24 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3712e9b9-e26f-3044-bc43-e419545b4ab4 | -2.64479 | -54.69436 | 2026-09-24 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 538e16bb-118e-32c1-98b1-34ca0e8107e2 | -3.79666 | -59.37066 | 2026-09-24 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6a3f29f-fb84-3c0a-bd11-14b02e70b761 | -5.10746 | -60.26283 | 2026-09-24 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 3fa68ef7-0383-3001-9f3f-47c15f2d9801 | -3.1693 | -60.09706 | 2026-09-24 05:48:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3681b7da-68a8-364f-8b17-6790c1ace5fc | -3.78727 | -60.75784 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5c2cb19a-39c8-3c09-a8a6-0a9f56fb230f | -3.68348 | -60.58208 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35f675ec-1fbf-36be-8428-81659f504f34 | -5.41229 | -60.21635 | 2026-09-24 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a849a431-8bc7-3360-b758-6b7ebbb6825c | -3.16489 | -54.60541 | 2026-09-24 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64f50c30-cc49-3830-a160-ef065c9dc6f5 | -1.83795 | -54.71769 | 2026-09-24 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 758b5bfe-9aca-3e19-b233-7337d339c989 | -3.77563 | -60.72 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c7f29b5-c2ec-32a9-831a-e66da6ec12fd | -3.15225 | -54.60354 | 2026-09-24 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 7d7b9fe2-adf5-3a2b-b369-162ee7336dcd | -2.84178 | -59.97046 | 2026-09-24 05:48:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d827ca9-fc18-35af-aa51-324c683bf170 | -5.37421 | -56.0574 | 2026-09-24 05:48:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4492fbdc-76e3-32bf-927e-52067ff1cdf7 | -4.13848 | -56.32637 | 2026-09-24 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 06c324cc-8f21-3cfc-b542-302cf3cf4cdd | -3.91734 | -59.6647 | 2026-09-24 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fe40ad7e-038b-3125-a455-2c47d2fe01f5 | -2.88751 | -54.08699 | 2026-09-24 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c809889f-335a-3c56-b49d-87d7652cde19 | -3.90271 | -60.59162 | 2026-09-24 05:48:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05bcdbb1-85b2-314c-836c-48dd14b120af | -1.83192 | -55.72227 | 2026-09-24 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| de8735af-4adb-3878-b063-cf3fb6a8f1d8 | -3.10674 | -60.70826 | 2026-09-24 05:48:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7bfd952-474c-301c-8a5e-33442d357187 | -3.83136 | -59.36105 | 2026-09-24 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cbb3b3a-08eb-32e9-9972-8df4ec2a5a3e | -3.67496 | -60.58073 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39e142ad-f9e7-3fb3-a032-972b518de13f | -5.8198 | -57.7382 | 2026-09-24 05:48:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 047dbeb6-c941-3232-a7ea-398ea5ece22b | -3.17707 | -61.10404 | 2026-09-24 05:48:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a7c0f1d-12ad-3320-b997-4220a189b062 | -3.81997 | -58.88506 | 2026-09-24 05:48:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2660b3e0-b9de-3bfd-8ad4-ef6f5f605485 | -3.77082 | -60.72329 | 2026-09-24 05:48:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb3609b0-ba30-3ab3-bae1-6a2d6a48177d | -1.92444 | -58.26134 | 2026-09-24 05:48:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fbe66a89-e59b-349c-aa84-a80549d59279 | -1.83821 | -54.71772 | 2026-09-24 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9867c8e6-f8d5-36ef-b56a-089cb9d24b98 | -3.83483 | -59.35925 | 2026-09-24 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53ea506c-f29d-3db2-835b-e5febf6130a3 | -3.9781 | -59.78692 | 2026-09-24 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5db26ee1-6343-3752-8410-f83e4d5b6e53 | -3.8536 | -58.89017 | 2026-09-24 05:48:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f14355e2-dcdf-3f1f-833d-310d76cb8fb6 | -4.06993 | -59.86293 | 2026-09-24 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 81ab969c-6ae1-3192-97e2-d3b3e8fc15ed | -2.5604 | -57.41747 | 2026-09-24 05:48:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46886195-282b-3bfd-bfe4-c4d78b48d37c | -3.23169 | -60.10445 | 2026-09-24 05:48:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a1fdfb86-c189-33e1-bdde-073260566029 | -1.63213 | -54.91796 | 2026-09-24 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8f4017ba-dda4-3017-a8fe-cf6b53eda0a6 | -4.72013 | -55.98546 | 2026-09-24 05:48:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9feaf34b-5f6b-3e57-b39c-f2d68d1c1bcb | -5.25103 | -60.17228 | 2026-09-24 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e72b52bf-83dd-3205-b024-bd914f8d814b | -1.27863 | -57.04055 | 2026-09-24 05:48:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3e31bc1b-4c8f-3421-a222-8dda9e53643e | -3.70807 | -54.19795 | 2026-09-24 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6eebc768-3b67-32f9-8e2e-c3e6e3b8f6d9 | -2.71407 | -57.50801 | 2026-09-24 05:48:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 40b79349-1f19-3338-bd06-9dad69939cc0 | -3.81439 | -58.88964 | 2026-09-24 05:48:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4f0f7de7-511c-30f8-80ef-7ba928dafd8d | -7.88806 | -61.17026 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b7a855e6-310c-3a3e-8844-027b70b3ddb3 | -6.44453 | -59.95142 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 812a1ca9-dab3-371b-ac98-c5dc94bca466 | -6.10447 | -59.87844 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d4947f8f-20bc-3a27-b20f-12e292607ea4 | -8.31099 | -70.54115 | 2026-09-24 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0095da96-4e02-3f06-934c-98f0d34a36dc | -6.67218 | -58.55415 | 2026-09-24 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fce614c-21b8-359a-addf-79fee025a9e2 | -6.31242 | -57.75092 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 06138704-3a64-3078-a853-7bf79ef631b4 | -8.88947 | -62.5472 | 2026-09-24 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7759de49-1918-39f4-b987-a276dbe04bd7 | -7.04619 | -62.93483 | 2026-09-24 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ded8591-53bb-3905-acd5-8092553b3548 | -6.34527 | -57.77195 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eeb0725c-980f-32cb-a923-58485bd3117f | -7.51776 | -61.47696 | 2026-09-24 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c70dd22-e2c5-3da7-88ce-29fe9c2c1ada | -6.10417 | -57.66906 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ccdcf08a-82d6-3cc0-8e14-b536563d180f | -8.19937 | -70.47475 | 2026-09-24 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27f24efc-408e-36d6-8a53-3e8d1dc10d52 | -9.87551 | -63.45444 | 2026-09-24 05:50:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 036736ae-4da7-323e-9a7c-085b56ef79db | -6.45264 | -58.12223 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67d795bc-26d4-3fc1-b2d4-db1f31048140 | -9.69771 | -64.90958 | 2026-09-24 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 913d7c3b-0208-3b6f-aeee-ee434bcaa0f5 | -6.68331 | -55.04619 | 2026-09-24 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 69bf66d8-7b87-3796-aac8-44dc9c19fe9f | -8.8809 | -62.54959 | 2026-09-24 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23561750-8768-3145-bdb5-ecc9a130575d | -6.54596 | -62.91696 | 2026-09-24 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b4c773f-a106-3a74-8c4e-b59a6d3f8c87 | -5.86348 | -60.15522 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73961ea3-c416-335c-8c98-b8188191ffb4 | -8.02518 | -71.36201 | 2026-09-24 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 828aae82-2db6-3a9a-8f31-3e69d7c98d23 | -9.03343 | -61.66142 | 2026-09-24 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f4b2ac21-aa33-39a5-a6fa-0c989b6b5767 | -8.38749 | -71.0743 | 2026-09-24 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef151541-7702-3283-85c1-8c3178542aa8 | -8.87266 | -62.54184 | 2026-09-24 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bec7cdf7-0bb4-36cd-b9a9-95e6bde34e6b | -8.061 | -69.91309 | 2026-09-24 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f341e98b-24b6-3bd3-8d74-084a56ae529d | -5.91991 | -59.91887 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d66448a-4907-3ceb-ade1-f4f7c80e605b | -6.45581 | -55.00509 | 2026-09-24 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de0949f1-b721-31ee-bb86-d1ea8003b69a | -6.67867 | -58.58289 | 2026-09-24 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66cee296-6eb9-3ed3-9ae6-92f16efd72d5 | -9.04442 | -65.40932 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df5339e3-99b0-3361-ab04-13fca23e34f7 | -7.67042 | -69.93153 | 2026-09-24 05:50:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19a2558b-822b-312f-9a5f-34a9be61632e | -6.10607 | -57.67328 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35a8cf53-1cb7-3e6f-ba24-0429756e7cba | -9.16425 | -61.36306 | 2026-09-24 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34c39b80-b490-3008-8ab7-7f2efb1fe312 | -9.22226 | -67.38692 | 2026-09-24 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 624fdb13-8bae-3619-b1c9-f6cc3dbfd2e3 | -9.69711 | -64.91364 | 2026-09-24 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 08da962f-6764-31f9-85f1-f50d5aa8f9b2 | -6.92596 | -62.90931 | 2026-09-24 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1b4b590a-e972-337c-b181-eafaa8bffbd4 | -9.72743 | -65.02528 | 2026-09-24 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa8a0837-a757-3f2b-9a5c-56e86b338aec | -9.56037 | -65.98621 | 2026-09-24 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97e92971-c71e-3845-9096-dc6fb4dbd231 | -7.47031 | -63.80891 | 2026-09-24 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84e747e4-9097-3399-b982-51de23382bd8 | -7.9023 | -61.16388 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 11619221-af40-3113-ae64-762788753579 | -6.66926 | -58.57536 | 2026-09-24 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a0f2350-a0c1-31e0-bb4a-23863b4b2161 | -9.71327 | -65.02307 | 2026-09-24 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2eb1fb10-562a-3b35-b346-03d422c2e5f2 | -9.71683 | -65.04835 | 2026-09-24 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9fc50b4-8da9-3e83-9c94-60802c96c8fa | -7.90111 | -61.17244 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fb9b379f-321c-361f-928e-d62466843bc0 | -6.04085 | -57.76788 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ff0c1557-69a6-3387-88da-584c48036f39 | -6.3153 | -57.74985 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4396249-8944-353d-b22a-bc0e9b2c2c0e | -10.37355 | -64.07909 | 2026-09-24 05:50:00 | NOAA-21 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9801ba47-5fd9-32a7-95fc-6759611dae42 | -8.1184 | -70.14335 | 2026-09-24 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0c38be9-ea61-3c0e-a5fc-36aacb7628a9 | -6.1084 | -59.88404 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2461ebc4-678a-33d1-8a71-fa512a3babb9 | -9.93819 | -60.72147 | 2026-09-24 05:50:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 25247487-c5d6-35e6-89e9-47d8aee10c61 | -9.69911 | -67.38424 | 2026-09-24 05:50:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58820b08-3826-329e-9379-a02721b29337 | -6.11302 | -59.88485 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 683c4e53-a8e6-39ba-9bbd-9e73b77310ff | -8.64892 | -67.0292 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5a390e7-9d99-39fd-a73c-3ad95e35b0dd | -8.87027 | -62.53709 | 2026-09-24 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2773a347-2d14-34d4-8a7c-ec6fd7274301 | -8.00723 | -71.30771 | 2026-09-24 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README83.md)
