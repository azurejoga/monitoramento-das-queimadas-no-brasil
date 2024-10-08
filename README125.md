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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1323928-7fc8-3e49-865d-bf9248b55a96 | -10.58527 | -64.41206 | 2024-10-08 05:23:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0d916ada-d634-3b8d-bb87-88c489c32b7c | -10.54961 | -63.83997 | 2024-10-08 05:23:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 280a2267-b562-3496-97d1-907cd3ee57c0 | -10.13948 | -63.66656 | 2024-10-08 05:23:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7532ff8f-a9a4-341b-81f3-3e628c1c7cb3 | -10.13884 | -63.67042 | 2024-10-08 05:23:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 05db31df-d18f-3e42-91f0-bb10262c60cd | -10.02958 | -63.47908 | 2024-10-08 05:23:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d2b876c-27a5-366b-bbd7-f9fc60c456c9 | -10.02613 | -63.47849 | 2024-10-08 05:23:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6e79ef06-3f97-3f0f-a65a-349d0c71dd9f | -9.81506 | -64.22291 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e435040-4352-34ff-8ed2-56f5cc468fdf | -9.80943 | -64.23463 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d92bac1-b621-3ed5-a23f-0811c549289a | -9.74056 | -63.99504 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96c3e7dc-0bc9-3d12-8f8e-1298abd8e016 | -9.73759 | -64.23246 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52041afd-591d-373b-8a31-a0fced4a3d52 | -9.73402 | -64.23182 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3241b55-b661-3ce9-a5ad-d597140ea280 | -9.73046 | -64.23117 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| daed14e4-bf5d-3989-8adc-c12036d22fc3 | -9.70982 | -63.9621 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3cf0dabd-dc3b-36ff-9d48-2d2730a27a5a | -9.59155 | -63.64659 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 575add58-da6c-3c24-a977-a549db84cd32 | -9.58807 | -63.64601 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b2413011-8c76-3a99-8489-40c51a0d4020 | -9.57897 | -64.11935 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be04a220-5302-3a2c-8441-31d247efc54c | -9.57608 | -64.11472 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c365df6-d992-3e71-8e5b-dde06a8cf962 | -9.57541 | -64.11877 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 245563a6-08a4-3f0b-877d-0a3b2f73a349 | -9.57319 | -64.11005 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fcb7b42-42b2-3369-9570-9aafd099be85 | -9.57252 | -64.11411 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a3e46b0-db12-3b34-a738-544eb16c41a4 | -9.57186 | -64.11819 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 629f4be5-6f87-33f1-8939-74ac1250d7e4 | -9.56577 | -64.22263 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8e82e0c-23d5-3ba6-85a0-1c8d871091da | -9.5651 | -64.22674 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 09eb77de-3381-3729-85b8-2065d91f3172 | -9.5622 | -64.22203 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0e72d45-55ce-3ce4-978f-542458820aee | -9.54861 | -63.57242 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f9b8e24-9faf-3c9c-8b18-e4e6b7cdb781 | -9.54798 | -63.57629 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c9f0e051-2247-3e51-b216-07037b15b15c | -9.54735 | -63.58016 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d0310574-634f-3421-942a-5650bfc4a26b | -9.54672 | -63.58403 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b5150b9-fb9f-3e02-b90a-e0e5657421bf | -9.54609 | -63.58791 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7820eaef-16c0-3b47-811d-2d8914dbfa39 | -9.54514 | -63.57183 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0e93c115-8329-36d3-bc2f-078e492aea72 | -9.54451 | -63.57571 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b339537-6326-38f6-bd13-b0f42bdbdeda | -9.54388 | -63.57957 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af9d4e17-629c-3683-a139-99256d16a9c0 | -9.54325 | -63.58345 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01cfa2b1-6cf7-3995-9dd0-434d950f34c1 | -9.54262 | -63.58733 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8bf7dc4-bce5-305b-b7b5-7b9f1b11cd56 | -9.51016 | -63.50242 | 2024-10-08 05:23:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca3c39f8-62f8-3792-833d-4de0f9ad7c2f | -9.50727 | -63.54164 | 2024-10-08 05:23:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f54b3aa-96e0-3478-8eb7-95da5228e633 | -9.5038 | -63.54106 | 2024-10-08 05:23:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3115a787-4fcf-3ba5-bc34-da64d2ada7e0 | -9.48143 | -63.52538 | 2024-10-08 05:23:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce1a0469-14bc-3b6b-b403-1a9ad16e93ce | -9.43816 | -63.62636 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85e79658-c9c2-3715-bb11-28c7af898faa | -9.41018 | -63.71017 | 2024-10-08 05:23:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4ea1b137-0b7d-3e80-8955-86121113cc89 | -9.40953 | -63.71413 | 2024-10-08 05:23:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86de76b7-f447-34c0-887b-b9eefab8795c | -9.40668 | -63.70959 | 2024-10-08 05:23:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8a024cb4-6b30-333a-b9d7-c0afc9d440ae | -9.36117 | -63.81125 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 032d9575-b2eb-3459-acdc-7c5950b5fba8 | -9.3583 | -63.80675 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f99fe197-6eb6-39dd-8ecc-04f72aeb1bd8 | -9.35766 | -63.81062 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e1c6e048-a89a-3ffb-a2eb-641fa72102a2 | -9.3548 | -63.80606 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47cd226e-7602-3f3e-b82d-f5a618f53f92 | -9.35415 | -63.80999 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 966d2ee5-b9aa-38a1-8798-0522717dedc2 | -11.74607 | -63.8207 | 2024-10-08 05:23:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 68b0ffa2-a39e-3e54-99db-08d1c13b88d3 | -11.74264 | -63.82005 | 2024-10-08 05:23:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a18ede91-5cde-3546-a358-67860ed65aff | -11.74201 | -63.82384 | 2024-10-08 05:23:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6361583d-e58a-3d38-b720-1f6d9384efed | -11.69027 | -64.02871 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc1e090e-e865-35f2-bca7-9f9c5be83966 | -11.68682 | -64.02804 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| befdd6c4-54ce-3de3-b157-cc0ca80cc6ae | -11.68617 | -64.03191 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c87e424-22d9-35c6-ac0d-b5c75804d02b | -11.68397 | -64.02373 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b11c7c2c-687a-3c77-b11a-f00f06cc46d7 | -11.68336 | -64.02741 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbae1328-7564-39f3-b4ec-6b1b3d534051 | -11.68272 | -64.03126 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f351b6d0-f0c3-3242-9974-c7e0b434acee | -11.68223 | -63.99153 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 138fb002-f2a6-3ea2-8717-9af84dae5eae | -11.6802 | -63.99194 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65033e8f-2fc8-3479-9090-dcbab00f257b | -11.6799 | -64.02679 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 848b253e-869a-334e-960f-f8857768cbe6 | -11.67878 | -63.99085 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ea4901f-c177-3dd6-991a-8d6e3d6eddfa | -11.67675 | -63.99128 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22740d21-eb08-33eb-8179-40a24d2eccfa | -10.9775 | -63.94912 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9c8080a-14b7-32ec-9348-f4f00846965d | -10.91844 | -63.86308 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec45bff8-d377-3855-b2c4-6f56774d0683 | -10.91715 | -63.871 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b5778a5d-ba9c-3ff3-b5ab-940c631a4357 | -10.9156 | -63.85868 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1e4f7fc-631c-3f89-8eed-e1dbb230795a | -10.91306 | -63.8742 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7030b1ed-71f3-3a85-ae22-3dc1bd01198c | -10.91213 | -63.85807 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca94c06f-54f4-3402-8d65-375a84f21bbb | -10.90807 | -63.86109 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 131346bf-e4d0-3c8a-942b-8591f1730bf3 | -10.90461 | -63.86044 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bb8a9cc-2df3-34dd-95ee-530e686e0018 | -10.89891 | -64.16229 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce95c36b-2da0-388c-92b5-52f357add20e | -10.8982 | -64.16647 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c3aaabf-ed4b-380c-9573-168097a7f8a1 | -10.89469 | -64.16588 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d144f24-9f62-315d-84e0-cceda8d45960 | -10.89332 | -64.17401 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83286bc9-36a1-3bc2-95fa-43752dd60017 | -10.89215 | -63.91473 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7116b2d5-caf8-3444-aec1-122de44b987b | -10.87035 | -63.8953 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0edd6c8-9498-3e3b-973d-fa952b1c01b2 | -10.8675 | -63.89093 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6e982be-4c3a-3b68-bf73-8526954e28e6 | -10.86686 | -63.8948 | 2024-10-08 05:23:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2015e7e2-5138-3f9e-88f3-96bf7616ffda | -10.86466 | -63.88649 | 2024-10-08 05:23:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fd085c02-b9c2-3457-b9a2-f1fec86c66ee | -10.86402 | -63.8904 | 2024-10-08 05:23:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a1d5f7f7-bc0a-3cea-ac42-99d2cd47ec3c | -10.86337 | -63.89429 | 2024-10-08 05:23:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 80c8622e-4151-3800-8d76-0bc3c9caadde | -10.86119 | -63.88593 | 2024-10-08 05:23:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4674a3b-e1e1-370f-a1e1-872d3bbe6b7d | -10.85423 | -63.88483 | 2024-10-08 05:23:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95021b8c-8711-3118-9e9d-1bbbec3875a2 | -10.85076 | -63.88421 | 2024-10-08 05:23:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e02d519e-d045-3127-82cd-8fc55051c52e | -10.83863 | -64.17407 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8bae312-e74c-38b5-bf06-11b4306b6f8d | -10.82609 | -64.18429 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f570c499-bb5e-3fad-a8cf-07b046a7a967 | -8.29299 | -64.06158 | 2024-10-08 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39ded479-18f8-3293-905b-498d72360911 | -9.75254 | -65.23611 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3834c13d-a1e9-336b-863c-962d0b2197e0 | -10.41722 | -64.83609 | 2024-10-08 05:23:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da3dc403-70ae-396e-88de-d3665d0d2a98 | -10.4165 | -64.84042 | 2024-10-08 05:23:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3fc92a2-f6f1-30dd-b35c-cdc2f54f1b95 | -10.41357 | -64.83549 | 2024-10-08 05:23:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0bbb8a64-031b-3646-b243-4f3c8907f6fa | -11.54128 | -65.13311 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64acccd1-8a5d-3fe7-8060-965123b97faa | -11.53689 | -65.13681 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5ad4626-9743-3827-9013-0311906d0d36 | -11.53614 | -65.14122 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d05774a2-0522-3625-9d3f-7e7ce76dad83 | -11.53336 | -65.04701 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 792a433f-0f5d-3d1a-b8ea-3ddcb38412d2 | -11.53249 | -65.14056 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fda694df-1f18-33c1-9cf9-a2085530c725 | -11.52972 | -65.04638 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db0fc0d1-3906-36e5-8d8c-b4a813987997 | -11.52899 | -65.0507 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0942bfc9-1e73-3c4d-b626-9ec34ab0b0b5 | -11.52609 | -65.04575 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e45cd81-a3eb-3503-8747-26664e76bd57 | -11.52445 | -65.14362 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f22840e8-00ac-31b0-b9ea-b4a777e3d88c | -11.5237 | -65.14801 | 2024-10-08 05:23:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |


[Clique aqui para ver as próximas entradas](README126.md)
