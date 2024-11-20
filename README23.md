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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1db6c783-ae2e-3c41-9ee0-3c6dc1801062 | -2.51369 | -46.40398 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dba3c017-8394-3868-9712-89c63dfa87be | -1.88622 | -50.96627 | 2024-11-20 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 6000b22e-26b1-3b7d-b45d-217e03eca196 | -0.96088 | -51.72538 | 2024-11-20 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9262ec44-3107-3a04-be0b-fad597db9634 | -1.68787 | -50.19798 | 2024-11-20 04:25:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0231737-e921-3264-bb03-d11bb608f967 | -1.97047 | -52.09985 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4810e2d9-fca8-3eac-be08-c97638e63836 | -3.54825 | -43.96921 | 2024-11-20 04:25:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc21f601-8c72-3d95-8289-bf0725797b7e | -0.91571 | -51.78119 | 2024-11-20 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3fd093bb-a61e-3525-81ab-1c8eea2340d3 | -1.96896 | -46.42899 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d287f1ea-0753-35e6-a6d1-1691b68d6726 | -2.16244 | -46.38809 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e2ecf2b2-3f49-356c-9d08-92e0e4ca030b | -1.93677 | -46.41689 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b9dc63d-5998-3517-802e-4854f62f005b | -2.68965 | -46.08421 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04014c68-0f3e-353e-a74e-18226b3086c8 | -2.26291 | -48.40997 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6580a67-fa63-3f38-a836-b0998d666d3b | -3.18204 | -46.43763 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b6d67609-bd35-33c1-a2be-c3000ba9e2f1 | -2.68619 | -46.19307 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a01fc67-30ca-3450-8a13-ea28a090b5f4 | -2.6902 | -46.23258 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 703e03dc-bacb-3682-8f8e-6eaca7241337 | -1.32071 | -52.39921 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d8ebae74-40da-3f2c-94af-6a7829f0b991 | -3.38802 | -44.43807 | 2024-11-20 04:25:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e37d3517-5b57-389e-9b09-c318824cfc7e | -2.63282 | -46.05782 | 2024-11-20 04:25:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6204fe8-5328-3288-b33d-c710185d17f5 | -0.94826 | -51.71893 | 2024-11-20 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d8139d8-81c0-3559-8a5e-94716128438c | -1.31046 | -52.40974 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 716db754-874c-31e9-bd2a-7babf4bb64c8 | -2.16472 | -48.34156 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 223242be-61a8-330f-9287-395dd05ed86f | -2.5907 | -47.47609 | 2024-11-20 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 485b60df-8203-3f06-9224-b0e9077d7a46 | -2.91287 | -46.83144 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6042b1b6-6660-3ff2-a42f-ebbcb010998b | -1.52683 | -55.49103 | 2024-11-20 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eb8a0d46-5271-37bf-b8fe-fa73fd6c661d | -2.21193 | -48.41032 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e9b1c86c-344f-30a9-93e3-ba6b18f96d88 | -3.18983 | -46.27953 | 2024-11-20 04:25:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee0f35cd-9ac5-31db-994d-bc6cb0cba21e | -2.11802 | -48.54926 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 92e0a50d-1d53-333a-b3e1-557e24df3a99 | -1.71115 | -52.48587 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8cfc51fb-f6cd-3478-85b2-7e9dad09fec4 | -2.51292 | -48.36497 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d94efbc2-63a6-3d38-9ac3-88a07ac3a48f | -0.24889 | -48.59285 | 2024-11-20 04:25:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c760cd69-bcfc-3d04-b634-abf2988fd994 | -3.59696 | -43.62843 | 2024-11-20 04:25:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 45f68eb8-8853-3286-aaef-c33bce145b93 | -2.72732 | -48.73081 | 2024-11-20 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 286f3f87-88e9-3812-aee8-3fd6017e289f | -2.63482 | -46.56531 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f43d52b4-5f21-3211-bd05-30143319d3c2 | -1.98765 | -53.13633 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 55c729f1-d600-33b2-b100-bd5c0627189c | -1.6235 | -52.5932 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c07eb7a3-952f-3465-80d5-e2f5b71a5b95 | -1.86628 | -46.7988 | 2024-11-20 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0de52d05-288b-392e-832a-8f5a8f9dc7f0 | -2.66647 | -46.23245 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78a5fb28-a2d9-3211-8e3a-5a5e77c7b018 | -2.68727 | -46.18616 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8f6115eb-8c81-3737-98a4-c46430147fa8 | -2.69019 | -46.08076 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aec788fe-bd7d-380f-8e90-fa666d40343e | -1.73444 | -53.03053 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bff4245c-8bc5-357e-8a55-a8640fac9453 | -0.2789 | -51.55648 | 2024-11-20 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1112599d-9a28-3ee0-a236-55e055102720 | -2.63992 | -46.20713 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 51d7b862-927a-37af-a8b7-6f061f58842e | -1.05689 | -53.09462 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a63478ae-9bea-36b3-bb7d-93d647e00170 | -1.58975 | -50.44299 | 2024-11-20 04:25:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3fd76083-3f90-321a-af84-e4c6d99c1d49 | -1.21589 | -51.79232 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e32ca67e-c17c-3bbc-81df-6dc381509fdb | -3.78658 | -41.60732 | 2024-11-20 04:25:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 255558be-00b3-33db-9c64-452ecfaeada7 | -2.55778 | -47.28782 | 2024-11-20 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f50d6880-83cf-392f-9c39-5524a429e2ac | -1.52175 | -55.48638 | 2024-11-20 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84db51aa-1d87-3251-9149-f1dd4f40bd6f | -1.9285 | -46.4478 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bf633b8f-2adf-3ee2-917c-4289778088d8 | -1.1392 | -51.67999 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a2edcd26-869c-39b2-a236-31a2dc7c0172 | -2.68249 | -46.23846 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 488694b7-a8cc-317e-ae6a-b23c1368f2fc | -2.69459 | -46.22619 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb5cf3b9-ce69-374d-a01c-a5d69f9e9bc4 | -2.45249 | -49.1438 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40fcc5ec-9c11-3e5f-9962-fc96d4e07417 | -1.99939 | -46.60581 | 2024-11-20 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 6c84ed2c-7276-34da-b8e2-d0fa1cd3196b | -1.24188 | -53.36452 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fb3942f-f28f-309d-9180-63bc4f4fbe30 | -2.28326 | -48.48625 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5be29a4-81b5-3da3-86b5-da1fd156e0bb | -2.69289 | -46.21532 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1d6bd3e-57d9-3a6c-b660-e05c685cc223 | -3.6259 | -42.40434 | 2024-11-20 04:25:00 | NOAA-21 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c9de0324-dfa2-32f9-b354-0b49138d006f | -2.62185 | -46.25742 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 787cb1f8-9acc-3e51-9d2f-f1c3b4386b00 | -0.90626 | -51.72585 | 2024-11-20 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6cfb411c-a194-3b1d-90d4-9a3b6820d475 | -1.86252 | -47.82101 | 2024-11-20 04:25:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3708835f-f0e6-39a7-ae1a-a5139afd8982 | -0.18647 | -51.62927 | 2024-11-20 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ab73b817-151b-35a6-a235-5e6d32caaac2 | -1.7111 | -48.02355 | 2024-11-20 04:25:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5150f6c1-2901-31be-9474-a59a77be188d | -2.51896 | -44.9974 | 2024-11-20 04:25:00 | NOAA-21 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 96b7e77a-0ce5-39ec-be02-5f5db485613f | -1.24122 | -51.74735 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a259792-62b1-3b30-a800-7357fb4cb77b | -2.35914 | -48.95015 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cc04e0e8-847f-3470-b1ab-83480f4aca7c | -2.74921 | -45.70287 | 2024-11-20 04:25:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5362db8-2ffe-3071-823c-3350ba1332d6 | -2.6978 | -46.05373 | 2024-11-20 04:25:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43ac4f71-d645-33f0-b016-1da57434021d | -1.51608 | -55.48547 | 2024-11-20 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 15565192-390c-3b7a-9456-ddb5c730a072 | -1.88132 | -47.8827 | 2024-11-20 04:25:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b75452cf-a1e1-30f6-8570-893a0566b17d | -3.58716 | -43.62307 | 2024-11-20 04:25:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17d5d3de-34de-37c4-83f2-aca053b585c9 | -2.05797 | -53.43079 | 2024-11-20 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ba7c7320-7ccf-3b4b-a4a3-995029557413 | -1.96976 | -52.10431 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b64cc6fd-ccfa-399d-9c7d-0937dd1dabb5 | -2.83196 | -46.67508 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e28410b-854f-394b-96f7-bd508078c014 | -1.11062 | -52.38978 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f3e6bc8-1c21-32f4-ab45-6ad4b6707b21 | -1.73867 | -46.68432 | 2024-11-20 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 28c34687-fb23-325c-920e-a5698cbc405c | -3.3618 | -45.11099 | 2024-11-20 04:25:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b475944-a477-3ea1-b49e-f735b6ed12cf | -2.91793 | -46.86475 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6cc9d7da-840a-330f-95ac-150e47b3d792 | -2.47419 | -46.28696 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c9265a0-91d7-3b26-a530-deadb6c7ea9b | -3.2756 | -44.48319 | 2024-11-20 04:25:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f78f070-089f-39d3-89a0-f2eb890c0a35 | -2.62098 | -48.32428 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0763d62e-b230-377a-b8a5-46e5a720da57 | -3.07585 | -45.11254 | 2024-11-20 04:25:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b8d0645-a4cc-32f5-ab66-0c87d5f54039 | -1.59031 | -50.43947 | 2024-11-20 04:25:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b3de09c-0ad5-326f-805c-ad8b8b306056 | -2.84862 | -46.67766 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95cdfd80-44cc-3a41-a387-e68ab75c5ef7 | -2.68357 | -46.23155 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7148dec8-81df-35d2-b762-39d104d5a929 | -2.66316 | -46.23194 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ee540e0-e69c-3608-a800-2d73b0bf6915 | -2.17606 | -48.38424 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81e8442f-e5d1-3e60-839b-4d9258fdb8ad | -2.26509 | -48.41751 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78d310bf-2330-39f6-99d1-63294b490966 | -1.77476 | -48.65944 | 2024-11-20 04:25:00 | NOAA-21 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ef6509e-2025-3856-9586-04ccb20f2351 | -2.63761 | -46.56931 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9b7d49fc-9edd-35d2-bd29-0d1d985102ef | -3.3285 | -43.08619 | 2024-11-20 04:25:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f373b1e2-d298-384c-a0a2-296adb5114c4 | -2.72378 | -49.34742 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 81e57fd8-f6aa-307d-b884-745a85584965 | -1.20038 | -46.53601 | 2024-11-20 04:25:00 | NOAA-21 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2080c2eb-be39-3824-961a-fd35d5112875 | -2.24926 | -46.83281 | 2024-11-20 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b26e6bcc-2330-3a79-a827-ebc408f94b2a | -1.47883 | -54.44825 | 2024-11-20 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab2d338a-ee8b-39b2-af77-b4cb45542f6f | -2.14568 | -50.65144 | 2024-11-20 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6601813-fd62-325a-a348-8ce6aa1a6c2f | -2.88896 | -45.83409 | 2024-11-20 04:25:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f6607a2-35b7-315a-8200-712d243be9a3 | -2.52393 | -47.07615 | 2024-11-20 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ce397b64-325b-3646-bacc-5a2a0b6e78fb | -2.66511 | -46.60936 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7381545e-7fd0-3eeb-8588-5c354a02a7ad | -1.2119 | -51.76057 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README24.md)
