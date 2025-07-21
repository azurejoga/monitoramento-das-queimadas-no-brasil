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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5bfde0c6-3b4e-371b-a591-6a3d4a189b1f | -10.1357 | -49.6538 | 2025-07-21 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| d1261c2b-ccfb-3272-b87b-1e20f440b9da | -6.7194 | -44.3231 | 2025-07-21 13:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 115.0 |
| ee1dd794-581c-373d-a884-0f1eff7b8949 | -7.2771 | -60.1889 | 2025-07-21 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 85011c16-378c-3f3e-8cd5-73b4960f8c9f | -8.9405 | -44.4457 | 2025-07-21 13:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| cc91f8ba-0b96-3e46-ae16-0a6e706ac573 | -7.5622 | -44.5678 | 2025-07-21 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 0e055645-d3e7-39f6-8cf5-bea9e349cd85 | -7.2771 | -60.1889 | 2025-07-21 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| f786c5e9-bb98-3d07-8748-dba4ce402375 | -10.1357 | -49.6538 | 2025-07-21 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| b576b937-a588-3ea6-b7d1-45e16809a7d2 | -6.7192 | -44.3461 | 2025-07-21 13:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 41a96b7a-d3cf-3208-8efd-df754aeea8bf | -6.7053 | -45.7117 | 2025-07-21 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 6cc13d13-4861-3ec7-b09f-8923bc2c003a | -6.7194 | -44.3231 | 2025-07-21 13:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 5f1a67d1-bdbe-372a-b427-71d1110d4789 | -13.8875 | -44.0177 | 2025-07-21 13:50:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 4f7d848e-f32a-324f-8b14-d7cf2e60e780 | -6.9801 | -42.809 | 2025-07-21 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 124.1 |
| 257444b2-de66-348a-aa67-d0a222b573ca | -8.9405 | -44.4457 | 2025-07-21 13:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 051a290c-a312-3788-add9-6a27919a2978 | -7.2772 | -60.1698 | 2025-07-21 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 161.8 |
| 635606a9-a20b-3299-b90a-1a52541d3fc4 | -7.2957 | -60.169 | 2025-07-21 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 6390b5cd-f154-386f-acdf-42a7ced9a3d1 | -6.1937 | -44.3896 | 2025-07-21 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 566a7fa8-a2f1-37b3-810f-ad4c933dabb2 | -7.9648 | -43.9738 | 2025-07-21 13:50:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 92.2 |
| c8415d6d-3c1d-3fe1-9478-ff5f449ecd17 | -7.2644 | -44.2972 | 2025-07-21 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 46256c18-d26a-3526-951a-cd46e1799f97 | -7.2402 | -60.1904 | 2025-07-21 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 14302cee-2185-34e0-91e1-c3dd1fbdb8f3 | -6.7194 | -44.3231 | 2025-07-21 14:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 0a8080ad-5448-3f8c-bd3a-cba38730e3ea | -7.2402 | -60.1904 | 2025-07-21 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 580118da-d8e0-3f31-9b31-80cf436f47b2 | -6.4656 | -45.3249 | 2025-07-21 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 3f21e692-a8d8-3e45-9434-d809808a5f2c | -9.4031 | -47.9707 | 2025-07-21 14:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| be4af973-af02-3264-80fa-b890f1eec3bc | -7.2772 | -60.1698 | 2025-07-21 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 154.8 |
| e71fe66d-30c6-36a5-a82b-5b9dda7c8bf2 | -7.9648 | -43.9738 | 2025-07-21 14:00:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 21c6ccd9-6404-3307-84fc-70c3bca8a354 | -7.2957 | -60.169 | 2025-07-21 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| cb7b40f5-9b58-3b0c-9422-23c73cd377a7 | -6.8958 | -45.4026 | 2025-07-21 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 142b4760-7325-3c22-b8af-9a88aee16f6a | -11.6079 | -44.2321 | 2025-07-21 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 132.4 |
| bb72c0d1-1412-32a4-9879-2a5f44e2c804 | -6.3777 | -44.7411 | 2025-07-21 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| a4fccd25-5903-3745-be98-dff1cd3ad731 | -13.8875 | -44.0177 | 2025-07-21 14:00:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 055e8b95-ad2b-375d-bbe0-9bf45b2a251c | -7.5622 | -44.5678 | 2025-07-21 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 78ca5765-2639-39e4-bf07-c7798e2fee7d | -11.6271 | -44.2292 | 2025-07-21 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 5d12bd83-c4ee-379c-9845-fb3b7b3a2199 | -10.1357 | -49.6538 | 2025-07-21 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| c10ea02a-cdbb-36bf-b934-bbb00a5ee5df | -7.2771 | -60.1889 | 2025-07-21 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 956b0f33-d9d6-3ca2-9b52-faa189e2d498 | -6.1937 | -44.3896 | 2025-07-21 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 140.5 |
| f23795f9-f70f-3079-b30a-d9f78918b786 | -7.2644 | -44.2972 | 2025-07-21 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| aca6e0f9-1e52-326a-9c1b-5fd9b436c088 | -7.2771 | -60.1889 | 2025-07-21 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| fe5c07bc-1a61-3cb5-bb66-607e074f0628 | -6.7053 | -45.7117 | 2025-07-21 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 6086bd0b-0727-3596-8535-6f34b58d0ff5 | -8.9405 | -44.4457 | 2025-07-21 14:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| b2f0cbea-f2eb-35a6-8db3-572352e93889 | -7.2402 | -60.1904 | 2025-07-21 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 0f5d79ee-9224-38cd-98a4-d56843fc2030 | -6.7194 | -44.3231 | 2025-07-21 14:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 38996857-70f6-378d-9801-81d9949ca7ce | -7.9648 | -43.9738 | 2025-07-21 14:10:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| c3801b87-3b4e-3de4-8192-1cc4f56a7719 | -7.5624 | -44.5449 | 2025-07-21 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.1 |
| c846aaa9-351b-33e2-a8dd-bb505af5559a | -11.6079 | -44.2321 | 2025-07-21 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 176.4 |
| a7fa64b5-1fc6-356e-bfdc-860d2384b1b6 | -7.2957 | -60.169 | 2025-07-21 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| c799be86-2a85-377a-aeac-9e9a30b6d01f | -7.2772 | -60.1698 | 2025-07-21 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 164.3 |
| 2f2c8014-ff57-3cc5-9485-9bb2840f468b | -6.1937 | -44.3896 | 2025-07-21 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 7f56ce48-9dc9-3f2c-aebf-ca80bb280d25 | -6.3777 | -44.7411 | 2025-07-21 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 57549b9b-489c-39ee-904a-5486e3548788 | -8.9405 | -44.4457 | 2025-07-21 14:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| f98704fd-d787-3faf-bbe7-2fbebebee7f3 | -6.7194 | -44.3231 | 2025-07-21 14:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 984bfc6e-c551-300b-bda9-9c787f36e94d | -13.8875 | -44.0177 | 2025-07-21 14:20:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| c3a34da8-0d38-3258-930a-754be182dce0 | -6.2124 | -44.3881 | 2025-07-21 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 5735de69-2dcd-3c26-a2ee-7274fbefe82d | -6.1937 | -44.3896 | 2025-07-21 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 185.5 |
| 77a711dd-009d-3349-8512-c0351986deb2 | -9.4031 | -47.9707 | 2025-07-21 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| cf98f5fd-73d3-3df0-8694-1f04de2c3e48 | -11.6079 | -44.2321 | 2025-07-21 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 0914aaac-d60f-391d-94f5-8ad85e3857fb | -6.7053 | -45.7117 | 2025-07-21 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 7e3d9012-9717-3f40-9cdf-e326485864ec | -10.0703 | -59.1001 | 2025-07-21 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| d7be6cac-358e-3106-a7a7-0e5a35c86b57 | -10.0516 | -59.1013 | 2025-07-21 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 158.5 |
| c2be6fd0-f418-3c15-8a92-9bd5d7df1f0f | -7.9648 | -43.9738 | 2025-07-21 14:20:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| e9ff525c-4992-3e71-8549-87d41ea7d99d | -6.3777 | -44.7411 | 2025-07-21 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 52d96c2a-e4d7-3a92-8277-0d84850d1b01 | -7.5622 | -44.5678 | 2025-07-21 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 07ea68e4-94f4-3cee-a4a9-4337166507b5 | -8.9405 | -44.4457 | 2025-07-21 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 86.9 |
| bc38140b-0a6f-3ad7-9251-e7c140a991a5 | -10.9035 | -50.1948 | 2025-07-21 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 33f7e713-c1b0-32f2-bb0e-9fde46387682 | -6.896 | -45.38 | 2025-07-21 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 85c4c179-4483-386b-bda4-e37ddb7522fa | -7.2646 | -44.2741 | 2025-07-21 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 6c88ac43-ece7-38e0-b015-64cb6443aa17 | -6.1937 | -44.3896 | 2025-07-21 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 4c855ad9-6663-396e-90fc-19413a37b8aa | -6.2124 | -44.3881 | 2025-07-21 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 1f853b8e-7866-33d2-b929-50d248d06515 | -6.7053 | -45.7117 | 2025-07-21 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 221.2 |
| 02c71dc7-976d-32df-bf20-c6f8596dc405 | -10.0516 | -59.1013 | 2025-07-21 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 195.6 |
| 2fc85615-58dd-3922-abb5-4a239468e396 | -7.9648 | -43.9738 | 2025-07-21 14:30:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 82.1 |
| c43bd868-04ed-34ea-8834-90bc22e9150e | -13.4883 | -45.5137 | 2025-07-21 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| a10c8436-ce6a-3909-99fc-fca75e96fcd3 | -11.6079 | -44.2321 | 2025-07-21 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 144.2 |
| d01032ce-d539-3504-b878-59df410fd685 | -6.3777 | -44.7411 | 2025-07-21 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| a19e2aa5-c35b-3386-9e5e-48a0664ab09d | -10.0703 | -59.1001 | 2025-07-21 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| f1a704fa-96ca-30d9-86fb-c672eecea09d | -7.5624 | -44.5449 | 2025-07-21 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.0 |
| ecd862f8-d39a-3d73-93a7-10abc1f30c37 | -6.6865 | -45.7132 | 2025-07-21 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| cced5a80-7409-39be-b3d2-432902c0f07f | -10.0329 | -59.1024 | 2025-07-21 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 5540bd23-86ec-314f-90e9-c45ee99291d2 | -10.0516 | -59.1013 | 2025-07-21 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 306.7 |
| 3909f7f2-1e60-3ec2-8e77-7b8e20e5e5be | -6.6865 | -45.7132 | 2025-07-21 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 92c58efd-281c-3f19-a15d-e344a6419f32 | -11.6079 | -44.2321 | 2025-07-21 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 224.8 |
| a6277842-b0af-3c69-9278-5eb9af18be69 | -6.1937 | -44.3896 | 2025-07-21 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 0f56d395-cf28-31ca-9fc5-854ab6e3bbcc | -6.896 | -45.38 | 2025-07-21 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 1c2959ef-e53d-3ee7-8784-714f74666b5f | -7.9648 | -43.9738 | 2025-07-21 14:40:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 1dce8cf2-0b9b-3a3b-b7ef-752b582684c0 | -7.2644 | -44.2972 | 2025-07-21 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| a1ea3d8a-1781-3dba-9659-e936223c22cb | -6.3777 | -44.7411 | 2025-07-21 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| ab181664-f681-34a7-b19e-d1456104b203 | -6.2124 | -44.3881 | 2025-07-21 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 057a7a9a-bb49-30ed-8fb9-b00b684aae23 | -8.9405 | -44.4457 | 2025-07-21 14:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 33d2236c-3d28-38cb-9e21-d4bdc0420b58 | -10.0703 | -59.1001 | 2025-07-21 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 100.3 |
| acff5729-b535-37b6-a4b7-6b62ecb4ebaf | -6.7053 | -45.7117 | 2025-07-21 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 245.2 |


