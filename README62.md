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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 536d77bd-147c-3cec-ab8c-6e43daab8b3d | -2.74732 | -48.607 | 2025-09-16 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf4231ba-0feb-3d37-882b-2e507ba8de24 | -6.18617 | -43.47345 | 2025-09-16 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c50e66d-bc01-3b2b-8eae-9ca57fff1d10 | -7.46055 | -46.14813 | 2025-09-16 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d56cfa9-1e51-32b4-8a12-ade761cdd69f | -3.65024 | -54.0632 | 2025-09-16 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8aa1752c-7587-34ed-9245-1100839242b7 | -3.74207 | -49.04923 | 2025-09-16 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0b8e1529-9d07-3a10-9e49-995612a8126d | -8.17761 | -47.13367 | 2025-09-16 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f56957b-19a9-3e9b-9d4c-47c45e72c68a | -6.12457 | -53.80413 | 2025-09-16 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e808d19-0591-3010-bf10-3c1f6c5c2886 | -6.35643 | -43.16237 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93682770-0206-3988-89dd-aa1b6ffcfc63 | -5.00341 | -47.64291 | 2025-09-16 04:49:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40deebe4-2951-3949-983c-a904621f5efe | -7.27709 | -46.5859 | 2025-09-16 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d65d7bdc-0d71-315a-9976-7f81d280a795 | -7.40062 | -49.9968 | 2025-09-16 04:49:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 055eca4c-8654-3d45-b8e6-c6e75104048a | -3.83743 | -44.10377 | 2025-09-16 04:49:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f3dcdc1b-737e-371e-892a-7e6edce829b6 | -6.52406 | -41.82398 | 2025-09-16 04:49:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 047417d5-0b66-3f2a-b195-960d68a5dbdb | -5.78467 | -43.94825 | 2025-09-16 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f0df892-5182-36e0-9bcc-639f118172cb | -5.98729 | -45.84629 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ecc69a5-9081-36a2-bfab-453023124548 | -5.22677 | -43.69821 | 2025-09-16 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bf0fe0ca-607d-3e0d-aef2-382482786df5 | -7.54473 | -50.48183 | 2025-09-16 04:49:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 312c077e-ca9a-3363-a76e-9624dae8bfcc | -3.95423 | -49.4353 | 2025-09-16 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4359f76b-20b3-39ab-95df-f3b83f72204d | -3.42403 | -43.15212 | 2025-09-16 04:49:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c1c7432-a749-3211-9701-b0ba37e8dd6b | -6.37091 | -44.41448 | 2025-09-16 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39a8abab-9ecf-3bd4-95a3-cfd0e267da62 | -6.82788 | -47.84715 | 2025-09-16 04:49:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 26de8497-a9da-3f54-9dc5-08d7ce2672a9 | -3.40553 | -46.90417 | 2025-09-16 04:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f07a059-39f8-3b4f-af41-dd9a2bbde7a0 | -4.49307 | -50.50272 | 2025-09-16 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0fb01be-98f2-3ddf-8530-6e87b4998153 | -5.53784 | -42.65698 | 2025-09-16 04:49:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| da8043ea-e5bc-3c68-9a1c-129632e4743d | -6.26097 | -43.47261 | 2025-09-16 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a281d3e-5850-3383-8311-5ead41484304 | -5.76788 | -52.36739 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12564354-adf6-34e6-9a89-f84740cdaed1 | -6.33917 | -43.16678 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56b4e022-a061-3a43-98d1-3bebfc092dbb | -6.31538 | -47.74098 | 2025-09-16 04:49:00 | NOAA-20 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c534e68f-5c08-33fd-8847-262e625b7824 | -3.21851 | -47.12242 | 2025-09-16 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5ca018b2-c507-31f7-87c6-924d028106a6 | -6.2899 | -42.39102 | 2025-09-16 04:49:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2fd0fa8f-aae0-3604-b73e-0e3479acccb4 | -3.38815 | -50.1486 | 2025-09-16 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3a76975-3e9d-3b89-8f31-b0bad493b5e5 | -6.34012 | -43.15986 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 40f43d90-b06c-32e9-b712-9a5f90ea6ac2 | -4.59527 | -43.31985 | 2025-09-16 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0348bd51-6e40-398c-b51b-4170407e9923 | -5.34326 | -44.82023 | 2025-09-16 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80673bb4-84fa-3bfa-b979-ab5977c27f42 | -8.20419 | -45.55048 | 2025-09-16 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d4eb400-951f-3498-9810-9ed75031a7a4 | -4.73879 | -50.94159 | 2025-09-16 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f360092-4507-3bf9-a8c9-b09205c0ea15 | -7.66902 | -44.47486 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4a9c290-2353-3dfd-b01d-bb1a3fc9d09c | -7.057 | -44.17508 | 2025-09-16 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db61abcb-b92d-3111-a628-26a9e7b54475 | -5.53339 | -42.65688 | 2025-09-16 04:49:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 90f864e2-d779-3dd0-8331-bf98e0b5fb28 | -7.48063 | -47.39237 | 2025-09-16 04:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 876b75b0-cab0-3629-8255-04b04cb697c5 | -5.80261 | -45.69809 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35a626e0-e27b-3067-9526-66e5bbf8ddd2 | -6.33963 | -43.16338 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9626e0b0-e74e-3b44-a8f4-5e41a34774b0 | -6.22199 | -43.90275 | 2025-09-16 04:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3526b48d-2257-3349-91b1-828a21cedadf | -7.36717 | -44.29542 | 2025-09-16 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc76392b-3470-329f-b30e-71a71825d1c3 | -7.63183 | -46.55207 | 2025-09-16 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26f66a8e-dfea-3274-b5ae-56b66a8c862b | -8.11882 | -48.26511 | 2025-09-16 04:49:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c182d7f7-c3fb-3bda-ae28-e049473398a1 | -8.00613 | -45.66934 | 2025-09-16 04:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 90725e96-d517-34de-80f9-9ef74acd3cfd | -7.38287 | -49.99402 | 2025-09-16 04:49:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24244981-8b73-34d0-9551-fb2445e36acb | -6.3313 | -55.85926 | 2025-09-16 04:49:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e581971-cab9-3c3b-a8b9-adcf7b195fe7 | -6.55986 | -54.98273 | 2025-09-16 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e811800b-9708-37ec-91ec-7f02c73b60bc | -3.82101 | -44.11257 | 2025-09-16 04:49:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aad85693-03ba-3c23-bc8f-59a0b8dcd7aa | -5.89483 | -45.7418 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1102b26-3671-385a-9342-50f1b9b57abd | -5.76457 | -52.36687 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97b8d72a-ca0d-3826-bc3f-2ba39163ee30 | -7.6915 | -44.49958 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ed54cc2-20bd-3655-805a-c203bf1a840b | -7.08748 | -44.54868 | 2025-09-16 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8bceb22-e315-3d8f-bdf4-0f0695fd1ef2 | -3.21692 | -49.17535 | 2025-09-16 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef6c14c3-e28c-35e8-bbc1-adcc675a44d7 | -5.78122 | -45.93871 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4601db98-50cf-3832-8787-c54a375c5044 | -3.83251 | -44.10305 | 2025-09-16 04:49:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dfbcdf10-6f89-37a2-a753-15fbaedeeae7 | -7.62804 | -46.54719 | 2025-09-16 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d1e0fa7b-d058-3aea-8cc2-04717f225c4a | -3.85407 | -48.97778 | 2025-09-16 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7400a1aa-8259-3c97-84db-29db67bd592a | -6.44831 | -43.31214 | 2025-09-16 04:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da1a5715-fdc8-36ce-9879-5f1f155ee34f | -7.71701 | -45.30076 | 2025-09-16 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b05da6fe-c40d-3fb6-99f1-bebc627c988b | -7.26276 | -46.5928 | 2025-09-16 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 371f6e76-80ce-3c6c-9e62-6f25e108a982 | -7.13934 | -47.97827 | 2025-09-16 04:49:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f7059f0d-c73e-3efa-b39f-216cf865f911 | -6.99718 | -44.57429 | 2025-09-16 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe48d750-9f91-3ecf-978d-e06d9a77d2d3 | -3.87994 | -52.29861 | 2025-09-16 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f7c2ec5-af95-319b-b445-607a1407107b | -5.79023 | -43.94598 | 2025-09-16 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9f43f436-0aea-3257-b3e6-95490284bb58 | -7.72659 | -45.30223 | 2025-09-16 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ec7e006-dd27-30ff-85c1-dc10f22150e2 | -7.67836 | -46.29114 | 2025-09-16 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e56a8aef-cd92-3caa-b27e-6c53e4d05002 | -3.83411 | -44.10467 | 2025-09-16 04:49:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7b6a0cbf-2918-3dcd-9379-99e0620bd7c9 | -7.69325 | -44.67169 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05c72ebb-75dd-33e6-9749-4c7573a846b6 | -6.39948 | -41.75689 | 2025-09-16 04:49:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0208b9bc-2829-3961-adae-8b59478bf63e | -8.00339 | -45.67014 | 2025-09-16 04:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3849a275-2a48-37cf-ac8d-3dd757903b07 | -6.46266 | -46.0131 | 2025-09-16 04:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 092089c6-4b0b-3b68-87ee-78818eec779c | -4.59527 | -43.32114 | 2025-09-16 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73a6e575-5649-335c-b50f-da1f83153b1e | -3.38415 | -50.24142 | 2025-09-16 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 517cf415-a1a0-3d9c-84e2-7d0623ccaa61 | -5.83545 | -44.15736 | 2025-09-16 04:49:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac1b7ced-4ba0-3841-9f7d-b5f1912ef12d | -6.52265 | -51.18909 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9695c15-45c8-3113-95f4-79a032e3cac1 | -3.92762 | -52.1685 | 2025-09-16 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4ee3b995-eea1-3095-b150-fcf15f545f06 | -5.77612 | -45.9424 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7284ab5-e610-38ee-a868-fd311e7f8d9f | -4.04267 | -49.0765 | 2025-09-16 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3cd9ad8c-c415-3402-979d-ac6ae7bced22 | -5.93187 | -44.87197 | 2025-09-16 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3704d2ec-95c5-381c-bea3-06d13b97eeab | -7.66862 | -44.4778 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bba02fbc-98b7-3713-84d9-2aeb248398b3 | -5.9201 | -45.72718 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eec29b72-9b64-3ca7-b4f8-8b95d17f5c0a | -5.25463 | -44.14465 | 2025-09-16 04:49:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f8bcbae2-fafc-3123-b6b4-b930adaae88c | -7.31696 | -43.95501 | 2025-09-16 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5707833c-e3d6-343f-a937-feebed55e942 | -7.39232 | -50.00374 | 2025-09-16 04:49:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a7f6481-11c6-33f1-9948-fa5d024c5676 | -5.80643 | -45.70362 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90960a7c-00ab-306c-ae46-b546b245915d | -6.17646 | -45.14472 | 2025-09-16 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ed1cf0f5-58d2-3cd5-b16e-011f0ff8de8a | -4.17716 | -48.57146 | 2025-09-16 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77c05598-0936-3cde-b920-ac2347f04098 | -6.21683 | -43.90191 | 2025-09-16 04:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f10de2ba-87af-3058-aacc-781af0bf837c | -4.79469 | -49.54407 | 2025-09-16 04:49:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0ff2d4b4-0156-39b8-8649-9a44d01f1695 | -6.37153 | -44.40994 | 2025-09-16 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77158734-96ec-36df-b022-cfc4e492c139 | -7.20811 | -44.38391 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6401c28c-cdcb-3c4c-b233-5db56c36978c | -3.40499 | -46.90764 | 2025-09-16 04:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05c8f5a7-15f4-395d-9f0a-6a10333ec853 | -3.82428 | -44.10317 | 2025-09-16 04:49:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da14a2f8-58f9-3c45-a3d4-4bd284e89419 | -7.26656 | -46.5973 | 2025-09-16 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f158d43e-51eb-3ff5-a6de-1080f53ba4e4 | -7.14258 | -47.98398 | 2025-09-16 04:49:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 2d10bb7f-ccdc-384b-aa81-400d18d4c470 | -7.08293 | -44.54476 | 2025-09-16 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b49c8fa-ed45-3fbd-83a7-513d5a8dafda | -7.53046 | -46.72384 | 2025-09-16 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README63.md)
