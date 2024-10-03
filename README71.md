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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b6704d6-b6fc-3186-b84b-a6971cbcb32c | -19.4949 | -42.88046 | 2024-10-03 03:38:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| b747f6a8-c218-3bb6-9daf-173797bc9532 | -19.44524 | -43.0657 | 2024-10-03 03:38:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e56b8af8-578f-30fd-9634-144eb36f77cc | -19.44089 | -43.06493 | 2024-10-03 03:38:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a6c07d2a-8c1c-37c4-a5b0-4b269e130c94 | -19.4402 | -43.06333 | 2024-10-03 03:38:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ee64c745-677e-3d81-854c-18c358454101 | -19.43822 | -41.37219 | 2024-10-03 03:38:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 496a4283-0d6c-3510-a6db-e0a8eecae35c | -19.43707 | -41.37836 | 2024-10-03 03:38:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1a5f08f3-5e8d-30b9-8afc-3b3fd7bcf30b | -19.4342 | -41.35042 | 2024-10-03 03:38:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 278a19e1-8276-3ea7-a2a1-36cf0d941512 | -19.43365 | -41.35328 | 2024-10-03 03:38:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 1e98bb34-0939-3958-9179-d6ffe72bccb4 | -19.4333 | -41.35521 | 2024-10-03 03:38:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1e53dba1-a7a0-3f31-ba3f-b7c686304d2f | -19.4298 | -41.35216 | 2024-10-03 03:38:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 765854c4-dcfd-316b-ba29-24dd47b52f87 | -19.42947 | -41.35408 | 2024-10-03 03:38:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 76639407-333e-3ad0-9a3d-ffacb199ca1a | -19.42894 | -41.3569 | 2024-10-03 03:38:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6babe91a-31cc-3491-87df-ce3dbf36b60f | -19.42496 | -41.35658 | 2024-10-03 03:38:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7fa4e11d-6d0d-32df-8fec-0c6a2b00b5db | -19.42456 | -41.35871 | 2024-10-03 03:38:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 864ceaa5-0c19-3452-b261-235902898f7a | -19.42403 | -41.36174 | 2024-10-03 03:38:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2a4e1add-705b-325f-a8af-1922129d6e2c | -19.02326 | -43.20047 | 2024-10-03 03:38:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 6faa8fc8-3b47-3058-a52b-5eb31683682a | -19.42356 | -41.364 | 2024-10-03 03:38:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 529df87e-1d22-3228-a599-07424a899ebf | -19.42325 | -43.08583 | 2024-10-03 03:38:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6ddbe488-9ed5-30d0-baca-2e471175508e | -19.42231 | -43.09054 | 2024-10-03 03:38:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4688c770-aa7b-35a2-8c3a-9d4529ad1041 | -19.42185 | -43.08891 | 2024-10-03 03:38:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 70f44851-203a-3fa2-811a-663138aa2e8f | -19.31291 | -42.60289 | 2024-10-03 03:38:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 4c0b0500-28bc-3a9a-b2fb-8bd9a7624ffd | -19.31205 | -42.60733 | 2024-10-03 03:38:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| fb874228-b575-3294-b94c-be5359ed760d | -19.30882 | -42.60369 | 2024-10-03 03:38:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 56b1a5ec-26d2-35eb-9190-231dc82923fb | -19.30794 | -42.60846 | 2024-10-03 03:38:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 3d6a24bf-2de5-3924-b334-89007fd10103 | -19.30779 | -42.60669 | 2024-10-03 03:38:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 2e5dfeab-f95b-32a5-a5b8-fc6e9c7f0b5b | -19.30701 | -42.61346 | 2024-10-03 03:38:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| f53dd006-1d28-3cbf-926f-8f2c36ec7dc5 | -19.30682 | -42.61168 | 2024-10-03 03:38:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 8f84ba46-0b4b-3f9f-8efe-374728fbc7a1 | -19.30367 | -42.60788 | 2024-10-03 03:38:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 377130ac-8b93-31d0-a763-84de2d797826 | -19.30354 | -42.606 | 2024-10-03 03:38:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 666f1309-173b-353c-ab39-d7a698ab826d | -19.30252 | -42.61125 | 2024-10-03 03:38:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 893c18ff-8c85-32a7-a6a9-064246ecb33a | -19.30197 | -42.59358 | 2024-10-03 03:38:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 073c4194-cfd2-3101-97c1-1732970bfc5c | -19.30186 | -42.59217 | 2024-10-03 03:38:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c6353ade-57b6-3a75-8385-1ef161e9a3bb | -19.29771 | -42.59298 | 2024-10-03 03:38:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| b00db363-2055-35f4-81de-6940f367213e | -19.27675 | -43.7691 | 2024-10-03 03:38:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 953647c5-f872-3a5b-b029-73f559336619 | -19.27579 | -43.77403 | 2024-10-03 03:38:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4ba74215-9a7c-3171-86e2-dcca4ae3f996 | -19.27485 | -43.77882 | 2024-10-03 03:38:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51493dc5-0178-3ec0-a7d5-911fd3391bcb | -19.27224 | -43.76803 | 2024-10-03 03:38:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6d1e1a6c-92d6-3765-a13b-2d7bcda71f40 | -19.27127 | -43.77298 | 2024-10-03 03:38:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 843a93fa-d44c-34a9-8343-95a121bace8a | -19.27078 | -42.36849 | 2024-10-03 03:38:00 | NOAA-20 | BELO ORIENTE | MINAS GERAIS | Brasil | 3106309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 113cbdda-8073-3852-a94a-2f718e7b8878 | -19.27034 | -43.77774 | 2024-10-03 03:38:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97bd6c72-62c9-336c-95da-ee8449f2be5b | -19.26938 | -43.78262 | 2024-10-03 03:38:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f5dd085-4691-3d6c-b829-6f7feb36c7bd | -19.26771 | -43.76699 | 2024-10-03 03:38:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b003864-87bc-3352-a343-698bb6655d0c | -19.26674 | -43.77197 | 2024-10-03 03:38:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd11077b-12dc-3937-ba1c-dde398ae5fbb | -19.26581 | -43.77671 | 2024-10-03 03:38:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4775da4c-9118-326e-9a02-71a3ba7463b0 | -19.26416 | -43.76101 | 2024-10-03 03:38:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8793219-25cc-3347-aa00-14f025e536a8 | -19.26128 | -43.77569 | 2024-10-03 03:38:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34914b0e-4310-3fd0-800e-21d420e5eea3 | -19.25408 | -43.76425 | 2024-10-03 03:38:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 60a8de08-a0ad-3b2b-98c3-08d92171e769 | -19.2488 | -40.62395 | 2024-10-03 03:38:00 | NOAA-20 | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1801a449-2b65-3b1f-a7be-32bd23e71a1e | -19.24794 | -43.37945 | 2024-10-03 03:38:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2cb02f60-7085-334c-9ae0-59b7fcbe53bf | -19.24791 | -40.62888 | 2024-10-03 03:38:00 | NOAA-20 | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 154b7c17-ddda-39ab-9e1a-8833ffa83894 | -19.247 | -40.63383 | 2024-10-03 03:38:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 32e05fef-8273-3799-8a74-256a8faafa46 | -19.24445 | -43.37367 | 2024-10-03 03:38:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8bf26ff8-1d70-39e0-89ab-5228a5ab2ad6 | -19.24359 | -43.37815 | 2024-10-03 03:38:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e57324f4-6995-338b-8ba1-4469e088b433 | -19.24325 | -40.63305 | 2024-10-03 03:38:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7f39b036-7ccf-318c-819c-9052ccb48a93 | -19.24265 | -43.38301 | 2024-10-03 03:38:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8596cbb1-8ba5-3144-aa33-800bb503c6ad | -19.24168 | -43.38803 | 2024-10-03 03:38:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9a39626c-abb3-34d7-86e5-957d2305a645 | -19.17886 | -40.16136 | 2024-10-03 03:38:00 | NOAA-20 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 31428320-564f-3d3c-bade-5d237092e2de | -19.13439 | -44.64133 | 2024-10-03 03:38:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f55a711b-29e8-3f06-b242-9dad0a77930c | -19.133 | -44.64073 | 2024-10-03 03:38:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e6bc9102-5e70-3794-85f4-a20b01930a5e | -19.11179 | -40.36727 | 2024-10-03 03:38:00 | NOAA-20 | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4cfb7b10-9c59-3bc7-9080-3feb6864a99d | -19.09246 | -48.05358 | 2024-10-03 03:38:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12a2917b-bee1-3f36-85f8-0216940e94b9 | -19.08654 | -48.05215 | 2024-10-03 03:38:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2e3afff6-5b13-3787-ae1e-b4e2ad2bd3d0 | -19.08555 | -48.05657 | 2024-10-03 03:38:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fd2692b7-d7bc-320f-8fbe-21f5140634a7 | -19.06488 | -44.41728 | 2024-10-03 03:38:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b927313-4c8d-3083-aa5b-311cfc521120 | -19.0608 | -45.56147 | 2024-10-03 03:38:00 | NOAA-20 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e08d36b-c857-3a77-b48b-147bee9b8b8f | -19.05896 | -44.42197 | 2024-10-03 03:38:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82c67c86-08da-3c8c-9327-d2d1a9616772 | -19.04744 | -46.16296 | 2024-10-03 03:38:00 | NOAA-20 | ARAPUÁ | MINAS GERAIS | Brasil | 3103801 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cffa0f11-80aa-3020-b570-afbb01e7006d | -19.04672 | -46.16634 | 2024-10-03 03:38:00 | NOAA-20 | ARAPUÁ | MINAS GERAIS | Brasil | 3103801 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7f7b94f-32f3-35f0-8f51-c1344dea8904 | -19.04599 | -46.16978 | 2024-10-03 03:38:00 | NOAA-20 | ARAPUÁ | MINAS GERAIS | Brasil | 3103801 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38350754-f421-3311-bc31-6fae43cb7fad | -19.04138 | -46.16537 | 2024-10-03 03:38:00 | NOAA-20 | ARAPUÁ | MINAS GERAIS | Brasil | 3103801 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57967ec9-cc12-3f77-a460-8e7075544994 | -19.04064 | -46.16882 | 2024-10-03 03:38:00 | NOAA-20 | ARAPUÁ | MINAS GERAIS | Brasil | 3103801 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53b0bf92-fb03-308e-ba3d-969201e8e782 | -19.0405 | -43.20595 | 2024-10-03 03:38:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 4360b75b-4c24-3192-9115-b2ddf34e3d21 | -19.03715 | -43.19958 | 2024-10-03 03:38:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| ce524464-ed78-3502-b747-72d0630eb96a | -19.0362 | -43.2045 | 2024-10-03 03:38:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 68703bc3-4d7c-3770-9e2e-c2bfd4824872 | -19.03189 | -43.20314 | 2024-10-03 03:38:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c0ebf3e2-e67f-3ebf-ac09-58a1c4267721 | -19.03091 | -43.20823 | 2024-10-03 03:38:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3141c92d-b96c-359d-a685-03548b00b6cf | -19.02993 | -43.21326 | 2024-10-03 03:38:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8d62361f-3bd3-3607-b5b6-090b7760eba1 | -19.0266 | -43.20682 | 2024-10-03 03:38:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 22690f30-fa27-36e8-a06c-a2941bd95fc1 | -19.02231 | -43.20533 | 2024-10-03 03:38:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| ba1f78df-04b5-378d-a98d-d83a608b761b | -19.01888 | -43.19946 | 2024-10-03 03:38:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| c31dcf81-b9f7-3819-92cd-5e00b29454cf | -19.01792 | -43.20441 | 2024-10-03 03:38:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 0f9ba910-4242-30bc-b574-0d80394c8787 | -18.97991 | -43.21142 | 2024-10-03 03:38:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0d485a6f-132c-3e1f-9c01-38fdf1af78ab | -18.97901 | -43.21599 | 2024-10-03 03:38:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b8837c66-18da-3032-a49b-bdf4997f5042 | -18.9781 | -43.22062 | 2024-10-03 03:38:00 | NOAA-20 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3e0264a0-95d9-3e2d-9916-61750023da56 | -18.97516 | -43.21762 | 2024-10-03 03:38:00 | NOAA-20 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0dd32710-b58c-3e4b-b6ef-5399e9ae79ca | -18.97427 | -43.22228 | 2024-10-03 03:38:00 | NOAA-20 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| cc39a41f-8d60-31d3-aa19-c7a78353aeb0 | -18.9737 | -43.21968 | 2024-10-03 03:38:00 | NOAA-20 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f8dbcf81-363d-34c9-94bd-4aeb8ca5a0b1 | -18.97337 | -43.22704 | 2024-10-03 03:38:00 | NOAA-20 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ae7d5b81-bc04-385c-a120-62ff47d72e61 | -18.97276 | -43.22438 | 2024-10-03 03:38:00 | NOAA-20 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3a0fbbed-326d-31c9-85bd-c6816f640c01 | -18.9104 | -41.27615 | 2024-10-03 03:38:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 3b598fdd-4f92-37bc-a687-6773ab321a13 | -18.89897 | -41.20808 | 2024-10-03 03:38:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 9740ed52-c683-3a4a-b50e-694780490240 | -18.89806 | -41.21311 | 2024-10-03 03:38:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| e388bbb5-bbbe-3ba7-8cae-42d761b64be0 | -18.89418 | -41.21223 | 2024-10-03 03:38:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 6faee6bd-f078-3aba-bb2f-e59c90aa74ad | -18.89028 | -41.21145 | 2024-10-03 03:38:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 67e4705e-31ef-3fad-b2e4-057ef4e02eed | -18.88935 | -41.21654 | 2024-10-03 03:38:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 3a9999f9-8104-327e-a807-21479e96dde6 | -18.88842 | -41.22171 | 2024-10-03 03:38:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e9e9a88b-1cf5-3fdb-97eb-1a82af25cb24 | -18.88641 | -41.21049 | 2024-10-03 03:38:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 0369214b-0252-310f-94e0-17c440f00839 | -18.8855 | -41.21547 | 2024-10-03 03:38:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 56501a61-9032-3074-90dd-1cc977e272dd | -18.88457 | -41.22061 | 2024-10-03 03:38:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| d70deaa3-34ee-3159-8bef-c32de39c9c61 | -18.88074 | -41.21938 | 2024-10-03 03:38:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |


[Clique aqui para ver as próximas entradas](README72.md)
