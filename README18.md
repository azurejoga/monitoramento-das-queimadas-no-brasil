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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c67f4ea-2456-37c3-850b-1ac746fc7af0 | -6.88458 | -43.75349 | 2026-08-22 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 17c682bb-4339-304d-9862-c9a55e24822e | -4.72126 | -44.33981 | 2026-08-22 04:25:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cb71a59a-b9d5-3f12-8351-e227fa8dc90b | -3.26741 | -49.52221 | 2026-08-22 04:25:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 931a7651-1f5d-3a34-8aff-90599258ee46 | -5.61755 | -45.7156 | 2026-08-22 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 513f782c-9b54-3332-bd23-b4457ee4bb48 | -5.58508 | -44.01029 | 2026-08-22 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7041a1a8-ec2d-36de-9a02-93a5b41fe017 | -2.8922 | -48.79198 | 2026-08-22 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 693e5492-a939-31ff-86b0-7b93962592e7 | -6.78361 | -42.87081 | 2026-08-22 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 63aa0ad1-179d-31b7-92a9-c72df4279869 | -6.75421 | -47.12508 | 2026-08-22 04:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 659174e3-3469-347a-9b37-66bd1d7067c1 | -5.6034 | -44.02392 | 2026-08-22 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91e25a0b-6f10-3a1d-8efa-bc26b3330eef | -5.5966 | -44.00429 | 2026-08-22 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 213a687f-7cf7-35bf-8fae-2c40ba9d59a3 | -2.50184 | -48.13806 | 2026-08-22 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e7f9e053-ff2b-32a0-9fdd-dd2d5689016a | -6.23865 | -44.85511 | 2026-08-22 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4723774f-e786-3562-a815-a79644ecad01 | -4.65373 | -42.42976 | 2026-08-22 04:25:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cd13a130-4127-3144-a594-0506fce6cbd7 | -6.9183 | -44.96943 | 2026-08-22 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a120495-4b43-3228-b88b-f367d29793c5 | -5.79589 | -50.16551 | 2026-08-22 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 568c29e5-1f97-300d-a187-63121c8b143e | -2.45348 | -48.55835 | 2026-08-22 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e2d10b3c-ff10-30c9-bedc-38b85f27357e | -5.60006 | -44.0048 | 2026-08-22 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23d7800f-6975-3b1c-921c-5f0d3eeb386b | -5.96668 | -51.96652 | 2026-08-22 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9ba7fbf8-ab52-3fe9-94c3-c9e1165b7dfc | -6.24374 | -43.68349 | 2026-08-22 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a10f95c-5a17-302f-9077-20c90670f54b | -6.8781 | -43.74846 | 2026-08-22 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 089c30e9-dc02-37bc-83ed-a061f99befb9 | -6.24726 | -43.68402 | 2026-08-22 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c508ba0f-9c24-3221-b7aa-cf32309f3196 | -5.75061 | -53.58348 | 2026-08-22 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 129acf2e-5526-30c2-9608-4a59408c41df | -5.71499 | -46.18349 | 2026-08-22 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c4be0e8-6e63-31fe-90fb-18c4cbe60ed3 | -3.3619 | -50.66932 | 2026-08-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8d0d8ce6-8f2d-365f-b7c0-e2a3308b3285 | -4.26583 | -48.19464 | 2026-08-22 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32ece2f3-c3cd-3f06-a305-dfd380e85340 | -3.03501 | -48.41197 | 2026-08-22 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 71a51e33-fed6-3b1b-a539-6fbc945aa4df | -3.66298 | -43.39283 | 2026-08-22 04:25:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ce15d01-fa4b-31d7-83fd-75283f399efd | -5.96309 | -51.95834 | 2026-08-22 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b94013fa-6362-37ef-9a54-12263b17f04e | -2.88575 | -42.95424 | 2026-08-22 04:25:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e397f193-7956-3f6d-bb8e-c72670701239 | -6.8787 | -43.74447 | 2026-08-22 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6f3d215c-887d-3442-9c1e-a05eea67b258 | -5.62632 | -45.70278 | 2026-08-22 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eab1c09b-9e79-3b2a-8e0d-ebec1b9bbde5 | -3.53855 | -48.18194 | 2026-08-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d8a10c8d-0c03-3f02-97d2-1af209d4e5b2 | -1.82604 | -47.89241 | 2026-08-22 04:25:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a6bdc25-50e6-33ab-8c33-a7ba64bd40ec | -6.88223 | -43.74501 | 2026-08-22 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 75ab8502-bb38-3766-ada1-496edb249cfc | -5.55381 | -43.43406 | 2026-08-22 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0714ab5b-54b0-3639-b433-73e34e86b79a | -5.71775 | -46.18745 | 2026-08-22 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbc3e14a-27d9-3901-b278-f242831d4fc2 | -5.60397 | -44.02011 | 2026-08-22 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 48cb8fd4-32a4-3bc5-ada8-b77ae52d1524 | -5.58682 | -43.99894 | 2026-08-22 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55679bfa-0337-3741-9504-24d6fb3c600a | -3.53795 | -48.1858 | 2026-08-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d90a043f-b0b1-35e9-9461-ff47b9e35c54 | -6.91719 | -44.97668 | 2026-08-22 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d25cedae-c059-31d5-b130-2f186533f164 | -3.21506 | -48.93665 | 2026-08-22 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d0243b7-2f25-3871-8467-1c9897fcf595 | -4.69271 | -42.54629 | 2026-08-22 04:25:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f34c9ff6-7cb7-3d39-880d-92c34429a0c4 | -1.59698 | -47.35856 | 2026-08-22 04:25:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a245d30c-477e-3eed-a870-868978d3dc2c | -5.60283 | -44.02773 | 2026-08-22 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e010fb76-eabd-33ca-ba35-6517c071f791 | -5.84774 | -46.11639 | 2026-08-22 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 443a841f-4ae2-3149-955c-0c9a2057429c | -6.87636 | -43.73589 | 2026-08-22 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1f174bbe-861c-3e7e-b95d-6058689e3d3e | -6.8893 | -43.7461 | 2026-08-22 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 043a1cf9-754d-3591-ab7c-6d81eb31859f | -3.26668 | -49.52674 | 2026-08-22 04:25:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3aa5796d-b8e5-3432-9266-70c009f125d2 | -5.28638 | -44.03502 | 2026-08-22 04:25:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e98cc10-d5a1-3795-9c83-d81323c63eb0 | -5.60059 | -44.02431 | 2026-08-22 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2970e7f4-62ea-38c3-b453-de79fa8c214b | -3.36323 | -50.66985 | 2026-08-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cda7c26d-58d3-3b56-9bfd-cfde2267d3e1 | -2.45283 | -48.56245 | 2026-08-22 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 748b8748-beea-3eaa-b6e9-36deb824b807 | -5.73079 | -44.52221 | 2026-08-22 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6399a1e4-60bd-3d82-ae08-6302aff8c132 | -4.58631 | -44.75668 | 2026-08-22 04:25:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1bec40a-4708-30e9-8bcd-a544a25d5bfd | -4.86533 | -47.40789 | 2026-08-22 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2baf11ee-dea2-32a0-8105-8eb56946cb1b | -5.96666 | -51.96292 | 2026-08-22 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 258b256f-7e2d-3861-bf24-1773eea351b5 | -7.06853 | -44.99224 | 2026-08-22 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 144a3fe4-d9e3-34e4-bb00-4f87d67b886b | -2.49832 | -48.13753 | 2026-08-22 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2d9b2b6a-c9b5-31b6-abbd-a24a82d89a19 | -7.18271 | -42.7568 | 2026-08-22 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0151a91f-6a98-39ee-8769-84e463be8078 | -4.18307 | -49.40108 | 2026-08-22 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50477f4b-8a95-3635-8d68-007ebdb4f0be | -6.7257 | -48.11568 | 2026-08-22 04:25:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dc174fde-c784-32ce-81f3-6bc78bec82f4 | -7.09121 | -44.66199 | 2026-08-22 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 954bb5db-d38c-38c4-ad03-650ec8729238 | -5.18925 | -35.84686 | 2026-08-22 04:25:00 | NOAA-21 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8059e695-c2b0-3d76-ad1c-27f3c51cbdd3 | -3.53934 | -48.18604 | 2026-08-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9493d9a9-247f-3870-a7ef-43ed04eed34b | -7.06895 | -45.58403 | 2026-08-22 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cb4461f-6101-3160-b845-6b78fb631655 | -5.47534 | -45.11773 | 2026-08-22 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d3e63082-44d3-31ec-8d99-68c72483c7b3 | -6.91774 | -44.97307 | 2026-08-22 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b15b813-9e50-3902-81ca-e4bb68cd6e0f | -1.74752 | -55.25311 | 2026-08-22 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27ee8b3b-f242-32ad-8d8c-4efed13a450d | -6.86872 | -46.00032 | 2026-08-22 04:25:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c990216c-8cb9-332a-a9ea-5d44c88acced | -5.59373 | -43.99997 | 2026-08-22 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c9b1be25-41b2-398d-9411-725866dece50 | -4.91748 | -37.48878 | 2026-08-22 04:25:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0c733fc6-1ba7-32ed-a864-ae59cd088cb5 | -2.89582 | -48.79255 | 2026-08-22 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e1dd43c8-13eb-3a28-bab3-7d871af252ef | -4.94183 | -55.78455 | 2026-08-22 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 818b0c06-9663-3765-bffc-814a37450afa | -5.96733 | -51.96265 | 2026-08-22 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6e600deb-bd0e-3ac4-9175-1a8875ad3bb4 | -7.06909 | -44.98866 | 2026-08-22 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cdef04b2-f56e-3ce7-a6d6-0d0be94d46ad | -7.18645 | -42.75737 | 2026-08-22 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f6bdd92e-586a-3d53-8e59-c39d338eeeb5 | -1.20716 | -47.88856 | 2026-08-22 04:25:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42b119d2-030e-35a4-a235-0a58c930d442 | -6.37848 | -43.23771 | 2026-08-22 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a7ce03a-e311-3e5e-b544-23ba8297f25f | -6.89224 | -43.75061 | 2026-08-22 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f4a38d83-6aad-33e8-91ca-df84770047f0 | -2.89598 | -48.79987 | 2026-08-22 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 663b05a8-2ab1-3b13-bffe-a4d5498afd04 | -4.27337 | -48.19193 | 2026-08-22 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bcc6fc21-ab0a-3b7b-a93a-3ca265682acf | -7.08484 | -44.99866 | 2026-08-22 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 94d6cf5e-5d3e-3b67-879a-f4d83e6ff074 | -6.35001 | -44.07612 | 2026-08-22 04:25:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7cc986a5-91fa-39a9-97df-fc25cc4e5f3f | -4.4699 | -55.39528 | 2026-08-22 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 672cef99-6295-368e-9ae3-3395028f8354 | -6.75034 | -47.12804 | 2026-08-22 04:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5cdfdd4-eaf0-3e3b-b1a2-7f176e9f884a | -2.89665 | -48.7957 | 2026-08-22 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2bd82ef5-b27a-3458-96b9-e0d742305142 | -2.82963 | -48.65072 | 2026-08-22 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 56b236a6-6df9-3c46-8c83-f5c548d7ed34 | -4.17939 | -49.40051 | 2026-08-22 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa844b40-051e-3698-8bcb-e301b524afc0 | -6.21455 | -39.81228 | 2026-08-22 04:25:00 | NOAA-21 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c77f3938-8a22-38e5-b83b-6ce0d6681ca1 | -6.87282 | -43.73536 | 2026-08-22 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7e94beb-bf76-3f23-b4f4-cb70fb71105c | -5.55734 | -43.43462 | 2026-08-22 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 243525ce-0138-3894-b64f-e6df6b6b4dd2 | -3.05766 | -46.92758 | 2026-08-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6ea82d6-7409-3180-acd9-0e7cd4b149b1 | -6.78806 | -42.67407 | 2026-08-22 04:25:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| bd8035cc-071a-34e7-8eac-97f8ef18bad4 | -3.42201 | -43.16441 | 2026-08-22 04:25:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd3b2b59-220e-34dc-8195-dd32232130f0 | -7.08092 | -45.00168 | 2026-08-22 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 51439d46-c9c4-3d86-b07b-b5e274824a8d | -5.14363 | -38.04821 | 2026-08-22 04:25:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1537aa22-fea6-37ae-8b37-a556476de0fa | -7.14482 | -43.11031 | 2026-08-22 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5f066fd5-f140-3578-9339-fc770e6094fe | -5.74977 | -53.58847 | 2026-08-22 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3fed06f3-8b79-37a0-89c3-fb8acfcdb940 | -5.58566 | -44.00652 | 2026-08-22 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44165c47-e8dc-3235-811b-90c28d97413d | -5.82718 | -43.4929 | 2026-08-22 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |


[Clique aqui para ver as próximas entradas](README19.md)
