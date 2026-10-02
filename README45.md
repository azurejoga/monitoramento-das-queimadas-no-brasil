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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d507e997-9ac2-3327-8be8-de36d5407bb8 | -9.66636 | -47.66331 | 2026-10-02 04:17:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d01e23f-c99d-3b46-bf4a-8899d7b14e54 | -10.51545 | -50.85343 | 2026-10-02 04:17:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 11781f9b-791b-37cc-8517-5802032d67a1 | -11.13849 | -44.60894 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebcbea8f-088c-38b2-ac18-3ec2fac35b08 | -11.4649 | -43.5082 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d8e3548f-f829-38f6-b149-f15345f16942 | -10.90233 | -51.18611 | 2026-10-02 04:17:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8b41d7bd-091e-31cf-aa53-944aaf8f4b92 | -12.51444 | -43.10601 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d9494167-559e-3a5b-9e12-eb7b81640a18 | -11.80103 | -43.57433 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 514a99b3-b145-30e6-99e5-617899f5b039 | -13.86686 | -43.637 | 2026-10-02 04:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 40151fd1-dcb8-3623-abf4-2827b70fda6c | -15.24182 | -46.16482 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d1f20033-f48f-30ca-8352-578ce9d88b68 | -13.33154 | -43.86055 | 2026-10-02 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bf7f6afa-416c-300d-bd63-195176f3a61a | -12.56306 | -43.07785 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5683f596-bbd9-3f3c-94e9-e38de9d3f825 | -12.46216 | -44.15203 | 2026-10-02 04:17:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 99c1e73c-6005-34a2-90d0-dd23abc0b29c | -11.25272 | -44.25325 | 2026-10-02 04:17:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23d78133-689e-3e5a-bc0c-c26b2e99356d | -14.04048 | -43.84761 | 2026-10-02 04:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f43163a-bae8-381d-a7ff-2234656a500b | -11.72632 | -43.44648 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c83fcbc9-48e4-3c58-b921-c82196fb5320 | -11.69534 | -43.59726 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e512e7b-a215-3486-857b-881f93c09d2e | -11.73959 | -43.44867 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 584ecca4-c69e-38ff-9744-665bf9480457 | -11.77277 | -43.58053 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16579058-6565-39aa-b18d-e3628452a8b7 | -10.82115 | -51.09543 | 2026-10-02 04:17:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eb602ac8-46c9-3e70-a30e-536720f82c7f | -11.15273 | -44.60751 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5525402b-f9ea-3848-a595-ffd16f1344e5 | -11.41082 | -43.40163 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1512e175-3ed7-3487-a6c6-365caf799c74 | -11.78111 | -43.57106 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c7660245-9bc5-3676-8f18-3b419c2c1f78 | -14.098 | -43.93411 | 2026-10-02 04:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9cac5e69-1444-36f5-b5c9-807e9d4898f4 | -11.47405 | -43.43003 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5f61aa88-28a7-3325-9327-e671310f5abc | -14.43461 | -44.77389 | 2026-10-02 04:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b7c26a5-b6d0-3014-bbd1-1d48ce79c4c8 | -11.72195 | -43.43127 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3f372a1-50b1-328f-b2d7-238117ed44e4 | -11.6549 | -43.59423 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 505e724d-b640-35e1-98b2-eafeb9b73f97 | -10.26271 | -49.66486 | 2026-10-02 04:17:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| af38a853-71b5-30b3-9586-187594833cbd | -11.15769 | -44.61985 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 5bac90a9-cabc-3c7d-b734-bf666c4605d8 | -12.52549 | -43.1006 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 342f17b6-bf9a-3440-ae4c-67692a4619f6 | -13.38442 | -44.01928 | 2026-10-02 04:17:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b78f22f-431d-3b58-8346-000da4ba5738 | -11.47511 | -43.44469 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d6c5ca27-5de9-3e1d-ad34-e229bbfb4e84 | -11.66155 | -43.59533 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 818775d4-6ab6-380d-b67d-d20a6bb067e9 | -12.52274 | -43.09653 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 90226f4c-edc9-3779-83f3-021a46edac4b | -11.69202 | -43.59673 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7542c8e-0ffb-3a30-8dc1-73aac0385375 | -11.25562 | -43.52078 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4d84df8-50d2-3530-be08-c8758acaa139 | -11.72964 | -43.44702 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97a9a7c1-5635-3238-923c-fce27849642c | -10.26355 | -49.66007 | 2026-10-02 04:17:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| b8568978-6911-3215-8adb-7cb016953f12 | -11.77666 | -43.57754 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29a5ae8a-8815-3a00-b132-50aeca795c38 | -16.99538 | -41.18413 | 2026-10-02 04:17:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b514cf6f-faac-3901-8a08-e9ecc5093648 | -9.86643 | -48.23101 | 2026-10-02 04:17:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5516a949-4350-391f-9b10-0bab8bfc33b6 | -15.25506 | -46.17116 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0e12b457-1315-3285-9f0c-50ea7ec6ceaa | -11.76612 | -43.57946 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0b1e7918-2526-36c9-8c8e-2a01039c1aa5 | -16.13243 | -43.74316 | 2026-10-02 04:17:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cfacf3a0-8622-364a-9fbf-fae00dbc6ece | -8.53956 | -54.56936 | 2026-10-02 04:17:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dbe9f866-b74d-335e-bca3-6ff5b7a44c12 | -13.86243 | -43.64353 | 2026-10-02 04:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 25da2dc7-9422-3c00-9ef1-a2616f71fbdb | -12.9915 | -51.28826 | 2026-10-02 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 303cde03-2e7b-38f8-a52a-d1e6631a65e6 | -11.79771 | -43.57376 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ff94fe6-e5f2-3144-9fdc-2bfeb191dd20 | -11.12109 | -44.6062 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c5341b3-1f4f-3004-a666-49e19a0870b7 | -11.70701 | -43.58831 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce529e63-58ce-3f56-b71c-eeec29b1e91b | -12.52992 | -43.09409 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0ac269b2-0051-3880-9250-9855857832b5 | -11.13694 | -44.5972 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0df6fe1c-d7dd-3018-8ba3-15bf7e48a325 | -12.52162 | -43.10358 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 21b23f2a-d83a-3267-bb45-24f4b192d89e | -9.334 | -50.99833 | 2026-10-02 04:17:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d357306f-5190-353c-b1d2-e7227aa248a5 | -15.04044 | -40.50689 | 2026-10-02 04:17:00 | NOAA-20 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0d5c5bac-4355-3c91-ae1b-e9e12135b14e | -11.77609 | -43.58107 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7942cfb-5a76-3705-8e17-a0897650aadf | -15.24809 | -46.17006 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9fd579a2-1f19-36fa-af08-e6830c4af412 | -11.76781 | -43.56894 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12f04417-d54f-375a-b3cf-216a0ef90dfd | -10.89565 | -51.194 | 2026-10-02 04:17:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5031b12-9c41-3c28-9e41-91d6773170ed | -11.65927 | -43.60947 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 177e6092-ffed-3129-8646-cd97562629a1 | -11.68311 | -43.60973 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d56979e7-ede3-3c72-bc63-86b7baead48d | -13.33543 | -43.85755 | 2026-10-02 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3d9028b5-7b33-3eb9-99ab-dac929d7b1d6 | -12.51887 | -43.09951 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0bf730bc-a74e-34fd-aa89-7f35d52dd5c7 | -11.11768 | -44.60565 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24d573a8-e38a-3a41-8911-6f99df305f50 | -11.79553 | -43.56615 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 521893b8-358f-3a91-a23d-8ee37f981816 | -12.99258 | -51.28274 | 2026-10-02 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 65588665-f6e4-3f90-9361-a5377d8c08e4 | -11.75891 | -43.58191 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| cb5b653a-b2ca-398d-8ab1-9bc125c60215 | -11.1419 | -44.60952 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 69ef2210-f6a2-3acb-b404-0077e03f6e27 | -11.13509 | -44.60836 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a7076f5-18f5-3298-9e9d-7916952f7c73 | -12.83174 | -50.65289 | 2026-10-02 04:17:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 085a75d9-ef59-3a99-bd2f-2f84381126c1 | -14.3311 | -44.74108 | 2026-10-02 04:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 590c6425-af70-35fc-bf8d-e443f164f779 | -11.73697 | -43.5715 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 57e57929-8a69-3830-a5c4-8e89db97be88 | -10.84161 | -48.6878 | 2026-10-02 04:17:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cf0f1d35-e172-3caf-8148-d2f337b1c999 | -11.75615 | -43.57788 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 71dfdb8c-8887-3477-9bf3-252eb4841f22 | -12.52218 | -43.10006 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 41c964e3-5bd7-35bb-8318-166528aece0f | -11.30571 | -50.92982 | 2026-10-02 04:17:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e50cd6b-71a4-3fd4-a86e-9ab03a36d5af | -11.25549 | -44.25747 | 2026-10-02 04:17:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a0448b0-fb1c-3c0e-9db3-0f610f68f0a7 | -11.25053 | -45.23095 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12fcc135-5836-33a2-869e-61aa58d4de0b | -11.65376 | -43.60131 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 7b3857e6-fe5d-370f-9438-13a7bc64818d | -13.63865 | -41.35763 | 2026-10-02 04:17:00 | NOAA-20 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 33f2b85b-1457-3f65-ba93-1643e19854e3 | -15.49808 | -41.55171 | 2026-10-02 04:17:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b525e4a3-0302-357d-8fe9-e9dc95a16b08 | -9.89984 | -50.1567 | 2026-10-02 04:17:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 944741cc-bdcc-3a2b-bdca-174a3f19846d | -11.68091 | -43.60215 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b78de07-7ef3-3e65-9954-1795c5c14a51 | -11.2634 | -43.5148 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0e36ed08-9ae4-306f-a433-bed81de5f7fc | -12.93038 | -42.48874 | 2026-10-02 04:17:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6d44cd36-1d3d-3656-8211-57a7602bb3cb | -11.27207 | -43.56706 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc90ce69-50ac-3be6-aed7-6aef321ed5fd | -12.53434 | -43.0876 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7a86f72b-cf27-3e01-b76d-1d79e399c58b | -11.10527 | -44.59591 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b2f0af6-27b0-3c71-a02c-d40c265316ac | -11.68367 | -43.60622 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f52a989f-f098-36b2-9957-24bfe24d6f29 | -12.98427 | -51.28618 | 2026-10-02 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b0b74e25-331e-38bd-9499-28f53dd70e72 | -11.66373 | -43.60295 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.7 |
| a8413040-1165-3aef-8326-456f052d09b5 | -8.54604 | -54.57058 | 2026-10-02 04:17:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 566612c6-fda3-3bb6-b53f-c5d40fb2b894 | -11.76945 | -43.57999 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 840541b3-a1bf-328e-b5e7-4fc46189f5dd | -15.93189 | -41.3557 | 2026-10-02 04:17:00 | NOAA-20 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| ac9ab39e-2fdf-3f1d-8f8c-8eca38b2095a | -12.44177 | -44.193 | 2026-10-02 04:17:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa620c7b-3633-39e8-b145-3332f2a3f1e4 | -13.39326 | -46.82098 | 2026-10-02 04:17:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da5cc3bc-c3b1-33db-a673-687a78b80a6d | -8.53413 | -54.56272 | 2026-10-02 04:17:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d949b7dd-d0f4-3910-984d-86f983499f5b | -13.38717 | -44.02341 | 2026-10-02 04:17:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b07a537-0e5b-3e76-8eb4-fedc32826293 | -14.34235 | -44.73546 | 2026-10-02 04:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6dc46b21-b887-3f93-8e20-d47f7f313eb7 | -11.13756 | -44.59349 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README46.md)
