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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93bd759c-bb3c-30b6-8ede-460231217783 | -17.1199 | -56.18807 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| f07c60d5-de84-3246-af09-eca6328ecb0a | -17.11939 | -56.18409 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| a6334daa-2dde-3e44-bc6c-f95d7f1347a2 | -17.11839 | -56.19457 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| a297135d-be89-38a9-b9a3-7de7a66db01f | -17.11793 | -56.19059 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| a68a9e45-3366-3c31-bb97-7acee6b08b22 | -17.11645 | -56.19709 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 285fe56e-cb9e-3077-8034-0d39a23b09ff | -17.11539 | -56.20746 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 1efa8f66-0d80-35f3-8eb3-9e22176d3366 | -17.11465 | -56.18002 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 31710462-d240-33fa-9510-1f0cb9804c43 | -17.11389 | -56.21388 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 72b121e3-1892-36c5-b3f9-a8507217eb09 | -17.11354 | -56.20997 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| fb14edb6-b6f1-337f-99e3-b85fb5f3ea83 | -17.11315 | -56.18646 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 07a4b4b6-68d3-32db-9404-f1850a427b07 | -17.11238 | -56.22037 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 1d11b2d7-a64e-372a-9510-d70eb2a3e727 | -17.11208 | -56.21645 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 43518256-9757-331c-9ded-e8522becee6c | -17.11164 | -56.19293 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 860c5721-5f3d-3682-b9c4-029495564726 | -17.11118 | -56.18893 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 1dcee918-95a9-3efb-b990-a841cc2cacda | -17.06606 | -56.13713 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 6656cc64-6e1c-39a0-aea1-237df6b8420f | -17.02885 | -56.10677 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 180d50ad-5a8b-3e49-a3e5-61825f59291d | -17.02485 | -56.10009 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| f62d83e8-38c7-3a39-8dfe-3606278cb749 | -17.02212 | -56.1051 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 546e90e0-0794-3f68-a7ee-3fff339525c5 | -17.01436 | -56.17095 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 5aedf110-89c9-3c1c-80e5-10815cd3f114 | -17.01289 | -56.17748 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 20307d66-f165-3efe-b11c-8737dee3b2a7 | -16.99497 | -56.16717 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| b86abdbd-b5f4-339c-a8a7-9f27f971513e | -16.99412 | -56.16592 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| cf7c5196-2136-3838-ae1f-ceca3954524c | -16.99264 | -56.17243 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 7cceb9da-8c40-3f89-87e9-52cdfed71d10 | -16.98972 | -56.1591 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| be064fd6-3351-302c-bc4a-a1d0b74e71f5 | -16.98883 | -56.15781 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| fbcfdf06-5350-3403-8ace-e488ce6cc0a1 | -16.98822 | -56.16553 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 3a8c7e40-f2ba-3e69-869d-cca135d93816 | -16.98737 | -56.16424 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 5f34299a-a02d-3ce7-a11c-c33710e485d8 | -16.98669 | -56.17204 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 30f6dc71-510e-37f1-998f-b135a3b6e87f | -16.98588 | -56.17078 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| c7ef02bc-dff7-3218-a48c-aff2268947d4 | -16.98296 | -56.15749 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| e21dea05-2f19-3124-b386-0ef0cce74efc | -16.98 | -56.10943 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b5174f79-1e85-3410-832a-8d3c6e64053e | -16.97326 | -56.10778 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6762f733-436b-34d3-b996-740b600f2455 | -16.71699 | -55.53568 | 2024-09-29 04:04:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 21ff62e8-e7a8-3f4e-8c87-7b405cea5224 | -17.05157 | -56.73085 | 2024-09-29 04:04:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| b63dae97-40bd-39fd-a788-6fe140a3bec6 | -17.04995 | -56.73782 | 2024-09-29 04:04:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 8089aa5d-378a-3850-a25d-b34af783d609 | -17.04949 | -56.73042 | 2024-09-29 04:04:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 26ea0442-80f4-32cf-a0a1-ac6584cd9bf1 | -17.04782 | -56.73739 | 2024-09-29 04:04:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 9dab159d-1273-3be2-8109-8c0e37c55faa | -18.62583 | -40.00661 | 2024-09-29 04:04:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 60dafdd3-4528-3016-bf23-d63833470d28 | -14.51104 | -39.73645 | 2024-09-29 04:04:00 | NOAA-21 | IBICUÍ | BAHIA | Brasil | 2912301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fb49b9fc-1eab-38ea-8ea9-711784fa0bd9 | -14.23755 | -39.8779 | 2024-09-29 04:04:00 | NOAA-21 | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 74edf66a-86f1-3b6b-a6a5-a6f2771d0ad1 | -16.12133 | -39.62326 | 2024-09-29 04:04:00 | NOAA-21 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5425eb18-9281-3b7d-9996-e4eb576a9a63 | -16.95217 | -40.76226 | 2024-09-29 04:04:00 | NOAA-21 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9708021b-4af2-397c-be94-7ed9652758ea | -16.95072 | -40.76214 | 2024-09-29 04:04:00 | NOAA-21 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ea222a32-4b9a-3c92-a27d-2a66994a90e2 | -18.54665 | -41.34483 | 2024-09-29 04:04:00 | NOAA-21 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 0ac00865-0be1-3d6b-a7e5-acc5a193198b | -18.54329 | -41.3443 | 2024-09-29 04:04:00 | NOAA-21 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| d5c7bac2-c20d-3856-8fc5-331cdd1ed10a | -18.54216 | -41.32882 | 2024-09-29 04:04:00 | NOAA-21 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| bb0a5bbb-099c-314f-9b8f-ce191b7ec7dc | -19.43421 | -40.78815 | 2024-09-29 04:04:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 48cc95e0-7882-3df0-9309-d176bd02ab22 | -19.42577 | -41.36914 | 2024-09-29 04:04:00 | NOAA-21 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 25081add-0ba4-3c31-80a9-a198e9d4cb33 | -19.34489 | -40.84711 | 2024-09-29 04:04:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 740de309-50e3-3fca-b590-a806e35b9c39 | -19.18722 | -40.33136 | 2024-09-29 04:04:00 | NOAA-21 | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 187c39e4-4905-3beb-b0d8-5dd40e322f8c | -18.94625 | -41.27711 | 2024-09-29 04:04:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 63ac8e54-5750-3b76-890b-b40a34a9ca00 | -20.18216 | -41.6856 | 2024-09-29 04:04:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 824d3919-3c77-316a-8f4d-30c6ea9a8069 | -20.18103 | -41.68158 | 2024-09-29 04:04:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 02d1d620-8953-37ff-8a55-4ed09d6934d7 | -20.18047 | -41.68537 | 2024-09-29 04:04:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 662ae7d2-3c89-3b50-9b20-a22fd00ab8f5 | -20.16212 | -41.62351 | 2024-09-29 04:04:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 235a1e99-24d7-33d7-93df-ea3ac0e6ce40 | -20.15875 | -41.62294 | 2024-09-29 04:04:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6b90567c-3c14-3ad8-a248-ec65549b0a87 | -20.15818 | -41.62676 | 2024-09-29 04:04:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4b6a2518-4c97-3cc8-bdac-c212607b0f73 | -20.15538 | -41.62236 | 2024-09-29 04:04:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 7b45634f-570c-3a13-9b9e-6b7d33eb429c | -20.15481 | -41.62619 | 2024-09-29 04:04:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4476d75b-a7fc-3cfc-b030-4e1dd5997ee5 | -19.93728 | -40.74265 | 2024-09-29 04:04:00 | NOAA-21 | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 95816a82-3660-3af6-b3b0-a32e9f5c6f8f | -19.93671 | -40.74664 | 2024-09-29 04:04:00 | NOAA-21 | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fab521e2-fb10-3dd0-af33-d437f5453d87 | -19.93613 | -40.75067 | 2024-09-29 04:04:00 | NOAA-21 | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b3696383-d35d-355f-8a26-f60cc60dd672 | -19.93384 | -40.74199 | 2024-09-29 04:04:00 | NOAA-21 | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a12a1182-0a3f-3f85-a67f-2fc704e75943 | -19.93326 | -40.74601 | 2024-09-29 04:04:00 | NOAA-21 | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 23b97d87-5f13-318f-90e1-3c4f573a5efd | -19.74895 | -41.61888 | 2024-09-29 04:04:00 | NOAA-21 | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a4f84ee1-676d-3161-88d9-2dcc776f2553 | -19.74839 | -41.62265 | 2024-09-29 04:04:00 | NOAA-21 | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6a738690-014b-33dc-8888-ca00ce73897e | -19.74559 | -41.61831 | 2024-09-29 04:04:00 | NOAA-21 | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d8bafffe-a359-3f53-b24c-f1a073719ae8 | -19.74503 | -41.62209 | 2024-09-29 04:04:00 | NOAA-21 | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 869164f7-0ce9-3d24-bb93-b0ee97f3380b | -19.74223 | -41.61774 | 2024-09-29 04:04:00 | NOAA-21 | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 12cbabd0-1cc4-30f6-94f2-c9999267e10e | -19.74167 | -41.62153 | 2024-09-29 04:04:00 | NOAA-21 | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bbd99706-db29-39c9-a0f1-d2f1e0f97b5a | -14.32598 | -41.71673 | 2024-09-29 04:04:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c899e704-eb97-3c24-9838-7692a2430ab1 | -13.89931 | -41.66097 | 2024-09-29 04:04:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 62dd0258-45d8-39a3-ada4-d9b6d8988277 | -13.89876 | -41.6645 | 2024-09-29 04:04:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 1d021e25-dd3c-3c36-85a9-69c8cf20d96a | -13.89601 | -41.66043 | 2024-09-29 04:04:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a15ecbac-a7ab-3a48-8587-dbc7e03083f3 | -13.89546 | -41.66396 | 2024-09-29 04:04:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bdca6266-4239-3733-a60d-d403ae1cb965 | -15.83737 | -42.16525 | 2024-09-29 04:04:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.8 |
| 6cb29f0f-1365-3f46-ab6a-f00bdab62766 | -15.83681 | -42.16882 | 2024-09-29 04:04:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.8 |
| 1137e3f8-0f79-380a-bedc-4cbac4c7a92d | -15.83407 | -42.1647 | 2024-09-29 04:04:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.8 |
| 3766fed2-f6f9-3d20-a140-ddce841c5437 | -15.83351 | -42.16826 | 2024-09-29 04:04:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.8 |
| 3575c40b-3bd3-317f-91a0-4874ebe8f19e | -17.67925 | -42.74174 | 2024-09-29 04:04:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03fb86ed-4ec5-371a-9264-a5aae7249365 | -17.38616 | -42.65844 | 2024-09-29 04:04:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f642a732-2762-345c-93c1-c4b15f81c0a9 | -17.98185 | -42.30823 | 2024-09-29 04:04:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d2fe323e-f377-3f14-bf3c-75fda8931c31 | -17.93361 | -42.13709 | 2024-09-29 04:04:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 97ca8d47-73f0-3faa-90a8-638dbe83e88b | -17.90657 | -42.13632 | 2024-09-29 04:04:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4f5de622-bc0c-360e-b3e6-12332ff3b0c1 | -17.90326 | -42.13576 | 2024-09-29 04:04:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6628d0ae-3318-366d-b0ce-7d4d0a3cded6 | -17.89995 | -42.13521 | 2024-09-29 04:04:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| eccdd13b-73f0-3aff-bd34-6835a8273b1a | -17.89939 | -42.13884 | 2024-09-29 04:04:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d5aaf159-87cd-3182-95c6-a6d6dca30ec0 | -16.7698 | -41.72549 | 2024-09-29 04:04:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d1190429-54b8-3cb1-a07e-c8e4b44e1cca | -18.5581 | -42.99258 | 2024-09-29 04:04:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 13472ca3-1d8b-3cf2-b992-42e263f08ec9 | -18.3986 | -42.79805 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 553bb776-6baf-3217-a471-f682003634f6 | -18.39803 | -42.80166 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2595fa2f-bc36-3ffc-84b9-b030b79cb038 | -18.36921 | -42.76682 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 1cb6e3d0-fb02-3f01-9fbf-46f31af9442f | -18.36591 | -42.76624 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| f5985f91-ee08-3b59-8eca-65ffcc494281 | -18.35714 | -42.75732 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5b6d04ea-a711-3ce8-9f41-2a628229d3be | -18.35658 | -42.76093 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| be0cfcf5-838c-30ec-a605-d3a6a6830932 | -18.35384 | -42.75675 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 62771a31-a322-3830-b2a0-4e2ed74980eb | -18.35327 | -42.76036 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 60d0cee7-ac1c-3110-8932-23dacdf3175d | -18.35271 | -42.76397 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 894e4885-a034-34d9-b492-d067955b1ba1 | -18.35214 | -42.76759 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 41aec045-2d04-3a3e-a03e-c84ffea64463 | -18.34883 | -42.76702 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |


[Clique aqui para ver as próximas entradas](README32.md)
