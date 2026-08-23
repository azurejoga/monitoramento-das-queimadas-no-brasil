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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98c05621-5217-3ea8-8d9d-f8372ce11122 | -8.38052 | -47.39175 | 2026-08-23 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b95aff1c-f092-3a6d-954f-172d8c853f5b | -2.35251 | -48.83531 | 2026-08-23 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 534974fd-c311-3c23-b3b0-214a6fbb376b | -3.70539 | -53.68695 | 2026-08-23 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2e3ee82d-c39a-3872-8dab-96769f501bbc | -4.30574 | -46.4192 | 2026-08-23 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be7e3036-38a1-3832-ae7a-ab848111c6cb | -7.2586 | -49.87245 | 2026-08-23 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a3b03a34-837c-3392-8c27-c1c5e4dfb3ab | -6.90276 | -55.70524 | 2026-08-23 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 051bf325-7e46-3666-9e0e-bf47e8d4dee8 | -8.96444 | -50.75175 | 2026-08-23 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 19bc6b0e-849f-3e5e-9893-17aa914f4ca5 | -3.703 | -53.6851 | 2026-08-23 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8e149065-575b-3ef4-a1cb-53b3b4e0e2d7 | -9.4521 | -40.32687 | 2026-08-23 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| f5da9d0a-1672-3e58-82fd-7f22c47ef7e0 | -6.19904 | -53.53131 | 2026-08-23 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9f2dabe1-c1a0-392a-8e51-dc4467bf452a | -4.16875 | -42.44528 | 2026-08-23 04:08:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3378853c-1da3-38cb-aee9-549cd5299729 | -9.02315 | -50.73686 | 2026-08-23 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cf60a8c4-39a0-3027-93a5-f1eec48d41dd | -7.76129 | -39.21733 | 2026-08-23 04:08:00 | NOAA-21 | CEDRO | PERNAMBUCO | Brasil | 2604304 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ad016a91-a686-3c4c-83cd-1d8d5e8575ab | -7.08596 | -45.01598 | 2026-08-23 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e1deca3-91e8-347c-81dc-a7372263bdb5 | -3.44433 | -39.56145 | 2026-08-23 04:08:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a648630e-0ffa-3101-bdeb-8de87de46f65 | -6.89828 | -51.56597 | 2026-08-23 04:08:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f547a28-be49-3a88-ae41-62d67c2c353f | -8.96342 | -50.75752 | 2026-08-23 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 42c1cd05-014f-3e5c-b6d0-cf44feef0c26 | -2.5678 | -47.24493 | 2026-08-23 04:08:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4a2a2771-49d6-33bc-9195-1e8f465610ca | -7.47647 | -45.13098 | 2026-08-23 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4c339fb2-4972-3659-b519-7b82ecc1c98e | -6.79463 | -42.67841 | 2026-08-23 04:08:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9bd73840-69a9-34ad-a231-34581d0d1fa8 | -8.46149 | -46.99441 | 2026-08-23 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f3432c49-bae3-3a3f-8dcf-1d5fd845c478 | -8.09806 | -50.05424 | 2026-08-23 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b23ab7e3-a089-3486-a26a-d57ce6c1a649 | -6.19546 | -53.52768 | 2026-08-23 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ee3b7696-1b36-3208-b3f8-92bcbbf068a8 | -7.14565 | -43.1016 | 2026-08-23 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 32ab412a-33f7-3c9a-a05d-bf86e059a3d2 | -6.38196 | -54.96135 | 2026-08-23 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7fc7dcbc-0be8-3609-bbaf-3cc79acac7f1 | -8.98413 | -50.75888 | 2026-08-23 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3d268b66-2821-33ae-a754-430714c90f3a | -3.379 | -39.2039 | 2026-08-23 04:08:00 | NOAA-21 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ec0d2b23-893d-3178-b978-c40a8e8dc0b7 | -8.96393 | -50.75467 | 2026-08-23 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b5cbee49-8eaf-30af-9f18-8a69545c2d1b | -8.96291 | -50.76038 | 2026-08-23 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e105e154-37a6-33e2-9dfa-3a37ab3653a6 | -7.1816 | -42.74706 | 2026-08-23 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0ed68688-b295-3115-ad79-cb9ab3397825 | -7.26842 | -44.19956 | 2026-08-23 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28bd422d-d471-3954-9aa8-ee06cba58e63 | -6.78462 | -42.67685 | 2026-08-23 04:08:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ae772748-eb2d-394c-8716-40eff8f31859 | -9.78978 | -46.61979 | 2026-08-23 04:08:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 695f581d-4b67-3f50-ac8e-3f73e767c12f | -6.38176 | -54.96258 | 2026-08-23 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 523a7f97-58b6-38db-9fa4-b9009dd01a1b | -4.1693 | -42.44172 | 2026-08-23 04:08:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ddacf3ec-7759-340e-8bf7-b497f925389c | -7.48878 | -39.96062 | 2026-08-23 04:08:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 12c1ca0d-3755-3333-a29d-2d95e12f9b25 | -7.17993 | -55.42 | 2026-08-23 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3d242a47-3dfb-363e-930d-59606bcbb8fe | -7.30193 | -42.99861 | 2026-08-23 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b2680d5e-464d-3f9c-ab1d-ca44d6f6e3a6 | -6.92111 | -46.40852 | 2026-08-23 04:08:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e749378-4b6f-327f-8579-6f8d9abcdfef | -8.99296 | -50.75883 | 2026-08-23 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8188b0cb-4bfe-3e41-a72f-580637405490 | -2.9901 | -48.96039 | 2026-08-23 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b7e8a873-2758-3fee-937f-762de0dfed9f | -4.17267 | -42.44223 | 2026-08-23 04:08:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 6a82f306-65af-3856-ace2-04bfd2cf9f27 | -4.17602 | -42.44276 | 2026-08-23 04:08:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| a98c12b0-c4c8-3d93-b6a2-f2234f90bf69 | -7.2627 | -49.90734 | 2026-08-23 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8cf8a791-4c73-3305-8599-5e42c13ef72f | -8.811 | -46.61899 | 2026-08-23 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33482106-f370-3213-8d81-936d0e0905cb | -5.96193 | -53.62906 | 2026-08-23 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 560d505c-97a0-3bfc-a472-893e2c970f03 | -7.47944 | -45.13555 | 2026-08-23 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 159c02c2-9605-38bb-985f-4ddf2cbdcbfe | -10.01796 | -44.28435 | 2026-08-23 04:08:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f69b805d-04ce-31b5-a944-e6f951a533e1 | -6.51573 | -51.45224 | 2026-08-23 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2931d0f-7542-37b0-a8c3-8b4e0b1a3495 | -6.19643 | -53.52247 | 2026-08-23 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cca97c47-f6bd-30fa-9780-24348d28148c | -7.14901 | -43.10212 | 2026-08-23 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 45f88c73-5e38-38ea-8925-b7a19942760d | -6.20182 | -53.52876 | 2026-08-23 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c36667ab-4501-37f7-a8f2-05fea922087a | -8.08903 | -47.26325 | 2026-08-23 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3aeaa8d4-110a-32a1-b4d0-ff20cdc463d5 | -6.77793 | -43.08756 | 2026-08-23 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42c70b2b-a3f7-36d4-9f7a-feb828f1c230 | -5.95213 | -52.12643 | 2026-08-23 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5232dc00-c46c-30c6-a1a6-f8305951c49d | -10.45538 | -37.14928 | 2026-08-23 04:08:00 | NOAA-21 | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| cf2593e4-2a7f-3156-9535-13e6abac6c57 | -7.81571 | -42.15458 | 2026-08-23 04:08:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7c8ea3b4-e025-3c81-9f03-296bef1143a6 | -2.45792 | -49.28919 | 2026-08-23 04:08:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d8c763f-720b-3227-b952-862fb0e9cce6 | -6.3796 | -54.97426 | 2026-08-23 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b3e5f3a7-6dd8-32f5-8cba-89438c330d3a | -4.1665 | -42.43763 | 2026-08-23 04:08:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 86cb92e8-ba18-3c44-8620-e7fee30217b6 | -6.1927 | -53.53016 | 2026-08-23 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 97f27e6a-0d9c-3831-85c3-5300d7a3664e | -7.73955 | -46.14241 | 2026-08-23 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b5bb503-d980-3d06-a5f3-451c6cdfface | -8.98234 | -50.75961 | 2026-08-23 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 63ce9ff9-6d35-37a3-8aee-d3af0b909181 | -6.92078 | -46.41146 | 2026-08-23 04:08:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a2f07ed4-8380-3319-9afb-d41930991a53 | -9.53614 | -43.00232 | 2026-08-23 04:08:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| eea1aba2-9ccf-3998-a583-583e98d50a78 | -8.58216 | -45.54927 | 2026-08-23 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 559338d5-4b9d-3178-82b9-b3a2420a5616 | -8.46206 | -46.99108 | 2026-08-23 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e060aba-1b7b-3f1d-816e-2713b829d56e | -7.75615 | -46.18404 | 2026-08-23 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85f8cbff-ff27-3483-824a-53488eeeb567 | -5.81483 | -46.61784 | 2026-08-23 04:08:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93d05d2a-253a-3173-bf65-8eea7acd8980 | -9.45104 | -48.23657 | 2026-08-23 04:08:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 08744589-d6bc-373f-baaa-033c8815325d | -7.1516 | -42.78927 | 2026-08-23 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a7c4b814-3cb9-3660-abd3-c9403d57e60c | -8.98284 | -50.75689 | 2026-08-23 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1ff66f09-dfb2-3739-b384-c0e9b9c966e3 | -8.08559 | -47.25887 | 2026-08-23 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| afabebb3-1b79-35b4-89c2-769bc771c83b | -8.92616 | -48.5407 | 2026-08-23 04:08:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3f90499a-a51c-38c3-8b4e-383d500fb059 | -2.45842 | -49.28616 | 2026-08-23 04:08:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bee64a66-c93d-3633-aeb0-8c60c7b0df8e | -7.57002 | -45.2016 | 2026-08-23 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| faddec75-b142-32d5-a8f8-fbca7a524128 | -7.08737 | -45.00736 | 2026-08-23 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1e71912c-d390-34c7-8e19-f3bf4334adc9 | -1.61208 | -54.40059 | 2026-08-23 04:08:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| af904d5d-5837-31b1-a118-c0ef28405422 | -8.97906 | -50.7579 | 2026-08-23 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6e1888d0-e33d-3546-b332-903cb6c0c020 | -6.37558 | -43.23837 | 2026-08-23 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8caa015-152f-3b10-8dc8-4f22748439c4 | -7.48896 | -45.14551 | 2026-08-23 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c825100-ddd3-38e6-a5f8-da862251980b | -9.63677 | -48.31773 | 2026-08-23 04:08:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1286d272-6d78-3969-b28f-2fa5b7bc9f84 | -3.01133 | -51.05589 | 2026-08-23 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5dd74148-0762-30ff-9b67-e9be49a47df1 | -5.95134 | -52.13081 | 2026-08-23 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47ee5809-c936-3514-b95e-94c03cfd683a | -4.95187 | -43.46812 | 2026-08-23 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75a5745e-e7f2-330d-b86a-0f9b23f7ebd2 | -7.14882 | -42.78522 | 2026-08-23 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b43d9a68-117d-300c-bd29-d8ba2cdb05f2 | -8.3471 | -46.50579 | 2026-08-23 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d6a57ea-f09a-3321-8b1c-3a8d14d9375f | -4.16539 | -42.44476 | 2026-08-23 04:08:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| dcf329ce-03bb-37e6-9136-e15144181ac1 | -7.74242 | -46.17211 | 2026-08-23 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6257a4cf-c549-3091-8f56-ad6c5a7a5341 | -7.64412 | -42.72742 | 2026-08-23 04:08:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d9b0a7f9-2304-311f-b34b-de295c2bc086 | -10.01515 | -44.28008 | 2026-08-23 04:08:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 332ee3fc-7bc3-3811-b3db-7989d969dd55 | -6.79964 | -42.66833 | 2026-08-23 04:08:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6bcea9e9-d8a2-351a-89e6-2b935ede3ea0 | -7.13008 | -44.54411 | 2026-08-23 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e061d986-851b-30d5-a316-e7063f232322 | -7.26727 | -49.88096 | 2026-08-23 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c42a9d4d-aaa6-396a-aa88-51d7295ed60a | -5.7816 | -50.19267 | 2026-08-23 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56a59477-21a8-335a-affa-1ee9866c7d12 | -5.61129 | -51.78954 | 2026-08-23 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66a6612e-4f17-30dc-8f29-9398ebe0d164 | -7.78028 | -42.90031 | 2026-08-23 04:08:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b88be37a-0d91-3963-805e-ed59784940a3 | -9.45033 | -48.24056 | 2026-08-23 04:08:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d2da6aa9-c9c5-3d10-b0d1-daa5a1735b49 | -7.3014 | -42.9803 | 2026-08-23 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0ffd091d-bd42-3d0f-bd99-a5295ee878ee | -7.15715 | -42.75405 | 2026-08-23 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |


[Clique aqui para ver as próximas entradas](README12.md)
