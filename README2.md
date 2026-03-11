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
| 195cc449-be7d-38de-b13e-0b9674a61191 | -7.80163 | -41.85587 | 2026-03-11 04:02:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.1 |
| 6e794065-8adf-3c7c-a8ec-1f01fe15e5d3 | -8.195 | -36.03882 | 2026-03-11 04:02:00 | NOAA-21 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d97840ef-74ee-3753-b1f5-9dea6eb47eb2 | -6.38039 | -38.17497 | 2026-03-11 04:02:00 | NOAA-21 | TENENTE ANANIAS | RIO GRANDE DO NORTE | Brasil | 2414100 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1b83c7ed-bb5c-35fa-96f6-0667ebccf15e | -8.58548 | -40.21894 | 2026-03-11 04:02:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.1 |
| 5ab99fbd-a9d9-394e-bc35-e37bfcb4d1ac | -9.15782 | -40.08192 | 2026-03-11 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 560dbbc8-f3a9-3d60-8a5a-6d82b82c56ab | -9.08567 | -42.36649 | 2026-03-11 04:02:00 | NOAA-21 | SÃO LOURENÇO DO PIAUÍ | PIAUÍ | Brasil | 2210359 | 22 | 33 | nan | nan | nan | Caatinga | 0.1 |
| 50bf9d5f-66a2-3aba-bf0d-b61080ea96fd | -7.32677 | -45.78699 | 2026-03-11 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0095afb2-f04c-3af9-8033-9e72798c1f79 | -13.36554 | -51.38192 | 2026-03-11 04:04:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3885e6ab-b560-3754-831b-1575067e3fda | -11.55851 | -38.25814 | 2026-03-11 04:04:00 | NOAA-21 | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 34e94c14-16c7-3d4f-a4a0-ca4f7ad9922d | -15.13349 | -41.30288 | 2026-03-11 04:04:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| e551903e-f1a5-373c-b4c1-365d0c56a460 | -14.43962 | -48.44566 | 2026-03-11 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 6679adcb-233b-3b8b-8b43-f7ce4373ee8d | -16.10961 | -42.6513 | 2026-03-11 04:04:00 | NOAA-21 | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| b0aa86e2-a95a-3945-9b38-99ff39f8a6b7 | -12.83057 | -52.12052 | 2026-03-11 04:04:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25c39ef5-12be-3a29-9d75-b818c47889da | -12.31583 | -42.5365 | 2026-03-11 04:04:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 72ea1fe6-f978-3a3b-993d-6231c20a5c88 | -16.42922 | -42.63177 | 2026-03-11 04:04:00 | NOAA-21 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| eae29eae-0dc8-3ab9-9ef6-3d6e68c332ef | -12.6608 | -45.60379 | 2026-03-11 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7f984693-36a6-368f-8891-f3151bcf76d5 | -14.69793 | -49.73531 | 2026-03-11 04:04:00 | NOAA-21 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 0.1 |
| af5807ba-ab4b-3f54-82dd-06e814b224ee | -15.62054 | -40.73741 | 2026-03-11 04:04:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 05b2f898-b1e2-3c4a-ba01-6c004defaf99 | -16.12576 | -40.35754 | 2026-03-11 04:04:00 | NOAA-21 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e1760fc6-e001-36af-9179-1a6c62404672 | -13.30664 | -43.87957 | 2026-03-11 04:04:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 167dc60a-e609-3266-bcc6-4a06fb5fc4cc | -14.45545 | -53.54563 | 2026-03-11 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 14a4c2c1-31ba-35fc-ad1a-f1a948b4e582 | -12.0281 | -45.34462 | 2026-03-11 04:04:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| db9e0fad-5f2e-3ef7-bb1c-1e5bf8254cdb | -13.61416 | -51.76962 | 2026-03-11 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 8d218348-9c1a-36f3-a07a-c60937b1b14c | -16.49884 | -39.51435 | 2026-03-11 04:04:00 | NOAA-21 | ITABELA | BAHIA | Brasil | 2914653 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c8fdef11-13f1-3bc6-b324-3200a339895d | -15.1432 | -41.83145 | 2026-03-11 04:04:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8f2df6c2-ec20-3c90-b6dd-b6b016ac2512 | -10.02274 | -39.63234 | 2026-03-11 04:04:00 | NOAA-21 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 0.1 |
| e8e45e7d-5503-3796-aacc-26252b376804 | -8.62714 | -50.7425 | 2026-03-11 04:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.1 |
| c9f6ca17-59ea-30d7-83a8-f1444e0908b1 | -14.40048 | -54.01622 | 2026-03-11 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 80bce0a3-3e42-3565-a96f-e80592513f50 | -13.55001 | -40.94474 | 2026-03-11 04:04:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 604d4e50-c173-3c74-8e15-ed728545da9f | -15.24723 | -41.84111 | 2026-03-11 04:04:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 2d87d8ed-9fe5-3299-b223-0f35adb967f8 | -12.54197 | -47.06849 | 2026-03-11 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| e30d0776-b2a4-391f-92b5-96f4fd278901 | -17.11759 | -39.50881 | 2026-03-11 04:04:00 | NOAA-21 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 81d23a48-48e4-3b62-b5a1-6e9bd43c49bd | -9.47183 | -53.33595 | 2026-03-11 04:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 55635e3e-8212-30bd-8270-6c44ae1a739e | -13.3807 | -51.33277 | 2026-03-11 04:04:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 748a222c-6e00-3169-8cf4-738704f5eb5b | -13.28504 | -55.55598 | 2026-03-11 04:04:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 72fd1f84-7351-3dcb-bdd4-f8fd22308f6c | -12.79203 | -44.8328 | 2026-03-11 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e03641fd-522f-3a80-b5aa-27add188c7a1 | -15.1465 | -41.83199 | 2026-03-11 04:04:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bd9f3712-8cc3-3191-a5ea-a39d23272861 | -16.78399 | -39.44037 | 2026-03-11 04:04:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fdce56ef-8c4f-310f-b4c9-65733e048147 | -15.61668 | -43.839 | 2026-03-11 04:04:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 0.1 |
| f2c8dade-4978-38c2-bb8e-8cae848ea497 | -11.55374 | -38.26578 | 2026-03-11 04:04:00 | NOAA-21 | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d2f0ee8f-b808-3bdd-b60f-bbd37e44117f | -9.83638 | -51.08298 | 2026-03-11 04:04:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 98b97211-7f57-3d18-b6e0-7e7b10730f37 | -12.68417 | -55.57417 | 2026-03-11 04:04:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 21051bde-3e27-39c6-b8b4-68bf38de8610 | -11.97614 | -45.66891 | 2026-03-11 04:04:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| bbf17a11-856b-365f-9b6d-aabbd99f11fe | -10.41746 | -40.2928 | 2026-03-11 04:04:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 34eaa1df-acf1-3b36-9d15-be1e7f3f5cf1 | -13.13859 | -53.04642 | 2026-03-11 04:04:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 7776bf20-d0d9-31b0-942d-d38ed8dfcd68 | -15.82464 | -43.21726 | 2026-03-11 04:04:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7163f709-bda0-32f0-ae72-683639e0dbf1 | -11.28828 | -39.91341 | 2026-03-11 04:04:00 | NOAA-21 | CAPIM GROSSO | BAHIA | Brasil | 2906873 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6183adca-9aec-327c-ae99-c65e494dbbae | -16.22819 | -44.34763 | 2026-03-11 04:04:00 | NOAA-21 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 0.1 |
| f9ef44b3-d700-3499-a585-75dc2f477c91 | -15.32735 | -41.10196 | 2026-03-11 04:04:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 42a2c622-3ada-3e3d-b37e-caa0ee6b82c5 | -19.0338 | -48.48945 | 2026-03-11 04:06:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.1 |
| a1647e0f-a31a-3e0f-9ea1-9e3589254cfc | -20.52719 | -48.90493 | 2026-03-11 04:06:00 | NOAA-21 | GUARACI | SÃO PAULO | Brasil | 3517901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c21c9083-b5b5-350c-986b-4f6252728cb1 | -22.9241 | -45.56288 | 2026-03-11 04:06:00 | NOAA-21 | TREMEMBÉ | SÃO PAULO | Brasil | 3554805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 7a1b5339-f0b2-37e8-bdb8-534522647728 | -17.95137 | -47.31327 | 2026-03-11 04:06:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1479a741-8d3d-33a7-9726-bd2e26608f74 | -19.23151 | -47.51466 | 2026-03-11 04:06:00 | NOAA-21 | PEDRINÓPOLIS | MINAS GERAIS | Brasil | 3149200 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 607b353b-972d-3c5c-9a5f-6189e64eb9af | -15.33924 | -52.93286 | 2026-03-11 04:06:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36a67b80-9a87-39ee-92d6-6f32ad4d5389 | -18.15198 | -45.63074 | 2026-03-11 04:06:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| f80403f2-8458-319b-b051-3ea491098a82 | -19.01316 | -40.84171 | 2026-03-11 04:06:00 | NOAA-21 | ÁGUIA BRANCA | ESPÍRITO SANTO | Brasil | 3200136 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| a52546f7-9304-3bf0-8bcd-360f5977fa6d | -16.65757 | -50.30259 | 2026-03-11 04:06:00 | NOAA-21 | FIRMINÓPOLIS | GOIÁS | Brasil | 5207808 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8c709b43-5077-3543-a989-bc14c79f1bfd | -17.57692 | -40.1567 | 2026-03-11 04:06:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| a08a317a-b37a-3432-8711-0d3de8f1dde6 | -19.38929 | -48.41007 | 2026-03-11 04:06:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b8178cb-cd1a-3882-8d96-32aacdd0f027 | -20.77451 | -42.90023 | 2026-03-11 04:06:00 | NOAA-21 | VIÇOSA | MINAS GERAIS | Brasil | 3171303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 4a5d364d-d47b-3452-9dc6-9fe188a522d5 | -16.09889 | -55.81651 | 2026-03-11 04:06:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a757b702-9d9b-3bfb-b97a-cbf8a4350184 | -16.66074 | -46.2977 | 2026-03-11 04:06:00 | NOAA-21 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 69000ca7-4965-39f7-b485-6fb5c94d7a80 | -18.67797 | -52.65017 | 2026-03-11 04:06:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e9285f39-c53c-33cb-97f8-5a3d781f0a0d | -19.94902 | -44.71498 | 2026-03-11 04:06:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| db39b5ae-827c-307a-81f8-1fd5752e5661 | -20.04445 | -41.33387 | 2026-03-11 04:06:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 0031056e-c146-3cab-b19a-b19c651fcda6 | -17.42341 | -41.86162 | 2026-03-11 04:06:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 03eafb30-e934-3060-8248-a12b86f7c145 | -17.09774 | -46.46954 | 2026-03-11 04:06:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b51fb2cf-0f42-3a61-9e94-d9a2d00e7784 | -15.72976 | -56.6021 | 2026-03-11 04:06:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cfe27a39-e57d-3bcd-afbe-d79d33552b28 | -17.87203 | -46.00249 | 2026-03-11 04:06:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 325ff426-f4cf-3af8-b858-da877bfaaad2 | -17.02383 | -45.3602 | 2026-03-11 04:06:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91fc94cb-77a2-3411-a05b-4a8a48177ddc | -20.1389 | -52.19312 | 2026-03-11 04:06:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| db0a785b-a00f-3569-95cd-68b7102d6f9d | -17.26495 | -43.7827 | 2026-03-11 04:06:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.1 |
| dda97146-c625-36e7-8d92-19a68c7e872f | -18.60468 | -46.98551 | 2026-03-11 04:06:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| bd2cccad-e650-3596-bbdc-6ff6d680119b | -17.101 | -46.4509 | 2026-03-11 04:06:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 500aab31-8274-3dd4-8777-31ef1d6de78b | -20.4217 | -41.19291 | 2026-03-11 04:06:00 | NOAA-21 | VENDA NOVA DO IMIGRANTE | ESPÍRITO SANTO | Brasil | 3205069 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 43fa1822-20b8-3122-bc9b-a3b66d009dfe | -18.88504 | -40.08436 | 2026-03-11 04:06:00 | NOAA-21 | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 1a70a0ba-9e78-3a37-866f-5ca21b16a8e5 | -20.4822 | -41.82792 | 2026-03-11 04:06:00 | NOAA-21 | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.0 |
| cbcb3c67-ebf4-39e9-ae5e-ccb8b51443d9 | -19.02642 | -41.77346 | 2026-03-11 04:06:00 | NOAA-21 | CAPITÃO ANDRADE | MINAS GERAIS | Brasil | 3112653 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 636c6e06-9555-3af7-825d-159e6069a7eb | -19.74065 | -52.00719 | 2026-03-11 04:06:00 | NOAA-21 | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 0.1 |
| d4fd85fd-0260-33a9-a301-eb2cdab9a090 | -20.19146 | -44.36612 | 2026-03-11 04:06:00 | NOAA-21 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| f43bee2c-fc01-382a-a413-79570268e5e0 | -21.92358 | -51.85321 | 2026-03-11 04:08:00 | NOAA-21 | PRESIDENTE VENCESLAU | SÃO PAULO | Brasil | 3541505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1a8365fd-6b90-3697-a230-47b1f50b8294 | -26.26179 | -50.04201 | 2026-03-11 04:08:00 | NOAA-21 | MAFRA | SANTA CATARINA | Brasil | 4210100 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| da4d4956-b7a6-3f4c-abfb-e16d25eaf124 | -23.21059 | -52.3817 | 2026-03-11 04:08:00 | NOAA-21 | NOVA ESPERANÇA | PARANÁ | Brasil | 4116901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 46871423-471d-38fd-9c5d-414d218fed23 | -21.57493 | -53.2987 | 2026-03-11 04:08:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9cb88800-48d8-3f52-ad68-34b8d2c74e98 | -24.04655 | -46.92039 | 2026-03-11 04:08:00 | NOAA-21 | ITANHAÉM | SÃO PAULO | Brasil | 3522109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 838d07d9-be90-3221-8b22-c6ce64ea6c29 | -22.49113 | -49.28181 | 2026-03-11 04:08:00 | NOAA-21 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a9d3d8ad-cad5-3e90-bb37-92615523b3e1 | -23.8294 | -53.97431 | 2026-03-11 04:08:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 4811de7a-520d-38c0-9160-6cfe9c942f05 | -24.92033 | -53.5215 | 2026-03-11 04:08:00 | NOAA-21 | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 4b74f637-67c0-3a62-b0bf-a95dac6abc2f | -24.65775 | -51.22101 | 2026-03-11 04:08:00 | NOAA-21 | CÂNDIDO DE ABREU | PARANÁ | Brasil | 4104402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ad90b1fc-a5c5-3138-87a8-50e67197c968 | -25.21949 | -53.61017 | 2026-03-11 04:08:00 | NOAA-21 | LINDOESTE | PARANÁ | Brasil | 4113452 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| a5882b84-dd01-369e-9b35-43febb3626da | -24.92426 | -50.34561 | 2026-03-11 04:08:00 | NOAA-21 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1a96aa02-f1e7-32c8-8422-e470f0681add | -28.97616 | -52.43567 | 2026-03-11 04:08:00 | NOAA-21 | FONTOURA XAVIER | RIO GRANDE DO SUL | Brasil | 4308300 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| bb80bbd1-a260-33a0-a73f-c67c80aa285c | -27.20332 | -50.48591 | 2026-03-11 04:08:00 | NOAA-21 | PONTE ALTA DO NORTE | SANTA CATARINA | Brasil | 4213351 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| c4a15f23-2d38-33b8-a34f-357067bbf9cd | -23.32143 | -55.00033 | 2026-03-11 04:08:00 | NOAA-21 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 49a1f392-ea12-3677-8321-0c9191f23a4d | -27.69864 | -49.61201 | 2026-03-11 04:08:00 | NOAA-21 | BOM RETIRO | SANTA CATARINA | Brasil | 4202602 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 6cdd4566-c075-3d6a-b320-172875484610 | -27.58379 | -50.28117 | 2026-03-11 04:08:00 | NOAA-21 | CORREIA PINTO | SANTA CATARINA | Brasil | 4204558 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| fe8219f2-c992-3edf-9cc8-5a43400a81de | -25.69591 | -50.2197 | 2026-03-11 04:08:00 | NOAA-21 | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.0 |
| 6f6b5f28-4e1b-34ee-ba41-15b39a0c6409 | -25.97092 | -50.36621 | 2026-03-11 04:08:00 | NOAA-21 | SÃO MATEUS DO SUL | PARANÁ | Brasil | 4125605 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.0 |
| e5afc091-e5fb-317e-944e-f4e157a1ee9c | -23.23101 | -55.17592 | 2026-03-11 04:08:00 | NOAA-21 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |


[Clique aqui para ver as próximas entradas](README3.md)
