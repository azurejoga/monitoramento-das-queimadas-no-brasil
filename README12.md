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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13b43304-8597-3257-901a-67411b3d2b7f | -12.16039 | -57.13959 | 2026-06-28 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 04630ebd-54a4-384e-a645-b154a4f21daf | -12.08527 | -52.02025 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 54c147cb-0b84-31bb-9f5f-9b63a33a1e5f | -12.18264 | -52.91045 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4cfffc4e-4f32-3ad2-89ff-9b8513d3c901 | -13.4533 | -44.03976 | 2026-06-28 04:14:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80877063-3bd8-372e-994a-b80cedbd6e31 | -12.09218 | -52.01164 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c8a26a11-5494-3807-bfbf-221e8183e5ff | -12.22861 | -56.55478 | 2026-06-28 04:14:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6940f21b-11ad-3bb4-81f2-4a523743269d | -12.08465 | -52.02355 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6292f801-e2e9-38e0-8a58-af41b7d0c751 | -17.70505 | -46.77459 | 2026-06-28 04:14:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1b39798a-6b4c-3d18-9e91-c6dbee6d8966 | -12.19805 | -52.89035 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 517976ed-55d9-3bec-ba9e-3b7a64129bcb | -12.19035 | -52.90039 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 451c5c1b-5916-3764-8c7c-a64d25ffd05c | -11.20836 | -54.29733 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| ab40114c-f239-39cd-8bcd-4267456696d7 | -12.08004 | -52.01923 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 435d9edc-7695-3be4-95fc-b7a220ea2de6 | -12.08986 | -52.02465 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f784aa43-bfd9-33b8-9282-226d588cd3a5 | -12.18557 | -52.89554 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1de0f664-d671-3fd5-af29-329f17d08b6e | -12.27568 | -50.1 | 2026-06-28 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6a51b272-cdbf-39d8-b05e-dc4f4a003c69 | -12.16593 | -57.14827 | 2026-06-28 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 275743aa-0a53-3011-850d-661bae752a7f | -16.04251 | -50.5604 | 2026-06-28 04:14:00 | NOAA-20 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb85a291-917a-37c3-8587-87ed18c12792 | -16.75282 | -45.81638 | 2026-06-28 04:14:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0cf715fc-520a-3882-a795-316140b8b1e0 | -11.21263 | -54.3113 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 2f4fa2ae-b3c8-32d7-99c0-4baa4766b88f | -10.77765 | -54.10598 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0692b303-0821-3e6e-b79d-5bc8d5e3c5af | -12.19254 | -52.88923 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0e5417f8-30b8-3b75-9744-0b868ea6e556 | -10.78464 | -54.10269 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbf3e0bc-7223-39ba-a94d-e89135024574 | -17.30904 | -42.65345 | 2026-06-28 04:14:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 4cda664b-5dbc-3bfe-85f1-e3bf6db10d60 | -12.18295 | -52.87969 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a9ec619a-61a0-305d-8f2c-2169aff1dc41 | -19.49547 | -44.80338 | 2026-06-28 04:14:00 | NOAA-20 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac25c2c2-a83f-3471-97db-5106a235de95 | -12.08837 | -52.00383 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 98cb0ca6-694e-3f5e-acfc-6913c494a086 | -11.52109 | -54.79787 | 2026-06-28 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 452e20cb-344e-38b8-af92-5c4b6aeaaf50 | -12.18888 | -52.90786 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| aa436e4e-0acd-3eb0-ad3b-08f65296f1a5 | -18.95957 | -44.08668 | 2026-06-28 04:14:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6915d51d-fb41-3e5c-947f-2c36439a9642 | -12.19399 | -52.88184 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| edf7739a-1374-3d72-a0b3-c2cd56d463d1 | -12.54239 | -57.187 | 2026-06-28 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e577f3d-948a-3888-b049-d7fe7faf40fc | -12.08714 | -52.01034 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2b6805fa-14ed-3a97-be1a-2f7573402bb8 | -12.18005 | -52.89445 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| add2f351-b828-3351-b3fc-f97cb20192bd | -11.20604 | -53.82347 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a5f8b04f-8d14-3a57-b64c-4453b12f34f7 | -12.08378 | -51.99948 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a787fd1-6047-3e29-9e3f-626f9e8f0739 | -12.09025 | -52.02146 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 80c74563-5588-32df-ab2b-532aca6a9871 | -17.70088 | -46.77802 | 2026-06-28 04:14:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5d3af5e7-a5ed-3def-894f-28b54a9e83bb | -11.21881 | -53.82131 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9890179f-5395-37e4-a299-7cc807ba59d4 | -12.16747 | -57.14113 | 2026-06-28 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7a2c7c2d-92d3-301b-922f-4c939e393713 | -12.19181 | -52.89294 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| eeb98421-3eb3-3f50-9c03-6aeb44024cd9 | -11.21867 | -54.30932 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bea14860-0790-3ce4-923e-a0052fb2b857 | -11.21584 | -53.81958 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 347299fe-584e-385a-979e-d96a1212595c | -12.22998 | -56.54845 | 2026-06-28 04:14:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6115761a-3d61-3817-9040-63ac4f3dee5a | -11.20649 | -54.3101 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| af26b7f0-9f65-3172-b738-11a3bbc01d5c | -12.16194 | -57.13243 | 2026-06-28 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 553e3472-ec33-3c1e-91a3-04f79fe92b43 | -12.2705 | -43.51165 | 2026-06-28 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9d4473ad-5d66-3113-b94b-eaed114d1de4 | -12.17859 | -52.90186 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 227b8cf4-6aff-3c24-b3fb-768bf1d62c43 | -12.18484 | -52.89925 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b0905757-a1e1-32df-ab59-5cebe659e6f2 | -12.08192 | -52.00931 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 884f3144-9e9e-3e98-936f-7929f4ce45aa | -17.30421 | -42.65289 | 2026-06-28 04:14:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 6e9a2501-a230-3fe4-8445-9ff5f68f8d7c | -11.52835 | -54.79425 | 2026-06-28 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 34561527-18de-379a-9a80-730a51412d85 | -10.78372 | -54.10735 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c52aef34-ed46-354b-a7fe-01fb8f798abf | -12.52978 | -43.20673 | 2026-06-28 04:14:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ff26355d-6699-3bc2-87f0-5f04eebe01f6 | -12.52974 | -47.04832 | 2026-06-28 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7deee589-2627-3a35-a09f-313521df9e15 | -12.19513 | -52.90528 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| db4b39d5-6e54-3dda-9973-be69963a8358 | -12.78929 | -54.88869 | 2026-06-28 04:14:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df4a23da-0445-3442-b71f-0a4123519527 | -17.50603 | -44.89521 | 2026-06-28 04:14:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ade354e-35f5-3310-b36c-f9276c2a4bf4 | -12.19586 | -52.90154 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c43f5fc4-b764-32ff-b8fa-a72c3530e5aa | -12.17932 | -52.89814 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a37abca8-fec4-3814-8c4a-b69c14db9c3a | -11.21876 | -54.31253 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 5c8d94ab-765e-3177-92a4-3a3d316f5797 | -12.09111 | -52.01805 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dc7b01b9-4b05-3401-8e08-345cd1066dc1 | -11.20838 | -54.30044 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| c25e56d0-b97b-3f46-8248-18f4a28c4167 | -12.18014 | -57.15116 | 2026-06-28 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ce133ca3-5bde-38b3-b640-4380f3c66db9 | -12.08762 | -52.00727 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| af9a981a-797e-353e-98bd-c36264e748d4 | -12.18775 | -52.88445 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8f312479-a0db-3a6b-a596-8dac1b139e06 | -12.18565 | -57.16006 | 2026-06-28 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 03dcdc0a-09e6-35b9-8486-801f30e1f424 | -11.21451 | -54.30169 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 7a2dff39-3c2e-32b2-afe3-5d48fe0499a0 | -12.0813 | -52.01261 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5771977a-6db8-3acb-8890-a3f4db928810 | -12.26387 | -43.51056 | 2026-06-28 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 18dc975f-2ffa-3265-92a7-614250bdd556 | -17.34727 | -42.62898 | 2026-06-28 04:14:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| d996946e-9ad0-3bd5-8f60-8870fd17abcd | -13.88853 | -47.1728 | 2026-06-28 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b7ec06cc-705e-3b66-85bf-2b983ab75faf | -12.19732 | -52.89407 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fd85cfee-18ac-33ff-af1f-985be04cc35a | -11.21408 | -53.82837 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 1bc83376-23e9-32fe-9f3b-86d0369e4dc7 | -12.18702 | -52.88813 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 35a4501a-3601-3e2a-b690-6d74cc93b221 | -12.18222 | -52.88339 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e1883d20-6e37-3a55-9f57-361a7a40d339 | -11.5258 | -54.78993 | 2026-06-28 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| ed90a3dc-1b7f-3927-8323-c1efff853ebd | -19.33795 | -42.16056 | 2026-06-28 04:14:00 | NOAA-20 | SÃO JOÃO DO ORIENTE | MINAS GERAIS | Brasil | 3162609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d8f6d22f-6865-30f2-8f3c-0c50fe7e2344 | -12.1841 | -52.90298 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 02010052-46b3-364f-bbd7-169d4836099a | -11.21255 | -54.30808 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 621a2647-7e48-3f03-9714-7d569dfe6843 | -12.09089 | -52.01818 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 91505a2f-d70b-3dee-991d-dc6bf55b49be | -12.19687 | -52.86713 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6e786811-4681-3877-a517-106ca54db4a3 | -12.18992 | -52.87339 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d4e674b8-7a6f-3016-9952-71ca6272f565 | -12.1995 | -52.88294 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 27a8bb58-478a-32a7-ac5f-3127f3c5ac76 | -12.19366 | -52.91278 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4fc97e2f-b4c9-33a4-8b67-5cf4a697aab6 | -12.54939 | -57.18879 | 2026-06-28 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7dae30d-9f00-33f6-aa33-8569854762c7 | -12.19064 | -52.8697 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3fd71aa4-602d-3d28-8165-c1556a211c0d | -12.09234 | -52.01149 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 20da8193-1b80-3cd1-9737-f0cc3a6a49e7 | -12.17149 | -57.1569 | 2026-06-28 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c7803e05-7f3d-317a-8b0e-cbf0a3625e3b | -11.21796 | -53.82574 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 23bf54b3-2ba7-3572-bdfc-7134335fc1e6 | -12.26937 | -43.51873 | 2026-06-28 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00f0384a-8e1e-3719-996e-3bbdba946c32 | -12.17458 | -57.14256 | 2026-06-28 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| dff0a4a6-a814-36fd-a39b-f96271c849c1 | -12.08316 | -52.00274 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92f839e0-fd2f-3566-aa60-f8b292da38f3 | -17.34783 | -42.62522 | 2026-06-28 04:14:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| bb221eae-a83f-3b79-8a8e-90567a9ba808 | -15.44026 | -43.66315 | 2026-06-28 04:14:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6b240614-3505-38b0-ba44-d2613834964d | -12.19615 | -52.87081 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2d6795e8-7515-3653-8fdf-3faf606a7437 | -17.50544 | -44.89885 | 2026-06-28 04:14:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff9652af-e607-33a3-8c3a-93995251c2fa | -11.21357 | -54.30645 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| c7a4ce1c-37cd-307e-953c-942b551cf84e | -11.20641 | -54.30689 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 17a819be-8550-37d1-9452-52d093821108 | -17.30365 | -42.65662 | 2026-06-28 04:14:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 0c3f615a-df10-379a-96d6-12b1f017775c | -12.09154 | -52.01491 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README13.md)
