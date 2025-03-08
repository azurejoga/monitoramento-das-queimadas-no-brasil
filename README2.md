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
| b86939e2-9a9e-3c12-b5af-6aa3d330f71f | -10.66507 | -44.40085 | 2025-03-08 04:01:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 909a87c7-53ca-3b4e-949d-9e8e839bab72 | -10.34498 | -37.14407 | 2025-03-08 04:01:00 | NOAA-21 | AQUIDABÃ | SERGIPE | Brasil | 2800209 | 28 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 6019f6a2-0a1b-3ac5-9b1e-f7d7ab21ed20 | -6.97001 | -43.01613 | 2025-03-08 04:01:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d31ca1c2-8194-3dca-aea4-286202e213a1 | -10.34126 | -37.14355 | 2025-03-08 04:01:00 | NOAA-21 | AQUIDABÃ | SERGIPE | Brasil | 2800209 | 28 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 85c1d050-132f-3c88-a550-1c0602502a29 | -10.04392 | -37.68801 | 2025-03-08 04:01:00 | NOAA-21 | MONTE ALEGRE DE SERGIPE | SERGIPE | Brasil | 2804201 | 28 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4f9ed902-7234-357f-92bf-313a60128adb | -6.95711 | -43.00576 | 2025-03-08 04:01:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9e74b7f9-952f-3cd0-8613-e7acccb36dec | -10.34542 | -38.48164 | 2025-03-08 04:01:00 | NOAA-21 | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 434df57d-5c4a-3562-b1e0-2d7d084d3a72 | -10.34061 | -37.14799 | 2025-03-08 04:01:00 | NOAA-21 | AQUIDABÃ | SERGIPE | Brasil | 2800209 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 2bc2a635-44e3-3df1-816e-764eb14a2649 | -6.96223 | -43.01905 | 2025-03-08 04:01:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| bbfcd1eb-ed25-3c58-bcc2-209b1506e58d | -10.66433 | -44.40519 | 2025-03-08 04:01:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c241545-51f0-3317-aab8-a6d06d3700e1 | -10.34433 | -37.1485 | 2025-03-08 04:01:00 | NOAA-21 | AQUIDABÃ | SERGIPE | Brasil | 2800209 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| bad729d3-7b69-3ee7-9001-75c3e57ca491 | -9.00108 | -42.71615 | 2025-03-08 04:01:00 | NOAA-21 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dcafd6ba-0d0f-3593-9403-cde168b9b727 | -12.2345 | -40.29427 | 2025-03-08 04:01:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b98c0dd6-3089-37bc-89f8-323d9fb1c816 | -6.97357 | -43.01672 | 2025-03-08 04:01:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a21bf319-c10f-3953-972a-a92e60b96deb | -6.96579 | -43.01963 | 2025-03-08 04:01:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 710436da-9347-3331-a054-c3fbb07b78af | -10.62935 | -44.63428 | 2025-03-08 04:01:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b478070-f29d-3f05-a13e-9b1ce744085e | -9.60806 | -37.55137 | 2025-03-08 04:01:00 | NOAA-21 | PÃO DE AÇÚCAR | ALAGOAS | Brasil | 2706406 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c9ed61e8-a248-3109-a2dd-037d8414c381 | -10.49259 | -42.48663 | 2025-03-08 04:01:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 81349847-7d45-3685-8600-1307317a8052 | -9.15605 | -43.1242 | 2025-03-08 04:01:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4a2ec428-d554-39b8-ac61-90fa9bf6e62f | -10.31782 | -48.64564 | 2025-03-08 04:01:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ad891f5-c885-38b2-9e26-3cd33ad973f5 | -10.66142 | -44.40022 | 2025-03-08 04:01:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee5bf456-4793-35a5-bd3e-b0b8631ef428 | -6.95644 | -43.0098 | 2025-03-08 04:01:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9f8c123f-e725-309b-9ed8-8c8e3b505140 | -6.96935 | -43.02021 | 2025-03-08 04:01:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 50715dc3-1196-3278-b24f-dec19feb1170 | -10.10566 | -37.37212 | 2025-03-08 04:01:00 | NOAA-21 | NOSSA SENHORA DA GLÓRIA | SERGIPE | Brasil | 2804508 | 28 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 70e3a982-3699-30c1-b577-666db2154040 | -12.90472 | -45.06823 | 2025-03-08 04:01:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb749570-c999-31c1-b033-6de0cdea21c8 | -6.96156 | -43.02313 | 2025-03-08 04:01:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 677116ce-8a63-3497-b1c1-8cb35133b247 | -6.96512 | -43.02371 | 2025-03-08 04:01:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e9d16002-6147-30bd-93e2-b010a54d5ea7 | -5.67376 | -45.22969 | 2025-03-08 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bd19486f-8b10-31d8-90d2-7a56aa0f3849 | -10.98239 | -44.72743 | 2025-03-08 04:01:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b69cece0-8fb8-33fd-aca8-0ce59cd3ce22 | -10.98314 | -44.72297 | 2025-03-08 04:01:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 312ef7f0-7842-334c-a769-c763fb118b5f | -11.80105 | -46.64907 | 2025-03-08 04:01:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e95821b-9c2f-3a4e-b9df-8c1f2235cff9 | -10.69544 | -37.05045 | 2025-03-08 04:01:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 99ac39be-5779-3c97-8511-aa0a5649b9de | -11.64519 | -39.97071 | 2025-03-08 04:01:00 | NOAA-21 | VÁRZEA DA ROÇA | BAHIA | Brasil | 2933059 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9cd9bbd4-4f92-31c8-bcd6-7bfcf3f37971 | -8.07436 | -34.9786 | 2025-03-08 04:01:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dd67901e-0919-355a-9736-086ab728b43d | -12.59765 | -46.7421 | 2025-03-08 04:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b83867e-f543-3692-b0b8-2750d0cfc2f5 | -10.62563 | -44.63379 | 2025-03-08 04:01:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a9cfe9d0-3060-3d15-b04e-a47e2f999e7c | -6.9629 | -43.01498 | 2025-03-08 04:01:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| f8ce965a-943b-371a-ac1e-679d08e04eb3 | -12.86201 | -38.36707 | 2025-03-08 04:01:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c50ad45a-d638-37f0-90a2-a2abed6ed87e | -9.00169 | -42.71237 | 2025-03-08 04:01:00 | NOAA-21 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c674fb49-11f1-3f99-87fa-6f15266146ce | -10.69688 | -37.04816 | 2025-03-08 04:01:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5f143bd5-572c-39b6-b54d-b2aeaf9358f4 | -8.07487 | -34.97489 | 2025-03-08 04:01:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 86dd5cdd-cd78-3ea6-9f09-315e878e4fc6 | -9.99869 | -37.56991 | 2025-03-08 04:01:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a60c97ca-4357-3129-810d-ddc164b9c3f6 | -10.346 | -38.47778 | 2025-03-08 04:01:00 | NOAA-21 | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ec5de32b-fe3f-3b40-816a-387b37409367 | -10.49317 | -42.48295 | 2025-03-08 04:01:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 659153ce-d003-30a5-9520-85f3a985e44b | -6.96646 | -43.01555 | 2025-03-08 04:01:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| e73e63ee-64e4-3bfd-b737-beea4f25b510 | -9.90918 | -37.59246 | 2025-03-08 04:01:00 | NOAA-21 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 20e38df9-cf36-3947-b9f4-f48b02560e5e | -10.10609 | -37.37081 | 2025-03-08 04:01:00 | NOAA-21 | NOSSA SENHORA DA GLÓRIA | SERGIPE | Brasil | 2804508 | 28 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0084f33b-ea83-374d-9582-ebfefb3dd78d | -19.14685 | -47.09591 | 2025-03-08 04:04:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9ff3ceeb-cee0-3a53-8157-66d7f8678006 | -19.46853 | -44.30115 | 2025-03-08 04:04:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3932e6a5-b39f-3174-b932-b3ac3e336f45 | -19.85179 | -43.84538 | 2025-03-08 04:04:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| be39e680-1bf3-3b94-9cc9-f154b5ad99c7 | -15.83024 | -44.5369 | 2025-03-08 04:04:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d922611-e9f2-3853-bf48-1c5e4c2fc900 | -17.98327 | -47.21855 | 2025-03-08 04:04:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 69105cc6-d3a3-3914-96ad-10b20b1175f7 | -15.82957 | -44.54092 | 2025-03-08 04:04:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb48165b-8ba5-3181-a0e7-fba8a2dd905a | -20.38811 | -41.1824 | 2025-03-08 04:04:00 | NOAA-21 | VENDA NOVA DO IMIGRANTE | ESPÍRITO SANTO | Brasil | 3205069 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a8d397b0-3f90-39f8-9c4f-c72a6c30e899 | -20.20785 | -45.52717 | 2025-03-08 04:04:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3812c1da-2455-3d24-9943-bdc6656d7b9e | -15.30583 | -47.87743 | 2025-03-08 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53b71d77-6c1f-38fc-9f7a-d115c9e9bdd5 | -16.68268 | -43.88529 | 2025-03-08 04:04:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae0e25aa-b401-35d7-a4c3-31d291fe020d | -19.18488 | -40.12727 | 2025-03-08 04:04:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 905b3f22-0e87-3e13-87c0-06c493147c1c | -17.597 | -43.19666 | 2025-03-08 04:04:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e2fdccc-c473-37b7-b255-95f24220e695 | -14.85311 | -46.78612 | 2025-03-08 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a25b678b-34e6-3a36-9448-dab2e317cd5c | -20.34696 | -40.36212 | 2025-03-08 04:04:00 | NOAA-21 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 56e948b8-22c2-3fac-b288-a1a8a78cfc81 | -17.77787 | -42.80775 | 2025-03-08 04:04:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56fbbbdb-fa5c-3b26-817f-f758fea0d17c | -13.17456 | -45.22577 | 2025-03-08 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1eeb7fa-bdc6-302f-bf9c-2faf53cdf476 | -19.15974 | -40.25507 | 2025-03-08 04:04:00 | NOAA-21 | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8a01672c-df05-39d2-aef5-1f9d5213fc7f | -13.17087 | -45.22512 | 2025-03-08 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76a290b7-e034-304d-8ba9-bcab13e10b3e | -15.30657 | -47.87344 | 2025-03-08 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 437f3ae3-bd04-309f-b43e-3142f86d6e57 | -16.61182 | -43.33357 | 2025-03-08 04:04:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 653ee8a3-9c52-363b-a0a8-28fefce26a09 | -17.78118 | -42.80832 | 2025-03-08 04:04:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84368ff7-1efe-3d7d-a864-8da487758390 | -13.35884 | -47.03077 | 2025-03-08 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db315d44-1bed-3b93-a2d8-cfd6bbd8d7f2 | -18.21746 | -45.23305 | 2025-03-08 04:04:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa4e3113-8497-378b-b117-e45e2ad0ac73 | -19.74199 | -43.87194 | 2025-03-08 04:04:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05ce2470-ee1b-3c78-a395-9f88515a29f1 | -19.18135 | -40.12671 | 2025-03-08 04:04:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 344f84cd-d38e-32be-be4a-0d3aed11fe59 | -18.49394 | -41.86663 | 2025-03-08 04:04:00 | NOAA-21 | FREI INOCÊNCIO | MINAS GERAIS | Brasil | 3126901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0774d54f-86ac-355b-949c-eaf30482f650 | -17.34709 | -43.86211 | 2025-03-08 04:04:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76c3dd0a-52d5-3d3f-82f4-627cb60a79b9 | -13.57844 | -43.35359 | 2025-03-08 04:04:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c00ac74e-c1a6-36fb-be8b-6ef07305dcc2 | -16.24368 | -44.43731 | 2025-03-08 04:04:00 | NOAA-21 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0e1ae147-3fba-3b42-94a7-5b0badb67788 | -13.8773 | -44.3119 | 2025-03-08 04:04:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e224f14-1e66-3516-bc9e-1ad31759806b | -18.80138 | -47.02048 | 2025-03-08 04:04:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46524f2b-80be-371f-8aa1-79daa9771086 | -18.03971 | -39.9259 | 2025-03-08 04:04:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 65967c6f-7298-3b75-a2c1-0f5fa7065cdd | -20.06627 | -43.04694 | 2025-03-08 04:04:00 | NOAA-21 | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 67cb1f61-3d76-348a-b2bf-cb0683356e67 | -13.87313 | -44.31533 | 2025-03-08 04:04:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 853524f7-804e-303d-89d0-7acf86a72bfb | -20.21129 | -45.52787 | 2025-03-08 04:04:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e88a7dca-47f1-3e0a-8565-50c99f9253be | -13.87663 | -44.31594 | 2025-03-08 04:04:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe08ada6-0661-3605-a2ce-4d2586d1300e | -13.8738 | -44.31129 | 2025-03-08 04:04:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9eac612-8903-33e3-9c26-d763975b0577 | -19.71642 | -40.35282 | 2025-03-08 04:04:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 24dc378c-15c3-3e4e-8535-c7a134b0d12b | -20.04457 | -45.55165 | 2025-03-08 04:04:00 | NOAA-21 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 9d6ba220-80c8-39f2-be58-6e38c504b80f | -13.90679 | -46.1057 | 2025-03-08 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1980f70c-f6a8-3fe6-a123-1d1060f5ae87 | -21.6126 | -48.47771 | 2025-03-08 04:06:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54285249-52e4-34b4-9e70-8736ae1af799 | -20.99659 | -51.79385 | 2025-03-08 04:06:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 10e8df3b-7a1b-3a44-9678-c45167fdef43 | -23.92227 | -46.37101 | 2025-03-08 04:06:00 | NOAA-21 | SANTOS | SÃO PAULO | Brasil | 3548500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 18f3af7d-5948-3974-b34a-32f084d4c020 | -22.62503 | -42.96024 | 2025-03-08 04:06:00 | NOAA-21 | GUAPIMIRIM | RIO DE JANEIRO | Brasil | 3301850 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a7dde648-e21e-3d87-9eda-0da3cebfdbd8 | -20.50823 | -47.50687 | 2025-03-08 04:06:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b99f2281-406f-37f1-99f7-dc3567494882 | -22.54183 | -48.81275 | 2025-03-08 04:06:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9acf27a-a820-35dd-8d48-87f1bd8abc62 | -23.0208 | -48.43268 | 2025-03-08 04:06:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ad14ad7-dacb-38a7-b063-e1a21ea4f2d6 | -21.25659 | -48.7117 | 2025-03-08 04:06:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| ded7430b-256b-3f49-9784-cdffd4a05eee | -21.88016 | -53.71857 | 2025-03-08 04:06:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ceb144b1-141d-39ef-be2c-775216b5066d | -23.73566 | -53.24911 | 2025-03-08 04:06:00 | NOAA-21 | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2aaf3a07-83b2-3153-a2e6-7a9ef6187e43 | -21.25989 | -48.71614 | 2025-03-08 04:06:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 32224ecf-3ab2-342a-9aa4-456c7feb3950 | -21.2559 | -48.7154 | 2025-03-08 04:06:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| feba4f95-122c-3bae-b07e-7c2ad163d9fc | -25.72713 | -50.78056 | 2025-03-08 04:06:00 | NOAA-21 | RIO AZUL | PARANÁ | Brasil | 4122008 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |


[Clique aqui para ver as próximas entradas](README3.md)
