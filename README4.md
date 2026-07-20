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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a3d6247-35d0-360f-a9d1-43c0d0a07144 | -10.43917 | -50.21421 | 2026-07-20 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 606ddb42-a0bc-3fbe-ab07-3eecc0061036 | -10.44651 | -50.21156 | 2026-07-20 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 74e4c2f1-c3fb-373c-b9d6-565b4a40092e | -10.44256 | -50.21473 | 2026-07-20 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41f4a5c5-1249-35b9-af13-0bfa0e6b0137 | -11.83217 | -44.77066 | 2026-07-20 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ccbff40-f4b1-3939-9e4b-001079e957dc | -11.83621 | -44.77648 | 2026-07-20 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5a22c46-1642-3d85-b665-1aabf989100c | -5.63171 | -47.10292 | 2026-07-20 04:46:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d51d97a5-449e-363d-80d3-f1d252e82e4e | -10.80127 | -50.22727 | 2026-07-20 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f863cf8-e862-3257-9e41-3184af223509 | -10.68488 | -49.62053 | 2026-07-20 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 735eff95-efde-3c5f-8eb4-6e95e7c541d1 | -9.09645 | -59.40231 | 2026-07-20 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bf1d31b1-9ef8-3aa6-aece-e660ec8faad3 | -7.91152 | -48.25986 | 2026-07-20 04:46:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d55333ad-1299-37a6-a312-92cd22e6c9d3 | -10.46914 | -49.09657 | 2026-07-20 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 79592f2c-ffce-3a29-b900-9b464b902604 | -10.87783 | -50.16207 | 2026-07-20 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2d0e976-7857-365e-aca9-9f50c8dace0d | -5.73462 | -49.09414 | 2026-07-20 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1993e459-91e5-3282-a03d-e95ba7d16958 | -9.09738 | -59.39709 | 2026-07-20 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b9f1146-a3ab-3414-a8f4-0218e65337f2 | -7.91511 | -48.26043 | 2026-07-20 04:46:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8dbe124f-7b62-3020-8e8e-537f8004a465 | -11.79807 | -47.10298 | 2026-07-20 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4db79665-9ea1-313b-a306-fa79316f2bc8 | -11.26646 | -49.94935 | 2026-07-20 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a074a659-bf44-3272-95d7-19b73622792e | -11.80317 | -44.32505 | 2026-07-20 04:46:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1140affb-4d57-372d-93f0-29372a35f9f4 | -7.9145 | -48.26456 | 2026-07-20 04:46:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5b6ef6a3-5633-35c1-b817-c696c01475cc | -9.1022 | -59.39791 | 2026-07-20 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa6b16e2-ad91-39d6-8b0b-6e5ee43519b2 | -5.79847 | -45.11441 | 2026-07-20 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1da2121b-93fb-3b55-8567-8a326b785778 | -10.79787 | -50.22674 | 2026-07-20 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b56b2ae-75a4-33be-bbdb-bfc3f2798c7b | -10.68835 | -49.62106 | 2026-07-20 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1c3b241-4726-3d8a-9d7d-551adc5e60d5 | -10.43862 | -50.21791 | 2026-07-20 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d28dbf0-581d-32ed-981f-ef5c27939913 | -10.55479 | -56.34119 | 2026-07-20 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2c2aa2d5-4a9b-339e-a055-20d7d07e184f | -10.6866 | -49.60888 | 2026-07-20 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ea30619-9f05-327a-adb8-1901e18a51c2 | -6.7417 | -47.21533 | 2026-07-20 04:46:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ec00abe-bcc5-3e7f-9744-529aad3c6305 | -10.93325 | -50.30389 | 2026-07-20 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 853c9cef-031f-387d-8077-2feafd3a28ce | -10.80182 | -50.22355 | 2026-07-20 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3dd1382a-9364-3c07-bf59-bd436ec633dc | -10.46854 | -49.10059 | 2026-07-20 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2e1315d6-0121-311d-b8ee-b97b3f91d463 | -11.38696 | -47.50113 | 2026-07-20 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8991c3b4-3676-3e66-a207-1835004cd36c | -9.11699 | -48.82092 | 2026-07-20 04:46:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7874122c-2353-31a3-9fa1-4b0f87ae5f4d | -11.39414 | -47.50696 | 2026-07-20 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e7beabb-5c10-33bc-bdcb-cba3e7de4675 | -10.55562 | -56.33637 | 2026-07-20 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6bba7b5-962d-3b2b-8586-dc5139b68f25 | -8.82727 | -48.33487 | 2026-07-20 04:46:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d0a066bf-af46-31fa-a4e4-f74dea336561 | -6.73796 | -47.21476 | 2026-07-20 04:46:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 148079a6-84fd-3255-a56a-f5ea1ce0ee3f | -11.80167 | -44.32128 | 2026-07-20 04:46:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a775c74-62a8-3078-b2db-341ecdbde151 | -7.11892 | -44.0303 | 2026-07-20 04:46:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88d28df7-9865-34d1-a19a-611002dc8128 | -10.21511 | -48.87767 | 2026-07-20 04:46:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 480fdab8-fddf-3bda-81df-620d65f14dc5 | -10.55261 | -56.33092 | 2026-07-20 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85fbfe0d-b6e9-35cb-b9f8-90a1879465ff | -9.55573 | -44.89822 | 2026-07-20 04:46:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5be5824d-5e0e-3e1a-b62c-85b19ba6415d | -10.44706 | -50.20787 | 2026-07-20 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b40f5a61-f702-353d-ad81-d36997a8f5c7 | -7.1196 | -44.02528 | 2026-07-20 04:46:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a06bd7c5-a108-3f47-b6d5-3a633ce3c73b | -11.3902 | -47.50662 | 2026-07-20 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c013dc66-74bc-3b70-a53d-368ed3ff93b5 | -6.72218 | -48.11377 | 2026-07-20 04:46:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4abcddbb-f007-37b4-84aa-a6e7c0fe1d1b | -11.17625 | -54.11454 | 2026-07-20 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbd0f904-152e-3bbb-a405-44706d4ea6a8 | -10.87775 | -50.15902 | 2026-07-20 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1bc41694-759a-3cdd-a397-4c8a3f38b829 | -8.09777 | -43.66286 | 2026-07-20 04:46:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 17cf32ad-d340-3534-8ee8-5ca1289a1128 | -9.87418 | -53.32465 | 2026-07-20 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6a3e03e-1811-398c-8531-542018ece79e | -5.67242 | -43.57534 | 2026-07-20 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e8c2b3b9-ea33-374c-8fa0-0870b53282d4 | -7.29879 | -46.24643 | 2026-07-20 04:46:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eaf65340-f5ca-3439-84ca-e8625820595a | -7.30279 | -46.24704 | 2026-07-20 04:46:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72617431-4028-3848-beaa-7833ae07eb8a | -9.51292 | -46.67722 | 2026-07-20 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 637d9e4f-5d24-3638-9d48-255da5623d68 | -10.87839 | -50.15833 | 2026-07-20 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75c4de28-a122-3fd1-92d9-cd5299db9d3b | -10.80523 | -50.22408 | 2026-07-20 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66357f9b-bdd8-311e-8713-a2f5e6c2bb42 | -11.83298 | -44.77681 | 2026-07-20 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af8b660a-4871-3a76-ae07-ce10689fa73e | -6.59294 | -51.70224 | 2026-07-20 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97129872-8bf7-33f5-bcfb-2ab2cfa4e36a | -11.98065 | -47.10541 | 2026-07-20 04:46:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6e77b333-25d6-34c1-9dfd-2687b9f526ef | -5.71098 | -45.66277 | 2026-07-20 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6b3485ea-a149-3459-9a0e-1b98facc053b | -8.83088 | -48.33543 | 2026-07-20 04:46:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a5a4209-f335-3373-b4f2-a6c81ec6af2c | -8.93862 | -47.60148 | 2026-07-20 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e2db84d-d25d-347f-9e26-7e4f4baaed32 | -10.68778 | -49.62494 | 2026-07-20 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82a1530f-ea2b-3c36-82dd-0a1d7eadb94f | -6.72574 | -48.11435 | 2026-07-20 04:46:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a582c687-f3c6-3978-bd82-1323b86ddd7d | -8.93042 | -47.60494 | 2026-07-20 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7212e00-cee0-3eeb-8c94-092293fd3e80 | -5.67316 | -43.57035 | 2026-07-20 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 78aafc0d-df5f-333b-acb6-0eaba383152f | -10.79731 | -50.23045 | 2026-07-20 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 301f5378-13c8-3957-8d64-cfce426d5d85 | -6.59571 | -51.70623 | 2026-07-20 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2cac1ceb-9f32-3694-82bf-e860b7806757 | -8.93485 | -47.60092 | 2026-07-20 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 218a0f10-7ce5-3229-ab24-efbdc0bf2b71 | -13.37486 | -54.31544 | 2026-07-20 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5177a28b-47a3-3c5f-924b-62e0bb4f33ba | -13.34775 | -54.31091 | 2026-07-20 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07e095a7-e02b-33f0-84b6-98292c8ec063 | -12.00262 | -50.55676 | 2026-07-20 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b52979b6-644d-36da-ad95-7ffd69199b03 | -12.99172 | -62.16081 | 2026-07-20 04:49:00 | NOAA-21 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92e5f8f4-906a-3b71-917b-8ba523855759 | -14.11604 | -46.35101 | 2026-07-20 04:49:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dabd8148-98fe-3487-9787-a8b1f0f983b5 | -16.80905 | -54.59089 | 2026-07-20 04:49:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 75a5c6fd-54ec-3056-8b4e-004b8d318eb1 | -13.68451 | -48.79731 | 2026-07-20 04:49:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cdf3a599-37cb-379e-8ec1-58109e61f499 | -11.61677 | -54.5762 | 2026-07-20 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80e1fb30-7d27-3b53-8943-0aa105f3c1f6 | -11.31659 | -54.47939 | 2026-07-20 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ae47b94f-8e6b-364f-ae44-8a77b11bd3d8 | -13.69196 | -48.7986 | 2026-07-20 04:49:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0992b573-f944-3835-be6d-0d6d79391fa5 | -10.90806 | -56.37075 | 2026-07-20 04:49:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c5c30a32-9ffa-3506-8bc8-783ffb39ec15 | -11.99471 | -50.56314 | 2026-07-20 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7cfd9b1-6bed-3425-8259-2fa5987548b8 | -16.64633 | -49.53242 | 2026-07-20 04:49:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d63f44f1-5372-339e-8c99-c0b20a9cb662 | -10.90887 | -56.366 | 2026-07-20 04:49:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fac90d63-aa28-3998-9453-2d94baf07a47 | -11.74641 | -57.81306 | 2026-07-20 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9715a65c-50d2-3c21-bdfb-8c48598a2522 | -12.99241 | -62.15731 | 2026-07-20 04:49:00 | NOAA-21 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9bbf1a95-55d5-3679-9327-b9b3ba44f75d | -12.99848 | -62.15491 | 2026-07-20 04:49:00 | NOAA-21 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05c6073a-ab93-35cf-9a25-96c0a9b98dde | -15.46464 | -54.35268 | 2026-07-20 04:49:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82e9acc6-0a62-38b6-938e-088e703f3595 | -13.56296 | -47.77323 | 2026-07-20 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cf6fca3-7eff-32a6-974c-4fbacdc56418 | -16.80571 | -54.5903 | 2026-07-20 04:49:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e345a58-3c2d-368d-aa28-683e9ef1454c | -13.67894 | -48.79896 | 2026-07-20 04:49:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e70d8338-3ecd-3759-9f28-253290b80347 | -16.62618 | -49.39088 | 2026-07-20 04:49:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ba7ba14-b729-361d-b935-30ad196ddb68 | -10.90505 | -56.36531 | 2026-07-20 04:49:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6306259e-a984-3451-82c3-1a4e7e2db481 | -13.68823 | -48.79799 | 2026-07-20 04:49:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4b9a5fe9-1193-3f9e-b8a5-97ca3b8fc85d | -12.94995 | -44.72998 | 2026-07-20 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9ff30a1-ee1a-387d-8fc2-fc0cdb1483a0 | -16.60654 | -54.49542 | 2026-07-20 04:49:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28b572e1-c438-3f33-b0cc-e708c2ff1473 | -14.11659 | -46.34959 | 2026-07-20 04:49:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc3b9add-a48d-3ddb-804a-b871fa4a42f2 | -13.35113 | -54.31149 | 2026-07-20 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a615e7b-624f-3d7d-823b-e202cfe5df88 | -14.75734 | -48.40513 | 2026-07-20 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f15bbc93-502f-3afd-b6fe-9b5758ea012d | -13.29494 | -44.618 | 2026-07-20 04:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54f09c0f-2456-3acb-959a-e4c39d5d3a3e | -11.74294 | -57.80851 | 2026-07-20 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a046152a-45c0-3fe2-a02b-d77196d5d03a | -11.6133 | -54.57562 | 2026-07-20 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README5.md)
