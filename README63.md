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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52dfe01d-898b-31c2-bea3-a7ad0c5cde44 | -7.29912 | -43.92913 | 2025-09-16 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 856df5e9-e956-30cd-9c03-cb7efc8251e2 | -5.93555 | -45.19202 | 2025-09-16 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d059b393-c85f-3a9a-86de-8942f5a7f6c4 | -6.63035 | -44.74052 | 2025-09-16 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 501f76dd-baf2-3749-9f86-384d86627ae0 | -6.15561 | -45.1208 | 2025-09-16 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8e38b475-ada5-3f45-880f-d831a1ea2fdb | -7.28225 | -46.61207 | 2025-09-16 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41b8af80-de02-3835-bae7-2e6291dab11d | -2.25966 | -47.84552 | 2025-09-16 04:49:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1996c6e-d193-38e7-a61a-dc9529169cbb | -3.64613 | -48.32564 | 2025-09-16 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b0b5b9b-49c0-3611-a418-ea6177fa3164 | -7.40538 | -49.98925 | 2025-09-16 04:49:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2780512a-7e03-327f-9f12-9239db5dfdfa | -7.40894 | -49.98981 | 2025-09-16 04:49:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e84f286-d6e5-3192-8a6c-613ffa6085eb | -6.76025 | -48.11035 | 2025-09-16 04:49:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffbc74d4-4f6d-3f37-b77b-5d1d985e73be | -7.13464 | -47.98281 | 2025-09-16 04:49:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e0cb8ae7-e63b-36aa-b03e-67e246a8a45f | -4.40753 | -50.28361 | 2025-09-16 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11ec5bfe-a84a-304c-be04-4e4a8c543ed2 | -6.9659 | -44.54234 | 2025-09-16 04:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60349ed4-1716-3d6a-9357-f679846910d1 | -4.15927 | -46.7918 | 2025-09-16 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a49668ef-1c7f-3e85-b05f-c11f31c0e761 | -5.77884 | -43.91655 | 2025-09-16 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c3ed524-c0ce-3f93-91b5-f7bf4640b080 | -7.39647 | -50.00029 | 2025-09-16 04:49:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ebb1e022-ab40-31fd-b4e4-544dfb05f5ae | -7.67674 | -44.49409 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3354677d-eb81-3d06-a347-d69388fa7f36 | -7.40833 | -49.99385 | 2025-09-16 04:49:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf7eaf89-b832-3c2e-a8fb-26ca673c1f0e | -3.53828 | -52.20243 | 2025-09-16 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba5f5247-f394-30d3-acee-447f7280bd52 | -3.83168 | -44.10849 | 2025-09-16 04:49:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7844d662-a5a7-3dc9-91c8-518128ac511c | -6.34555 | -43.16074 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c9c1f2d7-ee78-3ffa-a7ca-a3bc058d4002 | -8.34507 | -44.72074 | 2025-09-16 04:49:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03f7d819-bf0f-3684-a83d-41f2aee38a96 | -8.17185 | -46.76154 | 2025-09-16 04:49:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45967b3d-f62a-340f-b1cd-eb078584e3d0 | -7.27532 | -46.5983 | 2025-09-16 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc99945a-a02b-3573-8337-77a734044731 | -5.02101 | -50.86786 | 2025-09-16 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 280850bd-015b-37c6-88d7-b8049260bbe9 | -6.22101 | -43.89886 | 2025-09-16 04:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e4648002-a965-312c-83aa-357070177234 | -5.79623 | -43.94072 | 2025-09-16 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea8e9ded-9017-3daa-b8cd-1efa586ef115 | -6.22057 | -43.90191 | 2025-09-16 04:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 47dab28c-7393-3cd3-a01e-f32aa3aa793c | -7.93799 | -47.65061 | 2025-09-16 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a803590-366b-3566-9a6a-5bb79ae9c229 | -6.40377 | -43.33619 | 2025-09-16 04:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2ad7240-62b7-3ca6-9741-51bf0a3f05d3 | -2.64234 | -48.05113 | 2025-09-16 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7dc6d2d7-7902-33f3-adff-64f9a59a8745 | -4.28706 | -55.25591 | 2025-09-16 04:49:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9f1a35f-d205-3c5e-8f53-18e7eff91108 | -7.85538 | -46.10432 | 2025-09-16 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4ea7056d-b3af-3905-b12a-69038a61d054 | -7.39292 | -49.99974 | 2025-09-16 04:49:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 700f6f25-95ac-3b1b-9d6a-e709e5888603 | -7.99276 | -45.66226 | 2025-09-16 04:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fd072f32-a206-3980-8b82-1ad1ed318bb1 | -4.9167 | -48.26188 | 2025-09-16 04:49:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f32e800-c35d-3428-8de4-226075e49706 | -7.40002 | -50.00083 | 2025-09-16 04:49:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98607b17-78a0-3475-9c32-367b9f169533 | -8.08218 | -46.82942 | 2025-09-16 04:49:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d51f844d-6dd6-3869-a098-2bac1b53853b | -7.13788 | -47.98849 | 2025-09-16 04:49:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5e3d2ac4-8b20-32a1-9330-0256a528bdf6 | -7.20771 | -44.38672 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a93ece3d-8798-3dca-a164-bb4cdae4c6bb | -5.79717 | -45.92328 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3df7b665-146e-3435-9287-02da0c47cdb9 | -3.8276 | -44.10231 | 2025-09-16 04:49:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a5e224cf-8b9f-3b11-839c-c49e858ca540 | -6.41353 | -44.36545 | 2025-09-16 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 317d3b5b-1a39-3e52-ac20-215cd8dbea29 | -7.0817 | -44.55334 | 2025-09-16 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9108bbcb-8b13-372a-a048-ef7a861af6e3 | -6.92324 | -44.77085 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5e702315-29b4-3120-b2f7-107524571935 | -7.26421 | -46.6139 | 2025-09-16 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8cbc8c11-16c1-3a0b-8096-250954e1e691 | -7.51324 | -47.65685 | 2025-09-16 04:49:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff1b2f4a-981d-31ac-9174-5edd17a9908a | -7.14331 | -47.97884 | 2025-09-16 04:49:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 11d95d5c-f0c6-32fd-a224-f9c426fe9716 | -6.46675 | -46.0023 | 2025-09-16 04:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ffaa149-71ef-3831-9ae4-999da75a9aaf | -3.12738 | -52.43879 | 2025-09-16 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b5cc170-5589-33d1-a7cd-95952badf32f | -3.25084 | -51.87205 | 2025-09-16 04:49:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d75ff0d-4772-3236-a92d-1b7d946736b8 | -5.63099 | -45.33187 | 2025-09-16 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f95e55e-a0eb-3cc7-b16f-cc6d98b1b111 | -5.78707 | -43.89605 | 2025-09-16 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e04e946-40d4-3cec-8dda-aefce278f6a9 | -6.75952 | -48.1153 | 2025-09-16 04:49:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 35cad55f-bcc2-31f9-8115-3a04a3a52f11 | -8.00217 | -45.66354 | 2025-09-16 04:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a73c25e6-30cc-3e5c-886f-117a50e6efb8 | -5.34753 | -44.82374 | 2025-09-16 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ce5fa5a-5378-3332-a651-bb39f2d0a83e | -5.80032 | -45.93279 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61374fb3-69d1-3deb-aa94-eea5a82b00c9 | -3.07404 | -48.81415 | 2025-09-16 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3273691b-4b92-38ca-88a5-03c2dd80eb1c | -8.41989 | -45.75009 | 2025-09-16 04:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 01ac90f5-81bc-357a-80b8-75ee9d8aab87 | -6.43169 | -52.01068 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a8b1d15c-4ae7-3e4f-bda4-fbc21e6c1f5a | -5.67126 | -51.14273 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27c6dcb5-7056-3c9b-a01d-24d3c7eeecda | -6.43169 | -43.31296 | 2025-09-16 04:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4ac404f-1795-3520-bc17-1adcdcb6215e | -6.0983 | -52.2528 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c44c0cdd-9f5b-3817-b151-883513250c72 | -5.05641 | -45.201 | 2025-09-16 04:49:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c42b555-d25f-3830-b9fb-9673c6233cc0 | -6.18617 | -41.19788 | 2025-09-16 04:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| e0438df0-0bc2-3f6c-a4ab-77c07f69a8d1 | -6.88339 | -46.06812 | 2025-09-16 04:49:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de19bb7e-c32f-3d47-a912-dfe596c8c635 | -4.76501 | -48.0596 | 2025-09-16 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 28c6e9e5-788d-38fb-88c4-a57e6f30c73e | -6.43219 | -43.30931 | 2025-09-16 04:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75967d8a-a2bb-3b53-b45c-01b1d9bb6870 | -6.42838 | -52.01016 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3731a91f-edd7-3168-b2e7-c20affd16a67 | -5.79667 | -43.93773 | 2025-09-16 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a23caced-1ede-3f76-858a-a1cc59c71e0e | -5.09581 | -43.82787 | 2025-09-16 04:49:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 974a7b56-2018-3e70-bbec-b9a499389356 | -6.99717 | -44.57308 | 2025-09-16 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ab3ab1a-cd1f-35ce-accf-113d8337d0cb | -7.05466 | -44.11518 | 2025-09-16 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| faa77d06-5ec2-3a4b-87a8-c51f1b92e1c6 | -5.24963 | -44.14385 | 2025-09-16 04:49:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7010a6f1-4faf-38c7-bcc7-4095cd2f7654 | -5.97115 | -45.86263 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b13bca8-2b67-3362-a51b-931d3da90f23 | -6.62131 | -44.73375 | 2025-09-16 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54a82bc2-2792-391e-b1da-805ba596f5b4 | -1.35446 | -54.64913 | 2025-09-16 04:49:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 29fb9613-2762-347e-86c5-c1c2a3b31d5c | -6.97635 | -44.54064 | 2025-09-16 04:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3e3035d-f4bf-33a2-8cc7-14d62f3b6f45 | -7.0495 | -44.11445 | 2025-09-16 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 04844543-ea0b-3dcb-8d2b-f9a8603c4e7d | -3.8053 | -41.56721 | 2025-09-16 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d4096735-63f4-3a4c-bb54-fd8b8c38134f | -6.52432 | -51.20053 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a33624e2-c3fe-3679-9e30-42abae8a7141 | -7.55927 | -50.45628 | 2025-09-16 04:49:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b17a8635-3795-3425-9ec3-8900efc64e6f | -7.66455 | -45.14749 | 2025-09-16 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1dc931c-4b3f-3feb-ba57-1bc80ae124de | -6.8256 | -47.86231 | 2025-09-16 04:49:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91762671-fa08-3616-a73c-7ec75c2bd311 | -3.81113 | -41.56813 | 2025-09-16 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b9425f2a-9e46-3d96-bc03-91e92af81cb3 | -6.09922 | -46.50017 | 2025-09-16 04:49:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed80b0b0-53cb-346d-81a6-ce1128c957d6 | -7.43354 | -46.1767 | 2025-09-16 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42d4a685-0157-3d17-bc8c-653fb427f32f | -7.6894 | -44.66263 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04b46e37-e708-3afd-a25d-9fc8d29ca581 | -6.37132 | -44.41171 | 2025-09-16 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ee4dc99-2c60-39c9-a799-72b4cc3618b7 | -7.98474 | -45.65118 | 2025-09-16 04:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2bbebbb-3f8a-3259-825f-3960cc46b0d4 | -4.01256 | -43.23621 | 2025-09-16 04:49:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 191e49f9-451b-3538-b29a-1767c2740c26 | -7.69191 | -44.49657 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 621366f5-ae1d-3dd7-9d4f-c6d65d04a7aa | -7.69439 | -44.66355 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd03eee2-0f32-341c-8375-32e9709a6f84 | -7.81015 | -46.12353 | 2025-09-16 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 760b4fde-fe0a-3722-9f7b-11b9604018e5 | -5.22633 | -43.70124 | 2025-09-16 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0ad595e2-1346-3ddc-a0b2-36a5042a7476 | -7.26772 | -46.58921 | 2025-09-16 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a50b8ec7-4d87-3835-9c99-d0063c85ac46 | -7.67581 | -46.30891 | 2025-09-16 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2276c1ec-edf8-32b8-8b7e-16c182522a6d | -6.46858 | -46.00414 | 2025-09-16 04:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5fdcff4-ae9a-3443-886f-8c6df4db362a | -3.8059 | -41.56306 | 2025-09-16 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 285b6388-b002-3447-9207-097b80c45eeb | -5.84048 | -44.15822 | 2025-09-16 04:49:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README64.md)
