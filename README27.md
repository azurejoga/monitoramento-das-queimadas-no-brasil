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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a70c1346-b16d-329e-aa4c-216d2367e768 | -3.63597 | -54.3209 | 2024-11-22 04:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 646dca30-223b-3ea9-af30-47ad02e4b870 | -3.3444 | -42.7872 | 2024-11-22 04:12:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 9af3d18a-e0ca-3812-ac51-bba3f8b30aa5 | -1.97514 | -46.36674 | 2024-11-22 04:12:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 781aaddc-644e-336c-b55b-021a1926425c | -3.84953 | -52.3493 | 2024-11-22 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 342fe08a-06a8-3eb6-a5d2-f5e04bb3efc7 | -3.32913 | -54.09783 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e7c9725-62fb-3d75-b337-2f93c10e2941 | -0.93055 | -51.72101 | 2024-11-22 04:12:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67d36696-0d7d-3ff4-9547-bad2af61b9fe | -4.00631 | -43.25112 | 2024-11-22 04:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 176bf15a-88ac-380b-9d4b-4a83f5138f32 | -3.76304 | -46.1211 | 2024-11-22 04:12:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 769915c4-2437-324a-bb1f-2574e0750471 | -7.74144 | -38.61109 | 2024-11-22 04:12:00 | NPP-375D | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 07a51aae-70e3-34e7-a025-c8dae1506ef8 | -2.08859 | -46.28321 | 2024-11-22 04:12:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b30a9ad5-1c39-39fa-9e72-a03473312299 | -3.10256 | -53.98869 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb4f6063-9a89-3e43-9255-2a35e14a8114 | -3.29394 | -46.15281 | 2024-11-22 04:12:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a5e0fa7-49ed-3b91-b173-03761955478a | -1.20054 | -51.95525 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f3a12014-b503-3196-9ed1-dca043752425 | -0.27045 | -51.57483 | 2024-11-22 04:12:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d966e051-7f69-3993-905b-ecbec977525f | -2.66733 | -46.23692 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9127fb88-dcb9-331c-afe1-d04e182404e8 | -1.23037 | -51.7403 | 2024-11-22 04:12:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e86572c8-e3aa-3608-b866-9ccc4375706a | -2.42711 | -46.52 | 2024-11-22 04:12:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5716cd49-66e5-3cc9-be99-cb97b64635e7 | -6.18422 | -45.44766 | 2024-11-22 04:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6f84588f-52fd-3aa2-8f85-f5ae1338ed63 | -2.66075 | -46.15457 | 2024-11-22 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 900b7f40-8bfe-39b1-88ec-ad23a34a975f | -1.52104 | -47.06248 | 2024-11-22 04:12:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c88903f3-2e4f-3af1-9846-e09a37bb4d1a | -3.64391 | -51.45909 | 2024-11-22 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8fb69f20-dd4c-3df5-91e7-4a4b1cad0956 | -4.68819 | -45.66676 | 2024-11-22 04:12:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdcf34ef-2f31-3a36-9e56-3657b189ecba | -3.46364 | -45.91222 | 2024-11-22 04:12:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9610bf92-795e-3e50-b545-7f3a2a13c0aa | -3.46063 | -45.90723 | 2024-11-22 04:12:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 694ff6c1-211e-3209-b95e-5c8f8c33cc37 | -2.79387 | -45.94915 | 2024-11-22 04:12:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be8a1e53-6c34-3b43-a8c2-d3484a9a478d | -3.58134 | -54.5211 | 2024-11-22 04:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 549dfb92-0d54-30cc-a5e0-866ffc4fcc77 | -3.23765 | -54.24005 | 2024-11-22 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| f4584e4e-2fc8-310b-a738-56e748d2027c | -4.09213 | -46.2092 | 2024-11-22 04:12:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e530125-a586-3324-a4e9-d515cb03f603 | -1.77022 | -53.60837 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 46312287-8b3d-3c67-925e-8fda832f4773 | -3.20909 | -54.25222 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0e22fb73-8d37-3bd1-94e2-3c5c7b5b8517 | -4.0129 | -49.91382 | 2024-11-22 04:12:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 25647e7b-59f3-3a14-88fe-72fddc8d219e | -2.69986 | -46.22066 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 27934d87-c463-342d-8104-22890cf451d0 | -4.68887 | -45.66253 | 2024-11-22 04:12:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c900c034-acfb-3e0c-a15a-bf249c34d33f | -2.0029 | -54.51793 | 2024-11-22 04:12:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3f404add-c769-3016-91c7-282a07414e12 | -6.82072 | -46.77417 | 2024-11-22 04:12:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 89a7cbc4-6277-398e-a0ea-61e50efcb4bb | -2.6082 | -48.24551 | 2024-11-22 04:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75083505-fce7-3541-81e3-6237fabdac72 | -3.19015 | -46.5535 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d4c9227-0ebf-39c3-a54b-33a9834cab5e | -2.70564 | -45.23488 | 2024-11-22 04:12:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73e6cacb-46c5-37be-bb04-8f00ca338767 | -3.69329 | -50.21985 | 2024-11-22 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d428f12-bd86-315f-898b-406d34c49266 | -3.6786 | -52.37004 | 2024-11-22 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76427e48-bca8-3ede-a92d-f33cc01a8673 | -4.1349 | -54.66148 | 2024-11-22 04:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 11e8ed6b-cda0-3dcd-913d-ae8ad55c1a0a | -4.43342 | -46.58553 | 2024-11-22 04:12:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91bab04e-5317-3e58-9486-fefdf1fcf9cd | -4.10378 | -42.45969 | 2024-11-22 04:12:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3f5c5b85-f92c-3b10-b5d0-accba237e13f | -1.19479 | -51.95431 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| bcb35350-ba87-3ceb-a5b1-c7b4302c4e9a | -2.69443 | -46.08905 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c9bbe8d-8795-323a-8797-507c85ad4fa5 | -1.44629 | -53.3877 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cc38d4a0-c86c-3b8f-99e1-f6b6b38b1c98 | -6.92309 | -37.10671 | 2024-11-22 04:12:00 | NPP-375D | SÃO MAMEDE | PARAÍBA | Brasil | 2514909 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1d06e9c7-7415-3e78-bc25-34f93283f5ee | -0.80695 | -51.78543 | 2024-11-22 04:12:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d347c4a-6478-3115-8065-bc8e5fdf4a40 | -3.28212 | -53.82635 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fabf7e53-8d43-317c-80e1-0708ba8c8076 | -2.34825 | -50.36932 | 2024-11-22 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a31f2038-7aaa-389a-9882-05a5510227c7 | -4.01204 | -49.91887 | 2024-11-22 04:12:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e01c17e3-164e-3d79-8144-f528946f2279 | -1.59564 | -53.81224 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| bd98046c-bb27-389d-969b-c5fd64a50aac | -3.7919 | -44.01395 | 2024-11-22 04:12:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffdfc37d-ae74-302f-8c0e-9d9ca83e08c1 | -4.54302 | -42.97882 | 2024-11-22 04:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fbf7afc8-b7bc-38eb-a03d-5e1c08f17431 | -4.18398 | -53.58003 | 2024-11-22 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3bdc44d-db4c-345f-afb9-13f265031f3a | -2.44034 | -46.53724 | 2024-11-22 04:12:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e902b9f-f3e7-38b9-b720-5f6ffdb4f44e | -1.74545 | -46.30153 | 2024-11-22 04:12:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de75147e-e81e-3fac-a2c9-6b65b408cf90 | -2.69914 | -46.24933 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a209fd7d-1b01-3f38-a2a5-a7e43e7e37be | -4.23514 | -48.62777 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 437be168-ded9-31f3-8973-723b8e0076af | -0.95453 | -51.71697 | 2024-11-22 04:12:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e98e3dd1-b15d-3201-9081-2719815c2846 | -5.81546 | -44.7527 | 2024-11-22 04:12:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d268a02-5edc-392c-8927-298c035bd2c1 | -3.34172 | -53.3314 | 2024-11-22 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1206f901-a940-3470-9524-8a73db001adb | -3.50673 | -53.79649 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10ec3a17-e4b3-37ef-95e6-24264a1405fb | -0.34418 | -51.56423 | 2024-11-22 04:12:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 78a966ef-8494-3f53-b1f6-64300ba5d443 | -2.70643 | -46.08409 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ad11f33-cc92-30bf-a36b-b72b3289aee9 | -3.9001 | -40.97533 | 2024-11-22 04:12:00 | NPP-375D | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e24fab32-cf89-3a78-a083-9237cb5d33b3 | -2.35332 | -50.37013 | 2024-11-22 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a985ff4e-1faa-3d62-9ecf-142bfeb61b46 | -5.09265 | -45.93679 | 2024-11-22 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25d31898-9355-3263-a9b6-3b0ae522945d | -4.25054 | -46.11433 | 2024-11-22 04:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 728c4cab-08a7-3955-a973-f4614543d5b3 | -3.7885 | -44.01341 | 2024-11-22 04:12:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64abe103-1a32-32a2-a1bf-17325a4f5ba6 | -4.24983 | -46.11871 | 2024-11-22 04:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b37c8e3d-9cc9-36fd-bd99-2d3a84c64310 | -4.49178 | -45.80003 | 2024-11-22 04:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c368944-723a-3d0f-9ac1-a88a94d085e1 | -2.70524 | -46.23587 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8da78f18-add8-30b5-8f47-c74fbbe5fa57 | -3.73385 | -50.43961 | 2024-11-22 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5365c7ca-519e-3f1a-90be-d246d2de83cc | -3.21548 | -54.2536 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f16285d0-1380-33fc-a53f-52623a7574f8 | -2.63739 | -46.20318 | 2024-11-22 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d904a0d3-bf47-3822-9670-590c9fcb93d7 | -3.72981 | -50.43322 | 2024-11-22 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32ade719-dce9-3b7f-9b1b-f503a9fd8afc | -3.5059 | -53.80137 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b0ebcd52-897a-30cb-ab1e-a9c0f013eb0b | -1.2575 | -53.35891 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45060fb1-432c-3e70-8f2b-5b00e0fbe0d5 | -2.70265 | -46.08348 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68609c35-265e-3458-8333-7e3a70c92fe0 | -3.88996 | -46.66149 | 2024-11-22 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab199be9-b484-3048-9824-34bac6ed8ed0 | -2.44267 | -46.54768 | 2024-11-22 04:12:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 263d117c-974a-3b86-84c0-f9070cd72235 | -2.78743 | -48.10377 | 2024-11-22 04:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6bf34151-b1a6-34fe-9282-9855a567a4f0 | -4.57944 | -48.01629 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e87d3b1-3fd4-3c1e-8647-4e5cfab4b7aa | -3.88307 | -43.34719 | 2024-11-22 04:12:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90c685c9-be32-3c3b-bcad-4f26aa27216b | -3.24129 | -54.25762 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| b5d92bf7-d3e9-3a95-9318-e531b9304d8d | -5.46249 | -46.47994 | 2024-11-22 04:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ceace33-ac9f-38f2-8ca0-b181041c2777 | -4.43401 | -49.59042 | 2024-11-22 04:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fbf8acc-6969-3fee-bee5-dd158d5e5612 | -2.78447 | -51.40771 | 2024-11-22 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7c4ac69-956d-3887-a730-ad18b3349e6d | -3.13525 | -44.86349 | 2024-11-22 04:12:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57c35678-59c2-3553-bdf8-0ee89588fb40 | -1.25913 | -52.06742 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93778d96-2c34-3ecf-9d6f-7d5a568c989b | -2.17152 | -47.95182 | 2024-11-22 04:12:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fd1f1ca-6b15-32cb-861c-2d5a1029c849 | -3.04447 | -54.8491 | 2024-11-22 04:12:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c1f5462-e359-32f0-bd8e-ea5b09c5b967 | -1.61748 | -52.58677 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 878ec96e-cf9d-3ca7-a096-f6d6a1682ea4 | -1.80386 | -48.46751 | 2024-11-22 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8def78a-3632-3045-a06d-8c3d4bfb08cf | -2.62001 | -46.26299 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35818eae-c861-3712-a1b3-53ae572bca74 | -3.53049 | -51.1013 | 2024-11-22 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 121d78c9-bb68-3750-a2bc-2b699509df42 | -4.19892 | -53.49382 | 2024-11-22 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 165ade1f-2de3-3b8d-8cb4-996d0ab0887b | -5.19795 | -44.22236 | 2024-11-22 04:12:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2e808ef5-a014-3c3a-881f-e240f2569b20 | -1.18905 | -51.95335 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |


[Clique aqui para ver as próximas entradas](README28.md)
