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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdafafbe-2bbc-3351-ac32-bd1430e68fc9 | -3.00126 | -54.76738 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| aad6f510-c951-31f5-bd02-9fd4838ac5f9 | 0.9891 | -50.02775 | 2026-10-09 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41670fc0-3215-3c02-8d0d-a65a25e06fa5 | -3.28835 | -42.28067 | 2026-10-09 04:25:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c4a9783-7a85-305d-943a-cf6074b9359e | -3.16866 | -50.44516 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91e095cc-51a0-314f-a61b-8d581f9fb827 | -3.25178 | -54.04504 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eb3e443b-0dbd-3800-b05d-90dc258ed30d | -4.15294 | -44.34374 | 2026-10-09 04:25:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 818618db-e63c-3fb7-8e67-5f42bad0f3b6 | -3.01132 | -54.03936 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 001de8e1-9a59-3354-9d96-f5fcbf7ee2d2 | -1.15 | -54.21918 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f8eeed57-2c2e-3109-8445-7d65541b9533 | -3.19544 | -42.96524 | 2026-10-09 04:25:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f68e49eb-754a-3b4b-8863-986e65674dd4 | -3.01223 | -54.06043 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e52ece52-8faf-313b-a661-b675696c4ce0 | -3.08143 | -53.95511 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f61b8035-f885-3946-9b6b-3b0bb2d39260 | -3.30664 | -54.05613 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5071a423-69dd-344d-839a-a4291fdf4684 | -5.32165 | -43.41956 | 2026-10-09 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e263d6d7-ae25-327f-ac7e-e296fcbaf654 | -5.71111 | -53.48072 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 064dfb95-5ac3-3bc2-b607-c732f137365c | -3.59871 | -54.67611 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1407a89-7713-3501-97d8-431ef5cc85b7 | -3.30324 | -54.01419 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 46d95884-d495-3fad-aaeb-494e9c30ccad | -2.81129 | -58.28727 | 2026-10-09 04:25:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 8d51ada4-b1e1-3585-a18a-b5dd3e9220bd | -2.88368 | -54.16127 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8dd78e8f-7ff6-39e8-ab95-52b47b000330 | -2.84184 | -54.12968 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8d3cae1-b6d1-380d-83c7-c407c5ec6703 | -6.89821 | -45.88624 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 71ab598c-3b9c-3d57-971b-4618b64b6c7e | -6.0057 | -40.96074 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| c51b629d-fbeb-3038-abb3-70d7e0886628 | -3.87963 | -55.99232 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ce6a9293-b59e-3c2b-98b8-17952dfa8925 | -3.01181 | -54.09363 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e7f2d85-ef02-3551-a8fd-580041b290d4 | -3.59654 | -54.56269 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54031c25-b1ca-3b45-b600-dc3ae9f507c5 | -4.89155 | -43.34179 | 2026-10-09 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d99cef4c-fe60-3991-b84a-c9e098fb1bb1 | -6.88612 | -45.89864 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fce1a5b-19e9-3876-a0db-7a3463929605 | -6.91254 | -45.88131 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6ba230e-b889-395c-b571-cba60417c062 | -3.72626 | -54.22541 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f44a5b4b-048d-3433-8512-76e229d64a57 | -5.08846 | -46.21367 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6591dc6-0bfc-36b5-bf31-0fea93dc086d | -3.00829 | -54.09023 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4097a740-06ee-3848-a20e-2913edc78127 | -3.30104 | -53.70734 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0524eaad-f261-3c62-a7d3-5b92209496e1 | -3.66608 | -44.76921 | 2026-10-09 04:25:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac06788f-3b11-3c98-a207-35bb2d8ea53f | -3.32825 | -50.18265 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc4038f6-f55c-3027-b7dc-d9b2cc621ace | -3.48415 | -50.08689 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2af7d290-79d2-33de-898c-b3c59fcd8855 | -3.26643 | -54.0499 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b770ec2d-230a-32ff-bc08-33a8c8f6d0a9 | -6.23319 | -43.85763 | 2026-10-09 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b40d029-e689-33cd-95f0-62988076569d | -4.75392 | -55.66099 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a505743d-dff9-3f21-8637-ea0a31039a69 | -3.02133 | -54.06789 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d97b149e-f881-3376-a79b-4994a8645390 | -2.58513 | -56.18608 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 004b5245-11d3-337a-9858-1bdc318b79ad | -6.45789 | -46.02716 | 2026-10-09 04:25:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79aa692f-42b7-33fa-9b1b-d1518a279fe1 | -2.73783 | -54.10566 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1cf46fc2-4a33-317c-8ae3-5f69739808be | -1.59601 | -47.35498 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 250978a0-4131-3c90-bca2-599fee3a4f48 | -3.48342 | -50.4889 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ac00a7d4-3f4e-3448-855c-ee48e18030a8 | -6.22968 | -43.85717 | 2026-10-09 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f1102f5-e3ae-3ece-aa09-f5cee816acab | -6.69458 | -45.31144 | 2026-10-09 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 448685c9-485b-3e70-9a2d-801e73cc97f2 | -4.64416 | -48.74004 | 2026-10-09 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5eb742ad-9e0b-3bf1-8dbd-b77568ec8e0b | -3.9448 | -55.84929 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 59097b1c-26aa-32d9-accb-e7e5fc497a58 | -3.11782 | -53.79631 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2c5c020a-047c-3135-8220-eb0a5826a5a6 | -4.80353 | -54.67296 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2ecdf740-4aee-3f71-b6c8-7c7b8346f871 | -3.57183 | -54.67231 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1f74cb0-51a1-3b9a-b3d9-c346113535fc | -3.23575 | -50.17975 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e1b4ac52-e399-3f70-b5d2-85bc6d05c159 | -6.37162 | -42.52053 | 2026-10-09 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 195430db-6055-3f34-b742-8ba7b3699cb0 | -4.64065 | -48.73952 | 2026-10-09 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0647ba5-a9ef-32fa-af0c-c433c21d9353 | -2.56832 | -56.17886 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27135bf8-01d4-3b11-b908-2ba5fa5f81ba | -3.25468 | -50.40934 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a1497051-5213-3764-958b-728aedd2bce4 | -5.23711 | -48.4084 | 2026-10-09 04:25:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 197fb9fd-9714-372a-ac3d-da07383e21e2 | -6.55162 | -38.07344 | 2026-10-09 04:25:00 | NOAA-21 | SANTA CRUZ | PARAÍBA | Brasil | 2513208 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d4835a20-bd49-3eb0-a058-6806632827ca | -4.37004 | -41.81425 | 2026-10-09 04:25:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 06a28f62-2999-3732-8332-d91dd6ca0d37 | -3.198 | -50.56097 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8a71744-87f3-3f78-b78f-d401beb8a7e0 | -0.99816 | -47.65697 | 2026-10-09 04:25:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6f96f99c-f63e-3fca-9ebc-34db3c7ed2fc | -3.50416 | -59.26498 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 30a73c74-07e2-3019-959c-c1855571e261 | -3.03867 | -54.27715 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f85f05f8-0f87-38e9-8432-9a8fd91c7666 | -3.26866 | -54.28758 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7a08bd20-d0f0-3f07-93d7-1bb6cf78afd4 | -5.88698 | -43.4178 | 2026-10-09 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 32cf3a50-a95e-3b80-85be-aa3bf72503c5 | -3.00275 | -54.09241 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfd60f24-2219-381f-80f1-85fabe5ff62c | -3.42874 | -54.06456 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1d44993-a24a-33a7-81c4-2fb3da976b51 | -5.09336 | -46.20387 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b051ffb-691c-3e95-91b6-98b6f35427c3 | -3.30558 | -49.12409 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67e0932b-7435-3147-a4df-9976300d10ed | -2.46267 | -56.0624 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4360f025-6ed0-3666-aa7e-faf767406d26 | -2.86894 | -40.01456 | 2026-10-09 04:25:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 6acf77b7-6567-3685-badb-57264caab7d5 | -3.30762 | -53.86402 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4caf939a-bbec-3a84-b872-3ff30c16469d | -4.32981 | -55.01451 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8d7cc0d2-82bd-396e-a0ee-75f56a3ef016 | -3.47769 | -59.50235 | 2026-10-09 04:25:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ff87a447-10a3-3413-9167-b73bba0e296e | -2.39705 | -51.29833 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd1d79a6-9322-31fc-bf0a-5a2d98cf784a | -2.50649 | -56.15741 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d51dfff7-42fe-326a-8e9f-8f94c7465cf0 | -3.30014 | -53.71297 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dcc8b83c-5c16-3c49-b721-33762e9a8338 | -3.08126 | -54.27359 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2c47bff-cd3a-37ef-ae79-d702a955518f | -3.57132 | -54.67544 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97f23564-3ae1-3c16-aa74-09e731702795 | -6.16497 | -44.86027 | 2026-10-09 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23bccb1b-ecd0-362f-acbd-25d5c6fae8c6 | -3.09791 | -54.28655 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b71008e-e625-3a4f-a8f7-6f839b0c4195 | -4.56279 | -54.20847 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9286a6b0-2fd6-3250-9309-dcaec28aebbd | -4.517 | -54.8983 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 03e52e23-b1fd-3275-8003-4e2243f6bb83 | -7.12937 | -41.80955 | 2026-10-09 04:25:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ad8ae7e1-bc9d-3584-b9a3-dae2c5d2ce16 | -6.96242 | -45.24651 | 2026-10-09 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ca23713-7e5c-3439-afdc-8a166fde9a18 | -3.02834 | -54.05703 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 427c1c73-3eb9-3481-b180-2cd10423d493 | -3.17839 | -50.58151 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 83323740-e63a-308a-893a-b78c15b4ceff | -4.1275 | -50.83536 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5a4ad4c-ad1e-3ec6-a667-2e97b6ae0285 | -4.93673 | -45.72474 | 2026-10-09 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 082c8cb0-e85e-3ff3-9d45-99257cff387c | -6.32336 | -43.79039 | 2026-10-09 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 431389b0-4eb0-3296-9390-9784b0cb038f | -4.85891 | -42.83967 | 2026-10-09 04:25:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6521da24-9cab-3ea5-acfa-fadea3acb262 | -7.17876 | -44.28412 | 2026-10-09 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 53150e35-ea79-31bb-8037-449016a00c70 | -5.09781 | -46.21864 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 83ef169a-b07e-38ef-9ced-6b073c641716 | -5.40575 | -45.92209 | 2026-10-09 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82e30b9d-68f9-371c-95c7-654196e5c089 | -3.43707 | -54.5431 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 950712ab-c747-3b51-b7db-83c683672726 | -3.58934 | -54.66819 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6df231fb-cc80-3e40-91e0-91057374567f | -3.09525 | -53.93354 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f1673ffd-3f74-3004-815f-2ca3a5d0e120 | -5.24229 | -48.39405 | 2026-10-09 04:25:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bee72abc-4531-3657-b82c-22483704ceb3 | -6.83101 | -39.56318 | 2026-10-09 04:25:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7a8ed539-af5e-3728-acec-29af8e4111c5 | -2.99288 | -53.89968 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| aecdf4a1-c193-39f7-9d93-0f480b2229ba | -5.10111 | -46.21915 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README79.md)
