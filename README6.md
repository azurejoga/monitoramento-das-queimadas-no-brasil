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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5871ff17-4810-35c7-bec8-7d0d359c09b4 | -4.38657 | -42.14296 | 2024-12-27 03:40:00 | NOAA-20 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 843f8735-1fed-3af4-be72-db3b267ab393 | -5.13137 | -43.24382 | 2024-12-27 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 81c808e1-2892-37f7-b1e0-d458e0f1e401 | -4.03678 | -46.21481 | 2024-12-27 03:40:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32e18481-f576-3072-b055-a7f1150cd2c3 | -9.33398 | -35.97713 | 2024-12-27 03:40:00 | NOAA-20 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| ed4bc5a5-f5bd-3d6d-84cb-2f3faa41b3b6 | -7.45134 | -35.27426 | 2024-12-27 03:40:00 | NOAA-20 | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f9a81378-b097-30bc-aa03-2ee1f0ced236 | -5.63631 | -43.71949 | 2024-12-27 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4e63a7d9-727a-3998-a965-2805e7b3ef74 | -3.19624 | -45.99406 | 2024-12-27 03:40:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6deeaf74-f456-3284-9a66-ee515be5ab57 | -4.42282 | -46.55988 | 2024-12-27 03:40:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| ec1cf25e-cb63-38e0-a515-04e99e87be93 | -5.21578 | -44.9116 | 2024-12-27 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a710ed5-b442-3d33-8b99-ba9a1ed1a616 | -4.69888 | -38.16498 | 2024-12-27 03:40:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a1091591-5f97-3997-9461-acca537e5917 | -5.63846 | -43.70697 | 2024-12-27 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5e4a706-f597-3f3c-8eaf-3a2abd334dbf | -9.41969 | -35.99416 | 2024-12-27 03:40:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 1cd3bdb2-b5fd-35d1-8ab2-422098e1f18d | -2.28504 | -45.5783 | 2024-12-27 03:40:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fcd0d453-fdcd-359c-b82f-fd2de0a18e21 | -4.24506 | -41.92695 | 2024-12-27 03:40:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 52ce5409-2a95-3806-97e5-36364e6f15e3 | -11.07556 | -37.13638 | 2024-12-27 03:40:00 | NOAA-20 | ARACAJU | SERGIPE | Brasil | 2800308 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5ce0556a-c119-380c-9381-4055afa0f37f | -5.63792 | -43.71013 | 2024-12-27 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc91d288-15f5-3240-bbae-3b722fb96e96 | -6.71495 | -35.03411 | 2024-12-27 03:40:00 | NOAA-20 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 292d7599-98a9-3e02-8c5f-4b63376fb5af | -4.51989 | -42.07928 | 2024-12-27 03:40:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 0e84137b-948f-3f5e-862e-a067efc938f6 | -4.5575 | -44.13239 | 2024-12-27 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8d2c692f-23b5-3912-aaa5-a28df83b6dc5 | -3.07188 | -41.9003 | 2024-12-27 03:40:00 | NOAA-20 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 4.4 |
| f6ec8783-76e6-3bd4-9e8d-8011eace4b3f | -3.03521 | -40.12254 | 2024-12-27 03:40:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 85c5fe38-72ca-3b6e-9d2b-a9a89162e124 | -5.64779 | -43.71486 | 2024-12-27 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b3ffbab8-6b15-3a06-8a72-82e78c9bf7a5 | -6.20974 | -41.56366 | 2024-12-27 03:40:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 0e941ad4-533a-3206-ad72-4679792f4c74 | -3.06215 | -47.77693 | 2024-12-27 03:40:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ff2b4cfd-7540-3a48-88f9-dbd9c0d03cff | -7.90005 | -35.22786 | 2024-12-27 03:40:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e7b36da7-5e3a-3a3f-9ace-9e9ea2dec8a0 | -4.25088 | -47.58581 | 2024-12-27 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5f7c055-bdac-3af7-b463-f594540f4d60 | -5.92248 | -43.78174 | 2024-12-27 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30b8bac8-b8fc-3772-aa26-a8a1374f5069 | -3.06483 | -47.76832 | 2024-12-27 03:40:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4f5fbf22-6857-33b0-8e69-b24dc8d777bd | -5.92823 | -43.77944 | 2024-12-27 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc70bf02-07ef-321d-b5fa-e9b384232836 | -3.22983 | -45.97129 | 2024-12-27 03:40:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c711c042-ddc8-3a99-b63b-fa397fb2bebf | -3.18677 | -46.12655 | 2024-12-27 03:40:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad179c23-3024-3f89-8e4a-2487c8668d43 | -7.33119 | -35.06704 | 2024-12-27 03:40:00 | NOAA-20 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 650bd0e4-cb5f-39e5-8926-2ad598f1c76e | -5.63577 | -43.72268 | 2024-12-27 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8e8e0a9a-d353-36ad-a271-df76b107a7c0 | -8.63406 | -35.95758 | 2024-12-27 03:40:00 | NOAA-20 | PANELAS | PERNAMBUCO | Brasil | 2610202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| cc9928bb-ab12-3274-bc3e-dffb4e05f757 | -5.2204 | -41.27815 | 2024-12-27 03:40:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f2f6ac68-a282-3f3d-8c95-a19b27b5dd0f | -4.55207 | -44.13147 | 2024-12-27 03:40:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3ca941b-12ef-3419-9394-21826cee3ef3 | -6.5818 | -34.99509 | 2024-12-27 03:40:00 | NOAA-20 | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5bc5fab3-789a-3f39-bc1a-1dc00eb77062 | -5.24578 | -41.39283 | 2024-12-27 03:40:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1b828ff1-ff2c-32b1-af7a-362204a8a6df | -10.47285 | -37.01961 | 2024-12-27 03:40:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 1ac63d23-f1d2-39d3-aaba-76840060deee | -9.41637 | -35.99364 | 2024-12-27 03:40:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 8a190e61-c5a3-3959-972e-899de4770fa7 | -5.94138 | -44.44922 | 2024-12-27 03:40:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 93a6a692-dba3-31f3-81a9-23bb3ff20b10 | -5.92193 | -43.7849 | 2024-12-27 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4061f86f-416f-3cbc-9624-c29864be0168 | -3.8207 | -46.05606 | 2024-12-27 03:40:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c07e3265-e823-33b0-8e05-b189aae3211a | -6.58511 | -34.99561 | 2024-12-27 03:40:00 | NOAA-20 | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 80c8ceae-380d-301a-b65f-9631b29b5bc9 | -5.6352 | -43.72596 | 2024-12-27 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 43e4d18a-adf1-3a6c-b578-d8ebe1ac8b68 | -5.35883 | -39.34334 | 2024-12-27 03:40:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| b82a9af3-997e-36ea-895a-878981e09b7b | -6.21413 | -41.56467 | 2024-12-27 03:40:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1b121114-818e-3bda-81ab-b2e56f75c746 | -8.90258 | -35.26572 | 2024-12-27 03:40:00 | NOAA-20 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 99525ef5-6862-38b5-8871-da703456ab24 | -5.63738 | -43.71328 | 2024-12-27 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f96c3c69-3ea6-3a77-bd58-bd4dfa7e02e0 | -3.00086 | -48.06297 | 2024-12-27 03:40:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 568e0bb7-4ce9-3aa3-8bcc-94b29ec4b36a | -5.64833 | -43.71171 | 2024-12-27 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 48ca2ef3-7355-32bc-a84a-4664fa54e3cc | -3.23066 | -45.9665 | 2024-12-27 03:40:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6e56592-52f1-3e5d-87fc-2e6c490d1c93 | -5.64205 | -43.71721 | 2024-12-27 03:40:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8e4c8956-d39a-327a-ae81-9b44020e3229 | -7.13523 | -41.03822 | 2024-12-27 03:40:00 | NOAA-20 | CAMPO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2202133 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bb77f30a-cd07-3f74-8962-c24de9c390c9 | -9.41582 | -35.99712 | 2024-12-27 03:40:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 0edad5a6-9f74-32ee-a392-208c6c1a780f | -5.31286 | -46.06009 | 2024-12-27 03:40:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e1ba6255-c862-3ddd-936f-896fb308caff | -7.04187 | -38.34178 | 2024-12-27 03:40:00 | NOAA-20 | CARRAPATEIRA | PARAÍBA | Brasil | 2504108 | 25 | 33 | nan | nan | nan | Caatinga | 3.3 |
| eb602597-eca9-3551-a8ce-5f2a4c14554f | -6.90226 | -39.58529 | 2024-12-27 03:40:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2fc9dc02-6588-359d-a89e-a158cee58320 | -3.41019 | -44.9048 | 2024-12-27 03:40:00 | NOAA-20 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a9616a1b-f8fe-3d45-b9be-7cf3aa9863a8 | -4.02615 | -46.17983 | 2024-12-27 03:40:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0126beb1-c49a-34bc-81ad-a271f48f38e8 | -4.2473 | -41.92475 | 2024-12-27 03:40:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 57f80000-a14e-3809-a9e4-73889dac0faf | -3.99054 | -43.25503 | 2024-12-27 03:40:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a0250ea-8695-38cc-bc93-a6918217e074 | -3.23159 | -45.97499 | 2024-12-27 03:40:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d966f55e-e7e9-359e-9aab-b7cea85fe27f | -11.56591 | -44.82744 | 2024-12-27 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e50f7ec5-6519-3a9f-a41d-324e726f888e | -12.76184 | -38.48199 | 2024-12-27 03:42:00 | NOAA-20 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 72eac987-0cea-36db-aba1-3407d3d4a37f | -11.96093 | -41.32982 | 2024-12-27 03:42:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7a00eedd-eef9-3a42-964e-0aec83ead0ca | -15.40339 | -39.18911 | 2024-12-27 03:42:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9d128b37-5131-3376-a94b-3550bfc72401 | -10.43401 | -44.88901 | 2024-12-27 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c85d7f84-001c-38c9-bcbc-fffddd202d70 | -15.19305 | -43.73532 | 2024-12-27 03:42:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b4c6d4e6-db85-3d95-9233-ce3bc20640a1 | -11.44416 | -39.50724 | 2024-12-27 03:42:00 | NOAA-20 | SÃO DOMINGOS | BAHIA | Brasil | 2928950 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 73bdb23c-dcf7-3adf-a688-b61db9ebe607 | -11.56087 | -44.82646 | 2024-12-27 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18a80ec0-81c7-3972-97c4-fbfc3614b614 | -16.34718 | -43.69829 | 2024-12-27 03:42:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9625e167-0c45-3b69-b22a-afaf781afce0 | -11.23855 | -41.89125 | 2024-12-27 03:42:00 | NOAA-20 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d4c77eb5-505a-3b3b-9863-852f75a50a3b | -15.64248 | -39.18703 | 2024-12-27 03:42:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 64680c6f-35aa-3783-a3fe-81a9ee2118d6 | -11.44345 | -39.51151 | 2024-12-27 03:42:00 | NOAA-20 | SÃO DOMINGOS | BAHIA | Brasil | 2928950 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2952e2f8-d591-3264-a914-8b6a53159567 | -11.00678 | -41.99778 | 2024-12-27 03:42:00 | NOAA-20 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 820d0de8-f32a-34d1-9737-bb51a55660c8 | -11.88504 | -40.95947 | 2024-12-27 03:42:00 | NOAA-20 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 587fc165-8081-3a11-8f0f-021baef85449 | -10.42885 | -44.88802 | 2024-12-27 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97e9cbd7-1c4c-3a8c-9db5-e7fd727c8377 | -18.03973 | -39.92587 | 2024-12-27 03:44:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 67c5f147-4bb7-3395-9873-1186bb631261 | -17.09368 | -43.80516 | 2024-12-27 03:44:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4780efdd-bec2-3081-a969-c2f003b3e55a | -17.41925 | -39.60439 | 2024-12-27 03:44:00 | NOAA-20 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3dadeae8-0cdf-337d-843f-43a87d4183eb | -18.80513 | -40.25643 | 2024-12-27 03:44:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| ae79d917-bafb-338e-8c06-4a475ca71aa4 | -3.03393 | -40.11939 | 2024-12-27 04:31:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 992e189e-dbce-3872-a053-a26bbfdd4f60 | -2.62035 | -46.11732 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82cd824b-352c-34d0-83b7-0fe55be9f97a | -3.93789 | -46.98435 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0854244c-6d2d-3430-b63f-59e54cd05a20 | -3.82679 | -46.05621 | 2024-12-27 04:31:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| acbbf9ce-95f7-37b9-94a8-0756417c0784 | -3.03672 | -40.12128 | 2024-12-27 04:31:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 6084a1f4-44d1-325e-8e7f-3ff7b3bc4443 | -4.01144 | -46.70856 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 003ba347-272f-3472-beed-fac8f174eed7 | -3.87139 | -47.01996 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb6c8ec9-d65f-38a3-86f0-e33dfc9ed471 | -3.89722 | -47.00632 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 812e7a01-6d02-3f5a-84ab-d4f99ff7d2f3 | -1.60401 | -53.37101 | 2024-12-27 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2f1dc934-c4cf-3bac-ae93-1a15077b7cc1 | -3.89498 | -46.99894 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cdd7834c-19be-3be2-9a7b-d4060c815344 | -3.91179 | -46.93437 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45fdd277-8ae1-3f56-bc66-57a1163ac3d6 | -3.69103 | -47.1712 | 2024-12-27 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c9dec3f-c1cd-3070-95a9-90351f69ee9e | -3.91555 | -46.9102 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0006fbb3-04d2-31c5-a59c-a7262fb6f531 | -2.73568 | -46.18577 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de77a897-d13b-3551-b94c-8c4263bd855d | -3.92466 | -46.98231 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7d98fab-930f-348a-b581-6eaf3ec05fba | -2.71398 | -46.17168 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d49fa36-f767-3ab1-bf2c-555c1fa7f5ac | -3.92135 | -46.9818 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e61055a9-5960-3e40-a857-4be8d146ce16 | -3.19419 | -45.99236 | 2024-12-27 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README7.md)
