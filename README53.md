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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d185bf36-560c-384f-ba41-5174e3bba4ab | -9.21671 | -51.55931 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a8485f9-9ad3-3d96-a8cc-37133ec353a9 | -6.25949 | -53.11992 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66b08711-eca5-306f-90f5-375ca01d8243 | -4.84309 | -45.39969 | 2026-08-28 05:10:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 08d9b0f1-8792-3e18-b4df-22873ebbc35f | -6.24465 | -55.42835 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74cac9da-85e3-32e9-a770-86bf5a34ee6f | -7.27837 | -49.94598 | 2026-08-28 05:10:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fde2cf79-970f-3e38-833a-27a02895dc41 | -7.39404 | -55.15599 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| effffff9-65c5-3754-91e1-64ed78f9c1a2 | -7.24882 | -45.8612 | 2026-08-28 05:10:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b896ece6-5c3b-3e3a-b7f9-122006d2950e | -6.17212 | -57.7863 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e88b1fa9-10e1-3fa5-9c28-7641f4cfb382 | -6.62838 | -53.18801 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d369af56-cd52-3966-b9d3-73fbf8a681eb | -8.98663 | -52.38922 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dc408d5e-dbec-3075-9313-a9d7147ef383 | -6.53763 | -55.2496 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d8bad8bd-9998-311a-b621-8d35cf087dfa | -4.84941 | -45.3965 | 2026-08-28 05:10:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ed394923-94b8-392b-9851-f505308547bc | -8.61987 | -50.01394 | 2026-08-28 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5129d7f0-a919-3527-a701-4157cb19e7ce | -6.01856 | -57.73914 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d0f7e4b-d6b0-3173-94cc-dbe5970a6c72 | -6.27719 | -53.35806 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 746ed37e-49b2-366a-baf9-c4a5ad656da7 | -6.27831 | -53.37428 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb14ca97-ea7a-3ff9-8853-77cb31d82de6 | -6.4953 | -53.25539 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ebe95099-3d2f-3de3-86db-1a960594193a | -6.53485 | -55.24559 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a70e1cc5-7ecc-3080-bdb5-61ee61ba4738 | -6.75766 | -55.68718 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 26a29805-fbbc-3949-a200-c8e6b70ad975 | -10.06691 | -46.9413 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5987fa55-20a6-3dda-99a0-7364e1ee6fce | -3.46194 | -59.51871 | 2026-08-28 05:10:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 791b88af-20a0-320b-bedb-db70df5c3fdc | -6.00417 | -57.82792 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ef76d18-8d86-3075-ba23-3a572cfdab25 | -5.93882 | -52.36399 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b934d18-2459-31a6-a675-653f9db48558 | -6.12444 | -57.69161 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a7996ad-e0c7-389e-b8a0-af34d7bd5e50 | -7.57965 | -61.30367 | 2026-08-28 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ab02379-b210-39bd-b5c6-b4e250408b8b | -9.98678 | -48.59259 | 2026-08-28 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07ed21a8-3589-3501-a9a7-07261a638257 | -9.43893 | -51.68825 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a39724a6-0cd3-3e42-a164-4763f83609c5 | -7.02484 | -55.69406 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfbd5d67-0fa2-36cb-a1e7-2631f487d1c7 | -6.97007 | -55.63202 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09e5063a-b756-38d6-a007-68f7c0471852 | -9.34089 | -48.16567 | 2026-08-28 05:10:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 84116818-605a-304e-9dbd-da981d77e243 | -6.25623 | -55.41949 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d532aa75-6c04-30ed-83f1-9de49f50a69b | -7.35323 | -55.1607 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40729b8f-048f-3a25-b578-720fc6593126 | -6.15669 | -57.79515 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00301a42-f30d-3fcf-806f-5dcf99398414 | -6.11311 | -57.82618 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 860f8e63-329d-3f94-9d7e-55d92c6a1624 | -6.16292 | -57.79995 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0570ff83-70c1-3c47-94e2-7226a5d35a11 | -7.36969 | -55.50882 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a27b4e29-84ce-3e60-8f18-0345170bb5fc | -11.37697 | -45.14542 | 2026-08-28 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61247f85-f6bc-309d-9df3-41436ee0ff73 | -9.61396 | -55.11116 | 2026-08-28 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65242940-6429-3214-8e53-97ec906ea780 | -8.2976 | -55.10931 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b3c8fe1-3ec1-30b7-a0cc-4d28265b8f29 | -6.642 | -53.19416 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d74ad4b4-c5d8-38aa-a6ac-1ed67d4877fe | -6.52656 | -55.25502 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02358c68-3dcc-372e-96af-598a0c106192 | -6.11483 | -57.68629 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 187c4f4b-e447-363b-a7f3-559ffba26829 | -9.15566 | -49.96649 | 2026-08-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c6fa84d-779b-3c07-862c-afea1545d863 | -6.42942 | -54.94107 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 044f5d1d-c4b2-32d0-aa5c-7b482e4cb7af | -6.597 | -55.43434 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 824ccc85-eaac-34fe-8e6e-ed9698b5d462 | -5.2585 | -50.96807 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 98ec169c-f6e1-33d9-8cd6-e830a6d8d42d | -9.21008 | -51.54789 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d4dc7457-217d-3dd0-ae22-56f76305405c | -6.97451 | -55.64698 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7612d87c-c7c9-308d-a1ac-75caaeb79f26 | -5.98962 | -52.1953 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a220468f-e12b-3cea-b02c-dcebf3492941 | -7.24828 | -45.86526 | 2026-08-28 05:10:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a1e34c68-e910-3f94-8a6b-dfb232ab2d18 | -6.15787 | -57.78777 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df925a50-9a80-3e93-8e9f-bc3f85e4f976 | -6.84224 | -45.0256 | 2026-08-28 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b52e6462-4a69-340c-aacd-f2d70d1bf723 | -5.89332 | -52.11427 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 54e78f67-34f6-3a3d-b963-9cc1c95f4c23 | -6.23758 | -55.47346 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 144623cc-09b2-3a74-923e-76eb0cf42470 | -6.12044 | -57.69475 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9f01cf4-6296-3a2a-ac63-d38d17cdd67b | -9.22979 | -51.55428 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 408d786a-5808-3d40-939b-e85013423c50 | -9.44849 | -51.70737 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b0f84de-7990-33f9-a964-e0fd875b156c | -10.53688 | -50.77459 | 2026-08-28 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a140088-4a4c-353c-8155-606aeb666811 | -6.27951 | -53.36642 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c5f7e02-98d5-3bd6-b3ac-7c7f2375b7b1 | -9.28535 | -57.07761 | 2026-08-28 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cfd6a0e4-a6e7-3a2b-b8dc-fb8763a9395f | -6.52989 | -55.25555 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7932652-97a0-3567-8af5-571325cc2f2c | -8.67219 | -49.54216 | 2026-08-28 05:10:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 411ab976-ac9b-3b26-828e-3bbc602a15b1 | -4.92723 | -55.76901 | 2026-08-28 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a158313d-591d-38b3-977c-438eb53e077b | -6.50239 | -53.25636 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c2cb08d4-dd70-39fd-b0ec-a3b308022d07 | -5.47506 | -45.12297 | 2026-08-28 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24e8619a-26f3-319b-a8d3-f1ce5217abed | -6.26194 | -53.36373 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e0659a5-cf98-3bfc-b49c-1b915d5ea2ad | -6.49884 | -53.25588 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 70a79d20-97a8-313c-96fc-d60f159753d2 | -10.55464 | -50.41961 | 2026-08-28 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68a60aa3-03de-3d0d-953a-e3d78a827435 | -6.26956 | -53.36091 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f362eaa8-16ae-33bc-b021-55c4a821c48e | -6.73917 | -56.34032 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c1ab50f-14ac-3389-9eae-dddd7b6a69f3 | -6.26201 | -53.33961 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1c11ff1-dfe3-3761-85f5-5a61091032b7 | -6.17744 | -55.46756 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d87a5c60-47f6-32d8-8c2c-8e5dfacc540e | -6.76319 | -55.69515 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f9e9038-a925-3c25-a181-3e8fa69a33b3 | -7.38457 | -55.15084 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1dfe57c5-ead9-3ba7-88bd-fe02528c4217 | -6.26064 | -55.41306 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce52f7ca-9a25-3645-b1ce-de2ebe8db7a3 | -6.25733 | -55.41253 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ac8d26c-3803-3ae1-867b-137c82ad7fb4 | -6.81024 | -52.50225 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 858e53ec-1a89-3dbd-bcfc-26378dec7c55 | -10.55398 | -50.41692 | 2026-08-28 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 515cb3fc-4e7c-3ade-aec4-acb875113043 | -9.43384 | -51.57906 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4f43e22f-51e5-3c9d-b027-a330b88ddbb8 | -8.58611 | -54.82734 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5eae588-58aa-3922-a5ba-0cb06fdb2417 | -6.27419 | -53.37769 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67af60a8-f34a-30e2-948a-bd58a5cb1762 | -3.49705 | -57.01987 | 2026-08-28 05:10:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b7a229c-3c83-3245-bd85-aaa9bdb7d359 | -5.46916 | -45.12206 | 2026-08-28 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d90ffe2-f2a1-36fb-b621-6e4b0884e1ae | -8.21992 | -54.95489 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 054a6e67-0950-3291-b500-9056329483c7 | -7.27776 | -49.9501 | 2026-08-28 05:10:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 840d39ab-bcbd-3abd-8d6c-c334a3fd35b2 | -9.46924 | -48.18549 | 2026-08-28 05:10:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1478d2da-39f1-3291-b967-3e3b0c60ccfb | -6.26552 | -53.34016 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb1fed39-9661-36da-920f-137f8392856d | -6.15446 | -57.78722 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9536836-4492-3784-b3a7-380a3675128b | -6.16693 | -57.79681 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c41121f1-48ce-3837-907b-2cc0fc007225 | -7.42377 | -56.26532 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61b5faa6-abf8-3b9f-a8b0-3ee6e412b9fb | -6.27205 | -53.32094 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96f55fde-31c2-3c3e-927b-98ef073abeaf | -6.96789 | -55.64594 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 212b873c-c4fb-3890-8ab0-e7d8aa548f37 | -9.45862 | -51.57898 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac916248-1149-383e-aad0-98c359aeb5af | -9.22429 | -51.56396 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7833a1ec-f2d7-30d6-840d-71961846f14a | -6.62488 | -43.7361 | 2026-08-28 05:10:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1315c64a-8d26-335b-a158-c5cc9daa68ae | -8.60032 | -54.78052 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1323ec88-9196-3915-b73b-e5bc5814058b | -9.65823 | -48.29736 | 2026-08-28 05:10:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f91eeb73-9308-3be5-bd13-4803291824bf | -6.75213 | -55.6792 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d5b60425-d2a7-305c-aef9-9552e8f31866 | -8.07736 | -45.81196 | 2026-08-28 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ad6d9ee-4371-3127-a49d-4eff40896ee3 | -4.30639 | -59.4761 | 2026-08-28 05:10:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README54.md)
