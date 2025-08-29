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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58b15d61-3747-314a-a42d-caf636a4f672 | -9.1156 | -65.7513 | 2025-08-29 04:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 5f196834-f6aa-307d-bf8d-a077cf8525d0 | -4.11338 | -48.01969 | 2025-08-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9969c654-e6ac-3a5b-a43e-85aefbf11d7c | -5.69968 | -45.96112 | 2025-08-29 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5ac31a33-a254-341c-b064-38841d699435 | -5.9871 | -42.97597 | 2025-08-29 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3089d093-ec85-346c-a1d8-08a85f948672 | -5.18498 | -46.07333 | 2025-08-29 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 781c548c-9bbd-3a53-aa48-c99af8870e2d | -2.37872 | -47.651 | 2025-08-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef7e885f-f451-3016-8dc9-47451fbeaf23 | -3.04346 | -49.42688 | 2025-08-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9de2352a-6564-398b-a616-148a0081a3c9 | -3.17069 | -48.80903 | 2025-08-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12a824e8-b40a-3a29-97d7-8ef71f90bd3e | -3.42247 | -49.04924 | 2025-08-29 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 110b6c56-9f94-3549-9e06-8be5843aec0a | -4.15099 | -38.48324 | 2025-08-29 04:38:00 | NOAA-21 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9d1abb28-b6cc-3e63-a27f-bb1ffe2c0252 | -5.80141 | -42.57395 | 2025-08-29 04:38:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d4096188-6d44-3f39-8e8c-24aed9020e96 | -4.08236 | -48.04356 | 2025-08-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3b0589e7-be94-323e-b2c3-259f2983260e | -5.70347 | -45.95967 | 2025-08-29 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1bd909f7-6a28-3add-95dd-40f9ab9a1e9b | -4.07586 | -47.95631 | 2025-08-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6cc6bddd-e5fa-31fe-bf24-037077c8c6fd | -4.85856 | -42.54068 | 2025-08-29 04:38:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4697d392-1e42-3db5-aee4-cb75bdea7d52 | -5.98774 | -42.97155 | 2025-08-29 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 50daada4-0a1d-35a9-8b59-6116bc1dafdf | -0.75371 | -47.75416 | 2025-08-29 04:38:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c50dc93d-06bf-3ad1-870d-ea3e80c22b29 | -3.38672 | -47.49072 | 2025-08-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46a08cde-6367-3616-9a97-a51378132615 | -3.10981 | -47.49548 | 2025-08-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b675d4ab-97a3-3db0-82e9-fa1b82160825 | -3.04014 | -49.42637 | 2025-08-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd87201f-e440-3fba-a6bf-aa28e87b8094 | -0.75703 | -47.75467 | 2025-08-29 04:38:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 896c5416-3085-39c0-937b-9170f3daef3b | -5.62128 | -44.99994 | 2025-08-29 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 5abb0827-4b52-3846-97fb-d312b0a033e2 | -2.44353 | -47.32439 | 2025-08-29 04:38:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7d97fb5c-8994-32ea-a680-1680dd12d650 | -3.42577 | -49.04975 | 2025-08-29 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 93a7b072-ddee-3a53-81a5-625e187ab83e | -5.18199 | -46.06851 | 2025-08-29 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dad973b4-3a1b-3b79-ac9b-51b25a838f9f | -4.40514 | -40.69338 | 2025-08-29 04:38:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 62b51e7f-3c1d-3d23-a338-9c18acdce849 | -5.62097 | -45.0121 | 2025-08-29 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a70ac8bc-e9a7-305b-974a-69fc377fd8da | -4.49069 | -47.68837 | 2025-08-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 25923432-e2d3-3293-871c-03ad68234277 | -3.66313 | -50.95231 | 2025-08-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1d93e0c2-3a12-3e26-92ea-5742b22350b0 | -3.75958 | -54.82087 | 2025-08-29 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 4462168c-b1d8-316e-bbc8-78b0fd123b2b | -5.78781 | -42.57108 | 2025-08-29 04:38:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 058c68c8-16b2-30f4-9349-a9c82278e832 | -3.99017 | -47.95745 | 2025-08-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dc0ff785-036b-3791-8add-75bbc3a358ae | -2.44633 | -47.32848 | 2025-08-29 04:38:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5302fd9d-b5cf-3a8c-bd93-78cfa812c7c7 | -5.69917 | -45.96342 | 2025-08-29 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| ee009a27-5051-3cee-955c-d86080827257 | -5.87785 | -42.95294 | 2025-08-29 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ea84090a-d87a-3147-a4ed-dc5235a2282d | -5.63188 | -42.60914 | 2025-08-29 04:38:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 09fad28f-b90d-3f5a-b40c-68d7e90b1778 | -4.11234 | -48.20251 | 2025-08-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 866afd86-78b7-37ce-bcef-9533ad11a391 | -5.69981 | -45.9591 | 2025-08-29 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6487338c-32fa-3c3b-9b07-3b677ee2618e | -3.27671 | -43.52994 | 2025-08-29 04:38:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d75774a-8e90-3d2c-ae82-95f3f829155e | -2.98451 | -48.60716 | 2025-08-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99c4b938-4520-3124-9613-45c128a23be6 | -3.76775 | -54.82236 | 2025-08-29 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 7ecd5101-1980-3d2a-a292-3045305e0cc0 | -4.48897 | -47.6771 | 2025-08-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c98c5870-aabf-3f1c-9e12-a37cf44a2392 | -3.76512 | -54.81335 | 2025-08-29 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ef3b79aa-6ad1-3d40-ae6c-127010abe735 | -3.17123 | -48.8056 | 2025-08-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa12f8e9-a0b6-376f-b9b4-f9bbb9c65cfa | -3.49303 | -48.9441 | 2025-08-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ffb83c9-b09a-3ba3-bf5c-e4f30e9ee979 | -5.63423 | -45.24396 | 2025-08-29 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ccf15fb-b44d-336d-9fa6-4cfa3252d8c3 | -3.98568 | -47.8811 | 2025-08-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 20bfe495-dbc9-3f34-a59e-851c9f708807 | -3.5307 | -52.98934 | 2025-08-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea71f495-35b1-36c6-b474-e19429673e1d | -5.6185 | -45.00181 | 2025-08-29 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 5f567114-513f-3623-a1db-863293e97b15 | -5.59184 | -46.32884 | 2025-08-29 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b8940b53-b264-3ff6-98f1-328de68c01ab | -5.80596 | -42.57479 | 2025-08-29 04:38:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 98ebfda2-ea70-3245-a9d1-0e940b833784 | -5.62441 | -45.00541 | 2025-08-29 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 1a6b6def-73d7-31c7-a359-7ee5aeb30887 | -3.76022 | -54.81681 | 2025-08-29 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 671ad7b6-fa5d-3608-bf30-864a359c5494 | -3.08949 | -40.10513 | 2025-08-29 04:38:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 244e1e71-44ff-3cb0-8f05-bff31929bffe | -2.91891 | -48.30811 | 2025-08-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 166ce09f-a811-3872-bd48-e8ffc138c8d1 | -5.59675 | -45.52248 | 2025-08-29 04:38:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe64f785-1f67-3987-a8b4-e932f687ab6c | -3.75858 | -54.82513 | 2025-08-29 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d570873e-5268-30ed-a942-e9b69c4abc14 | -3.04677 | -49.42739 | 2025-08-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e754136e-208c-3286-b2fb-a998ab11ed6d | -3.62009 | -43.54572 | 2025-08-29 04:38:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d3fc7cf3-8233-324b-a6fb-38cb99316ee6 | -5.86069 | -42.94558 | 2025-08-29 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| c05f7973-f759-3059-a770-fb753de59d88 | -3.98513 | -47.88462 | 2025-08-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e0245af6-d744-3e84-995d-9a8b2fd2c526 | -3.73901 | -48.94079 | 2025-08-29 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 622e0d75-7ee4-3165-bfca-96c41cbd8dca | -4.85923 | -42.53612 | 2025-08-29 04:38:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ab11b354-cf32-3420-8823-c9cc90547043 | -5.8164 | -42.59959 | 2025-08-29 04:38:00 | NOAA-21 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 72130372-d354-3d06-8789-51b7fa1276c5 | -5.6192 | -44.99692 | 2025-08-29 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9407f7c9-65fc-347d-998d-eeb785cba17e | -3.08903 | -40.10822 | 2025-08-29 04:38:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0453ff2b-90d8-3feb-9384-f69ba681393d | -3.76383 | -54.82149 | 2025-08-29 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 7c19a89d-d333-3943-b665-7343e0ab0318 | -5.78776 | -42.6044 | 2025-08-29 04:38:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| a2691700-bd62-31de-9d90-76b5af7984ca | -2.44297 | -47.32795 | 2025-08-29 04:38:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f741832d-6cd0-380d-be9e-ac87fef08c5a | -5.69614 | -45.95853 | 2025-08-29 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9ebcd0a-18fe-34b2-9735-7d614eec208b | -3.74333 | -53.80585 | 2025-08-29 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12025d3b-b229-32ce-bdc9-35298ccfaf01 | -5.71881 | -45.53367 | 2025-08-29 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7887179e-cfe7-39d5-9b47-8f676be6201f | -3.76417 | -54.81771 | 2025-08-29 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 12e301c1-9a19-3fed-acdd-372d74f81e4b | -5.63805 | -45.24458 | 2025-08-29 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e7f05285-f9a1-39ae-a8d1-5c5e413f8306 | -3.52755 | -52.86697 | 2025-08-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40fbc482-6f01-37ee-adba-381ca64bf311 | -5.87149 | -42.96552 | 2025-08-29 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 5217702d-30e6-3f4b-b956-ced3a7e34d61 | -5.62054 | -45.00483 | 2025-08-29 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| e94d0ded-c996-3e38-b283-dc479635d20d | -4.14315 | -48.61642 | 2025-08-29 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1069363-498a-3205-beaf-3b08e24e19cf | -3.41971 | -49.04529 | 2025-08-29 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 83efca3b-6330-3cbd-9f17-ad90a0c332dc | -5.6178 | -45.00666 | 2025-08-29 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| d865554b-4e4c-3d7c-8383-2f813ac32b55 | -4.48842 | -47.68069 | 2025-08-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4274d2e3-3b81-3e78-9aeb-9e2f35620b17 | -5.69601 | -45.96055 | 2025-08-29 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5e58de00-838c-388d-9676-082108228360 | -3.76061 | -54.81303 | 2025-08-29 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 58db77c5-ec9e-35e3-b3b8-1f22b3832ffa | -3.76087 | -54.81273 | 2025-08-29 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 888c47c5-c186-3741-bf8f-47c3830c6516 | -3.42631 | -49.04632 | 2025-08-29 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 50ebdcd3-97d1-3578-b39b-3edf5b304858 | -4.12856 | -54.89949 | 2025-08-29 04:38:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83b615c1-d5bb-3ebe-8124-5736147e1838 | -4.06918 | -47.95527 | 2025-08-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7eac023-d7a3-3399-ab6a-3ff7718a4cd5 | -5.70284 | -45.96399 | 2025-08-29 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d5ec1caf-9fb7-3e90-93f8-bb77bfcd7bdd | -5.69902 | -45.96542 | 2025-08-29 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a27ed8bf-23a8-30a1-a816-4b21bdb7792e | -3.80498 | -48.64815 | 2025-08-29 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f4ce582-5080-34f2-9780-45e85ecc91f7 | -2.92168 | -48.31207 | 2025-08-29 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3b4bdf50-96e6-31ea-8ed5-21f3c236c5c7 | -3.76283 | -54.82576 | 2025-08-29 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b5df662e-9c13-32c4-95e9-b7ddb012b8e9 | -3.04731 | -49.42394 | 2025-08-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9491137e-15a7-3414-ac76-005e666485de | -5.62203 | -44.995 | 2025-08-29 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| f70a6704-d5d7-3696-9fcd-9e3f5ca0c9e3 | -5.86895 | -42.9515 | 2025-08-29 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 0978ee20-4f61-374f-86dc-4bee09e0230a | -3.24079 | -50.80376 | 2025-08-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51c05567-9101-3f4a-970d-5c2462f610e5 | -2.55852 | -47.71856 | 2025-08-29 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccbd619d-56c3-3989-8e8d-66d24eaa7a26 | -5.71438 | -45.53763 | 2025-08-29 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dec5ede2-a1fb-30ab-b52c-50cc47b826d4 | -3.92545 | -47.69374 | 2025-08-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5373bf4-776f-3113-9904-70a1ce4354e1 | -3.17399 | -48.80954 | 2025-08-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README39.md)
