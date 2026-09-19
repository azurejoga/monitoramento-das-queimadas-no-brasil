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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05ca4749-a9bb-39d1-a15f-2a6589cd2299 | -2.58823 | -59.99288 | 2026-09-19 05:42:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a41bff2b-1434-38f7-95a6-5d76eff448df | -6.76454 | -55.84714 | 2026-09-19 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59670b5e-e4d3-30ca-93d6-4658f45c9d30 | -4.49643 | -54.98265 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16c2cb6d-5452-36ca-8a73-747560e9e9a2 | -4.50992 | -54.96902 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe140571-b811-3cb5-a5aa-966b92c1a641 | -6.02286 | -51.76738 | 2026-09-19 05:42:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d341c118-6ac8-34e1-8074-99ea0e9ac51d | -6.45349 | -59.9811 | 2026-09-19 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 916cf882-c157-356b-8d50-349221e44fc0 | -4.42785 | -55.51207 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d53090d7-0562-3f62-b739-725e44990931 | -6.36951 | -58.29411 | 2026-09-19 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 052805e9-9e36-3c1c-b254-4c248bafff16 | -3.69992 | -60.61449 | 2026-09-19 05:42:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 317927c7-5725-3c84-bcdc-ca64c0b609e2 | -2.24775 | -60.03627 | 2026-09-19 05:42:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37b9e66c-47c3-3399-a8dc-2bbe5d74b1c3 | -2.8997 | -57.81024 | 2026-09-19 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 4dc171ca-fcc8-384f-a2f8-01b7da902b1b | -3.34307 | -59.81008 | 2026-09-19 05:42:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| fabc0a88-6ee7-392e-877a-92560d281fba | -3.15612 | -53.93779 | 2026-09-19 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80943fc0-6d46-37ae-a61a-ef276f2315b1 | -3.04052 | -51.37634 | 2026-09-19 05:42:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| daf051a2-a219-3e52-a03b-5c7b47dcfadd | -6.7416 | -59.42648 | 2026-09-19 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4d93b276-cfd8-3e26-a95e-1880b9acbe94 | -5.75936 | -57.45088 | 2026-09-19 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 78ff5444-1ede-353f-b73c-cf418f7d81a8 | -2.90037 | -57.80555 | 2026-09-19 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 610cbbc6-39a9-3818-9fba-5daa07448607 | -4.44364 | -55.00875 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a70030a4-29a4-37a2-81fc-a4f18ffe6edc | -4.48779 | -55.49104 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 291359a8-76c6-3814-97f3-29281e56b683 | -6.4416 | -59.97536 | 2026-09-19 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b96a071-8b0d-3d4e-87f9-a4873d20d5d7 | -5.74331 | -57.60349 | 2026-09-19 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba8ecc4e-1b28-3aba-a0d6-01a4090b0565 | -5.75778 | -57.44431 | 2026-09-19 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 542b613c-d39b-3468-9a76-ce2b899cbc5a | -5.74627 | -57.58206 | 2026-09-19 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fbc3872b-2ace-3be0-9ee3-035fdf0ded6a | -5.89737 | -59.94035 | 2026-09-19 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe1f9cf4-d20a-3727-8c6a-f7ed84870e83 | -3.12194 | -61.25341 | 2026-09-19 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5bc616f-c47d-3039-9bc1-e2cfce30f5cc | -3.55263 | -58.54776 | 2026-09-19 05:42:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 40529476-1d7a-3280-85a8-a8cc033307f2 | -4.21721 | -56.33277 | 2026-09-19 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b3c986e-b5cc-3433-bb45-4d3cce13b2a5 | -3.03758 | -61.24246 | 2026-09-19 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6142464a-69ae-3d76-9795-b40706eaa246 | -6.7146 | -59.46068 | 2026-09-19 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b4a2cc28-2dfd-3067-b9de-6900595da5de | -2.89329 | -57.78849 | 2026-09-19 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2beeb3c7-eea1-3664-ba23-2bca6d08b287 | -6.93794 | -55.03632 | 2026-09-19 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0eefd2d4-cfeb-3b69-a3e1-6a709e539c3f | -1.92636 | -58.33755 | 2026-09-19 05:42:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ae57ef8-dac5-3ffc-8465-129f1d1374f6 | -5.76274 | -57.44465 | 2026-09-19 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6172332c-23b4-3261-8adf-e573e79ebfc8 | -6.71087 | -59.45589 | 2026-09-19 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 950e31df-e69f-37dc-bae4-69b33dc53640 | -4.32178 | -60.88597 | 2026-09-19 05:42:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7228fe5b-d541-3d74-aae7-2e537e5f24f4 | -6.44879 | -59.98426 | 2026-09-19 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 12bd3e56-e3c0-339f-9d8c-97476f8a3347 | -6.7422 | -59.42231 | 2026-09-19 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c77b0ff2-f717-3070-b1a2-1c773d9ded04 | -3.55636 | -58.55268 | 2026-09-19 05:42:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 334c296d-4c4c-305a-b586-f00d25d65f4c | -3.71314 | -60.63106 | 2026-09-19 05:42:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f39653f-d2ce-3dcb-9eb2-dc0b02582e8f | -3.15334 | -53.9381 | 2026-09-19 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5205847e-b662-301e-a4c8-c2efd3ad0129 | -2.90427 | -57.81093 | 2026-09-19 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 2052c759-72ba-3673-ae66-fd160a0c2ee0 | -1.22602 | -55.72684 | 2026-09-19 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e39999bd-6662-3dd3-9050-d77c5fea925c | -4.49074 | -54.9819 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e74e0d7a-d680-3f18-912d-ac9458f5d085 | -6.02791 | -51.76524 | 2026-09-19 05:42:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5347b5e9-979b-3431-9439-1bd7a62c33b7 | -3.15016 | -53.93687 | 2026-09-19 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ac94ac8b-b398-33ac-8470-1c47d5e674e2 | -3.69781 | -60.62873 | 2026-09-19 05:42:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2892b0e3-111d-3aef-b141-8e910e7d7fae | -1.70297 | -54.89204 | 2026-09-19 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a68ba2a6-b50e-3859-abf4-4f2b81a5f9b1 | -3.1508 | -53.93259 | 2026-09-19 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e27f39bf-9be9-3a0e-ac0d-cfb987866971 | -3.0514 | -61.27335 | 2026-09-19 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d63e1597-32af-38e6-a6d5-0454523d0295 | -3.15395 | -53.9338 | 2026-09-19 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 455e25ea-7eea-3366-99cf-3d75383764bb | -1.22134 | -55.72298 | 2026-09-19 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fedfde01-0d84-3e54-9f61-2a04c906c97b | -3.69397 | -60.62815 | 2026-09-19 05:42:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba1e6345-3d98-3a62-b77d-c1ad5de6d468 | -3.79987 | -60.72342 | 2026-09-19 05:42:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8a1eae5-6ed6-38e4-82df-6f046cd6f28e | -3.21199 | -53.95387 | 2026-09-19 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa0fef3e-84d9-395f-b44f-9382ffcc6548 | -3.33505 | -59.80883 | 2026-09-19 05:42:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 91fab56a-6ad1-3775-b277-051a835fc60c | -5.75187 | -57.57739 | 2026-09-19 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d507e0a-2b0a-3094-b82c-2e716c749e49 | -4.56898 | -54.92093 | 2026-09-19 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f1e4ba90-39fd-3174-9291-e31ba884302a | -2.90487 | -57.80461 | 2026-09-19 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 0510aeab-19bd-3ee1-8637-7606f138b3b5 | -6.44935 | -59.98044 | 2026-09-19 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d1a1fc4e-ba49-3d3d-8c29-aa5d76992fc5 | -3.70931 | -60.63048 | 2026-09-19 05:42:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f368b871-6430-338a-9ff5-35bb52eb7e88 | -3.33906 | -59.80946 | 2026-09-19 05:42:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a138e7a8-3130-32ac-9750-8e7f6d285d60 | -3.69468 | -60.62341 | 2026-09-19 05:42:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29792271-b002-3def-ab3b-1fbd976a72bf | -3.11452 | -61.4224 | 2026-09-19 05:42:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e576617d-5c7f-31f0-9db4-9ec0b8b8ce83 | -5.76599 | -57.45661 | 2026-09-19 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8ac5e271-880d-3baf-9188-bd97cf4f416c | -2.64131 | -54.69083 | 2026-09-19 05:42:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f9f68f62-a2e6-3d98-99df-fcb073a481e8 | -3.73483 | -54.64876 | 2026-09-19 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29a157fd-ab11-3eaf-9f09-ad75a8a72374 | -5.7619 | -57.45037 | 2026-09-19 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 53f667e1-d359-3996-a0b5-88ce00803611 | -1.58176 | -54.432 | 2026-09-19 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 093d565e-a30a-36a1-9df4-601128648e99 | -3.14475 | -61.39993 | 2026-09-19 05:42:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 243a857e-6b64-3ef4-bf41-45dc43df65ca | -4.40715 | -55.50048 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61136ce0-d0fb-33b8-a360-77ef09c8287f | -6.7595 | -55.8426 | 2026-09-19 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf6eadf7-407d-305b-89c2-47c302f30c8b | -2.9063 | -57.79527 | 2026-09-19 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 44748d39-2f5a-38b1-ab55-cbb2881a0d3e | -3.35163 | -59.86135 | 2026-09-19 05:42:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 224ffdfb-c9cd-3bcc-acb1-4c2cc42a6ee4 | -1.58858 | -54.42525 | 2026-09-19 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d196730b-aeb2-3f52-8eed-50318dc98dcd | -3.11518 | -61.41816 | 2026-09-19 05:42:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76e5e2d4-e084-37e2-9f7f-0fe451f77fa6 | -3.338 | -59.81644 | 2026-09-19 05:42:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8d70fa83-2d50-3e55-85b4-421d056fcbf6 | -4.21 | -56.33337 | 2026-09-19 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46ebc1f4-dfff-35a9-be77-b5d34f728998 | -4.50751 | -54.96759 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 03a91d71-5ca7-3df8-ae24-9ae5012ebd8e | -6.71027 | -59.46005 | 2026-09-19 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9b918044-1c74-39f4-884e-08220783956b | -2.90558 | -57.79993 | 2026-09-19 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 678d281d-a498-3bb4-9596-b75e68938dd0 | -3.14411 | -61.40417 | 2026-09-19 05:42:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4129a059-a545-3e5d-9811-99e3d97b6df3 | -4.48884 | -55.48367 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6a8fa8f6-d09f-3e5d-9cb8-0c9f5bd25bc3 | -2.89258 | -57.79317 | 2026-09-19 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7db7d6c3-6cc8-3ecb-9cc5-d7d89c3e1ed9 | -4.42813 | -55.51716 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fab7279e-4ac5-3e3c-9d6c-bd86ea9822f2 | -2.90173 | -57.79457 | 2026-09-19 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f1f29342-2bad-3583-b23e-1bb401c2c553 | -6.45293 | -59.98495 | 2026-09-19 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9837b14a-50c0-3668-a76f-267b59f214c3 | -3.76063 | -55.95901 | 2026-09-19 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a297f4b6-672a-331c-a6d2-203275888397 | -4.06209 | -56.24841 | 2026-09-19 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9350f7e2-655f-3f23-a401-c69e2b89c7ca | -6.45063 | -58.14447 | 2026-09-19 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f4f57a29-2d54-3551-b5d7-d10a54249fce | -3.76109 | -55.95583 | 2026-09-19 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7b7fc83-93f0-3768-90f2-c88ff85e8763 | -6.13019 | -59.94331 | 2026-09-19 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 61b388b6-0392-3b52-b818-8992cba0bb45 | -5.74218 | -57.58587 | 2026-09-19 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e5f79f3-c630-3902-af8a-3a8a567b5cb0 | -5.91636 | -59.95477 | 2026-09-19 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bda4e9d6-8841-3a8b-a6b4-ff8bf1b4021a | -1.927 | -58.33339 | 2026-09-19 05:42:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac7c8f19-c288-349d-a0d4-53e8b77acb11 | -3.31585 | -59.60621 | 2026-09-19 05:42:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e54c83e1-10c1-3300-9a33-8ff200eedd0a | -3.69155 | -60.61807 | 2026-09-19 05:42:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e572fcd4-722d-383c-8bfc-291f3d2bd31d | -2.90344 | -57.81395 | 2026-09-19 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 34.4 |
| aa5391e6-10b3-33ef-b224-74d628d98ed3 | -1.49371 | -54.97688 | 2026-09-19 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 445b7dc5-661e-37aa-80cc-3610d402c761 | -6.13324 | -59.95137 | 2026-09-19 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a9afdafd-94d5-39e1-8a07-bb8d89dc1346 | -3.1122 | -61.41336 | 2026-09-19 05:42:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README96.md)
