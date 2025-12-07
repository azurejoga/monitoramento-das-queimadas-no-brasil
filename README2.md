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
| db500078-d107-3cc3-8bba-12a8259a21aa | -4.09021 | -40.83215 | 2025-12-07 03:51:00 | NPP-375D | GRAÇA | CEARÁ | Brasil | 2304657 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4512bc64-6067-3f85-8c70-a67223aa54eb | -7.24463 | -39.17826 | 2025-12-07 03:51:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e12f48ff-c1a7-3389-8077-ce5d9593ddbc | -4.94011 | -37.99922 | 2025-12-07 03:51:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6842bfcf-a490-3796-bb6e-3f5e3ca5934a | -6.94673 | -37.90373 | 2025-12-07 03:51:00 | NPP-375D | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3cbda66e-7311-3380-b2bd-3b77bd40f409 | -4.74382 | -37.87241 | 2025-12-07 03:51:00 | NPP-375D | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 995d3e6a-7ef0-3832-8637-54370d6b39ab | -4.93953 | -38.00282 | 2025-12-07 03:51:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f8f23665-7eaa-3bf6-a001-8966e6607d58 | -3.86015 | -40.64635 | 2025-12-07 03:51:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| daf63451-add2-3316-b408-9a5fba64a014 | -3.56105 | -39.14032 | 2025-12-07 03:51:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 877674e7-de7a-3307-8193-429d6aa30d3a | -6.53664 | -39.19751 | 2025-12-07 03:51:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e6331d86-61c0-37b5-bb8d-6bc9bd11660e | -3.56171 | -39.13623 | 2025-12-07 03:51:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 74cd6506-f4e3-36a2-97b4-5ee10f9e1dd5 | -4.33346 | -40.18724 | 2025-12-07 03:51:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ffdbf541-b146-353a-b449-fadbfedd1977 | -4.33294 | -40.1902 | 2025-12-07 03:51:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d876cb29-0267-3336-bd7c-c9576d7e4ae4 | -8.8103 | -40.82361 | 2025-12-07 03:53:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d2e760e9-8e2b-3eb3-b2b5-768647f1c0a3 | -9.86712 | -37.50011 | 2025-12-07 03:53:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e9137920-e212-30da-b559-bde894f9b303 | -9.87044 | -37.50064 | 2025-12-07 03:53:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 3.2 |
| dd8c7dad-b55b-3b31-a5af-9e394298f829 | -15.61037 | -39.51893 | 2025-12-07 03:55:00 | NPP-375D | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5e109a52-398f-3165-8e50-c6f3252dadf2 | -19.94804 | -43.98295 | 2025-12-07 03:55:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8c55997a-8219-3b36-ab79-b3134bf6c232 | -26.2071 | -51.56328 | 2025-12-07 03:57:00 | NPP-375D | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 767ebfa2-528e-3de2-aab8-d2e26ccad032 | -26.20639 | -51.56637 | 2025-12-07 03:57:00 | NPP-375D | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4fddf72c-0f15-3483-8e6d-8822bcc1a2b6 | -26.20782 | -51.56012 | 2025-12-07 03:57:00 | NPP-375D | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8deab499-3ddf-369b-b8d8-4b3b16280c51 | -23.29137 | -47.09224 | 2025-12-07 03:57:00 | NPP-375D | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 75af583f-d147-3282-85a0-d9f5dc638c15 | -20.72068 | -47.3517 | 2025-12-07 03:57:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de7c91b8-a5d3-3bad-98aa-11e0fed79586 | -23.8007 | -47.82626 | 2025-12-07 03:57:00 | NPP-375D | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 08ad4af2-284b-3505-abb2-be766745474c | -23.80507 | -47.82724 | 2025-12-07 03:57:00 | NPP-375D | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0b96188f-cfbe-3030-b865-cbb28bf6f46b | -23.29471 | -47.09756 | 2025-12-07 03:57:00 | NPP-375D | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b2f085bd-abb2-3709-baf4-a1da5897f2e1 | -22.09562 | -43.17557 | 2025-12-07 03:57:00 | NPP-375D | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 201713b5-4e76-3256-ab75-48b9750f9df5 | -22.02705 | -45.94059 | 2025-12-07 03:57:00 | NPP-375D | ESPÍRITO SANTO DO DOURADO | MINAS GERAIS | Brasil | 3124401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| f80b9d93-b5fe-3b3b-8985-bef7cbe5d66b | -22.91591 | -43.59032 | 2025-12-07 03:57:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 253cc99f-58b1-3470-8e0c-f3be5da14771 | -20.72515 | -47.35282 | 2025-12-07 03:57:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf386381-a60b-33d3-ae7b-11e744e7c7b0 | -22.0332 | -46.98506 | 2025-12-07 03:57:00 | NPP-375D | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7aa8bbf9-ec51-31e4-9c2b-9c378f29da38 | -20.6467 | -47.22523 | 2025-12-07 03:57:00 | NPP-375D | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a5e9130-dd87-360f-8558-a4cc32575695 | -23.29557 | -47.09325 | 2025-12-07 03:57:00 | NPP-375D | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 2764ab05-70c8-3b4a-b0d0-bbb89056a09f | -29.08199 | -50.62909 | 2025-12-07 03:59:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 24679ea4-a035-3243-a0ef-5d9b3db76ae4 | -29.0843 | -50.62478 | 2025-12-07 03:59:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b6132e17-83cd-3c3b-a19f-8cd00e709a54 | -29.08305 | -50.63033 | 2025-12-07 03:59:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b4c6db6b-028d-3ce6-8b99-37db4e657163 | -21.9589 | -48.5403 | 2025-12-07 04:00:00 | GOES-19 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 48.1 |
| c48eb3ee-58c0-39f6-90b8-79ebedd44d20 | 3.45009 | -51.25243 | 2025-12-07 04:12:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 632294cb-5b9f-36e5-bd3f-63feac202cb0 | 3.41552 | -51.25768 | 2025-12-07 04:12:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ec9ef09-3ab0-38f7-98f4-fb4d66c26eb5 | 3.44578 | -51.25872 | 2025-12-07 04:12:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96f4e1cb-5641-3c2f-a2e6-4af6a41a7deb | 3.45039 | -51.24978 | 2025-12-07 04:12:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c9cba23-888e-3c05-b9cb-1546a083a5a8 | 3.3354 | -51.31919 | 2025-12-07 04:12:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c275a45-c7db-30d8-888f-7fe5d63dacbb | -0.80738 | -51.94029 | 2025-12-07 04:12:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af6a49d7-5869-34e7-b77f-d681f1b55d4c | 3.45096 | -51.25381 | 2025-12-07 04:12:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2e3e2d6-22fb-3268-914a-02873753eebb | 3.46133 | -51.24398 | 2025-12-07 04:12:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87a511ae-cc6b-3a8a-b452-63f5cf6ec5a5 | -0.83796 | -48.54988 | 2025-12-07 04:12:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f7e4833-e47c-36b6-aed5-a5fb447bfbc0 | 3.45464 | -51.24353 | 2025-12-07 04:12:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ed8d87b-8567-33ac-9e5a-92ffab5df0b6 | 3.45069 | -51.25644 | 2025-12-07 04:12:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e94c67b-93d4-3796-bf67-ca00065f24cf | 3.41612 | -51.2617 | 2025-12-07 04:12:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a021eb76-dd91-3340-a53c-da8133e09850 | 3.41036 | -51.26258 | 2025-12-07 04:12:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 932831fa-76e7-3911-ac3a-8425883b5eb7 | 3.40578 | -51.2715 | 2025-12-07 04:12:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b71b0d2c-23c1-3633-9fcf-e907fdc34c85 | -0.96883 | -47.49858 | 2025-12-07 04:12:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52a2a60a-612c-3b55-b04b-46bf9c8f6c07 | 3.40519 | -51.26748 | 2025-12-07 04:12:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7e5deea8-c187-3c2e-98d8-81f66d0dea3f | 3.33601 | -51.32324 | 2025-12-07 04:12:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a69846f0-f873-3556-a616-3100f4b097ee | 3.44493 | -51.25731 | 2025-12-07 04:12:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c6fbf95-701e-3d5b-9841-a0f869183ada | -0.80798 | -51.93647 | 2025-12-07 04:12:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d00ece13-9a55-3b92-b3e1-e44161e74c81 | 3.42128 | -51.2568 | 2025-12-07 04:12:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.3 |
| df17c29a-84ba-3c75-a7b0-82b0aa801204 | 3.44948 | -51.24841 | 2025-12-07 04:12:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b5ab14d-e98f-36d7-a0f1-7bfb463cfd0a | 3.41095 | -51.26661 | 2025-12-07 04:12:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2aae3ecd-8f51-3df5-b45d-8b9048f2a87b | 3.45557 | -51.24487 | 2025-12-07 04:12:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6ebc13e-abf5-3f29-8159-cdd6fe17a8a4 | 3.4604 | -51.24265 | 2025-12-07 04:12:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1cee69ee-44bf-3443-92ae-8545c5959786 | 3.45524 | -51.24754 | 2025-12-07 04:12:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a28e099a-3b7f-3bdf-bd10-17e2c79a5759 | -7.64263 | -38.30828 | 2025-12-07 04:14:00 | NOAA-20 | SANTANA DE MANGUEIRA | PARAÍBA | Brasil | 2513505 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c0b558cf-5e38-3c71-997e-061703fabd28 | -3.5627 | -39.14024 | 2025-12-07 04:14:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e42b86cb-ba6a-3c76-8212-93dc77d60add | -3.8617 | -40.64659 | 2025-12-07 04:14:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3b04a092-93e2-348b-85ee-3f6d3a9261de | -4.01681 | -38.32326 | 2025-12-07 04:14:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 25b813ba-3ff2-3ca3-b1bd-9f24cd6b079e | -3.51248 | -52.18604 | 2025-12-07 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79b00d3c-fd02-3c1b-88f6-3dd1bd5b8c4b | -4.33058 | -40.19017 | 2025-12-07 04:14:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3fe88ba4-c7a6-3bd5-868b-767b60cb6526 | -2.96222 | -41.58086 | 2025-12-07 04:14:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 15c7d358-7e49-39d9-9a56-1e9f363cc5c8 | -3.84398 | -47.83352 | 2025-12-07 04:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4be9e80a-561c-342c-ac3e-3a4b96cbefe0 | -3.86228 | -40.64286 | 2025-12-07 04:14:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7188a9bb-c4f2-3730-ad89-8804befe36ad | -2.8021 | -47.57364 | 2025-12-07 04:14:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1335696e-41d3-34d5-b039-e0645bd76be4 | -3.8399 | -47.8329 | 2025-12-07 04:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16318ac8-28c6-37fc-b7c1-c09bc81a38d6 | -4.27748 | -38.05979 | 2025-12-07 04:14:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6f1dd5e9-54b1-3272-8c8b-72e37d84c65e | -3.95609 | -49.3802 | 2025-12-07 04:14:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b5b1dd8-4cb8-3ac4-9b40-8fb736e8d3a0 | -5.24644 | -38.43725 | 2025-12-07 04:14:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a26a5abe-4969-36f3-978b-eafd513b8b21 | -7.64257 | -38.30791 | 2025-12-07 04:14:00 | NOAA-20 | SANTANA DE MANGUEIRA | PARAÍBA | Brasil | 2513505 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b016163e-7a8a-315d-bc88-6f99c8ca42ea | -3.55904 | -39.13966 | 2025-12-07 04:14:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 615d91fe-542c-3de3-b27a-ca98b10d1195 | -4.26248 | -38.05237 | 2025-12-07 04:14:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f5c1bf0c-f885-3dce-b464-a2f74a511e61 | -3.84922 | -47.827 | 2025-12-07 04:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f861b90c-c244-3349-b420-5db5e9156d62 | -3.84864 | -47.83056 | 2025-12-07 04:14:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59dacb72-1c10-3f7b-b330-e2919d4253e7 | -19.94723 | -43.986 | 2025-12-07 04:18:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0c9ae611-0cfa-3924-8eae-25c5c62401f7 | -22.91645 | -43.59161 | 2025-12-07 04:18:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| de261e8a-3361-3040-b622-96a8e6186b41 | -22.03351 | -46.98659 | 2025-12-07 04:18:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0477006b-8fa0-3e6d-a382-f12ab5565263 | -20.91399 | -56.37999 | 2025-12-07 04:18:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5bb54e3a-1cdf-3182-a89b-d0a0a4caa1be | -23.29033 | -47.09132 | 2025-12-07 04:18:00 | NOAA-20 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4be91fa1-1443-32d5-9d76-70bb9be94e5f | -19.80308 | -44.99197 | 2025-12-07 04:18:00 | NOAA-20 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f0917396-fc73-3595-81fe-eee5beb908da | -21.9566 | -48.53774 | 2025-12-07 04:18:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ecde5cf-d8b6-3e6d-bdb9-bf8537921b14 | -21.93987 | -43.16396 | 2025-12-07 04:18:00 | NOAA-20 | SANTANA DO DESERTO | MINAS GERAIS | Brasil | 3158607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8662505e-54b0-341b-9557-f1314ba130c3 | -21.94355 | -43.16449 | 2025-12-07 04:18:00 | NOAA-20 | SANTANA DO DESERTO | MINAS GERAIS | Brasil | 3158607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d3615b0d-52e5-377e-a41e-a8d392b195ba | -21.9627 | -48.54297 | 2025-12-07 04:18:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 088c0024-9747-31dd-85ec-d0c08a1e4193 | -20.91924 | -56.3813 | 2025-12-07 04:18:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1ee7116-0027-3b44-844b-602e899fadef | -20.19969 | -52.9251 | 2025-12-07 04:18:00 | NOAA-20 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30c280f6-738b-32c3-a1b2-1f94fc386da0 | -20.91473 | -56.37657 | 2025-12-07 04:18:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a20442b-decb-32b1-8944-0502163ef993 | -22.0302 | -46.98598 | 2025-12-07 04:18:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef1a6d1c-cbb9-3483-bad9-9a4899ed818c | -20.72095 | -47.35078 | 2025-12-07 04:18:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 19521fa4-4c6b-305d-b357-2f00d394cab8 | -20.19882 | -52.92953 | 2025-12-07 04:18:00 | NOAA-20 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc9bab8c-b5b9-33b4-9e52-338f6e63ff92 | -20.26686 | -46.41087 | 2025-12-07 04:18:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b4967b20-45a5-3250-b267-959564dc0192 | -20.91621 | -56.36974 | 2025-12-07 04:18:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84ae597a-501e-3824-a859-518144c2c794 | -23.29364 | -47.09193 | 2025-12-07 04:18:00 | NOAA-20 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b8fde24b-3c05-3ec4-9d13-4fc0e3189ffe | -19.2227 | -43.99944 | 2025-12-07 04:18:00 | NOAA-20 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README3.md)
