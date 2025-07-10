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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a062ffe3-c51c-3e18-8abe-49e473337f62 | -8.50331 | -43.27804 | 2025-07-10 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 46.3 |
| c9be58c8-5067-305a-a9cf-f36f31c3924c | -9.29902 | -44.84298 | 2025-07-10 03:38:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 154b7893-f338-3f23-a55e-307fc4120045 | -12.99978 | -46.2892 | 2025-07-10 03:38:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3937993d-9228-32a0-b315-40e7b039ec5f | -12.99905 | -46.28288 | 2025-07-10 03:38:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c472aa75-13b1-3825-b74d-a2bd6a523031 | -10.62842 | -45.23671 | 2025-07-10 03:38:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eeb5d224-ef33-304d-b266-f48cdbfaf15b | -14.73325 | -41.72728 | 2025-07-10 03:38:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 146510b3-a2a8-31c2-8927-04cd0301ad00 | -11.90594 | -44.90816 | 2025-07-10 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 49b853a4-2bed-38ec-a9ee-ceb39683366a | -13.00957 | -46.3214 | 2025-07-10 03:38:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2987d706-d2dd-39f7-bcae-43aad75365be | -12.22365 | -44.21504 | 2025-07-10 03:38:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 479b5005-2f6e-319d-8d9b-3571844ccf99 | -13.1562 | -47.2799 | 2025-07-10 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67d39899-213b-3778-9bd8-b4149c210cb5 | -10.74891 | -40.83088 | 2025-07-10 03:38:00 | NOAA-21 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f55873ac-0a8e-3376-b4ba-70dc79e2f1de | -15.47351 | -45.19831 | 2025-07-10 03:38:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dbb26a9b-9587-30a6-aa12-95bb230be2ce | -8.88919 | -47.33959 | 2025-07-10 03:38:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5df6d2a0-9a0d-3852-bb55-2cf7aba96f1c | -11.36588 | -48.70623 | 2025-07-10 03:38:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 36d8c1ed-bb75-3e2a-8587-f85535e23520 | -13.67659 | -44.22292 | 2025-07-10 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 168bf1fd-45a2-3415-9c06-81309ce13f35 | -12.21969 | -44.2075 | 2025-07-10 03:38:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 010c9bb4-562e-35b3-ba18-c3b57cb74b38 | -13.87689 | -45.84479 | 2025-07-10 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d301d2af-1842-3caf-acc1-33f7e83b1021 | -11.36445 | -48.71312 | 2025-07-10 03:38:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7d65e2cf-cc01-3daa-9d75-a74541f93a8c | -12.10345 | -44.73759 | 2025-07-10 03:38:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46d48967-87cb-3ad8-a8e4-031bb2684345 | -13.03691 | -46.30744 | 2025-07-10 03:38:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1c2a6a37-3992-3931-b17f-c8680fcf829c | -13.38889 | -47.87745 | 2025-07-10 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ee52436-1b5f-3d1a-8c3d-d48cedb2f031 | -11.87936 | -40.95518 | 2025-07-10 03:38:00 | NOAA-21 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 14815fa6-728b-3b42-a0bf-2c76cc171ae2 | -13.03784 | -46.30286 | 2025-07-10 03:38:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 71a1afa6-474e-30aa-828c-90755459f964 | -13.1501 | -47.27802 | 2025-07-10 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c22022f7-b655-3880-bfef-edb9412278c9 | -13.89815 | -42.13394 | 2025-07-10 03:38:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 45317122-296f-3cc5-8035-f3814c0fad94 | -12.57452 | -48.8847 | 2025-07-10 03:38:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 399e4d53-2ec8-331e-826e-eabb659893c0 | -13.37107 | -47.89857 | 2025-07-10 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c732448c-d1af-3c00-b1da-c2efb50ee2a9 | -13.37227 | -43.76059 | 2025-07-10 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18342ea0-c228-39e3-b1b6-ff927a4182ac | -8.9951 | -47.45244 | 2025-07-10 03:38:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f0a496d-ab82-3d5d-b224-a5a0111fecf9 | -12.22429 | -44.21176 | 2025-07-10 03:38:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e727fcf-f5ab-39c6-9149-47af96911518 | -12.22492 | -44.20848 | 2025-07-10 03:38:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6e8e74a6-a1e5-35de-a40b-202a8f4546be | -10.89288 | -46.73321 | 2025-07-10 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 731ea347-4180-3fe2-b4de-c72c762a6ada | -13.29037 | -49.15797 | 2025-07-10 03:38:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 55665df5-9eee-391d-a0f7-83e23a6f2f25 | -9.83022 | -41.49811 | 2025-07-10 03:38:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| bcb7424d-b518-3579-9fa3-fac892cefdbe | -14.73252 | -41.73138 | 2025-07-10 03:38:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 521ab168-e808-3113-b91c-4fbfc1e97514 | -10.63493 | -45.23387 | 2025-07-10 03:38:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 67b8f3b4-17a1-39ca-ba1c-e31b3278a017 | -14.86246 | -45.12762 | 2025-07-10 03:38:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c124b096-7b60-30de-bd0c-9fce45e115d8 | -9.30476 | -44.84405 | 2025-07-10 03:38:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 19390777-dcb5-35a5-9cc5-89655ce31ee7 | -13.87122 | -45.84383 | 2025-07-10 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dea8f740-fc35-3420-b7e3-e096f47b9386 | -13.38051 | -47.88547 | 2025-07-10 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 44bad0dc-490c-39a5-bd26-c7bf3c459e3e | -11.95062 | -46.36282 | 2025-07-10 03:38:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e561b4bc-2d64-3ee6-bcba-bdd3a4f6abdd | -9.29329 | -44.84189 | 2025-07-10 03:38:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f8decee-cdb7-3d3e-84ec-a8719923fae1 | -11.06306 | -45.87212 | 2025-07-10 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 781d56bd-371d-3674-a92b-40acbc1175a1 | -12.09958 | -44.73691 | 2025-07-10 03:38:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e48f697e-778f-37b1-bb1b-26fcda45265f | -13.37215 | -47.89338 | 2025-07-10 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 15ed9d74-e52a-3150-ae68-d998fa624611 | -11.83148 | -48.2177 | 2025-07-10 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e562fc82-5b4b-3f17-aa71-18cddd5f5b88 | -9.09281 | -47.96909 | 2025-07-10 03:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 79ca2d70-2648-3364-902b-20221a186755 | -12.46896 | -46.91193 | 2025-07-10 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d5c91443-ed3d-309a-91b0-19fc76f64b18 | -13.00402 | -46.28852 | 2025-07-10 03:38:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 712d6cd0-0f45-33f9-8478-aa0ee7badb78 | -12.86147 | -38.3681 | 2025-07-10 03:38:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 06f3d98d-653a-3ed6-8f4f-594ee284b8d4 | -9.30289 | -40.23944 | 2025-07-10 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1f3d9f81-416b-30c1-87ac-95653e92aadd | -11.05718 | -45.8707 | 2025-07-10 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2b679579-9a2e-32f3-9b58-ab6ae12360b7 | -13.0087 | -46.32566 | 2025-07-10 03:38:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9f4fc5c-c532-31a5-9596-c26924219b62 | -15.47413 | -45.19786 | 2025-07-10 03:38:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2014d4e3-fef5-34fb-b0f7-c5c10204c076 | -11.67163 | -43.78165 | 2025-07-10 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb934cb2-8aff-3e91-8afd-8f44891f6af7 | -13.37237 | -43.75779 | 2025-07-10 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 511bc1cf-ef6b-3ff0-a9a4-17e1336d906c | -10.6227 | -45.23552 | 2025-07-10 03:38:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3feb22ea-b7e5-3f8c-bce0-c3559dbf0d60 | -13.90643 | -42.13371 | 2025-07-10 03:38:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bff05311-c434-31c5-a282-e2ccea20208e | -15.4742 | -45.19496 | 2025-07-10 03:38:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d8d71d1-8047-3098-986f-91afb5bbf229 | -12.48185 | -44.50478 | 2025-07-10 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a3e95b0-9c6d-36e8-b616-de75d979bd01 | -10.64224 | -45.22687 | 2025-07-10 03:38:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb4c4669-2619-38bb-b3da-35cece2507f3 | -8.8597 | -47.95051 | 2025-07-10 03:38:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9d9588dc-a379-3d98-8bc8-b583396a3a28 | -8.86009 | -47.95402 | 2025-07-10 03:38:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 94a804ba-5fae-3e04-9431-aabb2a5d9cd6 | -11.95763 | -46.35907 | 2025-07-10 03:38:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0cbb2b26-cc4c-382a-a7e9-a42d8df05353 | -10.63416 | -45.23786 | 2025-07-10 03:38:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c1d6e77-ac5b-323e-91ec-15318469d6fa | -10.89916 | -46.73438 | 2025-07-10 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a381c9e9-d6d8-36c8-9f87-4db60da91f69 | -12.98729 | -47.8308 | 2025-07-10 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0b512799-7e4f-3cc9-ad53-a9c6569dc293 | -12.43215 | -43.72311 | 2025-07-10 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 516ebd8b-07ba-3023-b584-29dcdfa27014 | -13.90202 | -42.13279 | 2025-07-10 03:38:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| a6e52a98-f3e1-3d03-87a0-82f83db8b1e0 | -13.89894 | -42.12957 | 2025-07-10 03:38:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 4dc7403f-0c6f-3a98-bcea-35edf9331724 | -10.62764 | -45.24076 | 2025-07-10 03:38:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b7ba603-b128-3722-95b6-ad6b38731820 | -13.37284 | -43.75768 | 2025-07-10 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c147d75-2ae0-3377-9f4d-5876e1802791 | -8.95829 | -47.2711 | 2025-07-10 03:38:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9c1a77d-0322-3561-8d68-42fed81cb574 | -14.73625 | -40.98079 | 2025-07-10 03:38:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bdcf2d3a-1162-37ad-994f-fbb6bdd50981 | -11.00117 | -42.77801 | 2025-07-10 03:38:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0890feee-6928-3b91-8e32-1207fcb8889b | -9.83478 | -41.49891 | 2025-07-10 03:38:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ace48ca7-99b9-3aa9-a8f3-8340105c31ef | -12.99811 | -46.28746 | 2025-07-10 03:38:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 703efd42-d723-33f1-9c2f-4a94e8389381 | -12.09801 | -44.73661 | 2025-07-10 03:38:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a6257cc-362d-3afd-84ed-0a4ece876748 | -8.95717 | -47.2768 | 2025-07-10 03:38:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30629104-f75a-37c7-9096-7061a61237ca | -13.9012 | -42.13715 | 2025-07-10 03:38:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 3bfaae15-bf87-3bea-8186-9bcbfe8db248 | -12.4277 | -43.71908 | 2025-07-10 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 91cfbead-1167-3c33-b58a-0596906fdb27 | -12.42712 | -43.7221 | 2025-07-10 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 31de5525-a51a-39c6-ae70-7af61c556971 | -12.43273 | -43.72008 | 2025-07-10 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f65ef467-dab6-3fe9-93bc-b245d158a0b2 | -10.62348 | -45.23147 | 2025-07-10 03:38:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 52e8708c-92a6-308e-ab14-721512ebb733 | -13.38142 | -47.8811 | 2025-07-10 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5934944b-2440-3666-9d68-0f22c2bfdafb | -8.8614 | -47.94728 | 2025-07-10 03:38:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4c843514-40b4-32b2-a1b2-aef85349e768 | -11.00604 | -42.77886 | 2025-07-10 03:38:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 709578ea-8b89-3999-830e-8375854707fb | -12.24324 | -40.96624 | 2025-07-10 03:38:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8f4a0ccd-2970-3963-a713-d059cdde0b2e | -10.64146 | -45.23091 | 2025-07-10 03:38:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15cfa572-820c-3564-82f0-d6df93845f2c | -13.89678 | -42.1363 | 2025-07-10 03:38:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 7e147e2d-1750-3944-bae3-303039aa0940 | -12.47654 | -44.50375 | 2025-07-10 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70156e1d-9f87-39d3-bc07-087b86139205 | -9.09207 | -47.96899 | 2025-07-10 03:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b9d6f737-562a-37a0-9d7c-bb70006d9baa | -11.06894 | -45.87353 | 2025-07-10 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8fcc4598-2c73-3989-be75-198e9f43ef85 | -14.84546 | -42.11277 | 2025-07-10 03:38:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 88bd80a0-3b8a-3a61-b82e-4a0e8cbd9d4b | -9.00183 | -47.45383 | 2025-07-10 03:38:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f050ff5-3c29-34ba-9433-a1fff738a16e | -14.73231 | -41.72728 | 2025-07-10 03:38:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 882a69dc-a902-3eb9-920f-90c1aa3c3ccb | -11.8276 | -48.21464 | 2025-07-10 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bcb0ca8e-b301-3518-a816-97bef105dfe5 | -13.6772 | -44.21975 | 2025-07-10 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a96981a-4d23-3617-b957-067c581b480a | -14.83757 | -40.90721 | 2025-07-10 03:38:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ef311fd7-5bee-3b12-9178-fed3c64f8665 | -12.9989 | -46.29369 | 2025-07-10 03:38:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README10.md)
