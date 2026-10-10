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

## Dados Diários - Página 150

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f000f01-f4d2-3e46-8147-da24f5121725 | -3.84734 | -55.78807 | 2026-10-10 07:35:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 00d04522-9a8e-3bca-b89e-34f35dd12d47 | -6.12496 | -55.69412 | 2026-10-10 07:35:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f89e6f97-2dd5-3360-8636-563309bea00b | -4.58302 | -54.95228 | 2026-10-10 07:35:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 399c35e4-dc5d-3bf3-8e11-ef1315b7a046 | -3.84218 | -55.79107 | 2026-10-10 07:35:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| f5938d7c-ae5b-3e47-91a8-e04a385c8efb | -3.6349 | -60.63583 | 2026-10-10 07:35:00 | AQUA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 69e3e70e-0b65-39a2-ac3a-75caa0d2a3ee | -3.81568 | -59.3342 | 2026-10-10 07:35:00 | AQUA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 85af66e6-9306-34c7-a811-a05ce795f5e7 | -3.98857 | -59.35401 | 2026-10-10 07:35:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 0f75610f-3a20-36cc-92b1-609f1dc9a7d6 | -3.74224 | -60.59671 | 2026-10-10 07:35:00 | AQUA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 21.4 |
| f16a6192-7ea7-356f-980f-6facabeb3e44 | -4.19287 | -59.40617 | 2026-10-10 07:35:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 908042e9-9cfd-3248-a7ea-027485877854 | -5.08529 | -60.21952 | 2026-10-10 07:35:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| f5d64523-07d5-3270-9b4a-0ad02248ece0 | -5.70711 | -53.47204 | 2026-10-10 07:35:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 4d411956-deb4-3903-b8a4-25c96f2f3a6a | -3.57644 | -59.07944 | 2026-10-10 07:35:00 | AQUA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 14ae7fa9-91ef-387c-9585-6079f738b015 | -7.18943 | -52.63102 | 2026-10-10 07:35:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 8e01583f-380c-3c91-8721-60acac5c1a0c | -5.79863 | -53.79816 | 2026-10-10 07:35:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 7b40b74d-0f8b-31a5-94af-505513268f9f | -6.46038 | -55.50336 | 2026-10-10 07:35:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| cfbd43c7-9981-3823-95fc-698cd77b350e | -3.70318 | -60.53936 | 2026-10-10 07:35:00 | AQUA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 46d584a2-aadb-3d14-a601-864e13cf73fe | -5.22356 | -60.04554 | 2026-10-10 07:35:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 579c74f2-3981-352b-9073-abae5d0f5bd9 | -5.23814 | -60.18782 | 2026-10-10 07:35:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8fa66b7b-041e-3bd4-98a7-b166bb74087c | -4.09827 | -54.01103 | 2026-10-10 07:35:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 36dc75d9-ce15-39aa-9aa3-19aa2391d5d2 | -4.10322 | -56.13279 | 2026-10-10 07:35:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 4b211650-52a3-37a9-84f4-7018a8fcb114 | -7.23445 | -55.18164 | 2026-10-10 07:35:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 598c9d06-00dc-3b32-a22c-c53d0adcadd0 | -6.31957 | -58.30643 | 2026-10-10 07:35:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| efacaf36-917c-32ef-ae63-a4c761aef91d | -4.59531 | -55.72105 | 2026-10-10 07:35:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 2de645f2-fe3d-3504-bfba-9d57c309bf81 | -5.89151 | -57.72128 | 2026-10-10 07:35:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2c1598eb-95ae-3257-b60a-013b3d5527de | -6.32836 | -58.30773 | 2026-10-10 07:35:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| df5afd35-2cb0-3ada-895e-e4c00354318d | -6.42377 | -55.25643 | 2026-10-10 07:35:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8e322e1a-cc3a-38bf-86cc-76a5bdeb65c0 | -7.50559 | -54.98972 | 2026-10-10 07:35:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 366b07dc-d2bd-3855-b82f-e7a8573198bd | -6.93907 | -59.24275 | 2026-10-10 07:35:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ef062ff2-6e91-3f9c-a04a-8e513f1776f9 | -7.50375 | -55.00278 | 2026-10-10 07:35:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 9711424d-bcb9-331f-9765-df2d27fdaa75 | -3.90266 | -55.80667 | 2026-10-10 07:35:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 99b11914-aff5-3907-9dd8-b1561f01b46d | -3.84373 | -55.78078 | 2026-10-10 07:35:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8d377740-e4aa-38d7-b751-4169d39ab984 | -6.37691 | -56.23003 | 2026-10-10 07:35:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2b5c41fd-748a-335d-8867-84b6f94d0bd9 | -7.23869 | -55.07828 | 2026-10-10 07:35:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 6d006c99-02e9-3fb4-bdb6-4d246a7c55c6 | -6.22437 | -60.03059 | 2026-10-10 07:35:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0b34fd44-feb4-31bd-8ff3-3f305b716d43 | -6.3202 | -55.33389 | 2026-10-10 07:35:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 40723215-bb4d-3eb8-ac76-948428ffb657 | -3.98883 | -54.46169 | 2026-10-10 07:35:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 528709b9-9b11-3ca1-b5d1-60e98f8e367a | -3.99063 | -54.44932 | 2026-10-10 07:35:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9a53fcac-9460-317e-82e9-1978136d7e46 | -6.43224 | -55.26999 | 2026-10-10 07:35:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d8e38fc2-a32e-3143-994d-e8115a7525e5 | -5.18352 | -60.30782 | 2026-10-10 07:35:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 32dca9e2-973a-3710-a4a2-06f03e499767 | -3.9872 | -59.36298 | 2026-10-10 07:35:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 26.7 |
| e64fc2da-f45c-3be7-b6b0-de5c4cf66073 | -6.47212 | -55.06266 | 2026-10-10 07:35:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 38ad9f47-69b3-32a7-987b-ada445403ce5 | -6.4621 | -55.49166 | 2026-10-10 07:35:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d4391b84-d4ea-31a8-87f9-8d09a5f1b4ab | -6.93774 | -59.25152 | 2026-10-10 07:35:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| fea0ebcc-1c90-3d80-aa8a-bdd1c787caa0 | -3.90178 | -58.94696 | 2026-10-10 07:35:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fbef2d39-3441-3bfe-91cb-c3e638f97f44 | -4.59286 | -55.7141 | 2026-10-10 07:35:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4e476866-524f-353d-9cf7-c7c84b0124af | -3.97848 | -54.45988 | 2026-10-10 07:35:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 0c2bb021-ecfa-36a9-96e4-7a876df20db2 | -3.98025 | -54.44761 | 2026-10-10 07:35:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 47249c8e-234b-3b35-a8e3-8011afe32979 | -4.12047 | -54.03461 | 2026-10-10 07:35:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| fac36732-5c48-3c93-8be0-cb972403a913 | -4.59127 | -55.72468 | 2026-10-10 07:35:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| c984e69f-9436-3362-9b4d-e56c8ecfe8ed | -5.07622 | -60.21815 | 2026-10-10 07:35:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| da3177cc-e7ad-312c-b65f-5ff6fd0e38be | -5.88749 | -57.7483 | 2026-10-10 07:35:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a29f7f21-1831-3b66-9d73-e4fe9ca9aff4 | -6.47035 | -55.07517 | 2026-10-10 07:35:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bd39ea41-fafb-3a3e-901b-6d6cacbbf76e | -3.90112 | -55.81706 | 2026-10-10 07:35:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 323ad5b6-ab85-3695-a563-dacd688a48a0 | -4.10468 | -56.12285 | 2026-10-10 07:35:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| e5b1ab93-c0a4-3812-9d43-7f9b37612d2b | -7.91259 | -54.71236 | 2026-10-10 07:37:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 5a1e6895-9d4c-38d1-a954-7ef2ece98391 | -12.2884 | -63.37553 | 2026-10-10 07:37:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 92f2f562-7d71-3ed9-84c0-bb1077c7d0fc | -8.5008 | -54.61244 | 2026-10-10 07:37:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 49be76b9-c3b9-3aff-9c94-14fc4f2bb882 | -9.25481 | -62.30125 | 2026-10-10 07:37:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7b2a095a-0f32-3050-a349-745f93613503 | -8.22947 | -61.17946 | 2026-10-10 07:37:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 29cdafaa-18be-3d12-a73f-ce83af83abef | -7.91066 | -54.72621 | 2026-10-10 07:37:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 6424b609-b573-3918-95f7-0d3649fcd06d | -8.50283 | -54.59787 | 2026-10-10 07:37:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 96a080e0-955f-36b5-a0e1-f2d9efad05a9 | -10.6012 | -60.4863 | 2026-10-10 07:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 8fa7d466-e3db-3431-b844-defef474c14c | -13.1047 | -46.3778 | 2026-10-10 09:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 199.5 |
| 18802aba-e5b7-3f73-9ff9-4231f72a6ab5 | -13.1052 | -46.355 | 2026-10-10 09:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 3ddb1767-29cf-33db-8aab-5ccd35fb3c15 | -13.1241 | -46.3748 | 2026-10-10 09:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 7a7cf08a-76b8-3ef9-8c24-83b73dc5a963 | -14.2092 | -41.8318 | 2026-10-10 10:20:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 109.3 |
| aef4f918-1215-3555-8644-e7fb55120131 | -17.0737 | -47.7351 | 2026-10-10 10:40:00 | GOES-19 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 96.0 |
| ca76278d-9f0f-3ba6-a6e1-f2f6d0bf86c9 | -11.7764 | -45.5265 | 2026-10-10 10:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| e226d114-e24c-31be-a367-da97983e5aea | -11.7956 | -45.5238 | 2026-10-10 10:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| a822857b-83d9-3259-acf1-4315d159bb31 | -11.1873 | -45.3347 | 2026-10-10 10:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| b9df1679-e001-35ed-8d6f-536c9e52ad36 | -11.7768 | -45.5035 | 2026-10-10 10:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 58fedb67-cd43-3436-9d12-394349aa75fa | -11.7956 | -45.5238 | 2026-10-10 10:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 146.5 |
| d422bffd-c81a-3e3f-b327-fc52e7dece63 | -11.7764 | -45.5265 | 2026-10-10 10:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 187.4 |
| ce48c2e2-0b23-3133-9ad7-bb73b913e4a6 | -11.7768 | -45.5035 | 2026-10-10 10:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 136.7 |
| ca0f4703-491d-3be0-b714-03a39c1ee07a | -11.7768 | -45.5035 | 2026-10-10 11:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| f6ef5e2f-6850-37ae-88db-10336879f49f | -11.7764 | -45.5265 | 2026-10-10 11:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 169.9 |
| 0a15dcd3-998b-33dc-bc9e-4551ca1d4f87 | -11.7764 | -45.5265 | 2026-10-10 11:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| bdc3d620-890c-3430-88c0-84f7cdb4543a | -11.7768 | -45.5035 | 2026-10-10 11:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 69d9f474-c2e4-3b77-b103-b4e3204c91d4 | -14.2092 | -41.8318 | 2026-10-10 11:20:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 99.1 |
| 76154c7f-afc6-3493-bdff-0dcf790f1009 | -11.0144 | -45.4042 | 2026-10-10 11:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 154.9 |
| cebcebe1-b0cd-356e-b71e-178939385589 | -10.9953 | -45.4068 | 2026-10-10 11:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| cf69fdf3-4bbc-314d-a377-6a4027859e61 | -14.2086 | -41.8565 | 2026-10-10 11:20:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 104.3 |
| a8ca3bca-e8c3-3208-b795-e79a9e437635 | -11.0144 | -45.4042 | 2026-10-10 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 5f975d25-eb12-3a2e-838f-af6d7d8497dc | -13.5282 | -47.4204 | 2026-10-10 11:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 110.4 |
| a0f511fa-41b8-3c87-9296-7401aedd4c52 | -11.7768 | -45.5035 | 2026-10-10 11:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| c36e7f5a-e716-3134-97cd-ba769b912993 | -11.7764 | -45.5265 | 2026-10-10 11:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 128.2 |
| c2e6707a-4aad-3b9e-ae43-56f1057ca1bc | -11.7768 | -45.5035 | 2026-10-10 11:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 30d0d776-9a12-3126-9f51-ed1211bd62d0 | -11.0144 | -45.4042 | 2026-10-10 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 216.8 |
| 227db3f3-c82a-320b-8a91-beb5a18dc681 | -11.1873 | -45.3347 | 2026-10-10 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 867d1ae9-d6f3-3666-80f3-e5a18ff29638 | -11.8978 | -47.3642 | 2026-10-10 11:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 4bc6294e-2e0a-360f-9226-a52e59d44cd6 | -11.7772 | -45.4806 | 2026-10-10 11:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 43e44f34-0af9-3390-97d2-e9de20cbfbfa | -11.0332 | -45.4246 | 2026-10-10 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 3c8ef30d-9e10-347b-b76a-5eb38dd266d8 | -11.0937 | -44.0975 | 2026-10-10 11:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 0b9641c6-88b6-3bfb-99c3-ed53c422d422 | -12.1733 | -44.775 | 2026-10-10 11:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 8a3cc9f0-5d66-3b70-b890-74c80df5a613 | -11.8978 | -47.3642 | 2026-10-10 11:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 48cd27c2-35b5-3573-8d24-08ffcb3acbd4 | -12.1729 | -44.7983 | 2026-10-10 11:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| f8ffdd20-4a69-38a5-a280-573f7ab5096f | -10.917 | -45.5317 | 2026-10-10 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 424309e8-394d-3fb3-9f41-39b8e7e43a46 | -11.7768 | -45.5035 | 2026-10-10 11:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 38e2082e-c12b-37b5-ac28-e359a29dea68 | -10.9361 | -45.5292 | 2026-10-10 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 208.9 |
| c6b93ce5-5014-34a0-bd16-f21e81d6ba67 | -11.7772 | -45.4806 | 2026-10-10 11:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 162.8 |


[Clique aqui para ver as próximas entradas](README151.md)
