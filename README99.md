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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07b3323a-f847-3e55-b415-5105f798b523 | -3.67043 | -54.53668 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| d33303cb-c1ee-3ebc-b963-875681509f8f | -6.07224 | -53.87687 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a7516632-415f-34c9-b41e-cf9ee419d0a6 | -2.49289 | -50.48108 | 2026-10-05 16:39:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d1d8d620-2e4d-379b-ba6e-7892c5f6ebf2 | -3.97068 | -53.46468 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 643a2f57-2605-3ed3-a267-7e43e94dc186 | -7.21883 | -55.18165 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f5f33ccb-fa36-34b9-8736-a1f401de27de | -3.85841 | -38.52337 | 2026-10-05 16:39:00 | NOAA-21 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0fa6b871-9027-3db7-ae5b-37eb1ccbe1de | -5.94975 | -41.34671 | 2026-10-05 16:39:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 54.1 |
| 99afe788-1122-3c78-a214-ba80f73e59a6 | -1.77367 | -53.78027 | 2026-10-05 16:39:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1f07aadd-3fc0-3385-b20a-e91320efdb83 | -5.97262 | -41.32138 | 2026-10-05 16:39:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| aec34064-e599-3c46-83b2-4e019fbf5b10 | -3.35948 | -59.89354 | 2026-10-05 16:39:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| f188a667-f0f1-3798-9491-d46fa70f2b55 | -6.03678 | -45.23478 | 2026-10-05 16:39:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1472fe9d-eb51-35fb-9eaf-6067f84cc281 | -4.08312 | -40.85683 | 2026-10-05 16:39:00 | NOAA-21 | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| dd52127c-e15c-3959-b965-ee04f0df98f1 | -3.81962 | -41.7986 | 2026-10-05 16:39:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 37.0 |
| aa7144e9-f2a8-3ae0-941f-c456a54f05a3 | -2.43874 | -58.01445 | 2026-10-05 16:39:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2cb67f82-c14d-3afd-b927-60952d6c2707 | -3.74682 | -39.54573 | 2026-10-05 16:39:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 99d78ce7-0151-3728-82a6-92a42e561439 | -1.61476 | -55.92253 | 2026-10-05 16:39:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| db4e1167-1922-34ff-8c78-939f202cea9b | -4.33384 | -43.82131 | 2026-10-05 16:39:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9e509c91-7fdb-38d0-9b03-62c115699bea | -3.12919 | -53.71539 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| bcee193a-f085-34f3-ba51-1aa5e7026fe5 | -1.72911 | -45.64124 | 2026-10-05 16:39:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bd9f318e-5068-3436-a963-5881fafedfe4 | -3.11685 | -44.29131 | 2026-10-05 16:39:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 584e8855-154d-39c0-9963-d2dc0d547bec | -5.47392 | -41.22972 | 2026-10-05 16:39:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 2ead5a09-dbde-3bb1-acf9-e51be7a51962 | -3.38011 | -42.83638 | 2026-10-05 16:39:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 981bdc92-ef20-3777-bbee-9dca2d7d59a8 | -5.12395 | -43.99819 | 2026-10-05 16:39:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| a5318ffa-6a70-32cc-9c1a-869c75f0ffa4 | -3.28848 | -42.25948 | 2026-10-05 16:39:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| dedf005d-1eb8-3a7d-822b-98665fe22cd2 | -5.24265 | -39.15504 | 2026-10-05 16:39:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 284fe1a5-f032-3050-b211-574d0950c347 | -6.38075 | -45.79839 | 2026-10-05 16:39:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5b172cd8-3362-35bc-a34f-43936b6e9e1a | -5.95293 | -41.31138 | 2026-10-05 16:39:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 21.1 |
| a6623795-f922-36be-ad93-b38586983f44 | -3.22235 | -57.89309 | 2026-10-05 16:39:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 10f19cb9-6c65-3101-b68d-7b484e024ad9 | -4.90744 | -41.73782 | 2026-10-05 16:39:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 6e10ad80-dd6c-3b6f-bd72-e0e04769e07a | -4.62271 | -38.93974 | 2026-10-05 16:39:00 | NOAA-21 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| aab1a363-d98c-32c6-8da0-27377709da59 | -3.27926 | -54.17989 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| cfa38edc-47f8-35ec-a3bc-954130e7e3e9 | -2.75823 | -45.5467 | 2026-10-05 16:39:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e6566361-2e82-3e0c-a37a-bcf9f7cddd33 | -3.28352 | -42.25603 | 2026-10-05 16:39:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 02ad9edf-84ae-3725-9f47-b738b4ce4b87 | -2.82608 | -43.68169 | 2026-10-05 16:39:00 | NOAA-21 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 05dd5d67-6ec0-3dc4-b714-d0461cd6ac6c | -4.34844 | -43.83155 | 2026-10-05 16:39:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 1cf162c9-64bf-3cbf-9053-5d7629b4de82 | -3.40887 | -58.45806 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 41.0 |
| b9ed016c-b96a-3670-a6bd-218b3667dc5c | -2.92875 | -54.12346 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| b4335d8e-4656-39e1-9663-e93f837c5b08 | -3.75163 | -61.01255 | 2026-10-05 16:39:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 50b46a3e-9dac-3bec-a579-c61a163f3962 | -3.37478 | -58.19336 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 239b599f-b30d-3393-b85f-49063a2dedb9 | -5.84659 | -45.01551 | 2026-10-05 16:39:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 46394c4b-5915-3574-8b18-4601b7c562bd | -2.77742 | -57.66685 | 2026-10-05 16:39:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 85fc5cc3-525c-3143-92a6-65d2946c67d1 | -3.22795 | -53.86676 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| f60cf060-5f1c-3b73-a071-b30d5bc779f6 | -4.33308 | -43.8166 | 2026-10-05 16:39:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ea706115-a39e-38d7-b5c6-f84884703e3c | -3.41089 | -58.46061 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| a668c5fe-690b-3433-9771-aa4c32f405f3 | -5.50479 | -42.8081 | 2026-10-05 16:39:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 3fc0dcda-95c4-3f97-9dd1-63eace65d45f | -2.77102 | -57.66076 | 2026-10-05 16:39:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 20.2 |
| cbc86ebc-e439-32ca-aad3-5f0693555bbc | -3.61943 | -44.42803 | 2026-10-05 16:39:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e2f99c3a-a225-3294-8f02-545e705e0b56 | -0.39826 | -52.00314 | 2026-10-05 16:39:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 44db20b5-3060-33e7-a44c-ee3bfd3d179c | -4.11761 | -54.42421 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 3075aa35-dd44-3d57-8e6e-dc80b387e9e9 | -3.10894 | -53.71144 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| a1c4da4f-cda8-34db-934b-c0760c60557d | -2.04275 | -54.30437 | 2026-10-05 16:39:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| ce48e6fc-6f58-3038-b593-5fd45d6ff8e8 | -3.74119 | -39.54357 | 2026-10-05 16:39:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 159455c2-4b89-3e16-8fd7-04af81770ded | -3.53132 | -59.3988 | 2026-10-05 16:39:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1687fe67-72f0-3ecf-8ac6-76f2356cc79f | -2.84371 | -54.07595 | 2026-10-05 16:39:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5cbd1c99-142d-38c3-a86d-4c941d920ca9 | -2.57586 | -57.79335 | 2026-10-05 16:39:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8067bac3-43b6-35b8-8cf5-9076e3cdb156 | -5.95485 | -41.35031 | 2026-10-05 16:39:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 54.1 |
| 585ce473-0519-39fc-817b-4d5c05d36f3d | -3.76451 | -39.84706 | 2026-10-05 16:39:00 | NOAA-21 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 81ea321e-6e60-3272-819a-c3489af73928 | -5.30483 | -43.21007 | 2026-10-05 16:39:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 1070f317-fc0d-3c6e-935a-ec4fc30d7d47 | -1.8517 | -50.6226 | 2026-10-05 16:39:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d121e233-40fb-3f23-87c4-a6e020d28773 | -2.88533 | -42.36687 | 2026-10-05 16:39:00 | NOAA-21 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 2a150dac-8b7f-398e-88cf-b4e30779a614 | -2.36453 | -44.6414 | 2026-10-05 16:39:00 | NOAA-21 | ALCÂNTARA | MARANHÃO | Brasil | 2100204 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2849b225-adef-3b82-8335-871066787c98 | -3.91255 | -44.14586 | 2026-10-05 16:39:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 416fa472-c131-3480-90b5-0496aef92232 | -5.89514 | -43.3088 | 2026-10-05 16:39:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| f7fdc886-c1f9-3d99-9288-7e94492e6f05 | -7.23113 | -55.1884 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 86433c07-d9de-3c65-bef9-ac8993b7279b | -3.11195 | -53.70345 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| b279ca76-32c8-3cd3-b714-2ff57a2ec73b | -2.95778 | -54.14368 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 80d00d21-c679-3474-a84b-ec9ec6262cb1 | -5.89737 | -53.63729 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d5b18bd0-71e5-3521-b85f-4a8b34e4ab1a | -3.93747 | -40.72895 | 2026-10-05 16:39:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 3549fb12-17d9-3cd4-94f7-295e8d59ae03 | -5.95188 | -41.35954 | 2026-10-05 16:39:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 204.7 |
| 59e7843d-12f9-30cc-87b0-afa24cab1d6b | -6.0701 | -53.83811 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ae0f3d92-e0f3-3657-b75b-b7de4a4f1d49 | -3.98481 | -55.81686 | 2026-10-05 16:39:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 1adbdf8d-9aa7-3227-8ddf-c3f37bc68c57 | -4.88582 | -42.75407 | 2026-10-05 16:39:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 92ef235e-0730-3c7b-90a4-894a7382ff7c | -2.89329 | -43.02634 | 2026-10-05 16:39:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 08252f9e-8fb9-3760-b0f7-6528f3fd5600 | -6.38415 | -45.79787 | 2026-10-05 16:39:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 79bde7b5-dfcb-3ed3-988a-ac52b36dc2e5 | -4.84821 | -40.25706 | 2026-10-05 16:39:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 572e983e-2693-303a-adef-834c17086605 | -2.80795 | -49.87245 | 2026-10-05 16:39:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fe060822-a614-31b8-bdcb-6f85a9c06393 | -2.07714 | -56.8373 | 2026-10-05 16:39:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 49d9c27f-27fc-336d-8d01-9ca98e5f307c | -3.36525 | -59.41777 | 2026-10-05 16:39:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| fa77261d-83c7-35a6-8f36-52abc9311581 | -1.46505 | -54.78396 | 2026-10-05 16:39:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| f0582be2-a50d-3da5-b1de-2dc7ad1ffe03 | -5.98245 | -46.48228 | 2026-10-05 16:39:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 36e02861-4254-38bc-b0b4-0cb98e9d2eb1 | -5.74196 | -41.6169 | 2026-10-05 16:39:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 33.3 |
| 04b6d7ed-58ac-3730-9d6a-16fdce4c090a | -3.50602 | -54.61197 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| e1217c0c-db89-36b0-a31b-cb12ac772278 | -3.55441 | -54.48333 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| daa2099f-f3f6-3186-8eec-56a9e03dbde0 | -7.22997 | -55.1908 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| eada1dd2-7f3c-31a1-96f9-bf339024a2e9 | -3.64148 | -58.62018 | 2026-10-05 16:39:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 24.1 |
| f0ea85c7-7b7b-3f3a-984a-55301dc262f3 | -3.89416 | -39.19166 | 2026-10-05 16:39:00 | NOAA-21 | PENTECOSTE | CEARÁ | Brasil | 2310704 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| b1e7d8cb-5f09-3570-8edc-9c05e3edfdf8 | -8.5554 | -66.9945 | 2026-10-05 16:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 32eb3d9f-8d07-343a-b3af-8e9e5fd5a287 | -9.1221 | -64.4031 | 2026-10-05 16:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.0 |
| c9276c12-0a34-3260-a6f5-576000b931a3 | -9.1408 | -64.3836 | 2026-10-05 16:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.1 |
| c0425510-bada-3a69-9933-f311432b0e27 | -9.4819 | -66.7836 | 2026-10-05 16:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| de39504b-c132-30e4-8a46-2809dfd6f717 | -9.1037 | -64.385 | 2026-10-05 16:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 85.2 |
| d21ce34e-6c9d-3306-9251-3201f3ec96a9 | 1.9133 | -55.7813 | 2026-10-05 16:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| a29c72d7-4c44-34a5-ad9f-0dc8d3d1a88c | -8.5918 | -67.1418 | 2026-10-05 16:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| ae6df636-fcdc-3b9f-bd7b-c29e9fb68ecc | 2.15204 | -55.97435 | 2026-10-05 16:41:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 68d2d041-6a65-34a1-894b-4b01a433713e | 1.81376 | -55.55098 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 5ff89d6f-4cfc-3fe3-8bb1-4ea7e80f08bf | 2.14458 | -55.9643 | 2026-10-05 16:41:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 19b60634-6190-3360-9d5d-24d4f148f309 | 3.57789 | -61.36115 | 2026-10-05 16:41:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 11.0 |
| a4049c4c-b2e7-3e6b-83ee-66d9b59c272a | 3.53771 | -51.5106 | 2026-10-05 16:41:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 2478372f-88c9-3e89-be11-0f342392c37d | 3.31324 | -51.33139 | 2026-10-05 16:41:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 11.6 |
| b1386261-9790-3051-9ae7-b78092e4896e | 3.56459 | -61.36415 | 2026-10-05 16:41:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 10.1 |


[Clique aqui para ver as próximas entradas](README100.md)
