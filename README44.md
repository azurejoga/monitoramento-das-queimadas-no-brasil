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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48c7d2fa-9f77-3d58-8dfd-a66d331185af | -6.91163 | -44.54007 | 2025-09-15 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35a6c60c-dcbc-3a98-9d45-71f7b612850b | -6.6831 | -45.50737 | 2025-09-15 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 120a1b51-2557-3beb-9218-25d17096f96c | -6.17066 | -41.20343 | 2025-09-15 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1e7e51d9-d188-3f35-b40a-5ca6e95b45bf | -5.64147 | -45.94804 | 2025-09-15 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 17761487-344e-3e98-9fcd-0b759756e490 | -9.1247 | -44.83767 | 2025-09-15 04:49:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 363b9da8-390c-3e56-b6fb-189efcb2bf6c | -7.73333 | -45.30538 | 2025-09-15 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 652cf31e-e8ff-32bd-a8b5-9d273fd93bef | -8.82463 | -40.67149 | 2025-09-15 04:49:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dc86d5a5-acba-3206-be7e-51e19e999596 | -8.97954 | -45.81957 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 849c8d92-923b-3f67-aa2a-79b1e7e90e78 | -6.64549 | -44.72314 | 2025-09-15 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 35635cef-7ed7-3b07-a4d9-f6d37de6a539 | -10.7376 | -44.77246 | 2025-09-15 04:49:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 50a52986-a7d5-3c92-9cd3-adeb2b36639f | -7.80096 | -46.12246 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9235341-5e40-30d2-a91a-d3ce6bc4133f | -5.96691 | -43.21345 | 2025-09-15 04:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ff7b7dd3-1855-3857-a64e-05e5b2f152fc | -8.91735 | -45.49383 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64318f20-05dc-3294-bc02-353437a30014 | -6.05614 | -43.5679 | 2025-09-15 04:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a99fc7d2-b7b1-3f73-a645-2b46a196a8da | -7.73277 | -45.30943 | 2025-09-15 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4bb6deb-c6b9-3a89-a19f-72247f75f2a6 | -8.92612 | -54.44358 | 2025-09-15 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d7099bd-6cbc-3143-aac4-79e79403456d | -6.89254 | -45.63326 | 2025-09-15 04:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 21c6038b-9cc6-36c6-8919-5fdbaff1996b | -5.63796 | -45.94398 | 2025-09-15 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 016856a8-b8b9-3824-beeb-2564716c48b8 | -9.01283 | -48.02504 | 2025-09-15 04:49:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a359217-e973-338e-ad2c-ffd7b822043e | -8.98301 | -45.76357 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9b2f470f-1049-323b-a1cd-6596db650b8b | -4.63162 | -46.11343 | 2025-09-15 04:49:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12d92f9c-c432-3ccc-b460-454312b1ad04 | -8.96965 | -45.76571 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe76411f-2655-3f9c-b3a9-5721b7b3a6b8 | -8.60331 | -46.34811 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85a4fec5-182e-311e-950a-7ec435f41404 | -8.9827 | -45.82795 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38af6e15-aba7-3389-80a6-5f0ee96f05bd | -8.95253 | -46.0425 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 87ca101f-6b90-3310-8167-dde3f94f9ded | -9.5501 | -45.9784 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 384ed502-abbc-3295-a303-c880943c2e1c | -6.66269 | -45.55938 | 2025-09-15 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb9e1d21-0113-3cde-b243-496aa549ad9b | -7.88785 | -43.57269 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| c5a9bb8b-9b00-3760-b25d-1eef73827b44 | -10.63346 | -46.23974 | 2025-09-15 04:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7e94fba-dfe0-3a69-aa11-85f556168234 | -10.76354 | -44.72145 | 2025-09-15 04:49:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7644fcce-6180-393a-ab91-697d0d506907 | -8.09348 | -50.16397 | 2025-09-15 04:49:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 230c6b55-4e13-3bf9-8bfa-c4e3ca5281d4 | -7.88682 | -43.56611 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 8e4d0353-399f-3521-a5b9-3b16b1d24c47 | -8.9812 | -45.80769 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62c213c3-16da-326a-8080-cf54256d85bf | -7.48277 | -46.14968 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69b77690-1102-3b9f-91e4-3aeb78d31a1b | -8.97844 | -45.82739 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 03f75f95-9676-333a-bc5a-7ddf85b06b64 | -6.56146 | -43.98774 | 2025-09-15 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1402c85-7095-303e-a8fc-99552b8d85fb | -7.87808 | -43.57127 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 63375e5c-a3df-39a0-ac61-7aaa6b3cd669 | -9.25177 | -45.65966 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24d441d3-4537-3d9f-bcbf-5d62a962a915 | -8.99779 | -49.79245 | 2025-09-15 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8efbe68a-46b1-3591-bba8-bbdb0160a367 | -7.88444 | -43.56115 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| da1fca20-95ff-3530-b139-e60a1189c30b | -6.64165 | -44.74887 | 2025-09-15 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| efbc1aa6-c5ab-336d-900c-5c57a424da30 | -5.69974 | -49.19867 | 2025-09-15 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4611d3cb-261e-3889-bcf8-fca2d6561bf8 | -7.87175 | -43.58129 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 7142b3af-64ab-31b1-9a56-699e5f783ce6 | -10.30064 | -45.38243 | 2025-09-15 04:49:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b994a8f-b770-323b-b48c-1cd2e4ce93e9 | -9.01654 | -48.02557 | 2025-09-15 04:49:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d267058-4da8-3615-8683-5a9f6ff007ab | -5.20858 | -45.1811 | 2025-09-15 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3bfbb40d-3371-30d3-a57a-6fbf2620a93f | -7.05448 | -44.67696 | 2025-09-15 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 22834166-f807-3925-afa0-f5c9ff663373 | -8.97451 | -46.21612 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7254dbae-23ec-349e-92e1-893c6d8571b6 | -6.1717 | -41.19614 | 2025-09-15 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8c1bf3e7-83c9-3ac5-9c1a-dc475155641c | -8.89492 | -46.16725 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7ae772c2-5103-3744-928c-58d0f7695a42 | -5.33602 | -45.80342 | 2025-09-15 04:49:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7ab892d-5312-3df1-b014-0695e6be0d0f | -7.78914 | -46.11742 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40387e37-3ef8-3bb7-bbd0-93aa684f3fd4 | -8.12332 | -43.66813 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b375ba0-d718-3b95-8b74-3aff5e52ec32 | -9.01218 | -48.02941 | 2025-09-15 04:49:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ceab4dc-dc58-3bb4-bfdd-ff0d3a9fead6 | -5.4898 | -57.09663 | 2025-09-15 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 836d345a-ed64-3eec-a40c-7fb30158cbf6 | -9.05683 | -47.01901 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa54ac43-14b1-31b2-93bd-972335d27ac1 | -4.24436 | -54.9216 | 2025-09-15 04:49:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44b36133-468a-31a5-8404-7a8faf5bb808 | -10.87979 | -45.44547 | 2025-09-15 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| afc262b5-3012-35eb-b7e8-fb4a5671ed74 | -9.36127 | -45.3868 | 2025-09-15 04:49:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f424501a-c471-3ca2-9215-f1657df4ba22 | -7.64513 | -49.72066 | 2025-09-15 04:49:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50fb6736-7270-3d27-873a-9511e6e5c13b | -8.64662 | -46.3657 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b1244a4-584a-34d7-a87b-8b8e46bc8a77 | -6.32139 | -43.3471 | 2025-09-15 04:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3388985e-fce0-356a-b83a-e0f292f1b5ab | -7.88711 | -43.57808 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 193.0 |
| 9965c473-a008-338f-a7a0-e0aad092f93d | -7.05629 | -44.12032 | 2025-09-15 04:49:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7e7e5161-cdf6-3b72-9ac5-8f43281137e8 | -7.89248 | -43.5614 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 22.1 |
| e5bf3582-95d7-366c-bbae-170d20019302 | -8.20692 | -45.55043 | 2025-09-15 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7fe5621e-80ff-36ea-89ea-5bddf7906e8e | -5.93068 | -44.86462 | 2025-09-15 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9857b4a-b1cd-3783-bcf7-dd25eb6858f7 | -8.43696 | -55.62942 | 2025-09-15 04:49:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2f4c423-175c-33f8-af37-f354cbf38421 | -5.75099 | -43.92368 | 2025-09-15 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fb2a790d-b6d5-3669-97e7-1a1bc322c94d | -8.89631 | -46.18675 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6c40e4a3-d65c-319e-b841-1a25d3712b5a | -5.79801 | -50.08857 | 2025-09-15 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 564d22fe-ab84-3b82-b82c-b090293e32a7 | -7.85542 | -46.11504 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5071e2bc-fb5b-3819-b8d4-1f79c0af66a6 | -7.40505 | -49.98795 | 2025-09-15 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71236122-ec69-3f58-a6f9-5bf9e0384a14 | -3.55685 | -53.53007 | 2025-09-15 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 007c1963-1290-38e7-a356-d30d4d6fd519 | -8.89546 | -46.16359 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18037b39-a741-3322-9573-893f0a687933 | -10.19006 | -46.15688 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32d78456-583e-3eed-bdd8-9f0eff477a44 | -8.89574 | -46.19062 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3dec9e5c-f2bf-36f1-bd87-801c88b50cc3 | -5.90352 | -45.74469 | 2025-09-15 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0e8650b-37cd-3889-955c-84162c44af76 | -3.65063 | -54.06176 | 2025-09-15 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8d6d95dc-ace9-3663-8c4e-94d4d0c601eb | -7.87474 | -43.58083 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 613f2165-497a-363f-866e-781572c71ad9 | -6.45313 | -44.52394 | 2025-09-15 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6e31bc0e-be47-3e5b-8b74-bfe79f4c4af6 | -9.04594 | -45.71983 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4d09f87-a361-3658-ba45-fd0b171d879f | -8.20272 | -43.76231 | 2025-09-15 04:49:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 88518138-5871-3287-9903-8d850328b6e9 | -6.64126 | -44.74246 | 2025-09-15 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba14bc24-ae2e-374b-9e25-f50d36bdf55c | -9.00649 | -47.06192 | 2025-09-15 04:49:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 532d7e56-1f8e-3054-b51e-ce621e139a53 | -7.84373 | -43.86005 | 2025-09-15 04:49:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9223faf6-8c10-3d2d-a0b3-f5f5b16e6d19 | -9.36503 | -45.39214 | 2025-09-15 04:49:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a91bf08-f706-34a2-8943-09405e1b9ddf | -5.76943 | -43.92657 | 2025-09-15 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a97b5013-de33-3b83-b48a-e04c4c390fbf | -7.88932 | -43.56184 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 296c02a7-3df1-33dd-9124-596cb0d7cb08 | -5.16286 | -48.14606 | 2025-09-15 04:49:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 30f8d4ba-d23b-3ed7-ab96-d81331f8018e | -6.16922 | -41.20225 | 2025-09-15 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4fc8558a-87e8-31c3-8046-17f20530f442 | -10.65985 | -46.23635 | 2025-09-15 04:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 041b3043-2c18-384b-b3c9-b4286f7cd909 | -6.15648 | -41.1827 | 2025-09-15 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 080ec57d-651f-358c-b155-375d8ceb8c6a | -7.05652 | -44.14176 | 2025-09-15 04:49:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1622fa37-6206-347a-9372-a916dd789f23 | -7.39719 | -49.99409 | 2025-09-15 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73bdc62a-982c-3a8a-b1ee-d5855b3eecb4 | -5.18333 | -45.17454 | 2025-09-15 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69d63a97-6b26-3e37-8cd8-5ab3d67216c8 | -7.84361 | -46.10974 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f823cb79-7d08-3515-bf42-d4e060cb6970 | -10.88426 | -45.44624 | 2025-09-15 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e1a7959-7f87-3273-afc9-f8097066ac7a | -8.11091 | -50.1629 | 2025-09-15 04:49:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 398f6a63-4545-36db-84b8-3c29a156942a | -7.89302 | -63.70964 | 2025-09-15 04:49:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README45.md)
