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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8c55766-3d7d-3b69-8d0f-ee08fcc72d7f | -2.56543 | -46.565 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33801b1e-dfdf-3f1b-8b1e-85d57604741b | -3.18041 | -46.26006 | 2024-11-25 04:33:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc8872b6-959f-3c49-b08a-ea4b0e93aae9 | -3.22851 | -46.43261 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78e56fd2-6202-3c55-ba62-cedc03b1b598 | -2.79928 | -46.81026 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64418187-9928-3ec4-9477-8085be1fbc61 | -1.72245 | -53.25045 | 2024-11-25 04:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3479217b-c1c7-357e-acf3-337b80fc31cb | -3.81106 | -46.60178 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 990bcc6a-1ee6-3da4-9ecc-fc32d5abd6d4 | -7.30892 | -55.30546 | 2024-11-25 04:33:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bd11e6c9-60b3-3021-bf14-6bf7be804ad3 | -8.56105 | -49.22531 | 2024-11-25 04:33:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2448cf72-327b-37d4-ab15-d10f9856e6ae | -4.05486 | -46.85007 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2cd5134-75f3-3569-98f0-686117c19a1e | -2.59304 | -46.56215 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3e1783a-e75b-308c-86d6-e029597801e3 | -4.24189 | -48.70056 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55aa8b16-ab8a-33b8-8183-6eea5acc0471 | -2.50137 | -46.23101 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb88eaa9-9f7c-37a4-b2f9-5deecb3649e7 | -2.81514 | -54.11762 | 2024-11-25 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec642b3d-258c-362c-b68b-21fd6b44ffa3 | -2.54799 | -46.54467 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7aced89e-0525-34ba-ad95-83cd67289306 | -3.83005 | -46.8965 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 863657e6-99c9-3983-a6af-e6f85aabd622 | -3.24989 | -54.22216 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bad04a7-4f10-3221-9d27-785a646da846 | -1.63778 | -52.10514 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f55f4d2-612e-371c-b3d2-73564af8f10e | -4.05886 | -48.32799 | 2024-11-25 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c6511d1-abc1-3f3d-9f1d-8ba16acaa3b6 | -3.50015 | -53.81997 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9de66625-1b01-36b7-987e-86d60ffea69e | -3.95488 | -46.90226 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa7301ce-f7fb-3ba9-ab16-d0368ece175c | -4.05261 | -46.84262 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7128e847-21d0-34da-989c-23218c65c722 | -4.19469 | -50.68678 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4297f8e0-1b75-3bea-b73b-165c17c0d36b | -3.97981 | -46.65322 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a324236-a05a-31fe-8098-2d612b09cc68 | -3.80977 | -51.37508 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64ad0eda-8be1-306c-a1e1-dc341c267236 | -2.66835 | -46.60268 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e47d2321-c796-3d0a-b8b9-1a049f551cb1 | -3.77812 | -46.68247 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5728785-afbf-392d-be29-60e76d4601ed | -5.74861 | -45.38429 | 2024-11-25 04:33:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e4b4e43-bdcc-321a-beeb-9bebc97e0c2a | -2.33369 | -53.8628 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ba03dec4-0e78-3784-b823-587b61ca91c1 | -1.62468 | -52.44566 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 164511ad-e97f-3388-bf13-f5ff96d3ae8c | -4.20586 | -50.23614 | 2024-11-25 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f9a91df-3324-3d22-81e4-68c61c993193 | -2.94278 | -51.00141 | 2024-11-25 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba9673f7-b52d-39d1-8ca2-e78e0a58f6bb | -2.74065 | -54.11141 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58288382-3620-3f43-ae93-7cc843aab258 | -4.23405 | -48.64174 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7d0727af-cbf3-31eb-a7ce-ade8e1386f37 | -8.31926 | -49.37686 | 2024-11-25 04:33:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8b648a7-81b4-3f4e-883e-7197b220ccf0 | -4.47364 | -45.5351 | 2024-11-25 04:33:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c29d1ddf-270b-396f-8f64-98f7c9f22d76 | -3.06017 | -53.22346 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d9561db4-9cdb-3809-8c27-589326829e7f | -3.33776 | -53.30779 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 249a26db-eacb-3db9-b7ad-6e48e4a7ae94 | -3.10656 | -53.96897 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd150a52-2d82-314b-bbf2-6d5a51281ee7 | -4.1406 | -48.76093 | 2024-11-25 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e7919a6-69c3-336b-aec8-12a7f4a794f0 | -2.52271 | -46.29158 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e48394a-0ded-3406-812f-13db01c23bb1 | -3.38696 | -50.73543 | 2024-11-25 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 966dd9dd-c6e3-3758-ae2f-affc0844223d | -3.28895 | -45.73548 | 2024-11-25 04:33:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 3cdf3fbe-3db9-3423-9868-2e8e01ddcb06 | -2.70393 | -46.287 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e6b362c-b28d-3fb1-83a7-dfa956b57569 | -4.06033 | -46.83669 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6de74320-9962-3e56-a742-be43e7f619a6 | -1.77127 | -52.71381 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef751280-128a-376f-8280-88d3cc156129 | -3.88367 | -52.34135 | 2024-11-25 04:33:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d41b727e-26cc-3668-9eca-5412da603e83 | -4.24572 | -48.63273 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| df8e2fbe-8f25-3641-9b27-d2515a810488 | -3.20823 | -51.42255 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1024001-9fdb-3465-83fb-0c624b8201a1 | -1.80335 | -50.90976 | 2024-11-25 04:33:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1873b63c-d659-320c-bccd-fcc70b2b90ee | -2.62894 | -46.13175 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aea92315-3bde-33ed-8e27-7db7f8b1b8ae | -3.78809 | -46.68401 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bd976a4-cfd0-30a5-a0dc-8110e15b1f74 | -5.58756 | -45.20742 | 2024-11-25 04:33:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 44bf4155-f80c-3899-a479-03602731f773 | -3.85012 | -52.14967 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b4c48e94-254f-3912-8c0c-51fff169af49 | -2.70765 | -46.21941 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce5ab7d5-8dc1-3a35-8d76-b79b64b0d3dd | -2.62315 | -46.21364 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9665f13b-0f56-3d0f-bdb4-997da74ae782 | -3.28738 | -51.12328 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b5f64842-c48b-3fc7-8c8b-a01fd57d18ad | -3.231 | -53.92496 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3b96128-87b8-3a2a-840c-f01cf02cdbf1 | -5.56671 | -50.9515 | 2024-11-25 04:33:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8f44d3b-4a9a-3416-aa95-f572719dabac | -1.4453 | -52.44913 | 2024-11-25 04:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93f7c587-0346-362e-81e8-1cab5af54f6d | -4.88748 | -45.71914 | 2024-11-25 04:33:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b48d94a-9fdb-332e-b0cc-b48ff3f95e08 | -3.68623 | -47.12182 | 2024-11-25 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 059e4405-756c-3411-9002-50260a30c6ee | -2.66072 | -51.715 | 2024-11-25 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21ae09db-983f-3512-b12b-e7a222d6ba32 | -1.62528 | -52.44194 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b4ab35f3-348d-3ee7-9fb0-b3674063ae9f | -3.87337 | -52.2046 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2378c864-f90b-33f8-bf8a-f34ad5ac1638 | -3.95659 | -46.91315 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b25318e-84be-34fd-9c19-be92d9833287 | -3.62453 | -55.30137 | 2024-11-25 04:33:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 65152606-2b13-33db-b435-ecf8ccec5811 | -2.65775 | -46.25482 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 597ec912-279f-364d-8aaf-2aa2b71c2fc0 | -2.59863 | -46.26389 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f72fe4ed-d452-3232-a4cc-53f62100c5a4 | -3.37814 | -54.67528 | 2024-11-25 04:33:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b365dd1-9b4e-365b-bc38-50f3ae2af0b6 | -3.68516 | -47.12871 | 2024-11-25 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b76c7551-45c6-3483-912c-f2f4b7e01c52 | -4.02862 | -50.5039 | 2024-11-25 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2fdfa38e-c945-3f5e-ba93-bd71ba08e163 | -1.35019 | -54.6364 | 2024-11-25 04:33:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f3c4c57f-453c-3a98-864d-228621b8e304 | -1.54972 | -52.58123 | 2024-11-25 04:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 37126950-530a-3ae7-b0fa-eb0786021c72 | -5.97319 | -46.30465 | 2024-11-25 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da8335dd-1d2d-3625-8257-1e9fd8e68a9a | -3.18015 | -46.50399 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 924d059f-0bd3-3753-9737-1bac97d10083 | -3.95991 | -46.91366 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ce8692c-3815-3848-9e86-e3af83276d38 | -3.67201 | -44.77601 | 2024-11-25 04:33:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f7c7f06-c051-3597-b17f-34d18e2c9d8a | -4.10334 | -50.71581 | 2024-11-25 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b558b554-4293-364a-9793-b54126302681 | -3.24238 | -46.43116 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78ee6d18-99e8-3d8a-9f5a-8158c547efba | -2.66503 | -46.60217 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bc03e6b-ba17-3863-a736-f10522507608 | -3.27467 | -53.81763 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad08ff33-8b87-336a-af16-9d4afb2eb368 | -4.0287 | -49.91496 | 2024-11-25 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2065c486-21c9-3f3d-9c33-e02a68cec4a0 | -4.26062 | -48.53803 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ecef1e91-fef5-3142-ab8b-410ca504a521 | -2.56265 | -46.56103 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e384ca67-43a1-3334-83e9-69654b5ae72e | -2.62532 | -46.19962 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aca6ba01-710d-3ac6-a47c-7013db6d876c | -4.29203 | -45.96862 | 2024-11-25 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26af4d7b-975f-3e38-9e19-76649e77f399 | -2.53974 | -46.40126 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30f9b4e9-651c-31ad-9905-b2500d640bd4 | -5.13453 | -46.19295 | 2024-11-25 04:33:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cbf92c94-44bd-3571-83b3-f087e17f09c7 | -3.27743 | -48.75667 | 2024-11-25 04:33:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bfc027d3-4628-3906-b7d4-c3ddf95573c4 | -2.58972 | -46.56163 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5973b921-f1dc-35ec-8ec5-6c7a22231da4 | -4.03536 | -51.02011 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24846986-5a00-39d9-a976-be4ea8702f6f | -4.24457 | -48.59663 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9452b898-f33f-3013-9f80-0123f2a29ef4 | -3.85095 | -52.14463 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6dccd66d-226f-3aab-b8a1-553d82fccab0 | -2.63037 | -46.21117 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62b72799-4c3a-3a85-bee3-430dad5a0383 | -3.80345 | -51.17764 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 056f9ab1-3f53-35af-b487-e12591781168 | -2.62649 | -46.21416 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b2015df-3394-35f7-b031-3f2069a46760 | -3.25255 | -53.59249 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d49b9b0b-720c-3c25-9ab5-f631af3f2a2e | -3.87934 | -46.66582 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1aefed45-c8ef-3818-b0ad-179947e9e62d | -5.8122 | -47.90364 | 2024-11-25 04:33:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fad0cade-095e-3396-9991-18318890c022 | -2.69813 | -46.19281 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README23.md)
