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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5d443f0-2356-37a3-9b71-3daf1be61dae | -23.7587 | -51.8688 | 2024-09-26 03:07:17 | GOES-16 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 85.5 |
| c6d3c8cd-5779-3441-bb30-31af6064ff6c | -23.758 | -51.8917 | 2024-09-26 03:07:17 | GOES-16 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 85.3 |
| b086a00b-d674-38f3-b469-26469dcd8a64 | -5.15735 | -37.73335 | 2024-09-26 03:15:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 38237c36-0744-39a3-ac05-3cbb7470ce49 | -5.15678 | -37.73668 | 2024-09-26 03:15:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8a509c4e-604b-364d-a8e3-a43e74bb08b6 | -4.56922 | -38.48139 | 2024-09-26 03:15:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c7484289-0fbf-3631-bfd9-e6d74be505b4 | -4.56856 | -38.48522 | 2024-09-26 03:15:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7f50f3df-6dc2-3849-9ac6-e0b12a1384b0 | -4.53325 | -38.03292 | 2024-09-26 03:15:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f28221f6-3960-3064-bcde-79c791bfd9e1 | -4.53262 | -38.03656 | 2024-09-26 03:15:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| fd1c0ed1-e6d1-3518-a8be-92057048ce5b | -3.79832 | -41.58477 | 2024-09-26 03:15:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 97450b55-cc8c-3923-9a79-c09e0b60f851 | -3.79717 | -41.59122 | 2024-09-26 03:15:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 8e5314c8-e5d5-3ef2-9bcb-fe81ee054517 | -3.79601 | -41.59777 | 2024-09-26 03:15:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 19f6aa8a-1d8d-3262-83fe-b4a403a17b9e | -2.6785 | -57.531 | 2024-09-26 03:15:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| c6165a57-5f6e-35b9-a408-36b5c3a3d432 | -2.6968 | -57.5307 | 2024-09-26 03:15:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 7b09487b-70da-38bb-a1b2-5df317359842 | -3.5673 | -50.3794 | 2024-09-26 03:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 5eae3ef5-a246-30c7-a4b8-201613e63c80 | -3.9208 | -46.4459 | 2024-09-26 03:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 79.8 |
| aca6d252-ab8c-3025-9758-cf13fe295661 | -6.8024 | -59.3044 | 2024-09-26 03:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 1f7fec61-3d0b-3ba3-aa38-9899ac469925 | -6.9306 | -63.1053 | 2024-09-26 03:15:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 20090907-c862-368a-ba97-e91301c5320d | -6.949 | -63.1048 | 2024-09-26 03:15:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 2fd27e2d-b278-3856-befe-6983f59348cc | -7.3636 | -55.5334 | 2024-09-26 03:15:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 8fe96b1f-ae4d-3e8b-bf46-363d8228fdd1 | -7.3637 | -55.5134 | 2024-09-26 03:15:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 379.2 |
| ac966ead-b901-3a36-9719-b7b83fd03590 | -7.3639 | -55.4935 | 2024-09-26 03:15:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 204.6 |
| d1305666-01e2-37d0-a99f-5fabda2b6b40 | -7.3821 | -55.5324 | 2024-09-26 03:15:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| d32cbd24-518f-3c7a-9198-429c88c74f64 | -7.3823 | -55.5124 | 2024-09-26 03:15:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 254.8 |
| e6495ba0-4d51-33bc-b3c6-049be21a5ece | -7.3824 | -55.4924 | 2024-09-26 03:15:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 154.2 |
| 9a852e2e-a993-3c6f-8418-3444b5b32f36 | -7.5894 | -42.2971 | 2024-09-26 03:15:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 72.6 |
| 1588e43d-4f3e-3128-9227-34a92910f5df | -7.797 | -54.7263 | 2024-09-26 03:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 22bc6264-80dd-32ea-ad98-137a6edcf2b4 | -7.8154 | -54.7453 | 2024-09-26 03:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 151.0 |
| a6ee377b-0ec0-3e38-8fec-0b4905631cff | -7.8156 | -54.7252 | 2024-09-26 03:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 185.9 |
| 231cff67-50c6-396e-836b-68abfc6fd762 | -7.834 | -54.7442 | 2024-09-26 03:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| a83c27ff-b8ab-3f5a-a44a-b462e78e75b4 | -7.8341 | -54.724 | 2024-09-26 03:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| e69dcb7f-397e-300e-933d-4e3c2d82b4ae | -8.1394 | -61.2817 | 2024-09-26 03:15:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 0935c5ea-7f53-3fcd-aa1f-861abf9c50c3 | -8.3153 | -55.0157 | 2024-09-26 03:15:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 1a2125b6-960b-3b64-9b74-037d906a549e | -8.3155 | -54.9956 | 2024-09-26 03:15:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| fee39a24-35d2-326f-a95b-3fe048f13bac | -8.8098 | -58.2172 | 2024-09-26 03:15:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 18dda4e1-90da-3acd-b90c-4462f2e29cb0 | -9.0657 | -61.3743 | 2024-09-26 03:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.8 |
| da58208a-0923-3519-a476-78bcfc4349d3 | -9.086 | -61.1245 | 2024-09-26 03:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 0c8be3bf-648a-3f6d-a36a-0927ed2767de | -9.1046 | -61.1237 | 2024-09-26 03:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 67b98ed4-a50f-3021-bd65-92ba739c94e6 | -9.3462 | -51.0704 | 2024-09-26 03:15:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 127.4 |
| a77fd530-c371-3d00-9fd0-2e5ab892a1af | -10.0322 | -53.4859 | 2024-09-26 03:16:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 47609d98-5223-327f-a27c-a46074f9e9da | -10.0324 | -53.4654 | 2024-09-26 03:16:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 7d6275f2-6c40-31cb-83e3-8d9f1c5f6869 | -10.0327 | -53.4448 | 2024-09-26 03:16:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 9de2b986-40bf-3264-aea2-32c3414493b0 | -10.0513 | -53.4638 | 2024-09-26 03:16:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 37d13ae7-84c0-308c-9b88-c5482f77b12e | -10.8355 | -45.8615 | 2024-09-26 03:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 1e446434-a207-3a6a-947e-5fc382b906d5 | -11.2029 | -45.5387 | 2024-09-26 03:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| f64401e2-72b0-3b66-86fe-a415548dad37 | -11.2033 | -45.5158 | 2024-09-26 03:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 5f7d7dc1-35f9-352e-b0f5-853a097456fb | -11.2217 | -45.559 | 2024-09-26 03:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.0 |
| a1983a7a-265c-33c6-a982-5e54cee9efd4 | -11.222 | -45.536 | 2024-09-26 03:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 226.0 |
| 9ea07928-ecf5-3e50-92af-1dcf9dd3fbf4 | -11.2224 | -45.5131 | 2024-09-26 03:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 2991c18f-4053-39cc-bea1-e7b10dc1ca90 | -11.2412 | -65.2997 | 2024-09-26 03:16:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 38.7 |
| af58f31b-7db6-33ba-a9e3-f0b52bf47822 | -11.2413 | -65.2809 | 2024-09-26 03:16:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 9a3ecdbe-3f5d-350a-ad0b-f8f4d1c6923a | -11.2599 | -65.299 | 2024-09-26 03:16:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 144.9 |
| df223df1-c14f-3ad1-9cee-92f990a4c02b | -11.26 | -65.2801 | 2024-09-26 03:16:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 131.6 |
| a087f0da-0e37-3bea-90df-085045d9aba4 | -11.2786 | -65.2982 | 2024-09-26 03:16:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 72266637-0a85-3134-b02f-46a2ed05b12a | -11.2788 | -65.2793 | 2024-09-26 03:16:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 71c31851-003b-30d8-9153-241090f4859e | -11.955 | -60.363 | 2024-09-26 03:16:14 | GOES-16 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 3499d42a-c94f-3df7-9566-5ba8bcf17697 | -12.2367 | -45.5045 | 2024-09-26 03:16:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 66f7f3ea-6f41-38f4-b405-4932541478b4 | -12.5026 | -48.9198 | 2024-09-26 03:16:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 4aa8fed8-6fda-3cce-a051-31f01ccbe18d | -12.5276 | -53.496 | 2024-09-26 03:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 7f56c82f-30aa-3c02-817a-912e51e6e19f | -12.5467 | -53.494 | 2024-09-26 03:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 0462d0bd-f6a5-3532-9a00-7abe70f8157b | -13.2152 | -45.6507 | 2024-09-26 03:16:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 06973ed3-29a1-322d-8fa6-6a76356faa41 | -12.841 | -62.7067 | 2024-09-26 03:16:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 9465ca69-5a9a-32d1-b1da-f78feeeca158 | -12.8411 | -62.6874 | 2024-09-26 03:16:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.1 |
| edc8f168-f2d3-31b1-8f1c-c9b6b5e47c27 | -14.8824 | -51.4992 | 2024-09-26 03:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 333e38b5-8110-35ba-8e17-42e2f4335e61 | -14.8957 | -58.0074 | 2024-09-26 03:16:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 6436de8a-0aad-3422-a873-39aa6fbcfea5 | -14.896 | -57.9873 | 2024-09-26 03:16:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 147.4 |
| efcfcccd-ddf2-337f-9cc8-544fbf68250f | -14.8963 | -57.9671 | 2024-09-26 03:16:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| a01f5707-50de-3877-acba-1b5e265669fe | -14.9153 | -57.9854 | 2024-09-26 03:16:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 179.8 |
| 1ea0f622-0e2c-3744-8bab-62c8b7df081a | -14.9156 | -57.9653 | 2024-09-26 03:16:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| e6286991-30a5-39ee-8e85-6a99e854f730 | -14.9348 | -57.9634 | 2024-09-26 03:16:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| ac8c0492-47b6-31ad-a5b3-32c8b1bd2877 | -14.9544 | -57.9413 | 2024-09-26 03:16:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 76212c07-29ec-3ad2-a863-aa059a5ee7e4 | -15.3371 | -58.1651 | 2024-09-26 03:16:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 073ab61b-c94e-3a22-91f4-1956bae258b8 | -16.098 | -52.0111 | 2024-09-26 03:16:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 3ce411ba-0efe-33cf-97d9-6b02586c34a3 | -16.0985 | -51.9896 | 2024-09-26 03:16:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 82.1 |
| b56c37dc-1aa8-34c4-8998-e5e1eba327ca | -16.1176 | -52.0082 | 2024-09-26 03:16:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 6c6b56ec-a211-3f9f-9bce-b0fbdce796cb | -16.118 | -51.9867 | 2024-09-26 03:16:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 4a26021c-8c08-3b3c-83e8-fd5706633aa9 | -20.4197 | -41.8798 | 2024-09-26 03:16:58 | GOES-16 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 98.1 |
| 4b075061-7066-3f05-8a41-1ccea7ebd357 | -20.4404 | -41.8737 | 2024-09-26 03:16:58 | GOES-16 | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | 93.5 |
| 073faa6c-b0ed-39ab-a490-bd920c0e92cf | -20.6074 | -51.5209 | 2024-09-26 03:17:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 205.6 |
| 63637d21-9c61-39d9-ac56-ef3608942093 | -20.608 | -51.4986 | 2024-09-26 03:17:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 188.4 |
| 441614c3-e0a7-3c32-a6e5-e782c328fde9 | -9.60871 | -40.61897 | 2024-09-26 03:17:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 67e08567-a493-3aaf-ba64-cf944e50f184 | -9.60782 | -40.62348 | 2024-09-26 03:17:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| f4563cac-5203-3a9f-867c-0fb50f0f793e | -9.60589 | -40.6182 | 2024-09-26 03:17:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 199f43c3-4776-3364-9cd3-4db9ebf84d4c | -9.60503 | -40.62272 | 2024-09-26 03:17:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 8beba293-908f-37e5-a70a-526383bc0f05 | -9.20707 | -40.25223 | 2024-09-26 03:17:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2ee3d185-a39f-3662-9a4f-1b1bacc329d0 | -9.16572 | -40.53486 | 2024-09-26 03:17:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4feb7a15-014c-3bd8-a325-6c3c41844c60 | -9.16488 | -40.53933 | 2024-09-26 03:17:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3005d407-c062-391f-b00e-960068a9dace | -8.67486 | -38.14417 | 2024-09-26 03:17:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 95ef7dcc-79d4-32a8-a989-8984f1b1b651 | -8.67308 | -38.14622 | 2024-09-26 03:17:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7ccd8154-f9c1-399a-8b55-b82088e5be5e | -7.80557 | -40.31941 | 2024-09-26 03:17:00 | NOAA-21 | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0887d231-5b7f-3772-93dd-4c181a3a536a | -7.59268 | -42.29196 | 2024-09-26 03:17:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| ae80cef9-eba7-3101-9cbc-bd0a33ae9969 | -7.59146 | -42.29822 | 2024-09-26 03:17:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| ccb1796e-5eea-3ce9-8c85-32054b5df5c4 | -7.5914 | -42.29149 | 2024-09-26 03:17:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 28.7 |
| 7db56137-5dac-3a81-af54-9d28db2be613 | -7.59023 | -42.29775 | 2024-09-26 03:17:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 29.7 |
| 5e3ca465-2e4b-3b0c-a7dd-627594454ae8 | -7.25049 | -39.85762 | 2024-09-26 03:17:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 7004a455-378e-361f-89a9-f89363488c06 | -7.24456 | -39.85657 | 2024-09-26 03:17:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 58fc5733-d847-3273-940e-37c2d1622a29 | -6.99801 | -35.21762 | 2024-09-26 03:17:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c674eba5-0003-3c58-89c1-3d826614719c | -6.95834 | -42.4737 | 2024-09-26 03:17:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 3413f34e-4203-32bf-a87b-a10ddd34f806 | -6.61668 | -39.58871 | 2024-09-26 03:17:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cc310e24-ef89-3432-a68c-485d14cf78c0 | -6.61152 | -39.58375 | 2024-09-26 03:17:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4380356e-e9c2-30b0-a652-eda4fc8f4274 | -6.61069 | -39.58828 | 2024-09-26 03:17:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |


[Clique aqui para ver as próximas entradas](README50.md)
