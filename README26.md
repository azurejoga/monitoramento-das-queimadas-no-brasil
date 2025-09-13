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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d715ff46-5861-38bb-88ee-0debddb3b82b | -12.99709 | -46.74007 | 2025-09-13 03:47:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2b3b06ca-b54a-3c4b-8916-7985b00dbb44 | -9.41689 | -43.40858 | 2025-09-13 03:47:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b91ef089-e2b1-30a2-8942-f246f7eac591 | -12.83012 | -47.94756 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 504a6255-1af2-3683-b98c-70a9743b2ab3 | -7.4377 | -44.40692 | 2025-09-13 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 796483ec-953c-3fd7-b1b7-3438222d894e | -17.13438 | -48.51371 | 2025-09-13 03:47:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bca17591-5dd2-3beb-bdd5-caafa5c2d2c2 | -11.86181 | -46.76117 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1278546a-0329-32c6-9632-391d701a610c | -14.19713 | -46.24316 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 27.3 |
| ed66829e-207a-3260-bfc4-31f35f8a978c | -11.48926 | -43.70304 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b829f97c-7938-32c9-afbc-99a3b793afa6 | -13.26485 | -43.74475 | 2025-09-13 03:47:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ab2bc05-ac4f-3703-8735-85abbeaec53a | -18.70351 | -43.39516 | 2025-09-13 03:47:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a59ee9d0-e1bb-3091-be28-5a854aa36e19 | -11.82876 | -50.55663 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 87201ad5-370a-3f67-8120-dc65b17d7a45 | -16.64641 | -49.77642 | 2025-09-13 03:47:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 071d66bd-cafa-328d-a2d2-6c559e87fc20 | -12.09004 | -44.87979 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6d276999-0d95-3a3d-be4c-24ca48adc88e | -8.95564 | -44.45861 | 2025-09-13 03:47:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5752efb4-e9d0-333c-a48f-ff173ab23c36 | -11.13929 | -45.31945 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 747bc284-f7aa-38e6-9e71-a3a5f9517357 | -20.02328 | -47.63575 | 2025-09-13 03:47:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45bb022d-8fdf-3e7f-85e0-784e9966ccda | -14.29683 | -46.06631 | 2025-09-13 03:47:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| fa0ffef9-29e4-393c-bfbf-92be156cb9c4 | -17.41053 | -49.25002 | 2025-09-13 03:47:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14b784e2-9553-3387-a7b8-bad64ceace82 | -10.38549 | -50.49665 | 2025-09-13 03:47:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94c075b9-aeeb-3a54-b602-e4ce6e2a76d0 | -18.61379 | -48.2094 | 2025-09-13 03:47:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49173256-7479-311a-a282-fdab61d4cec1 | -10.78433 | -50.55181 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| ec740eb2-987a-30dd-a4e1-c128b89f763f | -14.22 | -46.26671 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 63ab7a08-97bb-3ee9-8f6b-5540c88062c0 | -20.01868 | -47.63474 | 2025-09-13 03:47:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 350a4db8-0b11-3988-86d3-9b1875551b77 | -18.88656 | -47.05618 | 2025-09-13 03:47:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2217416-fdbf-31e8-94d9-e41d41a1baf0 | -20.01622 | -47.64367 | 2025-09-13 03:47:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09aff926-7f97-3bd6-bcd4-4dba8ddcf63c | -16.64368 | -49.78285 | 2025-09-13 03:47:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d278f152-2c4d-390d-8c86-380a1c54e55b | -14.28963 | -46.07517 | 2025-09-13 03:47:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ccf091d7-ba4b-35ab-a3c6-33f567db04d9 | -11.72783 | -46.59252 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9c2d7c6-4416-3d94-8810-1949a882f257 | -20.09757 | -46.92487 | 2025-09-13 03:47:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d909aa83-ddde-3fbf-8704-d1b7ac08c346 | -17.30195 | -48.73106 | 2025-09-13 03:47:00 | NPP-375D | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 00960a57-f4d2-37ae-b141-3022c3187009 | -12.12251 | -47.5957 | 2025-09-13 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 36ec22a0-d6db-3f74-847a-816b42702da1 | -10.3373 | -48.82947 | 2025-09-13 03:47:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 1a3188bd-5f08-3618-a8d2-3f88e37dc8b4 | -20.34321 | -46.66796 | 2025-09-13 03:47:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f77b629-ad8b-3494-8f63-309e917f751c | -14.1977 | -46.24026 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| cd05840a-4e2e-399f-9faf-824bd0cdee9b | -11.37649 | -43.5084 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec276c65-6728-397f-9f4c-c1d81ef59def | -11.85005 | -50.56142 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 96418562-3310-324e-9186-3e0488c0c78a | -20.01911 | -47.6558 | 2025-09-13 03:47:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 13a1fa93-6384-345e-8f5e-67d5a7472701 | -18.13802 | -48.45991 | 2025-09-13 03:47:00 | NPP-375D | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c204285f-c2a7-3f6f-baf6-86b73e0c85b4 | -9.195 | -45.78106 | 2025-09-13 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b39eae4d-cadf-3de3-b0bd-6a2dfbf06fd1 | -8.95222 | -44.4479 | 2025-09-13 03:47:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8829213-93b6-3f39-8b87-4b4bfe87c323 | -11.53484 | -48.29607 | 2025-09-13 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37a05818-4e20-3665-8460-01784cec6003 | -11.36344 | -43.50089 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc8372d7-41b2-3d38-905e-7dc31a1bd916 | -12.13313 | -44.84377 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4479a68f-1420-3cb0-888c-bde0775924cd | -10.74873 | -50.50518 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 33f8010a-aa7b-302e-8e7e-460833a65b31 | -10.7613 | -50.5233 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 62fbd5ea-4f86-376e-b364-82b5f1ccf935 | -12.09744 | -44.86806 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a06cec48-d22d-3a4c-b6c5-73aa6dea5eff | -9.71711 | -48.31979 | 2025-09-13 03:47:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 995f9eed-19e7-3528-b953-3868af482101 | -17.28669 | -47.23883 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddfeb603-273e-3e72-9e81-42227837165d | -12.08247 | -44.89232 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71156073-401a-328a-9ae8-7d72a6240674 | -10.01127 | -50.39771 | 2025-09-13 03:47:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 08cb24c3-09be-3377-85e1-b8676a94bc9e | -13.92122 | -48.27354 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 4d7e7272-f13c-3ad7-911b-8de44238d32a | -11.73162 | -46.6031 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79359876-f618-3037-8ac3-d221c6b28dc0 | -11.7152 | -46.5673 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 396573fc-4da1-34dc-a2c1-d5166620bbd1 | -13.26677 | -43.7599 | 2025-09-13 03:47:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25015c6b-d8c2-36cb-93dd-2dc2fbc02406 | -19.64051 | -45.07902 | 2025-09-13 03:47:00 | NPP-375D | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 63eed76a-d221-3704-9900-d444223cedb4 | -17.33582 | -46.66549 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7a21111e-8b4a-3410-b7a2-4ee5c07623ef | -11.83234 | -50.56141 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 5bfdafd7-b4f5-3f74-8d70-0f34daad2295 | -14.22151 | -46.27754 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 2daeaa04-c38f-3b7e-8777-49a7bbd91444 | -14.19463 | -46.2837 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 96f2fd1a-6f87-36f2-8147-69e028bfb61d | -9.00937 | -45.78019 | 2025-09-13 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1eabf07e-1c4b-3725-9c01-9b74586d7c5e | -16.33258 | -51.54046 | 2025-09-13 03:47:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e5a8368a-c4c6-3e4a-8d2d-1467267d85d2 | -12.84988 | -47.94309 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 130ec904-397e-3c04-a5f8-b57865812835 | -11.86271 | -50.57172 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| adf67eb8-76bb-397b-86b0-d5a12d37277f | -20.10382 | -46.91965 | 2025-09-13 03:47:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d1155f9d-69cd-3222-912a-3556afe63fca | -14.22336 | -46.27767 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 37.5 |
| bc3956a8-232d-3aaa-8e64-059d17be45b6 | -14.69584 | -45.14223 | 2025-09-13 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b9b730c8-acd7-31df-a4ed-2cb77d19ba96 | -11.44553 | -45.62813 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a734dd08-67b9-3e47-ac49-0b1a6c757010 | -16.33423 | -51.53318 | 2025-09-13 03:47:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 917f7002-7aa7-3937-b501-85465d672d97 | -9.75478 | -45.38967 | 2025-09-13 03:47:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77712922-f0ac-3a0b-b36e-71a16b94e932 | -7.55237 | -43.95152 | 2025-09-13 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bcf3ae6e-156f-3a75-bb7f-0647a544cce1 | -13.47412 | -48.44856 | 2025-09-13 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 737ba97d-b56c-3e89-a2e1-bdf62e82dc5a | -12.8198 | -47.96271 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5f88be08-ee75-33f1-a3b5-8361a39c654c | -16.52968 | -51.75996 | 2025-09-13 03:47:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ed0504e-f1a4-3b9e-8c8c-a3cbeaf49472 | -14.21673 | -46.30111 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 50.8 |
| f5fd7654-d706-310c-9233-8caab1aed001 | -17.2763 | -47.24984 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8265cffd-4b0b-3d81-9c3b-4e44b8c29daf | -11.86793 | -46.76447 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b6fb9d56-7a3e-3f01-9f65-08f4650c49b7 | -13.5852 | -44.88745 | 2025-09-13 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7a90b194-4f61-375a-9336-f723cc119d49 | -11.36255 | -43.50581 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 130c65a3-9e57-3b60-bc33-8901f6ad0311 | -8.17642 | -42.44218 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 89fae6e8-6465-3162-80bc-31880469e3ea | -11.77254 | -50.56271 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f2444f5d-22a3-38a9-acdc-b1f22087f666 | -11.85256 | -50.58432 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 3b4b0dfd-ae31-311f-a84c-ae9f9ae93b06 | -12.99148 | -46.7391 | 2025-09-13 03:47:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 956719f7-dbfd-36da-91f2-ee1f6fb2a947 | -17.92079 | -44.45398 | 2025-09-13 03:47:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c20f7e51-d156-38d8-84f6-8351fddede95 | -16.35885 | -51.54221 | 2025-09-13 03:47:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2089b2c7-a6bd-3d96-a754-1d7146674c7b | -16.55559 | -49.22188 | 2025-09-13 03:47:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f7290972-1123-335d-a1b2-410f635a8a1b | -11.93795 | -44.29579 | 2025-09-13 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6ea0c34-09fd-37da-9349-8912f0ba8f2c | -14.18415 | -46.28099 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 29fb1467-8df9-3d49-93a3-3837dc8954e2 | -16.33645 | -51.54412 | 2025-09-13 03:47:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 55bf5881-e765-3b9b-8ffa-2170b635cb63 | -11.4281 | -45.61997 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2822f7da-1acc-39e9-b1a0-2279e408a91c | -18.85604 | -46.83119 | 2025-09-13 03:47:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 29b8a5f6-c32c-3440-9d43-778356d2de63 | -18.42893 | -43.64934 | 2025-09-13 03:47:00 | NPP-375D | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68a79f37-ba7e-3771-8014-d68abf2cfc9c | -17.42136 | -49.22948 | 2025-09-13 03:47:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8ba38e7-831d-3779-837b-0b65fc58f1b3 | -8.48642 | -45.14993 | 2025-09-13 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 719f9d50-1150-3077-bfb1-93de48f2cba9 | -8.09502 | -44.51564 | 2025-09-13 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c610395c-1256-3804-a9e0-c577c3147853 | -13.77696 | -46.2964 | 2025-09-13 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 169125b5-a95f-382c-bb88-233f3eabbc6a | -12.13064 | -44.82574 | 2025-09-13 03:47:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba723b48-2cd0-32b6-866c-560fffef73a6 | -14.18268 | -46.26056 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 653502e8-f337-37bf-9e98-43c4441a8972 | -11.86751 | -46.76231 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 280954cc-9ad4-3fff-b2b7-8fad278e9ae3 | -10.71568 | -46.38573 | 2025-09-13 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a76f45b2-f7ec-3cc4-a4df-9dd0e3058a54 | -15.62318 | -39.24976 | 2025-09-13 03:47:00 | NPP-375D | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README27.md)
