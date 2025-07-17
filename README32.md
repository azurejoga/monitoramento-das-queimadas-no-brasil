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
| e8b59170-8c7e-3075-814c-d417bb0a5a80 | -6.89122 | -47.2513 | 2025-07-17 12:49:00 | TERRA_M-T | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| acc4ed43-0d4d-3fcb-8d95-82f4c5452008 | -5.86879 | -44.79987 | 2025-07-17 12:49:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| e92a703c-26be-3a7f-a04f-6dfee492e2ec | -6.17032 | -45.06073 | 2025-07-17 12:49:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| a10267e9-9357-35c3-97b2-c1ef9b3da8f6 | -5.66355 | -43.72809 | 2025-07-17 12:49:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 451cd5e9-7fbc-3d85-a80d-9ffd8c485d70 | -4.86222 | -45.30073 | 2025-07-17 12:49:00 | TERRA_M-T | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 6b944828-4639-3b65-8ffe-e0d73a584e11 | -10.18088 | -48.90919 | 2025-07-17 12:49:00 | TERRA_M-T | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 0655dd6c-260a-3b5e-8b1f-c9bfba1cfdae | -7.14129 | -45.30398 | 2025-07-17 12:49:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| b7895c28-a01d-35dc-9af7-d1afb760bd5b | -4.78076 | -45.33683 | 2025-07-17 12:49:00 | TERRA_M-T | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| f1f84626-a747-3a32-a7b4-6fda18c29bce | -6.68078 | -45.4764 | 2025-07-17 12:49:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 7541030d-ffd8-3e18-959c-0512a8dfac7d | -8.82411 | -44.51684 | 2025-07-17 12:49:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 69cbf385-d37d-37a7-bf73-285be0020105 | -6.89376 | -47.23183 | 2025-07-17 12:49:00 | TERRA_M-T | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 34.8 |
| ca164113-ffd4-31ca-b232-333851f3d11e | -12.47483 | -44.48763 | 2025-07-17 12:49:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 190.7 |
| 3d44216f-88d8-3fd0-98f5-e460ed069703 | -9.24939 | -48.56192 | 2025-07-17 12:49:00 | TERRA_M-T | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| cda7456c-f18b-342d-9c56-58b1f7955bc4 | -5.86749 | -44.82268 | 2025-07-17 12:49:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| c4d05c79-dd3c-3acc-84fd-4d003d5f2d0b | -10.5952 | -54.60979 | 2025-07-17 12:49:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 24bb59d4-7f42-39fc-b376-0234e8e64b1e | -9.80834 | -47.734 | 2025-07-17 12:49:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 35239790-3fc9-3b41-b4e3-3934b584c1ad | -12.43094 | -50.04496 | 2025-07-17 12:49:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 158.5 |
| e4a2cfd4-5722-3f5b-8d2c-fa60182bd02f | -6.1667 | -45.08889 | 2025-07-17 12:49:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 147969ab-0c3c-3b35-b178-9fc71c9b6dba | -7.70658 | -45.88049 | 2025-07-17 12:49:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| ff287c40-4ad3-337e-b3d0-b419a106f12c | -11.6879 | -47.94719 | 2025-07-17 12:49:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 4561a4b4-8641-3c8f-b50a-0ec9f661deba | -10.33832 | -49.92271 | 2025-07-17 12:49:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| d0c82f93-b4c1-3813-b088-c555ae9bd745 | -10.33541 | -49.91582 | 2025-07-17 12:49:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 1cb40b96-4f1f-3ed4-9aa3-0ff6a6273305 | -12.41636 | -45.37375 | 2025-07-17 12:49:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 67a64243-4175-34a1-b88e-d639b56e94f0 | -12.36439 | -50.37497 | 2025-07-17 12:49:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 80897efd-a6c2-3316-98bc-972f3a8c6391 | -10.97748 | -46.45052 | 2025-07-17 12:49:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| e6f0d8bd-9b4d-332f-b5a3-5b14f9352b5b | -5.87133 | -44.79348 | 2025-07-17 12:49:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 4997c526-722d-3216-80fa-0cbdf67e1e7d | -12.43271 | -50.03043 | 2025-07-17 12:49:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 2bc0ec17-d300-393a-b900-fc6cfde87e7f | -12.36262 | -50.38868 | 2025-07-17 12:49:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 5fc50157-8452-3336-940e-9c77c6b5267d | -4.59619 | -43.30056 | 2025-07-17 12:49:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 8bd34d53-64b2-3d66-8bef-e49d604b95bd | -12.48275 | -46.93349 | 2025-07-17 12:49:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 32.4 |
| f762eb1b-d66a-3398-a650-9f9476dce9b1 | -10.60772 | -46.24697 | 2025-07-17 12:49:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 33.4 |
| a72f1b2d-37c6-3d74-aefb-15264d637c95 | -10.67342 | -49.88544 | 2025-07-17 12:49:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b64e48cf-c058-34a9-8d62-8dd0450f9861 | -12.4006 | -50.46864 | 2025-07-17 12:49:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| bbcc4d19-52eb-3c43-9d64-d94e2eda991c | -12.41254 | -45.34464 | 2025-07-17 12:49:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 9e5e3165-33f3-38d9-b989-9f2a4c4ac1ba | -4.60094 | -43.30791 | 2025-07-17 12:49:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| fd0275c2-ca9c-3c83-908e-d79f7c32b779 | -12.56327 | -44.75086 | 2025-07-17 12:49:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| ded4ed70-156c-3dd3-a3eb-aca74f228037 | -10.33358 | -49.92954 | 2025-07-17 12:49:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 466ece19-4745-3447-91fa-b558c1766a83 | -6.67604 | -45.49671 | 2025-07-17 12:49:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 4dc3ef67-64f7-3bee-bbc7-af5103c19b36 | -12.47783 | -44.49466 | 2025-07-17 12:49:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 233.1 |
| 8321ec72-c5e5-343a-bfa5-303f1f0e8c5b | -12.5757 | -44.74529 | 2025-07-17 12:49:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 7e5087d7-452d-3aef-a8e3-18e64968cd0e | -12.37338 | -50.39006 | 2025-07-17 12:49:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 86119cbf-88ce-3364-a893-5e69b5b5f269 | -12.38593 | -50.37774 | 2025-07-17 12:49:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| f9aaa4ed-13ed-3ab3-a351-25bbc798577f | -6.92624 | -44.11746 | 2025-07-17 12:49:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 0daee16b-ab1c-3f25-a718-55bf41ff3ecd | -4.57108 | -47.73167 | 2025-07-17 12:49:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 630c386c-f18b-3610-bac3-ced465ffc612 | -9.80823 | -47.73975 | 2025-07-17 12:49:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 49032c40-7a29-3cc0-86ce-c642a2618baa | -9.24295 | -48.55453 | 2025-07-17 12:49:00 | TERRA_M-T | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 0280df13-9fc8-3c29-85d0-a03e16e41ddc | -8.82893 | -44.54547 | 2025-07-17 12:49:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 57.8 |
| aa6eb6eb-5c14-3d2b-aee1-6c2ca1ce481e | -7.35318 | -44.20142 | 2025-07-17 12:49:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 57.4 |
| cf1b7554-2e67-3ddc-9c2e-76fb7587a078 | -12.48566 | -46.90788 | 2025-07-17 12:49:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| ca533ad0-516f-30cc-94b0-a804193e4106 | -12.42011 | -45.34 | 2025-07-17 12:49:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 38.4 |
| a207b447-c122-3ddf-a387-9103a4ffcfa5 | -11.62855 | -50.13298 | 2025-07-17 12:49:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| bb61a29f-5a3d-3ca3-a950-4943d04c2b36 | -8.82012 | -44.55141 | 2025-07-17 12:49:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 66.7 |
| b64d6c13-7c5a-3ef1-a686-bd8ca0568a8e | -6.10801 | -49.59612 | 2025-07-17 12:49:00 | TERRA_M-T | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| a281853b-3795-3903-914a-846fdd2e9f30 | -11.68649 | -47.95369 | 2025-07-17 12:49:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| f63bd8ab-6e52-3ba4-a1cb-6c9421fd79c8 | -7.90232 | -55.41494 | 2025-07-17 12:49:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| b7221f31-dedf-3916-aef2-b20b41d71de0 | -7.34585 | -44.19472 | 2025-07-17 12:49:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 5bf8255a-a0fe-35b0-b335-890e1957e1c7 | -12.37516 | -50.37636 | 2025-07-17 12:49:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 6b1d0022-5e49-3cb8-86a5-b78da96b76c6 | -7.50916 | -55.01005 | 2025-07-17 12:49:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6fd636b1-8088-3d2b-b56a-511b950232f5 | -10.3851 | -49.90078 | 2025-07-17 12:49:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e13255db-d8c2-3b02-9ad6-3d5c0aa9db20 | -10.75705 | -49.59631 | 2025-07-17 12:49:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9861bf54-3811-3f6f-835b-41b26d699b2f | -4.56563 | -48.01093 | 2025-07-17 12:49:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 14df4f7e-3049-334a-a33b-ae67f5579403 | -12.42991 | -50.03905 | 2025-07-17 12:49:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 312.9 |
| d8a34f90-41d3-3528-898d-de0b235d5d11 | -8.8885 | -44.7969 | 2025-07-17 12:49:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 16868427-7c4b-3007-b3fc-38e1b3058e33 | -12.47041 | -44.5272 | 2025-07-17 12:49:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 7dfe5bcf-dc86-33b1-b952-7252191570ee | -10.97463 | -46.47519 | 2025-07-17 12:49:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 6d966bc1-8f1d-343c-a5e2-f6ce2870165f | -6.10972 | -49.58359 | 2025-07-17 12:49:00 | TERRA_M-T | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| cc27d9aa-4218-32ef-baa6-a96c66aa3c27 | -6.67747 | -45.50363 | 2025-07-17 12:49:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| a6cbd587-f39e-3d85-ad4a-b612c77b435d | -12.41884 | -50.03768 | 2025-07-17 12:49:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 2119c67a-161a-3d51-97a9-05bfdaab6aaa | -12.40906 | -45.37838 | 2025-07-17 12:49:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 9552d53d-7574-335c-8af5-0ced66e7cb9d | -12.40231 | -50.45508 | 2025-07-17 12:49:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 867477b9-8707-3ffe-98d2-6eed55f527b7 | -12.43178 | -50.02452 | 2025-07-17 12:49:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 040d5886-aa05-34c3-a400-5806c17aeed6 | -11.69946 | -47.95503 | 2025-07-17 12:49:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| dfc258e1-ab92-3e99-a675-3a6b517a096b | -12.4862 | -44.4928 | 2025-07-17 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 5ff03ae9-17e3-380c-816d-97c4b6fb8a27 | -12.3642 | -50.3911 | 2025-07-17 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 67710c3a-009b-38c7-9a6a-751f4814c100 | -12.427 | -50.0387 | 2025-07-17 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 377de89c-dc83-3973-99e8-b582cda049bf | -12.50398 | -57.77739 | 2025-07-17 12:51:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 0644e5fc-1351-3d60-8ec0-b8bde0efe482 | -14.09754 | -52.19793 | 2025-07-17 12:51:00 | TERRA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| cc613994-25a1-3c7a-bb6b-c8e40314bb36 | -14.31563 | -48.65208 | 2025-07-17 12:51:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 27.6 |
| fd6265f8-5c1c-3b7c-b9fa-3464efd06242 | -14.08781 | -52.19672 | 2025-07-17 12:51:00 | TERRA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 3a66b493-29b5-3d9b-841a-3512ecf0e3e4 | -17.20101 | -47.64889 | 2025-07-17 12:51:00 | TERRA_M-T | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 58.9 |
| b0df11c4-7ec2-3636-b6a0-fefcfe2d999b | -18.65322 | -55.73127 | 2025-07-17 12:51:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 4f297be8-e036-3fd1-bb6d-abd98fb27632 | -12.58802 | -56.97992 | 2025-07-17 12:51:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 43d5f2b1-4850-3e84-b3f2-cad5ca5bba5b | -14.08924 | -52.18559 | 2025-07-17 12:51:00 | TERRA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 4860f316-a907-35e1-a535-27bd441ad10e | -18.08936 | -54.28769 | 2025-07-17 12:51:00 | TERRA_M-T | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c10b04b0-e239-3137-b1e0-004fb6200006 | -14.72541 | -45.07288 | 2025-07-17 12:51:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 646f7016-2f9c-3296-8d85-7d821791dcd6 | -14.52032 | -47.66632 | 2025-07-17 12:51:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 61fee8ed-6d2c-3951-89c0-1e036f9e1f5c | -17.20354 | -47.65612 | 2025-07-17 12:51:00 | TERRA_M-T | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 2cde3d3a-c6a6-3546-aaed-c6a32c5cc075 | -20.43184 | -46.59752 | 2025-07-17 12:51:00 | TERRA_M-T | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 45137953-5cb8-39ea-9d16-83d68fd5b7cf | -15.37353 | -47.35184 | 2025-07-17 12:51:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 19.1 |
| a24e580f-dadd-3378-8dec-6e3ebd040fd1 | -14.7294 | -45.0803 | 2025-07-17 12:51:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 156.2 |
| 5b1f8e95-d1de-3e8b-bc88-037b2cb3f67c | -15.0692 | -57.00659 | 2025-07-17 12:51:00 | TERRA_M-T | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 9f506c37-ec2c-3845-8179-39249a278901 | -17.1643 | -46.11515 | 2025-07-17 12:51:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 1a8b453d-a836-33ca-bdd0-bfa7dd1ff648 | -12.50224 | -57.78862 | 2025-07-17 12:51:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a6b1fc41-27aa-3f88-9d87-3a601c097246 | -14.72137 | -45.11196 | 2025-07-17 12:51:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 400.6 |
| f1f70546-cc81-3c99-98c7-c7ae792388a7 | -14.02723 | -51.22348 | 2025-07-17 12:51:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 924caf31-6994-36b8-b3d0-9c8a65f71f50 | -15.37626 | -47.32679 | 2025-07-17 12:51:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 534514f3-4a77-3404-bcaf-f5f354ea0ab1 | -12.88002 | -49.19172 | 2025-07-17 12:51:00 | TERRA_M-T | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 45.9 |
| f7f1918f-4c12-3033-9788-5691c6724cb7 | -17.15599 | -46.12126 | 2025-07-17 12:51:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 46.8 |
| c58daf87-c083-3b55-a512-d5127547423b | -11.87513 | -55.45199 | 2025-07-17 12:51:00 | TERRA_M-T | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4f49be7e-bf3d-3b67-bd68-ee141a4fc614 | -20.44052 | -46.59228 | 2025-07-17 12:51:00 | TERRA_M-T | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 28.0 |


[Clique aqui para ver as próximas entradas](README33.md)
