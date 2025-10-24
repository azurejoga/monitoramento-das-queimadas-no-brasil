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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63e51924-078f-3549-8cf2-21bf3be19f1e | -11.05833 | -45.38884 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4fd1dc53-3f4a-3267-bbf9-a5e9f1897c6c | -9.24052 | -45.58865 | 2025-10-24 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e079fe2-8d40-3950-93d2-e8d099869ed3 | -9.9382 | -47.45699 | 2025-10-24 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b61c9cdc-1352-3f9b-b705-f36eea3e101b | -4.28435 | -40.70039 | 2025-10-24 04:17:00 | NPP-375D | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 19.9 |
| a8c04a36-92b7-3d87-adaa-221626ce32f7 | -4.63646 | -42.51528 | 2025-10-24 04:17:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4a281030-e692-3623-b436-79495a8dc424 | -2.872 | -50.7175 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 378afd44-c8c9-37e5-9ac6-be4d9cfc0aa4 | -2.39183 | -48.11642 | 2025-10-24 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 051681c4-f01c-39af-9c54-d04512fa3a34 | -10.91333 | -50.16703 | 2025-10-24 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe4ded18-7f6d-3975-931a-39755218844f | -12.07616 | -46.41393 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ab00728-394e-3283-9c20-7d4237e9d5d1 | -3.41007 | -46.90195 | 2025-10-24 04:17:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64d10d32-703b-323a-947e-a60fb1074ed6 | -4.15807 | -46.78817 | 2025-10-24 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e76fe7b7-a8cd-3e65-ab48-88652a5e662b | -3.14926 | -50.16812 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 665ab9bf-81e7-3187-be44-34ce4dc13043 | -6.91358 | -41.53905 | 2025-10-24 04:17:00 | NPP-375D | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e40c77c5-eab4-358f-bc07-10125e24b417 | -9.62635 | -46.88576 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a9f2276-dbd0-35dd-81f8-5e5a689d4e7a | -2.7441 | -47.1355 | 2025-10-24 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9a6c9377-864d-32d1-a94f-09b52656f5f3 | -3.12965 | -50.61683 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06074c4a-dd98-39f9-b1a7-aadaa3c033d8 | -11.04591 | -45.40155 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42feff22-d259-3b73-826b-d598b85c0fb0 | -6.36989 | -41.73938 | 2025-10-24 04:17:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5789dcdf-b53c-34d4-b5c1-65040607c107 | -11.36826 | -45.93454 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9be14ed5-2b7e-3104-972a-b28f35fa8c70 | -4.7984 | -42.75321 | 2025-10-24 04:17:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 70cd8fc0-19ab-3e80-bddf-10119b82873a | -3.87016 | -45.56213 | 2025-10-24 04:17:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 796e7dba-db06-3cb2-8c23-ebe60aaeb43e | -10.95539 | -50.36624 | 2025-10-24 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5fc7294b-13ff-32aa-9bab-a735d57cc9e1 | -9.44184 | -56.6526 | 2025-10-24 04:17:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3116e0de-4ee5-3a75-ac83-b0024ef102c0 | -12.07741 | -46.40631 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 52109800-95af-3d54-a97a-134382f6fc37 | -9.60716 | -46.91248 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f4be1b9d-eb1c-3882-93f7-f7bcee8bbad4 | -4.91751 | -47.32896 | 2025-10-24 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eadd1463-738b-3520-9da9-678ebb64f19c | -5.65715 | -45.95651 | 2025-10-24 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5e12e627-fa98-33f5-ab2f-767993054646 | -4.25037 | -48.12601 | 2025-10-24 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37199d90-f0b9-32c9-b015-bcd6a092214a | -12.03015 | -46.60685 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 554c7d78-3c1f-3a67-b2e8-787a38b4e1d3 | -10.01703 | -47.07503 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d39bffbf-ca98-3a79-8864-71ee6dbd4ba9 | -5.84515 | -40.83003 | 2025-10-24 04:17:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2f80f064-80ad-3e90-8e03-adfe80e2a5a6 | -4.91831 | -47.32398 | 2025-10-24 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f4d96ab7-b7c9-3ef4-86b6-10ccddc94c8b | -5.6038 | -48.65971 | 2025-10-24 04:17:00 | NPP-375D | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d108c77-4bda-3ad4-bad9-c2d915d7f1ba | -2.85274 | -50.73867 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3dce6f67-2ad9-36a2-ac6a-53397e7a5b6f | -5.4492 | -45.41278 | 2025-10-24 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 777afa86-1e07-3e9c-b042-68aaa258d118 | -8.56849 | -48.51338 | 2025-10-24 04:17:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a9708c2-8daa-3a4c-adc5-50ad0f842faf | -11.57978 | -49.53652 | 2025-10-24 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a064ee72-0596-3f76-860f-037acf0fa504 | -4.15101 | -47.67862 | 2025-10-24 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d795a880-04f3-34d7-a985-d4c95f2682e0 | -5.65782 | -45.95242 | 2025-10-24 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| fc37eeb0-cf99-35c8-8fc1-43d74feb8387 | -6.84419 | -41.55842 | 2025-10-24 04:17:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4746e7e6-4178-3a29-9a6c-e259643bef79 | -4.27684 | -40.7034 | 2025-10-24 04:17:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 01c3cdf1-62f4-3598-b384-b978144ed1c6 | -6.30632 | -41.87699 | 2025-10-24 04:17:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3b20d356-13e6-3e12-bf89-a046061ca37b | -3.16008 | -49.16402 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41f0e69b-7f4c-3f3d-a857-93ad9915f883 | -9.64291 | -46.89733 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fa7b9046-cdde-3ea0-8663-d6ee561f694b | -10.01146 | -47.10855 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9c6af36d-4a21-3c04-93fc-84a53d4b13cc | -4.85549 | -46.73127 | 2025-10-24 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa4ce3cc-478c-3789-9881-3650f5466610 | -9.86645 | -47.46429 | 2025-10-24 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24b171ab-b2ab-36b1-8300-4022b221e892 | -12.0724 | -46.43683 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 42d5e16e-180c-366d-862b-6d666a19168a | -6.89405 | -38.27433 | 2025-10-24 04:17:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8c0e5f9d-ed98-3037-92c4-48ded339d136 | -12.25321 | -47.45901 | 2025-10-24 04:17:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c25cf0b-d552-33e5-80bf-71196c09a1e3 | -3.70287 | -40.42561 | 2025-10-24 04:17:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e8e71788-24af-3dab-93f4-d02e1998d7d3 | -12.07864 | -46.44189 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a9f4e58-1dea-3df1-a2c3-d1ec263465fe | -12.03536 | -46.53249 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42675ab7-c765-3a2d-9189-6116f466f6e2 | -2.81617 | -49.14685 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| c6b5252b-c347-38f6-bddf-ec8225e88a4c | -9.23565 | -45.61836 | 2025-10-24 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed53a51f-4abc-35fa-8d5a-2cc6a6b716f1 | -3.48089 | -43.97989 | 2025-10-24 04:17:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a793021-113c-3155-93e7-d147f13c6682 | -11.02141 | -47.91566 | 2025-10-24 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f23237e-5ca2-31e1-acba-1dec203497a0 | -3.71174 | -44.41643 | 2025-10-24 04:17:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff9f5f18-4d6d-3c04-8d8e-14ada824d205 | -12.25035 | -47.45407 | 2025-10-24 04:17:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7cfe5b32-9677-36b5-a1e2-6197a1bb001a | -6.30127 | -41.8872 | 2025-10-24 04:17:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c16155c8-a403-32fc-afbd-b9f75acf4ffe | -3.47575 | -43.2451 | 2025-10-24 04:17:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| edbd9474-87a8-31c6-b57b-7849f3f6c982 | -9.23364 | -51.8268 | 2025-10-24 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00627304-8087-3ead-8ef5-8e705066a35b | -4.24938 | -48.12685 | 2025-10-24 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ceec6d55-79e2-3823-90f1-6f5895643e05 | -1.54724 | -55.4085 | 2025-10-24 04:17:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 427c3b7e-7190-3a77-aca1-de792f21dd7b | -6.12799 | -41.72189 | 2025-10-24 04:17:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d9034a5e-d4f7-34e4-bd46-229bdf204389 | -11.81922 | -44.16348 | 2025-10-24 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3850dfa-0726-39d8-a2f5-5854e66f6cf4 | -10.86969 | -44.41043 | 2025-10-24 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2bfafaf1-8d7d-37c4-bbee-b908019c0d56 | -3.51284 | -45.83835 | 2025-10-24 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69f45298-68c9-3810-9784-07e0eb846952 | -12.06959 | -46.43243 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bb68e5e0-af4c-369d-979a-660c97e3761d | -4.28375 | -40.70425 | 2025-10-24 04:17:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f7be1ef7-c6ff-3abd-8151-e936e893aaa9 | -4.91381 | -47.32524 | 2025-10-24 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 92e12106-2200-334f-9223-2165a37b4060 | -4.2485 | -48.55397 | 2025-10-24 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf3c26c4-902f-3474-b338-90da9af3f2fd | -10.96226 | -45.07869 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbd671dc-be50-3e22-bc79-40b34d994d76 | -3.47944 | -50.07521 | 2025-10-24 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81652c55-c46e-31e2-9867-4620d3b91775 | -11.16695 | -44.68994 | 2025-10-24 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a68b93fa-cd45-3834-b71c-dcce7506c864 | -12.65003 | -44.1234 | 2025-10-24 04:17:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83c3ad73-20de-3ca6-adfa-107c760e1e76 | -9.87317 | -47.72886 | 2025-10-24 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3bcdba0-0b24-3e37-8c35-cc8165405c97 | -12.29735 | -45.52979 | 2025-10-24 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9ed34bf-5a89-3fd4-9cc3-c9ae1106ae6a | -6.53854 | -43.9663 | 2025-10-24 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ee4f2ba4-a96f-306a-9cd0-de0dd6fce8b8 | -5.47806 | -48.86784 | 2025-10-24 04:17:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c9f6a5a-b43b-3e0c-8e79-999a64b7e450 | -6.44703 | -43.81885 | 2025-10-24 04:17:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| df1ce2a6-037e-3fab-819d-227b2362c9a3 | -3.44194 | -41.85172 | 2025-10-24 04:17:00 | NPP-375D | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 415cb790-404d-380e-967f-a80d05da8358 | -6.51804 | -37.48439 | 2025-10-24 04:17:00 | NPP-375D | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 20805838-a8f8-3925-9dd5-2a5f8899525d | -4.14175 | -47.65921 | 2025-10-24 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b464d0f1-0ffb-33e4-871e-65ce65937191 | -2.94937 | -51.53089 | 2025-10-24 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e892e050-307c-3d6d-87bb-6fd5d1af7c9c | -5.6237 | -46.43293 | 2025-10-24 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72dccec1-ae08-3bfc-b236-8225ce797875 | -10.01065 | -47.09109 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2d4b1b56-a3b2-32b8-8527-ff4867621070 | -9.26841 | -46.45016 | 2025-10-24 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd5fd2c2-7ca2-3c28-877c-5475f39066df | -11.37106 | -45.93881 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76a9449c-8b0d-3b96-9b89-a849a16b2bca | -5.42739 | -40.88303 | 2025-10-24 04:17:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a1e1213e-eb70-39f4-86e7-283830651974 | -6.84191 | -41.55052 | 2025-10-24 04:17:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 54680583-58e8-3d2d-bbc2-39c94a529b90 | -3.78654 | -43.90558 | 2025-10-24 04:17:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ced06b2f-c233-3f6f-85e1-8a8f68c7fcc7 | -11.09531 | -41.61462 | 2025-10-24 04:17:00 | NPP-375D | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0ed9838a-091c-31da-8c73-1c846c63aa6a | -12.09824 | -47.00034 | 2025-10-24 04:17:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39cb2504-d2a2-3473-8472-0406fbf4c915 | 1.19222 | -51.06008 | 2025-10-24 04:17:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48b2f3bb-bb3a-38b4-b039-79d325c67256 | -5.83958 | -40.79737 | 2025-10-24 04:17:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fedd0a84-7ca6-33b4-bac5-9f7e40af00b9 | -3.85338 | -49.13119 | 2025-10-24 04:17:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 90269553-785f-384b-8f19-4b30f3322937 | -9.93305 | -47.46513 | 2025-10-24 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36eee899-e095-3c68-ba75-dad059bd00ca | -3.22528 | -49.36279 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d51b8159-92d3-3e1e-b9bb-ce953cb781a3 | -8.82835 | -45.4166 | 2025-10-24 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README22.md)
