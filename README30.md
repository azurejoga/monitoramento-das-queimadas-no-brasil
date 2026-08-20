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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6defc7e7-3203-3a3d-a7b7-4c6c7c9cfbc3 | -4.09092 | -42.50631 | 2026-08-20 04:17:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e3851ed1-a879-3b61-82c4-a89e0a736b0d | -2.56774 | -47.24226 | 2026-08-20 04:17:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 4741acca-a085-3b27-99c1-51be3cf9631c | -1.82329 | -47.89286 | 2026-08-20 04:17:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce5ed1c5-6daf-33fe-9d83-5fdcdf8ef19f | -4.00738 | -48.06069 | 2026-08-20 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbe07dc6-4318-3714-8adc-699229b08d94 | -4.79184 | -42.80013 | 2026-08-20 04:17:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 201bac88-99cb-3889-9fff-441d976c224f | -2.1178 | -47.11495 | 2026-08-20 04:17:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5573371e-d1dc-31c1-b65e-6aecb8061571 | -2.32086 | -48.59548 | 2026-08-20 04:17:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 235c4b36-7195-345e-b90c-056250709e21 | -2.80935 | -48.59148 | 2026-08-20 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c3a44e24-cbe2-3bb0-9ed7-cd56e6886742 | -8.65977 | -54.64997 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 5922dcf1-07d7-3043-81da-2fc22a193555 | -6.23987 | -55.40759 | 2026-08-20 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f74f178-0133-3ae7-ac49-9a244fd06243 | -7.83005 | -46.6729 | 2026-08-20 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2fd6a877-f58b-365d-a22d-e3739519a7d5 | -6.35629 | -54.90095 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d742ab3-6f82-3010-b512-a073e617b644 | -8.49752 | -54.86932 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ab56bb94-0cee-3032-97d0-a37fb63f54bc | -5.79471 | -55.71495 | 2026-08-20 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05a8e71c-8596-3f01-92c1-9b60e0ccd0ce | -12.25732 | -43.1547 | 2026-08-20 04:19:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c1b1f0a2-6594-3510-a09d-6b1c6b8885f9 | -11.28357 | -45.78991 | 2026-08-20 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6d9f095-610b-3cf2-924a-913ddfb68e2a | -6.29248 | -43.6435 | 2026-08-20 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0311b2d8-cd94-3fbc-a204-85ee80c70f90 | -6.83638 | -44.9389 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9181f9b2-ab48-3c4b-ac27-758757485e69 | -11.11858 | -47.261 | 2026-08-20 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb5275fe-6d77-3ece-bae6-808251a025f8 | -12.24833 | -43.1682 | 2026-08-20 04:19:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| da681edc-f6f8-3ce9-9839-03bbfb9ab484 | -7.63319 | -42.78954 | 2026-08-20 04:19:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 042af282-706f-3efd-a179-7f0f6f1ea66d | -8.49066 | -54.87269 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5240c6a4-b88c-364f-9e53-a0aa0b9994c9 | -5.95148 | -52.20535 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b3692c4b-29d4-3e50-a60d-ed21b313af78 | -8.71303 | -49.61622 | 2026-08-20 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b3effc8c-4ea6-3158-890a-718bc2137ce8 | -11.81511 | -44.80685 | 2026-08-20 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 70b6d814-84aa-30e0-a658-bc3635c81d38 | -7.96437 | -44.66464 | 2026-08-20 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 9ac3d1db-8f68-3873-821d-1fbf4b48a36e | -9.50908 | -51.63804 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fbda24a7-d91f-3a3e-8499-90e88bdd774a | -8.65709 | -54.60032 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfa13f86-635e-3806-8452-c3893253f581 | -7.21919 | -43.30523 | 2026-08-20 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8f787e9d-bd8a-3782-8f5e-5d27a21b958f | -9.75442 | -43.31461 | 2026-08-20 04:19:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 694071d8-b03d-337f-aec1-cac1a321c418 | -5.79034 | -55.71355 | 2026-08-20 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a92d796-3c44-345c-8062-bd3ee1133985 | -12.19261 | -45.16584 | 2026-08-20 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 644e6679-688a-3d09-897d-3b35daf7b2a6 | -12.24333 | -43.13333 | 2026-08-20 04:19:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 50689918-3464-304f-ac67-f503f81f2a64 | -8.56832 | -54.66018 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 296f4672-9d52-36e4-83c4-35ae2ff9240c | -7.34668 | -45.81846 | 2026-08-20 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9fadaf15-22e4-36c3-875c-406e04f34251 | -8.46815 | -46.96029 | 2026-08-20 04:19:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7d6866a-83b8-37cd-90c3-99935a8b99e2 | -7.75432 | -49.20734 | 2026-08-20 04:19:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4cf78e9f-6e21-3cb8-81ed-d8e3a2684597 | -6.17741 | -39.38354 | 2026-08-20 04:19:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7d420bd9-f2e6-3921-a9c7-7af34361da8b | -6.52657 | -55.05798 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| af8c621d-b8fc-334c-a7c5-4ffa95625386 | -8.54679 | -54.72505 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7d7b430-eef8-30f0-8ccd-e25b76bff6b7 | -8.66404 | -54.65958 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| bbd0311f-85b3-3a68-8ab4-32c0d6fe60ff | -5.95095 | -52.2084 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99d4fcaa-f1b1-3a4b-b673-dbc69e002442 | -8.57574 | -54.78335 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d3bbc935-a627-3890-b36d-d4b71f54c3b4 | -12.45602 | -43.53167 | 2026-08-20 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 220ab46b-14fe-3b05-a48f-e828fa46ab49 | -5.4253 | -43.43474 | 2026-08-20 04:19:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4598de16-ce78-35d5-bde5-197cf3cca5df | -6.34918 | -54.90478 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 501e547f-2cfb-32f3-9f57-841e7180797d | -6.42847 | -52.76334 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 19381cdd-303e-38de-a81f-a8801e239ce8 | -7.96493 | -44.66112 | 2026-08-20 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53127999-03e2-3d66-bc0c-c85529441663 | -6.44194 | -52.7195 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e4926fe-ddca-3124-a9da-2e2c008203f9 | -6.29082 | -43.6326 | 2026-08-20 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb4e65ad-e86c-3027-8ab3-20c08fae728f | -8.53597 | -54.86287 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b56e64ff-e0b2-30f3-b4aa-fcf4718f8a12 | -6.42162 | -52.76117 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e16c7f92-7520-3f05-966e-a4812b4daabc | -11.30458 | -45.00495 | 2026-08-20 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6321608b-3b3e-3f17-86f8-fcecb6a5cbb8 | -7.59858 | -45.17621 | 2026-08-20 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 29aad30a-b9eb-3659-a849-2e92f54ce2fb | -11.28634 | -45.79413 | 2026-08-20 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b2ec26b0-c1af-3643-9acc-64a84dd6bd53 | -6.23126 | -43.70837 | 2026-08-20 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 959bbee8-f580-3e67-929b-c26e90f56559 | -6.23457 | -43.68756 | 2026-08-20 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bda9e7ae-20da-3c05-89de-8fce76a518ff | -8.48916 | -54.87017 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0253486e-ab49-3dea-ad79-62e645cbf7ab | -8.09132 | -51.66977 | 2026-08-20 04:19:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c896522-82fe-39c7-833e-7090186a601d | -10.89974 | -50.27387 | 2026-08-20 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b3c921c-81cf-3d2b-aeac-5168f6433097 | -6.52031 | -55.05683 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cb01aef6-6235-3ff8-8b21-d5cac59d3a01 | -8.66057 | -54.64578 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 2b68bd69-a60e-3dd6-83d5-2c5cbcae7d3f | -7.28702 | -44.07692 | 2026-08-20 04:19:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c3848a6-fb40-36a1-804b-6d1f00ea1584 | -11.3195 | -45.20665 | 2026-08-20 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49a2c387-ed99-3502-a66b-a7874a8344d8 | -6.43468 | -52.72886 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cb7c0141-9e18-3f92-b9ce-14417e085cc7 | -7.60714 | -45.16633 | 2026-08-20 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 307c93b1-60bb-34f8-ba88-517e7bc80c7e | -7.7633 | -49.20498 | 2026-08-20 04:19:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 20ec12f0-6c38-3091-9060-7bcd63e085f3 | -7.7488 | -49.46585 | 2026-08-20 04:19:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a30f968-0923-3399-8fec-4c20c1a4e66f | -8.52313 | -54.86519 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac3b79bd-c705-3ab7-9ac7-a490221dea54 | -6.1699 | -39.38247 | 2026-08-20 04:19:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dac8acbf-67e8-36b0-b6f8-fab976548f2a | -11.38871 | -46.3729 | 2026-08-20 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 35b83e2e-efff-3e90-8a84-fc7578a1884d | -6.86818 | -51.86614 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07fea1a1-c0f4-3342-a513-9974e3860851 | -10.4541 | -54.66502 | 2026-08-20 04:19:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ada0ae0a-d9e8-3bfb-8f83-1e7d8e94c62d | -8.56671 | -54.66868 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9d7318e-a801-3461-a731-13f2ea7576c7 | -7.97218 | -44.65866 | 2026-08-20 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b1ea9f6d-6a2e-3cb7-bf9f-3f8ed94d8b8e | -8.71793 | -49.61311 | 2026-08-20 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6185ac71-6f84-33a8-85c8-b08951aa9615 | -7.35237 | -45.82728 | 2026-08-20 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9a2c8d7f-67f0-32d8-a0c7-ec1aed8a20f2 | -7.96714 | -44.66871 | 2026-08-20 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9b05a0ca-aa21-3a75-b3a3-41c4dbc3c8b4 | -8.53514 | -54.86723 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 77d373d5-e3ae-3fa8-afbd-fd3e3fb15090 | -9.92242 | -48.75778 | 2026-08-20 04:19:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a62ce59f-297d-314f-90e3-97fd85052266 | -9.46241 | -51.59668 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c7a05705-24a9-36ac-8111-077ddef135ce | -11.5819 | -50.5402 | 2026-08-20 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 69077829-e2c6-36d5-83c4-aa2c47c7f00b | -7.61053 | -45.16685 | 2026-08-20 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea1e76e7-1cdc-349d-9ba1-a1bde33131b3 | -8.52057 | -54.87862 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 235e6f5f-eb9b-30b8-903e-a3cfb2af2d0b | -6.71402 | -47.78682 | 2026-08-20 04:19:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85171486-5191-30ba-b021-b671021b0f97 | -8.67908 | -54.6447 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f56b6fc9-ba48-3eca-bb57-9599966bf717 | -8.58482 | -54.73508 | 2026-08-20 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e660a96-9ae9-38d0-88aa-56970619340f | -6.78063 | -42.87704 | 2026-08-20 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 439b156d-dca0-321c-9add-c6d7fab55599 | -7.60256 | -45.17308 | 2026-08-20 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 63e25573-399e-35d4-93b0-025ab0e21a31 | -6.24485 | -55.41271 | 2026-08-20 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27b2e8e5-17d6-3b21-aa8e-4727c1000fbb | -11.31561 | -45.20964 | 2026-08-20 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4285d4b0-2c86-32ff-80b2-f129cbaa0282 | -5.79792 | -55.70914 | 2026-08-20 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa85f071-fd49-38b5-a605-8affa83ec003 | -7.35646 | -45.82402 | 2026-08-20 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 79ada989-8320-30e0-a280-876df13e3ef3 | -10.52282 | -50.78768 | 2026-08-20 04:19:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a7587d81-df39-332d-89da-d95425c0f090 | -6.95242 | -52.81772 | 2026-08-20 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28c050e9-66d9-3d17-aa19-7263045a6ab0 | -5.0039 | -49.47596 | 2026-08-20 04:19:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aadbfb1a-c94d-367e-91a6-8736b495976b | -11.3968 | -47.22235 | 2026-08-20 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6cb07698-4782-3239-b28b-ace6162eda52 | -8.09623 | -51.6706 | 2026-08-20 04:19:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cf627e2-9337-3fd3-ba1c-3487ecfc9f49 | -12.36963 | -46.44713 | 2026-08-20 04:19:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 877a1209-cad7-3265-989c-06aae799a8ad | -5.79913 | -55.7279 | 2026-08-20 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README31.md)
