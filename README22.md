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
| 2013576d-545c-3f73-a2a8-6f2002d15d45 | -5.12004 | -43.21509 | 2024-12-02 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce21c0dd-a87c-36c9-b953-0c6faecfba38 | -3.77919 | -52.03781 | 2024-12-02 04:01:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fbdc7680-af10-3c8c-b69b-d0598bb639d7 | -6.37227 | -47.35759 | 2024-12-02 04:01:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7088223a-60a7-3a1b-b028-e8a039d06a1e | -3.13356 | -45.97928 | 2024-12-02 04:01:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c64ecea1-3a7f-3001-94f7-36aa19de755a | -3.32359 | -50.19297 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0cd1cb6-e790-3706-b74b-9659a384ddef | -3.82042 | -46.53453 | 2024-12-02 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a62794e4-5b70-32b5-9a9a-24c934704f04 | -4.75341 | -43.71695 | 2024-12-02 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d2eb511-5b65-3f99-8214-1fbc76b587a3 | -3.69196 | -47.11692 | 2024-12-02 04:01:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f182c13-ec9f-3d13-871d-1fd4856c0792 | -4.91857 | -41.34307 | 2024-12-02 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 3fc0738b-a2eb-3739-b912-45ca5e23e667 | -2.09801 | -46.6164 | 2024-12-02 04:01:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6844c286-6962-3805-8dd9-120bc0a39548 | -4.77498 | -46.42917 | 2024-12-02 04:01:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 139c1a37-10f1-36a7-a0e2-4858fa32892c | -6.08453 | -48.06103 | 2024-12-02 04:01:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 2ec24cf8-4bb4-3a77-918d-5193e507a53a | -2.48706 | -46.57663 | 2024-12-02 04:01:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2b6c4b2-56b3-3d47-9be6-10e55e8148ab | -4.10673 | -39.99689 | 2024-12-02 04:01:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 73f1ccdf-bf36-3705-a50a-ce7f193ed161 | -6.1864 | -42.62079 | 2024-12-02 04:01:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 7eaf2954-0e71-3f31-ab9d-fce02977e2a5 | -3.54426 | -51.50153 | 2024-12-02 04:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc976353-da4f-3f84-9f50-abd9365811ce | -2.95927 | -39.96205 | 2024-12-02 04:01:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a4145726-666e-3e94-b560-c4b092151a88 | -6.07948 | -48.04696 | 2024-12-02 04:01:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c34f10b7-b2d7-3ad6-b972-3885f0fa16c4 | -4.92315 | -48.42833 | 2024-12-02 04:01:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bbec494f-6144-3fd0-8443-3a6f3cc2af16 | -4.92069 | -48.42681 | 2024-12-02 04:01:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d08e1d8b-3181-39fc-80e6-b4f9b5b3bf20 | -2.90814 | -51.58376 | 2024-12-02 04:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f32b44e8-26bb-3d82-b9b2-135555615b3e | -3.26444 | -46.45152 | 2024-12-02 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 76a89874-97b1-3234-8c2c-484ddd49194e | -5.19832 | -37.69131 | 2024-12-02 04:01:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ef2d50cc-98bb-3690-b358-6f308318bfc8 | -3.55511 | -46.02301 | 2024-12-02 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fc7b676-a5b6-3969-8db6-02d3ffcd72fe | -4.90454 | -41.34437 | 2024-12-02 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 49bcdb2b-0766-327b-87f1-2087ea73299b | -4.57613 | -43.35382 | 2024-12-02 04:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 5b6e41ef-a7a8-38a0-b11f-93eeb4ab683a | -3.37263 | -53.20897 | 2024-12-02 04:01:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ece07be2-1814-33db-b0c7-ee8ca000927a | -3.28536 | -50.55756 | 2024-12-02 04:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a5079b14-fafa-33d5-a9ac-4c139d0abc06 | -3.72465 | -51.08092 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 39bdeb0b-db31-3708-935b-36693246ecfa | -2.49858 | -47.26903 | 2024-12-02 04:01:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 772502d0-412f-32a1-b011-a8e63660c2a8 | -3.04716 | -49.37836 | 2024-12-02 04:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf484bc1-4459-3f69-8811-52d2f48fff0a | -4.58053 | -43.35003 | 2024-12-02 04:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 335119eb-afd4-397e-a376-2f74051cc62c | -3.26135 | -48.90211 | 2024-12-02 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 657fefd6-28a2-312e-8795-cf5cb0bded4d | -5.12368 | -43.21564 | 2024-12-02 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 16cb3155-7f6c-3cb2-a458-dcc389037561 | -4.08477 | -46.20974 | 2024-12-02 04:01:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3899eef7-b321-30a3-82e9-6bb95c84383d | -2.23543 | -46.38132 | 2024-12-02 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bde23204-313d-3343-8000-cd5cd0eb79b1 | -3.8206 | -46.53369 | 2024-12-02 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c89c466a-a65f-3235-9212-a1b620c2efb7 | -6.07855 | -48.05258 | 2024-12-02 04:01:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 67b34b64-b967-373a-9d66-7428d8f73bef | -4.07423 | -47.09076 | 2024-12-02 04:01:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5e2457d-747d-385d-a4f5-261620f37787 | -4.88946 | -41.29824 | 2024-12-02 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 80f3123f-8d21-3327-9a5a-a7cd7e983214 | -3.97786 | -46.75193 | 2024-12-02 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 41e67ebe-cee2-3e78-bcbb-d42ce008db85 | -2.91396 | -45.34958 | 2024-12-02 04:01:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05e3dee2-927b-3c48-9c46-aa2d03a87f12 | -3.26566 | -45.37511 | 2024-12-02 04:01:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1a4a233e-8edc-3e6b-9007-0863bdedc713 | -3.13214 | -45.98808 | 2024-12-02 04:01:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b648125-1333-3f17-8454-25123fdcba02 | -3.33022 | -50.18972 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 748c1503-eb48-3cac-ae3a-3ffba317d753 | -5.12071 | -43.21085 | 2024-12-02 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0804766f-13ad-3f69-9827-801b57729ab8 | -4.2088 | -48.12201 | 2024-12-02 04:01:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 752b89bf-bf40-32e5-82bd-62187c315b2e | -3.95732 | -46.50526 | 2024-12-02 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 599bbeb5-a817-39fc-ace2-f285e13b93d9 | -3.93497 | -45.79551 | 2024-12-02 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fccb6911-c719-3e33-8add-0be1ac8aa430 | -4.47788 | -48.11697 | 2024-12-02 04:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ccde9984-891d-31e0-8810-82de2bb56a1c | -7.22819 | -39.95933 | 2024-12-02 04:01:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8fc61ff4-6654-3359-a049-007ff8ba3267 | -2.86003 | -48.56015 | 2024-12-02 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9435a81-0de4-3d39-9623-7b7799ae26f2 | -4.00351 | -46.65297 | 2024-12-02 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1972dda-be51-3f64-877d-791dc6efe98c | -4.85917 | -41.31511 | 2024-12-02 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| aeb6819a-e993-304d-b38d-ac002b94167d | -2.8258 | -51.83609 | 2024-12-02 04:01:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6d43c959-f059-3c5a-bb2f-7cc8a1b5704e | -6.1829 | -42.62029 | 2024-12-02 04:01:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 2eb1dcbe-2647-3e35-90e5-c597890306d4 | -4.58279 | -43.35938 | 2024-12-02 04:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b9cd4127-f82a-37d5-8528-8e22e8ec30e5 | -3.70733 | -51.83048 | 2024-12-02 04:01:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| be19dfb4-8ad4-353f-8892-00314badf08f | -2.47299 | -46.57426 | 2024-12-02 04:01:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a45d734-f23b-38c4-8d89-4af677387a80 | -2.91429 | -41.73666 | 2024-12-02 04:01:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 23aa6981-04c2-3f17-8157-04b038cc3b23 | -5.61105 | -43.47526 | 2024-12-02 04:01:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7ff601a-8fd8-32c7-b0e3-e619aaebb196 | -2.54034 | -46.10025 | 2024-12-02 04:01:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c58ef4f5-d7a8-34b4-8437-b90aee883567 | -4.75256 | -38.46873 | 2024-12-02 04:01:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 09eafd7d-ca4b-391c-a293-49b512c17219 | -3.26196 | -48.8985 | 2024-12-02 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2dc1f3ca-662f-318d-82e8-fe242b645ed2 | -2.90257 | -51.57739 | 2024-12-02 04:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1674f2c0-0a35-394f-876c-e44c6b761e32 | -4.39996 | -49.77178 | 2024-12-02 04:01:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b009f5d4-2222-39a2-8c81-1f59afc3bf9a | -1.99267 | -46.45291 | 2024-12-02 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74f34f85-3aac-3002-aad9-acfd5adf1f60 | -3.74416 | -51.303 | 2024-12-02 04:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 977b243c-4494-31da-8e1e-f5df9e501d8c | -2.70473 | -47.74174 | 2024-12-02 04:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 28eb6aa1-0d9b-3bd3-b17d-c9fd69b2ef92 | -3.02888 | -51.54126 | 2024-12-02 04:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0a456e6c-d9b3-37a0-8b4b-effad9f42ca4 | -3.85435 | -46.52882 | 2024-12-02 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 913ac50d-b497-3500-b713-a84c5edc776d | -2.0913 | -46.31787 | 2024-12-02 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af582a81-bc5d-38cb-a702-0d53e3d8f2ab | -1.68649 | -46.20415 | 2024-12-02 04:01:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d1c7982-9ec4-3797-881a-431260d758f2 | -4.07399 | -46.68069 | 2024-12-02 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 912dbd43-32d0-3b8e-9c43-d42a2b2106a8 | -2.82409 | -51.83721 | 2024-12-02 04:01:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13c9b04e-c740-3e1f-81e7-4d67e0227ea0 | -3.03975 | -49.37463 | 2024-12-02 04:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f25db8e-9142-3212-93d8-298897304ab0 | -2.91769 | -40.44413 | 2024-12-02 04:01:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 77ab35cc-4fc1-31b6-8eca-abdd5308d409 | -3.32509 | -50.18426 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16ea98bf-b6de-3dfb-887e-385d1ee1a2eb | -4.05634 | -46.81611 | 2024-12-02 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d92053d-0c32-3afd-a9c8-0daa6121ed87 | -3.90809 | -49.7411 | 2024-12-02 04:01:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3e4c0384-3704-3986-a8e4-ed8ce6a0af76 | -4.55834 | -46.6268 | 2024-12-02 04:01:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e32d4c1-475d-3ab4-af37-8595943417a1 | -3.95121 | -46.00178 | 2024-12-02 04:01:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a7a5378-15b4-3d1e-9f4d-dd8ada35d17e | -2.09751 | -46.61276 | 2024-12-02 04:01:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2519da5a-92f5-3a74-9105-3d8ed4b514cf | -4.27013 | -50.85177 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2151226c-ccb6-35fa-bcd7-c0419e006849 | -3.49009 | -46.08488 | 2024-12-02 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 741e5251-5551-3f86-927d-c4ee889115d1 | -4.44222 | -45.36551 | 2024-12-02 04:01:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b848df31-88fe-39b0-87bb-99c820cee007 | -2.59456 | -45.65438 | 2024-12-02 04:01:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 449bbc98-920c-3689-99a6-1a636ec2a1fc | -3.69958 | -51.83616 | 2024-12-02 04:01:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 888dc5ee-8e77-3586-898c-fe043c5ed9e4 | -4.90509 | -41.3409 | 2024-12-02 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 79c99b4b-bf47-3287-8314-2aa050780349 | -3.74497 | -52.26282 | 2024-12-02 04:01:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d419b7d8-9b71-3734-9597-291268e5384e | -4.63259 | -45.45006 | 2024-12-02 04:01:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d4ff84e-539b-3d2e-9547-2d1086ae7fa4 | -2.6791 | -46.60752 | 2024-12-02 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e1868c16-9b0b-3c90-8f1b-83932dcbc2e6 | -3.15942 | -51.11717 | 2024-12-02 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a011f6df-cf33-3616-a36d-5ac659625b5c | -4.73588 | -43.24965 | 2024-12-02 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1051617d-3ef7-35ee-be25-34dda5089807 | -4.17147 | -48.19974 | 2024-12-02 04:01:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d787b07f-4139-3060-9359-a448a761ab16 | -3.70054 | -51.83072 | 2024-12-02 04:01:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 406a686f-846d-33e7-93da-160ace883316 | -4.4953 | -45.70807 | 2024-12-02 04:01:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55b10215-47f4-3d34-aaed-be87ad976974 | -3.09622 | -53.23799 | 2024-12-02 04:01:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 67fd2ddf-1191-3128-9691-2efcd0ab7966 | -4.3254 | -45.92336 | 2024-12-02 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 46e919d0-3c04-3e47-854d-2ce790d403da | -4.11004 | -39.99743 | 2024-12-02 04:01:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README23.md)
