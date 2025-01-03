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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 762fbd26-9cf1-3498-87d3-7b8f81491226 | -1.61703 | -46.20799 | 2025-01-03 04:25:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 50d44535-00e5-37d1-8850-28af79a2f97c | -1.16243 | -53.77208 | 2025-01-03 04:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6ac051e3-372d-3101-b33a-078445a69d22 | -1.82665 | -45.76332 | 2025-01-03 04:25:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a183af42-80ea-3446-8c01-b9302d696946 | -2.57495 | -51.89883 | 2025-01-03 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f28c8408-f3be-3f6f-9cfe-eceac343d624 | -1.64596 | -46.13367 | 2025-01-03 04:25:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 820f9bf5-21d1-3fc8-b1c7-edd2bfe2afa3 | -1.8854 | -45.5637 | 2025-01-03 04:25:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9e37169-6a0a-37e3-86b6-5f4b64e93e7c | -5.50187 | -44.82919 | 2025-01-03 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf78e626-2e60-30c0-a0da-1b040c292a8b | -3.90909 | -47.05413 | 2025-01-03 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71366a6b-fb81-3c28-9ae7-a3b238c27c9b | -5.04521 | -43.62191 | 2025-01-03 04:25:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fadfac87-1875-3c2b-b303-b74fccadec12 | -3.86412 | -40.45122 | 2025-01-03 04:25:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 379b1d28-2de1-3aa3-a480-f04e85e1640e | -4.87688 | -39.05009 | 2025-01-03 04:25:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d3ea9e55-8188-31a5-b6a7-e3e2e2c8d4f9 | -1.68952 | -45.90158 | 2025-01-03 04:25:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c276c92b-837d-3cd4-80fc-26d8b382fb54 | -5.97208 | -44.29434 | 2025-01-03 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ff72209-eb38-30a4-999e-412e03318416 | -6.13018 | -42.54567 | 2025-01-03 04:25:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 8547765a-1612-3745-8c0b-1078f39b32eb | -6.97136 | -43.5553 | 2025-01-03 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dceb0530-0b23-38c4-bfd5-ad38f60c2c8a | -5.09618 | -44.58971 | 2025-01-03 04:25:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0878384-e8d4-389b-9b0e-40facdf0135c | -1.64317 | -46.12966 | 2025-01-03 04:25:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29f619d3-0e46-32da-8f82-f890f01b39a2 | -4.15909 | -42.03017 | 2025-01-03 04:25:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6ad4b599-55f1-3c04-b4e8-fb2a71aba0e2 | -6.97919 | -43.55232 | 2025-01-03 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1fcbf588-13ce-3f0b-b87d-a7793c7a07da | -4.80209 | -43.30373 | 2025-01-03 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 25d6b2da-c108-31a5-828c-592ef3a7648e | -1.67776 | -46.17086 | 2025-01-03 04:25:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63e1e973-9adf-376e-955e-21bb097de0e7 | -1.71843 | -46.23097 | 2025-01-03 04:25:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7c297f8-7d7f-3c69-acc0-154f60b389b5 | -5.04518 | -43.62075 | 2025-01-03 04:25:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8a2e8348-4703-31b0-8438-cde0abe33a9c | -5.62687 | -44.83666 | 2025-01-03 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3cfe9c07-208e-3736-a4d8-3e28e25388af | -1.62038 | -46.20851 | 2025-01-03 04:25:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 86ba163d-670d-3827-8bd6-9a149c9537d1 | -4.15978 | -42.02565 | 2025-01-03 04:25:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| eebfa598-7b3a-36e0-ac55-55532fac0e13 | -1.37439 | -45.86288 | 2025-01-03 04:25:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d388a6f-5636-3538-b257-a50786e3514e | -6.76285 | -35.32016 | 2025-01-03 04:25:00 | NPP-375D | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 2f9a7b6b-c295-3660-adae-555ad18ff4b2 | -4.25653 | -42.60768 | 2025-01-03 04:25:00 | NPP-375D | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2e788ee9-1930-334a-9d18-16bc47d4be5b | -5.53424 | -42.8955 | 2025-01-03 04:25:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 90fb7e7d-2062-34a8-b063-ff0ec313f360 | -6.76234 | -35.32394 | 2025-01-03 04:25:00 | NPP-375D | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f54017b3-e789-3031-a371-133bfa11209b | -4.87415 | -39.05167 | 2025-01-03 04:25:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 089743a8-7bc2-3362-b4de-4db207121fda | -4.74173 | -41.82113 | 2025-01-03 04:25:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0cb71524-384c-3268-baec-ade0e55b6103 | -1.29128 | -52.10564 | 2025-01-03 04:25:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da1b9beb-361a-3d52-999e-03f35c2e7600 | -6.48318 | -43.11636 | 2025-01-03 04:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 850d7297-06b7-394a-92f0-88dad312a12f | -5.09278 | -44.5892 | 2025-01-03 04:25:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1c56cab-da28-35ec-926e-0591d51c0bdc | -4.52276 | -44.39492 | 2025-01-03 04:25:00 | NPP-375D | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9cb8cfd3-3424-34df-a262-956cc2e8fc56 | -5.18539 | -37.63439 | 2025-01-03 04:25:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3abd4b59-3b6a-3079-984c-ba623b812b7d | -1.6811 | -46.17138 | 2025-01-03 04:25:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7401a450-ef41-39d8-be69-59e40847990f | -1.77483 | -45.91848 | 2025-01-03 04:25:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2275ac3-6102-3188-8bb6-ba44c0f8df0e | -5.08767 | -44.5326 | 2025-01-03 04:25:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 468acb13-3c82-3c38-a45f-64b8728941bf | -5.70555 | -44.95895 | 2025-01-03 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b8e22303-5bc5-3b59-afea-0c2c717aa1f9 | -1.72122 | -46.23499 | 2025-01-03 04:25:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a8643be-5002-3a15-b31a-1b64329a58cf | -1.83097 | -45.71441 | 2025-01-03 04:25:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 999985bf-046c-3d52-85d3-bd7d7761328b | -4.72143 | -46.99333 | 2025-01-03 04:25:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2e974b84-e8f2-3cae-b2b8-3a838ada36bf | -5.92352 | -43.78791 | 2025-01-03 04:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb122e21-bb1d-38b2-9ddf-60b515c56261 | -3.85997 | -40.45057 | 2025-01-03 04:25:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f1f8e603-edf1-38ba-8b4d-d2f87c6968bc | -5.70249 | -44.79665 | 2025-01-03 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c0648fe-b449-365a-add6-64b6669164b0 | -5.18496 | -37.63744 | 2025-01-03 04:25:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b0ff5c2c-e6ad-38ef-9eb2-22e67997f00f | -3.71293 | -43.77488 | 2025-01-03 04:25:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e7942f0-a8cf-3c6d-bf76-5063fa5536a1 | -1.64651 | -46.13018 | 2025-01-03 04:25:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a640a72f-004d-3032-8ff9-36b60f30bf9b | -2.3027 | -46.41251 | 2025-01-03 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f259af99-8e76-3818-8b9d-ab393d21e00f | -1.77816 | -45.91899 | 2025-01-03 04:25:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c98576a0-c68c-3f14-95e8-368b2fd264a8 | -3.9055 | -47.2074 | 2025-01-03 04:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbf04f3f-91b7-3df0-9db9-26c4b4f09c29 | -1.72996 | -46.10031 | 2025-01-03 04:25:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74949780-c251-344b-a97a-967176c6a2a4 | -4.82848 | -44.02059 | 2025-01-03 04:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df05516f-8279-3ace-bc92-1ce2d1c29873 | -2.29265 | -46.41093 | 2025-01-03 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c38d9c7a-0024-3c82-aeb1-9746c3703477 | -10.48704 | -36.91776 | 2025-01-03 04:27:00 | NPP-375D | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 7535ad6e-e42f-3050-8d8a-e8dad3ddeb2c | -10.2936 | -37.5345 | 2025-01-03 04:27:00 | NPP-375D | NOSSA SENHORA APARECIDA | SERGIPE | Brasil | 2804458 | 28 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e4d250d0-b0bc-3377-ad9e-646190818224 | -11.01289 | -40.86319 | 2025-01-03 04:27:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f1eddd62-2ff0-34cb-952e-ed91e20ce142 | -10.29456 | -37.53595 | 2025-01-03 04:27:00 | NPP-375D | NOSSA SENHORA APARECIDA | SERGIPE | Brasil | 2804458 | 28 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9c3ddf81-912d-3007-ab61-32cc869695f3 | -12.18641 | -41.35189 | 2025-01-03 04:27:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e69931fd-4a75-3f33-abb9-8669e43af49e | -10.98994 | -37.27243 | 2025-01-03 04:27:00 | NPP-375D | SÃO CRISTÓVÃO | SERGIPE | Brasil | 2806701 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 95db1aa9-b9ae-3be2-9b69-faa3eb7430c2 | -12.21674 | -42.44884 | 2025-01-03 04:27:00 | NPP-375D | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2ae25147-acd6-31f8-ab25-a949d91b07e3 | -11.06875 | -45.15864 | 2025-01-03 04:27:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54b8ec13-22dd-32ca-85a1-6358356d3dde | -9.30642 | -41.06002 | 2025-01-03 04:27:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 05573bc4-e010-312d-9e24-2c16e4eab9db | -12.21537 | -42.44822 | 2025-01-03 04:27:00 | NPP-375D | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 054407ad-efc5-3454-a725-c657bc1ed568 | -10.29314 | -37.53823 | 2025-01-03 04:27:00 | NPP-375D | NOSSA SENHORA APARECIDA | SERGIPE | Brasil | 2804458 | 28 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 97e3c1c3-88f2-3c69-a15c-cc42e26b40d1 | -10.48581 | -36.91924 | 2025-01-03 04:27:00 | NPP-375D | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 676e0f8f-08bc-33b8-8a2b-25afe11d09a1 | -10.48633 | -36.91498 | 2025-01-03 04:27:00 | NPP-375D | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 8da2c919-f077-3825-998c-10503c3d66bd | -11.01738 | -40.86383 | 2025-01-03 04:27:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c802554f-3a2b-388f-ac11-527bb97161d8 | -10.59416 | -44.67793 | 2025-01-03 04:27:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6eb0dd5f-e0a2-356a-91dd-f9f3229d4c53 | -12.1858 | -41.35647 | 2025-01-03 04:27:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ef5bfd85-5d35-3d8a-8828-88aff40f3842 | -10.82535 | -45.15144 | 2025-01-03 04:27:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 112f396c-8735-3cad-ab29-05a3f39a559b | -9.19237 | -43.15858 | 2025-01-03 04:27:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b6589a6b-b296-35a1-ac78-2cb9a0b1136a | -10.82284 | -44.37133 | 2025-01-03 04:27:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f71d53cc-9b7d-373b-8ca0-06c838952c2b | -9.1827 | -43.11951 | 2025-01-03 04:27:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7f552c8e-3d66-3d3f-89dd-3dc4fedd1534 | -12.1908 | -41.35271 | 2025-01-03 04:27:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 88b37aac-890a-3add-84c5-6d6b63a4910d | -9.30529 | -41.06048 | 2025-01-03 04:27:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| a3e4aeb7-fc9c-32a3-83be-3e36ee7beb71 | -10.48649 | -36.92202 | 2025-01-03 04:27:00 | NPP-375D | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 94d18226-5c1c-3304-84e2-69bec05519e7 | -10.98822 | -37.27394 | 2025-01-03 04:27:00 | NPP-375D | SÃO CRISTÓVÃO | SERGIPE | Brasil | 2806701 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| bc906d32-f14a-3459-8247-b3d1e950bf40 | -11.06816 | -45.16254 | 2025-01-03 04:27:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 291869a1-16b6-3a20-bcfe-67170a5b5ee3 | -10.28898 | -37.53523 | 2025-01-03 04:27:00 | NPP-375D | NOSSA SENHORA APARECIDA | SERGIPE | Brasil | 2804458 | 28 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6a7b07ba-b5d1-3537-a752-db8797b8a07d | -11.22036 | -41.87239 | 2025-01-03 04:27:00 | NPP-375D | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 26a47c3b-fd2d-3991-8b5d-2c870fc4e2d0 | -20.66015 | -49.99035 | 2025-01-03 04:29:00 | NPP-375D | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3d498cc6-8c7b-3dd5-9714-993c0fc20d84 | -17.60756 | -49.59787 | 2025-01-03 04:29:00 | NPP-375D | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2043a569-f004-3cd8-970f-1fee8b510ff0 | -20.65682 | -49.98975 | 2025-01-03 04:29:00 | NPP-375D | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 50ba65f8-e17c-3ac6-bad5-3ff8e6ce4322 | -17.00943 | -49.78019 | 2025-01-03 04:29:00 | NPP-375D | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1100be25-5f28-3067-8e53-1020bac11bde | -23.98238 | -48.91732 | 2025-01-03 04:31:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df5c1b0c-3d69-34a6-850f-6b45a981eb7f | -28.586 | -49.44032 | 2025-01-03 04:31:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8980afbe-9500-3652-aa1a-7f3ddcde19a2 | -21.81964 | -55.34182 | 2025-01-03 04:31:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c341bf3c-95a5-31eb-9f5b-ba3252990840 | -23.98579 | -48.91792 | 2025-01-03 04:31:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c731a15-b867-3ed9-aa37-8eeffb6987c3 | -21.75473 | -49.55793 | 2025-01-03 04:31:00 | NPP-375D | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 82e5ff3f-3d84-3b7f-9765-76b6ecb2e1e1 | -24.24135 | -50.74004 | 2025-01-03 04:31:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b46eacbb-5934-3fd7-8939-ad1de81e90e2 | -22.662 | -50.66767 | 2025-01-03 04:31:00 | NPP-375D | MARACAÍ | SÃO PAULO | Brasil | 3528809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f3627026-54fe-3108-b3ee-ec4531b74aa4 | -22.53928 | -48.81369 | 2025-01-03 04:31:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f26c0605-e5cc-3673-ab57-03e5e20c3bc9 | -21.81563 | -55.34101 | 2025-01-03 04:31:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2674b2dd-fc36-3ba2-801a-6318c77ab167 | -22.65867 | -50.66705 | 2025-01-03 04:31:00 | NPP-375D | MARACAÍ | SÃO PAULO | Brasil | 3528809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ca45ba90-9dfb-3b46-a719-e83ab7213eb6 | -30.9298 | -52.62879 | 2025-01-03 04:33:00 | NPP-375D | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| e90f5332-f88a-37fa-92c0-18b477d53462 | -29.45557 | -54.06918 | 2025-01-03 04:33:00 | NPP-375D | SÃO MARTINHO DA SERRA | RIO GRANDE DO SUL | Brasil | 4319125 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README6.md)
