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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ba5509c-007e-319d-b3c0-a59bfea22565 | -20.38547 | -58.06084 | 2025-09-22 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6d920103-b0ed-3819-89e0-1311e9530893 | -17.27254 | -43.44067 | 2025-09-22 04:19:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c54abab4-be47-3378-bd72-78aabc6df68c | -10.40277 | -47.85067 | 2025-09-22 04:19:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b665f33c-5fa5-3606-9e71-da9c520e0ef1 | -17.34688 | -46.82575 | 2025-09-22 04:19:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bc81a8a0-b6b8-3c7a-81da-fca1be0793c8 | -21.36806 | -46.17372 | 2025-09-22 04:19:00 | NPP-375D | AREADO | MINAS GERAIS | Brasil | 3104304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e78f670b-cc30-3bf7-8598-712c61cd7b64 | -7.70442 | -55.45395 | 2025-09-22 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 829cd542-fa81-3119-a7bb-fb5e094a8816 | -15.5381 | -44.32525 | 2025-09-22 04:19:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3665c4da-1e98-3190-8ef9-a397b99bba9b | -22.41042 | -46.78771 | 2025-09-22 04:19:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 812826bc-340b-3f74-874e-e02ecb2d5ac4 | -18.37641 | -43.70153 | 2025-09-22 04:19:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a52f045-c1d4-3166-908e-ce18a07f95ea | -17.70371 | -44.08137 | 2025-09-22 04:19:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 33ab1bfa-a934-314c-a247-9b95483851f4 | -17.05326 | -44.90307 | 2025-09-22 04:19:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ce302b8-b81d-3c9b-954e-5f3b513b0016 | -11.52381 | -43.62709 | 2025-09-22 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8439e87f-8d8e-325b-b0a9-98b37afb50aa | -18.09725 | -44.26729 | 2025-09-22 04:19:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a630f8a7-4ba5-3370-a3dd-d141068e5e6a | -22.41826 | -46.78144 | 2025-09-22 04:19:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| da9edbce-bf1b-3b69-9241-a9bce47ed15d | -20.55047 | -56.14901 | 2025-09-22 04:19:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d64620e5-d5b2-3592-a8fa-63905949cdc2 | -8.76554 | -46.18766 | 2025-09-22 04:19:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 884d2c56-dbf9-378b-b065-4bf80321fda7 | -17.66741 | -44.09192 | 2025-09-22 04:19:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3cdcbfd2-0a2f-3537-8a1a-9d66aeed3a94 | -10.33951 | -46.07297 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 478f65d9-6a11-333d-871f-8d75f6ea0361 | -17.75867 | -44.38873 | 2025-09-22 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70d7eff9-8e87-307a-83f6-5c36acf36f2c | -10.46134 | -44.19046 | 2025-09-22 04:19:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23912c22-93ef-37f3-b3db-119a11831050 | -20.54445 | -56.15117 | 2025-09-22 04:19:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 723cb06a-07f5-32a9-af33-ed9c9d223cca | -22.41493 | -46.78083 | 2025-09-22 04:19:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fe4f8021-7abb-3537-b178-e5d49f22efdd | -20.53183 | -44.03555 | 2025-09-22 04:19:00 | NPP-375D | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d6f6266e-4801-34b3-9178-8e70c52d6d0c | -19.84705 | -57.29387 | 2025-09-22 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| bbc69bbe-ff19-3b3e-a414-fbfe364f58be | -15.9971 | -59.4721 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 4f194ee7-713a-37f5-9ba9-96c1e02df34c | -19.92493 | -42.36665 | 2025-09-22 04:19:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d3bfc8cc-06a8-3c42-82b8-284da0d3c1ed | -10.38961 | -46.08047 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 803b2da8-0802-3fb6-9e6a-cd400266c6a7 | -17.34076 | -46.8208 | 2025-09-22 04:19:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61965a6e-76ed-3dd3-9af5-fb00322649dd | -15.83608 | -59.51373 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c724ebb-cd24-3608-922e-53ef3490d063 | -10.25539 | -46.06655 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 62a8e3bb-8c95-3261-9424-f32cd7e9f5aa | -21.61065 | -44.72709 | 2025-09-22 04:19:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2b3fb64d-fbce-3202-9f2f-350eaa50d9b9 | -15.16471 | -49.58446 | 2025-09-22 04:19:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1fd338ca-b961-3c22-8304-6b289e1510a1 | -7.70353 | -55.45265 | 2025-09-22 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 16a9b5a7-8ecb-33fe-87eb-6bea824ecc86 | -20.37083 | -41.10152 | 2025-09-22 04:19:00 | NPP-375D | VENDA NOVA DO IMIGRANTE | ESPÍRITO SANTO | Brasil | 3205069 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 43fde271-063a-3657-bf55-4157f61ae6e0 | -17.34413 | -46.82141 | 2025-09-22 04:19:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f53d65e-f4a8-36db-bb4a-f61c941b3c88 | -9.73948 | -45.9528 | 2025-09-22 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe0c5b68-f9aa-3f41-9f12-1c96b3c60bb2 | -16.12117 | -45.67533 | 2025-09-22 04:19:00 | NPP-375D | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4472e515-6b8e-3e0a-8da5-5a5276435480 | -19.85465 | -57.28692 | 2025-09-22 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 880f7737-c44d-3ede-adac-e23e2eceb9fb | -17.42542 | -42.36814 | 2025-09-22 04:19:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c3cc640-35fa-33dd-916e-df30ae6a32bd | -18.98369 | -44.22926 | 2025-09-22 04:19:00 | NPP-375D | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 639b3238-aada-308c-bfdc-f30b07be57c9 | -22.40983 | -46.79145 | 2025-09-22 04:19:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a9cf30c3-fa04-3751-ab22-c6cd33e2f30c | -17.43978 | -44.81207 | 2025-09-22 04:19:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9581308c-9a4a-362a-9d96-e43e59a75bea | -17.33893 | -46.83205 | 2025-09-22 04:19:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03d9bc4f-16fa-322d-93d9-3af7984fcd7c | -10.35846 | -46.11852 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b234e9b8-22d2-366e-883a-f86653e19141 | -10.50407 | -44.04977 | 2025-09-22 04:19:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce97d318-1f74-3a95-a956-eee287cbd639 | -20.26557 | -55.50375 | 2025-09-22 04:19:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 97d75ec7-99b2-3126-aea5-c3f3fbdb4e29 | -15.77388 | -59.41319 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4de31d98-cd60-310c-800c-c0f27bbee3c9 | -10.04802 | -49.19669 | 2025-09-22 04:19:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffe9cd49-f89f-3bfc-bf3b-6dfd2804d7f2 | -20.78612 | -56.92246 | 2025-09-22 04:19:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c4a50850-50f9-32c3-9c85-7cf9ac44f34e | -22.41982 | -46.79327 | 2025-09-22 04:19:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 627ae086-b41c-38d6-84d2-03e84b170667 | -17.27138 | -43.44865 | 2025-09-22 04:19:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c34de45d-695b-359d-942d-b91a816f3f23 | -18.55289 | -43.84823 | 2025-09-22 04:19:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 77682c4f-10d7-3f32-ba58-d352626ff9ea | -19.31408 | -43.75793 | 2025-09-22 04:19:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c217cdf-6a7e-35a7-b7b2-1821077fcfcc | -9.73602 | -45.95225 | 2025-09-22 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7da4e301-c8ab-32c0-9f86-5bce0330a707 | -22.42159 | -46.78205 | 2025-09-22 04:19:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2834678-3405-34eb-a0e9-c0d43e907afa | -17.05995 | -44.90419 | 2025-09-22 04:19:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2f449d2e-6bc3-3678-b1f9-b13a4b8ddf9e | -20.67649 | -54.57461 | 2025-09-22 04:19:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3cff69a8-2161-37af-b1f8-66ab8d5d9f7e | -18.87073 | -43.34578 | 2025-09-22 04:19:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 76d0c190-dcb6-367a-8a52-a16da9f44aac | -15.96757 | -50.37468 | 2025-09-22 04:19:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b5976a5e-956c-305a-804a-3f9a798e6507 | -18.10065 | -44.26785 | 2025-09-22 04:19:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c388f4e-2cfc-3d6f-900d-5f9e6832c60a | -15.0412 | -55.29555 | 2025-09-22 04:19:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f95d3868-f443-38c1-9531-219788a299af | -20.43604 | -43.67695 | 2025-09-22 04:19:00 | NPP-375D | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0d2345f3-8a1e-32b4-8d4d-72e03805dfa9 | -20.26025 | -44.42367 | 2025-09-22 04:19:00 | NPP-375D | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bde8aa8f-fa40-3fa7-bf85-93f1c906b8e5 | -15.93633 | -42.18974 | 2025-09-22 04:19:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 52488adf-ce22-3e27-b58e-889c5eece297 | -18.05001 | -43.8406 | 2025-09-22 04:19:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 345a307c-f39e-3511-ada9-74f403906d45 | -17.75924 | -44.38498 | 2025-09-22 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba2426ff-f9b0-3cc6-a423-d0ba2c851334 | -19.8422 | -42.21025 | 2025-09-22 04:19:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 71a686a4-427a-3643-9352-ed555aee23d1 | -11.46759 | -43.53398 | 2025-09-22 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5c3e9a9-e8ec-3aa3-9e18-ed16a7aa9a43 | -19.96021 | -42.10416 | 2025-09-22 04:19:00 | NPP-375D | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 62d3bb39-21dc-3993-bf48-6c5c48e0c12e | -22.41767 | -46.78518 | 2025-09-22 04:19:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be42f1c7-8049-3eb7-8f9e-6d6a69ef1333 | -18.40166 | -42.86369 | 2025-09-22 04:19:00 | NPP-375D | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 6b02ac24-01c7-3603-8aeb-24e35fe15aa0 | -20.53682 | -43.72437 | 2025-09-22 04:19:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 08e61530-1d5b-3a9c-b068-61f5ca282595 | -20.18625 | -44.62051 | 2025-09-22 04:19:00 | NPP-375D | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 014e4fda-3137-3dfc-9296-8c9b3b268fda | -10.32415 | -46.10194 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 257233a8-11dd-3bdd-84fd-d3048ec0b87f | -14.62521 | -49.75086 | 2025-09-22 04:19:00 | NPP-375D | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 47b8fd93-f874-3c95-ab6d-eb7a9376306f | -15.53866 | -44.32161 | 2025-09-22 04:19:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e2bba5a7-eb09-3207-b245-aa569aa29815 | -18.38226 | -46.47107 | 2025-09-22 04:19:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 2e67e039-c16d-36c7-9660-0effa88217f6 | -14.69214 | -48.7838 | 2025-09-22 04:19:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 101802b8-8afd-33e5-b311-ec785c20f51f | -20.62642 | -41.19822 | 2025-09-22 04:19:00 | NPP-375D | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 60bb34c3-558f-3416-9edf-024088d8b3a5 | -18.37676 | -46.4626 | 2025-09-22 04:19:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 8cd8257c-3f5d-38d8-9323-5ab677c86e75 | -8.84992 | -46.15613 | 2025-09-22 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9de74ae1-f142-3b52-939e-923ed4f01f8b | -19.84663 | -42.20597 | 2025-09-22 04:19:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 6cfce2a9-dc96-3025-934e-01258edfd602 | -18.54755 | -43.97995 | 2025-09-22 04:19:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 143da520-13a2-314b-b0dd-11b12e95cab3 | -19.57471 | -41.65443 | 2025-09-22 04:19:00 | NPP-375D | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 0cf0da02-6c72-30e2-a547-bf7c793b94df | -22.41649 | -46.79267 | 2025-09-22 04:19:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 11b9d318-2d2f-39e8-b608-b28e658b1ca4 | -18.39927 | -42.85476 | 2025-09-22 04:19:00 | NPP-375D | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 5661177b-6eb6-3e4f-b958-5f04b9d840a9 | -20.62689 | -41.19452 | 2025-09-22 04:19:00 | NPP-375D | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4626f438-a1db-33bc-9a54-650d8442c263 | -22.41924 | -46.79702 | 2025-09-22 04:19:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 65.0 |
| f90463c2-4e02-3ff3-82bc-cc33f1d39e24 | -15.95033 | -59.38752 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2b486137-58c0-33a8-8343-8ef053389636 | -15.77251 | -59.41928 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 85dfa91f-15ee-323e-a47c-732a6206a1bd | -18.09714 | -44.26741 | 2025-09-22 04:19:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d85caf10-ca96-3ff7-9e65-24c4b55bb26d | -15.76862 | -59.42251 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7c726408-7eb6-3621-ada5-b67c4336a07b | -8.90453 | -46.10895 | 2025-09-22 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bcbc8294-d31e-347a-9799-011e61ebc28d | -10.34599 | -46.06535 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f4d6ac3-65cf-39de-8326-219b22bc6d3d | -18.37951 | -46.46684 | 2025-09-22 04:19:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 38ff2ee1-681e-3c60-a887-c60d81a1cf9c | -14.84157 | -51.73875 | 2025-09-22 04:19:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 67e947be-6499-323c-96fd-52657f4612a4 | -10.40653 | -47.85127 | 2025-09-22 04:19:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ecf215a-362c-3ee3-bafb-50072d408a97 | -20.43666 | -43.67267 | 2025-09-22 04:19:00 | NPP-375D | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 58bb9c0a-fbea-33bd-b30f-d61c7d67ac46 | -15.76302 | -59.42879 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4663d36f-5f42-33e9-9b36-7951db8f8061 | -15.9601 | -59.37668 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |


[Clique aqui para ver as próximas entradas](README22.md)
