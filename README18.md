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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a532b0d-bbfd-3a46-abfb-4179a90bfac8 | -5.84982 | -46.72789 | 2025-07-16 04:14:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e764cdf-164d-3a3b-baac-82231adf18f2 | -7.90179 | -55.42488 | 2025-07-16 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| caf1082e-441c-38da-be27-be6f70b23942 | -7.19257 | -43.1222 | 2025-07-16 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 65bd0d9f-f33d-3672-b3d7-01d063241be7 | -12.47299 | -46.92285 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a07410f0-7976-340b-9aea-e7eac0e3eabb | -13.01992 | -45.05431 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 39d34433-d522-3392-bb22-859ab012992d | -6.71565 | -44.33147 | 2025-07-16 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 60543f2e-c797-3f7b-b5de-e482b34683be | -7.04511 | -43.4781 | 2025-07-16 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c425d96f-d5a0-363f-aa85-12a979b91854 | -7.18927 | -43.12169 | 2025-07-16 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 756d5995-a7f8-36a3-932b-6ee4d6907e0c | -6.91409 | -52.85322 | 2025-07-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 78b3c645-e80b-3dfd-a47d-d8b0438599c1 | -12.99371 | -44.87655 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa9f2647-a212-3edf-87c6-9f5026fdbc83 | -7.899 | -55.4227 | 2025-07-16 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f46052d6-d5d8-380f-8f92-520dffaaba90 | -12.49374 | -46.9264 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b4a7313e-0cf0-3b6a-b497-4398468ce678 | -6.43744 | -44.96821 | 2025-07-16 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97c17f97-76af-394f-94ee-dc589b276a66 | -7.27209 | -45.29696 | 2025-07-16 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0bf0f07-c18c-3927-850a-8418a460fe6b | -12.5633 | -48.88962 | 2025-07-16 04:14:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d502d51-b42a-3572-b99b-afe5ebfcd12e | -8.91021 | -47.34813 | 2025-07-16 04:14:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9278029-804d-3617-bf4b-b378921b6a6b | -8.91681 | -47.35371 | 2025-07-16 04:14:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c648b51-cb67-3c50-bb66-3fdf50cbcba8 | -8.9508 | -49.83951 | 2025-07-16 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86346e05-955d-3ab5-83df-6ce879d56c13 | -6.87343 | -41.73224 | 2025-07-16 04:14:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1c592255-872d-326e-9961-a574a0ac7134 | -12.48055 | -46.92015 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09974eb8-4d9d-39f5-97ee-ceff3fde092d | -6.84999 | -44.80624 | 2025-07-16 04:14:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9f2c234e-e74a-3b07-b371-f5f442e1af3f | -12.07427 | -43.47735 | 2025-07-16 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ed4cadc0-01a4-3795-a6ae-ffc70bb03e34 | -11.48519 | -43.22701 | 2025-07-16 04:14:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 57996f5d-b7f5-3813-9455-5d561c2b4b11 | -12.03703 | -48.76339 | 2025-07-16 04:14:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc15be6c-fa17-3337-a888-82fd35a3833e | -7.50664 | -46.68235 | 2025-07-16 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4047759c-afdd-313a-9159-fff6e9fb0f2e | -6.70678 | -44.32283 | 2025-07-16 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 21e2ef61-9fe8-3873-ba89-57bf521eb42c | -11.78078 | -45.21684 | 2025-07-16 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5214d842-43a6-332c-8b92-986c527c8da6 | -11.26787 | -44.89714 | 2025-07-16 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69a64aad-4bfa-390a-9871-1077a85c1a9a | -11.46851 | -47.30713 | 2025-07-16 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2c79ee0-3409-3ff7-ba28-dd02a25afdd8 | -8.24591 | -44.91861 | 2025-07-16 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 32851534-eb1c-3842-b828-ff96ee00f606 | -11.45454 | -45.09058 | 2025-07-16 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79da074f-fb1b-33d2-a309-762fec6ae44e | -13.02155 | -45.06543 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 731c4fe8-47b9-389e-bb59-a7421a82ef86 | -8.54041 | -47.85384 | 2025-07-16 04:14:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e36b7dc-05ad-387a-a90b-958f8c1dc756 | -8.68293 | -51.45721 | 2025-07-16 04:14:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa50ce2a-c445-3d61-9b3c-1bf9f04c3a7b | -11.94904 | -48.41371 | 2025-07-16 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ba031254-60e2-3d1c-a131-50e6a0abb370 | -8.91095 | -47.34379 | 2025-07-16 04:14:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b6c913c-ebb9-3eb7-baf1-043f3452a69d | -12.99426 | -44.87303 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb0624b4-f7cd-359d-b3a8-8c6a4b937a6d | -13.12757 | -43.4863 | 2025-07-16 04:14:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4e02c992-642a-3b86-be36-a9a7ffa2dc40 | -12.03562 | -48.76585 | 2025-07-16 04:14:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b0f3d4c-d609-376f-bcff-d2580656993c | -14.1581 | -42.84243 | 2025-07-16 04:14:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 55d0fd61-02b1-3373-bfe9-605ea3cb9c98 | -6.37746 | -44.74961 | 2025-07-16 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1501decf-8511-346c-975c-cbb5c55b44cb | -7.27609 | -45.2938 | 2025-07-16 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b16af06a-6024-37a3-bf43-64e43f805e6a | -9.29512 | -44.84398 | 2025-07-16 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4cad6f87-9075-37dc-8635-a8275d24d8d0 | -13.02379 | -45.05133 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 841f3138-6eae-39dc-99da-616c61d59713 | -9.58985 | -40.35978 | 2025-07-16 04:14:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b2b807fc-e172-3fd2-9ffa-aa9f5c52f903 | -12.4771 | -46.91956 | 2025-07-16 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 075a07fe-c0c9-3e7d-bfa3-6794fcde3f4f | -13.01936 | -45.05783 | 2025-07-16 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 45bc82e2-60c0-3db7-a4f3-01cd5b313fda | -11.73902 | -48.52843 | 2025-07-16 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1f4023d7-ee68-31b2-9588-7e0bb3918111 | -7.59517 | -46.32593 | 2025-07-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0849980a-4daa-31b5-863e-fdb4a295a990 | -10.31887 | -49.9194 | 2025-07-16 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96b5e0d3-ea82-33fb-ba91-8846d4ed1f93 | -18.59409 | -52.40781 | 2025-07-16 04:17:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 250ef2f7-cf6f-3881-a516-8426aab777b5 | -20.02907 | -47.39441 | 2025-07-16 04:17:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 348f110f-254b-320b-aea3-d31ca8281e6f | -16.98421 | -52.00684 | 2025-07-16 04:17:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae3486f3-0e94-34c9-acd8-006e76b10976 | -20.34898 | -46.54648 | 2025-07-16 04:17:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 534458bb-387c-3b06-9bc0-d100b2bf265a | -21.95298 | -57.58556 | 2025-07-16 04:17:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c918a422-d814-31e7-ac78-6a430f57c6aa | -22.55889 | -54.9552 | 2025-07-16 04:17:00 | NOAA-20 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| f1a8364b-85d2-3401-9c79-1655f1511d4c | -20.4109 | -46.6054 | 2025-07-16 04:17:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12d1a430-fc60-3943-80c4-1235ce532170 | -20.08277 | -47.64653 | 2025-07-16 04:17:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d381766-6b4c-390f-911d-b08654e22e76 | -19.42874 | -49.20308 | 2025-07-16 04:17:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7f9f738-db1b-3129-afb4-76b6c5de4d9b | -21.95384 | -57.58949 | 2025-07-16 04:17:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90505dbf-4fd7-3030-ae4a-4536331aed59 | -20.35559 | -46.54765 | 2025-07-16 04:17:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 966ee78e-1296-3449-be11-2190483b14b1 | -20.02241 | -47.39315 | 2025-07-16 04:17:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55ba1b54-c85f-3925-98db-50a26bedad93 | -16.26349 | -43.80518 | 2025-07-16 04:17:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.0 |
| d377d74c-f3e7-37d1-a5f5-b048f79adba2 | -23.61069 | -49.00596 | 2025-07-16 04:17:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 119074aa-de70-36ff-8229-1113af2407af | -19.53076 | -49.67419 | 2025-07-16 04:17:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9f9411be-d241-39e1-b7f1-876908a850e2 | -20.9623 | -43.96852 | 2025-07-16 04:17:00 | NOAA-20 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 48909346-85c5-309a-9b0c-fa6cd768f245 | -20.08065 | -47.63851 | 2025-07-16 04:17:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 597ae6e1-e064-3211-befe-7734569f9aa6 | -20.084 | -47.6391 | 2025-07-16 04:17:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 6f0486d2-1dcb-3215-8fe9-3ac1780d00f7 | -21.95294 | -57.59354 | 2025-07-16 04:17:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4864c74-1bdf-32c4-bf52-309e6298b6e8 | -22.65849 | -53.38015 | 2025-07-16 04:17:00 | NOAA-20 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| af18e296-8b26-3ade-958b-c3d2ef1ee38b | -13.15782 | -50.77407 | 2025-07-16 04:17:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c9f80146-31fc-3576-a701-2d71957712d6 | -13.16279 | -50.77084 | 2025-07-16 04:17:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d8fcd235-63ef-3378-9a4e-de8dff8be712 | -14.58995 | -48.11665 | 2025-07-16 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88a8ba6a-004d-3622-b36e-6f1e3542b2e8 | -20.50899 | -47.41481 | 2025-07-16 04:17:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 694e0866-0982-33e4-9c1d-74e711b514e1 | -18.59063 | -52.40271 | 2025-07-16 04:17:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55059eff-338e-385f-a39a-c9edf083eac2 | -25.39217 | -49.61199 | 2025-07-16 04:17:00 | NOAA-20 | CAMPO LARGO | PARANÁ | Brasil | 4104204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1af43688-ca79-3de3-b646-720cce6552fe | -14.6036 | -48.66911 | 2025-07-16 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b013f08-f7bd-3fbf-b0d0-c9eabf8ba329 | -20.3586 | -46.59234 | 2025-07-16 04:17:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 286d153b-a327-3819-a4da-64a6f6cd9d31 | -22.56109 | -54.94472 | 2025-07-16 04:17:00 | NOAA-20 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| 48088f21-62dc-39b5-af22-512add738a7b | -21.16066 | -43.76224 | 2025-07-16 04:17:00 | NOAA-20 | ALFREDO VASCONCELOS | MINAS GERAIS | Brasil | 3101631 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3136b803-6830-3ad6-819e-71b92f8f1042 | -20.35802 | -46.59601 | 2025-07-16 04:17:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4906dfd2-516d-381d-a236-7727b6b62d19 | -14.91733 | -46.96374 | 2025-07-16 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36630caa-b287-3900-958e-4f757c696ff2 | -23.5753 | -51.42274 | 2025-07-16 04:17:00 | NOAA-20 | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d4f792d1-b6a6-3b04-918e-772b20da0178 | -24.95032 | -53.41235 | 2025-07-16 04:17:00 | NOAA-20 | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9b2853b0-5f4c-3616-9ce3-02571d3edf90 | -15.33583 | -49.46312 | 2025-07-16 04:17:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 82829de7-1ecf-320c-93c9-613f8b7ce61b | -17.50013 | -45.17846 | 2025-07-16 04:17:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fb23bc9-f2d2-3158-ba09-30fa5d99437e | -20.07668 | -47.64164 | 2025-07-16 04:17:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 3b8ec89d-73d0-3545-86b2-2aa1b8440279 | -21.95202 | -57.58972 | 2025-07-16 04:17:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6e5789f-c2ee-3b14-98ae-62994b6eef23 | -20.08598 | -43.9125 | 2025-07-16 04:17:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 154a0be6-e919-357e-9df5-cba91edd1e3a | -22.55755 | -54.93838 | 2025-07-16 04:17:00 | NOAA-20 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| 4a04025a-2861-317e-97b9-ec7c8c40b7c8 | -17.60307 | -47.00877 | 2025-07-16 04:17:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed03933d-dd75-319c-a912-ab9ce098d2bc | -22.56219 | -54.93952 | 2025-07-16 04:17:00 | NOAA-20 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| ad31ab4a-9f85-3eb9-b995-905fb6f49ca9 | -17.53067 | -55.64131 | 2025-07-16 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 31a07e8c-12e0-35fd-a17d-17335bec81dd | -17.5945 | -43.19771 | 2025-07-16 04:17:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a836a1b6-3761-395a-8149-a9c4d61e113b | -17.85545 | -51.70811 | 2025-07-16 04:17:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c47ab5dd-02c7-318e-bd82-5e0e84d8734d | -18.5949 | -52.40361 | 2025-07-16 04:17:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8055075-29ed-3be9-b1db-1872b03bc024 | -20.0907 | -47.64029 | 2025-07-16 04:17:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5bbbad1e-ea2d-3beb-bcf7-e85c85563786 | -21.95936 | -57.59089 | 2025-07-16 04:17:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5aac58fc-18b1-36b4-b9b9-f8075c8d450b | -23.46518 | -50.95888 | 2025-07-16 04:17:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 51da43d0-21dc-30e7-97c3-945cbf5a853c | -21.13885 | -47.72502 | 2025-07-16 04:17:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README19.md)
