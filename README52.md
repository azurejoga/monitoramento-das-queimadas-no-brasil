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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02036fd7-d3a5-33e2-82a6-16900c3909e7 | -6.36328 | -43.53646 | 2025-09-06 04:38:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84b3b1af-600e-3f1b-a9a1-9d78248d6511 | -5.85082 | -46.10511 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ccc514eb-9c5f-3604-bc16-87ace0525d6a | -8.88436 | -47.25702 | 2025-09-06 04:38:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2f4d7c1-5d01-31da-8e33-deddbd841a22 | -5.90528 | -57.73122 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd8b2765-b11b-3200-bacc-87132bbdad51 | -5.47537 | -45.60183 | 2025-09-06 04:38:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bb94067-031e-3385-8720-873e00c8372c | -6.61318 | -43.98339 | 2025-09-06 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d4289e7-88df-3cc5-b04f-91f1fee16bdd | -6.06305 | -43.342 | 2025-09-06 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d7c8081b-3f72-33ab-b69e-88670ee6415c | -7.79027 | -52.13104 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20de9869-7978-3099-add0-4e1f39105546 | -6.20419 | -43.41753 | 2025-09-06 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 656ebef5-8db1-3342-b8cb-9caced0aa4e5 | -5.98343 | -44.73229 | 2025-09-06 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3b6c1a2-4669-3880-bd77-10f9a340e7b5 | -7.81222 | -47.5077 | 2025-09-06 04:38:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 559c9c58-e938-3f3d-bd38-31ed0c72d58f | -7.00831 | -44.95284 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c86ea46-2137-3454-b06a-0f0ab8b38c00 | -7.69418 | -50.2846 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5ca00cb4-5de9-36f8-b2ae-02ae16222a4d | -6.32601 | -58.17229 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2ee5cf5-f0fd-31fe-b8f9-9898dbb0b2a4 | -5.8669 | -52.17057 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf349a30-e1df-3810-9201-6199b5ef2054 | -5.98489 | -47.61938 | 2025-09-06 04:38:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2aa848f3-7bf5-3af3-84da-8e5a5b2f8782 | -9.44551 | -49.4494 | 2025-09-06 04:38:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fbca74f5-3412-3a0b-83a9-8ebcbebc2316 | -5.96758 | -44.73266 | 2025-09-06 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d89437fe-33a5-329c-965c-3cd01560d06d | -8.93873 | -48.64899 | 2025-09-06 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 849f7a35-d5c8-3a77-b756-35a4f5d4457b | -6.15353 | -43.17622 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f97e3819-7fb4-3370-b254-4ff5a3f3de72 | -5.61747 | -42.87872 | 2025-09-06 04:38:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2b10b61e-fe4a-3206-a479-8bbbd1c265cb | -6.15834 | -44.24302 | 2025-09-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11fa52c2-deb0-37b2-9cfe-8c9601e69eea | -7.79844 | -45.42916 | 2025-09-06 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aaa286da-d5e3-3013-b834-e9e34c1b48f3 | -6.66547 | -48.40213 | 2025-09-06 04:38:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 85429e67-8284-3e69-aebe-71dbb80b3daa | -5.69435 | -53.75494 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc09ab5c-a75d-3b49-b075-77ac1d255c00 | -9.18462 | -49.11914 | 2025-09-06 04:38:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f798960-a40e-3d17-8849-19c6324922b7 | -8.86129 | -52.01646 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 081edd4f-37b9-3951-a173-75f9d62366c7 | -8.51558 | -51.31261 | 2025-09-06 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae1bff35-e8f2-379c-8492-99175deae292 | -5.8682 | -52.16251 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f85dbf7b-5638-37a7-acd6-b0c67bfb00e2 | -6.18897 | -53.24947 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59e66e00-c90e-36e5-b074-6bcbd8eeb32b | -2.5539 | -47.72925 | 2025-09-06 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02314575-9c65-3f6e-b60e-c9ca2fae015d | -9.08218 | -50.42163 | 2025-09-06 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96124355-443b-391d-9049-69e72b9ef020 | -5.76472 | -56.51236 | 2025-09-06 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01baa4bc-e106-3612-8bf9-a259e4394702 | -8.35425 | -52.51581 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1029e038-bc09-327f-8f45-4abaa3154712 | -9.06064 | -50.45034 | 2025-09-06 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 23939307-4467-3d2b-8051-082a2debc578 | -6.15475 | -43.16783 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 576ccf17-69a3-3789-aacc-9bbd95221373 | -9.07776 | -50.42806 | 2025-09-06 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ad77aa3-4932-3a0b-b763-5b8f7fafcb49 | -9.08322 | -47.01839 | 2025-09-06 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 41690be7-1a50-3833-9233-aefde02adfd0 | -5.67661 | -43.57235 | 2025-09-06 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2dc47f2a-cbd7-377f-ab0d-72618d10817e | -6.19978 | -44.18739 | 2025-09-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0e7a168-e43a-3edf-af04-3598c0815e9c | -6.8165 | -52.80865 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a4c0583d-6481-3392-ac10-862ec1640aa6 | -8.34659 | -52.51843 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ecac0cb0-31b2-30f8-afa2-c49d2002d7f4 | -6.04955 | -44.93706 | 2025-09-06 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af24801e-a909-35a5-89d5-4716995a40ec | -8.08189 | -47.57001 | 2025-09-06 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f130220-9d42-3f97-89b7-f762115797ac | -7.71729 | -50.33153 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae6dc881-7157-3dc6-948f-45d05942e57d | -5.7291 | -49.28723 | 2025-09-06 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b08d85ac-a609-3bc7-8d1c-d5add68cd3a3 | -9.31235 | -45.40178 | 2025-09-06 04:38:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fde6c95-716a-3ab4-ac99-f85fb17e3606 | -5.85019 | -46.10918 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a283ca13-127d-3653-b00f-61845fb15323 | -9.82975 | -46.54013 | 2025-09-06 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e8c77978-e694-3452-9bec-955b2b1f8264 | -8.54244 | -55.242 | 2025-09-06 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94c638e4-3474-35b1-a847-7f5c768cde17 | -8.43443 | -47.31861 | 2025-09-06 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a459ad3-dc80-32dd-a1ee-6873747e3efc | -6.00167 | -46.69957 | 2025-09-06 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 443a3078-4464-3437-a991-846d8f7148a9 | -5.86755 | -52.16653 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 073e0ad3-bbb3-3634-ae80-5ff0a7af1378 | -7.71242 | -50.34119 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8535a017-88ee-3df8-b1e3-eddafdbd0962 | -5.10349 | -56.14117 | 2025-09-06 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f9cb0f3-84f6-3674-8361-ea8c7c8ed79b | -7.68976 | -50.29102 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ffcf377-4477-3770-99c0-a2d8d85d7858 | -6.28052 | -53.44535 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 94fd1f4b-0e9f-3cf9-a70d-847811c65bb1 | -7.68645 | -50.29049 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cfdd5fcb-e149-3b62-a34a-a0e55cc36870 | -5.89971 | -57.73339 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85900ea0-66f2-3647-b0bb-7e6389b149f2 | -6.0052 | -46.70011 | 2025-09-06 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5156d188-8da7-3915-9ba7-1dc546c712e8 | -6.45238 | -44.67562 | 2025-09-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75490ec3-9107-32c2-8b79-b61b96a3fd3e | -5.72936 | -43.91545 | 2025-09-06 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f43dbed-32fb-3060-8210-8556ea81faf0 | -4.89807 | -55.99115 | 2025-09-06 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6dfff356-e7ef-3e8c-8cf5-6e87e1e55fcf | -5.94902 | -53.7986 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 190e69a1-bdde-3bda-affd-e6f92d8c7fe2 | -6.66601 | -48.39863 | 2025-09-06 04:38:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5a133d62-9154-3f35-9bea-7fc8a41c845e | -5.93368 | -43.02042 | 2025-09-06 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 78495fa6-3a87-36a3-87b3-bebd56031de5 | -7.76311 | -50.72361 | 2025-09-06 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ca34a81-08b5-3c9a-a815-42a7f1ee7df3 | -7.32594 | -48.50009 | 2025-09-06 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b189399-27bc-3589-b856-73d380392b13 | -8.87532 | -47.9201 | 2025-09-06 04:38:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2d8d2e2-964c-3064-87d5-b8e2fd83e5ad | -8.91055 | -45.11027 | 2025-09-06 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e9e4794-9a48-34b1-bd72-85b1fd975336 | -5.8369 | -44.11409 | 2025-09-06 04:38:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c177f8c9-b8ef-3ec2-9501-fe10fc522d0d | -4.26954 | -48.65418 | 2025-09-06 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c37ce720-164b-3295-a88e-8f196bb7f15b | -9.07721 | -50.43155 | 2025-09-06 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 95099248-7863-35bd-9400-0984ce49fedc | -7.60393 | -44.67258 | 2025-09-06 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86cc7254-7ff6-3d5f-9026-aa4becf60a1f | -4.89351 | -55.99039 | 2025-09-06 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76444a21-cf7f-3de1-b1e0-126d8b0e64f6 | -5.00751 | -56.0392 | 2025-09-06 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 108731b2-4174-3699-92ca-0d258994f975 | -8.05064 | -52.37936 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92ea4eb3-0841-3e13-a666-9d6a54b1ec2e | -8.85848 | -52.01214 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 518822c7-c916-39da-bfe6-3fa3dea3744f | -5.9048 | -57.73404 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7af6e954-577b-3bd9-b095-152571c34362 | -8.9348 | -48.65207 | 2025-09-06 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 704f6420-125b-3542-8696-a0f74150f424 | -5.84211 | -44.10728 | 2025-09-06 04:38:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d083a5c0-8dfd-306a-a3b5-9e085e46f712 | -5.92751 | -43.7179 | 2025-09-06 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19280704-639a-3629-97ac-2f922f6a4716 | -7.33624 | -43.94212 | 2025-09-06 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e14e72b-5cf4-3ea7-981b-889828a32448 | -3.80693 | -50.03414 | 2025-09-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 112f2b18-5619-36ea-95b6-b47f9285a265 | -8.63842 | -45.74918 | 2025-09-06 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a28d8f7-4c41-3a92-9190-f33c375daf7c | -5.93074 | -52.00118 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e34fcb48-3bf4-3610-8dce-35c7a20babcc | -5.95943 | -42.55105 | 2025-09-06 04:38:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| b956f999-b84e-3998-97e8-2c821b9c8482 | -6.22209 | -42.64202 | 2025-09-06 04:38:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 9e81b947-0d80-3c83-bf20-f7ddcdf82d16 | -5.86598 | -46.10306 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27ffa587-d06e-3d5b-9747-b3eb7bd3d9ef | -8.02302 | -45.42734 | 2025-09-06 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cb6b7c27-1322-3e56-8afb-7db60ed2678b | -6.61371 | -43.97985 | 2025-09-06 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 984bbf42-f1af-3355-a707-280cc5b40976 | -9.05346 | -50.45276 | 2025-09-06 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0bda0a3a-de02-35b9-97b0-4808c8dee2ce | -6.60484 | -43.98219 | 2025-09-06 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 56dfcf7f-785f-3105-9380-bd13de075fef | -6.1972 | -53.24619 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ca77b6b9-1f7b-3f0d-b2fa-d37e92db6504 | -5.92676 | -52.00103 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a8ea1ee-cf36-3dc2-9df7-881ae2cf739a | -8.5229 | -51.31005 | 2025-09-06 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35a367df-3f3f-3bfc-99ad-e0ac0ef5f69a | -5.99993 | -46.6871 | 2025-09-06 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fdc7e22b-cda3-3785-8681-71af52302de5 | -5.91634 | -57.72737 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7993cb88-8872-3051-9392-cdcb67cdac15 | -5.79296 | -45.62519 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83927bd8-7bf0-356e-92d6-5d241f28fd58 | -6.01656 | -43.69864 | 2025-09-06 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README53.md)
