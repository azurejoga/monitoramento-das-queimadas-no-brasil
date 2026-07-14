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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c15b1ea4-4100-34e8-ba5f-459b6083a246 | -10.0961 | -47.98246 | 2026-07-14 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51a07a31-1015-3511-9469-72f2639e8d84 | -11.57618 | -48.40177 | 2026-07-14 04:14:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f6b3503-89b3-36a7-8fe1-d2fd3db4005b | -11.767 | -42.0564 | 2026-07-14 04:14:00 | NOAA-20 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7dcc97cc-77c3-3a9e-ad56-f20a81ce2b2c | -12.45548 | -46.51646 | 2026-07-14 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6e27c404-0abe-3fc3-a8cb-7a0416283824 | -16.56656 | -49.89916 | 2026-07-14 04:14:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 590182ce-e536-3381-ab52-2cdbb6f61426 | -9.18009 | -50.88481 | 2026-07-14 04:14:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe4ecee9-3399-371a-8eef-9e35c1765180 | -10.75382 | -42.10817 | 2026-07-14 04:14:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0d879ba4-4e27-34c7-ad7f-e02c7b1b5e09 | -11.49345 | -47.61987 | 2026-07-14 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9861963a-94c1-3bb7-8940-1f118afb8b73 | -18.77719 | -52.4085 | 2026-07-14 04:17:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7705802f-cf02-3db5-9537-a62e0b2791de | -18.78192 | -52.40945 | 2026-07-14 04:17:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f50f4e00-026a-3a6a-942d-641bb92d8ede | -28.626 | -56.00495 | 2026-07-14 04:17:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 08d90a4e-f7a9-3d6e-9d2a-fae24e4ef97a | -18.17246 | -46.90709 | 2026-07-14 04:17:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e765c21-f114-361e-acf8-896d4913c45a | -18.17107 | -46.91519 | 2026-07-14 04:17:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a89a8d7-1cc0-384a-8cef-40d193bcc479 | -18.17594 | -46.92868 | 2026-07-14 04:17:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5227ed0-b5e6-3c98-8b88-769f228b9298 | -18.18012 | -46.92523 | 2026-07-14 04:17:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d9ae45ae-edac-3ff7-89f2-0463a7fbf356 | -19.71679 | -50.20692 | 2026-07-14 04:17:00 | NOAA-20 | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 31e2d943-5e5e-3af3-b771-d7158a31f700 | -21.2789 | -56.03574 | 2026-07-14 04:17:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| aa338690-0cab-3c23-80f2-7856b3d30817 | -22.70175 | -43.36087 | 2026-07-14 04:17:00 | NOAA-20 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9ca917d2-0bb0-3942-aed9-9cc6c8d75d96 | -20.70336 | -50.51613 | 2026-07-14 04:17:00 | NOAA-20 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 71efb37f-7da8-3f79-a5a0-1a0b1d066d5e | -20.65028 | -48.67965 | 2026-07-14 04:17:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b856ea0f-772b-3202-bfd5-9a4e4d21633d | -18.17385 | -46.91991 | 2026-07-14 04:17:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a162085b-4b5b-3862-814f-76e15eaeaef6 | -22.24167 | -52.88145 | 2026-07-14 04:17:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9ee0cfdf-8b7a-37b9-ba83-f3c9c56c04cd | -22.77282 | -43.75861 | 2026-07-14 04:17:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 687dcc6b-72f5-3115-8285-650931ead65f | -19.26562 | -46.51226 | 2026-07-14 04:17:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a8076a01-b519-3fa1-8e20-ea5878fac6cb | -18.7877 | -52.40515 | 2026-07-14 04:17:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 03da3537-bf76-3321-a5b9-35d7542e0925 | -18.17315 | -46.92399 | 2026-07-14 04:17:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3374c006-4d16-3dca-8e90-cf9921f908be | -18.17733 | -46.92053 | 2026-07-14 04:17:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1f05f2a2-570e-3084-81e4-f35da98f6a60 | -19.71607 | -50.21066 | 2026-07-14 04:17:00 | NOAA-20 | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 559cd437-25bd-37ca-893f-460f64ba6efc | -20.6514 | -48.67701 | 2026-07-14 04:17:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6e7cf38c-0150-32ea-ba72-e1fa8363fc33 | -18.77825 | -52.40326 | 2026-07-14 04:17:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3fd51139-98cb-3108-a01a-6fee53b5e061 | -18.16479 | -46.9099 | 2026-07-14 04:17:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8dbd35c7-8d55-36a0-ae20-2a8592cbcc85 | -22.7908 | -49.35312 | 2026-07-14 04:17:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c6974e0e-90e4-3f98-b364-3253f557316e | -19.13766 | -43.52938 | 2026-07-14 04:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af71b0ae-e453-3a7c-92fd-47cdf34a0c7f | -21.51039 | -45.40705 | 2026-07-14 04:17:00 | NOAA-20 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a0d3b46e-183b-3737-9a9e-9e07d2358491 | -20.70264 | -50.51992 | 2026-07-14 04:17:00 | NOAA-20 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 248ce50f-bd3d-3061-81cb-0f97f48a6359 | -18.16828 | -46.9105 | 2026-07-14 04:17:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 018835ff-ad9c-3b03-b0ff-87efc7322cd0 | -18.52651 | -47.23455 | 2026-07-14 04:17:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d62ca742-c20b-37af-bfeb-4be70f7f2a0e | -20.65111 | -48.67514 | 2026-07-14 04:17:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3019c8ec-98ad-3ed5-8bb2-7ec73b35fa22 | -18.18361 | -46.92582 | 2026-07-14 04:17:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f76803cb-7620-3f25-a1ba-bc2233587a9a | -23.13856 | -48.66961 | 2026-07-14 04:17:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d054ca0-b426-3231-af55-dfa60709ac10 | -18.16758 | -46.91456 | 2026-07-14 04:17:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ff5e8788-564f-3747-b0c0-51e3af7b03a2 | -18.21177 | -47.95321 | 2026-07-14 04:17:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce2cc141-42bb-3132-8914-fe00ec30f98a | -22.24219 | -52.87902 | 2026-07-14 04:17:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1d2ef335-7761-3b49-8f74-72b45de6969b | -20.48541 | -45.67269 | 2026-07-14 04:17:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 31b77b72-cad8-307a-a3bf-617fb7c85048 | -18.16897 | -46.90649 | 2026-07-14 04:17:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 146aec9d-0d30-3843-bc70-e6a2dfdca013 | -20.48601 | -45.66898 | 2026-07-14 04:17:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c813b8fa-c32d-3a7b-a1ab-a518328b5262 | -16.89203 | -49.06938 | 2026-07-14 04:17:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0cf9b6b7-9b87-32fd-ac87-8aca1e2e55bf | -18.1641 | -46.91393 | 2026-07-14 04:17:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0d6e9c7f-61a1-3b7d-9e73-8ab99b1fe7dc | -19.13822 | -43.52571 | 2026-07-14 04:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b0bd7ed6-9afe-3e49-8ac1-dd79eba09b20 | -19.26837 | -46.51679 | 2026-07-14 04:17:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4f00cb9-60e5-313c-9dd1-616070d53234 | -20.65393 | -48.68042 | 2026-07-14 04:17:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6cd4a660-8252-3e53-b2f7-4ac682c660a1 | -18.17036 | -46.91929 | 2026-07-14 04:17:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf0aa661-79db-320a-88aa-924c33cc4b3e | -20.65475 | -48.67591 | 2026-07-14 04:17:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e65adb97-136a-3b5b-90b4-5eb2bc8e58b4 | -18.78298 | -52.40419 | 2026-07-14 04:17:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ec9bffa7-f3ab-3d22-8faa-558d0d069e8b | -21.27332 | -56.03425 | 2026-07-14 04:17:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93f5e649-f286-3d63-a81d-d8cfecd3da50 | -18.17664 | -46.92461 | 2026-07-14 04:17:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b2d0bb10-b946-306f-bddc-a12065bc5750 | -18.17942 | -46.92932 | 2026-07-14 04:17:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e6ebccd1-9f0f-36f1-ad23-fc7607ff7a3d | -18.17594 | -46.90771 | 2026-07-14 04:17:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d13d3673-5093-349f-90a8-7e3fe2e05bff | -1.57298 | -47.75406 | 2026-07-14 04:55:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2349365-6d69-3ef1-9d4d-ac0e3b15d828 | -0.08831 | -51.27835 | 2026-07-14 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4969c8ce-14bd-3f92-bbeb-096178407148 | 0.89153 | -59.69227 | 2026-07-14 04:55:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f381609e-ce8f-3e5b-a510-9bb804a0e859 | -0.08776 | -51.28192 | 2026-07-14 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84167415-04f2-3062-ab7d-f39ad4a30e4c | -9.80453 | -48.91703 | 2026-07-14 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ef3c5d6-f748-3bd2-a614-240e8dd71a5f | -9.80397 | -48.92108 | 2026-07-14 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8565cd3d-41fc-31d6-a29d-02ef44f5dff0 | -7.76531 | -45.03018 | 2026-07-14 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 513c28ea-96e2-3f08-ae15-709dff7ca4bc | -7.77652 | -45.5049 | 2026-07-14 04:57:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9929422f-e9a4-3cc6-aafc-4ab8f59d0da3 | -8.17967 | -49.3393 | 2026-07-14 04:57:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 468271d4-2cc5-3bc7-8686-55923afc1ab0 | -8.73507 | -48.32834 | 2026-07-14 04:57:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 612dfd75-ca2e-31d6-b40e-d44073298522 | -8.89071 | -48.5037 | 2026-07-14 04:57:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0169433-cee3-3545-abbc-81c103369831 | -7.75942 | -45.03287 | 2026-07-14 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 09570d80-7e51-38bc-aa9c-c29633449866 | -3.15269 | -48.57893 | 2026-07-14 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e093785f-cfa8-309b-bf43-3afa9ee724f6 | -8.83334 | -48.33229 | 2026-07-14 04:57:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2a7b1b5-a25b-3969-8226-c8e69d03d374 | -7.78179 | -45.50558 | 2026-07-14 04:57:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3ea8beef-b31c-3166-9fac-5eb770d144e0 | -6.54779 | -55.15295 | 2026-07-14 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aea30d0b-eca1-3e0e-8d43-7377644ce585 | -7.75989 | -45.02937 | 2026-07-14 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8ee5c4e0-5b08-383e-aa85-5181f8f631f7 | -7.75446 | -45.02856 | 2026-07-14 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4a89af67-b8f1-3a03-9bdd-180688e0a627 | -6.48203 | -42.22633 | 2026-07-14 04:57:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 9a99903b-172b-3a52-ae63-7d3f8ed4fd4a | -8.88636 | -48.50302 | 2026-07-14 04:57:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7f789a3-d72d-312d-b370-4115d6b5baca | -5.93857 | -46.35253 | 2026-07-14 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3f391b89-127b-38f2-9fef-ec16efa3de29 | -5.82727 | -43.47465 | 2026-07-14 04:57:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 25cc92a3-ae9d-3e59-b3a9-c1c938c5fca3 | -5.91424 | -43.62011 | 2026-07-14 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d326cc8e-508a-3f8c-b537-9253d56999cc | -6.48692 | -42.22266 | 2026-07-14 04:57:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 471da2e1-fbde-39b6-aa3b-6f3217b654ae | -7.01612 | -45.41963 | 2026-07-14 04:57:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 287ae62f-5a33-33c8-b94c-0c16bb21f6f0 | -3.10363 | -52.21321 | 2026-07-14 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0c79b58-9e06-3b75-92ad-15e08205f676 | -3.82012 | -53.73127 | 2026-07-14 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a5c087c-3ff0-3008-bbf4-3a488896df0a | -2.80497 | -48.59451 | 2026-07-14 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 85260bb2-ae0d-3e9a-a60e-8cadc719c454 | -9.69823 | -47.70135 | 2026-07-14 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2bcd8df-5950-37ba-bc6c-3c6293281f81 | -5.83253 | -43.47987 | 2026-07-14 04:57:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc65551a-9097-3183-a70e-652ed56166b2 | -7.01139 | -45.41825 | 2026-07-14 04:57:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| df142e92-5d95-3a0f-9a21-b5f8887f5eab | -9.18438 | -50.88393 | 2026-07-14 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7f2fa4e-d17a-36ec-9006-1dda46925fcd | -6.49546 | -42.22311 | 2026-07-14 04:57:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| aa6ab393-aa4f-3b24-91d1-345b4969739b | -7.01664 | -45.4189 | 2026-07-14 04:57:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 52497551-f817-3cdf-8fa3-d8c9685c0f04 | -5.91368 | -43.62419 | 2026-07-14 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5f8409e6-a3a8-34e2-804e-86989fa5c09d | -9.10759 | -49.65474 | 2026-07-14 04:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41029622-a56c-384a-a875-ffc95eb7d104 | -7.01132 | -45.41579 | 2026-07-14 04:57:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4a9180ef-d4a0-34e6-b870-94ceb4a82d00 | -3.15615 | -48.58295 | 2026-07-14 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7747460c-d60f-39ee-88a1-fffc1b798ff0 | -7.77026 | -45.03447 | 2026-07-14 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79693785-48ca-3aea-b3c6-c021d31f7dfc | -5.8267 | -43.47886 | 2026-07-14 04:57:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 76ca40d3-921d-3e41-b9d1-77977571bcae | -9.10707 | -49.65834 | 2026-07-14 04:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 052a0ff7-22b0-3997-a7b8-ead4470767c8 | -5.82612 | -43.48306 | 2026-07-14 04:57:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README6.md)
