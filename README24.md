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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eef5a22b-e59b-394f-8d3c-ad28a47a65ba | -8.00154 | -44.81178 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5cbe5869-d869-3507-a73b-8bb4587888fa | -8.00098 | -44.80928 | 2024-10-15 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f0bca19-2d36-385a-8140-449c358b7825 | -7.72116 | -37.43165 | 2024-10-15 04:02:00 | NOAA-21 | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ccaa8bfc-13cf-3590-9474-da0a085b67ff | -10.69627 | -37.05086 | 2024-10-15 04:02:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 75e5d48b-28e5-30a7-89d5-06e298e1c80c | -4.72224 | -38.45522 | 2024-10-15 04:02:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 7c44c8b8-3617-3284-8665-1f7ce23248e7 | -5.46669 | -37.17878 | 2024-10-15 04:02:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a1c6b30d-21ba-3312-9cff-1d3535bddb31 | -5.39177 | -37.80298 | 2024-10-15 04:02:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 62501dda-9cb2-38c4-9a23-6a72124365fe | -5.33726 | -37.83991 | 2024-10-15 04:02:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 31cf09a5-76b2-32ab-8122-5fce590b1989 | -6.84677 | -38.54597 | 2024-10-15 04:02:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c9acdd16-67fb-334a-97f3-5e3af83cfb49 | -7.87502 | -38.40365 | 2024-10-15 04:02:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a03ac9e7-57ef-366b-adcb-9cf0afd49b38 | -4.79163 | -39.77681 | 2024-10-15 04:02:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4ad130fa-9594-3e8e-beed-de6a7cb5677e | -4.79109 | -39.78025 | 2024-10-15 04:02:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9546ae13-cb9b-3c12-83dc-6da8d9f9a428 | -4.78833 | -39.77629 | 2024-10-15 04:02:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fc1ca008-e911-3678-b3d5-1289a69d5bb2 | -4.78779 | -39.77974 | 2024-10-15 04:02:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 57d81d3e-6936-356e-86fb-57fa0a686403 | -4.78725 | -39.78317 | 2024-10-15 04:02:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2246ed99-cd69-32e2-8117-b3350d459cd8 | -4.78558 | -39.77235 | 2024-10-15 04:02:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4fb87846-fe10-3f8b-b82b-74a200222b1a | -4.78282 | -39.7684 | 2024-10-15 04:02:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1eebcf29-6552-3560-a6ac-ba524536097a | -4.32989 | -39.13689 | 2024-10-15 04:02:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| a71e4b3b-3d48-3fe1-bb0d-fc34cf383933 | -7.15731 | -39.31232 | 2024-10-15 04:02:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 7b9f9a9e-b65f-3677-9544-84ebaf617f04 | -7.51762 | -40.51197 | 2024-10-15 04:02:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 646782a3-11e2-360c-a26c-98b68bdc934c | -7.24981 | -39.85292 | 2024-10-15 04:02:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7209aa1e-161b-3a85-a413-8d28248c1d37 | -9.37702 | -40.41584 | 2024-10-15 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 5c0cb93e-10b9-3dc1-ada3-04c7554ae7b0 | -9.34282 | -40.69859 | 2024-10-15 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c7f7a0e9-e6f6-367f-8a1c-29ce1a3a80d1 | -8.8664 | -40.87132 | 2024-10-15 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e926675c-d340-310f-8f86-53e41ff07d69 | -8.24349 | -40.28786 | 2024-10-15 04:02:00 | NOAA-21 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f2d240fd-92e6-3ddd-9024-67b65573e609 | -4.73204 | -41.47251 | 2024-10-15 04:02:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4a05291e-9224-3ba1-a9bd-0b20b7330c68 | -4.67019 | -40.26345 | 2024-10-15 04:02:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d1ef5956-0488-3946-9366-22ec79fa8623 | -4.66799 | -40.27738 | 2024-10-15 04:02:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ea325f2f-822a-3f69-945b-cdee48460701 | -4.57194 | -41.24372 | 2024-10-15 04:02:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 71d61777-b6d7-399a-9636-18cf875ffab3 | -4.23215 | -40.38665 | 2024-10-15 04:02:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b374dc69-417b-3a0d-aabf-09f7c941ae6d | -4.2316 | -40.39015 | 2024-10-15 04:02:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| db96830b-2f9b-3c75-b328-77169c63f206 | -4.22827 | -40.38964 | 2024-10-15 04:02:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7b4e8f11-4344-3d74-af85-ea1a854dc597 | -6.39957 | -41.61122 | 2024-10-15 04:02:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c519e841-cb2c-3ba2-b5c4-047b9aac887e | -6.39898 | -41.61489 | 2024-10-15 04:02:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e54b36e8-45e8-3881-98fe-a0e8f61b40a0 | -6.39839 | -41.61857 | 2024-10-15 04:02:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 880cebbb-c4bc-386a-8920-08a90845e93f | -6.3978 | -41.62225 | 2024-10-15 04:02:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bf90b2ad-d1c2-37ff-b0d1-75cf0f4488cf | -6.39383 | -41.62536 | 2024-10-15 04:02:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 704731e5-19b8-345c-9fe1-f2c818bc9615 | -6.39221 | -41.61377 | 2024-10-15 04:02:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 232348be-0490-3cbd-ac89-e87fdd015b42 | -6.39001 | -41.60588 | 2024-10-15 04:02:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 1e5d80c3-d592-3e9e-a0c8-0667387e10eb | -6.38942 | -41.60954 | 2024-10-15 04:02:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 7871dd8f-425e-33a4-a1bc-c7f4582e98a0 | -6.38883 | -41.61319 | 2024-10-15 04:02:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 31e5baf4-8a18-37df-8153-38f8ab0ba375 | -6.38604 | -41.60898 | 2024-10-15 04:02:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f0b321c9-64a7-35c7-994a-2ed0640228f0 | -6.37264 | -41.58442 | 2024-10-15 04:02:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cb6d3709-b020-30a6-80fd-b535b8a196be | -6.37205 | -41.58806 | 2024-10-15 04:02:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7691dccc-4240-35ed-8679-547e845fa0bb | -6.37088 | -41.59534 | 2024-10-15 04:02:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| df38f1b5-8b78-33d1-89c4-38f4443f2275 | -6.36808 | -41.59118 | 2024-10-15 04:02:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bef6200e-9ff9-3b25-85e3-3e566813d1fa | -5.66064 | -41.24841 | 2024-10-15 04:02:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9a855abd-b7b7-36a2-b660-5998a8625cd6 | -5.66006 | -41.25202 | 2024-10-15 04:02:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 318c023a-df98-332b-840d-bfda4efb9406 | -5.12723 | -41.67975 | 2024-10-15 04:02:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 61da80a0-6382-33cc-92c5-b8d838298067 | -5.1244 | -41.67546 | 2024-10-15 04:02:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 027b379f-0fdb-3118-898b-616821b847ac | -5.12381 | -41.67918 | 2024-10-15 04:02:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 46289101-e4c0-3d99-af18-1a6cc65e7208 | -5.12098 | -41.6749 | 2024-10-15 04:02:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 63587093-13d7-345e-a2ff-c63bb4016177 | -5.11755 | -41.67435 | 2024-10-15 04:02:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f34f1007-b0d0-35a1-9b15-f9ae528f0dd2 | -7.08596 | -41.4065 | 2024-10-15 04:02:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cb2cae01-ba6d-373a-bf2a-742c6cb62770 | -7.04961 | -42.09328 | 2024-10-15 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c92cb47b-aeb5-390a-9016-1be383d939c2 | -7.04619 | -42.09272 | 2024-10-15 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 376ec473-851c-3e58-a30f-85402fca314a | -6.99136 | -41.99627 | 2024-10-15 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7f5d7934-0981-3dc5-b7cf-fb31000e04d9 | -6.87561 | -41.25191 | 2024-10-15 04:02:00 | NOAA-21 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8b6f9dd3-8cde-304f-8372-071181ba14ba | -7.99303 | -40.9694 | 2024-10-15 04:02:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 15d859dc-973c-3e23-b50c-278cd6a069a0 | -7.55311 | -42.23879 | 2024-10-15 04:02:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2f62ef25-fac2-3059-a014-52218caab43b | -7.3805 | -42.04662 | 2024-10-15 04:02:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ad827aa5-e841-3c06-a22b-603db71c9024 | -8.22833 | -41.67039 | 2024-10-15 04:02:00 | NOAA-21 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ac527005-6cf9-314e-babf-0702d4110562 | -8.13721 | -42.34333 | 2024-10-15 04:02:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6ef32a2f-98d6-3859-a0bf-f5ed387dca42 | -8.1366 | -42.3471 | 2024-10-15 04:02:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 91cfd864-c9b9-3c82-b697-d3f98e43b779 | -8.1344 | -42.33898 | 2024-10-15 04:02:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a6a4f996-f1cf-3043-8829-cffa1a5b905f | -8.13318 | -42.34652 | 2024-10-15 04:02:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 736a2f55-572d-3c49-94e4-8cbfb68de426 | -8.11155 | -42.04269 | 2024-10-15 04:02:00 | NOAA-21 | NOVA SANTA RITA | PIAUÍ | Brasil | 2207959 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 824c37d7-b46b-38db-9b64-99693b92089c | -9.49395 | -42.01564 | 2024-10-15 04:02:00 | NOAA-21 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 16f2d5ba-765d-340d-b594-2c8bd3d175d2 | -10.48693 | -42.44219 | 2024-10-15 04:02:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 20.9 |
| b7f04b15-297b-3c4e-9a8f-8351981d9c0b | -10.48356 | -42.44165 | 2024-10-15 04:02:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 20.9 |
| dc6e66f7-1c23-3a7b-b370-563000357517 | -10.48296 | -42.4453 | 2024-10-15 04:02:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| dd26934b-f144-3bed-a699-c636a5408706 | -10.48018 | -42.4411 | 2024-10-15 04:02:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 677c4d0b-fd1f-3d19-9776-7b1c2f1b6981 | -5.02763 | -42.42303 | 2024-10-15 04:02:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e2843074-fa82-3d17-855e-070099ec8c62 | -4.96976 | -41.80865 | 2024-10-15 04:02:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| eae9d8eb-5f88-3539-88b2-bb79ac15a08c | -4.09735 | -42.29457 | 2024-10-15 04:02:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 766ee8ef-00af-386b-84da-aaa74eefdb45 | -4.0967 | -42.2986 | 2024-10-15 04:02:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 69c58149-4f65-3a88-a4c9-24cb144ef43e | -4.09509 | -42.28598 | 2024-10-15 04:02:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cec7741c-6b3e-3f9b-9d00-4967ccd8f9da | -4.0249 | -42.13609 | 2024-10-15 04:02:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c516a7bf-8b56-3fc2-9b42-e55fa5ada8e9 | -3.92588 | -42.40998 | 2024-10-15 04:02:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 82.5 |
| 4ca32200-0269-3a4b-bd82-7a1d959b0501 | -3.92521 | -42.41407 | 2024-10-15 04:02:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 96.0 |
| 95cb73cb-fd11-344a-aa00-0b64489f7ae7 | -3.92412 | -42.40595 | 2024-10-15 04:02:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 8b16797d-fd0f-3fa6-845e-2a484e8e72a1 | -3.92347 | -42.41005 | 2024-10-15 04:02:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| e257aeb4-3387-3b9f-ab72-f3e90959095c | -3.92297 | -42.40533 | 2024-10-15 04:02:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 82.5 |
| 8817466b-b39b-3373-bac8-52216195d675 | -3.92283 | -42.41415 | 2024-10-15 04:02:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 80.2 |
| 67860633-de79-3a6e-9348-261e2460182d | -3.92218 | -42.41824 | 2024-10-15 04:02:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 80.2 |
| 3873d07b-200a-3ddc-af36-8e5208da504e | -3.92096 | -42.4176 | 2024-10-15 04:02:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 96.0 |
| af82a5d9-6243-3ea4-9578-16edefbcbc4f | -3.91989 | -42.40949 | 2024-10-15 04:02:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 223.6 |
| ee8e3925-3715-3855-a7c6-69ddd3bb0978 | -3.91925 | -42.41358 | 2024-10-15 04:02:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| e6ded922-cadc-3c78-a31c-de18e4b4d53a | -6.5744 | -42.09877 | 2024-10-15 04:02:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e3c89737-b536-38a5-a1b0-653eef0d924a | -6.36909 | -42.67883 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 62eab2f8-5c3b-3a9f-969b-b2a4f07478ec | -6.36845 | -42.68285 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ba32f3fe-addf-3ec0-a4db-31a88cfcdd9f | -6.33447 | -42.66894 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c7ffac3f-9c9c-3ba4-9426-f70a605bce12 | -6.29879 | -42.57761 | 2024-10-15 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 2213d048-6b91-3f6a-afa4-628b954f9622 | -6.2872 | -42.6041 | 2024-10-15 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| d5aa2208-5b75-319f-b297-adbfea468744 | -6.28648 | -42.60482 | 2024-10-15 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| e033e2d4-5b4d-3bb1-a139-da7f6326845c | -6.27979 | -42.62409 | 2024-10-15 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| eef6e525-e57f-323d-8099-9b6347a80c54 | -6.27753 | -42.61557 | 2024-10-15 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 9ca9bc4a-2650-3999-9f5f-b0c80f4bc842 | -6.18626 | -42.93296 | 2024-10-15 04:02:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f0a4b0aa-7189-3b03-9e47-2082207c4735 | -6.07055 | -42.41387 | 2024-10-15 04:02:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b2a2ea78-4376-3226-8085-db54ab03d569 | -6.06705 | -42.41331 | 2024-10-15 04:02:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README25.md)
