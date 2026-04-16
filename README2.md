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
| fc4a245b-273e-3b18-b5aa-5c0cf2178203 | -20.17109 | -46.59494 | 2026-04-16 03:42:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fcf11d27-6508-3d57-9f71-a775e0ffa11d | -19.59538 | -40.08154 | 2026-04-16 03:42:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6d936486-18b4-32d2-aecb-8ba6c6bf5806 | -20.17816 | -46.58785 | 2026-04-16 03:42:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a38ff13-da68-38a5-9e96-0fcd36ad9e86 | -20.17019 | -46.59909 | 2026-04-16 03:42:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42889ea5-a74e-3176-9a38-d30a231249bd | -21.70625 | -48.42922 | 2026-04-16 03:42:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7bc7185d-74d2-3d21-8adf-8e3dbb244f65 | -19.12817 | -40.38297 | 2026-04-16 03:42:00 | NOAA-20 | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ab71ebfc-2452-318e-86f2-f470f2e45e1a | -21.18954 | -47.36955 | 2026-04-16 03:42:00 | NOAA-20 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 426332eb-b152-372d-9c52-df45f0c36118 | -19.58894 | -40.07572 | 2026-04-16 03:42:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5c2849c8-ddd7-3eff-b8d6-3a44756dc072 | -21.71217 | -48.43282 | 2026-04-16 03:42:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 656606a3-1697-37bb-878e-9b07a11994f6 | -19.92574 | -44.0696 | 2026-04-16 03:42:00 | NOAA-20 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 87771a24-7f4f-331e-9956-61ff0cc2156a | -21.70529 | -48.43351 | 2026-04-16 03:42:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 89fa2334-0e42-3b36-88fa-1e9437bcc398 | -17.67094 | -46.73508 | 2026-04-16 03:42:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 487bb05d-25eb-3bf1-aaf8-27e70a80c6d4 | -20.18801 | -46.59346 | 2026-04-16 03:42:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a5ccc642-28c9-3ce6-a9f4-210101a807f6 | -20.68443 | -49.40088 | 2026-04-16 03:42:00 | NOAA-20 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac7fe28b-89b3-3acd-a186-2dd70c3d4205 | -21.70754 | -48.42677 | 2026-04-16 03:42:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5371bd10-df65-3702-b09b-4e8c8c0e9764 | -21.70657 | -48.43093 | 2026-04-16 03:42:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9e5b38d7-d94c-3468-81a7-f6ea49f89e44 | -20.17733 | -46.5917 | 2026-04-16 03:42:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04a04c51-bf23-3bd7-8031-f0662a0e7cce | -19.59899 | -40.08226 | 2026-04-16 03:42:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 21b14f39-d417-34f7-b564-59ce624f17d9 | -17.33953 | -43.58282 | 2026-04-16 03:42:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be0bc00d-8b51-36f7-9b90-b83868f5dc97 | -19.12531 | -40.37766 | 2026-04-16 03:42:00 | NOAA-20 | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 89087c4f-359e-354e-a022-f75d21449acf | -20.1827 | -46.59245 | 2026-04-16 03:42:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ed50f3fb-2da1-3587-a75b-752a7c439a9f | -21.70718 | -48.42509 | 2026-04-16 03:42:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9d878131-6926-3286-8057-76c722a3665b | -17.67179 | -46.73111 | 2026-04-16 03:42:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9179543b-bd61-3b06-a69a-3491d2dc0b62 | -20.18353 | -46.5886 | 2026-04-16 03:42:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f5e166f-63c8-3e36-b861-1d4623849e5c | -20.53394 | -49.49503 | 2026-04-16 03:42:00 | NOAA-20 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9651c05-1fa4-32c3-883c-105a345f9abe | -8.36769 | -48.08346 | 2026-04-16 04:27:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| caa67a9c-1868-34f1-8f9f-4f1f00d77e3f | -11.16696 | -46.54237 | 2026-04-16 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7899f86-63bf-36f3-a3c0-c535da48a763 | -9.46261 | -47.80771 | 2026-04-16 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa2dfe98-fdc2-3526-a525-69464600a7fe | -11.42869 | -55.09827 | 2026-04-16 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e746b1a5-5cc2-3e00-be15-0ae6e78c9f90 | -8.92976 | -45.66359 | 2026-04-16 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 226e0a06-9954-3ed9-a095-78007fad98e6 | -11.90745 | -43.84142 | 2026-04-16 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1452a7c0-c079-3d8e-a3f0-56c7d6ab218d | -11.71277 | -44.74382 | 2026-04-16 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 217945c4-c1b6-316e-9649-0683cc8907cf | -9.45645 | -47.82491 | 2026-04-16 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 946e13f9-7ec9-36f0-a1e1-543fd36941a2 | -12.01577 | -45.34456 | 2026-04-16 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 508f6865-6c2e-3a00-aadd-3f20ec6ee94c | -11.84228 | -55.02298 | 2026-04-16 04:27:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12b86e5a-1708-34c9-b9ce-d826ac1a2a77 | -11.27767 | -44.45662 | 2026-04-16 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4875a8ff-8756-384a-b103-4fb50c3a7409 | -11.45511 | -45.16073 | 2026-04-16 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4d9a5d22-d6c9-399a-b6f5-6e45ed33653e | -13.37289 | -43.20216 | 2026-04-16 04:27:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 66c47868-f239-3cb2-a201-e1a552a43353 | -11.96161 | -44.013 | 2026-04-16 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f3237eb-a692-3a72-a679-f839b3f5c849 | -12.97172 | -40.68469 | 2026-04-16 04:27:00 | NOAA-21 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 56dc8e18-1005-323a-b56c-398399450049 | -11.96464 | -44.01789 | 2026-04-16 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2d3bf42-666b-32a3-9069-13d891d73d9b | -12.45697 | -43.78162 | 2026-04-16 04:27:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96bf93b3-a670-3b31-8788-68277c54f9f8 | -12.84481 | -43.81882 | 2026-04-16 04:27:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bf44dba9-db2f-39ad-a5d3-23dcf45c21e2 | -9.45368 | -47.82082 | 2026-04-16 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b37d6d69-280d-3cd8-888f-7a448e60535b | -11.961 | -44.01734 | 2026-04-16 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf13b7b5-037a-39d4-945e-90685a1a8b4b | -10.40351 | -44.93137 | 2026-04-16 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7946065-8bfa-37d9-af4d-c6288d7734af | -11.96499 | -41.32968 | 2026-04-16 04:27:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fce812b4-d88a-3e70-a5f8-d4c943fbcbc6 | -9.45311 | -47.82437 | 2026-04-16 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d71cc77-9609-383c-832d-12227bc60d5c | -8.36827 | -48.07981 | 2026-04-16 04:27:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bb78e84-21fe-3943-aceb-68988519b414 | -11.70985 | -44.73931 | 2026-04-16 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1535f235-f1d9-3727-834b-de3e10bb4e4c | -11.1675 | -46.53887 | 2026-04-16 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f401549-e2d6-324e-bb78-0c17eb4667c2 | -8.59376 | -39.53851 | 2026-04-16 04:27:00 | NOAA-21 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 49d710de-8669-3c4f-8864-572cb4a31bb2 | -13.37348 | -43.20473 | 2026-04-16 04:27:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 34053ddf-940e-38a8-8496-67039dab4954 | -12.84416 | -43.82337 | 2026-04-16 04:27:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 35d0b862-1f0a-3e64-8ddf-0ea0eaf48e60 | -15.9723 | -49.85536 | 2026-04-16 04:29:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 02bc763f-d192-3401-909c-710f12c1fd24 | -15.28653 | -43.66931 | 2026-04-16 04:29:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| baf62d3e-cb4a-3a2f-95eb-08c59d6eb1bc | -18.49923 | -51.61644 | 2026-04-16 04:29:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8997cdb0-59c1-34c5-8efa-ee7af2bc4354 | -18.51441 | -48.16878 | 2026-04-16 04:29:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81e6280b-9f93-37bb-8cd3-d9ccffd53d81 | -19.97899 | -44.85506 | 2026-04-16 04:29:00 | NOAA-21 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 609b4c6d-ae94-3de1-9be1-d72564229432 | -19.12462 | -40.38234 | 2026-04-16 04:29:00 | NOAA-21 | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6e53e8e4-9f21-328a-a346-928640be4d1c | -16.60483 | -43.36122 | 2026-04-16 04:29:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31983bed-64f8-3c0e-95cb-52ab06a4cfd6 | -16.85386 | -39.54894 | 2026-04-16 04:29:00 | NOAA-21 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| abd53611-f1a4-3a38-9246-9b556f42984b | -19.59293 | -40.07726 | 2026-04-16 04:29:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fbb5e768-34e6-3366-bfa5-88c4e6e51a65 | -16.85421 | -39.54573 | 2026-04-16 04:29:00 | NOAA-21 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 30d06870-0a4d-35fd-8c2f-d5b34c8a3d23 | -19.59744 | -40.08447 | 2026-04-16 04:29:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0b6dba25-5dac-316f-8b04-bfcf5e039f6d | -16.84865 | -39.54848 | 2026-04-16 04:29:00 | NOAA-21 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 56c7387b-2fd7-3d1b-8bb6-e5ab441a4d5b | -18.51723 | -48.16888 | 2026-04-16 04:29:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f4cf534-10e6-3c23-8460-83eacdcb0f95 | -16.6053 | -43.35755 | 2026-04-16 04:29:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a770b44-0435-3387-a615-679769fccfa4 | -17.67496 | -46.73185 | 2026-04-16 04:29:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3e3c215-6510-3e95-8ec8-417e4f6a8309 | -16.60436 | -43.36488 | 2026-04-16 04:29:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2cc59dd4-fd04-37d0-967b-7d33a21c44c4 | -19.12965 | -40.38328 | 2026-04-16 04:29:00 | NOAA-21 | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 47dbfe49-4544-3e0b-9cd0-116858fa3019 | -18.5006 | -51.60824 | 2026-04-16 04:29:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 303e53ee-fdbd-357d-8d64-a57c5a3c23a3 | -17.67153 | -46.7313 | 2026-04-16 04:29:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 634554c6-adf8-300e-8f1e-14a9c073e148 | -19.59259 | -40.08055 | 2026-04-16 04:29:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 888397ee-c6e9-345d-aafc-ab5cbe596b74 | -19.59778 | -40.08121 | 2026-04-16 04:29:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| abfb9811-1ee4-3451-87d4-e9b20f3b3808 | -17.58066 | -45.38499 | 2026-04-16 04:29:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5ae22840-5e30-3c77-b92a-bc30f5951cfb | -17.33873 | -43.58464 | 2026-04-16 04:29:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb0f372b-9ccf-3ff4-aa90-97fc6be96451 | -16.4602 | -53.43575 | 2026-04-16 04:29:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e455d160-d7d9-339e-930e-b8569ec98428 | -19.92779 | -44.07004 | 2026-04-16 04:29:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b4e29aad-f934-3f3a-89f6-e33dbe2e53b1 | -19.12494 | -40.37937 | 2026-04-16 04:29:00 | NOAA-21 | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2655716c-b680-327d-9b5a-f8353903ab22 | -18.49641 | -51.61171 | 2026-04-16 04:29:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 764054d0-fb0c-39f9-b4e9-dbfa8f73c62c | -18.49572 | -51.61581 | 2026-04-16 04:29:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c363789d-de69-39fb-81e3-3b797038017a | -16.46416 | -53.43648 | 2026-04-16 04:29:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eeab0c50-c25c-3b61-8eb7-86a0c1cf1ee8 | -18.49992 | -51.61234 | 2026-04-16 04:29:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5a915b8-4b4a-3774-bd4c-7b04a2247b66 | -20.17222 | -46.59439 | 2026-04-16 04:32:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e610e2b-95bd-300c-b625-4b8e298f04d1 | -21.19237 | -47.37134 | 2026-04-16 04:32:00 | NOAA-21 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f89735cd-bb28-324c-8b74-15af4006b2ef | -20.18388 | -46.5882 | 2026-04-16 04:32:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe655a4a-e975-318c-80c9-16816a8194af | -23.40829 | -46.4233 | 2026-04-16 04:32:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0b5a1ac9-e59b-350a-8ad1-dc62c55ac264 | -20.40901 | -49.75848 | 2026-04-16 04:32:00 | NOAA-21 | COSMORAMA | SÃO PAULO | Brasil | 3512902 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b39aa5ad-45ef-319a-b0e4-9de2aeb4028c | -20.97964 | -48.9956 | 2026-04-16 04:32:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5d4b2be0-262a-362b-a638-bbfc43fa5fe3 | -20.18037 | -46.58758 | 2026-04-16 04:32:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ec38570-9ba2-3e83-88aa-cc3d2bc93cbb | -20.18797 | -46.58469 | 2026-04-16 04:32:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8599f48f-7a28-3a2d-8ec8-204812c1b4c5 | -20.68576 | -49.40285 | 2026-04-16 04:32:00 | NOAA-21 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87988d69-e522-3eed-91ae-d5ad5194a24f | -20.17166 | -46.59843 | 2026-04-16 04:32:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81318656-bd0d-35a4-8d70-15adaad2b1f5 | -20.1798 | -46.59166 | 2026-04-16 04:32:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca375dde-1d73-330f-a2f4-a5751680b9ca | -21.19582 | -47.37191 | 2026-04-16 04:32:00 | NOAA-21 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e52ee106-ccf9-338b-9faa-d691f0e083af | -20.1874 | -46.58882 | 2026-04-16 04:32:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97f1b1c1-49d0-32e3-9f09-cb2c03350a03 | -22.68381 | -47.13621 | 2026-04-16 04:32:00 | NOAA-21 | COSMÓPOLIS | SÃO PAULO | Brasil | 3512803 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 752b7a5e-e81d-3fc3-957c-67a3f16974a8 | -21.71011 | -48.4287 | 2026-04-16 04:32:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 986b0051-b66c-3c19-b89a-7a1d3a20bbfd | -21.70618 | -48.43196 | 2026-04-16 04:32:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README3.md)
