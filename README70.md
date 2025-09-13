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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12bdddfb-6f5f-312f-b43c-370574ccd913 | -17.42457 | -49.25765 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d7ac2d50-9fe1-3b2c-a28a-8e48358d9cfe | -20.60435 | -50.40017 | 2025-09-13 04:10:00 | NOAA-20 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e7069d08-e4e4-39e7-9e8b-930b42dedf4f | -21.00395 | -44.85698 | 2025-09-13 04:10:00 | NOAA-20 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 47bbd615-4f88-3a60-ac6a-ac82c9f8d685 | -17.496 | -44.32049 | 2025-09-13 04:10:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6fc0dce-edb0-363a-a786-4cd53de10ad5 | -21.62583 | -46.81975 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ece827a8-18d9-3c79-9ae8-9e8d1851de3e | -21.65005 | -44.38565 | 2025-09-13 04:10:00 | NOAA-20 | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 693c63cd-8707-34fa-aa1c-04ce235f4af5 | -15.77683 | -52.25066 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9cd5691e-02f5-3cd7-80f7-35f46ff20e53 | -16.64153 | -49.77661 | 2025-09-13 04:10:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cf780053-6c8f-3624-88f6-ef6e74b3a75a | -19.65306 | -45.8633 | 2025-09-13 04:10:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4412e52d-b663-3c73-899b-d77dda61d84a | -22.16081 | -47.37163 | 2025-09-13 04:10:00 | NOAA-20 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 1d02cd43-53d8-3f43-9db7-400d6290eb59 | -21.65004 | -50.12263 | 2025-09-13 04:10:00 | NOAA-20 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b3fdca1e-0c14-3a15-864e-34e76f9d7b04 | -15.16947 | -52.49941 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a4d31070-5ba2-328c-ba7a-34011faa8afc | -15.118 | -52.46308 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52f3bcc1-65fd-33bd-87c9-9ecb0f5f4713 | -21.62039 | -46.81052 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 86459dff-4c11-3c51-83fc-21e035e87fc9 | -15.1581 | -50.16528 | 2025-09-13 04:10:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 612f32c8-4f9b-31fa-a8ff-2151c8e2ac1f | -15.38056 | -52.10868 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8cbfac4e-debc-35a0-ba36-f1698cc01da7 | -16.11753 | -46.94614 | 2025-09-13 04:10:00 | NOAA-20 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4db2d1ca-0db1-336a-b326-1d5947e0f41e | -18.32646 | -50.9691 | 2025-09-13 04:10:00 | NOAA-20 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f1b812c-eb28-3755-bc38-4f46abaf096d | -19.06968 | -48.72408 | 2025-09-13 04:10:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dafb494f-6ada-3567-ae0d-ee6194e6cfa4 | -21.93323 | -47.57191 | 2025-09-13 04:10:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18f9224f-c780-3ab5-86c4-7f66060695f7 | -20.45019 | -46.43999 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55f5aad9-9f37-34fb-ab61-7c44ea91f59b | -17.1398 | -48.50807 | 2025-09-13 04:10:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 87ae2b47-9b25-3f6b-b79e-b77011bcbe16 | -16.64223 | -49.77287 | 2025-09-13 04:10:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 54004221-7da3-3a48-98df-a549c86c9043 | -17.44385 | -49.24271 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 867b5a62-8665-3c56-a52c-75ad4da13529 | -16.09652 | -46.95277 | 2025-09-13 04:10:00 | NOAA-20 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a6a4ce0-577d-3d81-92c7-58466d8678e2 | -14.99867 | -50.12323 | 2025-09-13 04:10:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 35fd84fe-011b-361a-908c-367777171bb7 | -18.12596 | -51.7162 | 2025-09-13 04:10:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18399f52-fece-36f2-956e-05386702a8b2 | -16.65102 | -44.92971 | 2025-09-13 04:10:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f68dcfa9-a7e9-34df-a9aa-06407a70ac75 | -14.61858 | -52.0857 | 2025-09-13 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b57cdc2-33ed-3f59-867a-2d24fb7fde6b | -17.54799 | -44.54874 | 2025-09-13 04:10:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6fe21073-83e9-3c79-8afe-9d5b2295060e | -21.07053 | -47.00879 | 2025-09-13 04:10:00 | NOAA-20 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15e8b9be-895d-3ae6-b139-ad65aed818c8 | -21.65277 | -50.12374 | 2025-09-13 04:10:00 | NOAA-20 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c8423a45-a1d7-3e1f-97ca-f497d80d19e6 | -17.46781 | -43.72335 | 2025-09-13 04:10:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 926521bb-75ea-3d00-b8b8-5ff4007d2a0b | -14.63327 | -52.091 | 2025-09-13 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ba586ed-38b7-330d-ba8f-3d20bdd589db | -15.24563 | -51.3947 | 2025-09-13 04:10:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| da121e62-86fa-337a-8cf6-25234e94bf81 | -18.76362 | -48.19534 | 2025-09-13 04:10:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 419768a4-6c4f-32a8-9f00-1ab51dbfad44 | -16.49193 | -55.14194 | 2025-09-13 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ac3f8b93-f70c-35bc-95bd-5b0a015d0d17 | -16.07022 | -49.99103 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8ce17a25-2bbf-3deb-9d38-e1b126d019d8 | -15.15457 | -52.49375 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c8e4495-a2cd-3704-81ef-83b8b09a9211 | -16.4928 | -55.13778 | 2025-09-13 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 344fe7a5-beeb-3adc-aad0-aff1b11716be | -15.75787 | -53.49897 | 2025-09-13 04:10:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f44d2e82-e5d2-3917-912e-7813b2bf3955 | -16.06941 | -49.99537 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 73bc4a05-8eac-3611-9c27-05c168960d2d | -22.12314 | -47.41188 | 2025-09-13 04:10:00 | NOAA-20 | SANTA CRUZ DA CONCEIÇÃO | SÃO PAULO | Brasil | 3546207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 40ecf88d-1418-3075-9f4b-3bff4891ebe1 | -17.30921 | -48.73476 | 2025-09-13 04:10:00 | NOAA-20 | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e2b354e1-cc2c-31c4-9294-4daa7f465f50 | -21.29981 | -44.93907 | 2025-09-13 04:10:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5315a10a-10b7-3f6d-abfc-9734051b164b | -16.92862 | -51.89088 | 2025-09-13 04:10:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2f1a488-ca78-3cac-bf0c-dbca680c5a37 | -15.50488 | -47.29499 | 2025-09-13 04:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcdefba5-64d3-3a06-b8c5-fe45f3cfc978 | -18.15441 | -49.19009 | 2025-09-13 04:10:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 21.6 |
| b42d9a5a-334a-3dae-b952-a082f0248be4 | -16.52956 | -51.75725 | 2025-09-13 04:10:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02c7f60c-024b-3f97-ab43-c869a6f543e3 | -21.61291 | -46.81337 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| be92a459-71ce-36ff-886a-daee2ec788dd | -15.77536 | -52.23161 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0dc8999b-222d-3eb5-9b98-4b32d085a8d7 | -18.47462 | -39.76156 | 2025-09-13 04:10:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 42bce329-3658-3ea5-9e55-6f9f3f11627d | -17.42449 | -49.23538 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0762261-d51d-3cab-861c-7b37bb881396 | -15.07759 | -52.49695 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 522c1b2a-f1a5-328c-8bdb-e4aba4fb58c7 | -15.68365 | -49.89639 | 2025-09-13 04:10:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9a4ece38-c227-3223-9e11-aae1c5277be6 | -22.79669 | -47.80687 | 2025-09-13 04:10:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bdd995fe-41ed-3862-a656-8a210e253a5a | -18.06788 | -45.4526 | 2025-09-13 04:10:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 115dbd30-3ed0-38e7-99bb-f3e11ec82be1 | -15.50766 | -47.29369 | 2025-09-13 04:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02ca193b-a572-380c-82e6-597064aa397c | -16.56187 | -49.2345 | 2025-09-13 04:10:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 247be487-7590-35a9-a0ff-f70be48b0799 | -17.41789 | -49.24882 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7cfcc2a9-743c-3946-a79c-569dcb8ed3b2 | -16.64572 | -49.7774 | 2025-09-13 04:10:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 20805675-f8a0-3140-a4bb-72fdeb1a7488 | -15.11214 | -52.49226 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 10944989-25dd-37c9-ac5a-740050789730 | -16.35513 | -51.53379 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c3dd551f-6437-3058-a11b-18240fef1caf | -16.4987 | -55.15439 | 2025-09-13 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| be1ba8be-93dd-3c41-8b9a-997965100bfd | -20.73347 | -56.74088 | 2025-09-13 04:10:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0318be0e-bf93-372b-a24d-63e870f5fba7 | -20.61546 | -50.22898 | 2025-09-13 04:10:00 | NOAA-20 | MAGDA | SÃO PAULO | Brasil | 3528304 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c583d01-cb4d-3aaa-a54d-367d30103829 | -17.54077 | -44.55123 | 2025-09-13 04:10:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b74449d7-3fc6-342a-afb2-06f1206b63b6 | -17.99221 | -46.92308 | 2025-09-13 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d14be8ac-30dc-3416-a2fb-3addd962b974 | -17.13002 | -48.49604 | 2025-09-13 04:10:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19d30c6f-e23f-3d51-bfc6-65abdc8ec276 | -15.69603 | -50.57732 | 2025-09-13 04:10:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad70e1b1-0c6d-30cf-9953-b732aca1ba3e | -20.02264 | -47.65225 | 2025-09-13 04:10:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82248d5c-b097-3194-a3e6-8c31fda4556e | -17.35819 | -42.70793 | 2025-09-13 04:10:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92ee1a8f-16e9-3530-a0f8-9ff009fc5f63 | -20.54873 | -45.83443 | 2025-09-13 04:10:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6010c645-d879-34a2-9053-c397d77c056d | -20.59551 | -50.40229 | 2025-09-13 04:10:00 | NOAA-20 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5057f799-d1bb-3cf8-81ab-badfa1234098 | -18.43816 | -45.93122 | 2025-09-13 04:10:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fcd8398-c4d1-3cd9-ab1a-fa65a3e7a83d | -17.13178 | -48.48612 | 2025-09-13 04:10:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6dc32fa-ca94-3d4e-8165-c199fca8d820 | -20.45357 | -46.44061 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b9540ce-f483-3f69-87d0-498bb4772f11 | -19.98301 | -46.91612 | 2025-09-13 04:10:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fca3a5d8-6172-376a-b6d5-38faaa41baad | -17.45643 | -45.09476 | 2025-09-13 04:10:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1152ebb2-41bd-37ee-9b51-84a289183898 | -16.07931 | -49.96608 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f68ee4c-e1e0-3a71-82e7-b604b47aebba | -15.59551 | -54.75954 | 2025-09-13 04:10:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4288c2d6-d1f1-33a7-94f3-a375b63f5edd | -17.35048 | -42.63424 | 2025-09-13 04:10:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 55464c70-5bf0-3735-8e57-3c2cf5731abb | -17.44447 | -49.23926 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9a23389e-a38a-3ca0-b727-2a6663e7d101 | -18.32999 | -50.9745 | 2025-09-13 04:10:00 | NOAA-20 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4d5f29e-2b0b-3f30-affa-1e466a8f810f | -16.11102 | -43.63026 | 2025-09-13 04:10:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9709b131-b44d-397b-9cb1-5500c887d052 | -15.77082 | -53.49686 | 2025-09-13 04:10:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ff7e8b8-9f24-314d-a4f5-dd617c9f201f | -14.63122 | -52.1013 | 2025-09-13 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86d4a1d2-b8fd-37be-a634-c06dbb1fb475 | -16.06512 | -49.99456 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 4fc7fb93-4248-30af-9573-e717b31447de | -15.13518 | -52.48388 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9827e005-818d-3cb6-ac74-7da7bd722a89 | -15.76461 | -53.49958 | 2025-09-13 04:10:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c48b0e68-0d57-3e34-9970-7ba6bafa0feb | -18.17921 | -45.20495 | 2025-09-13 04:10:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 174c6467-408a-37e9-9383-49798a17142d | -21.61973 | -46.81442 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| 9b4a4382-22d0-391b-8f10-4c9c49ddb3da | -15.0697 | -52.48262 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 612026ef-3727-38a7-8c44-e72a674d207d | -16.1391 | -49.92152 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93f05933-73e8-3419-bfd5-e011731628a5 | -16.40652 | -49.03191 | 2025-09-13 04:10:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d63fe26a-5177-3609-9395-ced63a1a6a2a | -16.36495 | -51.53803 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d637a216-7204-3850-be33-a8d74e63fcb8 | -21.64987 | -50.11757 | 2025-09-13 04:10:00 | NOAA-20 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3106736d-a503-3901-b9df-02f845cd4d2f | -16.01351 | -47.92589 | 2025-09-13 04:10:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b8e20dd-cc35-3ff6-998c-e962ca5951f4 | -20.57951 | -47.35402 | 2025-09-13 04:10:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 39b3e8ef-c16b-31eb-ab89-7746b33cf42f | -16.50418 | -51.78572 | 2025-09-13 04:10:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README71.md)
