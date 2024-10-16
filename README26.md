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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 566a165c-caf4-38fd-bc73-d3a76a136826 | -4.47044 | -47.7412 | 2024-10-16 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eb39e92c-7302-34ef-a53b-7f9d7006f9bf | -4.34674 | -46.69903 | 2024-10-16 03:42:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 27804945-ecd5-301f-a8ea-5ecaa6372fc3 | -4.34041 | -46.69765 | 2024-10-16 03:42:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a3a7c2fc-6ab3-3d69-96fb-6b069f677195 | -4.33952 | -46.70273 | 2024-10-16 03:42:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 25ca6f9e-99e0-31f5-8c04-c69865e939f3 | -3.95819 | -46.43205 | 2024-10-16 03:42:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 9ba6da77-da56-36e5-840b-7e3f6c46decd | -3.95736 | -46.43686 | 2024-10-16 03:42:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 24.2 |
| bc6f7ee8-4afc-3d86-a103-c95f41ad815e | -3.9564 | -46.44237 | 2024-10-16 03:42:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 86230c9a-8c6c-3170-936b-9ff88bb90238 | -3.95112 | -46.43529 | 2024-10-16 03:42:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 24.2 |
| ab3ebbe9-e53e-32c6-841b-6912928353ce | -3.95024 | -46.4404 | 2024-10-16 03:42:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 40da31b6-e199-3d38-ab75-a800c3f24667 | -3.93635 | -46.40815 | 2024-10-16 03:42:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4ff83ee2-b618-3b9a-a326-0c0287ecf57e | -3.93552 | -46.41291 | 2024-10-16 03:42:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 23608d9a-0ae3-3be9-8f5c-8629aa5aae32 | -5.51583 | -46.90199 | 2024-10-16 03:42:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 68404886-ff9a-3268-b48c-5288bb7c7924 | -5.51493 | -46.9071 | 2024-10-16 03:42:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7399ae60-7753-33c2-8f18-69425c9ad507 | -5.51155 | -46.90352 | 2024-10-16 03:42:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 77b5fbf5-d3c5-3e8f-9b57-04675c55b970 | -1.48584 | -47.3317 | 2024-10-16 03:42:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b86caf18-c723-338a-81ad-41a341668b57 | -1.43736 | -47.41034 | 2024-10-16 03:42:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8939acee-ca84-3db9-87eb-1d2960376402 | -2.9684 | -48.00309 | 2024-10-16 03:42:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e91bbf31-4e8e-3af2-8802-db3e5f358633 | -2.96724 | -48.00985 | 2024-10-16 03:42:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 5a19ba25-34f2-3fd9-8ee5-8a31e3a0f20c | -2.96619 | -48.00291 | 2024-10-16 03:42:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cfe188ea-63d4-362b-95ef-01182cd7e2c3 | -2.96499 | -48.00962 | 2024-10-16 03:42:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| eb6c84a9-0e39-316c-9003-a9b4b65f177c | -2.96135 | -48.00199 | 2024-10-16 03:42:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1f6c72d6-0127-3884-8ca4-78ac4fce93e1 | -2.96021 | -48.00866 | 2024-10-16 03:42:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a4fe1e61-0566-36b6-93ab-00aef3bc4a43 | -2.95915 | -48.00175 | 2024-10-16 03:42:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| aa6b2365-b901-3046-8d42-d451b09ec3ff | -2.95796 | -48.00841 | 2024-10-16 03:42:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d9f696b6-7e71-3c1f-b9f3-d553d62ae8a6 | -2.38587 | -47.59092 | 2024-10-16 03:42:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ee5d4ee2-64ec-34f5-8799-be8515f77386 | -2.38523 | -47.59155 | 2024-10-16 03:42:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 94dfc28a-4545-3504-ad2f-497b50089285 | -2.37895 | -47.58972 | 2024-10-16 03:42:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a7784bf8-5ace-3d76-99bb-547eb896a0f8 | -4.57105 | -48.01601 | 2024-10-16 03:42:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4b106b0f-2f61-3b89-93c3-8fe22182d94d | -4.36261 | -48.49092 | 2024-10-16 03:42:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8db9fa86-e628-3f68-8824-0df0cd1b3069 | -4.35869 | -48.48992 | 2024-10-16 03:42:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6fa41b1d-b97c-31ad-ad02-4b295fd22279 | -4.35751 | -48.49653 | 2024-10-16 03:42:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dca1195d-8f68-309e-b134-5a82c3e6f739 | -4.35553 | -48.4897 | 2024-10-16 03:42:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1d50a1f1-17d0-33ed-8c56-082190f8eb2b | -4.35433 | -48.49622 | 2024-10-16 03:42:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 107e84be-bcb0-3621-a38b-a30a0a74a1e9 | -8.22048 | -36.1348 | 2024-10-16 03:45:00 | NOAA-21 | SÃO CAITANO | PERNAMBUCO | Brasil | 2613107 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 676426c0-870c-3c1d-8421-ba3c1706a9a0 | -8.07208 | -34.97765 | 2024-10-16 03:45:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 13392108-bf5b-38e2-9076-c0d4fcda1ab3 | -9.99197 | -36.44672 | 2024-10-16 03:45:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ec569d26-fb27-35f7-8ca7-2464d85684f8 | -9.84333 | -36.50523 | 2024-10-16 03:45:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| eb7db903-c86f-3fc1-96e8-f55bb4ef53eb | -9.84278 | -36.50874 | 2024-10-16 03:45:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 14d880e2-4eec-398c-b819-af2308f0f39a | -8.64834 | -36.93031 | 2024-10-16 03:45:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b66c2f3b-4182-3910-93ca-4408914e0aba | -8.64776 | -36.93389 | 2024-10-16 03:45:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c90436a9-5731-3d9d-beba-0c17fbf4517c | -8.55418 | -36.73552 | 2024-10-16 03:45:00 | NOAA-21 | ALAGOINHA | PERNAMBUCO | Brasil | 2600609 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 43655f26-79ba-3f39-bfff-978ed3bdafbb | -9.57936 | -37.81594 | 2024-10-16 03:45:00 | NOAA-21 | PIRANHAS | ALAGOAS | Brasil | 2707107 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 66ead19e-5d95-3b61-ad76-ac9c6a7399d0 | -7.80809 | -40.48473 | 2024-10-16 03:45:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b9614d31-0194-3409-ad27-241153b75934 | -7.76084 | -39.41385 | 2024-10-16 03:45:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f82fa01d-3079-365d-a057-ea1af45396bf | -7.69983 | -40.43287 | 2024-10-16 03:45:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3c738a98-20b1-3d4f-94f1-22981c1fdb0f | -8.53775 | -40.21628 | 2024-10-16 03:45:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 639d8a32-e7ff-3c8b-aea0-e8194208fe83 | -8.13522 | -40.07475 | 2024-10-16 03:45:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 369b0226-82bc-3ec3-886d-5368ff9c4db1 | -8.13378 | -40.07653 | 2024-10-16 03:45:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8c6fa47c-a95f-395e-a875-67603546d95a | -8.00344 | -40.59198 | 2024-10-16 03:45:00 | NOAA-21 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 322643c6-5487-3d21-8d07-9361cd8625ee | -13.90406 | -42.51665 | 2024-10-16 03:45:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cc14cdc8-afc4-385f-8acb-fcaef9d69ee5 | -7.60452 | -42.21821 | 2024-10-16 03:45:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 3d94a068-b254-3ed8-92fe-0adff2fff2df | -7.60374 | -42.22271 | 2024-10-16 03:45:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 01d82252-3ebf-3fcd-bc3a-307f24b3d054 | -7.23686 | -40.86642 | 2024-10-16 03:45:00 | NOAA-21 | ALEGRETE DO PIAUÍ | PIAUÍ | Brasil | 2200277 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 39ad943b-6cd1-33f7-b076-d926c0d0dba8 | -7.23465 | -40.86633 | 2024-10-16 03:45:00 | NOAA-21 | ALEGRETE DO PIAUÍ | PIAUÍ | Brasil | 2200277 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5244ef3d-0e2a-3384-a962-05054453056c | -8.37441 | -41.25769 | 2024-10-16 03:45:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 85426b88-fb0f-3d9a-a995-4e7e97ff0a98 | -8.19 | -41.00101 | 2024-10-16 03:45:00 | NOAA-21 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| c5af4bba-3470-38d0-9407-fca3f7d206aa | -8.18937 | -41.00478 | 2024-10-16 03:45:00 | NOAA-21 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 67e3d311-34b9-32c1-9059-5185ed370761 | -8.18888 | -41.00051 | 2024-10-16 03:45:00 | NOAA-21 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| ceb2dd2b-e21d-3392-ab4c-b85a55502a2e | -8.18822 | -41.00428 | 2024-10-16 03:45:00 | NOAA-21 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 52937127-6f03-3344-9bef-cf5d6c9003c3 | -8.18587 | -41.00035 | 2024-10-16 03:45:00 | NOAA-21 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 8a97ebb0-3481-3c6d-8ce2-c21d5ca1c0a3 | -8.18524 | -41.00413 | 2024-10-16 03:45:00 | NOAA-21 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 5a96f6e1-2599-3dee-8205-9a88172f3434 | -8.0956 | -41.0081 | 2024-10-16 03:45:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cc646be5-15d5-32db-81ef-e19c86fb67e3 | -10.28775 | -42.38225 | 2024-10-16 03:45:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1123080f-fc35-311d-9ebc-6901d2e2a6a6 | -12.01484 | -42.3161 | 2024-10-16 03:45:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7f7fc337-ce0c-3e26-add7-eae080038a43 | -13.28665 | -43.43166 | 2024-10-16 03:45:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 13f57eed-6451-3cdd-a848-b1cf3143836c | -13.28583 | -43.43616 | 2024-10-16 03:45:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 06728a48-f792-3bc4-a398-7865691645df | -13.26042 | -41.96498 | 2024-10-16 03:45:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ab39b219-d9aa-35cf-b3eb-000e6c1b1b24 | -12.80862 | -42.50487 | 2024-10-16 03:45:00 | NOAA-21 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e2b9845a-181e-3aec-a1ca-f45db339e350 | -13.90627 | -42.51666 | 2024-10-16 03:45:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 04f5041a-7b6a-3af7-af07-4c4726858791 | -9.58483 | -43.50044 | 2024-10-16 03:45:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1e8c9a67-61d2-3435-9aa2-6808770f884b | -9.58468 | -43.49817 | 2024-10-16 03:45:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5e1227e9-e5b2-3006-ba8c-0a48bfacbae7 | -10.10264 | -44.22108 | 2024-10-16 03:45:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2a5bee0-b694-3fa2-88be-fc1afc8547d0 | -11.99747 | -43.78297 | 2024-10-16 03:45:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cb4c5d52-3337-38c2-bacb-40b7404a2d14 | -13.26144 | -43.65624 | 2024-10-16 03:45:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7c75c318-399e-395e-bc68-16d01c70750b | -6.24874 | -44.60709 | 2024-10-16 03:45:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e37139c7-bb66-3b68-9766-c56a69e03ae8 | -6.24686 | -44.60667 | 2024-10-16 03:45:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 136e6dd3-b32f-36f9-972a-b2f5841f17fa | -6.18834 | -44.5275 | 2024-10-16 03:45:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 107951a9-84af-3fc4-b69f-759dde12a82f | -6.18348 | -44.52356 | 2024-10-16 03:45:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 92e507c2-f0b9-3f79-be35-536603b3a665 | -6.18292 | -44.5267 | 2024-10-16 03:45:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| f68d5e4d-96ca-3393-8be6-0cb7eb4dbf58 | -6.18233 | -44.53 | 2024-10-16 03:45:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 31c0bc38-e914-3349-a1bd-e1183dd1d13f | -6.16916 | -44.82545 | 2024-10-16 03:45:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ddd0ebdd-782f-321e-8ef8-93d310183783 | -6.16362 | -44.82468 | 2024-10-16 03:45:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ed05dcb-9713-3eb1-9be7-5aadd2a232e6 | -6.1355 | -44.69722 | 2024-10-16 03:45:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6dd9cc78-f292-32fc-a7bb-e98b9afea742 | -6.97817 | -44.68256 | 2024-10-16 03:45:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 51385269-35d8-3bf2-ac29-98140290b889 | -6.91255 | -44.37871 | 2024-10-16 03:45:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b07a22d-c91b-387d-b977-690c1739dae8 | -6.91192 | -44.3823 | 2024-10-16 03:45:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1a489685-244e-337d-a9f1-bb48c69c402d | -6.90724 | -44.37794 | 2024-10-16 03:45:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6cbccc7c-5ff8-35d2-ab29-e99a66ca4e13 | -6.90665 | -44.3813 | 2024-10-16 03:45:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7735d738-789d-3252-9cf8-849d4446671f | -6.82259 | -44.66821 | 2024-10-16 03:45:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b23d7146-60f6-3473-97b0-525e31c98be3 | -6.82195 | -44.67176 | 2024-10-16 03:45:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d0df0eb-87aa-31e5-b1d3-eda28522be6b | -6.68555 | -44.07484 | 2024-10-16 03:45:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 91904532-2466-3dcc-97d5-21fe2dcc3f0e | -6.68499 | -44.07793 | 2024-10-16 03:45:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dee66e1b-906b-3c08-9132-f6bc824bf847 | -6.6842 | -44.07686 | 2024-10-16 03:45:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6fdb72fa-de02-31f8-8861-a7d2dd122f94 | -6.67783 | -44.70694 | 2024-10-16 03:45:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0226c66e-daff-3caf-9e54-26b435fcdf0f | -6.67723 | -44.71038 | 2024-10-16 03:45:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7dcba6b3-fff0-3cc4-bfff-55911d84d3c7 | -6.67399 | -44.70786 | 2024-10-16 03:45:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4ef918a0-9b83-382e-8dda-a9b5c347aa09 | -6.67182 | -44.70938 | 2024-10-16 03:45:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b2fd2819-52f2-348a-a7cc-254dd746a6b1 | -6.6692 | -44.70348 | 2024-10-16 03:45:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bf5043f1-9e5d-3162-bf35-66a96a0c9213 | -6.53627 | -44.42623 | 2024-10-16 03:45:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3ddbf6bc-11ab-38c9-81d2-fe3d4077bff3 | -6.53572 | -44.42933 | 2024-10-16 03:45:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README27.md)
