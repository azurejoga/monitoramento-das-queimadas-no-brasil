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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb400fbe-2ffa-385c-8beb-7d504bc4010e | -14.12458 | -52.36084 | 2026-08-26 04:53:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 891b9647-c6df-3370-91c7-6e3c5c967ff8 | -11.01693 | -45.06764 | 2026-08-26 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 094e92c7-5487-3e87-be02-81ce0171b93d | -15.34507 | -53.87766 | 2026-08-26 04:53:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0dc455bb-b1bc-3ebe-a28a-9a7492561b17 | -12.72865 | -48.38505 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61d53219-d1e6-372d-8148-f24ba9d31dcd | -13.28342 | -51.4677 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff89e46b-4b87-389e-a7f3-f35cc29c9990 | -13.16807 | -51.34404 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a45281f-4bad-34c3-8349-21417187fc7b | -12.7423 | -46.4869 | 2026-08-26 04:53:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 20fa81e9-e4cb-3f75-9707-546fa09bd93a | -20.51933 | -44.7322 | 2026-08-26 04:55:00 | NOAA-21 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 5b94e1cc-6401-3810-988a-cd7856ee912b | -18.54046 | -42.58167 | 2026-08-26 04:55:00 | NOAA-21 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0923288f-31a2-3183-bff3-4e81929ac456 | -16.19855 | -57.7571 | 2026-08-26 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7bc56ef2-255a-3673-958f-b7a8b64eca83 | -17.77751 | -47.09644 | 2026-08-26 04:55:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 98cc6916-a7c4-30e5-ae32-5c23a26b5c7f | -16.20208 | -57.75773 | 2026-08-26 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| fa3e9814-5709-3bb2-a0d2-5da96ae14887 | -17.96981 | -42.72559 | 2026-08-26 04:55:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a5d4850d-934c-372c-8c2c-f99e37d60c5c | -18.65187 | -47.29334 | 2026-08-26 04:55:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 42cffc97-7556-3c38-9ae2-58e9cd064bcc | -18.64694 | -47.29274 | 2026-08-26 04:55:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bb8c0cc4-2d62-3974-8b6f-d478bd43048f | -20.52184 | -44.73178 | 2026-08-26 04:55:00 | NOAA-21 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| d6423129-6879-3d96-82a4-d851e342da6f | -16.19924 | -57.753 | 2026-08-26 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 9646fe33-8855-36d3-ba80-122d4cf9f226 | -18.64985 | -47.29329 | 2026-08-26 04:55:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| af45d6d8-05d2-33b5-8d4e-e65244f402a5 | -18.47529 | -46.42736 | 2026-08-26 04:55:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a844b55f-3588-3d07-9b85-070a00191f9d | -25.31834 | -52.77306 | 2026-08-26 04:57:00 | NOAA-21 | ESPIGÃO ALTO DO IGUAÇU | PARANÁ | Brasil | 4107546 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7687610e-7b35-333b-a85f-e2cf2053e38a | -25.32118 | -52.77462 | 2026-08-26 04:57:00 | NOAA-21 | ESPIGÃO ALTO DO IGUAÇU | PARANÁ | Brasil | 4107546 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 5f335ee4-a9d0-3bdc-8b70-a52953dcfb5f | -10.7598 | -54.0179 | 2026-08-26 05:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 22d7a9ef-6d65-362f-90e0-ec9a5416ed0c | -13.2842 | -51.4541 | 2026-08-26 05:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 6767590f-bf19-3293-9300-62577ecb91af | -7.0613 | -59.2165 | 2026-08-26 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 7953dd76-ef99-34eb-adf7-6d3eef4f00de | -13.1903 | -51.338 | 2026-08-26 05:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| c933a7dd-d9af-3a44-aba5-c190e289e3d0 | -7.5289 | -61.3825 | 2026-08-26 05:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 126.2 |
| c62b12e3-e5b8-3b46-a8f3-1eb871f808ef | -7.0797 | -59.2157 | 2026-08-26 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 0b10f26f-baab-3e3f-8874-7d50ae5a66fc | -12.0358 | -46.0146 | 2026-08-26 05:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 567ad3d6-62a7-3dc7-aa67-360c03c4a95c | -10.7596 | -54.0384 | 2026-08-26 05:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 74b39daa-3b3e-3156-a2a7-546cc108d707 | -7.5105 | -61.3642 | 2026-08-26 05:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| b16646c5-4ea9-3002-91f7-cfb0b54422ad | -9.6024 | -55.1078 | 2026-08-26 05:00:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| acb84272-d22f-317b-9e31-32bb40d86ddd | -6.2677 | -53.3565 | 2026-08-26 05:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 78dc2903-f743-34cc-aa59-5a588c0351d0 | -6.6595 | -58.498 | 2026-08-26 05:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 35547870-8134-341c-8a4e-2a3d86992015 | -7.529 | -61.3635 | 2026-08-26 05:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| ab96f783-711a-360a-aff2-0304a7c45a04 | -6.641 | -58.4987 | 2026-08-26 05:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 937acd58-182e-30bd-9af2-2ab012286d88 | -13.3034 | -51.4517 | 2026-08-26 05:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 147.5 |
| c620ccef-2233-3371-aa50-29c37eddae85 | -7.5104 | -61.3832 | 2026-08-26 05:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 3f955ef6-6acf-36f1-8f3a-46825c37defc | -6.2676 | -53.3768 | 2026-08-26 05:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 24b21b91-5a5f-3d41-a7c1-ebbeee799e5f | -12.035 | -46.0602 | 2026-08-26 05:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| c02b8d4d-6c3e-3b7a-a2d2-037f5d8818b2 | -10.7784 | -54.0368 | 2026-08-26 05:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| f88bde8f-291b-3993-8622-717428870b61 | -6.2676 | -53.3768 | 2026-08-26 05:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 92aedf4f-4851-3995-854f-f635a6607c41 | -12.017 | -45.9945 | 2026-08-26 05:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 8f7e8b1a-16b3-32d3-9d54-a6f29d4b82e2 | -12.0354 | -46.0374 | 2026-08-26 05:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 306.5 |
| a21ebbab-f99c-364f-99c0-a98d47da3ca8 | -13.2284 | -51.3545 | 2026-08-26 05:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 84efafaf-c099-3609-9c09-c095851ab553 | -12.0362 | -45.9917 | 2026-08-26 05:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 984fd7ca-e024-3a22-b1e6-0bd035734321 | -7.5104 | -61.3832 | 2026-08-26 05:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 92b5ab1c-133d-31e2-b0b3-e010db03fd36 | -6.6595 | -58.498 | 2026-08-26 05:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 1506a0ef-0c52-3335-b155-d209103936db | -10.7596 | -54.0384 | 2026-08-26 05:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 213f5688-b24f-3b20-8edf-5ac8c450980e | -6.6409 | -58.5181 | 2026-08-26 05:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 1773cbb7-dc62-3f71-b2a3-7dec9617c7cd | -13.3034 | -51.4517 | 2026-08-26 05:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 163.3 |
| c6c47524-52b2-3ff5-8918-30f3db2cd34d | -9.6024 | -55.1078 | 2026-08-26 05:10:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| faaf9d37-02f7-3d8f-8ca2-f3631885f637 | -13.2839 | -51.4755 | 2026-08-26 05:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 1025469d-663b-396d-96f7-ef691bb2235e | -13.2842 | -51.4541 | 2026-08-26 05:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 25bb0a6b-1120-374a-ad45-c3195b16890d | -7.0797 | -59.2157 | 2026-08-26 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| cdc14b0f-45c3-3b18-8c6a-56e978eab3b8 | -13.3031 | -51.4731 | 2026-08-26 05:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 9ed4ae87-5e68-32aa-90f3-dedc85b527f9 | -12.0358 | -46.0146 | 2026-08-26 05:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 184.3 |
| 3c9f98fe-67e1-3200-ae35-41c294ca0219 | -10.7598 | -54.0179 | 2026-08-26 05:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 9828d82d-18cb-3eb8-96b4-fe4f6e841649 | -13.228 | -51.3759 | 2026-08-26 05:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 133.7 |
| b7f10656-4c6d-3fd0-9917-9b3c74148a5c | -13.2661 | -51.3925 | 2026-08-26 05:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.4 |
| e04d9275-7211-37c0-9227-c5058cd3f077 | -6.641 | -58.4987 | 2026-08-26 05:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 7152b2ed-e5ea-3c91-afbe-29d969903445 | -13.2472 | -51.3735 | 2026-08-26 05:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 176.8 |
| 7631884f-fa11-3223-918f-eba631802361 | -12.0166 | -46.0173 | 2026-08-26 05:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 44fdfb46-35e3-371c-a00e-30ec836824b7 | -7.5289 | -61.3825 | 2026-08-26 05:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 745dd550-cc20-3d06-877d-566841c3c1ec | -13.1711 | -51.3404 | 2026-08-26 05:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 3a84aae6-ecab-3dfb-817e-ecade023f2e9 | -13.2469 | -51.3949 | 2026-08-26 05:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 984ec0d0-220c-356b-8e55-5a5498a0a1be | -12.0546 | -46.0346 | 2026-08-26 05:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 2ce75f14-3ff5-38e9-9667-41ebafe20830 | -13.1903 | -51.338 | 2026-08-26 05:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 133e53df-ff28-3467-bbf6-30aa81051cfa | -10.7596 | -54.0384 | 2026-08-26 05:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 6ff54086-109d-3464-a198-c7919512f927 | -12.0354 | -46.0374 | 2026-08-26 05:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 397.1 |
| f643c937-abc2-3aca-bbf8-36208960b3da | -6.6409 | -58.5181 | 2026-08-26 05:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 94816287-b443-361f-ae8a-31e38f351c67 | -13.3031 | -51.4731 | 2026-08-26 05:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 51cccb4d-99a4-3e8c-8390-70ac3405da1d | -7.0797 | -59.2157 | 2026-08-26 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 6ccc13de-1c7f-3b1a-b3b7-2594985e7c99 | -12.035 | -46.0602 | 2026-08-26 05:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 54.8 |
| d795242a-e17f-385e-b216-5716629552f9 | -7.5288 | -61.4015 | 2026-08-26 05:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 86b6d42c-8c5a-3954-8079-3cf109d0fcb5 | -10.7598 | -54.0179 | 2026-08-26 05:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| e9a21a82-d8a3-30b7-b7bd-176f7986c51b | -12.0546 | -46.0346 | 2026-08-26 05:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 55.8 |
| b550bd3b-a7bc-3956-8913-50a72b4fe337 | -9.6024 | -55.1078 | 2026-08-26 05:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 5e2c51f1-9536-335d-827d-f2899bb48bb6 | -12.0162 | -46.0402 | 2026-08-26 05:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 96aaf052-a3c0-3170-9e26-c00b03bf990c | -7.5104 | -61.3832 | 2026-08-26 05:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 227b0e73-e650-3eef-a503-bd3530c8c784 | -6.6595 | -58.498 | 2026-08-26 05:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 1d9ef16b-c968-370d-8d3a-84d336def98d | -10.7784 | -54.0368 | 2026-08-26 05:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 9ab62880-e8fc-301a-86e3-74c2b224779e | -6.641 | -58.4987 | 2026-08-26 05:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 04252aeb-a0a9-33ff-a6c0-fd1976275918 | -13.2842 | -51.4541 | 2026-08-26 05:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| e7b124ca-377e-3d2e-8444-0b8d8b31e7ca | -12.0362 | -45.9917 | 2026-08-26 05:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| a19df54d-90db-3e94-a869-1ec6e9441771 | -13.264 | -51.5205 | 2026-08-26 05:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| bb391476-688a-3256-addb-a9ddfd2a5676 | -13.3034 | -51.4517 | 2026-08-26 05:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 120.2 |
| d978d448-32e8-365d-b76b-519bab2d67d4 | -12.0166 | -46.0173 | 2026-08-26 05:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 2d667e6e-746e-3516-94e8-b432e5a63ac0 | -12.0358 | -46.0146 | 2026-08-26 05:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 494.9 |
| 03c3ae68-6b55-39b9-8342-0ee9176e3e4a | -7.5289 | -61.3825 | 2026-08-26 05:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 76b0459c-ec07-3740-89d3-6921c217312a | -6.2676 | -53.3768 | 2026-08-26 05:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| a1c4bdd6-36be-3c5a-8471-ade5455802bb | -13.2839 | -51.4755 | 2026-08-26 05:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 25419ce6-58bd-3ee8-9c95-a23e4fd65494 | -13.2448 | -51.5229 | 2026-08-26 05:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| ac896056-4204-3d66-9ed1-0fa24082970c | -9.6212 | -55.1064 | 2026-08-26 05:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 9bdfe96d-5e80-362e-8456-92da3a8e4301 | 0.91497 | -59.62958 | 2026-08-26 05:25:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96a63ffa-e6fd-325d-ad3e-e9171b4ade61 | 0.9115 | -59.63013 | 2026-08-26 05:25:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efdac9b0-6885-39f1-8054-78416ed05c2c | -2.05093 | -48.04008 | 2026-08-26 05:25:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 51213d8a-f0c8-38ec-b0f4-e440f2d3cf7a | -2.04523 | -48.03922 | 2026-08-26 05:25:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 339d229a-4fcf-35b6-9a07-38a418fc4d70 | 2.0228 | -61.47374 | 2026-08-26 05:25:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e741f9a2-f0cd-3ecf-9148-1b1eba36e5e6 | -1.58743 | -50.44336 | 2026-08-26 05:25:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 933b6a26-ac82-314e-b67d-50f7ba2f4c0e | -6.14081 | -57.70605 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README49.md)
