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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e72b5063-b9d3-35f7-ab04-224406659217 | -5.26963 | -49.26535 | 2025-09-07 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27a92fe0-cdec-3a24-9bfe-9b36f7831ff3 | -7.73157 | -44.72229 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f9d498c-be9a-3d86-9c35-055d57808950 | -8.91733 | -45.81682 | 2025-09-07 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a249fb1-d1aa-333e-a4d5-ae51ab70d23f | -6.27112 | -53.43516 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10c4e6af-8dc4-356e-9de8-73d30fdb9a51 | -10.83514 | -55.10355 | 2025-09-07 04:19:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9a9ff8a-4f7e-3c68-ace7-2c84be0bc435 | -6.19514 | -53.25114 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d952073-433d-35bd-9718-821a2bdade52 | -11.1477 | -48.36798 | 2025-09-07 04:19:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3d5f882-975d-3065-9804-fb046f67757c | -6.22875 | -42.65185 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 777af053-9547-3354-8e55-70b8031be8b8 | -6.51852 | -43.06994 | 2025-09-07 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| beefbf8a-b13d-3b02-966e-0ad29e62d414 | -6.16653 | -44.2445 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f2710b5-33f8-3f9d-915e-b63a1d5333b1 | -6.23282 | -42.584 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d941f950-8bd5-3655-a886-9c06d8618bf9 | -6.59385 | -43.98696 | 2025-09-07 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41c85e1b-5474-3e14-86b5-c32ac1424460 | -6.17552 | -44.31686 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06d670dd-1b36-3c3b-a5d4-19506707ab50 | -6.54109 | -44.82109 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6a603b4-97c4-31d8-aea1-edd27fb2935e | -12.012 | -47.7842 | 2025-09-07 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80b7ea46-f395-3983-890f-ca7769c6c7bf | -7.40262 | -44.97898 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ccbf4755-1f7f-3687-9997-06a49da7074c | -6.5999 | -43.96998 | 2025-09-07 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd6178c4-228f-314a-bb25-aca27e2f4e56 | -7.45664 | -42.03439 | 2025-09-07 04:19:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5a80a8ec-daf4-3fc7-871e-eb9b1b61fbf3 | -6.59554 | -43.99795 | 2025-09-07 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9ee23e2b-a236-30e0-9830-2c97a1a48fd3 | -11.76891 | -50.64671 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 093b5462-f9c1-30e0-88ec-9b0404ec7659 | -9.83691 | -46.54797 | 2025-09-07 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32890ac3-d40d-3dad-89c2-1c5255a2bba1 | -11.60626 | -47.15828 | 2025-09-07 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3423bd98-fc88-31cd-846f-08d2c803432e | -11.15403 | -48.37334 | 2025-09-07 04:19:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8afc8a33-7571-3ec7-ba69-072ea340a808 | -10.35014 | -46.4602 | 2025-09-07 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f0150b3-eab9-31e2-9fb7-2ac3e4d480ef | -9.77759 | -46.89638 | 2025-09-07 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5ee820d9-ab0b-3884-9b12-30d789d0e8da | -10.1529 | -48.74058 | 2025-09-07 04:19:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fc13dbc6-8195-32dc-b78d-8aa747e9b080 | -9.02407 | -49.80055 | 2025-09-07 04:19:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c2a419c-eda5-3995-8f30-46e90b1d7d9c | -11.73283 | -46.6937 | 2025-09-07 04:19:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f516c520-d6e1-3592-8e10-e8561389158f | -5.61048 | -48.10047 | 2025-09-07 04:19:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d3e6c23-cc4b-3f74-a7ff-a337b7643c0f | -5.82887 | -44.12343 | 2025-09-07 04:19:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1f3e5506-996c-3e91-809d-11abf88a3aba | -6.23135 | -43.31124 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2d93b334-ee55-3f43-9c9c-ee0f8e69f6b5 | -11.32217 | -46.56372 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8f1597d1-f22d-314d-b891-9cd5af19d118 | -7.43619 | -44.93814 | 2025-09-07 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c508b23-9c81-37f7-85a3-5714d67b2877 | -8.18505 | -44.77641 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76dfafbb-19d3-3c49-ba22-d2a787b03ed8 | -11.40553 | -43.63016 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 88547564-0b39-3d6f-83f5-64c3f8e4eb28 | -6.5233 | -42.42086 | 2025-09-07 04:19:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| fed1d7fa-fe59-3eae-8d95-61477802e46a | -8.49253 | -45.10976 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac8c1c5b-5ef0-3091-9fb7-a817d030f32a | -6.89203 | -45.54222 | 2025-09-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e3b1675-5fa3-365e-be00-e042f102a3f2 | -6.53717 | -44.82395 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 0d73bd9b-a1cb-3b63-8eb4-456165570ae0 | -11.22368 | -55.01735 | 2025-09-07 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c3ad5f5-638e-3e28-8e0f-54f2b1079075 | -11.00617 | -52.05409 | 2025-09-07 04:19:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bc6614d7-6abf-3fa0-9e25-6dd22c7783bb | -8.0846 | -44.81009 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 492a62f3-fc00-39af-9ca1-4ccd248036db | -10.76974 | -48.26628 | 2025-09-07 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f12a544-5cb6-394b-b183-9d20e6621398 | -8.8923 | -47.25327 | 2025-09-07 04:19:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 890923f9-39b6-3a07-9279-48dc5b0ea073 | -7.63049 | -46.55438 | 2025-09-07 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a4e045c-ab05-3f48-ba43-5191c39014b3 | -8.15419 | -44.86384 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ebb097a1-5303-3e21-a443-5c1791c9e2a7 | -7.81377 | -45.42841 | 2025-09-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2903a644-bb51-368a-b631-8ecccc0f70a6 | -8.2919 | -47.43445 | 2025-09-07 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03ab385f-459d-3ce3-bf1d-97571867b0b9 | -13.01396 | -41.41966 | 2025-09-07 04:19:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| df82900e-5e04-3572-8dac-8a8cbb772dda | -5.95012 | -46.16499 | 2025-09-07 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d72b0a76-728c-3f0e-8ea4-29a64d9d1d6f | -6.24364 | -43.51082 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 73edcde4-8a73-398f-a0a0-cb372bbdcb77 | -11.94221 | -46.65875 | 2025-09-07 04:19:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9f5f9935-ffb7-32a5-95d2-ba18a43ad1b0 | -7.2888 | -39.21807 | 2025-09-07 04:19:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3c5f7fc2-d6c1-3ae7-860a-8e6699c49f29 | -6.1806 | -41.84576 | 2025-09-07 04:19:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 60e53b90-9cc1-3d05-9983-b4653bf30c6a | -6.20634 | -42.61845 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c0f1697d-af0d-3882-b3e3-81e529fed4e7 | -6.60291 | -48.05947 | 2025-09-07 04:19:00 | NOAA-20 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f3566db2-5472-3e42-a5d2-02df32b6c4f8 | -6.20634 | -53.24736 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b5a41e68-75db-32d5-a47b-e9742f3444b0 | -6.23304 | -43.2784 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 54805860-ef8e-33c0-bc11-4fdb84735e60 | -5.79686 | -45.6563 | 2025-09-07 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9a03e80e-830e-3835-8a1d-ada02ae1dd2e | -6.20631 | -42.64137 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 485a90f8-a813-3637-b49f-a38bea547f32 | -5.8399 | -44.11803 | 2025-09-07 04:19:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e4016a6-acad-3390-abfb-60cd390d92ce | -7.83647 | -44.94122 | 2025-09-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08e4ffb6-a5ae-317d-a84f-938f61b399fe | -8.46141 | -47.33577 | 2025-09-07 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8e143502-d431-37bf-ae1b-82ef69557797 | -11.3023 | -46.53869 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16949e0d-1659-3987-9128-931f9ad10f58 | -8.50025 | -45.10387 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24811f27-3f0e-3be2-bbc7-d513990adde1 | -6.2336 | -43.27482 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fef70972-86dd-3e0f-b455-8891ddbf6c3b | -12.87999 | -47.99198 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| afc3eb01-7d5d-3902-b769-ce719d2319f1 | -6.19715 | -42.63235 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 98c83566-c76b-39ce-b1d4-7f68f50ba1b9 | -5.85285 | -45.30515 | 2025-09-07 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca63814c-fcdd-3b8b-9b2a-912dad863a5c | -13.01241 | -45.22524 | 2025-09-07 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75c7c7fe-02d8-35c6-bfd5-59dad6f1604b | -8.11356 | -45.3166 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c5158dd9-0d03-3f16-aefa-1ae8e127c9a1 | -8.18511 | -50.13836 | 2025-09-07 04:19:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60fbf628-756f-33ac-a4a8-7b2e1f521250 | -8.68795 | -54.67154 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5bb66d78-3520-3dec-99cd-ef65816bdba6 | -8.45859 | -47.33139 | 2025-09-07 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea350e59-16db-34fd-a876-f1ea378b1d9d | -7.74234 | -48.81312 | 2025-09-07 04:19:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a7a5d2e-0971-380d-b393-f9a8476da102 | -11.21716 | -55.02282 | 2025-09-07 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6f00ebd-4817-3b87-98b8-89c106db6948 | -8.08845 | -44.80713 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e4a4deb8-7600-3a9c-8962-9759f910d0bc | -11.40495 | -43.634 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 32cfed64-d079-3e44-9207-c6a177f611fa | -11.29509 | -46.54113 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 980019be-2365-340d-ac96-8e1cfb66edf8 | -9.45482 | -56.03988 | 2025-09-07 04:19:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b78b6f50-d726-32df-8dd8-ac1a22fd8984 | -8.4444 | -45.02737 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f165a02e-5ff4-31d8-ac18-2c9d2711c887 | -11.76153 | -47.75018 | 2025-09-07 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ae155ca-f512-348e-8c89-576f92d12daf | -7.80881 | -45.43832 | 2025-09-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5eeddb03-3bb4-3524-9210-ced69eeb8472 | -6.79516 | -50.8464 | 2025-09-07 04:19:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c055904-39c6-3a5e-89e1-ea636ca41253 | -9.41025 | -46.76631 | 2025-09-07 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7bc84bc-6db6-3ea6-b37b-315b466dc5e1 | -8.11467 | -45.33103 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 538fc975-e926-3393-9683-920d066571bb | -8.50019 | -45.06112 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41ffa0b2-a03b-30d2-a549-4468bec023f3 | -6.28147 | -53.43698 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60b886fe-d9cd-34ab-9f20-d6b5d9841e04 | -6.85189 | -45.92189 | 2025-09-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd3161e6-ec1b-3e48-a2ba-f44781d1144b | -6.93478 | -44.32555 | 2025-09-07 04:19:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee92847c-d401-329e-b4d7-140856ab3c23 | -11.16793 | -49.93441 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7d8fa95-c394-37d3-a4aa-f968c75c0f6e | -6.23223 | -42.58776 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| aedfd64b-dced-3f8c-870f-8b72b98cde17 | -7.0194 | -44.97483 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afc141cd-9dd7-3e32-962f-079144cb71e8 | -11.94108 | -46.66583 | 2025-09-07 04:19:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 377e8a75-5342-30e3-a0bf-177cbea8a99a | -9.72312 | -43.97816 | 2025-09-07 04:19:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 23563fe5-c235-39e5-9fbd-0c64f55ff97f | -10.74074 | -44.35357 | 2025-09-07 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6692c22c-a3ea-3386-b867-7dbc63eb2f75 | -11.58753 | -47.17789 | 2025-09-07 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4df8963-524f-3342-a935-3c4d1ff47c61 | -6.27683 | -53.43297 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ba7d930-fffb-3e6c-bcc4-e52ae50f3af6 | -13.00907 | -45.22471 | 2025-09-07 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5900501-2712-3dca-b807-ae532e94b404 | -9.79647 | -48.51437 | 2025-09-07 04:19:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README53.md)
