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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e04904c1-286a-3424-97f2-ae60aa8170c0 | -3.76488 | -59.47744 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60509d07-ba12-3691-9049-4f1e8ef30bf3 | -5.82688 | -53.51906 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e468322c-b064-3973-91ba-b317e1cb3cd4 | -3.65565 | -58.87103 | 2026-09-21 05:04:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 07d01def-8431-3b17-8fb4-cdf96d84b464 | -5.85062 | -53.54193 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91af3e03-f420-319a-a63c-b3b1bc360c38 | -5.20096 | -56.10661 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bf62f55-3b04-3c87-8608-e2db999b0c79 | -2.86951 | -57.81225 | 2026-09-21 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5fe55c24-f46b-3349-8a20-5ba5cd8ebfaa | -6.28557 | -57.74426 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7b6ddbd4-42b1-34dc-9368-6ab1ffef7598 | -5.84657 | -53.52168 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e8c5b6b-7774-3b2d-878c-c25a6d3912d9 | -3.46455 | -58.40289 | 2026-09-21 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 23cb9678-46fb-38e4-8d7b-772d44169439 | -5.89496 | -53.64631 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c93e9a9f-48c6-3a48-8b50-cccb67edd27e | -5.88197 | -57.71864 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 456dccf9-dc66-38d6-983d-db1a1034c763 | -3.15368 | -54.84046 | 2026-09-21 05:04:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 855791f1-2aff-3130-bc5f-61428ef30707 | -5.88394 | -55.54723 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 79324b9b-d5b0-37fc-b3d9-84eef3677c70 | -5.85742 | -57.56025 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ff9777f-a37f-365b-ab54-6b5efe26d02a | -6.14427 | -55.70787 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95c1ee3c-29d7-3269-a8e5-a174b93b0f54 | -6.09685 | -57.62792 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c5174c58-a08e-34f6-ac15-279a432da495 | -3.3784 | -50.44135 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| eaecde18-ded8-368a-9d10-1f998d070feb | -7.24972 | -46.91147 | 2026-09-21 05:04:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 485745da-22e5-3a2a-9994-0d0271486c19 | -6.44448 | -55.63839 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea0e9730-c23c-3dca-a112-0660082bee1f | -2.81697 | -50.46687 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5af00eb5-5775-364e-80d8-13a5296d8523 | -2.46247 | -49.22641 | 2026-09-21 05:04:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe037f30-adfe-3f63-a974-4bdb5fec882c | -7.07967 | -46.28461 | 2026-09-21 05:04:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5f407bae-85e6-34d9-b900-b566a7c2f262 | -3.80026 | -51.35785 | 2026-09-21 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 834760c7-9e18-30b2-9734-fba34825c520 | -6.91709 | -43.72294 | 2026-09-21 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec7a27b0-ac3b-31ce-bd18-d5096a5ddaaf | -6.21804 | -53.57229 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2ef68eb-99e5-32e5-b972-d2bf5736027a | -2.46362 | -49.2241 | 2026-09-21 05:04:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f77f9c57-b017-3122-acea-a52618a12e2a | -3.45551 | -58.21378 | 2026-09-21 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0d2c3940-a26c-3fd8-8da3-096ad8bdc14e | -5.84081 | -53.53647 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d54a2c1-6d52-3d4f-822d-bc891f2bb16d | -1.24429 | -54.19004 | 2026-09-21 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af37e261-784b-3940-8da8-92d7f5878111 | -5.81505 | -57.54236 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8920ca88-e8ed-3291-8552-8cb03bf0675d | -6.2996 | -59.96512 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e0c55ce2-70b9-3a96-99f3-0fed85425019 | -4.33574 | -46.36922 | 2026-09-21 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49601abc-de6a-3798-815a-f84151554508 | -6.19933 | -55.44457 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5444db8c-8609-359a-9775-620c51be7e46 | -4.3494 | -55.6582 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09773fc3-c6bd-3ef9-ab4a-1491bfb1c9c4 | -6.12342 | -59.94944 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc91cd5f-c9d4-35a6-8d2f-58dcbee43590 | -3.0138 | -54.16498 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11720fce-ec42-3d02-b683-75176bdf1df7 | -3.32927 | -59.81242 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fee05d5-6d2a-3349-ab87-11958a673aa5 | -5.20811 | -56.10418 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2f2bc61f-e7b0-3695-b0e0-b5dff0bd36e5 | -6.97913 | -45.82233 | 2026-09-21 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4860fd2-b03d-32ba-ab36-c7a0825a3603 | -4.41043 | -55.24524 | 2026-09-21 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 883fb7c3-eb5c-3853-954a-0e544d3bee5b | -3.30368 | -57.86946 | 2026-09-21 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 32b01631-fe60-3aa1-8342-3dbb89c899be | -3.22576 | -61.04848 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41d634e9-5f23-3cfc-b1ff-4966e6d50483 | -5.83035 | -53.51958 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abfdce38-1626-3975-9554-4ccf294f2bb7 | -6.14364 | -59.94574 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d3f1638d-4d70-399b-8ef5-32f80701a1f7 | -5.84138 | -53.53264 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36861066-ee56-3fd8-8ee5-986b701bda83 | -2.79342 | -59.88895 | 2026-09-21 05:04:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e3eb0f82-3694-364d-be17-1a3ea9b2a11e | -4.01725 | -53.49377 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71459f9b-ac55-3e62-9e37-4f83e4b4182a | -5.84429 | -53.56055 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2818efb5-08bd-3afe-894b-5f284989f356 | -4.09822 | -52.11725 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0526293a-7c66-32ba-83fc-ce02da2bd90e | -6.14374 | -55.71132 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7a752a9-3655-348f-b429-c19c4a7ee9d5 | -4.40213 | -55.23339 | 2026-09-21 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c9a21f9-a4e0-3994-9050-6abcbb77978f | -2.99938 | -54.16992 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3daffdc-0ba7-3201-b7b7-92872acdb494 | -4.54782 | -54.93089 | 2026-09-21 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 88b0acf8-36cd-34b0-8a5c-6d000a3f373a | -6.2082 | -53.56689 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31059da5-3e5a-3009-baa7-9d86477f9a6d | -5.83499 | -53.51247 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a382e464-33d0-360d-9ddb-ea1d9a0baac7 | -3.43808 | -58.23176 | 2026-09-21 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 670e3459-d32b-3d0b-a6f3-3a43bfdc2877 | -6.13171 | -59.94608 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 26381bca-2f61-307d-92c7-ad4c4bec9d01 | -6.0246 | -55.3425 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bf352a1-6095-3364-b40a-c7aef3785f22 | -4.35428 | -55.49706 | 2026-09-21 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b97e4298-bd90-3e1d-a17e-d0404578e4d6 | -2.8256 | -50.46306 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 78b4d422-b0c2-3006-b6d0-b1d48fa084e9 | -8.37683 | -45.63361 | 2026-09-21 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1fa217ff-aea9-357f-8701-b16c77a8785d | -3.43922 | -50.60264 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d952236a-0a9e-36ca-9450-a7d51c10b8e0 | -5.82229 | -53.5027 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6bacc68-1bf5-37ec-b24f-b85e7db0dddd | -6.91576 | -43.72527 | 2026-09-21 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 83266131-db6f-3e0d-8fd9-5ee016aea7b4 | -3.6638 | -54.26876 | 2026-09-21 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5838c5b3-fc6a-37e3-bccc-4f3b9776fdc8 | -3.60691 | -54.04309 | 2026-09-21 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a49e03a-7f98-3f5a-bc22-af107d6389b1 | -3.71706 | -60.55468 | 2026-09-21 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67ec79ce-6d3c-3ae0-9efe-9258fe8bcfc4 | -2.48357 | -58.00725 | 2026-09-21 05:04:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d129f3f-7677-3648-b6c6-4d353102460a | -6.24347 | -53.30976 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44563579-b339-309d-bfc7-66fd3a00cfaf | -4.87901 | -55.88263 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d501135d-107b-31f0-8f10-1f440590c107 | -3.00774 | -54.182 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bfa19a61-a5c2-351e-bc13-42c9441446d4 | -3.00828 | -54.17849 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3974d2c6-da01-37f5-b263-15174f55f2fd | -7.43078 | -44.76775 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0a14436-238a-3a7e-9815-b74461c18ea7 | -5.97026 | -57.78155 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b9a8972-2c4d-382d-a2e8-f39586ecc0f5 | -4.9469 | -55.79819 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eeb0a946-6c2f-3ef9-889d-478e83cb4e49 | -2.45875 | -49.22741 | 2026-09-21 05:04:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 915a6c95-1ed0-3a67-b3c4-1ad00320e40e | -3.44268 | -58.01925 | 2026-09-21 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1d4bdc4a-2841-303e-b6c5-b6bf85cbc2e7 | -6.22647 | -55.61868 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cafab488-ce4f-3985-8fa2-b8ecf23fe552 | -5.20426 | -56.10712 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e33c8572-de0a-31f5-b987-9dc53922a5f0 | -3.49285 | -59.57312 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 10794f42-9645-33c9-b2d8-ca9d59e20027 | -6.34987 | -57.89051 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1af42400-1686-3054-9c12-db044c274f92 | -5.99552 | -45.24861 | 2026-09-21 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d88533d-5a51-36cd-9fbe-3945b72f3298 | -3.49435 | -59.61235 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d1fa771-85cb-371b-bb16-59ef053536f5 | -6.10168 | -57.68484 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0bade9ae-f550-3a8f-b2e1-0bd5c7eec579 | -5.261 | -55.92177 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d04543a-a528-30fe-bda8-7f663e40cf68 | -5.83153 | -53.51193 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4f08441-0d1c-3b47-991d-73298de3c0d9 | -5.8074 | -57.7445 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d38f6a45-990c-3b8b-8ba7-fc88668f8d04 | -6.07859 | -57.65495 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e7b6093-b908-3512-8de5-23bd29d8c08e | -6.39684 | -55.2654 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0176597-b0b2-3e42-b6df-d37c82f64dbc | -5.8153 | -53.52516 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3869be5d-9013-34c5-ac63-cd5401737ae2 | -2.82426 | -46.70858 | 2026-09-21 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b33e12cd-47ff-3bdd-8177-3360c95bf21f | -2.88021 | -57.78982 | 2026-09-21 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eeb1e3e5-3f8f-3367-b311-d193a8581531 | -6.09085 | -55.5512 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bc0bff9-d516-3ebf-8b0c-f25746747927 | -6.72755 | -55.08387 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 65d8b040-ca99-339b-9981-086d8bb916cd | -3.68973 | -60.59468 | 2026-09-21 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 395723ea-6cf5-342a-b9bd-baef6fefd266 | -4.45209 | -55.43827 | 2026-09-21 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 812c050d-ebe9-3d6c-88f1-3269745b34fd | -7.38882 | -46.03853 | 2026-09-21 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7dff526-7d77-353f-9e9a-746f83add3dc | -6.3216 | -60.02093 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c6f7b13-a5ee-3f74-86d9-3f78ea11ad47 | -2.25018 | -56.65601 | 2026-09-21 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4e1a3982-7b08-3685-b7ad-f4d7ee0fe354 | -6.92959 | -55.64763 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README61.md)
