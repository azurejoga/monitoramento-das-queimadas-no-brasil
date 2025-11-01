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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d28e875-fea2-360a-ada2-152cf76e4bbe | -5.48775 | -43.09498 | 2025-11-01 03:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| abbc1854-3eca-3be1-a984-f22375969919 | -7.47657 | -38.70959 | 2025-11-01 03:28:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 95578429-c893-392c-bff7-35925cf9ea16 | -7.47323 | -38.70608 | 2025-11-01 03:28:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ca0d8824-23f0-393f-bcff-a4babe50b306 | -11.27738 | -41.73775 | 2025-11-01 03:28:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3c863923-45c6-3ce3-a685-047e2d9ae8a8 | -14.02669 | -43.26893 | 2025-11-01 03:28:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 434798f4-754e-310a-8db9-8936645b6266 | -7.97098 | -38.28272 | 2025-11-01 03:28:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3993f61c-0d37-3751-865b-1272cd3f7017 | -13.63321 | -43.17562 | 2025-11-01 03:28:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e1295012-5660-320c-8ec4-00512ca9d09e | -10.90759 | -44.75053 | 2025-11-01 03:28:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 993f1f07-0cdc-397d-ad46-cdc2f1d45a32 | -10.64005 | -42.31411 | 2025-11-01 03:28:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 82bc668f-163b-360a-a27d-5cf387c7f9ba | -14.02432 | -43.26666 | 2025-11-01 03:28:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f971afc0-7ddc-3c0e-a484-0d48f93f6241 | -12.12929 | -38.16968 | 2025-11-01 03:28:00 | NPP-375D | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 15d6bdc9-2c76-3e4b-acfd-8a81a31a0e2b | -13.40864 | -42.99558 | 2025-11-01 03:28:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9b329128-20d5-36f2-adf4-57f6d56b7501 | -6.5502 | -43.24226 | 2025-11-01 03:28:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.4 |
| cd26bb71-58f9-343b-bb9a-5621e89be5fe | -8.71464 | -41.58877 | 2025-11-01 03:28:00 | NPP-375D | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4b5cd005-8d84-366e-bf2e-bec7758de0a7 | -13.63413 | -43.17122 | 2025-11-01 03:28:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| acbb7536-a566-3be0-b1bb-bc9ab0872d24 | -6.88714 | -42.84827 | 2025-11-01 03:28:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 0f257375-89d8-34c9-99ae-2f42a7e50f69 | -8.56812 | -40.91228 | 2025-11-01 03:28:00 | NPP-375D | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bb86e19f-977d-3421-bbe3-2a964b4d8187 | -8.5625 | -40.91135 | 2025-11-01 03:28:00 | NPP-375D | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f9c3ebc9-3af3-323f-bb80-981b376f9ab2 | -7.04599 | -41.47127 | 2025-11-01 03:28:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 55b71d7b-e259-33a4-97d3-507ba4aaa2d9 | -6.88615 | -42.8536 | 2025-11-01 03:28:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| f85cb822-5de9-37d6-8861-2a16fbcf86d4 | -11.83611 | -46.01132 | 2025-11-01 03:28:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 24dc6ccb-61f1-3041-9fbc-475ffe59effd | -7.96711 | -38.27863 | 2025-11-01 03:28:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cd384ca2-ff0d-3c28-94f1-b104df26dd0a | -13.29193 | -41.93137 | 2025-11-01 03:28:00 | NPP-375D | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0c89cd01-f1ee-351a-9f06-841e393cd32b | -11.66753 | -41.68789 | 2025-11-01 03:28:00 | NPP-375D | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 803e3a0c-0615-32c4-bee7-42131ba311d9 | -10.65989 | -45.16676 | 2025-11-01 03:28:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd9219c2-45ba-3459-adc4-00b87a40e58e | -13.20544 | -43.13087 | 2025-11-01 03:28:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e786582f-0eb6-302b-b7bc-9b1566ec37be | -13.21137 | -43.13213 | 2025-11-01 03:28:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fcf421aa-3052-3a64-b7f2-d2f28e467603 | -11.43839 | -45.14436 | 2025-11-01 03:28:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 74ff09b7-2643-3e39-8538-c358aaba21e1 | -13.16276 | -42.28711 | 2025-11-01 03:28:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e17c6d27-b4a5-31fc-92c8-0bcaf272cfb8 | -11.84126 | -46.01249 | 2025-11-01 03:28:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3e20c14a-d29f-316d-8d03-2479de4b5bd6 | -6.55132 | -43.2361 | 2025-11-01 03:28:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 6e971c9b-8dd5-37b5-8f51-cc9a8a058e86 | -7.03996 | -41.47061 | 2025-11-01 03:28:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bab1a821-201e-345d-8aac-11a171174311 | -9.73859 | -36.08709 | 2025-11-01 03:28:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| f996e48c-d269-3139-a410-cc9ec9a2e95e | -13.37997 | -40.06387 | 2025-11-01 03:28:00 | NPP-375D | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d454110c-8fb7-3eaa-ba6e-e1a7c157cbd0 | -13.16128 | -42.28479 | 2025-11-01 03:28:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b2030752-be15-33f0-a5a3-7600cf9e6f4e | -14.02761 | -43.26457 | 2025-11-01 03:28:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7b460a38-3a28-314f-899d-429823c065cf | -13.58221 | -42.9024 | 2025-11-01 03:28:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5b0c6721-88ab-3d5c-ae01-b4af205de8d4 | -8.0045 | -35.86189 | 2025-11-01 03:28:00 | NPP-375D | RIACHO DAS ALMAS | PERNAMBUCO | Brasil | 2611705 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 133b0b50-1afa-3e7e-b613-52cdbcf7155f | -13.35793 | -43.09417 | 2025-11-01 03:28:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cfbc2bad-f0a7-3478-a069-8a991ba29289 | -8.21533 | -35.35228 | 2025-11-01 03:28:00 | NPP-375D | POMBOS | PERNAMBUCO | Brasil | 2611309 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 77883f21-c67c-3ef8-a829-9110e2f71344 | -9.73947 | -36.08189 | 2025-11-01 03:28:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| f0bb1724-3211-3f78-b302-46d6006fe739 | -10.6392 | -42.31848 | 2025-11-01 03:28:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 686244e2-0596-3226-ac72-b7e9dfe9776b | -11.43686 | -45.15173 | 2025-11-01 03:28:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 110d950a-00d5-39c6-9770-7b3066c8a4be | -10.6333 | -42.31729 | 2025-11-01 03:28:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 133ebcb7-9dcc-3cb5-a98f-0186737bbf70 | -10.66122 | -45.16016 | 2025-11-01 03:28:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8fd13ce8-b4ba-3873-9127-d33015535614 | -11.84323 | -46.01305 | 2025-11-01 03:28:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 375ccef5-30e5-3dbd-a601-f04da85081a9 | -13.41448 | -42.99691 | 2025-11-01 03:28:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e7db8109-5b1d-38ec-a3bd-17bffd5572e3 | -13.58798 | -42.9038 | 2025-11-01 03:28:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8a061433-9a98-32b2-aee3-39e8dde0c546 | -6.55255 | -43.24243 | 2025-11-01 03:28:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 7de58245-e2f0-38b8-b2ba-4044184e9e73 | -8.81952 | -39.8315 | 2025-11-01 03:28:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 137c5c9f-03a2-30f9-a339-580f350621e8 | -6.88069 | -42.84683 | 2025-11-01 03:28:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| e96ed28c-9a0c-3999-a7ef-1abbc640f969 | -11.28297 | -41.73907 | 2025-11-01 03:28:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 89716478-ef97-3288-a9c2-e65c2fc56315 | -8.21451 | -35.35717 | 2025-11-01 03:28:00 | NPP-375D | POMBOS | PERNAMBUCO | Brasil | 2611309 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| da74a6d9-80ad-3ea6-bb09-1a09dc0ab244 | -7.96619 | -38.28374 | 2025-11-01 03:28:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| abbe5783-b5f2-350f-9f60-1b5051dffd96 | -9.73549 | -36.08117 | 2025-11-01 03:28:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| ae8c2780-21a3-31f7-b171-f90bf7bf2d28 | -13.63095 | -43.17328 | 2025-11-01 03:28:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 673d50ab-928b-3484-b9c3-19ad110b04aa | -13.29739 | -41.93266 | 2025-11-01 03:28:00 | NPP-375D | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bff15ec0-8af0-3db8-bd63-878e7988e3fa | -7.96623 | -38.28187 | 2025-11-01 03:28:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b78ee8bf-0f0d-3ced-b574-b3b4f146f23b | -10.63836 | -42.32285 | 2025-11-01 03:28:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dd740ae2-3f64-3e5a-a443-0697d2cc17cd | -13.35882 | -43.08982 | 2025-11-01 03:28:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8718ddac-ca4a-3184-b74f-9a82d20819f7 | -8.70883 | -41.58752 | 2025-11-01 03:28:00 | NPP-375D | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 54da9723-ba62-3e94-ae54-137df7eaf200 | -13.63684 | -43.17462 | 2025-11-01 03:28:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7d68e99f-5b7c-3897-98f6-88d3c34d33e6 | -13.20954 | -43.13042 | 2025-11-01 03:28:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e159a1e4-9b1d-3a54-8a5f-ef86ff00d6c1 | -11.26055 | -45.51791 | 2025-11-01 03:28:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 252de5c6-31cb-3721-b289-592806dd039c | -10.63415 | -42.31292 | 2025-11-01 03:28:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fb4771f6-db1c-3773-98d4-399843434d4a | -8.82472 | -39.83242 | 2025-11-01 03:28:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fd735fad-68fb-377c-b5f4-63ad95456a8b | -12.31003 | -37.91816 | 2025-11-01 03:28:00 | NPP-375D | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 913ddda6-b15d-3276-9f1c-40a9e572c379 | -13.16357 | -42.28315 | 2025-11-01 03:28:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fd32f70d-a713-3906-9cce-4669812cadd1 | -10.6313 | -52.1891 | 2025-11-01 03:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 9cfb0ea7-df07-3667-8ef8-04169b625f52 | -3.234 | -50.5789 | 2025-11-01 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| c454a274-d6d4-3cc6-95ee-b77c168c22d7 | -3.2156 | -50.5795 | 2025-11-01 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 8df82f97-5d08-35cf-af6b-ebd9da069884 | -16.9135 | -50.4707 | 2025-11-01 03:30:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 600ba529-0941-3b80-8b51-0f9f2e7afbef | -3.234 | -50.5999 | 2025-11-01 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 758f4a70-b44c-3efb-9a69-0d4c0b565f60 | -11.8447 | -45.9965 | 2025-11-01 03:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 215744bf-7a9b-3f8a-84ba-0e4b333fec89 | -14.20681 | -42.86835 | 2025-11-01 03:30:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 37411a36-8036-361a-a230-590e06d8fb3c | -15.11337 | -42.25702 | 2025-11-01 03:30:00 | NPP-375D | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6c184222-f599-3c27-bdee-a1bbc0e22780 | -15.11282 | -42.25808 | 2025-11-01 03:30:00 | NPP-375D | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f37a633e-e260-3f46-a5a9-8eefb6f3b87a | -14.20596 | -42.87243 | 2025-11-01 03:30:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 72a11c88-1eb2-3ed2-b94a-7462942391db | -14.60385 | -42.88753 | 2025-11-01 03:30:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 27552b2e-0646-37d5-a259-26ce40012932 | -11.8256 | -45.9992 | 2025-11-01 03:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| d59b2402-2dec-3ed1-a06c-4aec90d29c6f | -11.2798 | -45.5052 | 2025-11-01 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 5679ace3-9810-39d8-a54c-d22aeef8e19a | -11.2607 | -45.5078 | 2025-11-01 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| b1ee0a7c-9e6a-3598-b67e-75b357fb23b6 | -11.8447 | -45.9965 | 2025-11-01 03:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| b136459d-f900-36c4-b796-712486e85aef | -10.6313 | -52.1891 | 2025-11-01 03:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 61d33d0d-fdf4-35df-a579-e37dc5f1d3c8 | -3.234 | -50.5789 | 2025-11-01 03:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 5ef36b62-1a1d-3a61-a4e3-511b3962464e | -7.18886 | -41.64811 | 2025-11-01 03:47:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 58e366cb-14d8-3110-aefc-c410f0a2d8a2 | -8.23215 | -46.24876 | 2025-11-01 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80d2dffa-38f1-3382-b416-83d581f0e78b | -6.88666 | -42.84945 | 2025-11-01 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 6b3a81d7-4bf9-3824-af00-4f79d986b728 | -8.14993 | -45.44339 | 2025-11-01 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| faae602a-a706-314b-a75a-59a1bd10c95d | -6.99492 | -46.53076 | 2025-11-01 03:47:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65495c53-3a2c-3e3b-b146-df980b0b03a4 | -8.16924 | -35.24706 | 2025-11-01 03:47:00 | NOAA-20 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5709d133-a6d6-33f6-ba74-acb1ee4307cb | -6.33999 | -45.25911 | 2025-11-01 03:47:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f8ca3118-d006-366b-980b-65f682531a5f | -7.40105 | -42.47421 | 2025-11-01 03:47:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8cd01dfa-f809-3e33-aad3-4ccbbf3b3633 | -2.76029 | -45.39589 | 2025-11-01 03:47:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7689cbca-871c-3b68-b5eb-29f002dbfd37 | -8.22685 | -46.24785 | 2025-11-01 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4b2b5863-4cce-32c4-8340-034f268b44fa | -7.83921 | -40.26098 | 2025-11-01 03:47:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cfd0c57b-2937-3704-872f-2ce9d1a20de2 | -6.57722 | -48.73479 | 2025-11-01 03:47:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5a154b95-ce8d-39bc-852a-59cc4774406e | -7.04213 | -41.46759 | 2025-11-01 03:47:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5dd83143-aefa-3a94-afd3-1b08d93acf3f | -4.29739 | -41.43963 | 2025-11-01 03:47:00 | NOAA-20 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 43659c49-35fa-338c-b556-c3901f2ef1ee | -8.18264 | -44.76257 | 2025-11-01 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README11.md)
