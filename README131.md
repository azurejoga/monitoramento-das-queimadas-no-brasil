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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2c962f0-f0cd-3fec-85e2-4fd107949357 | -6.6129 | -43.7317 | 2026-09-23 12:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 211.4 |
| 63c78065-cbea-377a-bbdd-1b9f85819499 | -8.0923 | -44.3307 | 2026-09-23 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| f5e8daa1-68cc-331b-aa79-ef4b56bec667 | -7.0352 | -44.6396 | 2026-09-23 12:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 184.8 |
| 1da9f626-efa1-3b00-8d03-68089be238f8 | -8.5989 | -44.5531 | 2026-09-23 12:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 99.8 |
| e8fb7de5-eb51-3390-b032-2fff7b4eb1fb | -8.5992 | -44.5301 | 2026-09-23 12:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 225.1 |
| 97e5524a-a16e-3f7f-81b7-59097eeaa0fa | -7.0164 | -44.6413 | 2026-09-23 12:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 9984d8e7-1e93-38fc-ad05-9d7bc67253ef | -8.378 | -45.6036 | 2026-09-23 12:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 197.7 |
| 5a01e897-913f-3ccf-82ed-e6da6c1ddffd | -6.6331 | -59.9265 | 2026-09-23 12:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 1420ef2c-ec9b-30fb-a7a3-f9b7924ab716 | -8.7916 | -44.2778 | 2026-09-23 12:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 187.3 |
| 405d12a0-d910-3a14-8010-f2e4268de729 | -11.1 | -51.0475 | 2026-09-23 12:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 106.2 |
| efccf079-a150-3d4a-b4ce-eaa771c0065d | -8.9202 | -45.9536 | 2026-09-23 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 1d8d35cd-94b5-3c1d-847a-c8599222ff33 | -6.6146 | -59.9272 | 2026-09-23 12:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 880169c9-25b9-3340-8834-db83bcd93399 | -8.9016 | -45.933 | 2026-09-23 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 4761b780-727f-3360-8b88-11877118d989 | -8.0298 | -44.8197 | 2026-09-23 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 2667ee0d-9680-3272-8e5e-20067e9a32f6 | -8.3591 | -45.6056 | 2026-09-23 12:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 1511eea4-9de8-3e3e-ad06-cf3811cc3f7d | -8.8102 | -44.2988 | 2026-09-23 12:10:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 8e9b2c17-5c00-3a90-a634-ecc4d7c3da41 | -9.9163 | -45.0885 | 2026-09-23 12:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 074ea80e-1a9d-3f00-8a9e-1fdf53e2acdf | -8.9205 | -45.931 | 2026-09-23 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 001c992b-3fbb-3363-9f7d-f488e366ad65 | -8.8108 | -44.2525 | 2026-09-23 12:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 4913763b-181e-3964-8f53-1ca7b7e9f399 | -9.5735 | -46.5337 | 2026-09-23 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 59797603-78d9-35ec-b83d-61e60735997b | -12.2975 | -46.3857 | 2026-09-23 12:10:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 59a860fb-c28f-34ba-a794-8fd454df23a2 | -8.9013 | -45.9556 | 2026-09-23 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 163.7 |
| 614e8b4a-caff-3bc1-9eba-e9c96275e5dd | -8.8105 | -44.2757 | 2026-09-23 12:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 297.6 |
| 50a74cd0-5e9c-32c0-9c58-436af345ce7b | -8.7912 | -44.301 | 2026-09-23 12:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 34ada7b0-a262-3564-99ed-a3b789c561a9 | -8.39 | -45.6 | 2026-09-23 12:15:00 | MSG-03 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 47f0c4db-502d-3265-8fd3-8515a63350c4 | -8.8102 | -44.2988 | 2026-09-23 12:20:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 111.0 |
| d9df3b00-82b6-38d0-86ca-5502dc19c8a3 | -8.9202 | -45.9536 | 2026-09-23 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 118.8 |
| da091cb1-8331-3242-a59a-8f84eb87c34f | -8.378 | -45.6036 | 2026-09-23 12:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 109.8 |
| e6d06512-4534-39b1-98b7-323f04e73583 | -8.3783 | -45.581 | 2026-09-23 12:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 1c3416fc-7a65-3623-8ef1-4ad0bbae09fb | -8.0923 | -44.3307 | 2026-09-23 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 3af17077-0795-355b-8c06-bab7bba3afab | -7.0352 | -44.6396 | 2026-09-23 12:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| dc0ab9bb-ef1d-3cf1-ba7f-1bff5e4a60eb | -9.5735 | -46.5337 | 2026-09-23 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 248.4 |
| 62da6f33-de98-37e9-9d37-ca9aa8323bf1 | -8.9013 | -45.9556 | 2026-09-23 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 97de78a0-1340-3345-b4a9-b41de8fbc45e | -9.5545 | -46.5358 | 2026-09-23 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| e7f0cb5f-bbe6-38b8-a457-250a258f3a00 | -6.6127 | -43.7549 | 2026-09-23 12:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| bdfd4804-e62b-343c-acf6-fd91d0ae7423 | -8.5803 | -44.5322 | 2026-09-23 12:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| f077a956-6431-3425-820d-2954f5139918 | -9.5549 | -46.5134 | 2026-09-23 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 070be8a7-821c-39c2-af6d-501b95e1d88c | -8.9205 | -45.931 | 2026-09-23 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 167.7 |
| ecc48b1b-b38a-3b6f-9abd-d59e37ddb242 | -6.6129 | -43.7317 | 2026-09-23 12:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 333.5 |
| 1b006396-fc5d-359f-9f9a-28e2a6b04b9c | -8.9016 | -45.933 | 2026-09-23 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 8bca7069-4d6e-3b0d-9841-ed5044948bc8 | -8.7916 | -44.2778 | 2026-09-23 12:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 134.6 |
| f8852a88-cfd9-370b-8cc8-73c6d1cef00e | -11.3976 | -44.2167 | 2026-09-23 12:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 54a25b29-629e-378f-98d5-13e372f1ad50 | -8.5992 | -44.5301 | 2026-09-23 12:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 95.5 |
| f494fcdd-81cf-3cff-906c-9760174c67c5 | -8.7912 | -44.301 | 2026-09-23 12:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 732bd211-a0ef-355b-80cf-2cb3870cfa80 | -6.6146 | -59.9272 | 2026-09-23 12:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 179491d0-b852-3138-9bcc-18c8f3309a97 | -6.6331 | -59.9265 | 2026-09-23 12:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 4ba32ea2-dd67-3a28-9d69-b1d1011a4878 | -9.6043 | -48.4529 | 2026-09-23 12:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 931aec9a-c6bf-3ca2-830a-537acaaa4265 | -9.5924 | -46.5316 | 2026-09-23 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 163.4 |
| 797127c9-decf-313f-923c-00dc47c69428 | -8.3591 | -45.6056 | 2026-09-23 12:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 853ddc5a-d40e-3411-a43d-82e2f5739f36 | -8.8105 | -44.2757 | 2026-09-23 12:20:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 203.7 |
| d93b9141-e7e4-33d5-89fd-6a549123247d | 1.27334 | -50.85569 | 2026-09-23 12:21:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 38c8b11a-3916-3baf-8b68-62634236881c | -1.32055 | -53.13913 | 2026-09-23 12:21:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 82605dcc-767d-30ee-8822-32001bc8432e | 1.56699 | -55.90501 | 2026-09-23 12:21:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| b5d1f255-cfcf-3f74-b357-74b589e3732d | 2.09196 | -50.94791 | 2026-09-23 12:21:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 0f73486a-dc70-3076-b97c-af2516426067 | -2.82746 | -49.23306 | 2026-09-23 12:21:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 6ac094c9-6e22-3a36-b540-66c310fe63e6 | -3.23263 | -53.95099 | 2026-09-23 12:21:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b5714b1b-2b62-38ba-ab69-89e8a5aa7cb5 | 0.59833 | -50.79624 | 2026-09-23 12:21:00 | TERRA_M-T | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 30.4 |
| c1cddd1a-d3a7-37ff-8cd5-20793353c824 | 1.53781 | -56.03181 | 2026-09-23 12:21:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d844f25a-60e1-39ea-bef5-627c54e6ef01 | -3.20984 | -53.38934 | 2026-09-23 12:21:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| edf11a1d-37bb-37d5-99b4-2b038e44b180 | -2.51846 | -57.72962 | 2026-09-23 12:21:00 | TERRA_M-T | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2e86efa8-598e-3acb-ae5d-11f2900d992e | -3.00619 | -54.18022 | 2026-09-23 12:21:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8857cfe6-2184-357a-a625-b09f33921fd5 | 1.56574 | -55.89624 | 2026-09-23 12:21:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 0e4ce10f-dc67-355e-b965-ff68713bea0a | 1.56705 | -55.84247 | 2026-09-23 12:21:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 541a689b-9296-38fd-8fef-4ce81df01c22 | -1.88434 | -55.52045 | 2026-09-23 12:21:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 05e39f41-79bb-3df6-849e-1718ad8ef628 | -3.21977 | -53.39059 | 2026-09-23 12:21:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 845f791b-c18b-3024-bdc3-39b7457d28d1 | 1.5733 | -55.88627 | 2026-09-23 12:21:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| b7a218bc-0b7b-3d7b-b85e-ed0e0e9b267c | -2.44848 | -49.22787 | 2026-09-23 12:21:00 | TERRA_M-T | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| dfbb2601-c0af-3168-926b-77b5da840204 | -1.88307 | -55.52932 | 2026-09-23 12:21:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 58e8ff27-ce98-3437-a05d-c58c1cedb61a | 0.60047 | -50.81136 | 2026-09-23 12:21:00 | TERRA_M-T | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 10.4 |
| b0297deb-a53b-3383-a816-1662fdd1f392 | -2.62297 | -57.96504 | 2026-09-23 12:21:00 | TERRA_M-T | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 48aef2b2-1338-3183-8247-971c14b63dc0 | 1.27327 | -50.84976 | 2026-09-23 12:21:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 0584d23d-44c3-3c8a-a506-4b8bcb9b0cf9 | -2.95652 | -54.08436 | 2026-09-23 12:21:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| b19d7915-afdf-3367-89b3-eb341e9c240d | 1.43868 | -50.80525 | 2026-09-23 12:21:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 865a9e09-3569-3f19-9693-b527c7a00fac | -2.9623 | -54.0812 | 2026-09-23 12:21:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9f26dc2d-b8a1-3e61-bc4c-8e13ad6e8ab3 | 1.44076 | -50.81989 | 2026-09-23 12:21:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 6502216c-884d-3eb2-a9e0-8ab54579edad | 1.51021 | -55.83886 | 2026-09-23 12:21:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 90200530-2682-3861-9219-79eba8533ac7 | -1.92605 | -58.25279 | 2026-09-23 12:21:00 | TERRA_M-T | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 17.1 |
| e8794757-32c3-31eb-adec-082379138e23 | -1.88255 | -56.24258 | 2026-09-23 12:21:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 33c991d5-600f-3914-b828-33e191d165b2 | 1.5658 | -55.83371 | 2026-09-23 12:21:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 3916523b-1860-3529-9e3f-83c3442300f9 | 1.56824 | -55.91378 | 2026-09-23 12:21:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 20c9f8ed-839a-3607-9689-c3357b6079cd | -2.56784 | -57.51888 | 2026-09-23 12:21:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8728b6a5-d3e1-30f0-ad04-ab55990ffb3c | -2.45481 | -49.22321 | 2026-09-23 12:21:00 | TERRA_M-T | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| bfee11ad-551b-35ef-bd6c-d899fc953e34 | 1.51009 | -56.02666 | 2026-09-23 12:21:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| a28d1d38-0900-365c-97e5-ceeff6ca7318 | 1.57205 | -55.87751 | 2026-09-23 12:21:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 1dd23cfe-9859-3a7d-b1b1-1d7f2694dd0c | -2.51715 | -57.73885 | 2026-09-23 12:21:00 | TERRA_M-T | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 2904a2ca-9160-3ed5-80af-ee3fc95e557c | -1.54633 | -52.77666 | 2026-09-23 12:21:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 0784370c-83d4-3e83-b048-a020c087a993 | -3.21817 | -53.40189 | 2026-09-23 12:21:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 1efd8c95-f24b-3b63-8f1b-b5b50c712080 | -3.2422 | -53.95232 | 2026-09-23 12:21:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 6a2791e3-b059-344d-b4e4-d2658f4367e7 | 1.5683 | -55.85123 | 2026-09-23 12:21:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 04286c8b-1ef5-3bef-9153-064f170e9f16 | -2.51414 | -56.6115 | 2026-09-23 12:21:00 | TERRA_M-T | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 37190603-a880-3005-aea1-302733aa2a01 | 1.56955 | -55.85999 | 2026-09-23 12:21:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| bd7a553e-758a-3bdd-b8f7-c1b69f18a23d | -2.94706 | -54.08307 | 2026-09-23 12:21:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| dc388d5e-385a-3127-8f17-22c1f99ad1a3 | -3.00762 | -54.1701 | 2026-09-23 12:21:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 297895bc-f9ff-3ac2-a885-9ebb5b21f674 | -2.76643 | -57.03297 | 2026-09-23 12:21:00 | TERRA_M-T | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 4a76f837-a0a3-3e6f-8ab0-0b0bb3b6b04a | -1.02223 | -53.73337 | 2026-09-23 12:21:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 3437a7a3-d660-36ed-ab92-23827a4fc916 | -1.8042 | -57.11817 | 2026-09-23 12:21:00 | TERRA_M-T | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3f32601a-c0b7-318d-af33-99f2c776ad8c | -1.22019 | -54.54965 | 2026-09-23 12:21:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fdd1538e-6a89-323f-a605-3f1cefb90bd9 | -4.0107 | -52.10263 | 2026-09-23 12:23:00 | TERRA_M-T | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 433ec5b8-8c68-3eeb-96c1-272eca537f70 | -6.66971 | -58.56942 | 2026-09-23 12:23:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 67108821-51ea-3d3c-9b35-54062cc72460 | -6.63869 | -59.92859 | 2026-09-23 12:23:00 | TERRA_M-T | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |


[Clique aqui para ver as próximas entradas](README132.md)
