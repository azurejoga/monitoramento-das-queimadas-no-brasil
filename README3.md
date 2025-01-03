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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89d016d0-84f3-3f8f-bddd-4251b8d1bb60 | -4.16475 | -42.03191 | 2025-01-03 04:01:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 24.5 |
| 541e5dab-22b4-3993-98ea-766a22c209f0 | -3.9086 | -47.21049 | 2025-01-03 04:01:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d96fbfdc-9a69-3fe1-bd8b-b5ae66517094 | -6.12251 | -42.54318 | 2025-01-03 04:01:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 85f6da88-4108-33d0-9487-3df0c41ebc43 | -6.38393 | -39.93651 | 2025-01-03 04:01:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 843c236d-27c2-327e-8082-68a276692050 | -5.41403 | -43.20248 | 2025-01-03 04:01:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| edbfa027-df3f-3fb5-a99b-19604242e8ee | -5.53566 | -39.18002 | 2025-01-03 04:01:00 | NOAA-21 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fdafc599-86dd-3fbe-b602-5bb4fba3a45f | -3.3235 | -46.82987 | 2025-01-03 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bee24358-d9c7-36c6-b215-3bf51ddcbe2f | -5.92707 | -43.78326 | 2025-01-03 04:01:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1bd05008-1a79-3a42-a5ff-fd33d2b93138 | -3.21908 | -41.90873 | 2025-01-03 04:01:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c77743b-d028-3c16-a497-eaf1f8614d3b | -6.12188 | -42.5471 | 2025-01-03 04:01:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 7ccfda6e-53eb-3ffb-b6ed-9b8598e7d1da | -6.75502 | -35.06025 | 2025-01-03 04:01:00 | NOAA-21 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4c4b9d48-6577-338f-b1cf-06dbef422d2f | -3.69611 | -38.82618 | 2025-01-03 04:01:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d439f960-c6bb-3eca-9701-c1b65d22109c | -8.72424 | -35.71711 | 2025-01-03 04:01:00 | NOAA-21 | CATENDE | PERNAMBUCO | Brasil | 2604205 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a3693ef8-b13e-3854-8885-5cc0ce1ae5f8 | -6.65587 | -38.90834 | 2025-01-03 04:01:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 272d35e1-45de-3b6f-a91a-6e949df2e34d | -5.66921 | -45.20906 | 2025-01-03 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54e10fa7-2235-3b9e-9107-31bc41bcc6da | -10.79328 | -37.25089 | 2025-01-03 04:01:00 | NOAA-21 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 93cd278d-b5ea-3b37-999e-01cd6bbdf30f | -6.23627 | -43.31698 | 2025-01-03 04:01:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67087f46-c9b7-3762-b415-59c776dbd868 | -7.81153 | -35.23549 | 2025-01-03 04:01:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9b63fee3-540b-336e-9e38-55f71d4694ce | -9.87319 | -36.28551 | 2025-01-03 04:01:00 | NOAA-21 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c0d55e54-088e-3a4a-b4db-b7f26b477a30 | -8.0682 | -35.15712 | 2025-01-03 04:01:00 | NOAA-21 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8d4f8dc2-565f-3d34-b5cb-b0d396a86903 | -4.5394 | -44.05622 | 2025-01-03 04:01:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b9cac6c-df5e-3077-9046-7a9bb9201962 | -4.80426 | -43.30655 | 2025-01-03 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 55e70b63-3050-36de-9878-93725c9480f9 | -4.26165 | -42.60387 | 2025-01-03 04:01:00 | NOAA-21 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32c58025-56fe-3c85-babc-57277a568b01 | -3.55778 | -43.56363 | 2025-01-03 04:01:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44bfcad7-0d06-3520-9203-469e330f1264 | -7.23548 | -39.77731 | 2025-01-03 04:01:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b9a149e2-236f-3160-bcf7-78d4fd1f1bc8 | -4.26099 | -42.60795 | 2025-01-03 04:01:00 | NOAA-21 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2e9353d-fef0-37f6-83b3-d612606ea988 | -5.93442 | -35.62176 | 2025-01-03 04:01:00 | NOAA-21 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8cbe420f-cf97-3f91-96d1-10843474255f | -4.87531 | -39.05229 | 2025-01-03 04:01:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 912a84f9-242a-39d3-88d4-8f63c0cda6cd | -6.12888 | -42.54818 | 2025-01-03 04:01:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| fb1925f1-4b8c-3904-819b-a3a372c675bd | -5.92481 | -43.77373 | 2025-01-03 04:01:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04c4f5a1-4a43-3bac-8789-0205de432786 | -3.86023 | -40.45272 | 2025-01-03 04:01:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 7c839ba0-b299-361b-b084-6b27ff50e0b8 | -5.97538 | -44.29317 | 2025-01-03 04:01:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7df32ea8-d984-374f-ab6f-cb663574905a | -7.20556 | -39.72999 | 2025-01-03 04:01:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b484a983-05f9-39a9-95ce-57dd64191ded | -6.29346 | -41.01297 | 2025-01-03 04:01:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fab1214a-6d2b-3bbb-a8f9-0dcd95b86a5c | -5.5354 | -42.89589 | 2025-01-03 04:01:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 55da2f39-10e3-3ba6-bcf0-630aa030b90d | -6.12951 | -42.54427 | 2025-01-03 04:01:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 58e8855d-4618-3f70-b339-38bccf158655 | -4.16188 | -42.02747 | 2025-01-03 04:01:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 24.5 |
| 1470d725-96ca-3254-a8c9-6b9ca8d08dfe | -7.97133 | -38.43038 | 2025-01-03 04:01:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c2c6ad3e-4a65-364c-ba40-360e51e0fc81 | -5.631 | -44.83963 | 2025-01-03 04:01:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e7f6d7f4-0065-3d98-b9f5-1f4d0bc851dd | -7.8852 | -42.44254 | 2025-01-03 04:01:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 634151fb-22e0-38ff-ab91-6f40d9e2802e | -8.44768 | -40.77098 | 2025-01-03 04:01:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b0430104-0fe1-30f3-b616-489ce25196e2 | -6.46216 | -39.95986 | 2025-01-03 04:01:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0a149263-6f21-3b28-a6e2-73736f6519b8 | -5.40104 | -42.93913 | 2025-01-03 04:01:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e973322d-b14e-38a2-a3ce-d424081cf4a8 | -6.7753 | -38.61503 | 2025-01-03 04:01:00 | NOAA-21 | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c2952fbb-c313-311e-9900-5edaea99faf5 | -7.97189 | -38.42662 | 2025-01-03 04:01:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 155c54a3-578e-3ad6-b683-a0a6e79bc6c5 | -3.54375 | -41.96569 | 2025-01-03 04:01:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0791e4ea-4b09-35af-a780-10a09e862b12 | -4.2363 | -42.13025 | 2025-01-03 04:01:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 609de9ce-2045-3465-ab2e-b0bec630b85d | -6.97525 | -43.54963 | 2025-01-03 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 122ea32a-347e-3c6b-aeb9-da76b36e3b46 | -7.48608 | -35.12629 | 2025-01-03 04:01:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 981404ce-0269-3412-bb35-b396a535c613 | -6.9782 | -43.55447 | 2025-01-03 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 68caabe4-acaf-3c1a-8469-56b28fbfec2c | -3.45491 | -39.56701 | 2025-01-03 04:01:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7658d59c-6b52-3892-8152-0abac6fe7839 | -5.04815 | -41.53243 | 2025-01-03 04:01:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4973b335-4d48-3489-be83-0b4cb362017e | -2.29811 | -46.41585 | 2025-01-03 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bb7fc702-35c6-3b7e-a25f-f6030d13e449 | -4.48598 | -47.14132 | 2025-01-03 04:01:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b527ed7d-5841-3a28-aa5e-5e701abb400e | -2.29889 | -46.41091 | 2025-01-03 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f1fb6f97-5c46-317e-83f7-5a0e337af81b | -10.73464 | -36.986 | 2025-01-03 04:01:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0228e439-0a64-3256-9475-c4f105a502eb | -5.63043 | -44.84307 | 2025-01-03 04:01:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d14b6824-922e-3bd9-bd90-f94c7b667bf8 | -4.90065 | -40.09044 | 2025-01-03 04:01:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 59df33fc-9750-37e9-9876-726b6fb903f5 | -3.86356 | -40.45323 | 2025-01-03 04:01:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 6e5302f6-e88b-3a9c-8457-523b3ad28311 | -7.81609 | -35.23258 | 2025-01-03 04:01:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 5eb2a54e-3514-3199-936b-c60b9f687c8f | -7.88863 | -42.4431 | 2025-01-03 04:01:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 136e16d5-892c-3117-a142-5fc17d587053 | -7.14454 | -35.07262 | 2025-01-03 04:01:00 | NOAA-21 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0fbb59b2-001b-3917-b0bc-f0733f778f26 | -2.2942 | -46.41018 | 2025-01-03 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9b9f1cd-d17b-3159-b3b7-93b0414157ad | -7.73276 | -39.10658 | 2025-01-03 04:01:00 | NOAA-21 | PENAFORTE | CEARÁ | Brasil | 2310605 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1d799d2e-a43a-304a-b32a-3c864dd883e4 | -5.50127 | -44.83183 | 2025-01-03 04:01:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 803b1579-f94e-39c8-b604-24f97a9a7409 | -7.76712 | -34.93645 | 2025-01-03 04:01:00 | NOAA-21 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 9de8dad2-431d-3721-89ac-431dae8bb09e | -4.99356 | -44.16632 | 2025-01-03 04:01:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 468f1958-c8a4-30b2-94a2-b413705fd8ec | -8.07229 | -35.15771 | 2025-01-03 04:01:00 | NOAA-21 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2a7a0802-c778-3148-8930-cf0abe7f15e5 | -9.02066 | -40.26167 | 2025-01-03 04:01:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c421aead-7615-33c8-ae72-a2807c91f28c | -4.40355 | -43.3758 | 2025-01-03 04:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 673a00f9-171e-350f-abde-4de099e3f0d1 | -5.18597 | -41.53161 | 2025-01-03 04:01:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e45d635b-1188-38b5-93cc-febc21b2d17e | -9.02429 | -35.71773 | 2025-01-03 04:01:00 | NOAA-21 | JOAQUIM GOMES | ALAGOAS | Brasil | 2703809 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 02abe8c9-4cfd-3e5a-90e6-5adc742298db | -5.63558 | -44.8368 | 2025-01-03 04:01:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 1ff1b7b5-f80f-3c48-bed4-bbfcfbc11ab1 | -10.61014 | -44.32589 | 2025-01-03 04:04:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ee45e604-251e-3057-ae4e-f94cac1fdce1 | -11.07087 | -45.16015 | 2025-01-03 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db84b8be-aaf7-3112-ba80-3718a2802c64 | -14.64861 | -42.89303 | 2025-01-03 04:04:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 73354034-0836-352d-a47f-415a88f11834 | -12.26471 | -44.98486 | 2025-01-03 04:04:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e0c1283-e0ce-38bd-a99e-117e9bcd96a9 | -12.2181 | -42.4471 | 2025-01-03 04:04:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a49a8c2a-d887-3e17-876b-35ec9738969a | -11.01821 | -40.86554 | 2025-01-03 04:04:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 8fb8179f-7332-30cc-8e5a-7e10a80bdbd9 | -12.18557 | -40.50594 | 2025-01-03 04:04:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 49afc4c8-6be9-3a83-9866-a6fa4265614d | -10.98735 | -40.47237 | 2025-01-03 04:04:00 | NOAA-21 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 105f4bd6-a82a-37f7-b16c-a37b4f8dd53e | -11.93093 | -40.41461 | 2025-01-03 04:04:00 | NOAA-21 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cf00654c-1ec3-320f-a3ce-2ea956bab418 | -10.98295 | -40.47891 | 2025-01-03 04:04:00 | NOAA-21 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ce95a9c4-db31-3a6b-a3d0-f7254abad34b | -15.07934 | -48.94511 | 2025-01-03 04:04:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dcd15fc4-7d0b-31a0-b219-991fc46c74e8 | -12.18649 | -41.35889 | 2025-01-03 04:04:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b6f231bf-3a30-3ca5-8a31-496a3b81ab37 | -11.01545 | -40.86152 | 2025-01-03 04:04:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 110116fe-e9b8-32be-8704-e6df07d4edb0 | -10.61232 | -44.33503 | 2025-01-03 04:04:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 07f35d1b-dd42-339a-a668-14c82c8ceec6 | -11.22445 | -41.87175 | 2025-01-03 04:04:00 | NOAA-21 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6ab63584-e0c1-3343-8f27-e2a05030eb24 | -11.96928 | -41.33427 | 2025-01-03 04:04:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9667af1a-9e23-3423-9264-fbd1d8deb0e6 | -10.61304 | -44.33076 | 2025-01-03 04:04:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2af4186e-b400-3eb7-902f-8cd6537589d9 | -10.82753 | -45.15012 | 2025-01-03 04:04:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1c196732-7657-312f-bbdb-162ff2473dbd | -14.87505 | -40.77908 | 2025-01-03 04:04:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c3c48eba-2276-384e-8629-72136b8dab57 | -12.94267 | -39.53843 | 2025-01-03 04:04:00 | NOAA-21 | ELÍSIO MEDRADO | BAHIA | Brasil | 2910305 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d533d30e-6d3b-3395-831d-c7dc0969f7b3 | -11.01875 | -40.86205 | 2025-01-03 04:04:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fdeed398-e5f3-3f49-8267-42c666d6b177 | -12.19034 | -41.35592 | 2025-01-03 04:04:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a37167fd-5f49-3b54-8d6a-be0e134bd235 | -10.60725 | -44.32101 | 2025-01-03 04:04:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ed4f5146-4cb6-3185-8c9a-d885f0717916 | -10.60653 | -44.32527 | 2025-01-03 04:04:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2fb6a5ba-ed6c-309a-8519-ecfd2c5f8863 | -11.0671 | -45.15957 | 2025-01-03 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a050f0a4-c71d-3c06-a502-67e0a041c35b | -11.0149 | -40.86501 | 2025-01-03 04:04:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| faead6e9-c4f3-3a57-ae05-f289c131f2f0 | -12.21751 | -42.4507 | 2025-01-03 04:04:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |


[Clique aqui para ver as próximas entradas](README4.md)
