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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4cc3509c-6d63-32b3-9156-62dcfe8333a7 | -6.68464 | -46.30195 | 2025-10-09 05:29:00 | AQUA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 62433830-127b-3644-a11f-6b2a4050a87e | -7.28148 | -41.97098 | 2025-10-09 05:29:00 | AQUA_M-M | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 3b7140b5-240a-39b2-af10-4927187e975e | -3.8584 | -42.25453 | 2025-10-09 05:29:00 | AQUA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| c4af42ea-3578-35a1-a7b5-571425a7d576 | -7.50194 | -42.71632 | 2025-10-09 05:29:00 | AQUA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 1e48885d-c924-3ea7-b099-aa7ffb15f82c | -5.40086 | -40.98475 | 2025-10-09 05:29:00 | AQUA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| b1689c39-b001-3cf8-8f07-da0f3a5c5423 | -8.20235 | -43.35299 | 2025-10-09 05:29:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 5cda9fbf-34b8-33a3-8ada-4138215fced5 | -7.01819 | -42.85266 | 2025-10-09 05:29:00 | AQUA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e3d0856c-b85d-3007-9fec-d76ce51e91ce | -8.18405 | -43.33791 | 2025-10-09 05:29:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 64cd174e-bb4a-386d-b2bc-4327bb1b6303 | -7.76789 | -44.03483 | 2025-10-09 05:29:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 5aafd7f7-b3a0-3ea0-9e25-bf430ecbf721 | -5.40234 | -40.97518 | 2025-10-09 05:29:00 | AQUA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| bcfd8ed1-0dee-3061-be3e-6d01dd19873c | -7.76152 | -44.03982 | 2025-10-09 05:29:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1380711f-d8a1-367b-a1ca-1dbfb2422f61 | -8.19414 | -43.33953 | 2025-10-09 05:29:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.3 |
| 3f716364-6627-3ab6-8bac-f2363ebf6aa9 | -7.01432 | -42.74708 | 2025-10-09 05:29:00 | AQUA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 56bcc23e-ffca-3972-af1b-c8aef044040e | -8.18594 | -43.32613 | 2025-10-09 05:29:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.2 |
| e59bf2cd-9129-34ae-b9bb-d5a3c24ea9bc | -8.20423 | -43.34119 | 2025-10-09 05:29:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 41c177b8-c0d0-3b78-9816-dde559581316 | -7.77227 | -44.04127 | 2025-10-09 05:29:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3dc34e46-2890-3339-b83c-10cbf9ae4c20 | -8.19602 | -43.32775 | 2025-10-09 05:29:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 35.4 |
| e9978f69-7103-3ca6-bcd7-5239acc9f681 | -7.34944 | -43.86185 | 2025-10-09 05:29:00 | AQUA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 31648db0-1dd8-3d59-a8a3-3f50e54fc971 | -7.01642 | -42.8641 | 2025-10-09 05:29:00 | AQUA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| ab9e60b8-c52c-33a9-94d4-4a441e3c08bc | -5.39938 | -40.99433 | 2025-10-09 05:29:00 | AQUA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| c9ca9417-0b2c-3334-873b-e4cdf51920cb | -7.48173 | -43.10501 | 2025-10-09 05:29:00 | AQUA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 0434121a-885a-3fa2-abb2-5a6043b20e79 | -10.86373 | -44.62227 | 2025-10-09 05:31:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 48d89758-6f00-34ca-b912-f4a06f339c3c | -16.28806 | -47.13135 | 2025-10-09 05:31:00 | AQUA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 53dbb727-9928-3201-b5eb-974a313e9ca5 | -15.05677 | -42.33562 | 2025-10-09 05:31:00 | AQUA_M-M | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 15.2 |
| ae952c91-f1ed-36da-81bd-4ec1f6370e27 | -9.08983 | -47.94372 | 2025-10-09 05:31:00 | AQUA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 9acac6af-8328-3de4-ac4d-41e5f6dce892 | -14.97748 | -46.2894 | 2025-10-09 05:31:00 | AQUA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f50f1350-4a5a-3be5-aee7-5589d9d39bfc | -11.75087 | -45.13438 | 2025-10-09 05:31:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 96dcbf96-956a-375f-9fbd-c5f7607e4464 | -13.78905 | -45.86608 | 2025-10-09 05:31:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2032cb82-3647-3077-abc8-c370ba03acfd | -13.78656 | -45.88066 | 2025-10-09 05:31:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 76c4b9cc-2d83-3d9a-9765-ba52fe73fa31 | -16.74989 | -43.96814 | 2025-10-09 05:31:00 | AQUA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 61976c3f-d59c-3047-8c9e-aab4f061c614 | -10.85531 | -44.60729 | 2025-10-09 05:31:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 11842ef8-c78e-3c27-afc9-133b1a529f5c | -11.78092 | -45.15448 | 2025-10-09 05:31:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 62fcad9e-dd26-3ec3-a76c-c20b1aa39b27 | -16.74357 | -43.97091 | 2025-10-09 05:31:00 | AQUA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 6de4c17c-4830-33eb-86f8-0ac17f5409ec | -11.74717 | -45.14165 | 2025-10-09 05:31:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 973f0afe-06ac-3459-b207-4b73fef985b3 | -14.41096 | -43.97125 | 2025-10-09 05:31:00 | AQUA_M-M | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f913ad93-22b9-3be3-a952-09cbf6692d51 | -10.85315 | -44.62044 | 2025-10-09 05:31:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| bd7a9ceb-a7f6-3ebd-993b-10b0188c4c93 | -11.24097 | -40.33138 | 2025-10-09 05:31:00 | AQUA_M-M | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 971a1297-7b01-3b00-a991-64b7823d391a | -15.47133 | -47.95247 | 2025-10-09 05:31:00 | AQUA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 091115c8-fb20-3f3a-a722-7490416fb7b3 | -11.23963 | -40.3403 | 2025-10-09 05:31:00 | AQUA_M-M | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 96012343-d7da-3f3c-a0a6-8f6efc4a01dc | -11.78334 | -45.13999 | 2025-10-09 05:31:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d2f21bc2-5ced-32c2-a9b8-34d81fa02fa0 | -14.42228 | -43.96205 | 2025-10-09 05:31:00 | AQUA_M-M | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4426a32e-0eac-3942-a0cf-903c50e284be | -15.28969 | -46.15307 | 2025-10-09 05:31:00 | AQUA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 31a94dac-2552-37c8-92c5-471afe85f475 | -15.2163 | -46.3773 | 2025-10-09 05:31:00 | AQUA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 0458bf3d-8bd2-3597-b225-0bcfc72afdc2 | -16.74824 | -43.97826 | 2025-10-09 05:31:00 | AQUA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| ee865888-3481-381e-bc24-8f4794b6159c | -12.5843 | -41.28551 | 2025-10-09 05:31:00 | AQUA_M-M | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| e1d106be-bbdb-3659-9d14-c55e0541579d | -12.23152 | -43.78383 | 2025-10-09 05:31:00 | AQUA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 424986d0-b76d-3723-b760-ff1a10d86522 | -14.97686 | -46.28346 | 2025-10-09 05:31:00 | AQUA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 71485ed8-b36a-3e4d-9217-1fd46b7273ee | -14.7216 | -48.36418 | 2025-10-09 05:31:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 84526c90-1b9f-3594-a61b-6c27dec1a437 | -15.05819 | -42.32632 | 2025-10-09 05:31:00 | AQUA_M-M | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 6d38cee6-8077-3817-a1b9-a71bfbf65e94 | -15.55861 | -45.31707 | 2025-10-09 05:31:00 | AQUA_M-M | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| f5ac4950-7900-39bc-a0b5-afed44f7f214 | -15.07298 | -46.60086 | 2025-10-09 05:31:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 0c2e39c2-55f2-3a03-b56d-62d13f301a34 | -14.42054 | -43.97287 | 2025-10-09 05:31:00 | AQUA_M-M | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 6154e9a3-e283-3f5e-b733-05f1c000cbd1 | -18.64763 | -43.91323 | 2025-10-09 05:33:00 | AQUA_M-M | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 103e8a3c-1a95-3247-ba89-13bbce74ac56 | -17.62783 | -47.21237 | 2025-10-09 05:33:00 | AQUA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 50dbe590-836a-3438-916d-84dedb50e4d1 | -18.04471 | -44.95993 | 2025-10-09 05:33:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| aa6c02d9-4c98-3601-baeb-483f547f9a69 | -18.6461 | -43.92282 | 2025-10-09 05:33:00 | AQUA_M-M | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 2a404928-5bae-3e46-ba2f-5d6b60b17f40 | -18.09024 | -44.44367 | 2025-10-09 05:33:00 | AQUA_M-M | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5d5c5962-6fb8-37c9-b03c-f2f949c69196 | -17.95543 | -44.99606 | 2025-10-09 05:33:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 6e3e3637-c58f-329f-9baa-2b4e30aa01a1 | -17.20267 | -47.65478 | 2025-10-09 05:33:00 | AQUA_M-M | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 21db9e0e-3cf6-3651-b11c-eafb26df43a9 | -18.41161 | -45.23359 | 2025-10-09 05:33:00 | AQUA_M-M | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 1101a990-ecb7-3834-983e-31b8b46a6712 | -17.95359 | -45.00734 | 2025-10-09 05:33:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 6a6bb90d-d0e8-350a-8a15-f830d2d2ccb8 | -17.26746 | -46.95934 | 2025-10-09 05:33:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 66af840d-56a7-3bf9-8454-b75f5b26d612 | -17.63064 | -47.19661 | 2025-10-09 05:33:00 | AQUA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 171615e3-e6b7-3cf7-9125-558276b0ec6c | -18.78318 | -44.61756 | 2025-10-09 05:33:00 | AQUA_M-M | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| deafc0ca-5b5a-3a7b-acea-e95a06bed5e3 | -17.21445 | -47.65727 | 2025-10-09 05:33:00 | AQUA_M-M | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 21.5 |
| c11347f4-c681-30d5-98d0-432de03fa95f | -17.6479 | -44.4324 | 2025-10-09 05:33:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 52dfeae1-5073-3a1e-894b-42ee25e9e62b | -17.88767 | -42.8655 | 2025-10-09 05:33:00 | AQUA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 4c4a2c07-f9fd-301b-941d-6bd3ff74252b | -17.64615 | -44.44313 | 2025-10-09 05:33:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7786aa5c-f458-3b67-90c2-cbcd777e7269 | -17.95729 | -44.98469 | 2025-10-09 05:33:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f902ef5c-1520-36fe-9241-223828bb09af | -18.78493 | -44.60699 | 2025-10-09 05:33:00 | AQUA_M-M | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 6db1930d-ef8a-3250-b6c9-d40be1232264 | -17.38539 | -46.87758 | 2025-10-09 05:33:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 7c5cfcb0-2c1f-37a2-a58e-7b0950ad6ebb | -17.52314 | -46.75615 | 2025-10-09 05:33:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 869fbf21-6a0b-3e6e-b813-9755f09f6fa2 | -18.05436 | -44.9616 | 2025-10-09 05:33:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 8aed6214-c128-3643-832c-7c35f0bb9b3c | -17.21756 | -47.63969 | 2025-10-09 05:33:00 | AQUA_M-M | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 9a87d2f8-0b60-3dbb-8489-2f7a6ab1c444 | -17.52572 | -46.74146 | 2025-10-09 05:33:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 64.2 |
| de82dc49-acc1-3200-999e-64862249e25e | -17.64195 | -47.19877 | 2025-10-09 05:33:00 | AQUA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| a1d128f2-5fe8-3938-8a24-50698e0c2489 | -17.63914 | -47.21465 | 2025-10-09 05:33:00 | AQUA_M-M | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a1b12570-2fd5-3165-850c-4ce1489eb4b2 | -17.97538 | -44.9591 | 2025-10-09 05:33:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 49959752-4d65-3b5e-8dc2-8a3dbcfa6dcb | -17.26442 | -46.90458 | 2025-10-09 05:33:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 79fb8f34-5b68-3812-b5b7-632e16b1cda9 | -18.42134 | -45.23544 | 2025-10-09 05:33:00 | AQUA_M-M | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| da16fb06-0142-3c3a-ab1c-d869c9aa4618 | -17.26484 | -46.96922 | 2025-10-09 05:33:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 6e95576f-c23f-3661-8e2f-5f2dcc2c8580 | -17.26476 | -46.91005 | 2025-10-09 05:33:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| a2ef8328-e418-3317-94df-e0abf7e9b8d2 | -18.06567 | -44.41751 | 2025-10-09 05:33:00 | AQUA_M-M | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 084679b3-d1ef-31f4-8352-ee0f4c9c061e | 0.88617 | -51.14795 | 2025-10-09 05:36:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a5f35d4f-59aa-30c7-8a71-5b45bc392ee4 | 0.90243 | -51.13024 | 2025-10-09 05:36:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7cb4a49-f505-3ac4-8806-04d8e7d9340f | 0.88647 | -51.14653 | 2025-10-09 05:36:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d262787-541b-3f26-ad9e-b3e12eb46eaf | 0.89759 | -51.21386 | 2025-10-09 05:36:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8626741-41ca-3511-8328-e0f61cb2c343 | 0.90775 | -51.12474 | 2025-10-09 05:36:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b884bc3-e5a8-36fe-b4c4-121b9db1061a | 0.89081 | -51.21024 | 2025-10-09 05:36:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddc91ec6-45c0-35b1-8755-3e977707b71c | 0.89155 | -51.21471 | 2025-10-09 05:36:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46fb74f3-9107-32af-bbb9-747fc65ee944 | 0.89179 | -51.14112 | 2025-10-09 05:36:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b16effb4-26b4-3a2a-a99a-570504ac3fc1 | 0.89612 | -51.21097 | 2025-10-09 05:36:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0f328281-2e6d-3b1b-b655-8fcae7e53cf6 | 0.89637 | -51.13118 | 2025-10-09 05:36:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96db7b93-efff-3fec-9e65-126ab46a092d | 0.89711 | -51.1357 | 2025-10-09 05:36:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6334b803-fb32-3ca7-bab9-be2ab65ab375 | 0.89687 | -51.20948 | 2025-10-09 05:36:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37af6431-d209-3151-be77-7ff584fb3cc2 | 4.46342 | -59.89818 | 2025-10-09 05:36:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd23429d-12e3-3695-9dd6-6b0436d67631 | -2.88805 | -50.72828 | 2025-10-09 05:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84a594da-7280-35e1-b5e1-72f8aae84fa0 | -3.39262 | -50.14165 | 2025-10-09 05:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9754ac79-bb50-3773-af7d-89a49e329f87 | -3.38485 | -50.14693 | 2025-10-09 05:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd5d7612-1cfd-3821-b3d2-26c21e2d9f83 | -3.38637 | -50.14362 | 2025-10-09 05:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README59.md)
