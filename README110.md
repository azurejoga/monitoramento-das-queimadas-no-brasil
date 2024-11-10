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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0b26056-f8f1-3bb2-b944-ff5a2691a842 | -4.11931 | -43.59326 | 2024-11-10 04:38:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a4139c6d-0e83-3d84-b0e1-08cca15fa15b | -2.412 | -50.30557 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c6e6ddf2-669a-3675-b325-5ba56b634edc | -4.62842 | -49.08148 | 2024-11-10 04:38:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf55788a-736e-3c02-817a-2735a40b3a82 | -5.57092 | -43.96847 | 2024-11-10 04:38:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 43133b54-4039-319a-b498-f61036fa3f29 | -3.95263 | -48.1646 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 68589da7-b6f2-3c8d-8efc-05dadceff60d | -3.04628 | -49.54236 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c3619256-3811-32df-b3c7-3c8576dedc22 | -3.10385 | -49.40736 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16f39fc4-598c-3015-a174-802b22e7643d | -3.01717 | -53.26353 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 28b5455f-0f66-3aad-b825-7524e0a9ecf6 | -3.14348 | -48.58018 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b79e2e4-b1ca-33cd-b485-cc491bb3416f | -6.24858 | -43.56508 | 2024-11-10 04:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf34e963-f6c8-33d9-9817-abd6e00cb42c | -3.40774 | -50.32705 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d6f572d-4302-3499-af6c-9c41c134f2fb | -3.63717 | -50.18097 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ead1651-bd92-3acb-bc6f-334d36bd2da2 | -3.54009 | -43.56344 | 2024-11-10 04:38:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c70abccf-f567-38a2-8bfe-841d307f6b01 | -2.91194 | -49.5322 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 416ce512-b743-3def-9b7d-4fc82ac44bd0 | -3.02374 | -51.53118 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c4082db-4d29-3ca6-a98a-65fc26bf59be | -2.4735 | -49.32684 | 2024-11-10 04:38:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3f9965d-07fc-3837-a4a3-635db2c87dbf | -6.22969 | -47.27734 | 2024-11-10 04:38:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ae0aeac-cfc9-38ab-ab60-1b1ba54196a4 | -9.59651 | -36.02823 | 2024-11-10 04:38:00 | NPP-375D | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0398fef5-07fc-3d87-a62f-21d8b3019e33 | -3.52349 | -53.28082 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5774fc4-0a0e-36fa-a951-6bbd07434aea | -4.19745 | -48.39808 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 620d9cff-fa1e-3c15-b362-91a06ed2fbe1 | -4.11184 | -46.10513 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d250e988-6879-3859-b653-16cff3446702 | -2.80056 | -51.4812 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 432da751-0463-3f17-a108-c80bf6214a32 | -2.47129 | -49.36239 | 2024-11-10 04:38:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d45e9339-6e79-3e60-a7a3-075eb1442425 | -2.89347 | -49.38917 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e66bbb3a-def0-3340-a1cd-654f10f418f9 | -4.1131 | -48.5019 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6ffcc45-3416-30b2-ba21-4927cc53f67b | -2.87008 | -49.51484 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 545ff3a0-0f20-319b-8633-daa89912ccbc | -2.11335 | -52.12484 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9685f947-519f-3f2a-926c-6becb4ba5c5f | -4.38579 | -48.5769 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1985f9e6-4134-34b9-8aa8-09663865e35c | -2.69171 | -49.86869 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4948c61c-f7f8-38a0-9a30-c9e9f2c693d2 | -4.07294 | -48.32914 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e92becdf-a404-347a-a9a6-2a7cac74bef3 | -3.14103 | -50.4484 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 74043182-64ed-3271-9569-1302a315be9c | -2.48016 | -53.97706 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 495c6092-365e-3fd9-8703-88a6948399cc | -4.06106 | -50.0161 | 2024-11-10 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a56545b8-bb3c-3147-af31-ee1f58ae7ae0 | -2.4292 | -51.96209 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 406dcf6a-4d63-3e0b-9831-e386f961cf1b | -4.78881 | -48.66114 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b78a503-9075-345c-9ed4-2f54062362e3 | -2.61266 | -48.33807 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91b50b28-fd06-35e5-840e-30f31cdf624d | -3.29841 | -50.13918 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88e06d43-d154-3fa5-99c6-31b9510fcc87 | -2.31662 | -50.57824 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5f3289f4-7f09-3466-9ecb-201e96b83539 | -2.98006 | -50.49124 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0cab8b39-ba7f-3cf6-98ad-4f6d1cbd0659 | -3.58464 | -49.89804 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 095d4b2f-3c2a-3abe-a0d2-448d09c9ec54 | -2.42176 | -53.67294 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 049160bc-a8c9-3801-80b3-ce90f73f96b8 | -3.98701 | -48.16283 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df3d548f-4895-390c-a4ea-f9612fbdc101 | -3.76578 | -50.38305 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cfbfd61-8cc6-3dda-9625-8bf14e12ee4f | -2.65234 | -49.40157 | 2024-11-10 04:38:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bedf8473-fe44-3de0-b10d-a5cc4ae6544b | -3.23561 | -50.28963 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a0f7e9e6-051d-3774-bc79-44e6025ece4b | -3.13331 | -49.11992 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5a9772e-e5cc-3b71-a0ac-a084b34b46d8 | -2.48376 | -49.07522 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e8b7d86-8731-38e0-8ccb-74ad34f2a294 | -5.45368 | -43.26803 | 2024-11-10 04:38:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b52ea968-35c2-3562-b538-709c9d1201a5 | -2.8541 | -47.81569 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f0f47c5-85bb-32f8-b363-c2cd471f27d2 | -2.64782 | -48.63296 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 285c0007-62cc-3937-b0e3-85451ecf0bdd | -3.61325 | -48.92563 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af8e6c3e-f1d4-36db-a0c8-c14972f4b44e | -4.28366 | -48.19112 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7f378b23-3882-3d7b-bb79-85ebf2d61e4f | -3.59127 | -47.34471 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87e8335f-1a21-3b2e-a526-31d5c4111046 | -2.92643 | -51.67328 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 359405ce-7836-3cfa-a5fb-8c1ca5e5cf71 | -3.13576 | -45.16188 | 2024-11-10 04:38:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fae04884-e1b3-3f28-b5e9-ea67ffc86bcb | -1.9597 | -53.06947 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 76c91535-ebde-38f8-aab9-53450fc3aaa6 | -4.76726 | -48.66839 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 812c412d-941a-3361-b3fa-19905edf5389 | -4.09988 | -49.10478 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5330665a-d26e-3caa-9837-26a0d1b6135e | -2.27436 | -50.66498 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9fb6194f-5755-37b9-8f86-744b15e84fb2 | -3.84202 | -49.96725 | 2024-11-10 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 263f4789-31b9-388a-9d97-dd0594dff6c2 | -3.11235 | -50.14408 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f75e25d5-4f9f-3eac-964c-521f6712afe0 | -3.44801 | -51.46979 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb364b18-9834-37a7-86a9-b1d571bc1074 | -4.77348 | -48.91014 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9843a0f1-54f3-30b9-b0da-f5aa6717c737 | -3.96812 | -46.98544 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91c6dd55-afe9-3fe6-ba95-7adc1130ae47 | -4.01343 | -48.29854 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11ea753a-aaec-3704-9642-0d656d067c4f | -4.06875 | -48.22537 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d9620e03-0013-333e-bb3c-33fd2317b510 | -5.97344 | -45.36139 | 2024-11-10 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 414fa222-a7f1-3054-b998-f3cefb2d7949 | -2.65039 | -49.24009 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 546cd10e-bd69-3d62-a384-e3d26aa11fac | -3.95936 | -48.18702 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 853111da-2f52-3200-a375-ec0d4ce8a6e1 | -4.63872 | -46.02827 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e570de9-0932-3da1-aafd-96b78da4efd6 | -6.26828 | -44.5439 | 2024-11-10 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4d8bbbcd-f421-3da8-9c1e-cc8e51f70b10 | -4.18161 | -50.42557 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6045c84e-dc7f-386d-989f-aec21afd5615 | -3.97995 | -48.40329 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f4be225-bab1-3b09-9bb4-6f3a9dcd1bf0 | -4.61015 | -48.63637 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a184822-2d22-3c10-9fe2-58d08970af6a | -2.18685 | -53.64484 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 366c583a-d619-33e1-9b2e-a3e7ce081833 | -2.87697 | -49.37245 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3610c162-42fa-377f-830b-7fa244fb78ba | -4.70958 | -48.79748 | 2024-11-10 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f52d8d5-0954-38a2-9b9e-3fa53dd3be2c | -2.83752 | -49.42724 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81f92823-ac4b-38ff-af81-80969437895f | -2.28645 | -50.67862 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e70a992-c115-3c50-b058-0b9197701a02 | -2.99105 | -49.5229 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9979cbf-fec5-3704-b044-4fb048b12b3e | -3.04661 | -48.03451 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91013cdd-efbb-3485-a802-37750f8529bc | -2.87702 | -50.41502 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8fec48f3-5c4d-3397-9bc4-589f166a4179 | -3.13669 | -50.36464 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7295b932-bd96-35ee-b923-2f964ac686a2 | -2.22155 | -50.76779 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f1c03051-e5a9-301a-9c44-cfccca98b5a6 | -3.03451 | -51.53286 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbce08e6-429f-3daf-8795-93541717f88a | -4.09329 | -49.125 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1893117-207a-329b-82e1-a49ede40ce55 | -4.72994 | -50.38111 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94e9e505-3185-3069-a881-a5bb46c90af4 | -2.67971 | -51.8177 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 00da44f7-461a-3746-9027-e5678a3808fd | -3.08549 | -49.56605 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2183b515-4198-3f43-bacc-c04a2678d49d | -3.25091 | -46.4786 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4738fecb-54fb-3929-a90c-740925c94099 | -2.64836 | -48.62952 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcb58202-83a8-34be-a296-b79a8363cad1 | -2.53923 | -56.7516 | 2024-11-10 04:38:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 949f06d7-f1db-365d-994f-8bc43337642a | -5.06301 | -50.00694 | 2024-11-10 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 8026492b-7244-3484-9281-f425862b8b34 | -4.92766 | -47.64028 | 2024-11-10 04:38:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95a7ad53-449c-33c6-982e-ec50be1ced56 | -2.72252 | -51.71202 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e9a2a05-1eff-345a-87fb-71c5b9889821 | -3.62282 | -49.61479 | 2024-11-10 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2e7d41c5-2b9a-3c3a-b864-264c9ce7da06 | -2.84031 | -46.63174 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66e72cc9-4e5d-324f-99d0-4d5898d28e48 | -5.51554 | -49.20039 | 2024-11-10 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0e0d9a8-4e3e-3382-97ce-231b85b11620 | -4.85886 | -43.966 | 2024-11-10 04:38:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6b91d800-f022-348c-bafb-2d9b05acb450 | -3.11575 | -50.1446 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README111.md)
