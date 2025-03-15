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
| b0115f5c-ad24-3ab1-95f7-62efb5bb6fbb | -16.47882 | -54.17179 | 2025-03-15 04:19:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1b27314-c052-3b54-a47c-d67f0a330de2 | -4.81704 | -42.98431 | 2025-03-15 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8404204-85a4-3c6d-87e6-ec71625356d5 | -15.60243 | -42.33413 | 2025-03-15 04:19:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 155d6e8e-d02c-36f0-b263-f5128e97e777 | -11.44256 | -52.92378 | 2025-03-15 04:19:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 100e23c4-d2b5-303f-803d-bf0e755c3db0 | -17.43683 | -42.62023 | 2025-03-15 04:19:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c7556f96-18b1-3d6b-af61-ec3b91a97806 | -10.60881 | -45.10994 | 2025-03-15 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 897565ee-cdd9-300a-8344-47a5ff820e7d | -10.57577 | -45.14777 | 2025-03-15 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f8937074-3758-3981-abbf-aff831c02679 | -17.51368 | -40.62519 | 2025-03-15 04:19:00 | NOAA-20 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ae277e2a-55f0-35cc-8ccf-a03090d26c7f | -5.21431 | -44.30814 | 2025-03-15 04:19:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b42ecd2a-ec79-331f-97a7-33c8576cc2c4 | -10.57246 | -45.14725 | 2025-03-15 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c99c2dda-c282-3789-b9e8-0314d234a482 | -5.67561 | -45.21743 | 2025-03-15 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 519ce5ed-89e3-395b-af11-ac8d6bcf848c | -17.78197 | -42.80947 | 2025-03-15 04:19:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26509ecb-2ef5-3ee4-950c-73ad7653b298 | -10.60826 | -45.11345 | 2025-03-15 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9d47ebfe-6e3e-3163-8571-a34e3a408576 | -12.12551 | -44.96213 | 2025-03-15 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a81a54f-c2d7-3533-bbb2-14a73872536f | -11.56914 | -47.62339 | 2025-03-15 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc8bd61c-f06d-3e04-ad6a-0f8959dd68b0 | -10.60329 | -45.10188 | 2025-03-15 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a629ede-91b4-3e65-bc28-8a8550c450ed | -5.97121 | -43.75049 | 2025-03-15 04:19:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d83666f1-eb82-395c-9e94-1caf4ae236b9 | -16.68051 | -43.88509 | 2025-03-15 04:19:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 34701783-9389-3dd2-82af-aa1341adc288 | -6.24272 | -44.83504 | 2025-03-15 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 679571c5-d2cc-3637-98ee-68a3d3bee6b1 | -15.26193 | -51.47114 | 2025-03-15 04:19:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b8dc040f-d272-37ea-9e04-48246094fb2d | -4.81313 | -42.98734 | 2025-03-15 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d78559c-89b0-3d05-9d51-b2cc90ac0f1d | -4.66907 | -43.2582 | 2025-03-15 04:19:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a921f1a-b99d-3ddf-af7a-8c5031f7bae3 | -10.57907 | -45.1483 | 2025-03-15 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a0200824-e9c0-3314-9c30-9784b4a54be9 | -11.88452 | -46.94056 | 2025-03-15 04:19:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85482578-c667-3fd2-9137-29a1f49a1b38 | -19.69243 | -48.10181 | 2025-03-15 04:21:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d071eddf-b5b8-308d-94ea-82d1919938b3 | -23.59293 | -47.43829 | 2025-03-15 04:21:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0998b2e1-540f-3982-974c-015d892ae14e | -18.97477 | -40.95477 | 2025-03-15 04:21:00 | NOAA-20 | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 19ef74ad-8efc-3826-b175-c73a8ba7a7b0 | -19.70527 | -44.77042 | 2025-03-15 04:21:00 | NOAA-20 | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c6921775-a8de-306c-8411-13140480a5f4 | -22.39977 | -49.80507 | 2025-03-15 04:21:00 | NOAA-20 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6e72cdb7-2601-32d5-813e-08a95203f8c2 | -20.76296 | -45.57307 | 2025-03-15 04:21:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b72a026d-5a22-33e0-85d5-4739391a1c1d | -20.76447 | -46.77049 | 2025-03-15 04:21:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4ae6ad79-c8bb-33da-8445-c14b7f14dd5e | -20.57712 | -44.57448 | 2025-03-15 04:21:00 | NOAA-20 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 20a402e1-b3c0-37ef-a15b-980cc6e08c8a | -19.69458 | -48.10972 | 2025-03-15 04:21:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45d4414b-7859-30b9-a8c1-68d5bba86a17 | -21.17995 | -43.98108 | 2025-03-15 04:21:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6105b420-f03d-33ce-81c6-cd1eeeec92b0 | -18.97757 | -46.96528 | 2025-03-15 04:21:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa6acabc-e847-3217-9e7f-9275b1df9bba | -20.76644 | -45.57362 | 2025-03-15 04:21:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 556b2d7a-b379-3f87-85ad-27667351833f | -19.54427 | -39.76794 | 2025-03-15 04:21:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 07babe35-f9d0-31a6-bfac-798ab84a2438 | -20.01475 | -55.5295 | 2025-03-15 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10ebfe05-3857-3f44-a77d-e078ce996a68 | -18.30081 | -54.57122 | 2025-03-15 04:21:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8eef4344-704c-38d6-ac31-a5cb56164624 | -20.47715 | -53.67504 | 2025-03-15 04:21:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 584c90e0-03e0-3a00-a5cf-4d5fd1da25e3 | -18.97036 | -40.95425 | 2025-03-15 04:21:00 | NOAA-20 | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 011aaef9-8f94-3f15-810e-ddb6c7a8192f | -18.97701 | -46.96893 | 2025-03-15 04:21:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 158627a6-5443-3c17-a3b4-57668c542016 | -23.43906 | -51.42875 | 2025-03-15 04:21:00 | NOAA-20 | ARAPONGAS | PARANÁ | Brasil | 4101507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 791622b8-537d-362b-8746-9fd392131574 | -23.30902 | -51.33921 | 2025-03-15 04:21:00 | NOAA-20 | ROLÂNDIA | PARANÁ | Brasil | 4122404 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 72a1c7bc-8cb4-36d7-96d4-762647c53fc7 | -19.98128 | -44.86173 | 2025-03-15 04:21:00 | NOAA-20 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a0b8a17-b0fc-3ce4-8b9b-81933854f1ad | -22.53876 | -48.81229 | 2025-03-15 04:21:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac4ab75d-dd7e-3731-81a0-eefa4e51260f | -22.6232 | -47.46317 | 2025-03-15 04:21:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b265e855-4229-3af3-ae56-6ddc3017c5f8 | -20.99553 | -51.79159 | 2025-03-15 04:21:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2e10a6bc-c560-3b4d-868f-9d12cdd39ebb | -19.54364 | -39.77341 | 2025-03-15 04:21:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e4ab55e2-f563-3acc-8c3c-b88cbbe147c1 | -20.55281 | -45.98103 | 2025-03-15 04:21:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f5e76be1-9d88-35ac-ae68-ed40b1b5eeef | -20.5778 | -44.57673 | 2025-03-15 04:21:00 | NOAA-20 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 268cf89c-463d-3ba5-a30d-fedfbcc87b7a | -22.78063 | -43.04292 | 2025-03-15 04:21:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 18fa58ef-6e43-359c-85fe-a3472d3382f3 | -20.01308 | -55.52626 | 2025-03-15 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23ef6b36-64c9-3209-9323-9c7663a1b6a9 | -20.7647 | -45.57207 | 2025-03-15 04:21:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9130c1c-f824-377d-b7a3-aa2f58990c07 | -20.01773 | -55.52728 | 2025-03-15 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ddacd07f-0a6a-3d10-a2c2-6101303090b5 | -19.90466 | -44.68996 | 2025-03-15 04:21:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| bc366f9a-c850-31ac-bf63-19330ab9f5c7 | -22.78677 | -43.75626 | 2025-03-15 04:21:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 694c1e16-732b-353c-9e5e-626ff2ba1f98 | -30.45516 | -52.72369 | 2025-03-15 04:23:00 | NOAA-20 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 76484904-1b59-3e18-93a2-27376caae41e | -29.77718 | -51.17492 | 2025-03-15 04:23:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| e03eb27f-a927-3d5c-8ad9-28ac3ab1eb7c | -32.09249 | -53.29219 | 2025-03-15 04:25:00 | NOAA-20 | HERVAL | RIO GRANDE DO SUL | Brasil | 4307104 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| 42f61688-965e-3936-a410-336dd4324355 | -31.71919 | -53.32581 | 2025-03-15 04:25:00 | NOAA-20 | PIRATINI | RIO GRANDE DO SUL | Brasil | 4314605 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 22b94c73-d95b-32e9-aa50-f076fb35f38a | -9.09246 | -40.43315 | 2025-03-15 05:01:00 | AQUA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 14.9 |
| cbe3a153-1356-37a7-82d9-f5e0864dbf6d | -10.60621 | -45.10137 | 2025-03-15 05:04:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 890a1dad-c099-3d4c-91fb-1b7c7436e240 | -10.57214 | -45.15211 | 2025-03-15 05:04:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| ff874cb7-7a40-3190-9d73-33956193b550 | -10.57531 | -45.13374 | 2025-03-15 05:04:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 6fb7b295-2a62-3841-8bfe-842d2473239d | -10.57114 | -45.14464 | 2025-03-15 05:04:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 31.4 |
| c1eb7fdb-52f0-3300-a3b2-594b78a4a8c8 | -6.20866 | -48.04937 | 2025-03-15 05:10:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f667f61-0fbe-3b7d-b1da-1ca4dd469f29 | -6.20326 | -48.0486 | 2025-03-15 05:10:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8a0d515c-2bbc-31dc-aaac-d184eddbb7eb | -6.20374 | -48.04522 | 2025-03-15 05:10:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4ffbdcf9-e950-3f48-a9ad-e65abf794b63 | -6.19883 | -48.04087 | 2025-03-15 05:10:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c647002b-1f29-3fe8-8ac9-e99693820b00 | -6.20423 | -48.04167 | 2025-03-15 05:10:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 786bd94c-7530-3650-81e5-9368feba2da8 | -6.19932 | -48.03741 | 2025-03-15 05:10:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 585820fb-a5a1-3b4f-ba3c-4fa456306037 | -5.00983 | -56.17562 | 2025-03-15 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e63be08-16ba-30c8-bbcd-598acbba11da | -8.83422 | -50.33689 | 2025-03-15 05:10:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 75055143-ebca-3e44-a0c8-11f2884d481d | -6.19836 | -48.04428 | 2025-03-15 05:10:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7dfc9cbf-5efe-3e3e-bfed-637629a5df4a | -8.83373 | -50.3391 | 2025-03-15 05:10:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d0ddcb31-b111-323d-aaa7-8f985f21c05d | -6.22766 | -48.05035 | 2025-03-15 05:10:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a1d0867-af66-38f8-b178-8c47b6fd424d | -6.20914 | -48.04593 | 2025-03-15 05:10:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4f69ab82-5a3f-35b6-9525-390264d189a9 | -11.11494 | -54.49743 | 2025-03-15 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2e2afb9-8b83-3016-8964-9990d18afbf9 | -10.57171 | -45.14965 | 2025-03-15 05:12:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 73640f07-70d7-3c03-b4cc-984ce7aa2f44 | -10.57855 | -45.15071 | 2025-03-15 05:12:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c03e5ce5-4fdf-3c8e-a9df-439937569907 | -10.57244 | -45.14324 | 2025-03-15 05:12:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2ba862ba-f5e2-3a97-aba7-9fd276fa87ce | -11.89005 | -46.94396 | 2025-03-15 05:12:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80dd350b-8b55-35d4-9e45-02da63859b87 | -10.57929 | -45.14415 | 2025-03-15 05:12:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 018cbc9f-0b03-3a6a-a20c-c54e7e6ab625 | -11.44361 | -52.92241 | 2025-03-15 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46163e15-b8a9-30b7-b6be-bbef43de07b3 | -10.60507 | -45.10163 | 2025-03-15 05:12:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| aaf3a1f3-2317-30e2-8efa-0223b8c06688 | -11.88378 | -46.94329 | 2025-03-15 05:12:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6920abb-7662-35ff-9244-908a04326684 | -10.60431 | -45.10827 | 2025-03-15 05:12:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| ee5d281a-3cfa-3cc9-a2a8-4fbe1d6ef867 | -10.6112 | -45.10896 | 2025-03-15 05:12:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89a52376-db6f-381c-bf52-53258db1037c | -15.26624 | -51.47151 | 2025-03-15 05:14:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c25cb47-3396-3775-b33d-0c19bd3b87e6 | -15.63287 | -57.30883 | 2025-03-15 05:14:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3016517a-d32f-32f6-b0fc-878ceaf57bdd | -16.4819 | -54.17148 | 2025-03-15 05:14:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7aa8d9ec-d21e-33c6-b751-134973efc84f | -16.07157 | -53.7516 | 2025-03-15 05:14:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2a520819-a3f0-3855-a497-a0ac42e81086 | -18.53438 | -56.17916 | 2025-03-15 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7fd9d8de-ccb1-350f-a7e4-2cc13b1afee6 | -15.6323 | -57.31269 | 2025-03-15 05:14:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72b8c8e6-ccb7-3a5e-bb2d-8cc331fc1248 | -15.63483 | -57.3121 | 2025-03-15 05:14:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77267015-5906-3dbf-8017-79fe5cab2a14 | -20.01287 | -55.52715 | 2025-03-15 05:14:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c612ba1d-d209-3861-8905-84c70a615228 | -21.99442 | -48.8002 | 2025-03-15 05:14:00 | NOAA-21 | ITAJU | SÃO PAULO | Brasil | 3522000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| de3b55d9-ffe6-310a-907e-14e0a91818da | -20.01684 | -55.52777 | 2025-03-15 05:14:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b43d52d-e509-3180-9585-22f5bdd2f9ba | -16.07578 | -53.75227 | 2025-03-15 05:14:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README6.md)
