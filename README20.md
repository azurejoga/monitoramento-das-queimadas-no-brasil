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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ebf8a64-e2fb-33e7-8da4-8c138e9fb84f | -3.85744 | -44.00159 | 2025-11-15 04:04:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3a35fd0-da80-39d5-ad41-8cd5281d894a | -4.55834 | -46.68595 | 2025-11-15 04:04:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 279cae38-5a65-3ec8-8464-3c2a1373d2cd | -2.73875 | -45.29401 | 2025-11-15 04:04:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc87a1d7-d338-3b6b-8f2b-231533c7c44d | -6.33106 | -47.26262 | 2025-11-15 04:04:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fbcf72bc-6632-3f14-b353-a68a91c7a0ce | -7.1461 | -41.24479 | 2025-11-15 04:04:00 | NPP-375D | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6a36b28a-a597-3950-9597-39ce15cd622c | -7.44992 | -42.76622 | 2025-11-15 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2a198c5c-b2aa-3521-86cc-42b395acaf8d | -4.42242 | -47.60035 | 2025-11-15 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1212a96a-e942-38b0-9cd3-dbd5eb24cf16 | -3.93809 | -42.7424 | 2025-11-15 04:04:00 | NPP-375D | PORTO | PIAUÍ | Brasil | 2208502 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| dbefde72-7011-3b97-bf07-60e4f18124ce | -3.71179 | -47.63151 | 2025-11-15 04:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62d59d9d-3bfc-3920-8b59-3b36eb5d06d0 | -3.17096 | -48.61502 | 2025-11-15 04:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 229e37a7-bb61-3d08-9d26-229034bb09f8 | -7.3136 | -39.78146 | 2025-11-15 04:04:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| acfa5897-6c7e-3c60-aaf2-a02823303309 | -7.29291 | -45.10489 | 2025-11-15 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf21bb3d-c6ef-3aee-acdc-2a8937dcc444 | -4.49963 | -42.87353 | 2025-11-15 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cafabd35-346c-3345-b202-cff12a24c1ba | -5.62702 | -45.04412 | 2025-11-15 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00bc27ce-3091-36d3-b017-1279e8269256 | -4.60585 | -45.96072 | 2025-11-15 04:04:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4659738-659b-3aec-9520-6b528482d49d | -1.05256 | -48.94906 | 2025-11-15 04:04:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c243c77-b72a-3dc1-a733-498f797a8b2b | -4.82657 | -47.09535 | 2025-11-15 04:04:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de05cbcd-0fc7-3e96-80f2-32fc92a821d0 | -4.41957 | -50.8256 | 2025-11-15 04:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cf4c1ca-8669-3407-83c9-036858b7a5a3 | -4.46429 | -45.65022 | 2025-11-15 04:04:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ff005ae-63b8-3a0e-9708-6609ebbf5908 | -4.10506 | -48.01445 | 2025-11-15 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61dd15e4-7e89-3b76-a43e-ddc20d411dfe | -5.77374 | -44.37948 | 2025-11-15 04:04:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a621e2e9-1143-383c-b206-986fcbf9768c | -6.03627 | -39.49064 | 2025-11-15 04:04:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d282ef3f-e359-35c3-af51-64edd4e60943 | -5.52472 | -41.77001 | 2025-11-15 04:04:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6d3f0a99-0452-398e-9c92-b7d0c52f1b34 | -3.37904 | -41.16408 | 2025-11-15 04:04:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7e1c219a-d785-3598-8e18-4fe16963b6fa | -4.67004 | -45.05341 | 2025-11-15 04:04:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e15bc97d-d3b4-34f8-87a4-43a4889bdb6a | -5.85673 | -43.27182 | 2025-11-15 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 838d926e-f293-3dda-a6d8-779836156fd9 | -1.49986 | -47.80798 | 2025-11-15 04:04:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 706f3f4c-155b-3278-83e8-1136209ef2aa | -6.10925 | -41.52357 | 2025-11-15 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4a7f9aaa-a651-316c-89ed-c2c458832bfd | -4.9797 | -44.5326 | 2025-11-15 04:04:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3dc049b8-fa14-334c-b994-2438b78fc544 | -5.88471 | -42.26897 | 2025-11-15 04:04:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f7a97d1c-3e67-356a-ac23-3cc4c3b24571 | -6.32635 | -47.26175 | 2025-11-15 04:04:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee2bd0ed-1ffd-31e4-b627-0fd52734033a | -5.42259 | -43.25645 | 2025-11-15 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5a13c327-c466-34f5-babf-dfbcdedb644c | -4.02574 | -42.47595 | 2025-11-15 04:04:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2bf1102b-7321-32d8-b5d5-02d7a0faa5c1 | -7.38774 | -43.31404 | 2025-11-15 04:04:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7d569010-7ddf-326e-9934-6449626c1ffa | -2.70925 | -46.97839 | 2025-11-15 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 981a1e25-1444-3adc-a460-c0b155fef5e0 | -6.51296 | -43.40789 | 2025-11-15 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 6f78490f-d50d-3161-a1b8-318b9f24a305 | -5.24054 | -44.34992 | 2025-11-15 04:04:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 810fc62e-4f67-3c5d-8f30-477423400373 | -5.71658 | -42.3471 | 2025-11-15 04:04:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6a8b4a48-1588-39f1-9c7e-4cca1b6d23eb | -5.59501 | -45.80001 | 2025-11-15 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4b761b1-3f98-3fa4-81a4-c7f43e9cfbce | -5.4242 | -43.25957 | 2025-11-15 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 55524360-1d0b-349b-9fda-b052ab8281a9 | -7.38412 | -43.31344 | 2025-11-15 04:04:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17977c42-5c03-3f54-ba02-908a48713454 | -5.48266 | -40.96796 | 2025-11-15 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9399a163-18e2-383f-9d5e-1b1bf2cf4b82 | -6.16524 | -48.04457 | 2025-11-15 04:04:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 524f98d8-b3f4-3b12-ad7c-59838f64189c | -7.42462 | -45.23326 | 2025-11-15 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a526972c-c0a5-3e98-b575-b2832ca7a08b | -3.9993 | -47.68231 | 2025-11-15 04:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d100b5e0-1e99-3374-b1e7-4459ac36e1e8 | -4.35381 | -46.49277 | 2025-11-15 04:04:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2e88c540-0415-3103-af46-a8c0ab91d0d7 | -6.88131 | -41.58952 | 2025-11-15 04:04:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 024eb1aa-373a-3d57-8894-469a296a447c | -5.0969 | -37.78648 | 2025-11-15 04:04:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 19.7 |
| 8db59c35-a97d-30a3-b75a-08365176eed7 | -4.6591 | -46.84223 | 2025-11-15 04:04:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1dca40af-cff4-3e0e-b552-bc3a6e70127c | -5.25117 | -43.95077 | 2025-11-15 04:04:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95d9765c-6b8e-3c66-8377-d2f5612b2f4e | -7.65512 | -41.29689 | 2025-11-15 04:04:00 | NPP-375D | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b47f4fb2-5659-321f-9171-0203f381d74e | -5.07134 | -42.49792 | 2025-11-15 04:04:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8b48bb15-a07a-3ded-b41b-a9068006afee | -5.72026 | -46.75234 | 2025-11-15 04:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7386415e-7a27-331f-a9de-91dbb22c9dc3 | -5.16455 | -44.85176 | 2025-11-15 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c85ed706-51a5-3498-a12a-41fac45044ca | -5.53983 | -42.69807 | 2025-11-15 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 40d28624-72e6-3a6b-99ab-6f09e82f8710 | -3.00849 | -49.43397 | 2025-11-15 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9ebbfdd-04af-39bc-81aa-60edd4687c66 | -4.39965 | -42.14616 | 2025-11-15 04:04:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ec2a9630-eed2-314b-b0b3-7167644778c6 | -5.51072 | -44.39323 | 2025-11-15 04:04:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4924b34c-0cb3-3f28-bc7b-e1be7b946bae | -6.15526 | -48.0428 | 2025-11-15 04:04:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e282bc01-32cf-3a50-8c99-743a0a822e47 | -4.18918 | -43.80777 | 2025-11-15 04:04:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 578150e5-e919-37e0-9fb0-23629998deb8 | -4.88022 | -44.95913 | 2025-11-15 04:04:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0ce1ce0-6fba-3ebd-9806-fd87122d1604 | -6.28501 | -41.75546 | 2025-11-15 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a1a72f90-ba39-3870-bfe1-baeef54bcffd | -4.39873 | -45.82777 | 2025-11-15 04:04:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc2ce078-2502-3127-ab07-e598c318171f | -5.24139 | -44.34486 | 2025-11-15 04:04:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 06b9a3cc-660c-3ffd-ba35-cd74fb002715 | -3.22402 | -45.48329 | 2025-11-15 04:04:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b7960d61-c27d-3065-bb22-4da41c4b236b | -6.30111 | -41.83044 | 2025-11-15 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ab515d18-14fb-35f3-bf84-4116e410fc23 | -6.88907 | -42.06121 | 2025-11-15 04:04:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b4024dba-7e42-3728-bd04-f6518e438dd5 | -4.37458 | -47.25 | 2025-11-15 04:04:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca4b8093-b0b2-3007-aff1-72f193d2a4e7 | -5.05168 | -44.67826 | 2025-11-15 04:04:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4122ab52-1f1c-3f85-939c-ef42f5887c25 | -5.50749 | -40.54527 | 2025-11-15 04:04:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cc0db08b-4b3a-3cd3-b35a-38ab16c5f10d | -1.29634 | -49.05684 | 2025-11-15 04:04:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35fd44e7-c140-3bd4-b851-a59ee9062492 | -3.99115 | -44.27998 | 2025-11-15 04:04:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23323ba4-4040-35e5-8f3d-e17d5e5675e2 | -3.21962 | -45.48256 | 2025-11-15 04:04:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f59ec22c-c9f0-3056-a97e-5c8197272b3b | -4.8393 | -44.75772 | 2025-11-15 04:04:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe0d5396-d0a4-339b-9c31-9f39485bb00f | -3.46268 | -40.50496 | 2025-11-15 04:04:00 | NPP-375D | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2dac2d74-c0c6-37ba-b3c8-ae1b87a25602 | -6.29768 | -41.82988 | 2025-11-15 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2ea1c6c8-d850-33bd-aefc-15ffa46e7874 | -4.42971 | -43.66087 | 2025-11-15 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8c2d233-b8a8-3f66-b3c3-4d8b981faeaa | -6.22862 | -41.73483 | 2025-11-15 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4db7ed2b-b57b-3d10-a948-1115e3113568 | -2.73596 | -45.31088 | 2025-11-15 04:04:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37438ca1-5fe2-3d36-b064-0591bfaaa840 | -6.28235 | -41.72834 | 2025-11-15 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 14214fd4-fd01-3840-8a37-acaee8b1421e | -5.5391 | -44.94714 | 2025-11-15 04:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10e21302-99bb-3a0f-aa10-959a9e16729c | -3.51193 | -42.79479 | 2025-11-15 04:04:00 | NPP-375D | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18f7e2b2-0cc3-3eb4-bfac-cc433c1414b1 | -3.05959 | -47.11504 | 2025-11-15 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b45af9ff-e672-3caa-8d09-393172ff0c3d | -6.27191 | -41.74952 | 2025-11-15 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6202b641-920f-3fec-aa75-7854b0b5c465 | -3.99346 | -44.26602 | 2025-11-15 04:04:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d8e3a1d-a67e-3590-a5c0-a8e0f6a0e78c | -3.17155 | -48.6115 | 2025-11-15 04:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ca7a70a-dc7b-3f27-a38b-3131937e0e02 | -5.23826 | -44.34735 | 2025-11-15 04:04:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 96e8b289-a43d-3545-9c44-b3f4e5940990 | -5.53849 | -44.9508 | 2025-11-15 04:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7f60694-cb20-37eb-855b-9ed543f83f3b | -4.10584 | -50.06596 | 2025-11-15 04:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 29bf9390-6489-37ea-9392-a639bae9035f | -4.05227 | -46.4189 | 2025-11-15 04:04:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b66fa045-0f5a-326c-934f-a7d297b1d1b5 | -4.70127 | -40.12359 | 2025-11-15 04:04:00 | NPP-375D | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9debb17a-e60f-313d-8bc3-31a34c85e103 | -4.60933 | -41.74399 | 2025-11-15 04:04:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6cbcc14c-1ccb-34d4-a2c6-1bef9e4a928e | -6.2862 | -41.74803 | 2025-11-15 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 283b77cc-4e1d-3ecf-9369-c31277bbf0e5 | -6.73088 | -42.968 | 2025-11-15 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 418c3f10-9347-3642-838a-345f751eae69 | -3.66052 | -44.81502 | 2025-11-15 04:04:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b596126-4a5a-3395-b577-2b34c827f049 | -4.90311 | -44.04587 | 2025-11-15 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4a88db5-4ea9-3b6b-bebf-557f87c50fba | -2.80431 | -52.96846 | 2025-11-15 04:04:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ebdf0ff-15fb-38d3-95a2-6a1431760059 | -3.98945 | -44.26536 | 2025-11-15 04:04:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70ef5f12-50e6-3629-8c1f-c472e1437df5 | -6.74345 | -41.42636 | 2025-11-15 04:04:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 945d2d51-a8e9-3f72-8ffe-566e48946093 | -4.33603 | -47.56767 | 2025-11-15 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README21.md)
