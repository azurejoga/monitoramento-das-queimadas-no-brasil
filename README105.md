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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aefbc946-6232-34bd-8c4e-06e55e95b357 | -13.72039 | -48.1049 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19ca45ca-1756-3261-8625-beaa6896c046 | -15.97962 | -50.90707 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| b79936a5-2d3f-3d86-9b64-8c5644b0eb21 | -14.00993 | -48.20825 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2408c54a-b632-3c00-bddc-d7fa9259d294 | -16.07672 | -50.91293 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b8292fd7-fed3-3a92-8021-72d6a13cca27 | -14.7417 | -54.62206 | 2025-10-05 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8bfa281b-12dd-3ea8-8752-3b9e04031456 | -13.7422 | -48.06141 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3bca07b0-0377-3ae1-bed1-8de0300c28e9 | -16.88145 | -49.3961 | 2025-10-05 04:49:00 | NOAA-21 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47718a03-5bd3-3836-aeef-5a0802023227 | -15.13027 | -45.74195 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89f73a45-0c01-3d85-ba91-13d5cf97e261 | -14.93168 | -48.35034 | 2025-10-05 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7c97c04-4486-3788-8ba5-b43b60833e07 | -15.58632 | -48.2121 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12f176b1-a24b-3775-aa10-15cf1d061415 | -17.88393 | -57.63249 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 597841b3-3d12-378c-b728-e7d63c84a1e0 | -12.95102 | -54.7325 | 2025-10-05 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b7cc70b-c2a1-3ee1-a378-611cdc79d2c5 | -15.98193 | -50.91556 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 57d61241-8aae-340e-ab1c-3092cec247a6 | -18.18175 | -53.34658 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db76ccf5-2b08-30cc-a17f-28f805794d49 | -15.19319 | -52.79244 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6893c71-7ffa-32b9-8571-7ed0894729a1 | -14.68491 | -48.31188 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7934f2ae-c86c-3833-8946-5d529c2b4655 | -15.60439 | -52.50868 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 77529208-afb3-320e-85d0-f3edbba83609 | -14.27451 | -45.86683 | 2025-10-05 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d796d01-80c2-3907-aabb-d48160aa3228 | -14.92495 | -46.84315 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 54c0eff2-d8e2-3a7c-b37b-123ecaddd595 | -15.61044 | -52.46912 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 638f798b-b4ab-3832-9d40-f7532709802c | -16.3844 | -52.15766 | 2025-10-05 04:49:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 27.8 |
| e1c0a5a9-d7d4-33ec-be12-dcb1a5c5733f | -14.82363 | -54.76636 | 2025-10-05 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| afcf6c06-ef47-3801-ae61-c9c9dedd8de9 | -15.96488 | -43.32683 | 2025-10-05 04:49:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28e3f311-8a83-3207-8d35-569c39a7c8ba | -15.34794 | -47.33539 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b42fa52-1acb-31c0-828c-893d47102b7e | -17.11512 | -48.92356 | 2025-10-05 04:49:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a275b515-db6d-3d30-9933-a250f18d67a7 | -17.70704 | -56.7725 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0ac7f0ee-05ea-36d8-9d7e-26dae67ad72f | -15.5834 | -52.49042 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 8ae26f06-c0f2-36c8-8d7e-a3bd0f2a6691 | -15.60053 | -52.5117 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| be35e562-c36f-3293-9ffb-00dc5b42a8d2 | -14.43546 | -48.2305 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ceb4153e-8745-3f1b-b7bc-fbfd2816fca6 | -14.22248 | -56.57316 | 2025-10-05 04:49:00 | NOAA-21 | NORTELÂNDIA | MATO GROSSO | Brasil | 5106000 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f7fc598-b31d-3b5b-b8f1-1beaee0ddfe8 | -13.72565 | -48.09538 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db617701-7ea2-3772-841b-5a155590b66d | -16.24281 | -52.91067 | 2025-10-05 04:49:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c664114b-53e3-3aa9-96bb-7f21f14cb4f6 | -17.97011 | -51.14926 | 2025-10-05 04:49:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82318edf-d27d-320f-9d85-433270b1bbab | -17.87926 | -57.59344 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| d860dfb1-0cc2-3f1c-bb89-9a1a92ef9997 | -18.17899 | -53.34241 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eaa004a3-c928-32b8-a4ef-2f0c4ed82f34 | -14.33369 | -47.6754 | 2025-10-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 64587280-3c5d-3940-b2d2-e78756a47a3e | -14.3367 | -45.85825 | 2025-10-05 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 580e2584-ab74-35d6-8e45-880293f21bd0 | -15.23065 | -49.29212 | 2025-10-05 04:49:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| beb09aa2-916f-3523-80de-eb1a7af38e98 | -17.95951 | -57.58364 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| daeec0bc-6bf2-357d-90b9-d70fb9212461 | -14.68675 | -48.26818 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7bec7740-aa29-3b56-a24c-4d5fa403a371 | -14.91924 | -46.85328 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 2ee674cf-316f-398e-aae6-08b7a31b9fa0 | -15.55164 | -46.95892 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e673be0e-c20b-3ac8-8197-6f51430dcbb8 | -14.84817 | -48.7608 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6a3a5e36-7fbe-3a87-a5ac-bee74c69691b | -14.9401 | -49.96995 | 2025-10-05 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96d66419-7325-38cd-8b47-a83ccc6a9e07 | -13.73378 | -51.3097 | 2025-10-05 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0d3ddc6b-a6eb-344c-9cfd-179c0ccbdef3 | -15.75596 | -46.26847 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 03153e68-3b0c-31f2-9f83-223179a8f3ed | -16.35434 | -51.47948 | 2025-10-05 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 454d7347-2c7e-351b-abc6-a3426cddce0b | -13.73233 | -47.95953 | 2025-10-05 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0b81cdf8-2861-3606-9e46-5765f430679a | -14.69115 | -48.35409 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fbe9bb1b-915e-3c89-9212-39afb824a924 | -14.01455 | -48.21026 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0183d972-3f1c-3714-a7ac-fc37ddae1521 | -13.91582 | -48.19358 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ba470ce4-824a-3040-9b1a-969d880d4564 | -14.59453 | -52.46542 | 2025-10-05 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0fe9f56d-f351-371a-bcc2-8a53356fa74a | -13.75138 | -47.96348 | 2025-10-05 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ce241217-4c3b-3ec9-b985-1ff440b1263d | -16.05704 | -50.92647 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a1a928ef-933b-366a-b4c3-47f4c4e7a9b9 | -16.94822 | -52.67887 | 2025-10-05 04:49:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c395d9f-adf7-37e5-8cb3-be9715ca1225 | -18.25179 | -53.33241 | 2025-10-05 04:49:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8f619905-7596-3b05-a52f-d3c21ad807b3 | -15.36132 | -46.29733 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66e64ab4-c06a-3600-a7a2-8a442b3a0447 | -15.77581 | -49.09444 | 2025-10-05 04:49:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ad49fd5-d80e-39f9-b347-316271d3b37d | -15.20046 | -56.83084 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d8b6d39b-a928-33af-8e5e-38fbaac07a3a | -18.19111 | -53.35186 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dae833b4-9799-388f-a4e8-d2431cbaa8fd | -16.36059 | -51.46086 | 2025-10-05 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 917199ef-fcf3-384a-96af-5e0457b1f5a6 | -12.9317 | -54.72129 | 2025-10-05 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69368719-aaa6-39af-8f25-4929f50df0a3 | -18.14457 | -53.3445 | 2025-10-05 04:49:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b63da6d-fd97-33ff-a2bd-5393d0c5f6f8 | -15.24598 | -56.7654 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5891916f-2e27-3230-a04d-cbbd932e9b8e | -17.96282 | -57.56483 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a7877803-f0de-3a6f-bbda-6a1fd8ffa7eb | -15.93665 | -48.9928 | 2025-10-05 04:49:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 58336676-7f78-368b-be4d-cf1a8e7b72f4 | -16.15158 | -57.58119 | 2025-10-05 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| ba45bea9-8f60-3b41-a8f5-b4558f447395 | -16.34583 | -51.46635 | 2025-10-05 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b37df6ee-5da3-3319-ae56-26b70ff44f5b | -15.98303 | -50.85921 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 67749f24-335c-35d8-9fad-56689c37dfe6 | -18.24905 | -53.32821 | 2025-10-05 04:49:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a8d44aba-a5c7-3b13-89b3-8cfcf3972303 | -14.99787 | -49.96606 | 2025-10-05 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 508e7488-3018-3667-8bab-01249d186480 | -17.96179 | -57.54906 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 8085fe0c-88df-3f82-8958-25d36c8ed0d7 | -15.42557 | -50.2121 | 2025-10-05 04:49:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 251cb0ce-dad6-3cf7-8bac-7741364b4715 | -14.95285 | -46.84929 | 2025-10-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f62e98a7-474c-3564-96c4-f4010ae1fca6 | -15.36493 | -47.97565 | 2025-10-05 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5838e603-d2ce-3758-ac96-ca03512d92e3 | -17.9136 | -54.68029 | 2025-10-05 04:49:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a71e83ea-c260-35fd-a303-a51187e38789 | -17.94886 | -57.60081 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 324dddb4-6c0a-3584-92dc-2a616cb2f5fe | -15.20747 | -46.39187 | 2025-10-05 04:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a88979ef-5382-3fd3-861c-dbf1344625dc | -17.95135 | -57.58667 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| e2cdbb72-1e63-38c2-94d1-62cb91c0219b | -15.98595 | -50.91228 | 2025-10-05 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c0c0d59c-f626-3498-8380-962cbbd8b3f5 | -15.57179 | -52.47742 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ecc02af5-bc09-31b8-a879-ce787a71908c | -18.20002 | -53.29398 | 2025-10-05 04:49:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7231c382-ba83-32e7-9704-f862ed341165 | -15.81038 | -46.25018 | 2025-10-05 04:49:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c69331b2-fa1a-3e82-9256-a488a2bdc7aa | -14.74386 | -54.63007 | 2025-10-05 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29179206-d8d7-335c-b805-cf411e94b492 | -17.97687 | -45.00355 | 2025-10-05 04:49:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfae2755-af90-3fc5-b20f-cc2235aeaaf1 | -13.92382 | -48.16496 | 2025-10-05 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e01262f-15f1-3f2f-a788-7233ef587a7a | -18.23857 | -53.33013 | 2025-10-05 04:49:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31802d4d-039a-35d1-a428-df7ea0b4afce | -14.67809 | -48.36261 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4ca4b117-ad1b-3658-825f-a7452010d256 | -18.24849 | -53.33184 | 2025-10-05 04:49:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f4b07bd6-2949-33b2-9628-3a11a5bcd8f1 | -14.67365 | -49.61216 | 2025-10-05 04:49:00 | NOAA-21 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ea47234-e53c-3f2a-824e-5f50e90db2ae | -15.55255 | -46.84853 | 2025-10-05 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3ce372e7-b64a-3239-a9a4-4fda9e8bb603 | -15.22431 | -56.80294 | 2025-10-05 04:49:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d80a86f1-bb12-36f0-b448-9a42e4810cf8 | -15.59999 | -52.51527 | 2025-10-05 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e658c79c-1933-33ee-a576-4e2ffa776d1f | -15.23863 | -49.28931 | 2025-10-05 04:49:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff949d21-bb55-3a72-9001-8c9ae26c6312 | -14.65369 | -48.33707 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f5dbfc76-383f-3231-a3e0-bbe2fa65a8ea | -12.91586 | -54.73473 | 2025-10-05 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 348624bc-29fe-3e05-a4f6-40144659f918 | -14.64732 | -48.3251 | 2025-10-05 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dd46d4f0-ba38-30c7-8c64-87773e2f5465 | -16.01776 | -50.84033 | 2025-10-05 04:49:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6d9b8b4-b343-3ab3-ac39-8f80e86fc4ed | -17.92433 | -57.60996 | 2025-10-05 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9a44d8d9-7209-3b77-9624-7cc5a573a9fc | -16.35436 | -51.45583 | 2025-10-05 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README106.md)
