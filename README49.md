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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f8e33c6-91bd-3262-a570-c5cba9200c9e | -11.10074 | -48.28246 | 2026-09-22 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 86570843-58f1-3178-9c4e-a2eaae3e529f | -6.44242 | -48.45775 | 2026-09-22 04:46:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0fea2d3-b925-38b5-97b8-1a2849b54fea | -8.26546 | -55.30511 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8e66684d-18e4-331e-99d4-fef9e1077ffb | -3.44597 | -50.65866 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e492d2e8-5e5b-36fd-a049-15c5c31938c1 | -5.9771 | -57.78573 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96d0e2cb-40d8-3527-9547-92d3f759e0cf | -3.71667 | -60.57519 | 2026-09-22 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 31476ddd-550e-3f7a-9778-57647bb3baca | -5.38029 | -55.90824 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 29d40800-4e0c-3e37-948c-f798a3261874 | -7.23992 | -55.6017 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ea53e660-34cd-3631-b3ed-58b02272c219 | -6.39062 | -60.02143 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b4d85d8-4df5-3ea7-8e09-500bf3784cef | -9.62599 | -43.94049 | 2026-09-22 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 6e12c992-0737-3dc9-b2ce-614b5f8efc01 | -8.2662 | -55.30067 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c699d1d1-0cf1-395e-8545-96ef3815f1bd | -6.9896 | -52.85365 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a14ed6bd-00d9-39af-88bc-c2018e7d05a1 | -9.29661 | -58.91266 | 2026-09-22 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f799b075-5c1b-3ead-b128-2e2d1c2e71d5 | -5.45627 | -60.14756 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81241e9e-feef-36dd-8ed5-720c2bda564f | -6.05394 | -57.82222 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0ba7cb07-2a09-3945-a079-9baaf423f491 | -6.13736 | -59.95094 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d79337b-043a-3515-a5e7-5e4f79ba956f | -7.56542 | -57.68074 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 02552dc5-29e0-38c1-81b4-170a9626e826 | -4.18477 | -51.24006 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9ca58ffd-b6c7-3a43-b92e-e496390b0f4e | -5.93747 | -53.52418 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1f2bfb9-e750-3a0c-a0e3-af3fd19443ab | -9.55842 | -46.55182 | 2026-09-22 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48386d34-4116-3a21-9d5f-8ed7421c1235 | -9.61767 | -43.92797 | 2026-09-22 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f87e1212-24d2-332b-bb0a-5517816315d2 | -4.95941 | -55.82374 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e10ecd5-9e17-34b5-a797-96bcf3f35afa | -3.58655 | -59.06412 | 2026-09-22 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38e2681b-fb5b-36a9-b790-b48c3d135951 | -2.56194 | -54.74126 | 2026-09-22 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f56a2c8-1c8d-3536-82c4-c1b1ed9f93fa | -11.38716 | -46.78624 | 2026-09-22 04:46:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e6db6659-4c56-309f-a337-c03b1dad8657 | -6.46508 | -59.99178 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 2c8e3d25-027a-3841-9fc8-29af042e5175 | -6.75342 | -56.32453 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48bdb555-eed9-3b96-b891-28a0a0f08b57 | -5.84921 | -49.79151 | 2026-09-22 04:46:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53224a89-8527-3b4a-80b2-0c1401ed3267 | -5.80615 | -53.5198 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2bc7b041-ada4-3874-b2f3-0339051b69ac | -6.80995 | -55.83235 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80c9a057-9614-3ef2-9c1c-0da680991094 | -7.13536 | -42.07968 | 2026-09-22 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 85b6d39a-1764-3b37-ba7e-420569b88b70 | -2.96473 | -52.14479 | 2026-09-22 04:46:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99a20e08-9c56-3094-927d-a15461acdae5 | -4.05572 | -56.31083 | 2026-09-22 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ae20748-fc9e-39f3-a31b-2ad41dad0cf4 | -5.99034 | -44.7236 | 2026-09-22 04:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 35ccd280-7d05-3025-9454-da190a432671 | -2.93206 | -57.79877 | 2026-09-22 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7aa84f27-e943-31a3-9bed-eed9ce74a37b | -7.13491 | -48.42799 | 2026-09-22 04:46:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 518afc88-10f1-3d63-ac36-a12f46e62f21 | -6.42156 | -55.02274 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 994c8c53-8e11-32e7-b334-fc7350b542c4 | -5.91278 | -51.95842 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1cbb62ee-0024-3dfc-83f6-c222feee8364 | -6.90311 | -42.95505 | 2026-09-22 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c3b8c409-a617-3e5a-a596-1d0cf378e603 | -8.32098 | -44.74393 | 2026-09-22 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1ebd75e-8fe5-3c66-bf2e-6f9a5ceda893 | -8.79272 | -44.27919 | 2026-09-22 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| b47134c3-9da2-3ce5-b53f-06b4757e4ed5 | -7.39255 | -44.78729 | 2026-09-22 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2bd46d2-16db-3d09-aabe-676e74840310 | -7.82988 | -44.9717 | 2026-09-22 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2121a5c-4dea-3bca-b929-6d3e44f5d89c | -8.15042 | -54.79889 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9cb68354-b536-3b60-8640-25598b405524 | -3.6855 | -60.56819 | 2026-09-22 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 27f47d3a-c24c-3d17-a4cc-d88f55f840c9 | -11.38704 | -44.22995 | 2026-09-22 04:46:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c33a25ba-eb3b-30c0-b415-b8123af04ac1 | -10.56373 | -46.72673 | 2026-09-22 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0da058a-2c01-3998-bac5-ad14f053ba40 | -7.40008 | -55.22483 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7a0e94f-9e3a-3bd4-b48f-09608e88933d | -2.56993 | -57.50748 | 2026-09-22 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3a44b4db-9b8b-3354-810e-95dce4f1d7e1 | -10.86456 | -50.16027 | 2026-09-22 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3bb81a5-d1ce-344d-8755-4f775a432616 | -4.4824 | -55.49165 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f39fcc62-ff2f-30dd-99a7-f19fd28761cd | -8.80401 | -48.75994 | 2026-09-22 04:46:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04c3ad38-a073-39c5-9e39-2e73a7f480f9 | -8.25149 | -55.2528 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18f79756-18d4-31e7-b00b-a01a6cde393f | -11.10805 | -48.31242 | 2026-09-22 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 89434951-f362-3759-a047-0c577751ce38 | -6.43445 | -55.61493 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f46d0b28-02cc-36bc-85f9-e1826ed47c13 | -9.87913 | -55.85888 | 2026-09-22 04:46:00 | NOAA-21 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0ea69db-d68b-3242-93b9-1f2df50f0bd9 | -10.76165 | -50.72952 | 2026-09-22 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| abe5c699-83d7-3d03-9871-42f94847d31b | -7.56228 | -55.01894 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e43a9f8-8045-3c4d-a6ce-3f42b576f6b0 | -3.8308 | -51.19842 | 2026-09-22 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 326e5bad-5409-3ecc-ac4b-925c7efff864 | -5.8729 | -53.64976 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 740e55d8-d3d2-30e2-ae7a-d6a769582dd2 | -6.91993 | -55.60942 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f2b1a30-de87-313a-bf8e-3ce8eb5273b2 | -3.06623 | -59.28099 | 2026-09-22 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87b4658d-b3db-38fb-a882-22d4d7b7f765 | -3.68465 | -60.59328 | 2026-09-22 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3135503-e752-3da7-90fe-1b93434ec229 | -5.9076 | -51.77542 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e5d460c7-8f19-30ce-9723-12516c1fe1fd | -10.68818 | -48.7161 | 2026-09-22 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d23b5956-110c-36be-acb3-08fd734a7ca6 | -6.58164 | -44.15813 | 2026-09-22 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 52386c20-a9f9-3572-a3c0-1fda4857203d | -3.47206 | -59.5325 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 707948f5-2d8b-38cc-ba3d-3a68e961b826 | -3.41726 | -60.20127 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66e78dc5-208a-3932-9fc6-c0a4c84b63c2 | -6.59564 | -39.14327 | 2026-09-22 04:46:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 2c0c084d-9628-3908-b0ef-471442c99c4a | -9.29273 | -44.37769 | 2026-09-22 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 991b0faa-1e51-31b5-8e5a-1630b2651fec | -6.09025 | -55.55534 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f27b2e39-1791-3f13-9fcd-78c0a59592bd | -5.87353 | -53.64584 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7fdf37a-c172-3f70-be3d-dc6a29e7f90f | -4.20506 | -59.91327 | 2026-09-22 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03191267-b07b-3906-aa24-b05d1295dc52 | -6.35216 | -55.75212 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d5170d5-5e20-39b8-ab7c-7af4dba09dd6 | -7.19416 | -46.55649 | 2026-09-22 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| efa58c7e-4356-3665-827e-329126b61aa6 | -6.02484 | -45.41888 | 2026-09-22 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e49faea9-8feb-3d4e-95b2-8505104ada8b | -4.38541 | -55.02733 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d409698b-d342-3c06-a17c-d9410c7e3979 | -8.19147 | -54.72872 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8efddafd-3939-3d83-96c4-2ae97cf97a79 | -9.28564 | -46.18841 | 2026-09-22 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 119aab0f-1e2c-3f04-bcf9-ef9054cfd0fd | -8.1765 | -54.82046 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7eb1242e-2587-381e-8611-36d605dbb8d4 | -8.79692 | -48.73388 | 2026-09-22 04:46:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 284b0ab0-3cca-3189-af01-bb820e45058e | -6.30613 | -57.74773 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bef11461-c2ae-39ac-8e32-696b5a23efa4 | -5.18763 | -49.33401 | 2026-09-22 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8118eba1-f25f-3015-ad63-d0eeaac0011c | -3.22158 | -53.95155 | 2026-09-22 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| afe8351a-b645-3e1b-94c2-b891a3d33c30 | -6.72403 | -55.07565 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 49d4cc4a-93ce-3ed9-978c-96affd37fb37 | -5.98388 | -57.77314 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 494c9482-0f86-3bf0-8b56-76306ed04a98 | -6.31095 | -60.01203 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b66db662-9ac1-394e-bf80-1a4cd42e3e59 | -6.66729 | -50.9434 | 2026-09-22 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98538927-9528-3b90-8774-3fd0f613b6d2 | -8.79685 | -48.75896 | 2026-09-22 04:46:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16d1d150-9cc6-3709-a0c9-d77cb3d422e2 | -6.73753 | -59.42175 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| be3f5341-41b8-3e85-a1a2-ec26bec8a009 | -6.13844 | -59.94464 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6512baf5-c772-3c18-831d-87be06bc7b0c | -5.3573 | -56.04862 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d03cb54-be94-3f48-b11c-92a0f108ed4f | -7.56904 | -57.68564 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| afd2791e-38ab-39ed-ae4a-5df32ef2c0c8 | -6.73595 | -55.07287 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7bb5aba-dcc5-3acb-b1fd-ba217e2c4dfc | -6.40605 | -51.24484 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60c8e55f-b9fb-39a8-b193-66d92389f7ba | -7.57772 | -57.68709 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8980932b-883f-38b2-ab28-db55bcc67dbd | -8.25516 | -55.25964 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f5afa0a-e6b1-399c-9025-07dcfe513de3 | -6.73294 | -55.06787 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 558d19a1-8eaa-31dc-835f-c56775ed5c69 | -10.45769 | -51.34259 | 2026-09-22 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb2a4984-0a1b-322e-933c-c04f9a4b4441 | -6.0607 | -57.86491 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README50.md)
