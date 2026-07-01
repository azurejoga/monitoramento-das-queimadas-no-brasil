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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8197302a-b083-3d46-9eaf-92c01df09d56 | -10.6596 | -54.5372 | 2026-07-01 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| f67d7663-b7c3-3a51-8ad1-4d4d6567c1b9 | -10.6787 | -54.5153 | 2026-07-01 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 0fbf2e67-d561-3ab3-acf3-0b82fc5c6a7d | -8.5933 | -48.0069 | 2026-07-01 03:30:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 9cdbc936-deae-3ccb-aada-822f7fd0027d | -10.6598 | -54.5169 | 2026-07-01 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| a6e2e276-3c67-3c0a-8d24-e16bb1576481 | -12.7562 | -44.4724 | 2026-07-01 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 289.7 |
| d18d7d95-f04c-37c8-9152-a8be105dcb48 | -11.4338 | -56.0509 | 2026-07-01 03:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 158.0 |
| 5d7fc261-a8ee-3175-9e7c-7487f7bbd049 | -11.4147 | -56.0726 | 2026-07-01 03:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| d1b6c557-8a93-3de7-91a3-ae6414eba334 | -10.6784 | -54.5356 | 2026-07-01 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| cc41c11a-46d5-3272-9d4c-e3e040b1c45b | -12.8548 | -44.3625 | 2026-07-01 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 77ccc526-8229-3251-9feb-8fdaea0c3893 | -12.8354 | -44.3657 | 2026-07-01 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 205.8 |
| 7b1d8a49-ff25-33ed-ad7c-86ca74ed3ce8 | -12.7557 | -44.4959 | 2026-07-01 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 437.4 |
| 45e8d433-9335-3e4d-b70f-e573c69674bb | -10.9401 | -43.0355 | 2026-07-01 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| be10d427-2dd3-30d6-afd1-5774faccfab2 | -10.9397 | -43.0593 | 2026-07-01 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 81571231-f321-38c1-a6ab-5dcf5ccbc3ff | -10.9209 | -43.0384 | 2026-07-01 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.1 |
| abb6e5d8-3739-3c56-a0ae-29c640db57d1 | -12.8552 | -44.3389 | 2026-07-01 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 274.2 |
| fcacc9c2-7b88-3c43-8dbc-1dd6261cbe3a | -10.6787 | -54.5153 | 2026-07-01 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 4d4b1383-9fae-36d3-ac52-b554ff20db99 | -12.7751 | -44.4927 | 2026-07-01 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 814.3 |
| 62a44df7-2307-3964-b7c2-a9ae2dc55b27 | -12.8359 | -44.3422 | 2026-07-01 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 565.3 |
| 77adc2e7-f9ab-3d0a-a0c3-1973fc19c432 | -12.8363 | -44.3186 | 2026-07-01 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 3c3a44f7-7961-3773-acdb-cda3fc05b1f1 | -10.9205 | -43.0622 | 2026-07-01 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 89062488-03e4-3227-a1fd-bffb25e987e7 | -11.4336 | -56.0711 | 2026-07-01 03:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 215.4 |
| 109926b2-95cd-31f9-b4cc-212501605af6 | -10.6596 | -54.5372 | 2026-07-01 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| f13db80f-f021-3541-8105-25ae30da83d8 | -11.5528 | -47.4546 | 2026-07-01 03:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 9fc56a0c-9885-3895-bba6-c8a7115ba793 | -12.7755 | -44.4693 | 2026-07-01 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 521.6 |
| fa53e354-b507-3a02-a5a2-d5c8cefe33fb | -12.8165 | -44.3454 | 2026-07-01 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| f8afada0-ffaa-37c3-ba63-12d59926c4f0 | -11.4149 | -56.0525 | 2026-07-01 03:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 162b4344-2b2d-324d-b500-5874871cb6d5 | -11.4149 | -56.0525 | 2026-07-01 03:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| ed326f5e-0187-32a7-9a10-b019ec04dc33 | -11.4336 | -56.0711 | 2026-07-01 03:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 101.2 |
| e18e746d-9644-3cbb-a711-e4ea31b6821d | -11.4147 | -56.0726 | 2026-07-01 03:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 498acd6d-9060-38f7-a6d5-fb470248bb36 | -10.6598 | -54.5169 | 2026-07-01 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 59556040-81e9-376b-bb7d-570685192cd0 | -12.8354 | -44.3657 | 2026-07-01 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 246.9 |
| 464a3310-b53d-383d-a296-ead0830dda50 | -10.9209 | -43.0384 | 2026-07-01 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 87661826-1334-368b-b6b5-2113397804cb | -10.6784 | -54.5356 | 2026-07-01 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| e10dffd1-20cc-347d-b00f-23873a619bdc | -10.9205 | -43.0622 | 2026-07-01 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 167.0 |
| c994c1cc-968d-3ab9-bd5e-64b62f5ff83f | -12.8552 | -44.3389 | 2026-07-01 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 253.3 |
| bdf98249-b69d-39e6-a6d8-0329ae307e03 | -12.7562 | -44.4724 | 2026-07-01 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 374.7 |
| d9aaf5da-af38-3f7c-91b2-53734f55bbe0 | -10.6596 | -54.5372 | 2026-07-01 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 3e6078dd-5a9d-3c8a-9bfa-a4da2846de5b | -10.9401 | -43.0355 | 2026-07-01 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 506d70ba-7baf-32fe-b9bc-582b3070c752 | -11.4338 | -56.0509 | 2026-07-01 03:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 102.6 |
| ff017d0d-2da9-381d-8521-233dbb5fe2c8 | -12.7557 | -44.4959 | 2026-07-01 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 384.7 |
| 1d8d8de7-591a-3d80-8f6c-7f59d487097e | -10.9397 | -43.0593 | 2026-07-01 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| f86543cd-17e4-32a3-b5c6-3d1971375b25 | -12.8165 | -44.3454 | 2026-07-01 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| e111f1dc-547e-3bcd-9715-b4a0d4ec5c1e | -12.8359 | -44.3422 | 2026-07-01 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 458.5 |
| d77e8ea7-2bc2-3e2b-8b6f-d561f0b56954 | -12.7755 | -44.4693 | 2026-07-01 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 567.0 |
| 0ca342ab-7911-312a-ae55-e0b4f323f73c | -12.7751 | -44.4927 | 2026-07-01 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 592.7 |
| 6d24a52b-8068-359f-a8ec-44b4604fd41c | -12.8363 | -44.3186 | 2026-07-01 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 443e8360-c2ea-39b0-ba3b-244a20bd3619 | -12.8548 | -44.3625 | 2026-07-01 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 98534272-c13d-3239-9067-f7ba520716da | -12.7746 | -44.5162 | 2026-07-01 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.7 |
| f63ab13e-05cd-3650-bdf8-1f1068c46668 | -10.6787 | -54.5153 | 2026-07-01 03:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 4a1239bf-f503-3cb3-9b83-ac255262b637 | -11.6286 | -59.0169 | 2026-07-01 03:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 44.6 |
| afae2fee-817d-39e6-a77d-cf37bbbcb778 | -12.7557 | -44.4959 | 2026-07-01 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 435.5 |
| d80e9f4c-7da9-3862-a8cb-67bc1459e230 | -12.7755 | -44.4693 | 2026-07-01 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 405.9 |
| 61299b0e-c9ed-3fe1-865b-5e9dce7d449d | -10.6598 | -54.5169 | 2026-07-01 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| edd4e826-f026-30d7-ba2d-0be2d176c483 | -12.7562 | -44.4724 | 2026-07-01 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 305.8 |
| 679b8924-82b3-39c1-a3ef-2a3550978eaa | -11.5528 | -47.4546 | 2026-07-01 04:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 9557d230-85a8-3325-988d-2c17f5571f0f | -12.8354 | -44.3657 | 2026-07-01 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 182.0 |
| d09e72f1-72c4-3a67-931a-91d7e9a25aa1 | -11.4338 | -56.0509 | 2026-07-01 04:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 6885ef98-df68-3f7d-8fb1-e47106c15e65 | -12.7944 | -44.4895 | 2026-07-01 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 530f7699-0b68-35e3-b66e-591f388036a9 | -11.4149 | -56.0525 | 2026-07-01 04:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 5f81f03a-d056-356a-a72e-26a86722ef3f | -12.8359 | -44.3422 | 2026-07-01 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 480.3 |
| e720c35d-66ce-396e-b6f3-ffc4cdf7b3d2 | -10.9401 | -43.0355 | 2026-07-01 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| e0c8e0a1-3718-3b18-b706-007b3c6cb228 | -12.8552 | -44.3389 | 2026-07-01 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 280.0 |
| 62458140-5c2e-3711-a1c0-8e5bc501ec58 | -11.4147 | -56.0726 | 2026-07-01 04:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 0af9d564-ce5c-30bb-a005-1ce91600700a | -10.6784 | -54.5356 | 2026-07-01 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| d8e829a6-f325-351b-be6f-435824268b38 | -11.4336 | -56.0711 | 2026-07-01 04:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 107.2 |
| efe402db-57a9-34ea-bd97-c9946e05d896 | -12.8363 | -44.3186 | 2026-07-01 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 94a427ee-bd91-3ec1-b14f-6c865a70da2d | -10.9205 | -43.0622 | 2026-07-01 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 135.5 |
| a823a18c-7ed6-331e-989b-9fb725fdccd2 | -12.8548 | -44.3625 | 2026-07-01 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 111.1 |
| ea88dd1e-7410-34b5-88f2-a0e4c6fb05a2 | -10.6787 | -54.5153 | 2026-07-01 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 78d22ff5-925d-3a62-a8fe-9897c4fc1a76 | -12.7751 | -44.4927 | 2026-07-01 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 599.9 |
| d0603638-29d3-3ac3-81f0-bd936e3ebe4d | -10.9397 | -43.0593 | 2026-07-01 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 3f127b7d-8519-3993-9b2d-ec60bf0cf495 | -12.8165 | -44.3454 | 2026-07-01 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 77d4082b-6f56-38ec-bd5a-b98d8b013afc | -10.9209 | -43.0384 | 2026-07-01 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 1d16ab48-598d-3f33-aac6-2e1881d905b6 | -4.18401 | -47.84348 | 2026-07-01 04:00:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f05b307a-1651-3e72-9ecf-bcca10bc0b38 | -5.10009 | -37.78654 | 2026-07-01 04:00:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b247378b-a634-39eb-9cde-181756d91f09 | -4.16181 | -43.08816 | 2026-07-01 04:00:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8be8d85e-ce81-3681-8ea6-34030b29a732 | -5.21107 | -37.47756 | 2026-07-01 04:00:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4f29757b-f1ca-315d-9eb3-1f16245fc679 | -5.13827 | -37.84037 | 2026-07-01 04:00:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 5079ac24-9ee0-3755-b677-a60a8a381201 | -4.84629 | -42.93279 | 2026-07-01 04:00:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4962a61-d56b-366d-b7bc-57cb649c0b0f | -4.84637 | -42.93227 | 2026-07-01 04:00:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a83607e8-66ff-3b09-9554-d329c99ad5e7 | -3.50368 | -48.03556 | 2026-07-01 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 798b2621-551d-319c-a47f-760328aa330a | -5.20764 | -37.47705 | 2026-07-01 04:00:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6a083fff-f34e-39f6-a15c-22df8dc600b8 | -3.50946 | -48.03315 | 2026-07-01 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 47a62509-420e-33d0-bbcd-28043b4c0c9d | -4.15809 | -43.08756 | 2026-07-01 04:00:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 780275ec-937d-3646-b886-b368b61018a4 | -4.85004 | -42.93279 | 2026-07-01 04:00:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fafb262a-173f-3dd9-b3fe-895846390cd7 | -3.67824 | -48.98689 | 2026-07-01 04:00:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ff98be1-8356-3859-9bac-6d8adecd69e1 | -4.16004 | -43.08697 | 2026-07-01 04:00:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f281e9ee-aa11-3c21-9352-55d7d8b0a270 | -3.50893 | -48.03627 | 2026-07-01 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c66755a0-1a9c-3f1a-8f9a-465d5673bc2b | -4.1835 | -47.84648 | 2026-07-01 04:00:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 039e7b84-945e-3cc5-af5c-d27b26afce68 | -5.13433 | -37.84348 | 2026-07-01 04:00:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 047f3f0f-59e6-37f8-b009-771b7bb2cca5 | -5.03292 | -42.7301 | 2026-07-01 04:00:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9cf9836f-c189-38de-baa2-d6c22daeec52 | -3.5147 | -48.03389 | 2026-07-01 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| af58f680-8244-394a-912d-b3805bb0ad5c | -3.50838 | -48.03961 | 2026-07-01 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 81380806-344a-3649-8eed-9b67491cdc19 | -3.91633 | -47.81996 | 2026-07-01 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a80aa1d8-d778-3c94-942c-4f06cd0a1f79 | -5.13772 | -37.84401 | 2026-07-01 04:00:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 21.5 |
| c7511eee-a499-3680-8401-9dbdf24413e3 | -2.85074 | -40.19095 | 2026-07-01 04:00:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8d53f249-a4fd-32fa-b36a-2ab7423d4899 | -3.51417 | -48.03706 | 2026-07-01 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| fb38b4f5-74cd-3119-9333-c64761934c15 | -4.03516 | -38.24887 | 2026-07-01 04:00:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 269818b3-99af-3a65-aca0-3e224f801688 | -4.16251 | -43.08372 | 2026-07-01 04:00:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78235ee8-81b2-3e80-b63d-ab2856f6b1db | -4.87434 | -37.52274 | 2026-07-01 04:00:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |


[Clique aqui para ver as próximas entradas](README9.md)
