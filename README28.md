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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 118d48fa-f49e-32c6-94df-1c6b4ec697f4 | -9.45037 | -44.87022 | 2025-11-15 04:06:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15028fd6-9fa0-345c-89eb-4c32a0ae76a6 | -8.19078 | -44.82656 | 2025-11-15 04:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ed9c3d4d-24e7-39b4-9665-8f45806d0e6f | -12.36674 | -43.69946 | 2025-11-15 04:06:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1951b84a-8c67-3a73-9f78-d6a56af2b801 | -7.39193 | -48.6519 | 2025-11-15 04:06:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5bd301c1-0fea-310f-bac6-c95233bb9ecf | -7.72771 | -45.81575 | 2025-11-15 04:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a835534a-e7c9-32c7-8b85-7a17fc21630b | -9.34525 | -46.5899 | 2025-11-15 04:06:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9e3e07c-dd35-3989-a428-24ab9c8476f1 | -12.75485 | -43.65089 | 2025-11-15 04:06:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8872a1a-331a-3f10-a63f-9b164007b4af | -9.02708 | -46.89059 | 2025-11-15 04:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 45d3ad0e-4873-3329-98cf-159995ec7f98 | -7.88282 | -48.39791 | 2025-11-15 04:06:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 087f519d-e1d4-3d63-9219-9a90427e1c26 | -9.13774 | -47.75925 | 2025-11-15 04:06:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eba5f0a8-aaa0-3559-b9cc-5df348b644fb | -8.66705 | -45.46384 | 2025-11-15 04:06:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4afcb495-1d48-389c-b81c-4410e89a2b80 | -12.48802 | -47.29938 | 2025-11-15 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e91a9293-22c9-3a26-bc07-d1b3c7fec3ce | -7.36223 | -47.28694 | 2025-11-15 04:06:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8eeccb3b-5ddb-3cc4-9029-a37f02cfda11 | -10.10628 | -47.51706 | 2025-11-15 04:06:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e17ee347-78a8-3838-be3c-2dc71d09486c | -9.20568 | -44.16909 | 2025-11-15 04:06:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| da6929d9-70b4-38cf-bf2b-6cd12be0ccd8 | -12.00774 | -46.76616 | 2025-11-15 04:06:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 99fb50b4-1215-3530-851a-edf8561abeec | -9.09658 | -47.79083 | 2025-11-15 04:06:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ede6e0a3-eda4-3a73-86e4-30fef80eb7a1 | -10.99059 | -47.72819 | 2025-11-15 04:06:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 02a98feb-e5f4-3475-a7e5-9fe663995845 | -11.17011 | -48.14021 | 2025-11-15 04:06:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 6a0266b2-bac7-34c5-b7a2-d428aff2d583 | -11.9536 | -46.74922 | 2025-11-15 04:06:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89b0cfde-1a2f-3081-886a-7932663393d5 | -9.20871 | -48.59019 | 2025-11-15 04:06:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6963585f-c4a5-3ac2-96ad-1a14f2de4622 | -8.19057 | -44.8287 | 2025-11-15 04:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e036b46-05b1-36fa-8878-226a0c6770fa | -14.04347 | -44.06777 | 2025-11-15 04:06:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c304ab9-693c-365c-a554-02d40762a079 | -10.70014 | -44.50399 | 2025-11-15 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8612533e-74ce-349f-a899-285b8a4998bc | -7.38733 | -48.64819 | 2025-11-15 04:06:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82133955-17a7-34cb-bcbb-7a8b585ca114 | -7.76523 | -45.16372 | 2025-11-15 04:06:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| daa1fe65-ee0b-31e7-bcdc-d32ab6cb1149 | -9.75351 | -43.97738 | 2025-11-15 04:06:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48daa2a4-1d33-35d5-b8dd-dc2d189fc2a7 | -8.85182 | -47.33612 | 2025-11-15 04:06:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6aad7aa0-1a61-31b3-861f-92a38b61d8fb | -11.96117 | -44.96047 | 2025-11-15 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62d387bc-d7f8-36e3-b38e-8bf8447e1561 | -12.25501 | -44.91853 | 2025-11-15 04:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ed977d6-342d-3e54-9766-777638b04a2b | -13.6051 | -41.07579 | 2025-11-15 04:06:00 | NPP-375D | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4566e508-36fa-326b-9abd-37870f4a819e | -12.80566 | -46.45343 | 2025-11-15 04:06:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7db845c0-f156-3c62-837f-bfb26c3f92b1 | -12.42785 | -43.18005 | 2025-11-15 04:06:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f9ae5b1-4b17-38ae-8d72-0c77ebd52821 | -13.17901 | -43.05526 | 2025-11-15 04:06:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 54f6ac39-36f0-335a-997a-64216f8e582e | -10.62687 | -44.58948 | 2025-11-15 04:06:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0008165c-b0f6-3d78-9b02-68010e9ba6a4 | -11.61006 | -45.09221 | 2025-11-15 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13524b46-358a-3ed2-a6eb-017313b43500 | -9.35516 | -50.74358 | 2025-11-15 04:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dce98a3a-9c65-38c3-aec0-3890667debcf | -13.35199 | -43.74668 | 2025-11-15 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a014314-199d-376f-9375-31aaa5dedcea | -7.88858 | -48.39402 | 2025-11-15 04:06:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8671712a-1906-35a1-aa72-f724240b9ee1 | -8.85107 | -47.33844 | 2025-11-15 04:06:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c7a3c0b-dd0f-376e-92cb-6ede689f2a57 | -7.88381 | -48.39225 | 2025-11-15 04:06:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 727587d7-b1e5-36d8-bde4-2fe284dd4cff | -11.32775 | -48.52001 | 2025-11-15 04:06:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ddc54b2-1e14-3ffa-bb56-37f4d54935b8 | -12.38768 | -48.11053 | 2025-11-15 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 86813196-58d5-35ad-8832-089ec82b8f11 | -12.79276 | -46.38232 | 2025-11-15 04:06:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf00c209-2acb-3a73-8fcb-f72e4c77116e | -12.38473 | -48.10799 | 2025-11-15 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b9cf0c0d-6f4b-36d7-9ff0-c475214f06b0 | -9.4847 | -47.28515 | 2025-11-15 04:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56bcf79c-b938-3923-9fec-b9b6cebc3fed | -13.67748 | -42.51188 | 2025-11-15 04:06:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7d386751-e805-33ed-bd20-3d753ff1fb08 | -7.88875 | -48.39329 | 2025-11-15 04:06:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2ba09747-914b-3a64-90ca-eba804c68466 | -9.01433 | -44.17698 | 2025-11-15 04:06:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0f2cce28-1cf6-3a6f-ae2c-634b86390a58 | -10.17535 | -49.31682 | 2025-11-15 04:06:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9e2ced10-ded9-35b1-9839-a026605286b6 | -13.93592 | -44.147 | 2025-11-15 04:06:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bea46afb-7c16-32d2-aa0f-163200fa9b01 | -12.67356 | -46.77331 | 2025-11-15 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 31.2 |
| c85b5b1e-bb47-3cbb-b1c5-ddcc354be149 | -13.19617 | -43.22701 | 2025-11-15 04:06:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 87602bef-838a-3c85-83e3-a965261c4040 | -10.71177 | -47.94337 | 2025-11-15 04:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c79f255-63d9-3f98-ab8f-57e75b5422c2 | -12.49228 | -47.30018 | 2025-11-15 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e73b9e2-9cc9-3d08-b3be-08b5ea54979a | -12.70048 | -44.47846 | 2025-11-15 04:06:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32096c16-4ddc-3fb5-baa3-940bd44f1d74 | -12.99546 | -43.80803 | 2025-11-15 04:06:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 246fad77-f0e5-395c-9728-a9380cde07bd | -9.75059 | -43.97256 | 2025-11-15 04:06:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff2257f6-cc4c-3c3a-bc27-535235c2d1e1 | -11.1634 | -47.44401 | 2025-11-15 04:06:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f8129f1b-aac3-3d63-be0f-93e7b056eae3 | -7.27062 | -48.02977 | 2025-11-15 04:06:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aa2bb560-83fc-3545-a57d-671b281311d0 | -10.35545 | -48.73186 | 2025-11-15 04:06:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| e42aa5d6-04ae-31f3-94d4-2142af885d3c | -12.44087 | -47.88119 | 2025-11-15 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2da6653-a457-3665-8400-e32e2f988773 | -12.42566 | -47.89831 | 2025-11-15 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45f33f99-58e5-3310-9259-a3a64d25f958 | -8.66361 | -45.45976 | 2025-11-15 04:06:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ecdec44-dd7a-3c39-99e4-0b0aee3bdae1 | -7.88755 | -48.39966 | 2025-11-15 04:06:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7c8d56a7-a7bc-3563-b1b9-e255d0621605 | -11.71036 | -48.39362 | 2025-11-15 04:06:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73f61569-9133-3af9-be1f-03e9be315ce6 | -12.02574 | -43.72878 | 2025-11-15 04:06:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c2a4a8e-1e35-3467-a3ba-d7cda496da6d | -7.21681 | -47.97946 | 2025-11-15 04:06:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 95eecb60-9d98-3a88-a1de-0f571667b33c | -9.44654 | -44.86954 | 2025-11-15 04:06:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 24f60238-d6d7-3c0d-a49a-21484c154121 | -12.44449 | -47.88639 | 2025-11-15 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d3b00e3-bc8c-3812-aea2-440ff53ca379 | -7.35758 | -47.28611 | 2025-11-15 04:06:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74182387-b44c-39b2-ac17-cbd8d3a9ee7a | -9.44826 | -46.97493 | 2025-11-15 04:06:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45e323fc-af6c-33a9-94a2-b9c06bee2218 | -12.84273 | -46.43137 | 2025-11-15 04:06:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 28bb032e-a445-3408-ab7d-35502fdd17ae | -10.18076 | -44.39248 | 2025-11-15 04:06:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 41139fb6-f9e9-3ba7-a7c2-c4b248ac0ee0 | -8.74545 | -44.23605 | 2025-11-15 04:06:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 77b1feef-d390-38fd-9a08-33051448a654 | -10.57384 | -44.81489 | 2025-11-15 04:06:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ac0a5bcb-0de4-3e1d-8d57-0955d97e51d2 | -11.06983 | -44.97104 | 2025-11-15 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1289ccb8-05bc-3d39-89c0-2801ce51474d | -7.87984 | -48.41489 | 2025-11-15 04:06:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f429d2c1-92a8-367b-a64f-4b10f05f8cad | -9.48917 | -47.286 | 2025-11-15 04:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9dc30436-427c-3875-a4af-8cd8d576914c | -11.96228 | -44.95834 | 2025-11-15 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 18cd78f0-e833-323a-902a-e193c4c5aefa | -11.85605 | -49.21074 | 2025-11-15 04:06:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 658ca5cb-4a82-3c5a-a6c5-3452194a675c | -12.67423 | -46.76957 | 2025-11-15 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| cc7bc533-332f-3dad-912e-3985a111cd6b | -12.44006 | -47.88557 | 2025-11-15 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f021478d-2ecf-365b-9a5d-113eeda18232 | -11.7149 | -48.87502 | 2025-11-15 04:06:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e74cbfb1-3dc8-337b-bc9a-067c10b2a091 | -10.54296 | -47.99645 | 2025-11-15 04:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 486a1f76-67e5-3f29-981e-3c1d7a009618 | -7.87688 | -48.40256 | 2025-11-15 04:06:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f099dcd7-ee54-38d5-9c0d-8f45223b0ed6 | -10.31679 | -44.274 | 2025-11-15 04:06:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4090eb1-1784-3e38-a351-96cc024e5d1e | -9.48996 | -47.28148 | 2025-11-15 04:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| e9081c8d-7bec-3b04-9398-bb37c7280cf5 | -10.38054 | -47.74761 | 2025-11-15 04:06:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5d9e68e-1c0a-393d-abdc-72b77aff2c9d | -11.59244 | -45.1274 | 2025-11-15 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f99d24bb-b5c1-3e90-805b-58929b27e74f | -12.68651 | -49.11589 | 2025-11-15 04:06:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f763b1d6-a6b2-37fc-887a-4d5cbbf9d60f | -8.06368 | -47.17078 | 2025-11-15 04:06:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8cf874cf-0014-340b-b449-c61b80a6ac6b | -12.92473 | -43.0933 | 2025-11-15 04:06:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 014f5a88-aad4-32d9-8082-f2639de97b6f | -8.33962 | -46.69868 | 2025-11-15 04:06:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c99817b2-6674-3874-b469-76de7805b099 | -11.85206 | -49.22485 | 2025-11-15 04:06:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cea3bb75-3cee-3584-b4e4-c035171f898d | -12.4235 | -47.9006 | 2025-11-15 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92d4dd8d-cc4d-3680-8484-0b5ee12d03d3 | -11.73684 | -44.44973 | 2025-11-15 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df88342a-7e58-33cf-9cb3-52ddca604e19 | -9.93199 | -47.84196 | 2025-11-15 04:06:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 143e7fcc-856a-395e-aa5a-40fd46039ba0 | -9.21363 | -48.59108 | 2025-11-15 04:06:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d0ef6b4-0059-32cd-bab4-19517048fb1d | -9.09984 | -47.78264 | 2025-11-15 04:06:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README29.md)
