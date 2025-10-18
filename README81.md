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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be8328c8-e68c-3c66-97b5-e6f8c95c035d | -10.24033 | -44.06731 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df0e75af-8e07-3490-89b6-454ae096b66c | -10.80868 | -43.93087 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24de91e2-0f6b-3eae-891d-d377a27ff21f | -12.64968 | -54.77187 | 2025-10-18 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e35362d-aa59-3bdb-a62e-d9a5993d0e0b | -15.04758 | -48.73849 | 2025-10-18 04:51:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad20407f-5628-3758-a889-fc59c0e07460 | -11.60979 | -44.07937 | 2025-10-18 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| da4cac67-8891-3343-bf7d-8901d04dc75a | -12.95194 | -62.18429 | 2025-10-18 04:51:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e6c1f64-704c-347a-a828-5e57419b983c | -11.60389 | -44.08222 | 2025-10-18 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52f898da-1f12-3b14-b8d3-848206ca62d5 | -14.93315 | -46.70835 | 2025-10-18 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 96f808d5-9c7f-3ec9-825c-9b360a1130c5 | -10.53415 | -44.51305 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8118a390-14a0-3143-ad38-215a424c2600 | -10.95096 | -49.7706 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7771d371-c5ec-3722-94e5-cf1f6132abf5 | -12.65634 | -54.77298 | 2025-10-18 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 396470b5-7595-3838-91ad-e10753034ab2 | -10.97771 | -47.93003 | 2025-10-18 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e004b8a-789d-3cac-8182-2bea10d40e9e | -14.90668 | -52.39804 | 2025-10-18 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e10b7658-6aeb-30b2-9369-4b3587702d68 | -11.20234 | -47.83386 | 2025-10-18 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf2e780c-9583-3cec-8420-c6a58192e81c | -14.9108 | -46.73194 | 2025-10-18 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5b03d70c-0b65-3761-892c-7785938b0c7a | -14.74184 | -48.18643 | 2025-10-18 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 087e573f-68c9-3414-af9c-bdd091547c2c | -15.5538 | -42.3472 | 2025-10-18 04:51:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69210c99-cee9-3901-b4c3-093ca5cdac90 | -10.68323 | -44.56216 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f62aec17-470b-3abd-96c1-c77d30cca0cc | -10.96202 | -45.47527 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 92b6031e-a1d9-3ae1-9658-c4029b8d1bc7 | -10.95315 | -45.4497 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b99e53ab-d539-3118-b072-82bf19773ebc | -11.19242 | -51.96418 | 2025-10-18 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7faf3d0a-bbef-3a6e-b275-c4ac706e5fc7 | -13.5097 | -47.99475 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5c9eb11-dc29-35c6-9dbf-eb0762e6bc6b | -9.85387 | -51.3993 | 2025-10-18 04:51:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fae9b07-2766-333b-aba9-1d306869dc4c | -15.79077 | -43.6536 | 2025-10-18 04:51:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04a42e3a-0642-3553-b255-2a478c443457 | -10.10707 | -44.55733 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 625c1c2d-d64b-393e-8659-d0b7464c890d | -10.46972 | -55.59092 | 2025-10-18 04:51:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d3f544a-be63-3146-9547-56a2ede9cc5c | -10.53873 | -55.25571 | 2025-10-18 04:51:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5a694c5-38a1-3c8c-abce-26cc53e01951 | -12.17072 | -45.05489 | 2025-10-18 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4cc9e5b6-f8c1-37c7-8c3c-bb8a5f71477a | -10.69927 | -44.56101 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 677fef6e-71dd-3b2f-874d-ac6e2f278631 | -11.81792 | -57.94588 | 2025-10-18 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2721641a-20c7-3ac8-b7b2-d92120fecec5 | -10.14782 | -44.52721 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c7f7c861-9573-3484-9e54-3e9151353ddb | -11.48892 | -44.23391 | 2025-10-18 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cd7aca2-01c0-3ff5-9d2c-f07298fefbb9 | -14.54499 | -49.28061 | 2025-10-18 04:51:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4fc9f2bc-dc37-32ea-bc0e-930a732b5dae | -10.163 | -44.53197 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cc4dfeea-5156-39a8-943f-4dc1bfdfe7df | -12.98625 | -48.45972 | 2025-10-18 04:51:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| edf76113-e7f4-3bf8-a8b4-b78744a08c4c | -13.76225 | -48.23664 | 2025-10-18 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f957733b-a6cf-3d6a-81c4-db391e7c3d6f | -9.53598 | -62.9635 | 2025-10-18 04:51:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ce9c6bc-efa0-3488-9349-f79b2aadff64 | -10.29256 | -44.02656 | 2025-10-18 04:51:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8ccf90f-01d1-3068-9d9c-0a7d8f3ee9c6 | -11.13576 | -45.07533 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53e2e5d5-2dbb-39ac-9a46-fbeb45afc3d8 | -13.77433 | -48.24293 | 2025-10-18 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bae496c9-a8e2-3560-bba4-25d3ece8a655 | -13.22405 | -43.98519 | 2025-10-18 04:51:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 457032f6-909c-33e0-a18b-5548ca798e1e | -10.49942 | -43.45475 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 957d4b01-92a0-3e60-9665-ae321bd350ff | -10.13571 | -44.53922 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 086b4d39-face-33b2-b3d0-977e079af612 | -11.36228 | -44.30618 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c97361d6-eecd-327c-bab6-4eadc3c95692 | -11.37195 | -49.37544 | 2025-10-18 04:51:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ce1b6b9-c71d-3b96-b842-f5857b9e5bf8 | -10.49383 | -43.45395 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22e2a6cf-b1fe-3947-9a2f-544cd0d469ce | -13.43809 | -47.98798 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a097a8a9-5a29-36bd-a948-316de71e9d81 | -12.16957 | -45.08701 | 2025-10-18 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c735a7ff-8357-38ba-98c4-2c36c123d58d | -11.47828 | -44.01127 | 2025-10-18 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c5e19da-8a6a-3994-b3d1-c69d116a3a18 | -10.51695 | -43.40635 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de90fbb2-2e09-3b54-bf49-f8282a531e5f | -12.48624 | -45.46989 | 2025-10-18 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee173939-beac-3f85-a6ea-8961ef06b71e | -9.78136 | -57.41165 | 2025-10-18 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a09e1d84-d512-3021-9807-1295446317f5 | -12.80164 | -48.65334 | 2025-10-18 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a52d14c0-898c-3d60-b765-c8a0687f91ad | -11.48849 | -44.23735 | 2025-10-18 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b3e1711-5615-39cb-9388-9ad1e4e3ddfd | -16.64657 | -52.52818 | 2025-10-18 04:51:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f031c38b-a072-30c5-b609-44339d1d072d | -10.23722 | -44.89709 | 2025-10-18 04:51:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 491bdfe5-13a2-3bb4-a577-0dd48ceeb436 | -12.9143 | -48.58759 | 2025-10-18 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d7a0b60-7e3a-35e3-a333-c90053e53031 | -14.42972 | -52.89936 | 2025-10-18 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9e77e4d-2739-38e5-9a23-22905030f684 | -11.54002 | -49.9239 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64cdbf06-bccf-3b50-8517-90e153ad4b5c | -10.10628 | -44.56348 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f3fdb14-9776-3d3b-a985-e62c7fcee670 | -11.61023 | -44.07582 | 2025-10-18 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 15d921f4-f0d1-3b3e-a646-5a95c6789102 | -9.9906 | -48.55037 | 2025-10-18 04:51:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bf209c51-a5b5-3807-8347-fc6327844861 | -10.16695 | -44.54195 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84c9ddf1-2c67-36c2-8e5c-0852dadd9c49 | -13.50917 | -47.99877 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9154f5b-54fe-3c33-9091-b85a24535c3d | -12.16712 | -45.0843 | 2025-10-18 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1ea45dd6-2ec0-3c46-86cf-e3eab4736554 | -11.51566 | -44.06681 | 2025-10-18 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1e07f24-e3ec-3dda-ad3e-ee76ee9b67bf | -12.30158 | -47.26434 | 2025-10-18 04:51:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 209703b8-5188-3dbc-acbb-89e9ed3da7b6 | -10.75502 | -47.88948 | 2025-10-18 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1fb12e65-fba6-3404-9714-dd949def0ae5 | -11.94409 | -44.24347 | 2025-10-18 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| de0ea034-a0f6-3963-ad6f-15701e13f0b1 | -13.43007 | -47.98258 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0da0d31-8548-386c-91b7-bc1d6ff9821c | -11.35693 | -44.30548 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 83871bcd-ce5f-3fd3-9acd-baa48423f81e | -14.86104 | -52.44563 | 2025-10-18 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6edb1e73-b017-3e78-838f-4a29471c4121 | -11.57308 | -44.66362 | 2025-10-18 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ef31b49-98bf-3f67-9952-a12eca700994 | -10.42733 | -47.73717 | 2025-10-18 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70cac640-7816-326a-9ed8-7c7a2e73e3e9 | -9.48505 | -54.50323 | 2025-10-18 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ea47dd9-1716-37a3-bf7f-6ee8b1e7cb0f | -12.78821 | -48.63005 | 2025-10-18 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 068ebc4a-d022-3b9b-9fc7-b832bcdc490a | -10.42517 | -45.01672 | 2025-10-18 04:51:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 25cfcc9f-f0a2-3f2e-a9d7-e7d6da0d2dd2 | -7.49373 | -63.51849 | 2025-10-18 04:51:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25cc2903-065d-3c1f-adb2-39321f912e8b | -10.23555 | -44.06235 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d0b99c7-74f8-3c8d-a478-f0c21eb06c85 | -14.86161 | -52.44185 | 2025-10-18 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98b48399-6a2b-314a-b25f-6c2d4d7db1b4 | -10.23988 | -44.07079 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a2b5868-0ce5-3026-9d4f-6f788f93f27e | -10.75558 | -47.88546 | 2025-10-18 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3cce7081-26b6-3519-ad2c-acb61695b6c9 | -10.53458 | -44.50983 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 77aba426-8d4e-3e31-b104-ce3aabbe9993 | -12.46116 | -45.46639 | 2025-10-18 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0b430ab8-3e68-3978-800c-3578963873ac | -14.13016 | -44.71052 | 2025-10-18 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c23b5ea-ca79-3a01-9c68-9cd555491ff5 | -10.26173 | -44.07014 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0ace8574-3f50-3fb6-aa56-9a8a8f043f64 | -11.60844 | -44.09005 | 2025-10-18 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ee91afe9-27e6-3f28-9443-d740dc91683a | -10.14221 | -44.52981 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e952e808-ca2e-3ec5-854e-93986589a117 | -9.32272 | -56.27078 | 2025-10-18 04:51:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7d137a5-228e-3d06-a53c-57e2ae789e91 | -10.50596 | -43.44802 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 664957e1-5416-3b6e-844d-70598a52b813 | -10.95368 | -45.46247 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9fba1e9e-3708-3b52-8d22-3182ead00da4 | -14.54945 | -49.27779 | 2025-10-18 04:51:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d4b02ff-3979-3dd1-972d-53a72036a205 | -12.15421 | -45.08482 | 2025-10-18 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6fc0aa1c-9da6-374a-8538-957422ab793c | -12.17346 | -45.07517 | 2025-10-18 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e99adfa6-2332-3a94-921c-7230f74df9b3 | -13.46296 | -43.76458 | 2025-10-18 04:51:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f4c5cf4-e8e7-358f-8b79-4c2da06a35fb | -12.16083 | -45.09309 | 2025-10-18 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf8fdc60-bd84-39ff-9ac2-30bd47a51eb0 | -10.81182 | -54.61612 | 2025-10-18 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 34a6fb95-c025-320c-83f1-45748f6a133b | -10.47845 | -47.73718 | 2025-10-18 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4010ab8-8d13-3505-a2dc-3d7a79bc62bd | -11.47193 | -44.01777 | 2025-10-18 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5192247-e0fe-3146-9a04-c8c6bb2eb94c | -11.73511 | -59.31505 | 2025-10-18 04:51:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README82.md)
