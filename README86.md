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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44f898cb-662a-3880-84e7-928d1199c119 | -7.05317 | -45.2024 | 2025-09-30 05:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 58d92bb6-6ace-364c-b915-45349bc115dc | -11.45502 | -51.50528 | 2025-09-30 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fff08591-a799-3cdd-9299-303b30beafd2 | -11.20357 | -53.298 | 2025-09-30 05:08:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a1b128a-1e22-396c-9467-e748bbdc3e8e | -6.7055 | -44.55807 | 2025-09-30 05:08:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 852ce428-4cf2-3e6f-af41-ee5a701d67e4 | -11.88507 | -48.04202 | 2025-09-30 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ac39199-6772-39d2-8444-c779666dccb1 | -10.19622 | -44.89834 | 2025-09-30 05:08:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 08419e73-8609-3e58-8c61-bdb4b6dc0823 | -9.51511 | -47.69587 | 2025-09-30 05:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a29fc0d1-971a-3936-a23a-8be529aec7b7 | -9.31091 | -54.51173 | 2025-09-30 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd6acaa1-f760-3fb8-861a-2b4a93cf0b3f | -13.24326 | -48.44454 | 2025-09-30 05:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2aeef067-06b7-3693-8363-9e283fc77af7 | -11.06858 | -47.81923 | 2025-09-30 05:08:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d88aec05-d22b-3e73-b593-be18b2bfb18f | -13.39844 | -48.07084 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6402e092-982c-3bc1-8b98-21665932cef7 | -11.25212 | -47.22178 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1814c71b-08c3-3333-b6e7-3bb0f553cf93 | -10.06687 | -48.19083 | 2025-09-30 05:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 086a1800-e786-3cb3-939b-a6f009a44c87 | -7.36696 | -47.04745 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e26d124d-430b-3499-868f-3ff042db59f4 | -10.89268 | -53.75071 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ad2e529-71a5-3da7-898a-a69a6e5f2116 | -12.44554 | -54.47558 | 2025-09-30 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf032d3a-42ba-3036-befb-dd0fdf27c977 | -9.40904 | -54.71446 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d078d38c-be56-33b7-ab39-ae35d393974b | -8.64927 | -46.60851 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f65cdac8-d4e8-3cd3-ac39-5cf02e018a46 | -13.23797 | -48.44422 | 2025-09-30 05:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4674bd7-6302-346a-bdea-c569cc19f39a | -9.42045 | -54.70863 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1704c4cc-406f-3373-a577-69f51ce64d6f | -8.06147 | -54.86307 | 2025-09-30 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c27cb89-67ef-3105-ae48-8b96c26f4825 | -9.93544 | -47.46013 | 2025-09-30 05:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be00732a-2373-362d-810a-17ae5ab54dca | -9.05088 | -46.69876 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 617829b4-e5ad-36bf-855a-59999821a65c | -11.2015 | -47.74262 | 2025-09-30 05:08:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 413788b6-0859-3973-8221-eea2c1c93393 | -8.32622 | -50.87641 | 2025-09-30 05:08:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 256b682d-5f8a-3b34-911c-57629793e4ff | -13.38615 | -48.06336 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6a18666-8ab7-32e7-aa9e-5d03e53d43ff | -11.20283 | -47.75169 | 2025-09-30 05:08:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 59b2a98d-4f9f-3fb6-8c44-0a54345c5205 | -9.02675 | -46.71002 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 56b97455-27d8-3cc0-a0fe-dd1b8bf16c7d | -12.82138 | -47.00696 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 73e1d216-6fb0-36cf-8617-b6f2d0e90b29 | -13.205 | -50.94041 | 2025-09-30 05:08:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 287b879d-cb7e-3256-a390-685bf6d7c65b | -11.28136 | -57.86732 | 2025-09-30 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fc0d589c-1180-3e47-976e-3fe769a718d3 | -10.61792 | -54.94971 | 2025-09-30 05:08:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4b591fe3-ef73-301f-9be9-52bd482caf49 | -9.40105 | -54.72084 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebb210a6-6aee-34ee-8a8a-43ae80569e8d | -8.87736 | -46.66133 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 86dee6d9-85c7-35a5-9e7e-78414a0ae724 | -11.67009 | -50.97187 | 2025-09-30 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0148d5a2-c677-3cb0-8d7a-30d0384956ad | -10.88325 | -49.39793 | 2025-09-30 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21219a39-abc4-3ae9-b30d-4a9c393218d8 | -7.3665 | -47.0507 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a614ef5-2392-3eb4-8009-304706ab98a9 | -11.15757 | -54.12082 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 9db91443-87b0-3dd6-8c3c-1bafcb8701c9 | -13.37361 | -48.16449 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 51df1922-ceac-3935-bcca-9edfc1a82829 | -10.71175 | -53.79767 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be7f7596-a066-3b6a-8364-68cb9711e461 | -11.62921 | -52.84523 | 2025-09-30 05:08:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e9a334c-4957-3d9b-9449-446afa976b2d | -8.87479 | -46.6381 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2abeb680-af63-34a2-a7e7-3171cc8439ec | -8.86386 | -46.59201 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b67b0bd7-d335-36f7-b931-41ba76bfafa1 | -10.0292 | -52.10877 | 2025-09-30 05:08:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e33154c1-6adb-37f1-9487-221b8eff2530 | -9.32561 | -50.63116 | 2025-09-30 05:08:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 880c8514-748c-3aec-bdea-dd641c1fefb1 | -8.8634 | -46.68102 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 31b6617b-a5d3-38e8-b3a3-e1370e25df5d | -7.79407 | -54.94348 | 2025-09-30 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7230159e-7a08-3cbd-aaad-01538b971ad1 | -6.72613 | -47.2067 | 2025-09-30 05:08:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 075235f0-8a41-3428-9c94-e01fd202959c | -11.90455 | -48.05796 | 2025-09-30 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42a15cea-ab74-337b-b266-6eb93c63a6ab | -13.21262 | -47.32648 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 09277689-462e-3a67-97e8-8ed7b5735240 | -12.7877 | -46.89665 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6efa8e6-8e93-3820-b144-35d0de8e1c96 | -9.0615 | -46.70417 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 093dde15-3ac5-32f4-8f69-c555141846ed | -8.1438 | -46.37629 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 80884dda-71fb-396f-91e6-8eef913a46e3 | -9.39589 | -54.70865 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7eb84de7-a841-37fb-b29e-ce129c518311 | -10.65505 | -48.53581 | 2025-09-30 05:08:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73be5c73-3acb-31e6-a406-7ac7da428523 | -8.11221 | -54.871 | 2025-09-30 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ce1b2e4d-04c0-35f0-8e5c-00c1c62af827 | -9.39875 | -54.71289 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d892021f-8a2b-30a8-acea-8a716b5843dc | -8.50526 | -47.2557 | 2025-09-30 05:08:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52b50a53-176f-3310-9e6d-c7b1ee4cc9aa | -10.95995 | -46.50587 | 2025-09-30 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e80ad33d-c0cf-3bde-9e34-301690ac0d66 | -10.10433 | -47.79203 | 2025-09-30 05:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51f34f98-3a97-3659-a14c-7a8f0a1682f3 | -7.20951 | -45.47731 | 2025-09-30 05:08:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6d4c9db-59fd-3764-9e57-4d4b1c734642 | -9.12271 | -47.64313 | 2025-09-30 05:08:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b2d0807-15bd-3d4e-9990-ef4aeb2d3701 | -8.87331 | -46.64919 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a4a855a0-4062-394d-ac4e-6fcadae494e4 | -10.83036 | -47.97328 | 2025-09-30 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f598727b-2210-3de6-8db7-3947632e0682 | -10.89031 | -53.74178 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1cd41f6-e20a-3f80-afd2-ecb378a7f7e7 | -13.5778 | -48.09678 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d620f35c-b287-3791-9422-041974cef490 | -10.41184 | -48.17317 | 2025-09-30 05:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2de507f9-9e90-3076-acb7-fcd92e9305dc | -9.40787 | -54.69904 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e87edf8e-1c5f-3374-8d6e-a575ef0ee7a6 | -11.89242 | -48.02665 | 2025-09-30 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f787aa7f-6ad4-3d1e-bdb9-4291ddce880d | -10.82986 | -47.97709 | 2025-09-30 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 892aad01-9ec4-3035-b6ae-4a5131d5aaaa | -9.62629 | -50.89683 | 2025-09-30 05:08:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e59bc634-5f8b-36ee-8578-551780dfa7f1 | -8.87262 | -46.61177 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae0d7817-3bfa-33f6-9802-6676f07a86e0 | -12.86873 | -46.90388 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0499b784-6238-3b64-9bf8-354fcf07ecd5 | -11.14393 | -54.11456 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b93dea32-48e4-345f-922b-d12c091f67fc | -11.9932 | -55.29779 | 2025-09-30 05:08:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11eff940-cf4e-3e81-946c-d57b0e876f19 | -9.13005 | -47.62791 | 2025-09-30 05:08:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6b14d1d-d315-3b5a-9f40-5444ee4c5961 | -13.36106 | -47.81508 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5db5669-0710-37d8-b22c-a354f53b9e00 | -9.10202 | -62.68718 | 2025-09-30 05:08:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3f32149-3ace-3d2c-84e8-1533f905354d | -11.68025 | -44.3015 | 2025-09-30 05:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f214fd4-9b3e-369b-ada9-9c3c54180749 | -7.81514 | -46.99313 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 228a1fb8-fbe1-3ebf-a046-aa031494a952 | -7.70486 | -55.44882 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8ddaaa6-2148-33f0-b4c2-6bf2dd438bd5 | -13.23225 | -48.44729 | 2025-09-30 05:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63f9f47c-b667-32c5-9f18-9ea9292af5d4 | -13.64035 | -47.33826 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8eb76734-d4fd-340d-8d40-cd78f0ca6e97 | -12.02666 | -47.89566 | 2025-09-30 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c893911-f574-3a07-b0a0-f3b10e7f585c | -9.4113 | -54.69957 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d2edd9b-c32b-3e5f-9237-874a51feffcc | -10.072 | -50.22101 | 2025-09-30 05:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 5cf5bffa-3d8e-3278-9c75-3ea82eedf486 | -6.50215 | -44.26485 | 2025-09-30 05:08:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 71cb674c-7320-3fc2-9c62-2bc0991b4a01 | -13.39267 | -48.07335 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed466150-7dba-318d-a617-9855fdd74fc2 | -12.78727 | -46.89822 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b6fd35f-3cab-31ff-8f8a-8952de834fe4 | -10.62644 | -53.69254 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60bd59dd-1c5a-3668-8a93-c840d324ef98 | -9.09764 | -62.68642 | 2025-09-30 05:08:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8942a86-3d1e-3a8a-8e9e-844c6f95f848 | -11.2567 | -47.22999 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1fce3f8d-5eaf-3626-8bed-a068f7e63bd7 | -10.89456 | -53.73809 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 716ffc89-a69e-35db-864d-e54591f77559 | -7.92249 | -48.18592 | 2025-09-30 05:08:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8f0e39a-4ec4-3e8a-8a5f-9801fd8ca60c | -11.06763 | -47.82653 | 2025-09-30 05:08:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 48556b4d-0b1c-3e83-b8ac-13649829bb1d | -13.41021 | -48.15615 | 2025-09-30 05:08:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3abb7a86-2a64-3226-98fa-05dd393ba710 | -13.57078 | -48.06425 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dcccb138-f92f-35c5-a02a-e67690971f79 | -10.08104 | -46.06219 | 2025-09-30 05:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8f67ca53-209d-3802-87ac-02fecf7df543 | -13.39882 | -48.06758 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8511e56e-3ef6-3757-b85a-175a78e8a83e | -11.06232 | -47.82582 | 2025-09-30 05:08:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |


[Clique aqui para ver as próximas entradas](README87.md)
