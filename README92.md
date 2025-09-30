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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7dbfd723-34e7-3a6b-9ba9-197650594012 | -10.63729 | -53.6942 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 217373c9-23f9-37aa-a570-1771ae5dd43d | -8.06091 | -54.8667 | 2025-09-30 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a5b4fe7-a9a1-3edf-92d5-6bf8ef50dce0 | -10.10514 | -47.78585 | 2025-09-30 05:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8dc956bb-87f3-3647-82ef-0150da16e6ea | -9.42616 | -54.71715 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ac50442-ed08-32a6-9ff0-4d2fa3929fcb | -12.84458 | -47.0079 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a325c678-2c9e-340d-81d4-614c1170e370 | -12.29255 | -55.14115 | 2025-09-30 05:08:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8cc3e56e-7bd2-3057-b045-0f75cabfa7a9 | -12.86826 | -46.90782 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a607e8f1-e945-3643-bde3-e9f2a6837de5 | -10.81812 | -45.3744 | 2025-09-30 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d792b72-ed7c-314f-b2f8-d228b2aac835 | -8.22884 | -45.50707 | 2025-09-30 05:08:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cadbec14-4b8a-35ae-9bbf-8deaf07f51fd | -6.7049 | -44.56245 | 2025-09-30 05:08:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5536a94c-2f33-34b8-85ac-2f7b65c099cc | -8.3194 | -50.87881 | 2025-09-30 05:08:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fea3847f-738b-3d0a-85ca-8312c6b4c631 | -9.04533 | -46.69783 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b268bcf0-c1c2-3349-8c0f-c336eaeb5011 | -9.39762 | -54.72033 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b8f1a8d-dbb2-3989-a8ac-1bd2382cedfe | -10.41249 | -48.16808 | 2025-09-30 05:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df17a02c-7fed-3dcd-bb29-9731b084d46c | -9.39646 | -54.70494 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39d05781-d73c-3ffd-aea0-3366377d6f33 | -12.85085 | -47.00426 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aef659ab-c880-3901-91de-1370410d1ddb | -10.95527 | -46.49964 | 2025-09-30 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 77ca71dd-20e3-33f7-be0d-0d57f6062ac6 | -11.17224 | -47.23376 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca4681a8-ec34-35d5-a3a2-6e426c19b689 | -8.49995 | -47.25486 | 2025-09-30 05:08:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 815d8c1a-8a2c-31f7-859d-48b6c563f8ea | -11.06279 | -47.82218 | 2025-09-30 05:08:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e19238d2-352d-3f25-8420-bb05068e4d41 | -13.09554 | -47.02959 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b71615ce-657d-360a-a279-c6cdce698427 | -10.92318 | -54.31696 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91d7b176-417b-3126-9618-4001bdc4a01b | -9.39989 | -54.70545 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aade704c-949a-345b-a943-1d29cafbd6b8 | -7.82947 | -47.0085 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f92965c-10ca-33e6-83dc-b7cab53e6b7f | -11.41981 | -44.90442 | 2025-09-30 05:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2d47aea7-f848-382b-9e58-f4466608c654 | -11.87811 | -48.05441 | 2025-09-30 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73fd2864-5c1f-3370-b497-9dceace2163b | -6.32383 | -53.17271 | 2025-09-30 05:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c46042e6-3ce1-3284-ba52-28e63abca9b5 | -13.04153 | -47.08194 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c72e3b2-cf6e-32e0-856f-7e1dbfef903c | -10.62945 | -53.69726 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ab3bb0e3-91f0-30df-9785-1433b30646dd | -10.18792 | -52.55327 | 2025-09-30 05:08:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c9640e6d-41af-3519-b5bc-721f62d164a7 | -10.95133 | -46.47998 | 2025-09-30 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 47a2c301-32f2-3fc9-ba57-571133f9d09d | -12.88168 | -44.68482 | 2025-09-30 05:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29754d3a-ae43-351e-8f53-2ffc72c52128 | -10.81306 | -45.36409 | 2025-09-30 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41210859-224e-3908-b989-467ddf97d39d | -13.4111 | -48.14868 | 2025-09-30 05:08:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e9a9569-910c-35bc-9781-70b290c468db | -10.06647 | -48.19383 | 2025-09-30 05:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1116dc0f-f94f-3aa9-b724-3564b086a952 | -9.51086 | -47.6925 | 2025-09-30 05:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb692fa9-7118-3cb9-9d1b-6e2ee0583550 | -8.61765 | -54.98866 | 2025-09-30 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4fe71629-3395-3929-ab39-9d065db4ec92 | -7.11661 | -45.55232 | 2025-09-30 05:08:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| adfd8577-d383-3df7-9c2a-4b96587a41ea | -10.89331 | -53.74651 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a069221a-92e6-3729-a838-bf7adebba32e | -12.1555 | -47.77381 | 2025-09-30 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a920044f-fe43-37d2-8254-6c541a0d7c8d | -11.20133 | -47.2225 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 448b9893-72dc-301e-8029-f169b894f1f5 | -10.64152 | -53.69059 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f33fc4e-25fd-3eed-b90d-8ee28ca357ed | -13.23674 | -48.45399 | 2025-09-30 05:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ddd0170-da41-3b7f-bd72-21fd1eef6ed0 | -11.05152 | -47.65589 | 2025-09-30 05:08:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 695c8aef-99b6-33c6-a93f-cefea0584c27 | -6.69992 | -44.55265 | 2025-09-30 05:08:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0661123-11fc-3d9a-844d-13aede531d4b | -12.22393 | -43.75073 | 2025-09-30 05:08:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a830f969-9904-3981-a360-6ec244348287 | -13.21002 | -50.93662 | 2025-09-30 05:08:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ed79d26d-f835-3f64-8146-768d3fc40a04 | -12.97048 | -48.41476 | 2025-09-30 05:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8354ee4f-8e7d-3bef-8f67-1b6a2d75626e | -13.64705 | -47.33028 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac25116a-8b0d-3679-8170-f2bca2c6a7bc | -12.83793 | -47.01482 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34e9eee9-f4c6-30c8-b65f-394a3c08ab15 | -10.95475 | -46.50364 | 2025-09-30 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7350d338-7921-3ae1-870c-8b08cc01c7d0 | -10.39851 | -48.1392 | 2025-09-30 05:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 517f286b-bed7-3a9f-afa1-bf9ff8f5edb3 | -8.3215 | -50.87972 | 2025-09-30 05:08:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 731887b2-0b02-34e6-86cf-17c110fe49fe | -11.93269 | -47.99627 | 2025-09-30 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| adb7c720-c89d-3748-afea-f1c18dda47dc | -6.37254 | -45.64791 | 2025-09-30 05:08:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d3672b1-0310-3125-bccf-518449728964 | -10.80685 | -45.36331 | 2025-09-30 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c2225ba-c474-397f-a7ac-df596f4ed256 | -7.70431 | -55.45234 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd43b670-aedd-3d15-acfb-fc82f412dc20 | -10.19175 | -52.55385 | 2025-09-30 05:08:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0ffcc68b-d981-3ef3-b4bd-3f9968a62263 | -11.65964 | -47.48651 | 2025-09-30 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7129e02b-0127-35ad-9a94-0f48308acbd8 | -11.25718 | -47.22624 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 622b7943-b112-31df-b68a-c11fc116d3a3 | -9.42274 | -54.71661 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 702e761e-9722-3fdf-a4c7-4ebdbe24f9ad | -10.40563 | -48.16422 | 2025-09-30 05:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2a18127-f36a-3c97-bb85-926bb9059db1 | -8.26439 | -45.51318 | 2025-09-30 05:08:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dda14436-5c96-39ce-aafe-b62dfe3fec4c | -9.41586 | -54.69267 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba8cf744-112f-3516-84f3-10e8a0f3b776 | -7.01474 | -44.47184 | 2025-09-30 05:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76735c7d-8b15-3307-a268-5503974fe9be | -8.85828 | -46.59114 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| febe0788-a67a-3c68-8d7d-e8b7fa3cce3c | -8.86292 | -46.6846 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4fd51891-a78a-3b7e-ad69-33825081fe71 | -7.82633 | -46.99124 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f10a701b-f39b-3e64-a1ca-e9d85d5cb469 | -11.89522 | -48.04684 | 2025-09-30 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c1046e2b-c0e7-36d8-8ede-56d2dedae840 | -11.90939 | -48.0621 | 2025-09-30 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 355689a5-49ec-3eff-a465-d567d1f2e95e | -12.22955 | -47.79739 | 2025-09-30 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c1a80c2-2463-33d7-9850-f84dddfd1b07 | -11.15279 | -54.12842 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| e36f09b2-4909-3204-8fff-adb3e176d94a | -12.45392 | -54.30629 | 2025-09-30 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b2a415c-1941-3722-b97f-1ebe0952fcec | -8.51043 | -54.59841 | 2025-09-30 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b734013-c289-3b50-8d51-a25e06347512 | -11.21476 | -47.20515 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 999718b0-6af5-3278-bbf3-780c2951f55e | -10.06176 | -48.19019 | 2025-09-30 05:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5640eabb-bea2-3fd6-b58a-b36ed96408b8 | -5.23438 | -56.01497 | 2025-09-30 05:08:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 24e51764-1e77-3a02-80e2-aa14a0f10f51 | -6.50896 | -45.21562 | 2025-09-30 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2cd52dd-f621-336c-819d-517d7a8a7eab | -12.82238 | -46.99855 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70223388-b1cc-3dcd-9d9c-82fa87c92691 | -11.74857 | -46.83939 | 2025-09-30 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25af5fb7-1326-3aab-8e4c-cd86176be75e | -7.34833 | -50.48376 | 2025-09-30 05:08:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b86b65c-393e-3460-bc6a-da4adb6e734f | -10.40468 | -48.17134 | 2025-09-30 05:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 248f20e2-6a0a-3592-a56a-88fc0f19db41 | -13.57688 | -48.05927 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 467b0cb2-45ba-3afc-95dc-5fc1929cff10 | -13.34418 | -47.81664 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd878016-b6d4-3bbc-af1e-bf609604b3ed | -8.14887 | -46.38113 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d72a9609-70e3-3cb7-9a9b-a889dddf7af0 | -11.17728 | -47.23826 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 98a29745-7c3d-3a99-93c7-d1b976a1ca0c | -9.32333 | -45.69624 | 2025-09-30 05:08:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6f295e6-a5d5-308f-a2cb-8f484274bbbe | -11.98025 | -46.57937 | 2025-09-30 05:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8a2b170-2488-3594-8dcf-1d05ddf6a08a | -11.14272 | -54.12273 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ae926087-2069-3af6-b8fc-93fc31b1a9ac | -11.8855 | -48.03868 | 2025-09-30 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b600b50a-8438-3f19-a711-9b96f6403b79 | -10.84238 | -47.96299 | 2025-09-30 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b181c61-8b0e-3345-bb36-8d3d3607866f | -13.37195 | -47.31517 | 2025-09-30 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 830c239c-ce50-3dea-970b-59ae29f263b8 | -11.44263 | -43.51273 | 2025-09-30 05:08:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b006787-bc47-3597-8517-15b90fd9db64 | -10.95081 | -46.48426 | 2025-09-30 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c31375a4-35db-3efe-9b9d-81be5624ffd7 | -10.3806 | -48.15565 | 2025-09-30 05:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41be992f-95f6-337c-a976-a82229021fca | -6.75046 | -50.92249 | 2025-09-30 05:08:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d519fbee-0eb8-36ba-84be-95535022eca5 | -6.8897 | -44.52468 | 2025-09-30 05:08:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a1748139-7ffb-3d51-a834-8bae279a5045 | -11.72224 | -44.44321 | 2025-09-30 05:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dcdee707-fe96-3b9b-86f6-cf41b7fda748 | -8.3681 | -55.20388 | 2025-09-30 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60373d78-ec41-3b8a-aff7-9e7fd815499e | -5.98381 | -51.9119 | 2025-09-30 05:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README93.md)
