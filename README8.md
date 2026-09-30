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
| 3ef1e2e3-4f8f-38be-a70f-4578e9dc0e82 | -8.2865 | -50.2731 | 2026-09-30 02:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 956b3376-6893-30c0-97b4-52513ee63f9a | -2.8898 | -54.1112 | 2026-09-30 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 9677f7c4-f982-37f5-a0e8-2208c535a4b0 | -20.5138 | -49.6289 | 2026-09-30 02:50:00 | GOES-19 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 023d4df6-7f24-3f87-b835-d5eb08365a0a | -2.9082 | -54.1108 | 2026-09-30 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 8f6d0d34-9b7b-3fae-ab02-fe992f9ad4d8 | -7.8297 | -45.8156 | 2026-09-30 02:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 5878d2e2-b0f6-3263-b1f8-1bcb3480556d | -5.7561 | -45.1747 | 2026-09-30 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 35.4 |
| c6b1c0da-36cf-314b-bf14-977a9e4ea32b | -9.9215 | -50.1682 | 2026-09-30 02:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 3ff061c7-d4ee-304d-a0c5-c81875126bc1 | -9.9218 | -50.1468 | 2026-09-30 02:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 8a3be188-3c4d-3084-ac43-1f0fee1f15a3 | -2.9082 | -54.0907 | 2026-09-30 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 20ccd608-2228-3622-9ab6-3f39996d3d4b | -2.9739 | -51.0455 | 2026-09-30 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 126.3 |
| d9d4fee9-7c5f-3775-bae8-3c79baf45157 | -7.8295 | -45.8381 | 2026-09-30 02:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| ebbed2fe-017e-3112-a63d-2fd6aea21c2f | -6.0739 | -47.2922 | 2026-09-30 02:50:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 5abc8829-f2f5-3b03-8ed7-cbe7ad6c14c1 | -2.9924 | -51.045 | 2026-09-30 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 28a95a4d-9aae-32b8-bbd1-4d02d7bcee2f | -7.8109 | -45.8173 | 2026-09-30 03:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 37134125-a9b4-32b4-a4e5-12b896c0c0e9 | -7.8295 | -45.8381 | 2026-09-30 03:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| f39975df-dfe1-3b1d-9adb-0568897aed8c | -7.8483 | -45.8363 | 2026-09-30 03:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 08aae12c-353e-3fb0-8845-1890b76bb2db | -3.2314 | -46.9376 | 2026-09-30 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 5f5cfbab-c815-35fe-ae0e-0f09d4e15e13 | -2.974 | -51.0247 | 2026-09-30 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 53b11fe3-b03c-367a-932e-4c7b3c258850 | -2.9739 | -51.0455 | 2026-09-30 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 125.4 |
| 53fca5a7-17cf-3a4a-bf7c-0a5b052af9f6 | -7.83 | -45.793 | 2026-09-30 03:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 7905ad79-80d6-37c8-bb29-727d63481bc5 | -12.3085 | -47.9539 | 2026-09-30 03:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| c9687a9a-8afd-3097-b940-d5c6d8149f78 | -3.2129 | -46.9383 | 2026-09-30 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 5849e9ff-500a-310d-b17e-ad37490b32bc | -2.9082 | -54.0907 | 2026-09-30 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| dc665b39-81b0-3cdf-bd86-a8f2bdb4a984 | -2.9924 | -51.045 | 2026-09-30 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| ea33e4c6-f060-3ebe-9abb-c8556a81c044 | -5.7561 | -45.1747 | 2026-09-30 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 41d69bdf-e6a2-3f54-9ec3-eec7c8f08102 | -11.811 | -50.4356 | 2026-09-30 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 9f5578ee-ba28-315a-b31d-c19c24b47b00 | -7.8486 | -45.8138 | 2026-09-30 03:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 91cd8a11-6c6e-31a2-9308-3e7d445bdbb8 | -7.8297 | -45.8156 | 2026-09-30 03:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 8c24ba34-b3c9-3204-b6d4-fe013b5b4721 | -12.3085 | -47.9539 | 2026-09-30 03:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 2b4fb928-0a83-38b1-8098-b1ea97d68876 | -5.7561 | -45.1747 | 2026-09-30 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| b0b0b4b2-21c7-3c40-a0c5-8b3dc1e108ee | -11.83 | -50.4333 | 2026-09-30 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| e4efe61b-a33e-30b9-bac3-4ec02c7e167b | -2.974 | -51.0247 | 2026-09-30 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 17f81219-29ae-30bd-9d1d-93457f16d628 | -3.2314 | -46.9376 | 2026-09-30 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 15eb51bb-77e3-33b8-85a0-90450f0cc593 | -11.8107 | -50.457 | 2026-09-30 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 1c9aac16-013e-3e88-92c5-dbeeb81db15a | -2.9924 | -51.045 | 2026-09-30 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 681f7590-bf20-3a7b-a4c3-48e1f5e11dad | -3.2129 | -46.9383 | 2026-09-30 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 578c31a2-1a6e-3e71-801a-8704f97ac219 | -2.9739 | -51.0455 | 2026-09-30 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| dcfafb36-4fd8-36bf-80c9-58a6f5528b86 | -12.9813 | -51.2359 | 2026-09-30 03:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 9daf6f9e-25cc-3e0f-ab04-14f67bf3f7b4 | -11.811 | -50.4356 | 2026-09-30 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 1f3ccbb9-6dda-3f63-bbc6-4e0be8b9c660 | -2.9082 | -54.0907 | 2026-09-30 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 69c880c7-f65b-351b-8656-4685d3eebe07 | -10.21642 | -36.30682 | 2026-09-30 03:10:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 334b5e3a-2392-34a2-805f-765cd5d3faa0 | -10.21101 | -36.30573 | 2026-09-30 03:10:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| 7224de5f-d674-3d57-9337-6ee793fea736 | -10.2056 | -36.30462 | 2026-09-30 03:10:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| fb14fbe4-be7b-3cec-9eda-edebbe7a70ea | -10.21168 | -36.30221 | 2026-09-30 03:10:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 22.2 |
| a89a296c-c162-3c98-9391-527bb038313a | -10.20968 | -36.31274 | 2026-09-30 03:10:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f940c6f1-d2b6-3116-9b5e-4e0be4bb1153 | -10.49744 | -36.97591 | 2026-09-30 03:10:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a30d858a-d264-31fd-b035-19fcb4e13706 | -10.21034 | -36.30923 | 2026-09-30 03:10:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| 802e8c92-08e8-32e3-8195-60c2f51e9769 | -18.3055 | -42.2191 | 2026-09-30 03:13:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 938885a7-c46f-3432-93ce-b94afccbaf65 | -18.30679 | -42.21355 | 2026-09-30 03:13:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d5beff3d-424e-3f12-8596-0e0154d710a3 | -16.67361 | -41.85319 | 2026-09-30 03:13:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d6274d00-eee6-3432-903b-21a520458e3b | -17.70764 | -42.05735 | 2026-09-30 03:13:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 6a70b327-41f7-3aee-9f26-b7f2e01bcb93 | -16.67202 | -41.86023 | 2026-09-30 03:13:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b322a07f-bdd3-39cb-8133-a2204dd0383f | -18.29607 | -43.33128 | 2026-09-30 03:13:00 | NOAA-20 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3fc27946-8bb8-32a3-bb23-d6b6a424434e | -18.11278 | -40.34321 | 2026-09-30 03:13:00 | NOAA-20 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c9f5c72e-403a-3bbe-9690-c04f35d81f94 | -14.20224 | -42.07551 | 2026-09-30 03:13:00 | NOAA-20 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 0debb4ae-9922-3458-9501-18717532bfcb | -14.20061 | -42.0828 | 2026-09-30 03:13:00 | NOAA-20 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 783b784f-367c-3a65-b902-dcc44fdd237c | -2.974 | -51.0247 | 2026-09-30 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| fb02d65c-418d-3fd4-a99e-66bc993a6ce6 | -5.7561 | -45.1747 | 2026-09-30 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 3be229c1-a62c-387d-8e54-9dd0cbf58cb4 | -7.8486 | -45.8138 | 2026-09-30 03:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 43.3 |
| a0dcc649-2031-3a77-b35d-00aeefef01d9 | -3.2129 | -46.9383 | 2026-09-30 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| af303a87-49fe-36a6-ad60-dfb40ef08135 | -2.9082 | -54.0907 | 2026-09-30 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| a720518c-3177-355e-a72b-8429c6544d0a | -2.9739 | -51.0455 | 2026-09-30 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 6c9b9411-ffe2-3aaa-9857-e2c98e816de6 | -12.3085 | -47.9539 | 2026-09-30 03:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 2b1dd6fb-76e6-33e1-a157-1704c13fd54d | -2.9924 | -51.045 | 2026-09-30 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 661afdce-2ea4-3339-8163-80b053550c46 | -6.895 | -43.7066 | 2026-09-30 03:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 6e2d321f-a412-3bcf-83fa-0993f37e0c1a | -2.9082 | -54.1108 | 2026-09-30 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 5065caf1-50cf-35ea-ae9a-b5737934568b | -14.1314 | -46.2571 | 2026-09-30 03:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 60.5 |
| ea2fc1a1-eb86-3a00-b474-8ccfb9540ea0 | -3.2314 | -46.9376 | 2026-09-30 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 30ce4b53-88df-342d-95f9-79b76ad52554 | -2.8899 | -54.0912 | 2026-09-30 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| d2b45fa4-a049-37ac-8e6f-73a134b4d873 | -2.9924 | -51.045 | 2026-09-30 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 7ad3e25a-7b79-3e74-91ad-cf17b753707f | -2.974 | -51.0247 | 2026-09-30 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 556b22f1-7d26-30bb-b994-86a078b08edb | -3.2313 | -46.9596 | 2026-09-30 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 8a874585-6511-36c9-9164-aa312ab86d35 | -11.8107 | -50.457 | 2026-09-30 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 96ebb944-c45e-3257-b071-e7553acbe4a7 | -11.8297 | -50.4548 | 2026-09-30 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 291992ae-76e4-3ad5-b2bd-3672bbf9430e | -6.0739 | -47.2922 | 2026-09-30 03:30:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 24759fd0-0180-31b6-92a5-5e67445e9f92 | -12.3085 | -47.9539 | 2026-09-30 03:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 6049ab2c-aef9-3ae1-a474-2204b1344c5a | -7.8297 | -45.8156 | 2026-09-30 03:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 74153b1e-2287-3523-a416-e3ffe79f469f | -6.895 | -43.7066 | 2026-09-30 03:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 16e13aa1-8d61-34a5-b933-f0a13de4ae20 | -7.8486 | -45.8138 | 2026-09-30 03:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 88a20ef8-6805-3fd4-b371-ec21fc5ecd9f | -9.9218 | -50.1468 | 2026-09-30 03:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 199b4179-e247-3252-9224-e611035816c7 | -2.9739 | -51.0455 | 2026-09-30 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 2db77e26-e532-339b-b704-bb747b254c09 | -5.7561 | -45.1747 | 2026-09-30 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| d7685a2d-0c58-34c2-8e27-4285d689599b | -7.8483 | -45.8363 | 2026-09-30 03:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 25473298-7c46-384d-9196-e6fd40931752 | -11.811 | -50.4356 | 2026-09-30 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 913b59ae-537d-3600-9bca-13c39234958d | -3.2314 | -46.9376 | 2026-09-30 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 0d3063e0-f585-3f32-9e60-7e026662d309 | -2.9082 | -54.0907 | 2026-09-30 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 41ec8af8-5e9c-3e08-a189-0667ebe2db71 | -7.8295 | -45.8381 | 2026-09-30 03:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 35b03797-557c-3c7a-a3c4-e76bf2c9aae5 | -5.7561 | -45.1747 | 2026-09-30 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 1ebacff6-9395-3121-8f01-61badf837b43 | -14.1119 | -46.2604 | 2026-09-30 03:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 0e480254-9d2e-359a-9168-d50760482169 | -7.8483 | -45.8363 | 2026-09-30 03:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| ae6072d7-65a6-3415-af07-af4e2d69d790 | -2.9082 | -54.0907 | 2026-09-30 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 72aa0833-5c70-32c3-9c0c-0f7eb5749c7e | -20.5138 | -49.6289 | 2026-09-30 03:40:00 | GOES-19 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 78.1 |
| aec18134-d0ce-3cdc-9fe6-be4ccc7a7183 | -12.3085 | -47.9539 | 2026-09-30 03:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 11149341-7d40-31ed-b445-3ac2f5f5a5d3 | -2.9739 | -51.0455 | 2026-09-30 03:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| df0107bf-b37e-3a8f-9100-df0eca0ccaf6 | -6.895 | -43.7066 | 2026-09-30 03:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 73.5 |
| df0caf8a-d27d-3b9e-9c4b-c803cbb22afc | -2.9924 | -51.045 | 2026-09-30 03:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 51a3da2d-d543-3683-9326-670b1b88311f | -7.8109 | -45.8173 | 2026-09-30 03:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| acd2d3eb-5027-3379-a79a-7b4345a7e2f3 | -11.3853 | -50.9743 | 2026-09-30 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 3336440d-d8ad-3eba-b1f0-a4bd24e2d5da | -7.8295 | -45.8381 | 2026-09-30 03:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| fa191f76-875c-3597-abdd-cddb73adb6f8 | -3.2314 | -46.9376 | 2026-09-30 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |


[Clique aqui para ver as próximas entradas](README9.md)
