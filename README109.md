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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 842b4fdc-707a-3bf9-8c3e-0f4e0aae9125 | -6.83236 | -55.54101 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db4d3e76-c37b-31e3-a7c2-9bb5a9ea0676 | -3.46136 | -58.40265 | 2026-09-22 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e36ea64b-cd54-3234-b78d-c85d4f4084b0 | -7.60904 | -55.36078 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fcdfd86-117b-3af8-9cfa-1d0e5ececa83 | -4.64347 | -50.99308 | 2026-09-22 05:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d6ea2ab9-842f-36d6-b903-f669a3769701 | -5.98369 | -57.78074 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 208c3f64-bdc7-3ec7-80e9-31de20af0432 | -7.72001 | -61.24137 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c0baf521-5aae-3430-9169-d79c75d5ed43 | -3.47762 | -59.5787 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa88204e-7e2d-3cee-9390-9c25e5411b5f | -3.32985 | -60.72065 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc1821ba-2dd6-327d-8c0e-3fd08f73d10c | -3.11435 | -59.3213 | 2026-09-22 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa6548eb-d574-3dce-a713-e9a2167dd832 | -6.19679 | -57.78491 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8920b514-1df2-347e-9fbb-004d1a7faebd | -3.19597 | -61.12517 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7569b8c7-f9fc-3e63-8665-19f5b3cfac2c | -4.20382 | -59.91421 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2a25853-a48b-366a-bde7-3a927f3e00ee | -6.627 | -59.93513 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6f3d8ec8-4895-3eca-9efd-6262b1468ae0 | -3.46141 | -59.53549 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38d80010-2361-35d3-91ed-ec023637b08e | -6.33882 | -59.94838 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7e550dd-adcb-309b-b32b-09dfb2f176db | -3.71394 | -60.55642 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39f748c0-3f78-3820-b155-db0c78ca4386 | -3.46683 | -59.54988 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9402632b-83ed-3036-b4f1-a479fb666cf9 | -3.17496 | -58.5955 | 2026-09-22 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab57913d-e63a-3506-9bf0-e8f2eb347644 | -6.29225 | -57.75082 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c55d16f-4f1e-3524-8edf-969292ed9375 | -3.04847 | -61.26348 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c691bb2b-3d93-335f-8fee-56e200990605 | -5.81776 | -57.74161 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d22bd5c0-cdf3-350f-a0a5-c7a93a94ce74 | -6.30798 | -59.94829 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b62ee1c-fa30-3c56-8013-142f7902a57f | -2.40996 | -58.27826 | 2026-09-22 05:42:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b3f9de3f-4780-3238-a9c4-03137c91819b | -8.60006 | -54.62189 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b644e4b7-f06e-3630-bd89-05d9c41b7be5 | -3.40399 | -61.29774 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9136f500-efc6-326c-92e7-b0d6f9e0f2ef | -7.61422 | -55.35707 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| def538a0-4681-3cb6-88f1-4839f88b75e5 | -3.71661 | -60.58426 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22e5b629-b149-3d58-ae97-c883727dd999 | -6.72468 | -55.09742 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61e2ab9d-9836-3cfa-a142-1fadfec9c5d7 | -2.60466 | -59.75866 | 2026-09-22 05:42:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9237f1ae-d336-36fa-bef1-3a31d963d23a | -6.07068 | -57.72987 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a7a104e-1672-38f6-b19c-85cb4a892f4d | -6.09 | -57.69734 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d1c945f6-8c49-37d1-8599-5747cb3ad4cf | -6.75072 | -59.07009 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4635a5e0-3bf8-36cb-be26-c32f7a6c2d3c | -3.2904 | -57.85954 | 2026-09-22 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0ab812bc-6bff-3021-8e63-1e8c25cd7286 | -5.98057 | -57.77179 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 69b74d9e-a24f-3064-9d40-519c4cd20aa7 | -6.31087 | -57.74511 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dbaf86c9-df48-3aaf-a7b6-b2cdce0c34a2 | -4.38642 | -55.03119 | 2026-09-22 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 075196a3-949b-3a6e-93f1-959657c04af4 | -3.38415 | -61.29132 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03850aa6-57cd-3d23-8acb-d495cc39a8fa | -8.60758 | -54.60789 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dd8c8c6-c9a8-3ef3-9885-fd13ad2dffb7 | -6.69721 | -56.16338 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dab7f54c-8757-3be2-ac8c-51ca7dd9d361 | -3.0589 | -61.28764 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e6fb854-08ff-3c38-ad64-98b9bb16c306 | -6.14564 | -59.94675 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 783d6668-13d5-37da-bd08-1fc01fa8e686 | -3.05639 | -54.41281 | 2026-09-22 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 932bb4e7-6e68-316f-8aae-73d2a7b06573 | -3.65096 | -58.86205 | 2026-09-22 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42452717-a35c-3e98-9640-629733482bc6 | -5.82269 | -57.73812 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fdf3e56-c518-3b75-b590-ea3dbddb89cd | -3.19539 | -61.12892 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ee123cb-4a71-3d1b-9678-456adec1d487 | -3.06971 | -54.39489 | 2026-09-22 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55f644f0-f188-3c3a-9a20-021922ba67b4 | -6.64286 | -59.9304 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 27.1 |
| dfefa8e4-3c3d-3a24-9743-46f014ed963e | -7.70326 | -61.53882 | 2026-09-22 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b53377ed-65a7-3958-9563-9982a35a92c4 | -3.24153 | -60.80597 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e13fbbfa-3020-3b9d-8d9a-55d687747afd | -8.9256 | -50.89796 | 2026-09-22 05:42:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 99100f9e-a3b5-3245-805c-af647ddf225c | -6.74556 | -59.42125 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ec30480-dba5-3ed1-b9b0-a98b133d945b | -5.97833 | -57.77233 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6c09af1-e016-37aa-8bac-efde150f62ce | -6.7537 | -59.11683 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acffb0ef-1831-3b5c-9492-f91669031f84 | -8.61627 | -54.62796 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f627f471-a773-3b43-9f74-a3aa7ba81f40 | -6.13472 | -59.96817 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eb509ffe-58e0-37d5-814f-1231170b4b32 | -3.22538 | -61.04898 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17e9fd49-5553-30a0-80a5-3f9099f3fa5e | -5.98402 | -57.70536 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6fcba0aa-48a2-3672-84b8-4292a908488c | -5.88525 | -51.58148 | 2026-09-22 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f6f9f936-abb9-37da-bfb4-1905ac3cff1f | -6.46032 | -59.98798 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 241949be-814b-363d-8059-e8838bdc5534 | -5.42375 | -60.17161 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03c45ab6-2c82-307f-9d32-e405bb0a2aaa | -6.73346 | -55.07289 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fda9f17b-3ecb-3ec0-ba24-58a237380b41 | -3.40742 | -61.29826 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de1568bc-e1e8-3335-8940-8a9b27113cd2 | -6.13744 | -59.95011 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15b606e2-c3ca-3f09-8630-01dae19472d4 | -3.41484 | -61.2956 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a975c2b-1736-3b61-9d4f-1b60162c5810 | -6.30115 | -59.93983 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0b49b0c1-6370-3355-a114-9d3ba766b9ea | -3.12909 | -61.24175 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de2d3cdc-43f5-33ef-a48d-2863ad7fb508 | -6.34381 | -57.86165 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a51bef95-60fb-34c1-94ec-50f00245fae5 | -4.05614 | -56.31106 | 2026-09-22 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ec21401-b86e-36ae-ba50-0964cc1ddfdd | -6.91807 | -59.63702 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 747c9ccd-ea00-3058-acc0-4c9de9d10f7e | -6.69242 | -60.01292 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5127a62a-d877-3658-a9de-418b7713f636 | -6.77699 | -55.49062 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46fa5346-267e-3d6c-b3df-6daa58ea4fa3 | -6.19246 | -57.78432 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c1a5e33f-8cbb-3b9b-a627-f0040eee8624 | -6.79654 | -58.79078 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28a59ccd-6d6f-3b4e-85a6-7d7ea031721c | -3.4645 | -58.3289 | 2026-09-22 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f3ccb86-8973-3a22-8c43-f78604150fab | -6.12128 | -57.75716 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| be63551d-e2f4-3714-b68d-71fb8a354daa | -6.31025 | -57.74927 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 729083d4-1767-35b8-9a1e-165d4c7c3cd5 | -3.46986 | -59.55492 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3043fcad-fcdc-39a5-87cb-9dc4b9e0feba | -2.93789 | -57.80408 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0ed4c0c6-86a3-3a4a-ae9a-04ba7955cfb7 | -4.3476 | -55.66524 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40985116-f91d-3bac-a7f8-e4b4e9a8da93 | -7.69974 | -61.53828 | 2026-09-22 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9ea6b86-82e7-3a8a-9455-67fc60691e6c | -6.74565 | -59.07655 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae79d1dc-f2ec-3e47-a44d-7325421d335e | -3.68648 | -60.5929 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ace16cc5-3e7c-388c-b613-241aae50460d | -7.60423 | -55.3569 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25bad7ea-5785-3a5e-bad3-8f0f0ae8afe0 | -6.06964 | -57.87089 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 070672e3-d8ca-3ed9-a006-08abdfa55cd3 | -3.10538 | -61.41515 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84589279-81b0-343d-a7a3-422d594cf43f | -3.77366 | -61.19651 | 2026-09-22 05:42:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d275e6d-4ec9-3b34-9c74-1d9ddc9f1ba2 | -5.73004 | -53.46651 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bfdc77d-171b-367b-bc46-13c4b993f679 | -6.46378 | -59.96497 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| faa4609f-a772-3975-a9cc-7411a7e2fecb | -6.81584 | -59.43427 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32a7ba83-623e-33db-ae8b-3acb9bcd3d65 | -6.13915 | -59.96424 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef9f74d6-e016-3db8-95bf-020239d9e4d4 | -5.81033 | -57.73215 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 254d68ab-e269-314e-ab76-952e7f543ea1 | -3.1048 | -61.41881 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25272050-0376-3617-9bef-cb59f682c6d3 | -6.38329 | -55.27935 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6864b5bc-a161-33f3-b7d8-173cd0c99acd | -2.87673 | -57.79105 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7406087c-6ec5-3f5c-8c06-06f0801302d8 | -6.72468 | -55.05886 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a005df2e-6782-37f7-8005-d553b8ab3a5e | -8.26329 | -55.30426 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 01b1cd23-ccf8-38d2-b66f-5943556972b7 | -7.57894 | -61.16636 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed50d0f9-f2b2-3dba-8a0d-1a6f740ce8be | -7.7116 | -61.24846 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7695f578-ee1f-3f71-84cf-091b514a30c1 | -6.2966 | -57.75147 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f0c759a-3b4f-3494-a164-50e5662b4856 | -8.92478 | -50.90447 | 2026-09-22 05:42:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README110.md)
