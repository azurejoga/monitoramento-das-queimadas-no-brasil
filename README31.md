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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23b23435-05ee-3726-b8c0-6cd74c962d83 | -9.086 | -61.1245 | 2024-09-26 01:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 5269b62e-1d60-38f4-a222-0ce959bb1178 | -9.1035 | -61.2769 | 2024-09-26 01:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 1feba59e-d1af-3ea4-afab-e7e5cf7f7763 | -9.1046 | -61.1237 | 2024-09-26 01:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 42d62e3c-1031-392c-9667-2181680f84ca | -9.1349 | -65.564 | 2024-09-26 01:05:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 1aa9a827-fb67-3d4d-806e-5fe8bfa3f5db | -9.135 | -65.5453 | 2024-09-26 01:05:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 0094b9ee-fc4f-3ca3-beef-e520bca9c595 | -9.3571 | -65.6315 | 2024-09-26 01:06:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 0125169d-d9be-315b-8ed4-6fd1b58ab28f | -9.5827 | -50.1584 | 2024-09-26 01:06:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 65b525eb-d4ef-3aee-85c9-44e418e9bb1e | -9.5829 | -50.137 | 2024-09-26 01:06:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 2755bd5e-58e7-397e-9ca3-2c04dd086109 | -9.6015 | -50.1566 | 2024-09-26 01:06:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 2ad94800-a71e-3efb-b401-92bdbc0ef87d | -9.6018 | -50.1352 | 2024-09-26 01:06:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| b9c1edc2-4274-3e41-b616-18eff119504b | -9.6149 | -57.7568 | 2024-09-26 01:06:01 | GOES-16 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 23.9 |
| ab81c23a-b67e-3de8-90ed-975e7af1c408 | -9.806 | -53.5664 | 2024-09-26 01:06:02 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 550f7cd7-7f88-396d-a6b0-e0319d1be408 | -9.8083 | -68.8152 | 2024-09-26 01:06:03 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 47.3 |
| b71c3961-d685-3e1e-96a4-36cd2070039d | -10.0692 | -68.5871 | 2024-09-26 01:06:04 | GOES-16 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 67c481cb-84f0-3aa1-845d-a0df3662fc60 | -10.3526 | -58.9068 | 2024-09-26 01:06:05 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 2d214069-b29a-3828-85c6-a449ff95b6e6 | -10.3713 | -58.9056 | 2024-09-26 01:06:05 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| e701e261-f0af-3829-a8d9-8c84735b1125 | -10.3882 | -67.8737 | 2024-09-26 01:06:06 | GOES-16 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 65681466-3f08-3c52-b12b-51ba12cc1278 | -10.8915 | -57.4521 | 2024-09-26 01:06:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| c9ad7026-c618-3ea9-b593-29366118cdb3 | -11.1354 | -46.1623 | 2024-09-26 01:06:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| c0614f79-a37f-324b-986a-fad0cb7bfdf3 | -11.2034 | -54.7752 | 2024-09-26 01:06:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 112.1 |
| f882ed14-252a-3a0a-85d5-5db322bfe62a | -11.2599 | -65.299 | 2024-09-26 01:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 662c5f15-dd0d-3ae2-9160-ce506cd4b2e4 | -11.26 | -65.2801 | 2024-09-26 01:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 18c7a5fa-92a1-36b7-ae89-6b77ae33fc40 | -11.2786 | -65.2982 | 2024-09-26 01:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 05038a80-582e-3e1f-8c90-cf3abbf76b06 | -11.2788 | -65.2793 | 2024-09-26 01:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 2a92f180-6abe-3953-b2f0-8a178ecdd486 | -11.955 | -60.363 | 2024-09-26 01:06:14 | GOES-16 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 71.2 |
| eb764349-14f6-37b8-91a2-1c516e2f1807 | -12.2175 | -45.5074 | 2024-09-26 01:06:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| f7dd798f-9e99-3cd1-b8dc-9f0e08b876e7 | -12.2367 | -45.5045 | 2024-09-26 01:06:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 79.8 |
| ebff84e1-01a4-3086-933d-807ec7fd231c | -12.5276 | -53.496 | 2024-09-26 01:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 0a1d2f87-aaf3-37e6-ab7d-1cedae4ef160 | -12.8219 | -62.7271 | 2024-09-26 01:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 39.2 |
| eec67cac-fc4e-3175-858b-7dafa2ef9b56 | -12.822 | -62.7078 | 2024-09-26 01:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 142.9 |
| cc10b833-78e9-352d-b9d9-f8191392ab27 | -12.8222 | -62.6886 | 2024-09-26 01:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.8 |
| c6d1e92f-d2b7-3680-869d-747d3b0bf2a4 | -12.8408 | -62.7259 | 2024-09-26 01:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 37e1f154-a237-3f94-adc7-9ee21d0c237d | -12.841 | -62.7067 | 2024-09-26 01:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 198.3 |
| 64fed4c0-8729-3163-9a8a-e2de1d165daa | -12.8411 | -62.6874 | 2024-09-26 01:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 4cd659cd-515e-34ca-ae31-81c767d08a4b | -13.1958 | -45.6539 | 2024-09-26 01:06:20 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 635581a8-878b-37a1-8517-3458e6e1f9e9 | -13.1963 | -45.6308 | 2024-09-26 01:06:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 8225b79a-3a29-377a-b219-d5aace1cacec | -13.7513 | -51.0736 | 2024-09-26 01:06:24 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 3b327c82-5825-3bff-869e-97fb55c415d9 | -14.4439 | -45.2555 | 2024-09-26 01:06:27 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 82c90335-b5e6-3943-9c90-edbffb4feb0b | -14.4444 | -45.2321 | 2024-09-26 01:06:27 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| c342f36f-b95f-36a6-b04d-84528cacf75a | -14.4634 | -45.252 | 2024-09-26 01:06:27 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 7794c74a-b690-34b1-adc0-a62a6daf609e | -14.4639 | -45.2286 | 2024-09-26 01:06:27 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 278.4 |
| 0e858528-529d-3a4f-8dd2-2d07b450221e | -14.4644 | -45.2052 | 2024-09-26 01:06:27 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 85649a3a-8158-3b26-b0ed-c768f02b8025 | -14.5705 | -45.6973 | 2024-09-26 01:06:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 7c1038ea-dacc-3b92-9886-7ce806b55782 | -14.863 | -51.5019 | 2024-09-26 01:06:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 0ee60481-5797-370f-bc43-9ee820cd5bc9 | -14.9156 | -57.9653 | 2024-09-26 01:06:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 7d307e51-10d0-3a9b-ac41-26d0970c0bbe | -14.9348 | -57.9634 | 2024-09-26 01:06:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 745ae121-3b84-3b9f-b595-9a2446f6abf3 | -14.9541 | -57.9615 | 2024-09-26 01:06:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 8fe91b52-e521-3e76-958d-d88cb0519f01 | -14.9544 | -57.9413 | 2024-09-26 01:06:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 61169947-ac19-3ebe-8105-beefa98293c6 | -14.9737 | -57.9394 | 2024-09-26 01:06:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 3c847de9-0067-320e-9369-2871b406901a | -16.8187 | -57.7854 | 2024-09-26 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.3 |
| f2221797-681a-3c5e-9a48-7d518087f26e | -16.7992 | -57.7876 | 2024-09-26 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 211.3 |
| 72d8c08b-c54b-3355-be9b-feee311b0ce5 | -16.7988 | -57.808 | 2024-09-26 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.7 |
| a01399a9-58e0-3da5-8bee-b097fac609da | -16.9925 | -57.9288 | 2024-09-26 01:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.9 |
| 8e47e113-bae7-3e57-a7a2-482850432b25 | -16.9732 | -57.9106 | 2024-09-26 01:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.0 |
| f39d76d0-9fcb-310c-b8bd-240535444e5b | -17.6538 | -40.234 | 2024-09-26 01:06:43 | GOES-16 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 176.6 |
| 41e62ba8-3b0d-39bc-bc6e-0f02f526d8d4 | -17.6545 | -40.208 | 2024-09-26 01:06:43 | GOES-16 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 98.1 |
| 0bce323e-00d2-3a3d-a9e6-0d0f997a05a5 | -19.929 | -43.7959 | 2024-09-26 01:06:56 | GOES-16 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 72.1 |
| c151b56d-d738-3ec8-b483-36c96c0c6c59 | -19.9298 | -43.7711 | 2024-09-26 01:06:56 | GOES-16 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 63.2 |
| 4398a51e-f760-3c61-948e-7c9340211b43 | -20.399 | -41.886 | 2024-09-26 01:06:58 | GOES-16 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.8 |
| 5294ff17-6bbb-3ba8-be18-03cca5555df4 | -20.3999 | -41.8602 | 2024-09-26 01:06:58 | GOES-16 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 62.1 |
| 30162a8c-c54f-364b-bc83-689cb19ba2dd | -20.4197 | -41.8798 | 2024-09-26 01:06:58 | GOES-16 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 95.1 |
| 2b67a662-4d40-3678-aaad-78e830d8edf5 | -20.4206 | -41.8541 | 2024-09-26 01:06:58 | GOES-16 | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | 85.1 |
| 79981257-a791-37f4-b3d3-0a03b3d853e9 | -20.5881 | -51.4802 | 2024-09-26 01:07:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.5 |
| 92f92f1e-8900-3b4a-a1f6-2e7c77b75555 | -20.608 | -51.4986 | 2024-09-26 01:07:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 184.2 |
| 68fff5cc-c3ba-3597-862f-64f3c3aae340 | -20.6086 | -51.4762 | 2024-09-26 01:07:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 105.9 |
| c348cf05-88e6-3d8e-9aed-81a4d77536c8 | -1.0369 | -53.3555 | 2024-09-26 01:15:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 4eb4bc43-60db-3b49-a78c-45b7ea743560 | -1.0553 | -53.3553 | 2024-09-26 01:15:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| f84a56b6-07fc-3121-bfd7-07f9c0e7260d | -2.6601 | -57.5507 | 2024-09-26 01:15:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 8db72254-c421-34cd-b308-a53c28f03455 | -2.6785 | -57.531 | 2024-09-26 01:15:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 86eb3dcd-7f27-3fcc-adb9-c943f2efeb32 | -2.6968 | -57.5307 | 2024-09-26 01:15:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| aea943d3-f29f-3726-a61a-25f3476e6da5 | -3.3158 | -53.2122 | 2024-09-26 01:15:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| f8abb3ef-2a09-387d-b7b7-5ec0a204f34c | -3.3505 | -53.7775 | 2024-09-26 01:15:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| e8c2259f-5b9b-39ca-8cab-a6726d175979 | -3.5488 | -50.38 | 2024-09-26 01:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| f5223cce-babd-3960-a4c1-c8cb5bb98d7d | -3.5673 | -50.3794 | 2024-09-26 01:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 569b4e9b-7194-324a-a2d4-3a430493a2ad | -3.7282 | -47.7266 | 2024-09-26 01:15:27 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 124.8 |
| 08b18385-a2f1-383f-8539-9e4ef1594969 | -3.8008 | -41.5989 | 2024-09-26 01:15:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 75.1 |
| 457b0fed-927a-37ec-888c-eea8e4263610 | -3.801 | -41.575 | 2024-09-26 01:15:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 56.7 |
| 34f1fd91-9609-3bff-836e-3245bc358bd2 | -3.9208 | -46.4459 | 2024-09-26 01:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 74.6 |
| fe0da4be-3164-395f-83fb-1512212a49f3 | -6.7839 | -59.3245 | 2024-09-26 01:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 0b8171b2-21ce-330e-b955-4b94f684d5b4 | -6.784 | -59.3052 | 2024-09-26 01:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 9ff4c363-b21a-32b2-a5e7-8975e0693ea6 | -6.8023 | -59.3237 | 2024-09-26 01:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| d3ceaafc-e07b-3f4a-b628-ddca9f6fdb2e | -6.8024 | -59.3044 | 2024-09-26 01:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 647ed918-6feb-306a-92d7-f6a95af30e26 | -6.9305 | -63.1241 | 2024-09-26 01:15:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 6b7b8a19-de06-3735-adbb-a7492aad8c48 | -6.9306 | -63.1053 | 2024-09-26 01:15:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| b691d6dc-a0d8-3273-bf95-28da435b9395 | -6.9489 | -63.1236 | 2024-09-26 01:15:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 35.2 |
| e01e30eb-4f55-355a-9943-db897b336810 | -6.949 | -63.1048 | 2024-09-26 01:15:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 62d798b6-c7b7-3441-ac9e-316ffa7d1ce5 | -7.2905 | -61.106 | 2024-09-26 01:15:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| d4124d5d-a9d8-38d2-a430-6b7bbc18097b | -7.2906 | -61.0869 | 2024-09-26 01:15:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| b96d3158-4fce-3147-a47f-71127a6fc68a | -7.5769 | -62.7828 | 2024-09-26 01:15:50 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 1cfc36db-1e65-3a0e-8eca-4a0fd36cc0d4 | -7.797 | -54.7263 | 2024-09-26 01:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 763f9334-63b4-38e1-b5c0-cc28caeca7e9 | -7.8154 | -54.7453 | 2024-09-26 01:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 1a41f548-70ca-3acf-be82-cc8b1e8acb5d | -7.8156 | -54.7252 | 2024-09-26 01:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 128.0 |
| af17498e-9fc8-3a87-8d75-163c6e5b3c89 | -8.1757 | -61.3946 | 2024-09-26 01:15:53 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| a4175c88-9913-312b-bf8b-8df2f46d8783 | -8.3153 | -55.0157 | 2024-09-26 01:15:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 1b0439aa-4200-34fd-b285-37e95d96aab8 | -8.3155 | -54.9956 | 2024-09-26 01:15:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 6e7844d9-9bd2-399a-85fa-1f663ac04452 | -8.5542 | -63.1814 | 2024-09-26 01:15:55 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 03b866a0-66de-3922-ad98-04fb61d81ef5 | -8.7087 | -54.7881 | 2024-09-26 01:15:56 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 385c169b-54f7-3edb-9860-1e4aa9e6f99c | -8.8098 | -58.2172 | 2024-09-26 01:15:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| d0a21ceb-ee95-3c86-bf75-5f03d4633eec | -9.0468 | -61.4325 | 2024-09-26 01:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 4c42b48e-1f70-3818-b7e2-9dbcf38dc4ef | -9.0657 | -61.3743 | 2024-09-26 01:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |


[Clique aqui para ver as próximas entradas](README32.md)
