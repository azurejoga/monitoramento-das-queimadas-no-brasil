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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c37e182e-a09b-3c14-b9ad-9ddbb5b215d5 | -21.46183 | -43.60461 | 2026-07-20 03:45:00 | NPP-375D | SANTOS DUMONT | MINAS GERAIS | Brasil | 3160702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 196c31e0-6eef-3c5c-9e1e-aff5a963bef3 | -21.13131 | -47.46394 | 2026-07-20 03:45:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b550a5f9-c002-3ab9-81b0-182bc6c774aa | -19.3902 | -40.30124 | 2026-07-20 03:45:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 41892ae4-d30c-329e-a916-ee22392dfde6 | -22.57767 | -42.06291 | 2026-07-20 03:45:00 | NPP-375D | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bb04dfdd-a259-384b-a81f-1ad2a249ec04 | -21.60584 | -46.6144 | 2026-07-20 03:45:00 | NPP-375D | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 611739af-8d6c-3302-a33e-9d27f0b7878e | -21.86385 | -49.24847 | 2026-07-20 03:47:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ee9e5f3a-bb52-3801-a573-da8eb6485d6a | -23.29971 | -46.1761 | 2026-07-20 03:47:00 | NPP-375D | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 580ffa82-2b2e-345b-9a11-2c7677aecc69 | -23.06171 | -46.89029 | 2026-07-20 03:47:00 | NPP-375D | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a15d4778-f7e5-34e6-bf11-333a3143ee09 | -22.90414 | -43.47562 | 2026-07-20 03:47:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 382b71a6-bf92-3628-9d53-15298aeb2bf9 | -23.05855 | -46.88937 | 2026-07-20 03:47:00 | NPP-375D | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 43dc0439-4d67-33e4-ad8b-57db4211716d | -21.87035 | -49.25004 | 2026-07-20 03:47:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 202cd85e-5d09-3076-89f0-2aa32ebd0b98 | -22.69385 | -48.69128 | 2026-07-20 03:47:00 | NPP-375D | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 00df2604-a40e-3da2-9be6-a1c2fb93152c | -22.90907 | -43.47463 | 2026-07-20 03:47:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b90cefb8-cc14-3ef7-ae18-65bf018e8e8c | -22.69255 | -48.69663 | 2026-07-20 03:47:00 | NPP-375D | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 17.8 |
| b25c06fe-869c-30f0-b98e-6bee6a761fdb | -21.86546 | -49.24922 | 2026-07-20 03:47:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2b148e1c-a2a1-302f-a26b-843b898b452a | -22.83321 | -43.00264 | 2026-07-20 03:47:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e13d90d4-e635-39ba-a7cb-29a953924469 | -21.87197 | -49.25074 | 2026-07-20 03:47:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 17bc4b08-3b7a-3fc9-aa7c-ef779ec52722 | -22.90161 | -43.32787 | 2026-07-20 03:47:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e34ba01e-bcfa-310a-af78-335e5c3cbe10 | -4.93935 | -37.16457 | 2026-07-20 03:57:00 | NOAA-20 | GROSSOS | RIO GRANDE DO NORTE | Brasil | 2404408 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2d0c406e-306e-357d-ab5b-419c245938ed | -4.67873 | -43.22189 | 2026-07-20 03:57:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f3a0fc1-f052-3742-b59a-616fd7c081dd | -2.8259 | -48.86303 | 2026-07-20 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1083334-f1ae-3461-a265-65bfd5cd420c | -4.66137 | -43.2263 | 2026-07-20 03:57:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9360c6f-e6d1-3b97-b521-93e49c19e708 | -4.66078 | -43.22988 | 2026-07-20 03:57:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12651292-ea72-3c65-884c-a7120e4a8c23 | -4.67005 | -43.22409 | 2026-07-20 03:57:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99018ff4-93d2-3435-a8a4-99d4602753d6 | -4.6257 | -39.673 | 2026-07-20 03:57:00 | NOAA-20 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b993af22-5d2a-39c9-b37d-ad1f588b3883 | -4.84181 | -42.73605 | 2026-07-20 03:57:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f8aff25-d319-3382-ac79-dd3a42ab527d | -2.83199 | -48.86407 | 2026-07-20 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d2060d1-0d78-336a-a4e1-09f82b3e3c7d | -6.73624 | -47.21608 | 2026-07-20 04:00:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d42629ea-c9f7-35de-b6ac-7bc94e25a90b | -6.60013 | -41.63091 | 2026-07-20 04:00:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 86163117-2f1a-3089-99a5-acbd99ac2f85 | -5.62696 | -47.1034 | 2026-07-20 04:00:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2f906c26-c08b-31be-9dac-7ff993b4cc7e | -7.11978 | -44.02673 | 2026-07-20 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58f3d662-aadc-3b81-8b72-60245a9a058f | -5.70656 | -45.66158 | 2026-07-20 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18e4318d-95c3-386d-bc64-c08343a9003b | -6.6015 | -41.62263 | 2026-07-20 04:00:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ae01f4c4-9500-3785-8a6d-3532ede385b0 | -9.28509 | -50.33027 | 2026-07-20 04:00:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74c66dfc-9ae6-3951-b2f7-dbd38a253382 | -8.92717 | -47.60319 | 2026-07-20 04:00:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14d6e0bd-4258-3cc9-878d-98b4e3aa424f | -9.555 | -44.89761 | 2026-07-20 04:00:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5befb30-a524-384c-98a8-c5636566626b | -8.93785 | -47.60209 | 2026-07-20 04:00:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8c7f9f71-ed2f-3703-905c-33bf138cebe5 | -5.6327 | -47.10109 | 2026-07-20 04:00:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3dd52b47-2c01-33d6-b1d8-be759751d397 | -5.80306 | -43.64201 | 2026-07-20 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2597e754-43f4-3cc4-9f73-6852d7861040 | -8.93279 | -47.60112 | 2026-07-20 04:00:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d9a9161-ba81-3482-8299-da4e890445c4 | -6.74666 | -43.13272 | 2026-07-20 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55a00b33-6771-3845-9d5c-b749251d2116 | -5.79616 | -45.11645 | 2026-07-20 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 735017d8-a09f-3fa5-bbe7-a762fe1f6c41 | -8.94688 | -47.61001 | 2026-07-20 04:00:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f88cef8e-4926-3b82-9673-629e2b7bbbdd | -5.71127 | -45.66229 | 2026-07-20 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d895c2d-2d0f-3cd2-bf8b-0d27327a581e | -8.93223 | -47.60415 | 2026-07-20 04:00:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2090764b-293f-311d-b88e-559551ab5561 | -7.11917 | -44.03037 | 2026-07-20 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8fccf60-fc5e-3362-83ce-4e5da6ffd78c | -5.95507 | -38.63121 | 2026-07-20 04:00:00 | NOAA-20 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 73a57d19-09f6-38d5-87a6-6c8b36c28321 | -7.11566 | -44.02611 | 2026-07-20 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42103a0a-5e0f-35a3-84d0-71d261a2a62f | -6.72259 | -48.11298 | 2026-07-20 04:00:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3a8d7243-8302-3d1c-9a6a-f621f13c7814 | -10.80495 | -45.59331 | 2026-07-20 04:00:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93e6677a-7d4c-3252-87ab-83a4cda011ef | -6.86258 | -38.35072 | 2026-07-20 04:00:00 | NOAA-20 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3d53acd6-90cd-3dac-9fa0-26fddb1cfb62 | -9.11546 | -48.82005 | 2026-07-20 04:00:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70591d88-4f6f-3153-bb47-e4dd9a05545a | -7.9101 | -48.26218 | 2026-07-20 04:00:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ce8a333-3d75-3eaf-aa4e-0560842ae50e | -5.80246 | -43.64567 | 2026-07-20 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 932f1558-b2a1-3397-9024-f8a99d318f60 | -5.67259 | -43.57117 | 2026-07-20 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e9cb35ba-e017-3488-b5af-9bb5bc1d71a7 | -7.91551 | -48.26306 | 2026-07-20 04:00:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 329fcff0-373b-38a6-b757-487cfaa10519 | -6.74195 | -43.137 | 2026-07-20 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e93a894d-8fb5-392d-8759-3e332d6d6400 | -5.63218 | -47.1041 | 2026-07-20 04:00:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39671360-282a-319f-88c1-bfd9595fb234 | -8.93841 | -47.59907 | 2026-07-20 04:00:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e8cbc990-43ca-3dab-9528-2033bc4d2e04 | -6.59723 | -41.62617 | 2026-07-20 04:00:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fb3a689b-3323-3ecf-ba7e-ecc133161f9f | -9.11475 | -48.82379 | 2026-07-20 04:00:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3cc79f6-2c51-3398-a544-c286c7b45c7e | -9.60058 | -40.61064 | 2026-07-20 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| ccad686e-6e42-3027-8a3c-1834a02935a2 | -6.72195 | -48.11656 | 2026-07-20 04:00:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2f5ff964-4ce1-3024-a524-78f6853b3316 | -10.79286 | -50.23164 | 2026-07-20 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8a09ad0-c162-3ea9-88e4-92068307579c | -19.52494 | -40.24265 | 2026-07-20 04:02:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| eeddc192-28dc-312c-80e6-5d412a9afe39 | -11.97739 | -47.1059 | 2026-07-20 04:02:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7499fdf-77ec-37a1-bf78-5b6e8d4b8499 | -19.63935 | -40.05586 | 2026-07-20 04:02:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c117fd25-9562-35f4-b0ce-3166479cbc9f | -10.4623 | -49.09876 | 2026-07-20 04:02:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4ede30b6-eb2a-333a-831d-191b4c9cf902 | -10.46696 | -49.10003 | 2026-07-20 04:02:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 26f81f01-26ba-37a4-b420-3b50c755ab0a | -13.56115 | -47.77221 | 2026-07-20 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61d218a0-c32e-375a-b5b0-72e2817c7dee | -13.29444 | -44.6151 | 2026-07-20 04:02:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d561768-94a9-3efc-bc33-bf1fbf80a141 | -10.79949 | -50.22856 | 2026-07-20 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 935155b4-f8ff-3ec7-b924-1eb107382cea | -10.79893 | -50.22783 | 2026-07-20 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2cab237-d5a1-31ce-8f4c-3e6d8f0009fe | -12.35294 | -38.27674 | 2026-07-20 04:02:00 | NOAA-20 | POJUCA | BAHIA | Brasil | 2925204 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 1f24a873-07ce-3663-81ef-7368a1ccf692 | -10.46765 | -49.09634 | 2026-07-20 04:02:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 29ffe441-9fe8-3377-af82-92528a51d0a8 | -17.43931 | -43.05902 | 2026-07-20 04:02:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b32fb190-bead-3745-b963-5b23437f1d50 | -17.43951 | -43.05991 | 2026-07-20 04:02:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 449714c6-6ede-32ef-8343-f065e7f73422 | -10.68689 | -49.62296 | 2026-07-20 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d457afa-a37e-3ce6-8ac7-a3a45bf8b09b | -11.98203 | -47.10679 | 2026-07-20 04:02:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66b2d068-d1e0-35f3-9f99-c011cf2a4c17 | -16.81781 | -46.8462 | 2026-07-20 04:02:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 485e994a-8a72-3fdf-b0ff-c837d81f8076 | -12.94729 | -44.73167 | 2026-07-20 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 50d23575-5e51-39f6-bd47-a8eb315ed676 | -11.83437 | -44.77792 | 2026-07-20 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b7f1a80-4671-3be2-978b-a3de94ea9d96 | -10.4685 | -49.09594 | 2026-07-20 04:02:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 73560087-4db3-3226-b32f-a09745c5b091 | -11.82826 | -44.76589 | 2026-07-20 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0200c6a-bd01-304f-87f9-5e296ff09e6e | -11.38585 | -47.50349 | 2026-07-20 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2dd746b2-143a-3caa-b578-17c999cca39a | -16.57755 | -50.31253 | 2026-07-20 04:02:00 | NOAA-20 | FIRMINÓPOLIS | GOIÁS | Brasil | 5207808 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25c58280-36e9-32ce-8948-e73d215e7ac7 | -11.8295 | -44.75893 | 2026-07-20 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ccd3bddd-0246-346d-b6b3-1e9bdf99c444 | -11.83373 | -44.78151 | 2026-07-20 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edc5b33a-88b1-363c-8fa0-34502b92d489 | -10.46301 | -49.09511 | 2026-07-20 04:02:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 81567fad-cc66-36f7-b83b-47540751c2eb | -11.81488 | -44.77149 | 2026-07-20 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81907834-a25d-3c78-91b5-07270260447b | -11.83161 | -44.77023 | 2026-07-20 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d882b15-1913-3fc5-b4ec-5a63a5b320cb | -10.46217 | -49.09546 | 2026-07-20 04:02:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3ea9c9fc-0a47-3231-b06a-b7697dcd816f | -11.80179 | -44.32384 | 2026-07-20 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 470d3d80-cd33-3e65-8703-f056a310b66d | -10.79367 | -50.22739 | 2026-07-20 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72592e92-ca46-3de5-a31e-f349f004cdd5 | -11.38103 | -47.50259 | 2026-07-20 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4df08aea-a6d2-39d8-b278-194b43e4e67d | -11.39061 | -47.50477 | 2026-07-20 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1da2fe7-c6f7-30f8-a4c2-9dd6e942f47a | -11.83038 | -44.77713 | 2026-07-20 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b0db835-09b8-34d7-921a-2d6e9bc31b21 | -11.39437 | -47.51148 | 2026-07-20 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82c02f34-3dc8-3f62-9104-5c9c64e46731 | -10.46778 | -49.09962 | 2026-07-20 04:02:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c620a8a9-4498-3b67-8026-efccddcd2e04 | -11.79479 | -47.10151 | 2026-07-20 04:02:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README3.md)
