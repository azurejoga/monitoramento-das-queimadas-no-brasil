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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e06148c2-a58e-3a1e-bf3d-22827a20b953 | -4.76792 | -45.74165 | 2024-11-08 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 492cbd43-1ae1-3262-9d8b-4931ad1da7fc | -4.44953 | -45.92223 | 2024-11-08 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ea0cdd9-b118-38ae-9627-844c0ed0cfec | -4.37735 | -48.58421 | 2024-11-08 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d9fc1d7-7b70-3f2f-9771-6535917b4ab0 | -3.79261 | -44.02581 | 2024-11-08 03:57:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 482e0f1c-7922-3ea6-a1e0-396c45b99b36 | -2.5636 | -47.34161 | 2024-11-08 03:57:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dd86f19f-0fad-3b3a-84d9-8f58b5991e6d | -0.92531 | -47.13557 | 2024-11-08 03:57:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 299cccf4-3dc7-347a-8877-516c6f78acf4 | -1.98383 | -45.61535 | 2024-11-08 03:57:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b7299e7-3cd5-3754-b084-19c14db1ef18 | -3.94975 | -48.14935 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5b57187-9a55-3d30-9920-7f4850e634cf | -4.51097 | -45.68865 | 2024-11-08 03:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7bf3e3e8-cc22-38da-984d-3f79b7bccc29 | -3.37581 | -46.10791 | 2024-11-08 03:57:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b086aa2-333b-37fc-b822-acc66e99660b | -5.67429 | -41.75757 | 2024-11-08 03:57:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b6eb16bc-b5cf-3b6f-8d2f-b5b8ceade841 | -3.27875 | -45.80327 | 2024-11-08 03:57:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ecc20ce-4c5a-323e-9ae9-43c736904b96 | -4.50731 | -45.6839 | 2024-11-08 03:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 730dadd5-b99a-3f17-bfeb-c56495145e6e | -3.95695 | -48.17033 | 2024-11-08 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bc9c8c64-1ddc-3040-bc3b-1fe01727c24a | -5.54522 | -41.68766 | 2024-11-08 03:57:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cd9f32f0-3a8f-3e09-9fea-e140160f22db | -2.17292 | -47.56191 | 2024-11-08 03:57:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15276b73-d5e5-36d1-830c-27e0584b1f08 | -1.22028 | -46.52747 | 2024-11-08 03:57:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb29833a-86be-364a-8409-d0472a79e2d4 | -4.78826 | -45.40834 | 2024-11-08 03:57:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef04f612-f4f6-3daa-9ee0-6c90b2ec8f2d | -4.37734 | -47.22735 | 2024-11-08 03:57:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc6d64f5-b278-3fca-861e-fc34d989ebd3 | -3.71984 | -40.70886 | 2024-11-08 03:57:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cce54c17-cc64-3736-835e-9c2cb79c5152 | -2.63577 | -46.77736 | 2024-11-08 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1734721-8e77-3008-8d9c-bbf80a537cdd | -8.30479 | -43.6046 | 2024-11-08 03:59:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3a7fc37-8b94-36f0-b231-53e012879a6b | -5.94506 | -43.77549 | 2024-11-08 03:59:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8306ecd3-d85b-331b-9e70-514f6c014974 | -5.63531 | -46.96957 | 2024-11-08 03:59:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c666650-b502-346b-82bf-0eabd49ce505 | -4.92161 | -48.52201 | 2024-11-08 03:59:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41d33099-3547-3d23-8a56-e2a3f612f664 | -5.68213 | -46.32533 | 2024-11-08 03:59:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a009ca20-1c24-3fe4-8293-174aa386898b | -7.24171 | -45.11963 | 2024-11-08 03:59:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac0907e2-5473-3a2b-9de2-afc002598c9b | -9.0477 | -38.23649 | 2024-11-08 03:59:00 | NOAA-20 | PETROLÂNDIA | PERNAMBUCO | Brasil | 2611002 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 98361197-f297-3508-ae5a-cd2f8fdd11b4 | -5.84842 | -45.31701 | 2024-11-08 03:59:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a45a7a10-e26e-383f-becb-e652d90f69ce | -5.5364 | -46.35674 | 2024-11-08 03:59:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0f94353-cfdc-3f5c-a1c9-dd975d17ad7c | -11.72582 | -38.33675 | 2024-11-08 03:59:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4c34f08d-cf86-36c1-9289-e295423ecc1f | -10.72716 | -49.82828 | 2024-11-08 03:59:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 036214d7-d0ef-369a-b966-e3e11a7027ce | -8.57699 | -40.37931 | 2024-11-08 03:59:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0366ef70-1925-3996-b1c5-e7dd0824c681 | -5.07953 | -47.93567 | 2024-11-08 03:59:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c75ff4c-1322-37ce-aadf-4b3271dbfec7 | -6.27997 | -44.73558 | 2024-11-08 03:59:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 554f95e0-7e4e-3dcb-b686-eba05d0bf004 | -10.72139 | -49.83043 | 2024-11-08 03:59:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2a216b6-d610-3187-a0c0-75e303e2adab | -6.08346 | -44.71869 | 2024-11-08 03:59:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99fa17a4-4ab4-32c0-8f32-fb8c99adf39f | -6.29529 | -42.03843 | 2024-11-08 03:59:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 31284012-3706-3a9a-bf28-7e78d91e338f | -5.68855 | -46.4383 | 2024-11-08 03:59:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c14cbfb7-2513-31dc-b492-469d253cec43 | -6.14894 | -42.50879 | 2024-11-08 03:59:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d2a00ac4-dc88-3dd9-9541-79e478705c26 | -6.07753 | -44.72002 | 2024-11-08 03:59:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 814d37af-9956-3381-b5ad-72147aebc7df | -6.74359 | -47.14682 | 2024-11-08 03:59:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6956af41-b9b6-3ceb-9c18-96630fe26ea9 | -9.57768 | -37.81551 | 2024-11-08 03:59:00 | NOAA-20 | PIRANHAS | ALAGOAS | Brasil | 2707107 | 27 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0b258bce-645e-31a3-a8fb-00ea31e9862b | -5.99684 | -46.08866 | 2024-11-08 03:59:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc14674d-6173-3a2a-b42c-eb355203e580 | -6.85246 | -38.89314 | 2024-11-08 03:59:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c944234f-3652-39ff-ac12-af3dc01bec69 | -6.16623 | -43.59069 | 2024-11-08 03:59:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5fee3e63-aa76-38c2-9713-2919da19c1fe | -10.72079 | -49.83361 | 2024-11-08 03:59:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 077425e2-ad41-3425-9e90-119009182571 | -10.73173 | -49.83247 | 2024-11-08 03:59:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd5a5c8d-73dd-3466-8a9f-9b716ee914cb | -5.99175 | -46.09224 | 2024-11-08 03:59:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03faafd9-6c82-37f1-8aab-f9a1d3029e30 | -7.02625 | -44.84415 | 2024-11-08 03:59:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d88a228b-ce98-372d-a302-b1451cd099f4 | -7.85606 | -43.78255 | 2024-11-08 03:59:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6a951b8a-5d08-3622-bfff-596f6a9edfed | -6.08151 | -44.72065 | 2024-11-08 03:59:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4f7369c-ad62-32fa-8cf1-c67c1dcd8da6 | -5.37571 | -46.26929 | 2024-11-08 03:59:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bf9e908-a350-3e02-b4bf-476aec260588 | -6.23023 | -46.23017 | 2024-11-08 03:59:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe83caf0-f381-34bc-9ab6-25599cacdfc8 | -5.07903 | -47.93866 | 2024-11-08 03:59:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8efc5b43-cec7-3a10-9a59-5bfa0f4db790 | -11.86719 | -38.35581 | 2024-11-08 03:59:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 93e3cc78-2bac-3d70-8a43-48973db045f3 | -8.57542 | -40.4324 | 2024-11-08 03:59:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a0b0683f-d08c-3f88-8f9e-1eea7b3720cf | -5.99103 | -46.09649 | 2024-11-08 03:59:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e3ddf20-6a93-3d70-87de-f78f13ffae96 | -6.74572 | -46.91798 | 2024-11-08 03:59:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e4af198-a4f1-3b50-903f-f8c58eb2e903 | -7.03107 | -44.83976 | 2024-11-08 03:59:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96bb5b3f-11a8-356a-8774-efc521dccd48 | -7.02762 | -44.84261 | 2024-11-08 03:59:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 61694d50-7e52-3b59-bb1b-5dfa2cd74d7b | -5.07853 | -47.94162 | 2024-11-08 03:59:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21181c9c-883a-3525-a310-79703b048a28 | -9.75083 | -43.57893 | 2024-11-08 03:59:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 463c763b-b747-3609-865d-016616a3fe30 | -6.39707 | -47.14278 | 2024-11-08 03:59:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5d47f068-3404-35e5-9a6e-b5945c84121a | -7.18087 | -37.91681 | 2024-11-08 03:59:00 | NOAA-20 | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d97edc60-0f2c-31e8-90ea-e34773c3ba9d | -11.49343 | -39.04802 | 2024-11-08 03:59:00 | NOAA-20 | TEOFILÂNDIA | BAHIA | Brasil | 2931509 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ea2926a1-cdac-39a5-8388-15b97b0c9a45 | -6.74438 | -47.14916 | 2024-11-08 03:59:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7ced887-da3b-3b74-806c-f168d08e5797 | -6.23461 | -46.23099 | 2024-11-08 03:59:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e2cb0b6-cd7e-37d4-9bc5-c143d5e60bea | -6.8558 | -38.89368 | 2024-11-08 03:59:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 84259344-a17f-331b-b9f0-333f69f5f8df | -6.49771 | -39.55803 | 2024-11-08 03:59:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 52a5cdb2-6b72-33f6-a1b1-fdf2a383af6e | -11.06383 | -38.439 | 2024-11-08 03:59:00 | NOAA-20 | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4e8538f7-85fe-3297-9285-e673a269ca60 | -8.25913 | -43.86086 | 2024-11-08 03:59:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7ab26709-c33f-346c-bac5-f57fdd4f6138 | -5.93087 | -43.65228 | 2024-11-08 03:59:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 72e3e47c-ce4c-37fd-bc34-7d5f802f566e | -5.59036 | -45.20588 | 2024-11-08 03:59:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24b6310c-8388-355b-89d6-cd5e8835448c | -7.54664 | -44.08866 | 2024-11-08 03:59:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 783596b3-2ed8-3418-be04-eb0a0f088de8 | -5.64221 | -44.24495 | 2024-11-08 03:59:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 59831f31-3105-3df9-86f8-2db95913c3bf | -5.6461 | -44.24556 | 2024-11-08 03:59:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 968f76b9-8016-3e79-869a-aefab19be086 | -4.92107 | -48.52509 | 2024-11-08 03:59:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8a766a26-12a9-37db-bd45-e1c235959fe1 | -7.24052 | -45.12669 | 2024-11-08 03:59:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3212af4-e68b-3391-895b-83121e4beaca | -6.37914 | -39.25109 | 2024-11-08 03:59:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5a50918b-f513-311f-acba-199b5531823d | -5.94431 | -43.78006 | 2024-11-08 03:59:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 29e3ee95-8e0a-3ba6-b01a-afbc61b1e01a | -12.72194 | -38.26693 | 2024-11-08 03:59:00 | NOAA-20 | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 574947ad-0ab1-3abf-b469-782ea3d02df4 | -5.37201 | -46.26392 | 2024-11-08 03:59:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf19110d-ad43-315d-9fd0-94a0c851f535 | -10.72199 | -49.82726 | 2024-11-08 03:59:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23fb5d9c-b2f1-3362-8a54-21616ec70674 | -5.43749 | -46.35629 | 2024-11-08 03:59:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8bbea3c2-e643-33dd-b037-a76f07cf4593 | -5.68691 | -46.43559 | 2024-11-08 03:59:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 37372177-8cf1-3aef-8f33-f101018fa2f7 | -6.75474 | -39.2596 | 2024-11-08 03:59:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7941f646-f4f3-3361-9beb-f58159c6c6cd | -5.9806 | -45.36498 | 2024-11-08 03:59:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 8f077ac6-0a71-38a9-bd70-ba257c572f57 | -5.96746 | -45.36692 | 2024-11-08 03:59:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73f8edf0-0101-365b-bf2d-11d344624f2d | -5.9413 | -43.77491 | 2024-11-08 03:59:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0bb19a99-61ff-35b7-8520-518042e61acc | -5.92996 | -43.65044 | 2024-11-08 03:59:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9deff22d-c842-3777-b6f4-5face16d8062 | -5.98412 | -45.36943 | 2024-11-08 03:59:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 3f30ead5-413a-3f3c-b0a7-bae4a260d678 | -5.66143 | -46.65032 | 2024-11-08 03:59:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 078a4fcd-a986-30aa-97a1-94c272a08ce0 | -4.98646 | -49.90316 | 2024-11-08 03:59:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc6c2d77-4cf1-3325-9de2-8ba627fdff1a | -5.68933 | -46.43375 | 2024-11-08 03:59:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 487333db-2796-3d28-a83f-3db67cb5d38c | -6.72007 | -46.07823 | 2024-11-08 03:59:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c5ec3b1b-2f71-302f-bb7e-f39e9b06ff95 | -6.23096 | -46.22582 | 2024-11-08 03:59:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ff95623-c56a-3d8a-bcb2-4cb2d9d261b3 | -11.72936 | -38.33728 | 2024-11-08 03:59:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d87ae086-ebe5-3c21-93c8-aa1106f2ee80 | -7.96779 | -37.85106 | 2024-11-08 03:59:00 | NOAA-20 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 729299a9-6de3-35d1-bbdf-692600b76262 | -6.07949 | -44.71803 | 2024-11-08 03:59:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README18.md)
