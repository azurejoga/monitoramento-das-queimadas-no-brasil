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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92b585b5-3402-3ee8-8f64-aea8e81c3e66 | -7.12802 | -60.12691 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6bff6dbe-8341-37f3-91ce-2a70b6d32b5b | -6.54144 | -56.19635 | 2025-08-15 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4b40966-0d8d-3c3b-a027-ea83129b4171 | -7.87955 | -61.82962 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbc14325-58bd-36c8-bcd5-24caf8e26be1 | -6.99762 | -59.98842 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 82a4db25-85cd-3a1f-be7c-4480efcf646d | -7.59742 | -63.52829 | 2025-08-15 04:51:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 543f5b9b-e8db-3aea-b383-05c0f1b6d191 | -6.10895 | -59.98394 | 2025-08-15 04:51:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c982089-cc9f-30f1-8021-3f8596c1cac6 | -7.03501 | -59.85131 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19045aa4-a1c5-3125-a5e4-70f2425eda5a | -7.341 | -60.62806 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a74d3402-16bc-322a-bad7-78343abb096a | -13.11076 | -57.16481 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8aad4b4b-6185-319a-9661-1b88c8a3ff71 | -13.4771 | -56.66835 | 2025-08-15 04:51:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 07eeae3a-799a-3164-bd39-6035206d581d | -6.91782 | -59.15078 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82cd1b87-1310-3473-beda-e0c5aab8719b | -6.90611 | -59.14001 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db47b7d1-d455-34d9-872a-f656e1271c12 | -9.85391 | -47.82341 | 2025-08-15 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff934b61-4304-39ea-a020-27002c74d141 | -14.27945 | -53.01922 | 2025-08-15 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d68d1a96-7f91-3ace-93fa-7d613effa100 | -9.14416 | -59.41861 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2132bf9-a4b8-38f2-a3f2-f4b93e0fb54f | -9.15276 | -59.42015 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82fd287e-134f-36dc-94d0-0faa964e21ac | -9.18544 | -59.65237 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d9257252-f3d4-3579-b790-6707b0437416 | -8.52245 | -43.29087 | 2025-08-15 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 006142af-9b1c-309a-aaba-02d9c4190609 | -6.53412 | -56.19514 | 2025-08-15 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e9ec4e5-a5b4-3d56-bc9e-1ae8abf5cd83 | -11.35758 | -55.43091 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ab8416e4-3054-372a-8029-b1b389de1279 | -6.70173 | -58.85628 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2a12527-41f9-3cdc-a1eb-8901b2865e84 | -6.92891 | -59.53498 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d262976b-c04b-3a85-8f93-e0a217f643e8 | -6.90832 | -59.15359 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ae032a0-b5bf-36c5-a9cb-ef024804a4a6 | -8.66993 | -62.45082 | 2025-08-15 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| acdfee9f-8a54-3233-8201-923540685568 | -7.95701 | -61.76187 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be70001e-db57-3158-a39a-046d307fb469 | -6.66046 | -58.82547 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 72d08afa-5742-3d27-be1b-9cb3f2bebf0a | -8.55238 | -63.92191 | 2025-08-15 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df244d16-eb3e-3a20-9fe4-3b0a10361bcc | -7.11641 | -59.62388 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66bbaa76-c8b3-3651-843c-e2208fe4c6e9 | -7.52835 | -61.33587 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9cca8c63-587c-36a0-86fb-1e12de49a5f3 | -9.15698 | -59.66062 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a972976-6962-3269-adcd-ed48bc0972e8 | -6.51369 | -56.20508 | 2025-08-15 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21e7ae5a-1db9-3f5a-94e9-fb82e306fd0c | -14.07257 | -46.31887 | 2025-08-15 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3a59c55-ddf3-34bd-b9be-1e6e95589d15 | -7.85634 | -48.23422 | 2025-08-15 04:51:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1af8668e-3a83-3634-a195-54e327cc3534 | -10.01279 | -58.42529 | 2025-08-15 04:51:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a9cbca38-344b-33ab-a795-6b66f038f261 | -9.1803 | -59.65601 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7a7d4227-5799-3cac-8f35-4abcc02587a9 | -10.34957 | -64.45338 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b7346d7-3d28-335a-9f57-7be873755574 | -10.33278 | -64.44576 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94f5e5cc-cf2f-300a-8fab-11eeb8c01b07 | -7.87604 | -61.82725 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f7a36fb-fcc9-3108-ab49-aeda7467f179 | -11.35082 | -55.42976 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| df036e9c-a778-3070-a3f6-61d4711cc9b0 | -8.91704 | -60.72687 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a0afcc7-63fa-3364-bd1d-aba8b41ff1c8 | -10.05167 | -59.11568 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f22c5d44-2dd6-3112-bdd2-d86cae334057 | -6.92293 | -59.1472 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 760ef5b6-f1f9-3408-ba0e-ff8e93085c67 | -6.48444 | -62.94452 | 2025-08-15 04:51:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ea38022-e97d-3637-8116-aa0942ba71f8 | -11.34524 | -55.42127 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b534b36c-6149-3a56-8adb-9a1aa2262acc | -9.83876 | -47.80926 | 2025-08-15 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f891ac64-634c-31c6-9c03-e197f4fa7dc4 | -14.73587 | -46.29907 | 2025-08-15 04:51:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37d37753-ac37-3707-877a-86009af61aa0 | -6.64617 | -59.0759 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a835796-b646-3034-8e3f-e150a3df7b26 | -6.93944 | -59.52749 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f9070cea-7bf2-3b1b-b04f-9d77b129d0f7 | -9.84918 | -47.82664 | 2025-08-15 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29140ef9-86a6-3f7a-a7cb-b450c8722bd7 | -7.5499 | -63.49398 | 2025-08-15 04:51:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e88f3eb5-fb25-3ea8-b503-db967d229ea6 | -7.52166 | -61.3745 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6898bd69-f485-347a-bd17-5f90e39cd08b | -10.16485 | -59.66239 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4fea475-9237-35e9-a400-2e55164f7c2d | -6.47825 | -62.93662 | 2025-08-15 04:51:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8255ccc7-a11b-33d9-9171-bf7df9e7dc14 | -11.2081 | -55.91708 | 2025-08-15 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 695abf1d-d14b-39f9-9d99-1c15a09096b6 | -11.93279 | -63.24379 | 2025-08-15 04:51:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5cee08e-4c76-338e-88fa-b7efd9261415 | -13.11709 | -57.14887 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 178195b8-12b5-33ec-8e2d-7460a0a0df99 | -9.74334 | -48.57567 | 2025-08-15 04:51:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d62b1f4b-b0e6-3afb-bd95-8c2b764934eb | -7.44893 | -49.24575 | 2025-08-15 04:51:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1c9342a-1f1d-3b78-bf42-635166dd314c | -9.17446 | -59.66368 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 339ce2cd-3240-37c7-9880-b67499fec7b2 | -9.50639 | -60.53075 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 4743b9ce-845a-3e31-8085-8d1449e285da | -7.81203 | -61.331 | 2025-08-15 04:51:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72ab2571-4afe-3da6-b567-4fdbdcab9a18 | -7.87831 | -61.81483 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bd0e656-4804-341f-a582-3bba455c42c5 | -9.34605 | -62.5887 | 2025-08-15 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 77b07d1a-01d0-34d6-bfc6-d8b53c4b32e1 | -11.31502 | -55.20213 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c5b934c-bb67-363b-a052-3c8f72782a5b | -6.88571 | -59.1539 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b49ad739-6b88-30e3-84bc-a39da5f5f741 | -6.64392 | -58.81849 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2487efa9-0095-36a6-a44f-c5f79087e7e4 | -11.35261 | -55.41871 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 36ebe2ed-7808-3520-b140-19ea7134deb3 | -13.32157 | -45.22833 | 2025-08-15 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce3e7628-754f-30f4-a240-90c091d47be0 | -9.78654 | -61.50214 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 788ee349-9c0c-3241-8743-15d19584b633 | -8.91615 | -60.73196 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2bf6c8a-5aeb-38cb-a424-f6e79273e62b | -7.5283 | -61.3317 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4931f23c-b774-3aee-877c-4e2a2432612e | -6.47756 | -62.94056 | 2025-08-15 04:51:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fda964a3-fb94-3eb4-91ec-2bd20a9add15 | -10.46945 | -61.327 | 2025-08-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d24aa585-33fc-3f00-b0b5-b57339a3c322 | -10.3588 | -67.71356 | 2025-08-15 04:51:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 388e7cd3-5273-3bdd-97fb-02d3bcbb0b1c | -13.48187 | -56.6612 | 2025-08-15 04:51:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c046436d-fbc5-32c6-bca8-08320109246b | -10.0114 | -59.22369 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4433721b-f19f-3019-9d71-ac3cdddc0c7e | -6.93494 | -59.52676 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d34b4b84-e702-3ec2-9572-9f928ec53984 | -9.16044 | -59.69214 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| febdec12-fd86-36b9-9558-cf2c5f32b4ef | -9.94016 | -60.50758 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d734346-8803-3bec-8b6e-a788186d3ec2 | -8.51187 | -43.32814 | 2025-08-15 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5f8f4050-6f39-3d92-8ede-e82df940e4d7 | -7.86106 | -48.22972 | 2025-08-15 04:51:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d226cdf5-170c-3954-863c-937038524dd2 | -13.32765 | -45.22241 | 2025-08-15 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e6a0646-211a-3eb1-b450-6bb5241c4339 | -7.93187 | -61.75408 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf7caeb9-ea87-3e78-ab08-722ab91d16f9 | -8.56168 | -63.91113 | 2025-08-15 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f77d519f-1913-38de-a78a-fa7cddecc13c | -7.58571 | -63.46224 | 2025-08-15 04:51:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2652203-1de7-3898-9c2d-1cd5a4616840 | -6.07829 | -59.9371 | 2025-08-15 04:51:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b66a6ce4-9a50-3b96-82be-a341e255ca55 | -6.95083 | -60.12221 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 71ea5df5-1e64-31cb-8f08-a431ab93999f | -12.68282 | -44.95611 | 2025-08-15 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f05672b2-fbf4-3b9e-8039-b4bb077135f1 | -12.78824 | -45.9554 | 2025-08-15 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d1e9ea49-8ba7-375d-b12f-22b94e5ca283 | -7.87428 | -61.80769 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3138f9f0-f974-3d7b-b001-1363839f3517 | -5.89615 | -57.74645 | 2025-08-15 04:51:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d55db569-20b8-397e-a774-b7f6bd88b0c5 | -8.29304 | -45.00927 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb21e5ab-8680-38d2-922c-bf26fbf0a06b | -8.84713 | -48.51841 | 2025-08-15 04:51:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6820cc7-96d9-39f5-abf8-a025e01e4fb1 | -14.73578 | -46.29811 | 2025-08-15 04:51:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f60cfcd-7c62-3cb7-b8b8-8a82dd613d8c | -7.86513 | -61.82058 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3e524d1-6f27-3b76-8925-a2857cb2b8a1 | -7.07143 | -59.2037 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e4993fb-83bc-3d84-b63c-9a1ccef2adc8 | -10.01208 | -59.2198 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cbeec2a-0168-34c4-9261-1486d62c706b | -9.50748 | -60.53013 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d5f84cd-0923-376c-a558-ef8447e00a67 | -6.9363 | -59.82238 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 69a57981-6f78-3017-ae41-8876c75bfe08 | -7.52383 | -61.33203 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README46.md)
