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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 462370da-1a75-3870-bab6-b6ec778974a0 | -2.9739 | -51.0455 | 2026-09-30 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 205.6 |
| 785589d0-b8f0-3c99-afb9-e9d588c3b985 | -12.2706 | -50.2735 | 2026-09-30 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 602e6535-130d-3600-a3e2-f1d60847d7ee | -7.8483 | -45.8363 | 2026-09-30 00:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 143.7 |
| ae6bb023-2ef7-3aa1-b105-d063069226bf | -3.2129 | -46.9383 | 2026-09-30 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| fbdac8fd-40b2-302e-b54e-5ee87ee270d7 | -9.1256 | -67.8507 | 2026-09-30 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| aeecc979-37f5-3391-b1ec-8f0dad1aeb35 | -5.7374 | -45.176 | 2026-09-30 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| e431f1dd-1687-35b1-96e1-ba4bd7a7062a | -5.7561 | -45.1747 | 2026-09-30 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 216caa90-48e0-3126-a7ee-266462cf2d66 | -2.9739 | -51.0663 | 2026-09-30 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| dc4e6b12-d846-3e8e-8f73-72ccc28dd982 | -2.974 | -51.0247 | 2026-09-30 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 160.1 |
| 30f02224-330f-35c2-8bf1-91d08cbf68fb | 3.2742 | -60.6105 | 2026-09-30 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 82.9 |
| b51d26e0-11f3-3328-9257-03efc48b5f3b | -7.7317 | -72.4597 | 2026-09-30 00:00:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 52f86b53-ae26-320a-a41f-0c6ad5c2c9a7 | -8.2865 | -50.2731 | 2026-09-30 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 5dd687c7-50ec-3508-8d0b-fc444a517124 | -11.8814 | -64.9323 | 2026-09-30 00:00:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 0fd0e43e-2894-3243-967e-c7557d358cbd | -12.2518 | -50.2543 | 2026-09-30 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| f17b393b-28e7-369e-8346-4ab3cec47dab | -12.3085 | -47.9539 | 2026-09-30 00:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 31155bef-805c-3fd0-b956-352bc16676de | -6.2311 | -42.4989 | 2026-09-30 00:00:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 33.9 |
| 201a6151-e689-362f-964a-1b79ca19b61b | -7.8297 | -45.8156 | 2026-09-30 00:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 335.8 |
| 25921049-e068-3a64-a04c-95794d13dff6 | -11.328 | -51.0018 | 2026-09-30 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 13bb9c69-5962-3e47-a2d1-39bf9bd1e95f | -7.4407 | -64.3459 | 2026-09-30 00:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| bc15419a-6d6a-3a99-9e71-6fe7365206d8 | -7.8295 | -45.8381 | 2026-09-30 00:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| cc32f2c3-5736-3e4e-992a-e08f40708430 | -7.8486 | -45.8138 | 2026-09-30 00:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 264.0 |
| e054c87c-e5e9-3254-a222-706ff4e9e6d0 | -2.8899 | -54.0912 | 2026-09-30 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 983a44f7-a177-3387-b643-9893c3db785f | -3.2314 | -46.9376 | 2026-09-30 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 275.6 |
| fe0ab996-349c-3f78-9b0a-600888273176 | -7.8109 | -45.8173 | 2026-09-30 00:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 993ca378-376c-324a-bf85-71d70bb47328 | -12.2515 | -50.2758 | 2026-09-30 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 0f53a5ab-d67c-396b-95ee-44c80813464a | -6.8292 | -55.1226 | 2026-09-30 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 41a1e5c0-b1d6-3231-8fc7-5aaab596c4d6 | -10.0779 | -63.0804 | 2026-09-30 00:00:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 6b047f81-de98-36b5-93cd-bb89e873fc67 | -6.2123 | -42.5006 | 2026-09-30 00:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 119.5 |
| 99e09209-ebbd-3925-95c5-808e239476df | -20.5553 | -49.5972 | 2026-09-30 00:00:00 | GOES-19 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 39d78df6-e172-3eb2-8e6b-92b3c093948a | -6.895 | -43.7066 | 2026-09-30 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 3c876972-b720-3cf7-b01b-1dc6cf7ba98c | -6.8291 | -55.1426 | 2026-09-30 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 73f89ee0-3bd7-3364-96b1-199b3cc7d071 | -7.7133 | -72.478 | 2026-09-30 00:00:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 65.6 |
| a0fe2522-fa57-39e9-9441-bf578ef75eaa | -11.4311 | -43.4121 | 2026-09-30 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 04b29b6a-3a35-316f-a8ff-ba41360e4c75 | -9.1257 | -67.8322 | 2026-09-30 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| cc79978f-6089-3586-821b-7f76d8948559 | -10.5316 | -57.7747 | 2026-09-30 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| e4dd9107-10b2-3c8f-a253-209807ee3e54 | -19.831 | -45.0153 | 2026-09-30 00:00:00 | GOES-19 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 63.1 |
| f3db2d79-7f8d-3bee-bfb6-90de106f364b | -11.8812 | -64.9513 | 2026-09-30 00:00:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 72.7 |
| f9b1e012-1e7f-3d80-9c72-06aa6d9336de | -3.494 | -54.7366 | 2026-09-30 00:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 292cf226-bc34-369a-875e-1ab77617cc57 | -3.2315 | -46.9156 | 2026-09-30 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| e3582733-d97e-3e1c-9035-97fa760c9504 | -19.2571 | -46.6756 | 2026-09-30 00:00:00 | GOES-19 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 5c8037d0-8bdd-315e-9f1a-897cdad7eee3 | -3.176 | -51.2473 | 2026-09-30 00:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| bec0ea98-fc68-3043-a957-a674820cdd82 | -2.9082 | -54.0907 | 2026-09-30 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 1d08b51b-3f42-3dca-a144-92cfd1a6c832 | -4.8192 | -45.6411 | 2026-09-30 00:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 62.1 |
| a0c50aff-7a5b-3c17-8f1e-83285668fffc | -12.3427 | -48.1929 | 2026-09-30 00:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 744b36fd-8ac2-3242-8c6f-8d93fbed6049 | 3.2924 | -60.6101 | 2026-09-30 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 87.3 |
| fb5c83c3-a4cd-3656-83f8-a5836c1def80 | 3.2741 | -60.6294 | 2026-09-30 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 71.3 |
| b35ae2c6-dfec-330d-884a-62b4cdfacc0c | -6.212 | -42.5243 | 2026-09-30 00:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 114.5 |
| cc1f7110-39b8-3f49-a044-d297978fb114 | -10.0593 | -63.0812 | 2026-09-30 00:00:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 55.4 |
| f44b5e9e-dceb-373f-b073-c540c88b88a2 | -11.4499 | -43.4329 | 2026-09-30 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 5b38e7e3-02d8-3cab-83cb-05f23cc92891 | -7.7317 | -72.4779 | 2026-09-30 00:00:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 2b3928be-2b9f-33b2-97a1-c239c79e08dc | 3.2924 | -60.6291 | 2026-09-30 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 3da1276b-d32d-3eca-bff8-f0ef3c1fbc4d | -11.4307 | -43.4358 | 2026-09-30 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 8ef6b13b-2041-3925-8703-2145cc675524 | -2.9925 | -51.0242 | 2026-09-30 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 00e73e96-e205-34cb-9669-63d707a5ff38 | -2.9924 | -51.045 | 2026-09-30 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 150.3 |
| b2433450-0335-365b-841a-584a4454487a | -9.1072 | -67.8326 | 2026-09-30 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 9557365d-c7a9-37d8-8e02-31845dd3b8f8 | -8.2678 | -50.2746 | 2026-09-30 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 4a38dc52-9443-3e9b-b2d0-bd8894852b63 | -7.8297 | -45.8156 | 2026-09-30 00:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 273.9 |
| 500422de-4d07-387a-a0c5-b79ada42e900 | -11.8812 | -64.9513 | 2026-09-30 00:10:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 80.1 |
| da13c494-672b-3292-a903-d614eac0b865 | -10.0779 | -63.0804 | 2026-09-30 00:10:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 77.0 |
| d99d247a-a753-31a5-968e-59b253bb869a | -11.4307 | -43.4358 | 2026-09-30 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| f92eaa5b-337b-33f2-a10a-4d2fa2f9e1d5 | -3.3801 | -50.95 | 2026-09-30 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 4cfe70e2-bee1-366b-a3dd-2fc402a1a384 | -11.6207 | -43.5248 | 2026-09-30 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 0cc274e1-6380-3efb-939d-6be57c2e352b | -9.1257 | -67.8322 | 2026-09-30 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 13838202-4846-38d6-b1aa-540da433bba2 | -11.6395 | -43.5455 | 2026-09-30 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 8e5f7073-13f1-345a-a528-ee9ddc60f181 | -7.7133 | -72.478 | 2026-09-30 00:10:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 43391593-2e4b-371a-bad0-86e09cd1281b | -3.2314 | -46.9376 | 2026-09-30 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 253.4 |
| ef554c18-2ae4-36e4-8ebc-d6108c19dee7 | -11.699 | -43.4416 | 2026-09-30 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 147.7 |
| b665dfb9-5a6f-3eef-8c8d-a7dd1c5e3f7b | -12.2518 | -50.2543 | 2026-09-30 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 3cf70f04-0e38-308b-bc63-49cb878bc7d4 | -7.7317 | -72.4779 | 2026-09-30 00:10:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 91.4 |
| b2790375-aa6f-3cf3-bfdb-3d1109ef2c6f | -2.9925 | -51.0242 | 2026-09-30 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| a45e4568-7730-3689-8807-b108d90803e6 | -9.1072 | -67.8326 | 2026-09-30 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| ab2aad7d-36e0-3e8a-b5e0-92cd899903b1 | -11.8602 | -50.9639 | 2026-09-30 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 54ac7422-0cb0-37b1-b5f9-6042e5f5109d | -7.8486 | -45.8138 | 2026-09-30 00:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 231.7 |
| cbb114b7-5a40-3d78-8534-214c5881786c | -2.9739 | -51.0455 | 2026-09-30 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 198.5 |
| 2e974ebc-f07c-3654-97e4-ed1aba5a37c0 | -5.7561 | -45.1747 | 2026-09-30 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 4566c7a7-93ca-3a02-8364-c351663715df | -10.5316 | -57.7747 | 2026-09-30 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 3255d9bf-00c1-3ac4-886e-bbaa390ffb73 | -2.974 | -51.0247 | 2026-09-30 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 144.2 |
| 76ef1950-7a69-30e9-be4c-f18ea74f5688 | -12.2515 | -50.2758 | 2026-09-30 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| f50c388f-59c9-370f-ba33-39c36959dc9d | -6.2311 | -42.4989 | 2026-09-30 00:10:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 38.1 |
| 986747b5-6b2d-3110-abb1-3b0f97ac1f32 | -6.212 | -42.5243 | 2026-09-30 00:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 228.1 |
| 0a51bd51-5d4e-33ee-bf9e-b1d1a916e2ff | -12.3085 | -47.9539 | 2026-09-30 00:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 177.1 |
| eace6a20-d973-30dd-a172-f5996c317427 | 3.2924 | -60.6101 | 2026-09-30 00:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 10b796d9-91be-3c5d-8701-b0492a2b7531 | -11.3277 | -51.0231 | 2026-09-30 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 36aeba1a-0200-3e13-bdcf-6b84b456237e | -11.7178 | -43.4623 | 2026-09-30 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 350c59cc-9956-3e16-9d42-2d962aa162c6 | -4.4507 | -47.9112 | 2026-09-30 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| c70b2435-323c-3413-998d-86f60b3b8519 | -11.3467 | -51.021 | 2026-09-30 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| a85466c3-1eb7-3351-9e89-6698a3986443 | -4.4506 | -47.9329 | 2026-09-30 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 104e48af-e4c5-3329-bfb6-4f8a4f92c91e | -6.2123 | -42.5006 | 2026-09-30 00:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 231.9 |
| e21b3fa3-2ded-3422-8b0c-d02240149cc6 | -6.895 | -43.7066 | 2026-09-30 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 112.6 |
| d093eb9a-b471-34a8-9f7a-9c41b9585ecf | -12.3089 | -47.9317 | 2026-09-30 00:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| a9c872a7-8aa5-37a2-a02b-1c59e212e4e9 | -8.2865 | -50.2731 | 2026-09-30 00:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 30eb3aef-a1bb-3642-9074-21e77c44c903 | -11.64 | -43.5218 | 2026-09-30 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.0 |
| f62cb9e7-45dc-3750-affd-bf3eb090cb06 | -11.8792 | -50.9617 | 2026-09-30 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 21f53637-56b7-387c-9064-69974988475d | -3.2315 | -46.9156 | 2026-09-30 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 9a3f2fbd-27ea-3a79-b5fb-62a7019776e2 | 3.2742 | -60.6105 | 2026-09-30 00:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 4e53cc4e-6a7c-3bfb-9fbd-ebcb249b431f | -6.1932 | -42.5259 | 2026-09-30 00:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 32.0 |
| d7859b04-b92d-3b47-a5ec-be5d431d11af | -11.6986 | -43.4654 | 2026-09-30 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| cea0bb6b-41f6-36d2-bcda-b1f739fd0ac8 | -3.2313 | -46.9596 | 2026-09-30 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 4a4c6d8b-d967-3156-b622-ea2e63fe6966 | -2.9556 | -51.0252 | 2026-09-30 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 0d9809d7-bd57-3640-8993-7b4a23170f50 | -2.9176 | -51.3169 | 2026-09-30 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |


[Clique aqui para ver as próximas entradas](README2.md)
