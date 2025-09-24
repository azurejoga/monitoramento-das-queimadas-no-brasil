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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4118ac3-f733-3563-8e75-1e9a8ee26d87 | -4.08134 | -48.04251 | 2025-09-24 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea2af5bb-264a-3459-a398-6ded1fd56de4 | -5.52094 | -43.86499 | 2025-09-24 04:00:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fe0e075b-c7d2-3aec-ac62-09e7a35a105d | -3.64154 | -48.32454 | 2025-09-24 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 563a5b5a-7d5e-340b-b404-1241135471f2 | -8.5228 | -45.0159 | 2025-09-24 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 874e2a38-806d-3936-a2f1-47625045cd44 | -5.63043 | -45.73565 | 2025-09-24 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0df1b7ee-0a10-3ed8-8aa5-783fbbf2df69 | -7.26112 | -43.01647 | 2025-09-24 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| de1f5a8f-2a8e-37ae-b5a1-51671f65d0e5 | -7.93815 | -44.10039 | 2025-09-24 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 147aa294-624d-3740-9649-2ab80ef5b4f5 | -5.91373 | -43.85705 | 2025-09-24 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f740317e-3f14-3656-990b-cb9372f6479d | -7.26248 | -43.0083 | 2025-09-24 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b55b1cd8-a261-3cb1-bc67-870824d76ef4 | -5.61565 | -42.98952 | 2025-09-24 04:00:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bc596f42-fc7e-370d-a5cf-74af654a2b54 | -5.98555 | -44.51033 | 2025-09-24 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f2afec8-043b-3b6d-8d5a-6d8f37ed5c45 | -7.80338 | -43.17975 | 2025-09-24 04:00:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b51493c8-031a-3c4b-a436-2f98f5bd0610 | -7.26537 | -43.01295 | 2025-09-24 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0674da11-929f-307c-bb2d-f98f0757d08e | -3.81513 | -40.38432 | 2025-09-24 04:00:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 90f163d0-6598-37f2-b61c-0af1df079178 | -9.48194 | -40.35679 | 2025-09-24 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a3070196-aaba-3c85-ab90-8e19080645d9 | -4.75004 | -43.62716 | 2025-09-24 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30f14137-ff62-3295-aee9-345ff7804478 | -7.31728 | -42.94201 | 2025-09-24 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 484c8712-4f20-30af-a5a3-e53b352d09b0 | -4.30415 | -48.09401 | 2025-09-24 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f26822e6-8cc3-3afd-a326-2fc09dbff9eb | -3.05089 | -46.9234 | 2025-09-24 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf83e9b7-6168-32cd-b252-2484d066cfc3 | -4.78971 | -43.23542 | 2025-09-24 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e6fb0cf-3da9-3264-9304-16889e6e2a86 | -9.52037 | -43.07927 | 2025-09-24 04:00:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 50a11209-9ec0-3028-9a4c-b5cceecd4ff0 | -5.47252 | -44.68967 | 2025-09-24 04:00:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1289f278-8349-3dbf-8b53-dc859d94432d | -7.94488 | -44.10617 | 2025-09-24 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6f99ee8d-7aaa-3107-a228-8f7113c02e19 | -5.61625 | -42.98806 | 2025-09-24 04:00:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8cfb88bb-ce86-3dc6-8b5d-9e4a2f0866dd | -3.79857 | -47.5824 | 2025-09-24 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f145b663-94f5-3a92-ab0a-749d75992291 | -4.42733 | -47.26569 | 2025-09-24 04:00:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 153bdbae-86aa-3c18-ae72-e6573afb3c06 | -7.55337 | -46.24276 | 2025-09-24 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f611afd0-b98b-3425-b74d-5edd73cc0cde | -4.78776 | -43.53572 | 2025-09-24 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cd11fca7-ccf4-35ea-8925-c43ab71421a5 | -8.81699 | -43.07769 | 2025-09-24 04:00:00 | NOAA-20 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7b831f28-cb85-344d-a316-a0f007b136e1 | -4.78995 | -43.04608 | 2025-09-24 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 27597251-ab07-3fdd-8beb-6cea5ebc0663 | -5.1938 | -42.70329 | 2025-09-24 04:00:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8e71290-4afb-3662-809b-8dd6f1678174 | -5.62679 | -45.73101 | 2025-09-24 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d0eef987-ebab-3728-8dbf-67140299335e | -3.64731 | -43.1115 | 2025-09-24 04:00:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3333aef6-96a9-3a09-bdb9-c9271c7ee134 | -7.52358 | -42.27624 | 2025-09-24 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a2e7f6b7-eade-3287-b9e5-afcf08dfac0f | -6.41679 | -43.08692 | 2025-09-24 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 97f89bff-917b-3ee7-937e-99f4852302bd | -5.91106 | -43.85431 | 2025-09-24 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5769743-0df2-3514-a5fe-ca312738717b | -3.7981 | -47.58521 | 2025-09-24 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cbc7f356-9ff0-312b-a823-672feda56535 | -7.37181 | -47.03702 | 2025-09-24 04:00:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 854ecc7e-6062-300b-8616-343007de8c75 | -5.30965 | -42.74969 | 2025-09-24 04:00:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 390dee99-ab63-37c9-bcbd-c51802c4d0d8 | -3.15403 | -49.11773 | 2025-09-24 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd749d7c-39c6-3d68-b4a6-9efafbdb0e6e | -5.39097 | -42.26494 | 2025-09-24 04:00:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d5737ca0-6d4f-3346-918b-33b2f8a31d5f | -5.64015 | -43.92046 | 2025-09-24 04:00:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| b3f6484e-12e4-301e-96cf-e8d0bbed85f2 | -5.76449 | -42.6002 | 2025-09-24 04:00:00 | NOAA-20 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| fd9a4314-de04-3a76-987e-fb9b0eeaaec4 | -3.41002 | -52.68152 | 2025-09-24 04:00:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 84dc2a98-4b6b-3cea-b8d3-4690140b464c | -4.40274 | -44.36543 | 2025-09-24 04:00:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 251ebc9d-11e2-32b6-b635-138f7249ac13 | -9.24568 | -44.49517 | 2025-09-24 04:00:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3489f2c8-e778-35f9-a5fa-e11ecb7486e2 | -7.77389 | -46.19436 | 2025-09-24 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d3eccea5-39cd-3c15-97f8-c438fc51484f | -5.61724 | -43.46552 | 2025-09-24 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c2e38fd-5055-3028-8218-0e7efb0c91ee | -3.60643 | -47.53442 | 2025-09-24 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4eb5d9d3-8d87-3503-bcb8-3c0a5352f279 | -5.91831 | -43.85302 | 2025-09-24 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8583fe08-dafb-3fa3-816a-ad12f349481e | -3.69066 | -49.01802 | 2025-09-24 04:00:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25c978fd-0089-30e5-9507-3ceba0894439 | -5.63541 | -45.73236 | 2025-09-24 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c47a57a2-c48e-3cd3-b264-e39d7becc69e | -4.19713 | -46.82006 | 2025-09-24 04:00:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6803ee53-4e03-34b5-adad-a62ef2bc9c9a | -8.02835 | -42.40688 | 2025-09-24 04:00:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dda6febe-ab6b-33a1-9204-f68a8c97e3c2 | -6.35379 | -43.3565 | 2025-09-24 04:00:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3e7b56b9-8634-37ca-b967-4f9d53af0c3d | -4.00882 | -43.27137 | 2025-09-24 04:00:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6af72a5-fa35-3634-aa6a-a8897b5d4141 | -5.29926 | -44.99947 | 2025-09-24 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b823a25-44cc-33a2-b70f-13c8300bbde0 | -6.12934 | -44.44234 | 2025-09-24 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| afecaa4b-ac06-3a0a-8d02-332244a7723c | -5.21818 | -43.7256 | 2025-09-24 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8d39db59-cc64-3a22-8721-0263a04907b9 | -3.18221 | -48.81195 | 2025-09-24 04:00:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8d24bfd0-c36a-302d-a70a-c18314578104 | -5.51991 | -44.21168 | 2025-09-24 04:00:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2442c639-be98-30f1-8e5f-342b7c845598 | -5.37274 | -42.26606 | 2025-09-24 04:00:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c144f039-475c-34e7-8e00-026bfb86d257 | -6.20423 | -37.62016 | 2025-09-24 04:00:00 | NOAA-20 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 19c41e99-6c1a-327d-842d-5fe05eb60b24 | -5.3024 | -44.80912 | 2025-09-24 04:00:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d887475-428b-3fda-ac1c-ad6dd317bd80 | -7.36775 | -44.53915 | 2025-09-24 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 960a9b16-4a4c-3add-bc13-bbc0f16ac2da | -4.30879 | -48.09803 | 2025-09-24 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 548b47cd-2ceb-3df4-8939-f18af2b5151a | -7.26942 | -42.9885 | 2025-09-24 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 474e11a1-8c23-3343-8543-0210f239ab4d | -7.98919 | -40.96786 | 2025-09-24 04:00:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 876ea895-fdde-38e2-919a-55eba22db1f0 | -5.17384 | -45.43644 | 2025-09-24 04:00:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f493bdd8-b375-39ab-a8be-72bca8e484b6 | -8.36466 | -40.3353 | 2025-09-24 04:00:00 | NOAA-20 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 897a2f94-8015-3fae-9908-8b6d2d5829fd | -4.71047 | -46.46953 | 2025-09-24 04:00:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23bb8dce-82aa-373d-ab9c-8ca63a4834ae | -8.78707 | -43.04 | 2025-09-24 04:00:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6b07aa27-9276-3544-9dc4-09bc8e3c6f75 | -4.91961 | -42.80254 | 2025-09-24 04:00:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f8c1a0b-552b-3932-ad81-ff5acf6c3b15 | -7.9464 | -44.09716 | 2025-09-24 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a998b2e-3f34-363f-a837-5a1420995f15 | -8.54843 | -44.95871 | 2025-09-24 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 837412a6-0e4e-38d0-8a80-e1449ef35a30 | -8.16437 | -46.24145 | 2025-09-24 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b6b8b61-b8cc-3336-9eeb-2214a593482a | -9.03275 | -44.95001 | 2025-09-24 04:00:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dfac32af-5234-313b-9ecb-40c40f7edc18 | -8.17299 | -46.2682 | 2025-09-24 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa55818c-2259-364c-97c8-28236c0be1a7 | -8.79319 | -43.02481 | 2025-09-24 04:00:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9ccfebac-fa1a-3fd7-a47c-9904cc261023 | -8.793 | -43.06965 | 2025-09-24 04:00:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| eb46a322-ea6e-3d95-95fd-382601fcf1a2 | -4.38212 | -43.29054 | 2025-09-24 04:00:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f53384fc-f8b1-36f0-b652-7ab31e22b036 | -4.87161 | -37.47273 | 2025-09-24 04:00:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c2e83e21-2157-34a0-b4a8-75e0353fb919 | -7.82735 | -47.86425 | 2025-09-24 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f0d69f6-08d2-381a-9119-b43b472d4652 | -7.36724 | -47.03619 | 2025-09-24 04:00:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4c1d6cf8-bfbe-365b-bb88-dea3862cffcc | -6.5353 | -44.22594 | 2025-09-24 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b34ab29f-1212-3438-9a79-4e7f94af0ac1 | -5.37527 | -42.25032 | 2025-09-24 04:00:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ca103977-2b7e-3478-a413-8af95fc5c3a4 | -7.48997 | -47.54614 | 2025-09-24 04:00:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ee03057f-e502-3899-87dc-5e9935051963 | -5.84115 | -42.64059 | 2025-09-24 04:00:00 | NOAA-20 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 98ff989d-2cec-3f34-9638-0094d29bf3d1 | -8.52981 | -45.02233 | 2025-09-24 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dee16a3f-d312-31b6-a8d5-ebecd45d5a43 | -7.94113 | -44.10554 | 2025-09-24 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f21fce0c-f77f-31ce-bf2e-4db6f0065110 | -8.54678 | -44.96868 | 2025-09-24 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 293c4b5f-4e9f-3e34-b04a-d7bd2fb7951b | -5.96938 | -44.12586 | 2025-09-24 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5638d919-00a8-3d69-90c7-7d4a5ea38c70 | -5.3814 | -42.27961 | 2025-09-24 04:00:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 31a606c5-a44e-30de-a7e8-2567a6f1b7ba | -7.2647 | -43.01705 | 2025-09-24 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e12e82a8-6189-3740-a4f5-d8ce8879ad66 | -6.59825 | -44.30951 | 2025-09-24 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bb450228-1706-32e3-941c-ef2e077f7841 | -5.7698 | -44.52753 | 2025-09-24 04:00:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e042a695-6332-3330-ae93-e783ee2dd5de | -5.7548 | -42.56981 | 2025-09-24 04:00:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3059e72b-6d03-3863-9d8b-3f36e21559a7 | -4.48619 | -47.68025 | 2025-09-24 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2581308-769c-354d-ba0b-db6af0774dbf | -5.23875 | -43.71932 | 2025-09-24 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4204c385-72ad-3843-8748-54ba1e7c7eba | -6.41248 | -43.09057 | 2025-09-24 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |


[Clique aqui para ver as próximas entradas](README9.md)
