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
| 55089ed3-0cae-3489-b681-75eeacf36b86 | -6.6426 | -53.18015 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 61d6291c-5f74-3a87-abcd-e28ba48a52cd | -10.81413 | -50.51371 | 2026-08-30 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f305a67a-a7a0-3d36-9be0-849aca892a61 | -9.50945 | -65.57816 | 2026-08-30 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3c7aca8-a422-3e8f-b45f-f57f37d1ef83 | -10.49151 | -59.61182 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 603c44d8-8689-35cd-b23c-e82ee4d25ec5 | -6.87429 | -56.57449 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1dd9ef9-888f-3592-890e-bc8c1a8811d0 | -5.48935 | -57.14875 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9b108f7a-439a-3dd2-af2d-e8948ad00932 | -6.84394 | -59.43112 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 990c9496-949f-3e20-aec1-2c15c0ed82ed | -11.29612 | -54.032 | 2026-08-30 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e09f6993-a2c2-3302-b6e5-1a19ab663db3 | -7.41691 | -49.74713 | 2026-08-30 05:18:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| daae6303-1180-331d-a2b1-160da52718f4 | -9.9343 | -60.43589 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bee9ab1-f1d4-313c-9de1-3103d6695deb | -11.0394 | -57.24711 | 2026-08-30 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa9d8e3e-24fd-39d0-814c-8d70daa079ee | -9.38822 | -66.51323 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 186bcd73-4d0c-3f1f-9f52-10319929e109 | -5.85982 | -57.54959 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dd94b1a5-493b-3fb9-879b-f4d9cd521b72 | -6.94607 | -55.70739 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f5f1f5b-e01d-3a11-9297-bc438d0f03f7 | -7.57315 | -61.30595 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 965ec5d4-0885-3a1f-858a-d59cc4936e3b | -9.05055 | -65.41207 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 390eb2ee-8e09-3104-ae45-37934c5d5fe3 | -9.71251 | -60.73931 | 2026-08-30 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52cce28d-24f1-31c4-9b4b-5388467073a0 | -7.25666 | -60.63016 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ba16f3e-7a71-3a44-add9-d42b2177a67e | -6.72174 | -60.01441 | 2026-08-30 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8516d60-935c-3bd0-ba84-55473b8851e1 | -5.75827 | -51.68803 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eed6546c-8014-3f4d-823f-4975ff4efb39 | -6.16261 | -57.79354 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08793c18-455d-3b73-b3ce-9cda6120e686 | -6.87077 | -56.57393 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9587aa39-b4dd-3aa7-99e5-af2ce0bfe500 | -7.51256 | -55.2767 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9afdd9e-15a3-3a3f-beed-808a00f3d60b | -5.48595 | -57.14823 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 228e3f34-26fc-3942-a8bf-fed97ae94582 | -5.88911 | -57.76275 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 13ea467f-b2af-3457-8375-0ef07bd51291 | -6.71014 | -58.56585 | 2026-08-30 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fec1bcb9-8aef-3533-9701-6c7c379943d7 | -8.25362 | -46.51021 | 2026-08-30 05:18:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7294b800-0c1b-370f-a25c-077739d1ccaa | -8.57945 | -66.95227 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9d58e45-fc2c-3cc9-8d0a-45ba04585146 | -11.29445 | -54.04443 | 2026-08-30 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 7b7fd431-665f-37be-ab43-f4e087a0fcdf | -6.95616 | -58.95276 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f8405d7-fdf3-3674-a826-1da6d46d0b92 | -7.91782 | -56.64058 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 954b0012-5c8c-3ee0-a3e0-7dd44db82fde | -5.88078 | -57.7723 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 46ad01ed-ee6d-3308-b659-54e8a741f642 | -11.15864 | -50.58667 | 2026-08-30 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 58bbd592-c971-31d1-afb1-688a3b1d1b80 | -5.48116 | -57.15173 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 10280600-387e-37b9-aeae-07cbc125d940 | -6.15817 | -57.80014 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce973cfb-57e0-306d-b52f-efdaa05f47b4 | -6.71399 | -58.56289 | 2026-08-30 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 79f730b4-777b-3d3e-b382-b2dce5ccc9bf | -6.79973 | -59.60518 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c81d7654-bcef-3d4c-b36e-9c87fda1908d | -6.07681 | -57.88968 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 19ff3056-43af-3c92-9fce-bba5b5fda7a8 | -7.30383 | -60.59352 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ae05de86-4a9a-3c75-b119-9f254f71a41f | -8.64146 | -62.84997 | 2026-08-30 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 992838e5-b426-3e9e-b1b9-67a0c8b0e3b6 | -6.87157 | -56.57295 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c9b5db6-a96e-3799-aaad-e30c5e091cc6 | -7.31556 | -60.60641 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5868e0ed-d6bd-3e55-810c-a4ef782d0070 | -7.46059 | -70.13186 | 2026-08-30 05:18:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a40122f9-4504-3a5f-b118-9ae6dd8a22b7 | -9.66434 | -55.10772 | 2026-08-30 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 8ef5ae3d-0df0-3e27-8413-e3ff05a1d9d5 | -7.24379 | -60.62442 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 508b451d-7773-32eb-b1b5-2a0efac42c1c | -5.49386 | -57.14197 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9cdfe86b-f13b-3e60-bab1-0c124d0af8b0 | -9.16707 | -59.51579 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77784d2c-66ba-3b54-af28-9ac48259abbd | -11.03168 | -57.25016 | 2026-08-30 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c33a4ad-ec3a-386e-a2ba-f24106fbc3fd | -9.16045 | -59.51475 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41a4d5f8-252c-3a19-b34b-59c0dafcc665 | -9.15877 | -59.50383 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0e353d3-fe4d-31e3-a90e-278b46c65323 | -9.7108 | -60.73179 | 2026-08-30 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 288d39b8-7740-36c6-aed9-038389aa4840 | -7.19559 | -59.83533 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6af93e3-db77-32e5-911a-67908f14c182 | -6.15113 | -56.11595 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5188a45-9051-3953-8741-9554f40c296d | -10.74856 | -54.06367 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d90e7ad-9f56-35fe-bed9-ab1cc40875fb | -7.56449 | -61.31605 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fdf55b7-0089-324e-8e03-94984790ef72 | -8.59526 | -54.7661 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af2eb5ca-5de4-36a1-a276-91f072956a1a | -11.16022 | -50.58176 | 2026-08-30 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 310c03de-cc73-3155-b3fa-a5e3c6068bc4 | -10.55235 | -59.61417 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3332b54e-cdbc-351d-a749-d13d41057589 | -11.24376 | -54.01374 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c2f82b69-56c5-38f0-9c9e-74079a850983 | -7.61195 | -57.62152 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d239f197-e2fd-32bc-9721-4d922593ce16 | -7.62271 | -57.61942 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0202ca09-fabb-387b-afa1-8b6ef3944731 | -9.03291 | -68.51112 | 2026-08-30 05:18:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca16b454-6896-3fc2-a384-bf4050230635 | -7.39901 | -55.15613 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3175f9af-b8b9-3ea7-8d5d-97426622a2e3 | -5.88358 | -57.77639 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1af3f365-3486-3b2e-bdd8-2618b0a0e3af | -9.65043 | -58.93889 | 2026-08-30 05:18:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f66dd409-1b37-3363-b42b-1451880fcf66 | -8.93366 | -67.37198 | 2026-08-30 05:18:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 295ec5db-df20-3d12-a787-8eeabfac4155 | -6.03847 | -58.04993 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75867f8b-c403-3819-94d5-3292aa09558b | -7.29877 | -60.60375 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb295b18-a1b0-3f90-ba2e-228092e9cebe | -8.5077 | -55.2952 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e4ac29e-9b90-3d3a-b931-7f76f68008b0 | -7.50901 | -55.32833 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01216844-b007-3fce-94b5-8ed26ffa8402 | -10.49537 | -59.60884 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a223a173-90e4-3aac-9b76-28c922395241 | -9.22421 | -59.76009 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f2c8462-b5f6-3d10-821c-8d587b505f49 | -6.49786 | -53.26035 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c477f00-9864-3467-96c3-48630acac066 | -9.15714 | -59.51423 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88efcb7a-02d2-3370-9b8e-8278190801b5 | -6.25346 | -53.69548 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5d8b8a5-8d5d-3ccc-ac85-8c2046603c89 | -6.024 | -57.83815 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9518ea7f-d8c2-3140-aa2a-de2727905e75 | -6.07961 | -57.89373 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f0887a82-e28e-36ae-9496-ac401df98755 | -11.79328 | -51.04589 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 21.8 |
| b69bef7b-f6db-3c48-909d-ed6e1eb9b66a | -8.60635 | -70.21096 | 2026-08-30 05:18:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cbed16dc-3d94-38de-91e1-7df35e4c2942 | -9.14951 | -61.09194 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c6f57be-bb1f-3d47-a125-b4c508ae0a56 | -9.16526 | -58.31131 | 2026-08-30 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 177a9a80-84cb-32a0-b308-cb513b3b201b | -11.1584 | -51.30089 | 2026-08-30 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 920bd2a2-b198-3e36-bdc9-77ad1d0843a2 | -11.79863 | -51.04661 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| bdc9ce6d-3b1e-3765-8421-34d1535f0611 | -9.8899 | -60.28473 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 491fc7a1-5094-3278-953a-cb628fd52013 | -9.0499 | -65.41596 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 65869a9f-b715-348e-b65a-bd24ec4b5043 | -7.329 | -60.60854 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34cf911a-a9be-3166-b880-02ba6f59e12f | -9.15269 | -59.49931 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fa9abe43-c356-368e-98ff-53da955c45a2 | -6.4268 | -55.52691 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9703336d-a8f7-3870-bc6c-91ce2b9a8d77 | -8.81024 | -67.28857 | 2026-08-30 05:18:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c00daa4c-2f2d-3686-bc06-58484d9fb10c | -7.4522 | -59.93353 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 07357715-cc2a-3c3a-8274-d657325d4c45 | -9.84795 | -60.27088 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 416916e9-b95a-3dee-b320-dcb393665e04 | -11.03524 | -57.22559 | 2026-08-30 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 90c9567b-4d0c-3ee1-a63d-e61285420852 | -6.88605 | -59.40237 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00c9a9cb-48cb-3bc0-afe7-cd906c3be775 | -7.56227 | -61.30805 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92744f3b-0282-37e8-b981-fedffbd5671a | -6.90586 | -58.99094 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5da0f02d-9763-34b8-978b-b5a996edaa38 | -9.15823 | -59.50731 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2df09bed-3b71-3c9c-8be7-f73412998d84 | -11.16401 | -51.29841 | 2026-08-30 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9af6c0ef-f854-3da9-9b3e-c5f69268d1e4 | -6.71292 | -58.56985 | 2026-08-30 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e8ab1ce-d3b4-3f4b-a3b4-57fcb940fe19 | -9.44874 | -66.73618 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 142a39c3-6068-31af-9f4e-17059715b54f | -9.61275 | -55.13116 | 2026-08-30 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README56.md)
