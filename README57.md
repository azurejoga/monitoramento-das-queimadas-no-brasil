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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f16e219-ee09-3db6-baa3-f82b0de6aa63 | -3.5215 | -44.6689 | 2025-11-15 11:10:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 93.6 |
| d748ef1f-024c-3b5e-a1e4-8177ec898daa | -3.5215 | -44.6689 | 2025-11-15 11:20:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 87.6 |
| a2b850a6-d60d-3502-83f6-2196412d3ade | -3.6729 | -42.57157 | 2025-11-15 11:57:00 | TERRA_M-M | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| d3bde92e-2dd2-3d09-8f70-3415ce98c666 | -3.35938 | -41.85329 | 2025-11-15 11:57:00 | TERRA_M-M | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| a57aee57-655e-3bba-bbf2-a987416be0fe | -3.33034 | -42.18049 | 2025-11-15 11:57:00 | TERRA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 104.0 |
| 3f8da411-703b-3a1b-a0d2-c1ac2e27586b | -3.51466 | -41.61613 | 2025-11-15 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 30.0 |
| 581ec8c7-8627-337d-aaac-39bf4e399542 | -3.47789 | -45.65551 | 2025-11-15 11:57:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 2aaca592-f46e-37e6-9f20-20a857bb89cd | -3.40017 | -41.44216 | 2025-11-15 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 38.8 |
| 13404f04-3bd9-384d-80c1-3114947eb9c1 | -4.17078 | -39.1749 | 2025-11-15 11:57:00 | TERRA_M-M | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 19.3 |
| a4b75b62-072f-3243-a798-8e82f8b52fe6 | -7.10528 | -39.0818 | 2025-11-15 11:57:00 | TERRA_M-M | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 02ae95c5-77a1-3cf7-a37b-b33b103f5f60 | -5.71014 | -43.16927 | 2025-11-15 11:57:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 20.4 |
| f72692b1-0c2a-3c52-af67-e59ba388108c | -3.23688 | -41.93795 | 2025-11-15 11:57:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a0216ca8-0d28-3922-9fff-1fc1236f3d89 | -4.27583 | -46.84063 | 2025-11-15 11:57:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 2afb17fa-17a6-396c-b923-339eb4c250b9 | -3.26398 | -43.60922 | 2025-11-15 11:57:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7f72f737-fa33-3591-8060-33d769ba53c2 | -3.24901 | -43.38858 | 2025-11-15 11:57:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 2963cf3a-8997-3544-a2cd-baab9c43c6b2 | -6.78652 | -44.77641 | 2025-11-15 11:57:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 21ab2f45-2919-31f0-bd90-06551953099b | -7.27025 | -39.76615 | 2025-11-15 11:57:00 | TERRA_M-M | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 5eae1f5a-c036-3403-b95a-9acc86b6928f | -7.11091 | -42.72576 | 2025-11-15 11:57:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 29d9ce6d-14ea-3252-9104-344225dca436 | -3.29515 | -42.05057 | 2025-11-15 11:57:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| d25f2fee-3d1f-3a72-99ac-0a17d9406089 | -3.55265 | -42.12305 | 2025-11-15 11:57:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 87.1 |
| b896a7dd-35d5-3831-bb93-6461f22542dd | -4.43837 | -43.66149 | 2025-11-15 11:57:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 58be01e4-59dc-3117-b9ac-429434a743f6 | -6.18099 | -42.12873 | 2025-11-15 11:57:00 | TERRA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 3dc0c3a5-cbf7-3cd4-8def-85c9a503b98e | -3.52775 | -44.66137 | 2025-11-15 11:57:00 | TERRA_M-M | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 20.9 |
| c104e171-df3a-3749-a6a9-d735bb8429ae | -3.53288 | -44.66867 | 2025-11-15 11:57:00 | TERRA_M-M | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 6541129a-2330-3c71-a7ae-f95f0a03ed8b | -3.70429 | -42.60269 | 2025-11-15 11:57:00 | TERRA_M-M | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 20.3 |
| b803746b-eb89-3d7d-a314-044a9b4485e6 | -6.27998 | -41.76016 | 2025-11-15 11:57:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 01f6f698-aaa2-39f0-9860-d5747ea8546a | -7.3352 | -38.20411 | 2025-11-15 11:57:00 | TERRA_M-M | ITAPORANGA | PARAÍBA | Brasil | 2507002 | 25 | 33 | nan | nan | nan | Caatinga | 22.1 |
| bc0aaff4-a9d8-3f19-a879-cb696eec65c7 | -6.13739 | -44.10345 | 2025-11-15 11:57:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 254fd176-45b5-3749-8c64-a9ff3a74b843 | -7.83236 | -37.39125 | 2025-11-15 11:57:00 | TERRA_M-M | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 40.7 |
| 35b05c05-fc50-3e12-a600-6fb0221eb0b8 | -3.36084 | -42.17327 | 2025-11-15 11:57:00 | TERRA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 3f4691e0-31c9-3c97-bfe9-1146f120e64f | -4.32218 | -45.27762 | 2025-11-15 11:57:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| f37f4466-767d-3afd-ad10-bcac69e80cb2 | -3.99972 | -44.26272 | 2025-11-15 11:57:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 8c7dd69d-dd5a-37cc-a1b5-545fae2ed5f4 | -3.04298 | -40.84038 | 2025-11-15 11:57:00 | TERRA_M-M | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| dc229685-515a-348a-8f8a-b5600e086f47 | -5.53223 | -41.76562 | 2025-11-15 11:57:00 | TERRA_M-M | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| fc00952a-e23c-3998-b45f-a9b6c7fc7390 | -5.42092 | -43.25368 | 2025-11-15 11:57:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2300de47-5444-30eb-ad2c-09e6379a798e | -3.28067 | -45.45924 | 2025-11-15 11:57:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 0cbe2b7b-b6bd-3d6b-901c-ee645c32f1ee | -6.33724 | -38.5335 | 2025-11-15 11:57:00 | TERRA_M-M | VENHA-VER | RIO GRANDE DO NORTE | Brasil | 2414753 | 24 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 917d896a-0c46-3875-b42f-8ebfa34becd3 | -6.12845 | -44.10222 | 2025-11-15 11:57:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 647907b6-e40a-3690-bcf1-47e33cbd3176 | -3.08953 | -42.3218 | 2025-11-15 11:57:00 | TERRA_M-M | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| eea23fe5-3cd6-34b4-8a26-2bc92d0b2d7d | -3.09079 | -42.31306 | 2025-11-15 11:57:00 | TERRA_M-M | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 20a1b073-5863-3e0c-9108-a76dcf82f77b | -5.18795 | -44.28172 | 2025-11-15 11:57:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 90b64e1a-313c-3978-919a-a68385c00328 | -3.47797 | -45.64951 | 2025-11-15 11:57:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 2349ac52-4f64-3e88-83b2-e28087d0323d | -3.43048 | -42.45649 | 2025-11-15 11:57:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 597dbed2-57d6-3845-9010-989db5158636 | -6.08171 | -41.65836 | 2025-11-15 11:57:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| f16741f8-3d5c-3ace-9743-8085ad698e2e | -3.55973 | -45.08042 | 2025-11-15 11:57:00 | TERRA_M-M | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 07bde2ce-444c-3398-9ac5-187073c96152 | -3.75202 | -42.45773 | 2025-11-15 11:57:00 | TERRA_M-M | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 10442f7b-ac28-3cf3-b8c0-48a14b9158c1 | -3.435 | -42.09424 | 2025-11-15 11:57:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| c94c7fa1-d021-38b1-841f-9211f6618990 | -5.23418 | -44.3454 | 2025-11-15 11:57:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| d839bdb8-899d-3b5f-90e0-d73f26408531 | -5.51596 | -43.87021 | 2025-11-15 11:57:00 | TERRA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e559be59-b6af-3de9-9074-061a56d56430 | -3.50035 | -45.01856 | 2025-11-15 11:57:00 | TERRA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2ec376f6-40d2-388f-8036-8d15642ad896 | -7.65092 | -37.70436 | 2025-11-15 11:57:00 | TERRA_M-M | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 21.4 |
| c257d80d-11fd-3cdb-a164-cd9097204b6d | -3.24772 | -43.39756 | 2025-11-15 11:57:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4bcdd377-2587-38e3-bd18-37be3ca51b92 | -3.70408 | -41.6456 | 2025-11-15 11:57:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 7bfa2798-3ce5-3ea3-8e57-d03d33ccaad1 | -7.10082 | -42.73341 | 2025-11-15 11:57:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 000afdfe-b8c8-3fdd-aca6-7852084c3f03 | -4.16759 | -43.04469 | 2025-11-15 11:57:00 | TERRA_M-M | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 83ab173c-70dd-3d83-9a89-83d09809edc8 | -3.54763 | -42.1581 | 2025-11-15 11:57:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 21.0 |
| c9bfe36a-9dfe-3841-8f4d-67126074c258 | -3.67285 | -45.03427 | 2025-11-15 11:57:00 | TERRA_M-M | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5d9d31ea-c441-30b6-a06d-fdceaea1e274 | -3.46309 | -42.0415 | 2025-11-15 11:57:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 40ead782-a8fc-3816-9158-fd9fde850abf | -3.342 | -42.17958 | 2025-11-15 11:57:00 | TERRA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 754b5bd3-58d5-3973-9854-d1d9e85ed5b3 | -7.74497 | -38.82973 | 2025-11-15 11:57:00 | TERRA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 13.5 |
| a528a0fc-519f-3623-abb0-6f6f02473e9c | -6.14458 | -48.05046 | 2025-11-15 11:57:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 862.5 |
| 113ae6c7-f530-3ac2-a9b1-695d43433edf | -3.69677 | -42.34303 | 2025-11-15 11:57:00 | TERRA_M-M | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 5b62ecf9-bfb0-37a2-b6fc-e45b64473e2d | -6.9416 | -37.79885 | 2025-11-15 11:57:00 | TERRA_M-M | CAJAZEIRINHAS | PARAÍBA | Brasil | 2503753 | 25 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 1758713e-c23e-38d4-aa81-9f07164886b3 | -3.63109 | -42.47011 | 2025-11-15 11:57:00 | TERRA_M-M | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 7191ced5-1e49-37f7-a0cd-db64bcc9000a | -4.36871 | -45.52089 | 2025-11-15 11:57:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 85.3 |
| c7344f48-b1a2-302b-871c-ae2151d5a617 | -7.82004 | -37.38962 | 2025-11-15 11:57:00 | TERRA_M-M | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 19.1 |
| fb8b0a3b-4272-32e5-9ffd-615d0c29c2af | -4.54732 | -43.22174 | 2025-11-15 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 6eb1c5bc-7487-3667-846a-c36c5dfaad5b | -6.78021 | -44.75615 | 2025-11-15 11:57:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| c45a7926-a063-3311-904a-8765e5b9842a | -3.4709 | -40.22752 | 2025-11-15 11:57:00 | TERRA_M-M | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 15.0 |
| bf00907c-a48e-35f0-a82a-fb69f65afcdb | -6.63558 | -38.46458 | 2025-11-15 11:57:00 | TERRA_M-M | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 4ec2be75-2a6d-3a3c-b756-9223092f2371 | -3.07362 | -45.18645 | 2025-11-15 11:57:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 642333e3-68de-33cf-89c8-dac963965dd4 | -3.35811 | -41.8621 | 2025-11-15 11:57:00 | TERRA_M-M | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| e5521f97-ec01-36f4-ac28-bfd1a58c2ce2 | -7.09806 | -40.72083 | 2025-11-15 11:57:00 | TERRA_M-M | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| bfa0842f-e4ae-37f8-9c3f-1f80a95d66c6 | -6.89174 | -42.06514 | 2025-11-15 11:57:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 43cf33cc-8187-3763-852a-861e0e9e4527 | -3.6713 | -45.04468 | 2025-11-15 11:57:00 | TERRA_M-M | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| faa45280-6866-3577-ac72-30d92d92b6a4 | -4.56998 | -38.67125 | 2025-11-15 11:57:00 | TERRA_M-M | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 11.0 |
| af16acf2-a9a8-362c-9147-5c4ca3cc4824 | -3.52785 | -45.45626 | 2025-11-15 11:57:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 38.8 |
| e39f32f3-cb95-3b8b-be55-1fea62163d12 | -3.32068 | -42.39064 | 2025-11-15 11:57:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 49827fb8-3c13-3d78-9284-e7f0f02696db | -7.63611 | -37.76655 | 2025-11-15 11:57:00 | TERRA_M-M | TAVARES | PARAÍBA | Brasil | 2516607 | 25 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 80b5001d-35e3-303a-8f8b-9dda9c48008d | -6.34103 | -38.52573 | 2025-11-15 11:57:00 | TERRA_M-M | VENHA-VER | RIO GRANDE DO NORTE | Brasil | 2414753 | 24 | 33 | nan | nan | nan | Caatinga | 30.9 |
| f4f4dfd9-9f32-322d-bed3-b4584f8125fe | -6.41833 | -43.81552 | 2025-11-15 11:57:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e2d3381b-c8e2-3ba3-b547-64b3528bb5ee | -5.23282 | -44.35477 | 2025-11-15 11:57:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 4531cd17-faf4-3bb6-a12a-36aee3c49ada | -4.39634 | -44.07533 | 2025-11-15 11:57:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 88fbb464-7ab8-3402-a236-a051080328b1 | -4.14518 | -38.77135 | 2025-11-15 11:57:00 | TERRA_M-M | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 36.5 |
| 074af9cc-b1bb-3a26-b2f2-a7eb7c2ebc65 | -3.61477 | -42.33407 | 2025-11-15 11:57:00 | TERRA_M-M | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 52b17591-0831-3cb9-be4b-8bdf0e52a8bc | -3.36834 | -41.60166 | 2025-11-15 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| f09bb6b9-8266-3342-a143-b710d79f027c | -4.53976 | -43.21166 | 2025-11-15 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 4e7848b7-50ee-33e4-b55f-72d3dcc64475 | -3.58213 | -42.43656 | 2025-11-15 11:57:00 | TERRA_M-M | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| d5f541a1-1f5b-3bda-a94c-3c349d7f4ba0 | -3.68171 | -42.44796 | 2025-11-15 11:57:00 | TERRA_M-M | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 460945d0-b5d1-361a-a1bc-190d5858cf99 | -3.66501 | -42.35888 | 2025-11-15 11:57:00 | TERRA_M-M | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 1041407b-8a9c-3c03-8c68-ed4525e91eb6 | -5.02179 | -45.34169 | 2025-11-15 11:57:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 05db647c-7a29-39bb-8283-7280b8039618 | -7.37635 | -37.51095 | 2025-11-15 11:57:00 | TERRA_M-M | IMACULADA | PARAÍBA | Brasil | 2506707 | 25 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 0747237f-296f-3f19-95fc-1f882d288ae4 | -3.46686 | -42.01516 | 2025-11-15 11:57:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 405c3337-6803-32ea-b342-5312b59bdb6d | -5.03683 | -39.71497 | 2025-11-15 11:57:00 | TERRA_M-M | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 25.0 |
| d6f00b24-eda1-3603-b327-f02842622ab8 | -6.04705 | -38.47655 | 2025-11-15 11:57:00 | TERRA_M-M | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 25.7 |
| 1deeedd4-3cfe-3f08-bcb4-63c3fbdeb045 | -3.52631 | -44.6714 | 2025-11-15 11:57:00 | TERRA_M-M | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 6e75c2f4-d764-3169-a738-72f60136e1cc | -4.13177 | -43.29219 | 2025-11-15 11:57:00 | TERRA_M-M | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 54b6e938-e866-3068-ac04-4aeb2d8ede34 | -3.32444 | -42.30203 | 2025-11-15 11:57:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 016c1f1a-c062-359b-b107-cad53a95ae87 | -6.41235 | -41.47274 | 2025-11-15 11:57:00 | TERRA_M-M | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 2806a7d0-2bde-326c-8383-a17dd45ffa89 | -4.85786 | -43.25433 | 2025-11-15 11:57:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |


[Clique aqui para ver as próximas entradas](README58.md)
