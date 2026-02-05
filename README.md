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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0d0aa46-35c8-3154-bba5-4679cc5a30f3 | -6.9615 | -35.0843 | 2026-02-05 00:00:00 | GOES-19 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 100.4 |
| c8e7e3d1-d971-3fbe-a832-14d131c0975a | -14.0616 | -39.485298 | 2026-02-05 00:17:00 | METOP-C | IBIRAPITANGA | BAHIA | Brasil | 2912707 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9b8afaa0-9652-3bf6-90f4-3c3439d1b820 | -8.0794 | -35.3904 | 2026-02-05 00:17:00 | METOP-C | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| de690ce7-1c5f-33a3-89ef-26c5fb0ee81d | -9.2992 | -40.402802 | 2026-02-05 00:17:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 72c6fbc6-86e9-3364-8392-484554ca59ec | -15.4208 | -41.418701 | 2026-02-05 00:17:00 | METOP-C | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 63c1a74d-6459-3521-acf8-211887a9f40b | -9.9197 | -36.238602 | 2026-02-05 00:17:00 | METOP-C | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c648b8e8-e3bc-337c-8103-ec0cda205753 | -5.2767 | -37.710201 | 2026-02-05 00:17:00 | METOP-C | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 992a547d-b26d-368a-85eb-72e10e0b456d | -5.3404 | -40.550598 | 2026-02-05 00:17:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d27527e1-29e9-314f-baa1-4979678485e8 | -5.267 | -37.712502 | 2026-02-05 00:17:00 | METOP-C | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| b711d1d7-146f-356f-aa57-b1415eeebef4 | -20.2418 | -40.220699 | 2026-02-05 00:17:00 | METOP-C | VITÓRIA | ESPÍRITO SANTO | Brasil | 3205309 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| aea05f9f-262b-3288-be9d-e6adeed75f2f | -10.9253 | -45.148399 | 2026-02-05 00:17:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8cfac6c0-b6a7-3aa4-a769-1455f0035b54 | -10.705 | -37.036598 | 2026-02-05 00:17:00 | METOP-C | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 970fc698-0f83-3bc8-8ffc-ede199a0c146 | -8.4757 | -35.161499 | 2026-02-05 00:17:00 | METOP-C | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ef3fb26b-2a8d-3bf8-a90b-fd12e4571054 | -5.3423 | -40.558701 | 2026-02-05 00:17:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3785e335-2faa-3608-a1fb-076866585f4c | -11.5306 | -37.540001 | 2026-02-05 00:17:00 | METOP-C | INDIAROBA | SERGIPE | Brasil | 2802809 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f0535985-4577-3e94-bb70-694c781fdd4d | -5.3521 | -40.5564 | 2026-02-05 00:17:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| cf58980f-dda0-3012-b642-e47ba5f6f41d | -3.9475 | -45.845402 | 2026-02-05 00:17:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 81e1568c-efd6-330c-a982-a30e21627ba2 | -7.0614 | -35.939201 | 2026-02-05 00:17:00 | METOP-C | AREIAL | PARAÍBA | Brasil | 2501203 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 7401b12d-4f29-3a33-a716-9c17e67a9cb7 | -11.5209 | -37.5424 | 2026-02-05 00:17:00 | METOP-C | INDIAROBA | SERGIPE | Brasil | 2802809 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f0d3b526-e0da-335f-9f80-a8610e6ec8ab | -10.7147 | -37.034199 | 2026-02-05 00:17:00 | METOP-C | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0560a9d1-7f22-3f05-9f67-9c8f06e6a24f | -8.4854 | -35.1591 | 2026-02-05 00:17:00 | METOP-C | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6c16467e-ca2d-399e-95cc-d2c42ba70343 | -16.470699 | -39.096401 | 2026-02-05 00:17:00 | METOP-C | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| aaa46a88-a551-383f-bb6d-99bbf801589b | -10.7173 | -37.044998 | 2026-02-05 00:17:00 | METOP-C | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 56d21878-fbc7-3366-96af-3c578c0599a7 | -5.2642 | -37.700802 | 2026-02-05 00:17:00 | METOP-C | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 3fe9cac9-a5e6-3c74-a67a-29619d3f561e | -3.9459 | -45.838001 | 2026-02-05 00:17:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 31081272-b521-3f8b-8b69-c72f9167ca82 | -9.9294 | -36.236198 | 2026-02-05 00:17:00 | METOP-C | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6b307152-46cb-3134-a4fa-9bcdcd7e6f4c | -9.3393 | -36.816601 | 2026-02-05 00:17:00 | METOP-C | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| ee2c0fe8-b991-37e1-b3d1-9ef22cf1bf47 | -14.0599 | -39.477798 | 2026-02-05 00:17:00 | METOP-C | IBIRAPITANGA | BAHIA | Brasil | 2912707 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| add4282b-8032-3135-bfef-0579e0bfc03a | -9.9325 | -36.2486 | 2026-02-05 00:17:00 | METOP-C | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 771447a7-e99b-3190-a10b-71eb2781e2af | -10.5934 | -37.0872 | 2026-02-05 00:17:00 | METOP-C | SIRIRI | SERGIPE | Brasil | 2807204 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 48480797-9750-361a-833a-09c3d04820da | -16.468901 | -39.088799 | 2026-02-05 00:17:00 | METOP-C | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ea58055b-7def-3616-85fb-8aec294b0524 | -8.0832 | -35.405499 | 2026-02-05 00:17:00 | METOP-C | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5d3fb550-941f-3851-916d-6368e1139cad | -9.3949 | -38.236401 | 2026-02-05 00:17:00 | METOP-C | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7ae40e11-2daf-31e8-9b69-e2f5975ce7a5 | -17.8391 | -40.0798 | 2026-02-05 00:40:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 60.6 |
| 7d97e465-b696-3c0c-b358-61012014a8ff | -12.3008 | -57.39666 | 2026-02-05 00:47:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fd273a04-e087-3600-995e-308a72d4685c | -1.55556 | -54.53568 | 2026-02-05 00:49:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 12981c05-474b-38e8-a4fd-32095f8a1f52 | -1.55698 | -54.54582 | 2026-02-05 00:49:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4febad9b-f73d-3278-937c-ba8e58928916 | -2.56933 | -54.73711 | 2026-02-05 00:49:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2a03c5a7-40b3-382c-a156-d8fc0bc928a2 | -1.54758 | -54.54721 | 2026-02-05 00:49:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 50b9b010-491d-3423-b6cd-b0a0cf64dadf | -2.5707 | -54.74675 | 2026-02-05 00:49:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 4df0d36a-2e06-313a-8d35-69369996d0a7 | -1.54615 | -54.53701 | 2026-02-05 00:49:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 831b27bc-b835-3f7f-ab45-9ebb1e9c00aa | 3.43008 | -60.73287 | 2026-02-05 00:52:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 13.5 |
| a4b3b1ed-9cea-3259-96c8-22f7f997fc67 | 4.15284 | -60.76408 | 2026-02-05 00:52:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c0afad6c-c479-3bb7-bad5-5a70e050a0a4 | 4.39887 | -60.6332 | 2026-02-05 00:52:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 0150f010-56f7-31fc-a4c5-b89efc37473f | 4.15812 | -61.02604 | 2026-02-05 00:52:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f05c843a-183b-3e90-a83c-2e0bc205618d | 3.432 | -60.73881 | 2026-02-05 00:52:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 895d7976-5737-35aa-b9f5-bb7b4aac6389 | 3.51225 | -60.89104 | 2026-02-05 00:52:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c7a9861d-f166-320d-b20e-2ceef1b71fb7 | 3.43357 | -60.72794 | 2026-02-05 00:52:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ba42cee2-fd57-3707-b6a9-809218bcd65e | 3.90982 | -60.18265 | 2026-02-05 00:52:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d60e0e58-15f9-3b83-b419-9211c3bda728 | -9.45569 | -35.85387 | 2026-02-05 03:00:00 | NOAA-21 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| ed45f3c3-58f3-3aae-adbf-4d4ebf0234e1 | -9.49314 | -36.85399 | 2026-02-05 03:00:00 | NOAA-21 | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6a67848e-f9fa-3970-8168-cce390f722f1 | -10.56032 | -36.97509 | 2026-02-05 03:00:00 | NOAA-21 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 660e4e75-5fee-3ff8-a0f6-57774c1a060a | -10.56651 | -36.97642 | 2026-02-05 03:00:00 | NOAA-21 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| ab49eacc-47f3-379f-a053-483f0d9f1770 | -9.4591 | -35.857 | 2026-02-05 03:00:00 | NOAA-21 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 4c4d95d3-14d9-30ed-8d67-031cbb605ff3 | -9.39358 | -35.54209 | 2026-02-05 03:00:00 | NOAA-21 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| dbb46c7a-5a8b-3a0e-a5ec-3761518dbbbd | -9.4549 | -35.85809 | 2026-02-05 03:00:00 | NOAA-21 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 1d004e9e-35ae-38fd-b6c2-170d74136324 | -9.39439 | -35.5379 | 2026-02-05 03:00:00 | NOAA-21 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ecd24bf3-ca8d-31f6-8a96-2f47f8dbf151 | -8.98775 | -35.43714 | 2026-02-05 03:00:00 | NOAA-21 | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| e1ed4fb6-2750-3ce3-8ec7-e3cd8dc192ac | -9.49053 | -36.84926 | 2026-02-05 03:00:00 | NOAA-21 | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 5429268c-fc76-3b19-b884-00aec33e3ed7 | -9.49412 | -36.84898 | 2026-02-05 03:00:00 | NOAA-21 | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 34327a6d-e7a5-3b79-8a64-873969126691 | -9.4532 | -35.85588 | 2026-02-05 03:00:00 | NOAA-21 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 3565554a-17db-3912-9bca-936b60ce3dc5 | -16.47138 | -39.11194 | 2026-02-05 03:02:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 927a0983-a066-3765-af28-75a43dd0c061 | -16.46991 | -39.10971 | 2026-02-05 03:02:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 04172d74-0763-3504-82a4-14cab75f85cf | -16.46618 | -39.10548 | 2026-02-05 03:02:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7838de68-9cdf-3004-b71c-ea1231249a9c | -16.47258 | -39.10657 | 2026-02-05 03:02:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d8f44dbe-a4be-3c1f-91b7-b7a744a97251 | -16.47107 | -39.10435 | 2026-02-05 03:02:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 62a89093-bed8-3830-bf2d-231fd9cbd680 | -5.34182 | -40.56718 | 2026-02-05 03:27:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| aba7967a-efcd-3137-8431-a3c89cc17f99 | -5.34156 | -40.56901 | 2026-02-05 03:27:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 31682bd2-7765-3629-a5d2-33ebf8ddae1d | -5.34224 | -40.56506 | 2026-02-05 03:27:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a712dfa6-ccdf-3753-8621-ad49a109868d | -9.00837 | -35.99559 | 2026-02-05 03:29:00 | NPP-375D | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9baced69-c82a-305f-8e5c-efc387aa52b9 | -7.48524 | -35.17048 | 2026-02-05 03:29:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| d049172a-b9fc-3cb1-9ed3-9b736c9b052e | -10.93283 | -45.16808 | 2026-02-05 03:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2014e6a2-1a5c-3fa2-b59d-f27a66660d30 | -9.49292 | -36.85312 | 2026-02-05 03:29:00 | NPP-375D | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c6073e7c-860d-33d3-b221-8aeb2961fd21 | -8.71207 | -35.2813 | 2026-02-05 03:29:00 | NPP-375D | TAMANDARÉ | PERNAMBUCO | Brasil | 2614857 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 58a733cc-c4c6-33a8-8726-23aa4e42a7fa | -8.07997 | -35.4207 | 2026-02-05 03:29:00 | NPP-375D | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0eb75d19-2c5f-3b47-8a0a-899325056804 | -9.45642 | -35.85748 | 2026-02-05 03:29:00 | NPP-375D | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 7e09bdbb-0f06-376c-b7fb-d7abd32619b0 | -9.49702 | -37.05569 | 2026-02-05 03:29:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 398ef24a-876d-3033-b9ee-23f83e8a108e | -9.33645 | -36.834 | 2026-02-05 03:29:00 | NPP-375D | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 35d2f568-6294-3d10-a93e-9325df19f59e | -7.48912 | -35.17114 | 2026-02-05 03:29:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 82afa375-5402-307a-80dc-6139ebfffb19 | -9.49977 | -37.05934 | 2026-02-05 03:29:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 154e4f79-2b8f-3081-b638-28f26ece200c | -8.6734 | -36.2725 | 2026-02-05 03:29:00 | NPP-375D | LAJEDO | PERNAMBUCO | Brasil | 2608800 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4fdc8809-66a6-3bed-84bd-78921b6f9824 | -9.49359 | -36.84929 | 2026-02-05 03:29:00 | NPP-375D | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 15e3ae90-5b18-36d8-933f-353bae0f5a32 | -9.45249 | -35.85677 | 2026-02-05 03:29:00 | NPP-375D | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| b22c39f6-8fb4-3f0d-8414-e0cb691674c3 | -15.42011 | -41.42931 | 2026-02-05 03:32:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 72fb9c52-4de4-308a-9573-22fd79ea44e4 | -16.47135 | -39.10245 | 2026-02-05 03:32:00 | NPP-375D | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ec35ecb1-85e0-3d72-8e7a-ecb30b5df50f | -15.28526 | -40.96986 | 2026-02-05 03:32:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c1f8e8cb-6a0f-3ed9-85c7-f274e70c6ca0 | -13.38827 | -39.95837 | 2026-02-05 03:32:00 | NPP-375D | ITAQUARA | BAHIA | Brasil | 2916708 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| dbddfbae-626f-35e7-a54a-ad0c11169bbb | -16.46977 | -39.1109 | 2026-02-05 03:32:00 | NPP-375D | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 31ba5d45-4c21-38ed-b239-9c3b31fe1933 | -15.47865 | -41.64779 | 2026-02-05 03:32:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 6c31690d-a7d7-36a3-b444-6356d3b1bff7 | -18.13174 | -40.21537 | 2026-02-05 03:32:00 | NPP-375D | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6e10319b-716b-372d-bd75-72f553088f44 | -13.35904 | -39.90228 | 2026-02-05 03:32:00 | NPP-375D | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 441d62e9-1403-372b-a592-9c863fc355cb | -15.42523 | -41.43027 | 2026-02-05 03:32:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 641d42bb-9593-34e7-a97f-5cbf27434fbd | -15.42077 | -41.42606 | 2026-02-05 03:32:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 90e3a57d-8713-3754-b23c-826a1e7153d1 | -16.47057 | -39.10666 | 2026-02-05 03:32:00 | NPP-375D | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 313bd8e0-3f2b-3733-8baa-1a541dfdcf19 | -13.38346 | -39.95743 | 2026-02-05 03:32:00 | NPP-375D | ITAQUARA | BAHIA | Brasil | 2916708 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ebbdda20-bf1c-37c1-8e1d-93749f190d9f | -18.1331 | -40.21378 | 2026-02-05 03:32:00 | NPP-375D | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0d11ff91-a893-3b3e-9fbf-2f99016cebd2 | -15.42458 | -41.43349 | 2026-02-05 03:32:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8e8edce5-b128-3949-8c72-86710fa4cb61 | -15.41946 | -41.43256 | 2026-02-05 03:32:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 96ebfbcb-a9a8-3fd9-bedc-91db1e1e1e99 | -27.69023 | -48.75121 | 2026-02-05 03:36:00 | NPP-375D | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3158ea3e-f722-35f0-90e8-fff65acfeee1 | -27.6842 | -48.74914 | 2026-02-05 03:36:00 | NPP-375D | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |


[Clique aqui para ver as próximas entradas](README2.md)
