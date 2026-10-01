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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7cfd964b-080a-3a78-827b-4a1558967911 | -13.55129 | -49.1777 | 2026-10-01 04:34:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52420343-8397-3bad-ba41-b4dd77978084 | -12.1832 | -47.3882 | 2026-10-01 04:34:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6db2f4d0-025e-3fa5-88c7-96f0ac075e4c | -11.16303 | -54.11614 | 2026-10-01 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 176f8609-b897-3649-b940-77db033016fa | -5.86079 | -57.76035 | 2026-10-01 04:34:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 431bb472-e0bc-38ac-bf2f-50c0b733e42f | -9.31419 | -57.70951 | 2026-10-01 04:34:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54e101e3-e00c-399f-8360-0b1eafb52f09 | -6.74966 | -55.09045 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d8e214bc-0e4c-3c45-bf4b-5fe09cc17cb1 | -11.61059 | -43.5546 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4c15106-091e-3208-9faf-e19ed92589f1 | -14.23889 | -44.23122 | 2026-10-01 04:34:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1d39394-fcd1-37cc-8ece-e37cdf289d58 | -10.79704 | -48.7652 | 2026-10-01 04:34:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f2bb3fcb-3af4-37b0-b038-1eb46d4d25f5 | -9.3134 | -57.71359 | 2026-10-01 04:34:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b07b82ba-bbbd-3a06-ad41-589847e5d0d9 | -6.36361 | -55.1425 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97685b78-6586-333f-a532-d4d2e55b54ab | -9.81161 | -44.82704 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 626d6d38-fd4b-31f0-a19f-848d459b267a | -9.07261 | -44.99708 | 2026-10-01 04:34:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fbb54207-e9ac-36ce-85e9-16f5bb0c5442 | -6.14264 | -53.06299 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f48b4ed7-a8c1-3291-a966-8ad2ba6236a9 | -10.77865 | -50.5307 | 2026-10-01 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 08a86d28-74e3-3c8f-ba86-183bbb36bb70 | -11.66023 | -43.53307 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72903119-5929-34a1-b18b-78885440a9fb | -7.33999 | -55.60167 | 2026-10-01 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c655136-6623-3dde-9cb7-1a963d253235 | -9.80985 | -44.83871 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fd01f40-9b7f-3936-ab33-acf3c513afab | -11.21097 | -45.15524 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 616a6f59-79e9-399a-890b-d9a74c3c08c2 | -7.50884 | -55.04253 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3e57328-0e71-3360-a98f-86b8949c0377 | -9.38531 | -46.06276 | 2026-10-01 04:34:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a676c386-1531-3654-abb2-e0608c709fda | -11.25981 | -43.52365 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b221173e-5230-3023-a78b-52fb74cee5e0 | -11.22648 | -45.19386 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 748cd98a-f6c6-3c8f-b056-418989365ff8 | -8.24899 | -47.98593 | 2026-10-01 04:34:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d681adc-13a4-3481-bdfe-132084efccac | -6.50645 | -55.37104 | 2026-10-01 04:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a6fa68c-3b18-332b-8a5f-c09963256439 | -11.14482 | -47.49021 | 2026-10-01 04:34:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 812796bd-796f-3191-be71-1819f1db0d3c | -11.40769 | -51.02692 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2fe42fde-0cf0-34a2-8fa3-7cd9b9cca699 | -11.44986 | -43.43905 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f2f0afb3-6123-3533-a231-62532a1e9c22 | -6.43084 | -55.80766 | 2026-10-01 04:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3575996-eea7-3f01-ae03-02cbc81dcd36 | -6.73698 | -55.59296 | 2026-10-01 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e6c7e8b-c660-33c6-ae05-7b5e7019a752 | -9.94928 | -51.46249 | 2026-10-01 04:34:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 613a605d-457f-3ae7-86b5-0267dd17d853 | -8.49857 | -44.76406 | 2026-10-01 04:34:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc6addf7-a1af-3250-9cf6-004922241634 | -13.87468 | -44.43441 | 2026-10-01 04:34:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 513c7f7b-6b0e-317e-a196-634fb47c1fde | -10.56149 | -50.04914 | 2026-10-01 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d06f267-e365-3acf-ac2d-31fc73bb16eb | -6.13786 | -53.28976 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 72ace2c6-cec9-32c9-a48e-7466067cb08a | -9.38589 | -49.15129 | 2026-10-01 04:34:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01b72746-fe82-372b-a83b-0d36c5b46903 | -13.68297 | -44.28894 | 2026-10-01 04:34:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4627f806-7625-3d9f-afbf-07b21863423c | -9.87131 | -44.93894 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe727fda-4d55-3fab-a2d4-accd67f644a0 | -11.47066 | -43.45665 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e369cad-59cc-354e-a9ce-48fb7a2d1f41 | -11.42275 | -43.41072 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d844c873-cddd-3def-8098-3a86d9562671 | -8.63016 | -45.32581 | 2026-10-01 04:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c45e95b-150f-37ad-88f5-aea0347acbcc | -7.48707 | -54.99036 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 977605df-9b66-3a43-b469-bf16c11feff2 | -12.50503 | -43.10601 | 2026-10-01 04:34:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 694385c2-415f-36ef-9fa0-c035b09aa3f5 | -9.20462 | -45.80404 | 2026-10-01 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 076bdcb3-6ff0-33d2-8922-0479fa87de73 | -11.19114 | -45.19226 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fe940e75-ee95-3363-b94d-f4d04b41dd6b | -11.83765 | -50.95041 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1240aea-7d3f-3033-af24-6959ab9f637a | -11.20445 | -45.19838 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5469bded-4ae3-361f-b6be-971b7353ec26 | -10.52942 | -57.78141 | 2026-10-01 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6f0c143-9a43-3160-b62e-a1811c0b9dc9 | -12.09059 | -50.68859 | 2026-10-01 04:34:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d1926a4a-07bd-3579-9862-2097f19f1e33 | -8.04278 | -42.85832 | 2026-10-01 04:34:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c5d1ebfe-cfab-32e0-8b87-ac02d6f5274b | -8.17544 | -54.79886 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17158be3-4068-3995-848e-18e4490fcc3b | -11.20578 | -45.14236 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6add6ae4-6569-39e3-a2b3-6c9cb9c72ae9 | -8.6229 | -45.37327 | 2026-10-01 04:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3128a2f5-12da-3932-ad38-132e2c94de89 | -10.73643 | -44.41374 | 2026-10-01 04:34:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d1fc4769-53e1-307f-942b-b6d003726e69 | -7.88842 | -54.72927 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ba1ea3d-d49f-34cf-995c-bba7b8e6ea78 | -9.06776 | -49.8759 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ba903e8b-e95f-321c-871b-677b2862820c | -11.74603 | -50.4053 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 85646dd8-b3ff-319d-a267-91746c52603c | -9.06 | -44.98743 | 2026-10-01 04:34:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1fc51795-2480-3a64-9ad3-e6c8e05b9927 | -7.19669 | -46.50993 | 2026-10-01 04:34:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e28f63b6-ff9e-3606-a5d8-9b6017d5c8d9 | -11.46062 | -43.44545 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 77ee13cf-63a9-3679-bdd9-745d17da5670 | -11.44047 | -43.4231 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4f5897d4-ee9f-3087-aea9-aea1efc658a4 | -11.78831 | -50.50005 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 558c8ac2-8001-3701-9dfd-3ea3be2fd570 | -11.68026 | -43.50221 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 920312b4-f023-37ba-869a-5b5a9c32df75 | -6.02591 | -53.36462 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85c278ad-6c93-3870-8775-fa33eda7b3cf | -7.52776 | -50.53468 | 2026-10-01 04:34:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3977848b-f9c8-3c93-8e12-520ef5a74dea | -7.5464 | -55.03264 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afb477fd-cd56-3f8e-b0ae-76d45ba33f20 | -11.25915 | -43.52834 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d89e31ee-4c81-3139-bba6-0e225753e989 | -11.61505 | -43.55045 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 790f9729-51f3-37d8-a554-742c116d713e | -9.65442 | -51.75025 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3aa5434d-f456-3a91-ac2c-8e729ba31afc | -13.33692 | -46.82163 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69c2ec40-98ba-3993-b2f8-d5abdeba4585 | -8.20957 | -46.20367 | 2026-10-01 04:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 986c3f32-6533-33cc-8cc8-8493f1ef73d6 | -11.38317 | -43.3681 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8d073a88-0dae-3cac-a385-22385d7a744b | -9.8058 | -44.81816 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d721d1c6-7171-37b3-b698-c1989454d77f | -10.53746 | -57.77037 | 2026-10-01 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed0f3e3c-0717-3fd5-8c8e-be3d209b9bbe | -10.84061 | -48.70942 | 2026-10-01 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51c3198d-8c9f-3415-a05a-f2be5d2bb010 | -8.06554 | -50.96297 | 2026-10-01 04:34:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb496979-d4a7-36f7-9cbc-c4c5c85a5069 | -12.55212 | -47.17855 | 2026-10-01 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 66f5c76e-3bb3-3c1a-ba18-0740274cd245 | -13.3809 | -44.02309 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f9c65f2-2239-3d45-9b0e-f99c008d6b69 | -10.25685 | -44.57964 | 2026-10-01 04:34:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f93263d6-09a2-37b7-89cd-6a4143affdda | -5.86699 | -53.49226 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0787ec87-cba2-374c-b409-9e8f95d60c14 | -5.86221 | -53.49227 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76982881-ca4f-3f81-b9fc-dda37308b0e4 | -12.64326 | -47.63602 | 2026-10-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c6af5ce9-d89f-3aa8-874d-3b8b00bc0b0a | -13.5507 | -49.1813 | 2026-10-01 04:34:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 094a68d8-5f73-3472-9105-19159ea8271e | -10.46123 | -51.76225 | 2026-10-01 04:34:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 160bff3a-4b9a-3187-98e0-64e9bdde5576 | -11.38903 | -43.40796 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb48623a-2631-312a-8bac-3f1b4f02af4d | -6.13117 | -53.27432 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8d5c28a-4c8e-3ad0-b2ca-f585f48e28a1 | -11.20808 | -44.83863 | 2026-10-01 04:34:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e824db9d-1d64-3a2e-b559-3f5fc93ae539 | -5.8542 | -57.76661 | 2026-10-01 04:34:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fa82dc8-562d-311b-aa10-14d3fedc5477 | -9.16631 | -45.59481 | 2026-10-01 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2dcfbe77-b313-3d9e-b7c4-fb7d0f9eac7a | -11.43038 | -43.41187 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 88cefa3e-4cbd-37df-b015-469a0819daaa | -10.54633 | -50.00974 | 2026-10-01 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| f204df2c-18f9-3a02-b391-891f81ebc344 | -11.66259 | -41.84382 | 2026-10-01 04:34:00 | NOAA-20 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| deb00cca-9294-3c1a-b9c4-9a11f3d182e4 | -10.6067 | -48.05297 | 2026-10-01 04:34:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f18b4032-085d-3abd-9734-0cef80127544 | -11.42902 | -43.42139 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0613c280-339e-3137-a9f9-ddc2ee0a3363 | -11.44711 | -43.45805 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f17bd6b-c98f-3de8-8362-30a3ad845343 | -8.63124 | -45.29597 | 2026-10-01 04:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b30aad54-645c-3184-b61d-5ffbe1b43d80 | -12.42811 | -54.40264 | 2026-10-01 04:34:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0aeb678-a81a-3c4b-8f6a-2df7a5248286 | -8.21113 | -45.47405 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1033181a-a6aa-3ccb-9acf-0258058f9000 | -11.4004 | -51.02564 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bbf4be8c-e094-3ed3-9fb1-3435f83366da | -11.45055 | -43.4343 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README57.md)
