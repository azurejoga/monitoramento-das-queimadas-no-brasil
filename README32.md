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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ee20a79-8cae-3f2e-b102-306f30aea54e | -9.92895 | -47.65941 | 2025-10-19 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8bc3cc08-01d4-34b3-8c3c-2d21c670d3a1 | -11.60943 | -48.5402 | 2025-10-19 04:12:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 436ea5f3-3a42-3a3e-b334-6f1d002c762d | -11.33642 | -45.25761 | 2025-10-19 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 05c19866-42be-3cea-aff7-4e6c55e25e4f | -13.8607 | -45.46014 | 2025-10-19 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a04b3bd-23cc-3419-b093-9524486a6068 | -12.01341 | -46.48434 | 2025-10-19 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3dad800-461c-330b-9e5c-57e70e564a32 | -13.53362 | -43.00952 | 2025-10-19 04:12:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 36.0 |
| bbf4f45e-8646-3695-81b7-94307068a471 | -8.24172 | -43.99022 | 2025-10-19 04:12:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4505875-59e9-33e9-beb0-a69f27925e4a | -12.41161 | -40.92212 | 2025-10-19 04:12:00 | NPP-375D | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a4a2a729-41e2-3931-9ee9-d2a009ecbf2b | -11.77914 | -47.5532 | 2025-10-19 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b9587825-eb08-3601-867b-b6933149f27b | -8.39074 | -40.47695 | 2025-10-19 04:12:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 32c74c92-524b-3386-aa3e-f5881aff2796 | -12.53844 | -45.45792 | 2025-10-19 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b366522-7126-31f5-8083-08d8aae867cc | -11.39136 | -40.68886 | 2025-10-19 04:12:00 | NPP-375D | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 49941f49-a4a9-32df-a1ec-da24d561ce94 | -10.87954 | -47.46054 | 2025-10-19 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 519f0bd1-df87-32ec-9c8c-33714cff0ab3 | -12.98102 | -47.26617 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a103765e-9ec0-336a-a408-4d0f9fbd0e1a | -10.88046 | -47.45534 | 2025-10-19 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b880e7b0-2bbb-3672-954c-1adee7cda998 | -8.60505 | -40.19182 | 2025-10-19 04:12:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 38.3 |
| ae2793c3-882d-3493-a8b2-7baa2eba512c | -8.25304 | -44.00758 | 2025-10-19 04:12:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ecb2e11-d9b6-3953-bb5c-1e7eaf58035e | -8.60405 | -45.43603 | 2025-10-19 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 39dfe2f8-ee21-3174-b284-886b5be59dfe | -8.39702 | -46.2349 | 2025-10-19 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae32d31a-5a6a-369b-bd50-0e62d300c644 | -10.82105 | -43.92513 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b434ddc-0dff-3b14-bc9d-0b69f118c81d | -10.35974 | -47.47909 | 2025-10-19 04:12:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6657a15e-53e7-3f71-8152-9a725b04217d | -11.13774 | -47.71971 | 2025-10-19 04:12:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 106778e8-f516-3477-8f17-f9e42fc6da71 | -10.92367 | -47.98977 | 2025-10-19 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| babfdbc8-c91a-3766-be1e-92fe104aa229 | -9.23114 | -46.06081 | 2025-10-19 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 435d4e57-f93a-3b66-9a47-822f805028ce | -11.61543 | -44.06699 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d8bfb62-19cb-3770-9852-3ec0cab4034b | -11.63552 | -44.09281 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c5c38c5-2caa-3ec1-a51d-0545d7019fe9 | -8.22789 | -43.3048 | 2025-10-19 04:12:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 34318fb8-c139-361c-8301-8278e335347a | -7.44808 | -46.84107 | 2025-10-19 04:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0575472-e94f-38a5-a456-cfcdfaaf24b1 | -11.97667 | -46.92808 | 2025-10-19 04:12:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 431c444f-920b-3509-883f-4b971bd921ea | -10.88844 | -47.45663 | 2025-10-19 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7fcaa050-7a8f-3c56-9919-45856ded4eca | -11.64818 | -47.85005 | 2025-10-19 04:12:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4b064d57-2ea8-39a0-8def-ffdce537a197 | -10.1177 | -45.51563 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9d2ea6ec-9357-30b9-9b35-4466838e9bb2 | -10.86633 | -47.60516 | 2025-10-19 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6afb951-cfc1-3b5f-886d-d250918ae212 | -12.14865 | -45.06195 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 77ccbca7-f4ce-3cf9-a0d2-ea17c4c46eb8 | -12.98781 | -47.27233 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0edf5dbe-c98e-3191-820e-d99980a53aab | -10.22562 | -44.06092 | 2025-10-19 04:12:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1aba6138-a553-39dc-875d-f124259ed7f2 | -13.53306 | -43.01307 | 2025-10-19 04:12:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 36.0 |
| 9e2741c0-186d-33f9-9928-352effb02908 | -10.87171 | -43.93362 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4021474d-9f2b-3d5c-b37f-53a01e311b39 | -7.95612 | -45.94133 | 2025-10-19 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d832f6fc-d17f-3d50-8440-4c7ff93955ab | -11.35513 | -44.29189 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf8468ef-08aa-3fbb-9cd7-625c29d03c20 | -10.15592 | -42.21093 | 2025-10-19 04:12:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 2294587d-e3e3-376a-abe4-d1422d98aeda | -12.15071 | -45.05733 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c928e862-8353-38b1-8cdc-e12340bc1fd5 | -11.03937 | -44.65878 | 2025-10-19 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d82f7d96-8cbf-3a0f-b735-8d10536f3a36 | -11.14699 | -47.71426 | 2025-10-19 04:12:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a05c955-a9cf-3c68-be29-515e6e99f555 | -10.12447 | -44.52945 | 2025-10-19 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d4497618-cd4c-3494-b8ef-cc6ccfee894b | -10.21988 | -43.53442 | 2025-10-19 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 669a6df1-7f44-36e9-a7ac-c7bbb1e24c0c | -8.42825 | -44.15217 | 2025-10-19 04:12:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c05c7e23-ec57-3737-b6b7-6b29d403f001 | -12.69095 | -46.9605 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d72c9114-9292-3807-8cbb-22a81be8b0cd | -13.02364 | -46.9563 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7abc4f6-3fb5-3306-932d-478048619e30 | -9.1776 | -43.23709 | 2025-10-19 04:12:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5c607533-dce0-3308-8542-0f84aeffa3f0 | -9.83076 | -48.83797 | 2025-10-19 04:12:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 195d614c-06dd-338f-9a61-399b535291f0 | -10.86495 | -43.93247 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cdfb3b30-0958-3344-bcae-46c1891afb0a | -9.2296 | -46.06995 | 2025-10-19 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f3c63cb0-c98f-3b59-918b-f3b51dcaf156 | -9.22285 | -46.06414 | 2025-10-19 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e920789c-a1ed-3de1-a511-5fa52e18af18 | -11.63419 | -47.85871 | 2025-10-19 04:12:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dec8f5da-73c7-3e55-ab3d-7fd0dde7d176 | -9.61932 | -49.02232 | 2025-10-19 04:12:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 59d64dae-7cae-3d1b-883e-d8ca0367d066 | -12.45676 | -45.4288 | 2025-10-19 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 9277e7c1-cbf3-3fcb-b91a-3b33c7ea80ee | -10.79447 | -47.85307 | 2025-10-19 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49f8d81d-aad6-3701-9d6a-14b481cd1683 | -10.45064 | -45.02508 | 2025-10-19 04:12:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b56335cf-32f5-331d-a5e0-9d14c66f5efe | -8.65647 | -41.0351 | 2025-10-19 04:12:00 | NPP-375D | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 69c38dce-633a-3342-a979-bac09b0a7abe | -11.62894 | -44.06924 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e2f6f71-3253-37b8-afea-3e029e839c49 | -10.22842 | -44.06523 | 2025-10-19 04:12:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f350b861-119c-3b9e-8941-52f38d9cfe21 | -11.47685 | -42.21936 | 2025-10-19 04:12:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| c8f114b5-4c19-3a93-8b3f-3cdd59ed2fe8 | -10.16202 | -42.2155 | 2025-10-19 04:12:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f6af70d4-f814-393d-813f-d47d564d8801 | -9.7662 | -47.87391 | 2025-10-19 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcde8ea9-6f3a-31aa-9441-a17682d67cab | -12.45827 | -45.44127 | 2025-10-19 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba07ce0f-eac0-3392-ac77-f6d4fd1c8d25 | -12.47011 | -45.43514 | 2025-10-19 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45b10af4-8836-399f-b660-ceb6ae591542 | -9.60583 | -49.01973 | 2025-10-19 04:12:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a84d38b-5d11-3b3c-9f78-235f1157b058 | -12.14336 | -45.07986 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4cc56f01-2385-3bbb-8bea-14ee6c6ca725 | -12.4596 | -45.43336 | 2025-10-19 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf5035af-9617-31f0-8dda-b7fb6a8b61b0 | -9.89149 | -47.65636 | 2025-10-19 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8907fc0-716c-3bf6-aae5-f283beff8812 | -12.24179 | -49.38925 | 2025-10-19 04:12:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1434d1e5-93b1-3b9b-8bd8-9eeefb257c46 | -12.49444 | -46.93214 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 426c5375-8403-35bc-bba2-34a0bb1164c1 | -8.61192 | -40.19287 | 2025-10-19 04:12:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 3957060e-666f-34da-91aa-2062d1fb1b78 | -10.97748 | -42.29559 | 2025-10-19 04:12:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2396e3f5-ab1f-3210-964e-8a0faf5f30a1 | -13.92339 | -42.95621 | 2025-10-19 04:12:00 | NPP-375D | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ccd3403e-bf74-389e-953d-15383d238a21 | -10.88907 | -46.07725 | 2025-10-19 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 27f25a01-da43-3787-ac36-56d2c7f5b73d | -9.52677 | -47.90715 | 2025-10-19 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e614b85-9d7c-3f9d-a6f1-6ccbb7bfeaf8 | -9.66572 | -44.55439 | 2025-10-19 04:12:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9dfe735-0816-3d15-9f67-fac32e7ad7d6 | -11.64683 | -44.08721 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6dce32d6-90ad-3662-9411-e3dd2717802f | -8.61479 | -40.19712 | 2025-10-19 04:12:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 3580b3b1-8723-3ba3-afdd-a4fbe2f5f5a4 | -8.25257 | -43.32365 | 2025-10-19 04:12:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cc094789-15fe-3d83-9154-686644ffa173 | -8.61562 | -41.52783 | 2025-10-19 04:12:00 | NPP-375D | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 926b850f-94d2-3465-988a-67dd30074c1c | -12.10714 | -45.87965 | 2025-10-19 04:12:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c870b859-87e4-3437-ab64-4f0a08e0f724 | -8.55678 | -44.57681 | 2025-10-19 04:12:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c43ed5ad-f312-3e3c-a5c2-e3f86a6790e2 | -9.10944 | -43.2113 | 2025-10-19 04:12:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7c05b46a-986b-3501-b1f0-7f3ab37be779 | -10.36437 | -47.47631 | 2025-10-19 04:12:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee004b59-9852-3897-9287-3ad52c9e35a1 | -7.34732 | -47.5831 | 2025-10-19 04:12:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f70b11b0-46f3-334d-b109-e57153291714 | -10.13607 | -44.52373 | 2025-10-19 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d837e11-f722-34b4-ac73-997ac2bacfff | -11.64756 | -47.85362 | 2025-10-19 04:12:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 300cdc35-167a-37d2-855a-5fa02e770631 | -10.84747 | -43.9333 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| afa16e09-c71c-3193-854f-8bcef7252598 | -9.82094 | -41.91308 | 2025-10-19 04:12:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ce890ad2-b563-32db-8b67-5c67e92b20d1 | -7.32529 | -47.25225 | 2025-10-19 04:12:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a603959-9e60-36e0-b8c2-661536bc7e73 | -10.77855 | -40.31476 | 2025-10-19 04:12:00 | NPP-375D | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 866c5a18-5e56-3e5d-9b19-7e2a495e733e | -10.12509 | -44.52567 | 2025-10-19 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f2d3b90a-453a-3637-9ff4-620a56c59fac | -8.24516 | -43.9908 | 2025-10-19 04:12:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a6b38d7-b4e1-37f8-aa39-c8c82374a2c8 | -10.8794 | -47.45374 | 2025-10-19 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f35921c3-cb99-3f28-a115-29e49337b5e1 | -12.14661 | -45.06058 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8856b188-a28f-36a2-a7b1-8d550e9f3055 | -11.62877 | -44.09168 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 308e6847-8e9c-37d5-bfb7-98fa5664de18 | -12.18779 | -45.09136 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README33.md)
