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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c872015f-4ded-3b0f-89c1-5fbfc3cc79d9 | -6.97513 | -39.69396 | 2025-10-18 03:10:00 | NOAA-20 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 095aff4d-c5c7-3df8-b978-c247defb34d6 | -7.54714 | -37.79541 | 2025-10-18 03:10:00 | NOAA-20 | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 110431dd-43a1-388d-8524-2abd3e186ab9 | -6.97758 | -39.68796 | 2025-10-18 03:10:00 | NOAA-20 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 9e9cefd7-6ca2-36ce-bbc8-ebdd4f9f5046 | -8.60677 | -40.20471 | 2025-10-18 03:10:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 10.5 |
| f3be1e80-1c9a-3e66-8f6e-895715aecf35 | -7.82116 | -40.21811 | 2025-10-18 03:10:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e4b13d8e-eb85-3424-8469-1b43a39607b5 | -7.54686 | -37.79569 | 2025-10-18 03:10:00 | NOAA-20 | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 99926430-efe5-3f81-8ee2-b0fd3a2e1286 | -6.98154 | -39.69592 | 2025-10-18 03:10:00 | NOAA-20 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b0d9a531-d66a-350e-a897-8c5b6dca2a72 | -10.61851 | -42.31325 | 2025-10-18 03:10:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 01c58e90-c2c7-3366-b27f-a9dca1715604 | -7.02166 | -38.50846 | 2025-10-18 03:10:00 | NOAA-20 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 55a64764-54c6-3e91-b085-8743bce6ccf3 | -7.54758 | -37.79168 | 2025-10-18 03:10:00 | NOAA-20 | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| df1e00ac-9a04-3f52-8806-d82a824bf3b8 | -8.61441 | -40.20036 | 2025-10-18 03:10:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 13.6 |
| c0ac1159-5119-3d8a-a554-ac245805f6b5 | -7.82244 | -40.21129 | 2025-10-18 03:10:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9af05be0-704f-3fe2-a778-6da3bdb3b16b | -6.98466 | -38.43669 | 2025-10-18 03:10:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1deac4ef-a154-3c5d-9915-980bea5c2e05 | -10.63435 | -42.30905 | 2025-10-18 03:10:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 89e1e528-cffd-37d9-81bf-1e39f732a682 | -8.61334 | -40.20603 | 2025-10-18 03:10:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 613f9c6f-705e-3b1b-af89-bf49c7b0cd36 | -6.976 | -39.68939 | 2025-10-18 03:10:00 | NOAA-20 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f5397fdc-8bce-3d9c-9d00-aa8ccd1bd449 | -8.22993 | -39.04369 | 2025-10-18 03:10:00 | NOAA-20 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| eed1a46c-77e2-3814-b909-22049f2359a1 | -10.62566 | -42.31482 | 2025-10-18 03:10:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2fc09540-f737-3b24-9796-222c2d24a880 | -10.61776 | -42.30626 | 2025-10-18 03:10:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| edb8e285-443c-3974-8bec-130c9d813ab8 | -8.60131 | -40.19748 | 2025-10-18 03:10:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 9.6 |
| bb7cf9cf-6018-3e72-9302-da1e9693c4d1 | -10.6234 | -42.31519 | 2025-10-18 03:10:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| a7c8ab5c-defe-35e0-869a-3d2a34428671 | -15.79637 | -43.57366 | 2025-10-18 03:13:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 93290321-132a-3c0e-87bc-200de91ec68d | -16.20093 | -43.68979 | 2025-10-18 03:13:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33646e5e-109b-30d2-86f7-6aa4b0189ca7 | -18.40665 | -41.83032 | 2025-10-18 03:13:00 | NOAA-20 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 20c6c09d-a966-371f-a050-b9703066981e | -13.95884 | -41.72236 | 2025-10-18 03:13:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6caaa7a5-5a8b-37ff-88f0-c7312ba53ae8 | -13.71021 | -40.98993 | 2025-10-18 03:13:00 | NOAA-20 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 6ad9f1e3-59fd-3163-becc-4b7a35876be3 | -16.19717 | -43.68647 | 2025-10-18 03:13:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c94b8da6-e9f1-3f1f-8e20-0a7c08626ca9 | -18.3912 | -41.84237 | 2025-10-18 03:13:00 | NOAA-20 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 963b54b9-5ad3-3c5e-b47b-1be1162022e5 | -18.40432 | -41.84095 | 2025-10-18 03:13:00 | NOAA-20 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 3952e84e-2fb7-3944-b70c-66e3d9c659e8 | -15.77423 | -41.33789 | 2025-10-18 03:13:00 | NOAA-20 | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4e421bf4-5aaf-3e4c-992b-7314302a5ac5 | -15.77264 | -41.33385 | 2025-10-18 03:13:00 | NOAA-20 | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 93470d8a-bf6e-3ddf-82d2-df23328b62e3 | -12.91656 | -41.83824 | 2025-10-18 03:13:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 07337b4f-8819-39d8-9855-857f1acf6907 | -18.40067 | -41.8284 | 2025-10-18 03:13:00 | NOAA-20 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 1ec222a0-5df3-38aa-bde4-290387ff0066 | -18.40099 | -41.82662 | 2025-10-18 03:13:00 | NOAA-20 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2242ff5e-3bd2-3678-98ce-9ddc635136d0 | -15.77155 | -41.33878 | 2025-10-18 03:13:00 | NOAA-20 | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d322f214-285e-3dff-b3a4-7b475246170e | -12.91512 | -41.84504 | 2025-10-18 03:13:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c626d2bb-7abf-3e80-82d5-026c76bd9ec2 | -13.70826 | -40.98863 | 2025-10-18 03:13:00 | NOAA-20 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1686307d-03ba-3d2f-9908-e1ed86546e36 | -16.52859 | -43.68472 | 2025-10-18 03:13:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 725ba9c4-e6b4-3664-bd88-2504731e5b1d | -15.7788 | -41.33543 | 2025-10-18 03:13:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e11f49f8-edb8-3001-ac74-3565a7d886f0 | -17.49266 | -43.46622 | 2025-10-18 03:13:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b230f9c3-20bc-3e52-94ac-a38bb5d6a6fe | -18.3961 | -41.84922 | 2025-10-18 03:13:00 | NOAA-20 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 2dce8fbf-07f9-3fce-86bb-89c407aac17a | -18.39982 | -41.83174 | 2025-10-18 03:13:00 | NOAA-20 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| d35f4ea9-1435-33e7-8c7a-eea2ce1f1cb1 | -15.79797 | -43.57983 | 2025-10-18 03:13:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e30dd481-f68a-3a52-ad68-b4bfaeec5d75 | -18.40545 | -41.83579 | 2025-10-18 03:13:00 | NOAA-20 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 0e461620-b021-3ee3-b435-2d602be6d7aa | -13.95761 | -41.72813 | 2025-10-18 03:13:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e47561d1-2e06-389d-b7da-c6ecf9980fd6 | -18.40578 | -41.83371 | 2025-10-18 03:13:00 | NOAA-20 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| 42416721-9466-363d-aa13-78b1960bcfe8 | -13.70728 | -40.99333 | 2025-10-18 03:13:00 | NOAA-20 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4fc2a8a0-53e3-35d8-9ea9-a92e1ef418a1 | -18.39827 | -41.83937 | 2025-10-18 03:13:00 | NOAA-20 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 4b9195da-d33f-344a-9c3e-c3813ec82a8f | -18.40457 | -41.83905 | 2025-10-18 03:13:00 | NOAA-20 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| 37d660a9-20fd-3798-bbd0-69184f0d5102 | -18.39947 | -41.8339 | 2025-10-18 03:13:00 | NOAA-20 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 30b74ca6-1557-3c96-860a-998f8c81aa8e | -15.78142 | -41.33464 | 2025-10-18 03:13:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 442e5e90-dfce-3ad9-aebd-8d7f19c10091 | -16.53022 | -43.67761 | 2025-10-18 03:13:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc72ef34-9dde-35c5-aa24-153f88ad7f88 | -16.20381 | -43.68972 | 2025-10-18 03:13:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6220f69c-1505-3543-8022-05a71c74c502 | -15.79957 | -43.57277 | 2025-10-18 03:13:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1a57ed30-7ca5-37da-ab42-730a73fd1db1 | -17.49097 | -43.47366 | 2025-10-18 03:13:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4bec8d9-7bae-3c42-8271-e830e937f56c | -18.39852 | -41.8375 | 2025-10-18 03:13:00 | NOAA-20 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 0afaba74-78f6-384c-b6fc-c8d8c3a8643c | -16.20215 | -43.68462 | 2025-10-18 03:13:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c327dd4-8b4b-3930-b0ef-084f84de036a | -18.76535 | -44.46674 | 2025-10-18 03:15:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b2c82a28-c400-3ad5-805d-f7317e92fec5 | -18.74049 | -43.71193 | 2025-10-18 03:15:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8d64fccf-c34f-3b00-b58a-0bbb27f46304 | -18.74241 | -43.71179 | 2025-10-18 03:15:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c02f0a5f-8ab4-386d-b535-e1b81ed27d87 | -20.69799 | -42.58114 | 2025-10-18 03:15:00 | NOAA-20 | CANAÃ | MINAS GERAIS | Brasil | 3111705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 970d87e2-6f72-3ca7-aa24-cb017ae1d2c2 | -18.77226 | -44.46875 | 2025-10-18 03:15:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6604aff0-124b-3a75-b437-a76309934c92 | -18.4163 | -43.70994 | 2025-10-18 03:15:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| faabfc4c-ec8e-32a1-b0e6-4532b64a2950 | -18.41904 | -43.70459 | 2025-10-18 03:15:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d231438d-11a0-368e-980d-d1801b913443 | -20.69863 | -42.57725 | 2025-10-18 03:15:00 | NOAA-20 | CANAÃ | MINAS GERAIS | Brasil | 3111705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 44492f3f-37db-3f6d-8eef-a64f828e9e43 | -18.4172 | -43.71235 | 2025-10-18 03:15:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 081c4e4b-4e62-3216-806f-50abb68e1793 | -20.69925 | -42.57567 | 2025-10-18 03:15:00 | NOAA-20 | CANAÃ | MINAS GERAIS | Brasil | 3111705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3e60accc-72f8-3ca2-89ee-a1b2f662c8b0 | -6.7377 | -44.3675 | 2025-10-18 03:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 111.5 |
| ce0b6fc9-9cb7-3cfe-a68a-3e47d6103cb1 | -12.5944 | -52.8223 | 2025-10-18 03:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 1fb92cab-54b6-3fbf-a26e-775815953291 | -5.0214 | -46.032 | 2025-10-18 03:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 128e3735-9c6c-3557-a55c-2f1c4b4303c3 | -12.6138 | -52.7993 | 2025-10-18 03:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 7b230d83-90e6-3811-9b3e-bf7b5e19aab8 | -11.204 | -47.8318 | 2025-10-18 03:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 2f3d55ee-2fbc-3d8e-9cc6-78b90e52874f | 1.7664 | -55.9608 | 2025-10-18 03:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| f2a906e4-dccc-3583-8051-5793eec933ef | 1.7664 | -55.9805 | 2025-10-18 03:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 558eaccf-c9ae-3298-9e1f-30fa89611175 | -5.0215 | -46.0097 | 2025-10-18 03:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 63219e9c-e32b-3022-bf29-0b33f4e2f473 | -11.6109 | -44.0678 | 2025-10-18 03:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 40a824db-70f8-3ee9-9a40-bdc142ad5af2 | -12.6135 | -52.8202 | 2025-10-18 03:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 92.0 |
| a4f46cc7-2f0f-3ff8-9431-046e61f40e86 | -10.4941 | -43.4315 | 2025-10-18 03:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 14b4d72f-69f0-39b0-8760-c7bf977f5f5c | -3.1431 | -50.2464 | 2025-10-18 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 0f301658-0ad1-3a42-aee4-6613f247d3f7 | -10.4937 | -43.4552 | 2025-10-18 03:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 06661b4d-b9f8-3cc2-a576-e9dac759eb89 | -12.6138 | -52.7993 | 2025-10-18 03:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| d785833c-7e70-3b2a-91fc-496421b46429 | -11.6104 | -44.0913 | 2025-10-18 03:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| c31b7ab2-4ead-3652-b801-313aaccba6e3 | -3.1431 | -50.2464 | 2025-10-18 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 2c778dbe-b46e-3b51-88a0-e85bdd5ef6e1 | -10.4937 | -43.4552 | 2025-10-18 03:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 4c5cc9a9-6e2f-3041-84b8-d55611a97f25 | 1.7664 | -55.9608 | 2025-10-18 03:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 125.7 |
| 99cdf3c8-f784-3d3e-9735-0308a3f1a597 | -19.1114 | -57.5486 | 2025-10-18 03:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 56.6 |
| 36590183-5f96-37ed-b01c-0cf9b393d809 | -5.0215 | -46.0097 | 2025-10-18 03:30:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 4985a582-3030-3217-8e1e-a8e8cded578f | -12.6135 | -52.8202 | 2025-10-18 03:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 4244eefe-61f6-3712-b970-79a147b05c10 | -11.6109 | -44.0678 | 2025-10-18 03:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 81294a45-93fc-3254-9404-46fb1dfae6e5 | -10.4941 | -43.4315 | 2025-10-18 03:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 827a2b31-27a8-3106-bcbd-ed25a1c80338 | -5.0214 | -46.032 | 2025-10-18 03:30:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 79.8 |
| bfe87658-ff9b-3f00-adcb-be2154c36be7 | 1.7665 | -55.9411 | 2025-10-18 03:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 7b8e3b40-db7b-3082-9769-50ce676eee3a | 1.7664 | -55.9805 | 2025-10-18 03:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 126.2 |
| 3d716e4f-f1f4-3512-8a51-a6b4db7b0da8 | -10.4941 | -43.4315 | 2025-10-18 03:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 162.5 |
| 61cdae38-a2f6-3ee9-adfe-3699d416a4b5 | -4.4445 | -43.2397 | 2025-10-18 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| a6fc65e3-52f1-3fae-a3ed-8a14bb78dd94 | -11.204 | -47.8318 | 2025-10-18 03:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 22814023-d44d-312e-9eee-12b13f225ba7 | 1.7664 | -55.9608 | 2025-10-18 03:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 69e9f98f-8cd3-3131-9dc1-c9952da570c6 | -19.1114 | -57.5486 | 2025-10-18 03:40:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 55.5 |
| ae5b817a-ba94-39be-890e-d5c8c9ff0fd9 | -18.4094 | -41.8387 | 2025-10-18 03:40:00 | GOES-19 | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.5 |
| 59a3a683-bf05-30c7-a191-db18abfa4a61 | 1.7664 | -55.9805 | 2025-10-18 03:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 113.6 |


[Clique aqui para ver as próximas entradas](README12.md)
