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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6a91433-6782-3672-8932-963904a2d34c | -6.13091 | -44.72738 | 2024-10-13 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 91efb9ca-ecb6-392f-a563-dc5e7f07f3a2 | -6.07511 | -44.62986 | 2024-10-13 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9633ece8-4368-3e16-a5ed-7bbfe69d86e6 | -6.07415 | -44.63551 | 2024-10-13 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 72ef9b3c-8587-33a7-b542-7947ea0ae2bd | -6.07006 | -44.05585 | 2024-10-13 03:47:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 39eeaa64-a9af-3e0e-be40-f7a2985ef6a3 | -6.06925 | -44.63457 | 2024-10-13 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c162b306-6487-3e13-8709-85e1308002b6 | -6.06829 | -44.64027 | 2024-10-13 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 085d5dbb-6643-33d5-89ff-cb5049677c39 | -6.06822 | -44.05833 | 2024-10-13 03:47:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5a248c21-90bc-3ea7-9c2a-124d39dc6986 | -5.80853 | -43.97048 | 2024-10-13 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7cc768c2-b905-3210-843d-526cd4f554d8 | -5.57371 | -43.93598 | 2024-10-13 03:47:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8da1b0d5-a66d-3114-99f2-9256ba9bc0a0 | -5.57279 | -43.93417 | 2024-10-13 03:47:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 95125c42-5b88-3db8-9b8b-5ef3bd86f95a | -5.14006 | -43.87866 | 2024-10-13 03:47:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69664eab-b3bf-3ea6-bc98-3ccf5d6e6031 | -5.13586 | -43.87964 | 2024-10-13 03:47:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd3725b1-2adf-3844-b174-41958c3917c5 | -5.89231 | -44.31519 | 2024-10-13 03:47:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5f1f9793-1a9d-31eb-ace5-c579486c9777 | -5.88664 | -44.31934 | 2024-10-13 03:47:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 042822a6-279e-306b-b1a0-2dd8b17f801e | -5.35525 | -44.41413 | 2024-10-13 03:47:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3cde1c8a-8ec0-3ea5-b31f-6364638f3b3e | -5.30811 | -44.3951 | 2024-10-13 03:47:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e81fe701-e5c0-3f4a-9b83-1e94d2fb3869 | -5.16709 | -44.36838 | 2024-10-13 03:47:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d9991088-4a63-3d6d-bd3c-48bb02bef901 | -5.16412 | -44.37001 | 2024-10-13 03:47:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| da9a4216-f8bd-33d7-8901-984508921848 | -6.04282 | -43.62088 | 2024-10-13 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5a59fef-8566-31c4-8b46-2cc8da6492fb | -5.37846 | -43.51377 | 2024-10-13 03:47:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 258550a4-b968-3cce-859f-7a68b1e5e7a0 | -5.37385 | -43.51303 | 2024-10-13 03:47:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f0f37ff2-7fad-39c0-b77e-7b5b4b33f391 | -7.07276 | -43.84745 | 2024-10-13 03:47:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd665299-cf70-30d7-ac34-b862824f0b9d | -7.27355 | -44.96649 | 2024-10-13 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef17de3d-e00f-35e0-8f04-e5f1e004d821 | -7.27253 | -44.97236 | 2024-10-13 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7124c96e-8af7-318a-9324-63a679e265a9 | -6.99992 | -44.70361 | 2024-10-13 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 91d081c2-d317-3157-965f-dd96dc3a8054 | -6.92801 | -45.14582 | 2024-10-13 03:47:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f0445e5a-621c-35e2-bea4-b3cf36441955 | -6.92753 | -45.14861 | 2024-10-13 03:47:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c671062d-155e-33cc-85c9-eff757abb4d5 | -6.92261 | -45.14716 | 2024-10-13 03:47:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 69086dc1-363d-3a59-8f26-bddf3ad211d5 | -6.6836 | -44.62848 | 2024-10-13 03:47:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45e1ebeb-7a05-3379-bc12-34c9b20ec5e9 | -6.53198 | -44.42604 | 2024-10-13 03:47:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cb311b84-0d45-35b9-8ea8-3d1a4bb71234 | -6.52719 | -44.42515 | 2024-10-13 03:47:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e662ad6a-bc66-3e9a-8d2e-e053ea6ddb41 | -7.27745 | -44.9732 | 2024-10-13 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fc3025cf-c6f6-3a17-ae20-ca2335920fca | -10.92989 | -44.67141 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2dea56ea-0345-33e2-be09-f29ccbd4f84e | -10.73213 | -44.69831 | 2024-10-13 03:47:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e9349579-ccb3-3adb-a468-d20ea9861233 | -10.73131 | -44.70008 | 2024-10-13 03:47:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7acad7af-5acc-3e20-b8b6-06b2f8f80de7 | -10.92907 | -44.67605 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9e427ffe-695e-3c5c-8198-d1472b764269 | -10.73586 | -44.70091 | 2024-10-13 03:47:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc0cfab6-f79c-3991-b9db-2509241fa81e | -10.71498 | -45.05222 | 2024-10-13 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ef3d3e0-fc34-302b-922e-a263b63395e9 | -10.03361 | -45.02449 | 2024-10-13 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cdb5c15a-6cf0-35fb-830b-b8db7bdd13ee | -10.92824 | -44.6807 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b225e6af-d591-33fe-9703-01491c02f630 | -10.71259 | -44.49046 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ca3da447-607a-30f9-a07a-bf5c3a513a76 | -10.03462 | -45.02711 | 2024-10-13 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d9df761-1de4-3d7c-8d5e-2990d6b92951 | -10.93155 | -44.66213 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3118835c-e91a-303c-9705-17564862cfbe | -12.32235 | -45.32227 | 2024-10-13 03:47:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9af8a1a-0db0-393b-9590-d17666eb01e3 | -11.93083 | -45.79073 | 2024-10-13 03:47:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03416885-d15c-366e-8a8c-bd5f0c53c88f | -11.92985 | -45.79605 | 2024-10-13 03:47:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f14918dd-d018-3105-9c52-02c715e6e6ef | -11.84395 | -45.12606 | 2024-10-13 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9727e528-73bb-36f9-8f4f-8c2a1a897645 | -11.84372 | -45.12309 | 2024-10-13 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31e04f7f-5089-337a-af29-72559aaa14f8 | -11.83938 | -45.12508 | 2024-10-13 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d4e95b2-fa45-3dc1-b3fc-ce8b4d10354e | -11.1287 | -44.95532 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 117842e2-3600-3558-a6a0-c741c79a1b25 | -11.12409 | -44.9545 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f598419c-1a56-30bc-9123-92ce17577d59 | -11.09893 | -45.91367 | 2024-10-13 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5db2d7a4-f382-3977-9e95-9bc5fb6d746e | -10.94345 | -44.67405 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 9ddd295b-87ab-305b-9209-87c6fb938602 | -10.94058 | -44.66388 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3920cb96-746a-33b4-a43c-a0fcfa0267d4 | -10.93811 | -44.67783 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a6bf922-9cdf-354b-8b29-f5ed8e88151b | -10.93276 | -44.6816 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a934672-31ff-3556-b698-0b651a980f4b | -10.94263 | -44.67871 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e81d3d2-8957-33bb-96b0-b33cd62f441b | -10.93976 | -44.66852 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0d3974bb-f8ed-329d-89f8-6413a850f4cb | -10.93893 | -44.67317 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 22554813-20ad-3914-b1d9-5dec49a41838 | -11.129 | -44.95755 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b1400fb2-1833-3245-a3d6-444510e0e5fd | -11.1244 | -44.9567 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d20fa86a-134a-32fb-bc60-04136fd76cfc | -11.09997 | -45.90806 | 2024-10-13 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a17b1951-122c-359f-981a-464fbe1536ad | -10.95532 | -44.64095 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0b3a9d05-d5e9-340e-8699-7766b993c0a3 | -10.9451 | -44.66476 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 770b90fa-08f8-397b-8058-c66898f21c81 | -10.93728 | -44.68249 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d144d35-2ecf-340b-bc04-e13a93abb9d7 | -10.93689 | -44.65836 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3ee69501-0934-33e8-9570-1d24530cb9c0 | -10.93441 | -44.67229 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e3e06086-b7d1-3324-b425-20048fb3d8bb | -10.93359 | -44.67694 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 490452bd-8484-358c-9ff3-9998ff700ac1 | -11.12524 | -44.95198 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3da07cad-e6ae-3525-9cf6-6994baacae73 | -10.9488 | -44.67028 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| b67d1153-e094-3311-973d-3f25a0e4b5fb | -10.94428 | -44.6694 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| c519805b-8cb7-3f48-bcbd-c2a90466d13e | -10.9418 | -44.68336 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf449a3e-25f1-3edc-b899-efe74ce0319e | -10.94098 | -44.688 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb6feddd-230d-36ca-8fe2-789519c8d703 | -10.93193 | -44.68625 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7d52541-9dc6-317b-aa2b-0fee6532d264 | -3.1052 | -44.5009 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be369cad-5fb3-3901-a233-04c05a2a8dae | -3.10059 | -44.49703 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55f0c4be-1526-3286-9682-eff6ec9bb1cd | -3.10009 | -44.50005 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28941be7-8f19-33b7-830b-f4f525b714e0 | -3.09788 | -44.49743 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b46692f-686d-3377-bed3-991df294a4f8 | -3.09739 | -44.50045 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 73038bce-260c-3614-90ff-c5bab6d2c962 | -3.09498 | -44.49919 | 2024-10-13 03:47:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9132bb8f-0aa5-38d7-8e6b-4223c550bd63 | -4.87909 | -45.76548 | 2024-10-13 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 920fd08d-9fe9-3aed-be76-fecb5a4afe80 | -4.87852 | -45.76882 | 2024-10-13 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdd5b29c-918b-3e5a-8bc3-ffc7aab78e88 | -4.87321 | -45.76728 | 2024-10-13 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba944606-4cea-39a5-af09-3291ac3999e1 | -4.8633 | -45.03989 | 2024-10-13 03:47:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 75224207-ef29-375c-8c45-89fc6da5ac73 | -4.86276 | -45.04304 | 2024-10-13 03:47:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8efeaf4e-c70c-3a2f-aed2-6450d8e8713d | -4.86222 | -45.04618 | 2024-10-13 03:47:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1694a98c-24b7-38bd-829e-cbb655627d48 | -4.86045 | -45.74448 | 2024-10-13 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9270c743-f4b4-3a84-a6af-6f354c4b5c2b | -4.85987 | -45.74783 | 2024-10-13 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d1af780-76db-30ec-91a3-bdc5120e45a3 | -4.85759 | -45.04223 | 2024-10-13 03:47:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| aea6221e-45cb-3c8d-b6a9-a2b9ae58c1e2 | -4.85502 | -45.7437 | 2024-10-13 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c2db3403-1044-3f43-9380-326561b0ecfb | -4.85444 | -45.74704 | 2024-10-13 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3470f37f-da1a-3aa2-98b7-49590cedc493 | -4.85243 | -45.04142 | 2024-10-13 03:47:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 30015b07-f5aa-362b-8e7e-0723346ca7d9 | -4.85217 | -45.85733 | 2024-10-13 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e914a61-c787-3c30-a503-db34c3107862 | -4.85154 | -45.86095 | 2024-10-13 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09e01b86-edfa-30a0-a399-a50ffed0ed47 | -4.84782 | -45.03742 | 2024-10-13 03:47:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 00e06cf1-b577-3a9f-bc7f-6aa9e324f581 | -4.84728 | -45.04053 | 2024-10-13 03:47:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 293b3053-2207-371d-b24a-a53a5835519e | -4.84677 | -45.85614 | 2024-10-13 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e709f774-a28c-32e2-857c-c8656f17ea6c | -4.84613 | -45.85983 | 2024-10-13 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7606983b-ce0d-3713-a6e0-14c2faf2d358 | -4.84174 | -45.67867 | 2024-10-13 03:47:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4aa43a7d-b42a-3e35-99e8-6b5a7687d9a8 | -4.84117 | -45.68205 | 2024-10-13 03:47:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README41.md)
