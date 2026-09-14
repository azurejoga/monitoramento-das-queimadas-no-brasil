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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf72c2db-75a9-3101-b75c-77765a69fdd6 | -6.28851 | -55.29002 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e82474b-6432-394e-923f-8be90629c706 | -6.10278 | -43.51358 | 2026-09-14 04:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a2b0bdb-67b6-3fbb-9ca3-0cfb25552ce1 | -7.87164 | -54.72253 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5b5216c-11e9-37af-ba73-b5a84e84e893 | -2.69636 | -57.54493 | 2026-09-14 04:32:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 28cb4f3e-775e-30bb-8e64-4d506cc91d8f | -9.43626 | -50.12029 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1e0fe83e-87f0-3598-bee8-2bc6a1c9d267 | -7.02003 | -44.63134 | 2026-09-14 04:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 25069391-6194-37f3-8aac-7a0600a815ab | -7.97276 | -43.98579 | 2026-09-14 04:32:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10053c36-1fc5-3092-a861-06fe2da4b882 | -2.91038 | -50.41479 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| bf6dfb99-ed11-3858-8f03-dcf1e68aa2da | -2.92118 | -50.46197 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e44c0bb0-8136-37be-b467-6d65153f010b | -6.3447 | -44.10728 | 2026-09-14 04:32:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ccdd8372-8860-332f-ac19-ef72edcd9316 | -2.90073 | -50.41772 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 189.2 |
| 9df945e4-703f-3dda-8ccc-713ff4c5cbd9 | -9.44245 | -50.13183 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d3ba3b2b-3ddd-3eab-b695-cc8cbd1ebcff | -5.19852 | -49.33226 | 2026-09-14 04:32:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d72631b-4e3d-3b76-ab7b-54cdc8c09d5b | -7.31367 | -45.29854 | 2026-09-14 04:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48c60e8d-f83f-3081-9c4d-85b40985e20d | -2.92741 | -50.43446 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| e2eebbb9-fb19-30a3-b064-14f455d09a94 | -2.91861 | -50.42068 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 5d5b4b36-edd9-3c02-b160-ad2845ef9404 | -3.23019 | -43.0355 | 2026-09-14 04:32:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 551cfecb-ee01-3565-8716-75dc0575e79e | -2.93857 | -50.42268 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c3acccc1-4555-3199-9f7a-ccf5dd3197a3 | -5.12967 | -55.94688 | 2026-09-14 04:32:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fcdb688b-4779-3540-93f2-0e68fa5dd8c4 | -2.90663 | -50.40965 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 265854f8-68f4-3c8a-b6a8-16683aefb5f8 | -7.0926 | -41.80615 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a021d265-5bce-33cd-8be1-44218b040d0c | -9.44521 | -50.12854 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2efd3743-6632-325f-a22c-bc80fb109402 | -7.10061 | -55.62595 | 2026-09-14 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5291ef8c-f971-3d10-8534-0a351cd7ef10 | -9.90939 | -47.6105 | 2026-09-14 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| daba0f97-cf72-37d2-bf2c-2bbc1fdab82f | -3.88411 | -41.04576 | 2026-09-14 04:32:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| be64d99b-1e17-3886-bd59-e0f9a784ecb4 | -9.45774 | -47.8507 | 2026-09-14 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b60f3f7a-44d9-313d-a47f-53d091e11d70 | -9.4275 | -50.12395 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9b771acc-1ee6-33ea-9ea9-09a6a9d36354 | -2.96309 | -50.41317 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 367bf64c-3ea2-3b8e-936f-fdc5c2fe96e9 | -7.29686 | -46.75446 | 2026-09-14 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f43afc6d-58b9-3580-9c7e-e09db463e304 | -8.538 | -54.70052 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a8be070-ffba-38c7-afde-efaffa057511 | -2.91548 | -50.42346 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 135.7 |
| 4ac157be-b1f5-3423-a63e-62e112c03036 | -6.69313 | -43.1454 | 2026-09-14 04:32:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c9025dc1-8988-3fc7-99ce-d73e1fe64244 | -6.8754 | -52.10245 | 2026-09-14 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 240134d8-af99-3c69-bc58-cdf207c83c7b | -2.89393 | -50.40307 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 114bc1c7-7706-3ca1-99f3-2553a4e636c4 | -9.16816 | -49.9955 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48a9e752-0686-3b49-9ba4-fad0fa93025a | -2.8993 | -50.42657 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 315.0 |
| fa3c7899-2bc8-351f-a4f0-9b0ce5fd9587 | -9.3769 | -50.20475 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d322d293-cb99-3049-9b9e-96ffbbbc7548 | -2.92591 | -50.40379 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 3cb53282-6c7c-3a16-8223-eea20a8b96e2 | -8.53706 | -54.70021 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 470e4d5b-825f-3a26-b2a0-d1b7f0f7859e | -2.91882 | -50.44798 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 1fdafd96-ac39-30b1-8ac8-5f989d914a61 | -2.89858 | -50.43098 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 315.0 |
| 871f6227-3be1-3a96-9c7c-1b1a19335be3 | -7.46634 | -45.96777 | 2026-09-14 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f8f1a57-ec31-3f30-bea6-d20148ee1fb9 | -9.33586 | -44.37292 | 2026-09-14 04:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 984a73ad-7696-3504-9416-279943c576b3 | -8.17057 | -43.11003 | 2026-09-14 04:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6ea5e361-460e-35d5-8e18-1260f59ebe91 | -10.31489 | -45.29231 | 2026-09-14 04:32:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bca23316-1f42-3bdb-87bd-0d4bb12eeadb | -6.24928 | -44.79745 | 2026-09-14 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| df862636-15b3-3a5a-a6ff-fbfb42cedc72 | -2.91622 | -50.44629 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 2218ec4c-6876-3e0d-a51d-0438c89841a0 | -6.69051 | -43.14198 | 2026-09-14 04:32:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b48e3cd-1daa-3e4a-9252-4979dbdb2bd9 | -2.9497 | -50.41098 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 531f5ffd-6da6-36a3-836f-25b81c5e6f51 | -9.44822 | -48.10556 | 2026-09-14 04:32:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 417ff6bf-091f-39ad-9ba8-764fa733567b | -9.44331 | -47.87256 | 2026-09-14 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99448b8f-eb3a-3dcd-a333-c381ea2db113 | -3.75956 | -51.1489 | 2026-09-14 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 0b2e9beb-978e-30f6-aad0-72858a8478b1 | -2.96382 | -50.40878 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eec5fd69-bc0f-3c68-bc15-d6e9860fa65e | -2.92516 | -50.42054 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 723eb103-562f-3e56-92b8-7dd450da0a6d | -8.5358 | -54.7072 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93d7dadf-a9e9-347e-83c3-351263ed3e36 | -7.09132 | -41.81448 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d785b225-1316-31f8-b03d-3e682cbc9170 | -9.44021 | -50.12098 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7bed2f17-9199-33b8-a02e-99970c341df1 | -7.15905 | -42.09901 | 2026-09-14 04:32:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 05f56214-4842-3b83-bde2-303eff9c14b2 | -3.41294 | -58.20995 | 2026-09-14 04:32:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8aba78bf-3cf7-3820-89f1-2587ba2c4509 | -7.33113 | -45.37643 | 2026-09-14 04:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dc0319b9-9145-381a-be5a-eabc12fabde1 | -2.91326 | -50.46389 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16e06e4b-3931-3369-9da7-d29348d42482 | -2.96455 | -50.40437 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4956aa2a-438c-3a1e-b14b-173e5231812e | -6.28545 | -55.27301 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea56e3b8-4d29-3fb2-b1e5-0d6270e45de5 | -9.31736 | -44.35908 | 2026-09-14 04:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97b8709b-f99e-3ff4-bed0-57230ffc7050 | -2.96672 | -50.39126 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89974686-f164-32b0-8492-36797b5e5cdf | -3.38178 | -50.76809 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 337546da-099e-3575-bc61-ac38bc84a4e2 | -3.38633 | -50.76886 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f88fefed-d85f-30f0-bcf6-4af3d1525dec | -9.44431 | -50.13365 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bf273364-5e21-39eb-bd84-914e5b8e4817 | -5.12881 | -55.95168 | 2026-09-14 04:32:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b3839d84-eff0-32e0-9fbe-1dcba38b9281 | -2.94669 | -50.4015 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| be486557-1b10-379d-b55c-38ed24855093 | -2.67577 | -57.55855 | 2026-09-14 04:32:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c5173001-544b-344a-b5e4-25e5c7d40eca | -8.5354 | -54.7144 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf1d4285-e1da-3b44-8d4d-4580e1577896 | -2.93189 | -50.43518 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 35565155-b937-3604-9997-dde04fbdc6f4 | -2.8984 | -50.40379 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5242f436-f121-3ca2-99db-5b0bb879d9b6 | -2.78144 | -51.3646 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fddaea59-511f-389f-99c6-0a51d3759e5a | -5.80506 | -53.8021 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8ec7cb43-515e-3906-832a-b6621789f532 | -3.22349 | -43.03446 | 2026-09-14 04:32:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 077fe136-b2f9-32f4-a63a-8ff192d05c59 | -7.02226 | -44.63882 | 2026-09-14 04:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f4df7ed-90a0-3994-9e20-13a1e09ef12a | -2.92664 | -50.41171 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a1fc0321-0ee6-370d-865f-ac90278a4aaa | -2.96081 | -50.39927 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2ef7a1b2-80c0-381f-9fdc-ffdd0fe84596 | -3.41211 | -58.21079 | 2026-09-14 04:32:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7f363edd-5e3c-3ae9-bfe0-35264cfebf7e | -3.22352 | -50.58856 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2d17b4a-615e-3845-be2a-107dc8659b02 | -7.87099 | -54.72601 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 48ee7f72-9d7a-3eae-985e-62609fe29a92 | -2.89787 | -50.43538 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| c759ad17-e881-3af2-86fd-69224f7bf59b | -2.91018 | -50.38766 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d5aa8761-7531-3170-864c-2f1677fd715c | -2.91919 | -50.40144 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 064857e2-9a01-3604-a892-53a620d6dc1a | -5.12164 | -55.95581 | 2026-09-14 04:32:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| cee928f3-aec9-377d-8098-616f8fb6a847 | -6.29429 | -55.29156 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d339875-fe48-3f51-8b9d-e70367784161 | -4.34623 | -54.78109 | 2026-09-14 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ba980ece-1005-3af8-a357-e42c1b94a77f | -5.89133 | -45.57439 | 2026-09-14 04:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b565a446-e043-3ef1-a836-8683387115f8 | -2.76933 | -45.50053 | 2026-09-14 04:32:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab0d7123-3cf3-3ed6-9ef2-5994829bdeee | -3.75492 | -51.14814 | 2026-09-14 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a10b4130-f8f6-3180-8fbb-dcbbf842fe33 | -4.1338 | -54.02139 | 2026-09-14 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c90750f5-b4d3-3c98-94c0-86f7aed9b36e | -5.92063 | -45.03698 | 2026-09-14 04:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e5c06549-580b-3c9e-93d8-09404bfb90e5 | -8.99604 | -50.82436 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f19565d9-2cb4-3003-bfbf-e164040a2a3a | -2.91079 | -50.46933 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b97a00c0-d688-3d39-8b1c-1eba42a7cb18 | -9.45359 | -47.85404 | 2026-09-14 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 20dc2659-62a5-31a6-bbbe-9fa1ae7c553a | -2.88141 | -50.42359 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 34a1527f-91f2-312d-b5d6-b466e1939905 | -7.1011 | -41.79891 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 10b4e01c-b1b9-3744-85ad-89a1cb66dd08 | -3.35085 | -51.29078 | 2026-09-14 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README19.md)
