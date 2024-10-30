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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f78e8b9e-980c-3038-ba23-7e3df5ea3144 | -10.623 | -44.923302 | 2024-10-30 00:49:45 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4f2d6744-f335-39fa-940c-753ad89b253c | -11.9292 | -50.699001 | 2024-10-30 00:49:46 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c61251a4-0f29-37d9-ba30-a24adf5088c5 | -11.26 | -47.894402 | 2024-10-30 00:49:46 | METOP-B | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5f67d58f-bca0-333a-acb1-52e09aeb9cf3 | -10.6351 | -47.698002 | 2024-10-30 00:49:55 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 17b99214-6b7e-3a4e-86ef-f6b5b5665c5e | -10.517 | -48.9958 | 2024-10-30 00:50:02 | METOP-B | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f64c0c2b-0c6d-32f0-8de4-71ef5e8de7ed | -10.5189 | -49.003899 | 2024-10-30 00:50:02 | METOP-B | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8c668a23-1205-37a4-b991-b60e1a58a7b8 | -10.3049 | -48.883099 | 2024-10-30 00:50:05 | METOP-B | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8de1eaaa-c332-3094-ac6c-6bef6f2f9689 | -10.2011 | -48.528099 | 2024-10-30 00:50:06 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 36d507bb-6c4f-3e9f-8ff6-c2088339c5fb | -10.1105 | -48.450001 | 2024-10-30 00:50:07 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b9341031-066b-33e0-87eb-9279a23041b4 | -10.1126 | -48.458599 | 2024-10-30 00:50:07 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 003bd6ec-7fe2-3dc1-9b08-74b121d4c748 | -10.317 | -49.4683 | 2024-10-30 00:50:07 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c828cb0a-e363-33f2-9d1a-355d603d678d | -10.3187 | -49.476002 | 2024-10-30 00:50:07 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 511bdd9f-0069-3576-aab4-c755e991f0b3 | -10.3543 | -49.6297 | 2024-10-30 00:50:07 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 28e72205-66e7-3dc1-9660-e9dc25912300 | -10.3561 | -49.637299 | 2024-10-30 00:50:07 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 77107cd5-6cc7-3573-9942-b9b964c089a3 | -10.3578 | -49.645 | 2024-10-30 00:50:07 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8a1c9983-3833-3686-b1d3-60c4e8b25810 | -10.2189 | -49.1343 | 2024-10-30 00:50:08 | METOP-B | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2a2dba07-36fe-3be7-aa51-4e4e30c319cb | -9.5944 | -46.627998 | 2024-10-30 00:50:08 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 056d2241-f26b-3780-b569-d21199899be5 | -9.9587 | -48.947899 | 2024-10-30 00:50:11 | METOP-B | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0afa983b-ba7c-3825-af3d-c69e9d1c1dc0 | -10.5733 | -51.911701 | 2024-10-30 00:50:12 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d203f891-10ff-3fd4-8a73-43c4611173aa | -10.6278 | -52.388199 | 2024-10-30 00:50:13 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5327a354-b9ed-389e-9880-f099d0720773 | -8.9732 | -47.611599 | 2024-10-30 00:50:22 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e1748bff-94e9-36ec-b081-64f734f6b47c | -8.9634 | -47.613899 | 2024-10-30 00:50:22 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3e8316a2-e6db-3a5c-a14d-d24bb90992a0 | -8.9657 | -47.623798 | 2024-10-30 00:50:22 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c2eb2e71-5131-38c9-99de-9c7c658bd658 | -8.9681 | -47.633701 | 2024-10-30 00:50:22 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ab84cdd0-f685-388e-901a-b506baafd946 | -6.9888 | -41.310001 | 2024-10-30 00:50:29 | METOP-B | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 42866e21-4edc-3210-8f58-454a65798eba | -6.9959 | -41.338001 | 2024-10-30 00:50:29 | METOP-B | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 117c55ab-55ba-362d-bf16-04456568a65a | -6.9792 | -41.312401 | 2024-10-30 00:50:29 | METOP-B | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cebf62ca-7102-31a7-9ecc-7ef362bdede2 | -10.0515 | -54.311798 | 2024-10-30 00:50:29 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f4cc7908-fa5f-3a08-b3f2-1029e4718f23 | -10.0532 | -54.3195 | 2024-10-30 00:50:29 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 117aca2c-07a0-3866-907a-4f0ce39147b0 | -8.8558 | -49.842701 | 2024-10-30 00:50:32 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc41760a-266c-3113-b570-f58561b2884b | -8.8575 | -49.850399 | 2024-10-30 00:50:32 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bd02f6e-30fb-30bd-9c52-16dbf5ab02a6 | -7.8897 | -46.875099 | 2024-10-30 00:50:37 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 487a75cb-7529-3319-9d18-f0bf6bb70d87 | -7.8924 | -46.886501 | 2024-10-30 00:50:37 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8fcfd4db-1ada-3f7e-8c39-93703e037018 | -7.8952 | -46.8978 | 2024-10-30 00:50:37 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6e630868-45a3-387d-a8ee-a8d0e85f2d58 | -7.88 | -46.877499 | 2024-10-30 00:50:37 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5789e502-5baf-38fa-9d53-bcdd6bd5b93b | -7.8827 | -46.888901 | 2024-10-30 00:50:37 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3f413d6e-925e-3a0e-b2ec-9c938e42d201 | -7.8855 | -46.9002 | 2024-10-30 00:50:37 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| de97bace-e606-30b1-acf6-fde0bc8559ef | -7.8702 | -46.879799 | 2024-10-30 00:50:37 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e7d2d06-fb1d-31e0-966d-1656056f0474 | -7.873 | -46.891201 | 2024-10-30 00:50:37 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ef9575eb-ceee-377a-bbd1-b41719d622b4 | -7.6843 | -47.3102 | 2024-10-30 00:50:42 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 96c00816-6296-3fd5-ad15-4aa4217ebdd4 | -7.6745 | -47.3125 | 2024-10-30 00:50:42 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 13d97193-5c9d-3eba-a951-192dd505bb33 | -7.4452 | -46.611301 | 2024-10-30 00:50:43 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e1d1540c-a661-3f37-9915-e9a74b2f8587 | -7.4983 | -47.135399 | 2024-10-30 00:50:44 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2295f204-e125-32dd-b031-60fc99558fb6 | -7.5009 | -47.1465 | 2024-10-30 00:50:44 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d9cb18bd-4410-3fd6-872b-a458a70702d7 | -7.2564 | -46.554401 | 2024-10-30 00:50:46 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1055043e-dc7e-31f5-8621-75176af4da5d | -7.3503 | -48.472401 | 2024-10-30 00:50:51 | METOP-B | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ed97c79e-d92e-33a1-b8d5-c49901225651 | -6.8971 | -46.8186 | 2024-10-30 00:50:52 | METOP-B | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 91bfa0f4-c612-31bd-8958-454d59674c7c | -6.8874 | -46.8209 | 2024-10-30 00:50:53 | METOP-B | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bf01810b-3acb-3930-bf49-89766c3dec64 | -5.9873 | -45.342999 | 2024-10-30 00:51:01 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 74f796ee-a364-3e5b-bf1a-1db8643bc695 | -5.991 | -45.358398 | 2024-10-30 00:51:01 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2c0fc4b5-f8f7-30bf-aa56-4fee35e8a717 | -5.9776 | -45.345299 | 2024-10-30 00:51:02 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 535df9a2-e2e4-352e-a0af-6942b7a2d60e | -5.9813 | -45.360699 | 2024-10-30 00:51:02 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d628c543-44b5-376a-b08b-4542acb51b86 | -5.985 | -45.375999 | 2024-10-30 00:51:02 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65b77f50-b966-3aab-ac58-69b666b14bd3 | -5.5617 | -44.306099 | 2024-10-30 00:51:04 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2088ab9b-b7f7-38c1-bab2-0d883e674c33 | -5.552 | -44.308498 | 2024-10-30 00:51:04 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0d823581-c7d8-3943-bcef-761280232306 | -6.0603 | -46.591301 | 2024-10-30 00:51:05 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 405ac6da-7d25-3a23-bfb9-635fd50eeb42 | -5.3116 | -44.926498 | 2024-10-30 00:51:11 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f87a8053-5573-3f2b-8b77-60cc6458fc0c | -5.3019 | -44.928799 | 2024-10-30 00:51:11 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3929eddb-aa30-3ca0-a026-92ab87932f05 | -5.547 | -46.509998 | 2024-10-30 00:51:13 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7fc8865-631c-3737-af96-c44f6c240840 | -5.55 | -46.522999 | 2024-10-30 00:51:13 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 28e8514e-d31f-3c3c-abac-10e0145ac142 | -5.0161 | -44.34 | 2024-10-30 00:51:13 | METOP-B | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a544f05-2b76-3479-9688-4841581269c7 | -5.0207 | -44.358601 | 2024-10-30 00:51:13 | METOP-B | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| de48d8d7-2b11-362a-a9e1-f374368367a4 | -5.0064 | -44.3423 | 2024-10-30 00:51:13 | METOP-B | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a55abc3a-bc88-37f8-ad88-754620358ded | -5.011 | -44.361 | 2024-10-30 00:51:13 | METOP-B | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 114c02f7-5b87-3e87-b75e-60c2c75adcb9 | -4.5093 | -43.095299 | 2024-10-30 00:51:17 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78555f49-37db-3b3b-af50-23087cce626a | -4.515 | -43.118599 | 2024-10-30 00:51:17 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d421aafd-862e-349f-a711-df55113a97ca | -3.9438 | -41.449699 | 2024-10-30 00:51:19 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c5dce57a-ed10-32c4-b726-1623573511cd | -3.9514 | -41.4804 | 2024-10-30 00:51:19 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5cf1b60f-9b85-3358-8b60-517400b6f5c0 | -3.9342 | -41.452 | 2024-10-30 00:51:19 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 79be0e8e-76c8-38d4-8e7b-b59e65e69caf | -3.9418 | -41.4828 | 2024-10-30 00:51:19 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 88c31739-259d-3989-952f-f0a96f5da87c | -3.9247 | -41.454399 | 2024-10-30 00:51:20 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9e23e98c-65f9-316f-a65f-c8bad64f33b2 | -3.9323 | -41.4851 | 2024-10-30 00:51:20 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 61bbe8c3-df3f-35c8-a684-2970eb5ba052 | -4.3644 | -43.7626 | 2024-10-30 00:51:22 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c1fa33b2-cfd2-362a-a2df-9781feea9b16 | -4.2709 | -43.4184 | 2024-10-30 00:51:22 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3608fdb2-3cda-3daa-98d4-f415df645e83 | -4.2763 | -43.440701 | 2024-10-30 00:51:22 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 316ae450-fe02-39f6-b266-a258d9f9b8b5 | -4.3497 | -43.7439 | 2024-10-30 00:51:22 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b54ec4c7-3e3d-3e66-9f5f-b0eca8d068e8 | -4.3548 | -43.7649 | 2024-10-30 00:51:22 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e3207279-8c67-3968-ad59-13fff2e3b63e | -4.3598 | -43.7859 | 2024-10-30 00:51:22 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 82573def-2ee0-34fa-916d-20b34a0222cd | -4.2612 | -43.4207 | 2024-10-30 00:51:22 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7a0fae76-4c2d-3d7c-8ef2-b41750fbcbb9 | -4.2666 | -43.443001 | 2024-10-30 00:51:22 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a196939-6297-33a9-8600-e5e5cf4195b3 | -4.34 | -43.746201 | 2024-10-30 00:51:22 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4a2701dc-76db-3613-a469-3642446bc7eb | -4.3451 | -43.7672 | 2024-10-30 00:51:22 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4dd842f8-43a9-3d62-a6db-a5716fc0aefa | -4.3501 | -43.7882 | 2024-10-30 00:51:22 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a0c31ee9-1074-3ea1-be25-1d6cb9e2e0ae | -4.3354 | -43.7696 | 2024-10-30 00:51:22 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8da596a-5a53-3ab4-81db-8f11b2c33ba9 | -4.7048 | -45.650002 | 2024-10-30 00:51:23 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6321246d-a52a-3028-97ce-f0abdfb9afa9 | -4.7085 | -45.665401 | 2024-10-30 00:51:23 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 574131be-302b-3171-8eb4-793fd04fc44f | -5.2444 | -47.931499 | 2024-10-30 00:51:23 | METOP-B | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 4e87f90a-f2d5-3010-99d3-804deba908b5 | -5.2469 | -47.942101 | 2024-10-30 00:51:23 | METOP-B | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| bc823de2-23fd-34bc-a89d-c439a8bb140c | -4.7097 | -45.713501 | 2024-10-30 00:51:24 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 40217553-316c-3cf0-b8cf-708539c7fce5 | -4.7133 | -45.728699 | 2024-10-30 00:51:24 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8935b57f-2aa5-3bcf-99f6-895a984eb329 | -5.2347 | -47.9338 | 2024-10-30 00:51:24 | METOP-B | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 214c6140-6d28-3eb2-a24f-358ec6b460d0 | -5.2372 | -47.944401 | 2024-10-30 00:51:24 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5d1b39c9-175f-36ff-a675-8253e5513772 | -4.628 | -45.586498 | 2024-10-30 00:51:24 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 637279bd-a1c9-3ff0-b23a-8414f8fce96a | -4.6318 | -45.6021 | 2024-10-30 00:51:24 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a7d293e6-d244-3385-997c-4ac0bfd896cd | -4.4411 | -45.793098 | 2024-10-30 00:51:28 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1620d85f-07f2-3bcb-a3b1-60394acb261b | -4.4447 | -45.8083 | 2024-10-30 00:51:28 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d64c8666-5fec-364a-8394-478a9cccad93 | -4.435 | -45.8106 | 2024-10-30 00:51:28 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7abd1211-3ee1-333e-817b-41d9daae2460 | -4.35 | -45.6688 | 2024-10-30 00:51:29 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 032600c0-55d1-3883-b031-70b87e135af6 | -5.4848 | -50.5214 | 2024-10-30 00:51:29 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9751ee43-e70b-3fb4-aeae-9f917bc132ea | -4.5102 | -46.430698 | 2024-10-30 00:51:30 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README14.md)
