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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6866f037-be0f-303d-b040-29a62df17c08 | -10.32491 | -46.38334 | 2025-09-07 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48ce43ba-0e31-328a-8cc7-a418c026d872 | -12.87278 | -47.99083 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0bd98d17-33ef-3d01-a383-14905ed9be87 | -6.61293 | -53.15144 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b0c0e0b-9323-3525-8bbb-3df601af8d67 | -6.27043 | -43.49299 | 2025-09-07 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 1cb5a220-d493-3baa-8add-05ee180ec13b | -10.58313 | -48.47121 | 2025-09-07 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92f90f93-4023-3350-9605-9f80171e37dc | -11.58105 | -47.75936 | 2025-09-07 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54b532ca-580c-3cf5-b1ee-cae769ad4a00 | -7.73265 | -50.31533 | 2025-09-07 04:19:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dcc06000-6cae-3126-a15e-bb78587520f5 | -8.31007 | -44.9743 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f862b47c-90b1-3f4a-969e-f0f7d8b4d4ac | -6.08161 | -43.31031 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bab9a79d-471c-3922-b1d1-a92c4d9323d4 | -6.08943 | -43.2822 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 62ed5a70-c259-3939-a782-7b78f0c24a96 | -6.19371 | -42.63183 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9ec4a589-6518-3bc1-ba1c-e036be804e75 | -8.34429 | -48.27068 | 2025-09-07 04:19:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de377aef-a7f4-3695-9f4a-6dfd33aebeb7 | -6.80072 | -47.06913 | 2025-09-07 04:19:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c990f4c-4c05-3055-998a-13ef5e78b4f5 | -8.33863 | -48.28259 | 2025-09-07 04:19:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b71ec3d6-3fa6-3988-a0bd-3e7f4cad1f82 | -5.69021 | -48.13852 | 2025-09-07 04:19:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8be8bf09-68c1-3ca2-b87e-991fc3d474cc | -10.34794 | -46.45257 | 2025-09-07 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a41134db-3f61-3dca-bade-dcd39ded3cad | -6.89363 | -45.59634 | 2025-09-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4033009d-e4e4-3e63-a253-bb3f6413fda9 | -11.18052 | -55.0492 | 2025-09-07 04:19:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbb29507-89c8-3746-afc0-d7f3aa7ad419 | -4.89817 | -49.92857 | 2025-09-07 04:19:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f09f7e1d-32a8-306e-b0e1-5cff59f8ce8f | -6.24879 | -42.43568 | 2025-09-07 04:19:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 30b57705-b226-3288-bd61-cc30c7ab8df3 | -13.00404 | -45.21285 | 2025-09-07 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31fb3363-fd75-3df0-bc68-9a4e4d51e2ce | -5.88515 | -43.41925 | 2025-09-07 04:19:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75a31840-7c8b-3eb8-b023-1df883b08b55 | -8.1845 | -44.77989 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| faf6e61c-ab53-3c0b-8564-02e370efbb6c | -11.15753 | -48.37398 | 2025-09-07 04:19:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81943b06-c41c-3feb-8be4-c5962316f56f | -8.65014 | -45.74526 | 2025-09-07 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7746e96a-557b-37d0-82e9-51fed84024e3 | -6.14389 | -44.2374 | 2025-09-07 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 805a01d7-4673-3b16-9e9e-27644a1257f1 | -8.14867 | -44.85583 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 043146a1-9ae4-32c0-8500-1433c13038ea | -8.11411 | -45.31313 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c376071b-f371-3f7e-8ff3-c2eb8b1d1f01 | -7.72917 | -44.60796 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4d223ec-f4b9-34ea-bed7-42f3e215d0d5 | -11.35652 | -45.57564 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8866a92b-86ab-3005-bae5-ca87eb1ee4e7 | -12.54281 | -48.07668 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19af9a17-b55d-37ec-b684-675c92bc5de6 | -6.38049 | -42.98569 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 89456755-86d8-3bf9-af3a-ca9068481f06 | -6.54622 | -42.93483 | 2025-09-07 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 508a2f8f-45ca-3432-aecd-3c59d0f70482 | -9.87159 | -53.81741 | 2025-09-07 04:19:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3aecdc7-526d-3e9d-9b7b-cf7e6eb1bcb9 | -6.18913 | -42.63872 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b036ec1b-dd94-3c2b-ad63-c40c4d391eb4 | -6.84068 | -52.85356 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5e6647e-8d5c-3c11-84af-17cab4908fe4 | -8.89169 | -47.25698 | 2025-09-07 04:19:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19a61b54-456d-3cb6-b166-5442311f19c5 | -6.2009 | -43.58762 | 2025-09-07 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a615452a-5299-30b2-a54f-c64990bb9550 | -11.83452 | -47.56001 | 2025-09-07 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 669955a7-4f3f-3fd0-8352-afc8c803faec | -7.63603 | -46.75843 | 2025-09-07 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d0f33b8-d93d-392e-b2d1-0d3f1dda7b94 | -6.19756 | -43.58708 | 2025-09-07 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9402d4c5-9787-37ca-89ba-cc981d63776f | -6.52501 | -45.8411 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab488306-d1ff-30e6-8d0a-6c96b013e186 | -9.39001 | -54.77 | 2025-09-07 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a87eb30-ffc0-30af-bc3d-458dcb85c498 | -8.50074 | -45.05764 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed565138-074f-3a23-affe-d379ac2e6b75 | -6.43707 | -43.62 | 2025-09-07 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e4e8c89-bb98-3b81-b3b1-4b6dc119e413 | -6.21031 | -42.6382 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 34f61432-e0c9-391e-8fe1-45d18e3d430a | -6.27523 | -53.44228 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e8f888b-eb86-3cfd-80b6-a306972d52e9 | -5.96779 | -53.5975 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f9152e4-5096-344a-b2fe-d4b75dafd4d0 | -5.89992 | -51.94107 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c1731418-add9-3a9b-944e-5833fa212ce4 | -6.19592 | -43.59768 | 2025-09-07 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3bed74b0-60e9-32a3-806c-8dc46befff82 | -8.46079 | -47.33959 | 2025-09-07 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e9ccc75-6d09-3210-a890-30cc2673a5c1 | -12.85236 | -47.9873 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88b07e7c-7e1d-39da-a99d-0c65433cc176 | -11.84287 | -47.57288 | 2025-09-07 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75258cfb-b112-323f-a8f0-f3ed0b642d76 | -7.40477 | -44.94382 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c52ab4d6-8731-3d84-bf2d-32c02fd7e70a | -6.30252 | -51.41047 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 401eddf6-6c90-3abe-ad2f-0480b371a51c | -9.08016 | -45.86095 | 2025-09-07 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 717ca3f8-f9dd-35e0-adec-90c1b00f4b05 | -6.19325 | -43.37876 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 007e9e4f-d001-3328-8cff-191cade40254 | -7.59191 | -44.66109 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38cd4588-6129-38fe-8070-8b36bf9cc455 | -7.73328 | -50.31164 | 2025-09-07 04:19:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4eac9caf-f677-3dae-9e57-63a195c42b03 | -6.14057 | -44.23687 | 2025-09-07 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 67c8f0bb-f2c1-3969-856a-1c306b8c2be4 | -10.72474 | -48.59779 | 2025-09-07 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32dc693a-f561-3c37-b3dd-f62dee1fb315 | -6.84169 | -52.84794 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d87ae41-2deb-3c09-a6c9-a2aa32d94c73 | -9.99137 | -51.63095 | 2025-09-07 04:19:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ced122ac-70ce-3e3c-977b-51ff8b040b13 | -5.61416 | -48.10109 | 2025-09-07 04:19:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff2a94b2-8d9b-3b83-847c-678608de82be | -10.84113 | -55.10107 | 2025-09-07 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6a7ea5f-1d65-37b4-adbc-0735cf1cceec | -6.51181 | -43.11356 | 2025-09-07 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3cf54eec-08a6-3b53-b518-6d55f7017d29 | -6.20781 | -43.37368 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cea452f1-d015-31d8-9d32-7747dcfad23b | -12.79426 | -48.02114 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 53e9cfe5-7afe-3766-949a-90fe5abd281b | -8.29233 | -45.38789 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ddc38da-846f-32e7-bc87-af517f86738e | -6.51713 | -44.71449 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90eca21b-d503-30a8-9c87-100b3b89d2e2 | -8.44669 | -40.60264 | 2025-09-07 04:19:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9b5ee358-c010-39bc-8e82-1e30ba657a4e | -11.21254 | -55.0184 | 2025-09-07 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f31c38d2-a79e-3234-8b63-492c989903a2 | -8.35149 | -48.27188 | 2025-09-07 04:19:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02637187-74e8-32e9-9a90-25f88bb73016 | -6.65979 | -44.80118 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e2e51a6-16da-3011-bb61-03f3d5e9d078 | -8.02244 | -45.44074 | 2025-09-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38413db7-c318-34ca-a496-978cd4db35e8 | -8.44494 | -45.0239 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 65760ba7-da2f-3e34-85b0-f09ba8fbc22b | -9.59101 | -43.32867 | 2025-09-07 04:19:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cfda294d-a5ed-3697-a7b7-4cae8d3da854 | -11.60111 | -47.15778 | 2025-09-07 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 007cd87c-7a45-3c98-b10a-a6dc85cd0905 | -11.57853 | -47.73186 | 2025-09-07 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62611900-56e6-36bf-8abf-76b5538eb7ee | -6.23024 | -43.29632 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f099b3a3-a2e9-37b7-a454-5922203a1761 | -7.01719 | -44.96742 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02822959-fa94-3ba8-a45f-ba890ac3d542 | -9.59305 | -43.7944 | 2025-09-07 04:19:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 63bf1270-e3f9-38e5-b881-49bae6aed5b4 | -5.58523 | -51.91036 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe99b1d0-b452-34cf-af39-b10954e9e25f | -6.22372 | -43.57296 | 2025-09-07 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44a334e4-ba07-3122-a8d5-ae1c2e411be8 | -6.86933 | -45.55634 | 2025-09-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2d0cf7f-d247-3011-86a2-457239c06bbe | -10.32547 | -46.37981 | 2025-09-07 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aedc8791-2ece-3171-b9ad-47506f3ffba6 | -10.78475 | -47.73697 | 2025-09-07 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03a25e56-b702-380d-b99c-a38131b0d162 | -6.20704 | -43.59219 | 2025-09-07 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9aacbc3-0dbc-30bb-be76-0d9ed6a1cd5c | -11.38722 | -43.54867 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42053886-1109-3056-9f1e-ef79c3ea1c7c | -6.94008 | -44.46552 | 2025-09-07 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 581ada12-8672-34e5-8682-06c85be74ff4 | -6.21284 | -43.36349 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10cf9b69-0ee2-33d2-b60b-cb8a416c5191 | -5.97303 | -53.5985 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4fd1ddd3-d9c2-35d9-8cd8-6ca1251a3864 | -6.83566 | -46.39808 | 2025-09-07 04:19:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b654e38a-0113-39d4-9722-2c0f058532d4 | -8.69752 | -54.68007 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3db2a91d-bca8-3170-91c5-7c93f33f0578 | -6.2364 | -43.27894 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 18627257-92a6-37e4-bbf6-ff22cdfbc14f | -12.29624 | -47.24609 | 2025-09-07 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a7c217e-a074-3f8b-8c2f-8ea5d13fbb22 | -5.80133 | -45.64973 | 2025-09-07 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f50ca8b-7fb0-38d3-90a1-c8c0465154bb | -6.22761 | -42.5948 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c6c08802-f1c3-3c60-bf66-f0a0713aa1e5 | -7.75239 | -44.0053 | 2025-09-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a483c73-a7f5-368c-8a5f-c25242f0f179 | -9.45748 | -56.05775 | 2025-09-07 04:19:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README46.md)
