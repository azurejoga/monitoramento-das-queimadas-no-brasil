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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3d2c1f0-59cf-3192-b69f-515b47008e93 | -7.20346 | -43.10846 | 2025-06-15 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 0f4e67ea-98fc-3b72-90c4-33ee441e522d | -9.4038 | -48.43516 | 2025-06-15 03:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d2bac48-97a6-3e99-a3db-c96c53a2f3df | -10.45327 | -47.94952 | 2025-06-15 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9457cfa1-9659-33f2-bbf8-49700c4bb3e2 | -7.11389 | -43.43064 | 2025-06-15 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 34eddad6-9903-34da-9756-89736e44017b | -7.23638 | -44.15851 | 2025-06-15 03:53:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f088e929-0c8a-348b-b05e-a14d53442167 | -7.21214 | -43.10477 | 2025-06-15 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 13b0243b-ef67-3b34-b921-7dfd3de88086 | -10.27737 | -47.61198 | 2025-06-15 03:53:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 836f7436-e25b-3cb5-9fc9-f195fd1ae5ad | -9.4148 | -48.4477 | 2025-06-15 03:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ce64f73f-590a-37b0-aa84-92a311e1c209 | -10.73456 | -44.49414 | 2025-06-15 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8cbd43d-f5dc-3226-a7a9-48c7b01cca0f | -7.20431 | -43.10347 | 2025-06-15 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| d2e669fb-26d7-362d-8750-1b6cacec6ee8 | -10.71684 | -46.55596 | 2025-06-15 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad37f04c-6058-3b28-ab87-f0a230129311 | -11.74884 | -46.75038 | 2025-06-15 03:53:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6232ff31-50a7-3f6f-8705-ab6730a9075c | -11.02151 | -44.64706 | 2025-06-15 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d48ddcad-672e-38e5-85c9-63934733a49e | -10.23214 | -52.23716 | 2025-06-15 03:53:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 75d64822-8b68-3211-8445-ff0263de231e | -7.23773 | -44.15074 | 2025-06-15 03:53:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8fe247bf-109e-3879-9722-fbb83fef8960 | -8.34696 | -47.08717 | 2025-06-15 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac772292-cda8-36b9-b7de-fc408dbb548d | -6.43921 | -45.72914 | 2025-06-15 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a39745e9-e473-3fd7-a983-57c3e9e43b23 | -10.14193 | -46.70285 | 2025-06-15 03:53:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 125db0ec-1e0d-3b18-bd77-18922b8c9924 | -5.68455 | -46.57292 | 2025-06-15 03:53:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbb15f97-e847-37f0-a1f2-eade40445906 | -9.04894 | -47.91652 | 2025-06-15 03:53:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3051a505-47cd-3dbf-b456-e7cd895977a3 | -6.4439 | -45.73009 | 2025-06-15 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6dd1898f-43f8-380a-8909-738cd6614029 | -11.57061 | -47.8707 | 2025-06-15 03:53:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 86fc9d9c-1559-3ea7-8ec6-dcd703698570 | -8.07649 | -43.11132 | 2025-06-15 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 30.8 |
| 65dc2a96-e1e2-3c87-b8b5-cca24c643b5a | -10.09415 | -52.7449 | 2025-06-15 03:53:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d196fe9b-5b07-314b-8255-bc4686ef144b | -7.21572 | -43.59965 | 2025-06-15 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30ac14be-493a-39f6-8c35-28974498c5c2 | -7.23706 | -44.15463 | 2025-06-15 03:53:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa5ade21-43aa-332f-9f2f-d401923e5744 | -7.2315 | -44.1618 | 2025-06-15 03:53:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2a2d56de-ab41-3364-8314-2d7859ade5bf | -10.52556 | -47.8307 | 2025-06-15 03:53:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e11d00c3-24d9-3149-af5a-f165746dedea | -12.2323 | -44.16263 | 2025-06-15 03:53:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 931a6b0c-af2e-3753-94ef-e4ff580b3efd | -7.23253 | -44.15032 | 2025-06-15 03:53:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8a1b5db-dbc9-3b30-a50a-44c2597d5f9b | -9.40443 | -48.43167 | 2025-06-15 03:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa430d0b-31e4-32e0-b738-690803abb7f4 | -6.68791 | -43.68214 | 2025-06-15 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1a7d0716-73b0-3761-acdd-c7283696ffa2 | -11.18877 | -44.48279 | 2025-06-15 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8440ba2c-1267-3ec8-94f0-291c32adbf02 | -6.88958 | -43.13191 | 2025-06-15 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec480f0c-446c-30fd-aa8b-b7af37a01c02 | -7.23352 | -44.15016 | 2025-06-15 03:53:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 85b638f3-8906-3e9a-a392-dcb4267bae4c | -10.74334 | -48.57658 | 2025-06-15 03:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 998094a7-80df-3a49-b4f4-e1e1b09e6496 | -9.41952 | -48.45221 | 2025-06-15 03:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 615ee185-f34b-3a23-a736-f40dbb83899a | -6.33482 | -43.74315 | 2025-06-15 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1772984f-f6db-38f9-b145-c9c4ed31584c | -12.23145 | -44.16759 | 2025-06-15 03:53:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec7b5be8-cac2-376f-b1ec-0119629a057e | -9.42082 | -48.44526 | 2025-06-15 03:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a5cf5e16-23c5-3449-9293-c163f70ea1b1 | -8.35199 | -47.08795 | 2025-06-15 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 431ac33a-ff75-3926-b388-969f862fba02 | -10.45033 | -47.95055 | 2025-06-15 03:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fbbf146f-fc79-338e-868d-f85651c68b01 | -10.99093 | -44.70201 | 2025-06-15 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39519ede-acaf-3afb-b021-f6cbb3d66466 | -6.83516 | -43.40501 | 2025-06-15 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 77cbf38e-dd4e-37ac-a8c8-c71f3f85eb2c | -10.07295 | -52.74748 | 2025-06-15 03:53:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f6b9d56-af63-317a-8dab-96b07d93a187 | -7.21129 | -43.10976 | 2025-06-15 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c1eed2e5-a2cc-3594-ba71-4e436940a166 | -10.50936 | -53.58088 | 2025-06-15 03:53:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 00c76256-507a-3472-9f66-edee6b3251aa | -10.65772 | -49.36093 | 2025-06-15 03:53:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 828cc46c-36ec-34ae-b3c1-d75219d1ba3e | -6.68729 | -43.68578 | 2025-06-15 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f68e0550-680a-396c-be35-dc5518160cc2 | -10.07986 | -52.74886 | 2025-06-15 03:53:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7870729-61d2-3327-bb80-988a6ffe057f | -10.52496 | -47.83389 | 2025-06-15 03:53:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a5c36b17-63c5-3408-b7b7-dbeaaf7ee62a | -11.1875 | -44.48986 | 2025-06-15 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b06a2af-cddd-3a2f-9bdd-7d576363994f | -7.24301 | -39.17937 | 2025-06-15 03:53:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ada3e964-b35c-3a06-b1b4-a82537cbad5b | -7.21517 | -43.59984 | 2025-06-15 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f4a4b49-0c01-3b21-b19f-0c5ff30ae3eb | -9.03846 | -47.02641 | 2025-06-15 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 67032bb4-f98d-3890-9c46-fc843ea99444 | -7.19955 | -43.10781 | 2025-06-15 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 19ef4586-06d0-35e1-b715-a947393d9796 | -9.04967 | -47.91197 | 2025-06-15 03:53:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e551e6e0-60da-333c-a0b7-11ed2164ac41 | -7.20738 | -43.10911 | 2025-06-15 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 2a4974ee-6083-3894-9583-9f135c3af939 | -10.72056 | -46.56173 | 2025-06-15 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9e33c3e7-994b-3bb9-aa55-2c7f73804b78 | -10.71592 | -46.56088 | 2025-06-15 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fc4821f5-aed6-3398-946e-30b3fb76382f | -10.73395 | -44.49771 | 2025-06-15 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b084753d-52df-37fc-b471-42ed06c32db5 | -7.23124 | -44.15811 | 2025-06-15 03:53:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8709e5e-eba3-3b21-8c54-2b0e642a289d | -9.04047 | -47.01533 | 2025-06-15 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c6e16d96-e87a-3576-b464-fff504483529 | -10.0375 | -46.59341 | 2025-06-15 03:53:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 06dc7d1c-a9b2-3dbe-acec-897278acda49 | -11.18631 | -44.49082 | 2025-06-15 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a81aa7a6-db25-37b0-a43d-55fffa62c33d | -9.04951 | -47.91336 | 2025-06-15 03:53:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2c6b5e5-787e-31ba-bde4-b8156cc87ab8 | -10.71797 | -46.5585 | 2025-06-15 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1a9c1d30-b748-3743-a18c-732d1843444b | -9.40192 | -48.42738 | 2025-06-15 03:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69360f36-f58b-3eb7-84da-90a327f21283 | -12.68445 | -52.39644 | 2025-06-15 03:55:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db0c6d72-30cf-30e0-85d1-0ec4577b608b | -16.68093 | -43.88325 | 2025-06-15 03:55:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c215bcef-08fd-3ba5-aab0-b740e21a3586 | -15.40081 | -47.88074 | 2025-06-15 03:55:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d08f40f2-fa77-3eb4-b759-9e8802d509c8 | -16.29631 | -40.20276 | 2025-06-15 03:55:00 | NOAA-20 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4252e989-7069-3489-a7fd-4aa558e56ad6 | -18.39348 | -44.18687 | 2025-06-15 03:55:00 | NOAA-20 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bff1b5bc-1fd3-3d3f-92c2-106417c0bf4d | -17.79611 | -42.73652 | 2025-06-15 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f0f262a8-ab34-3429-b95a-ef0bccc03f09 | -17.59059 | -44.71452 | 2025-06-15 03:55:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71317cf9-9ecd-3b05-9e5b-64cc5b1c44b2 | -13.91074 | -54.59913 | 2025-06-15 03:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| bf860dd7-16d6-39b4-8923-60b60008b52e | -12.6898 | -52.40328 | 2025-06-15 03:55:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| adf91256-0cd9-3a2b-af08-947b74610e0a | -15.41208 | -47.87234 | 2025-06-15 03:55:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b344bd2c-94fa-30e1-9723-2bfb03ddfacd | -12.4192 | -43.8143 | 2025-06-15 03:55:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dc571c8b-c7c9-3c8b-8264-50ea7229f01c | -17.7489 | -42.89427 | 2025-06-15 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4cdca085-f3bf-35c0-9bb2-5c3118356c27 | -13.9164 | -54.60749 | 2025-06-15 03:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 5c3920ad-23c2-3449-ba39-20a8bea0467e | -12.68894 | -52.40409 | 2025-06-15 03:55:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7e0f633c-fa3d-3902-b8bb-51b28f130be3 | -12.76564 | -44.41176 | 2025-06-15 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 18655f0d-4307-3036-bbe6-9dccfb451a22 | -12.09 | -49.48809 | 2025-06-15 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68005679-3bdb-3408-aa76-fcb492110f09 | -19.55742 | -45.31986 | 2025-06-15 03:55:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5a0e63ef-6262-3b4d-9107-8462fc5a4758 | -13.90915 | -54.60625 | 2025-06-15 03:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 0515ef79-7351-32fa-a8a2-e6026e03bd51 | -13.22851 | -49.83964 | 2025-06-15 03:55:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a851557-ccb5-3c9f-b868-f5ad8edb871d | -13.22376 | -49.83482 | 2025-06-15 03:55:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 636601b7-4509-3a04-a39f-aad7b3ee65f2 | -18.3963 | -44.19186 | 2025-06-15 03:55:00 | NOAA-20 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a4ecd175-4714-388e-8695-3bbb3d7487d0 | -12.69125 | -52.39326 | 2025-06-15 03:55:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 62ee3ac7-c6ac-3090-a797-b4a656e0c726 | -15.56776 | -47.85404 | 2025-06-15 03:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 121760b8-c594-3511-ba26-9f86c89d1043 | -15.56355 | -42.62607 | 2025-06-15 03:55:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3cfaeca6-7d81-3cf8-83ae-22f251457bd7 | -19.51661 | -44.26353 | 2025-06-15 03:55:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6476819d-a393-31b3-87fc-d7414517b9ce | -12.76653 | -44.40673 | 2025-06-15 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d2ea82d4-2b48-30ed-8fd7-7f7a948c3d70 | -12.69091 | -52.39789 | 2025-06-15 03:55:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 1a2bf415-756a-367e-b2d1-dd8c9d8c212c | -15.63586 | -49.37238 | 2025-06-15 03:55:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0782a6ff-ea9f-366b-a076-f7b0cc29badb | -14.83226 | -48.44001 | 2025-06-15 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| df281f07-d503-3e0b-bd1c-33da5450f0f8 | -15.64094 | -49.37356 | 2025-06-15 03:55:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a20d8b0-41a7-3501-a950-078c48cd4821 | -15.39772 | -47.8968 | 2025-06-15 03:55:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61f475db-59d1-3358-a4e5-ad3fbd4e133b | -15.33072 | -47.35343 | 2025-06-15 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README7.md)
