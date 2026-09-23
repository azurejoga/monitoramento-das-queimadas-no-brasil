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
| 17fc00f7-cdb9-3a45-8358-91b4f26deea1 | -8.83 | -50.48142 | 2026-09-23 00:01:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d12a7fc9-856e-3d5a-9171-1c225ee100c8 | -6.57893 | -44.15788 | 2026-09-23 00:01:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| e4785e8f-c8db-3876-bfe0-6e560b49636d | -6.92708 | -46.54299 | 2026-09-23 00:01:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 9b816bff-e659-30a6-a618-ca6eb4e17129 | -8.83249 | -50.50007 | 2026-09-23 00:01:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 6eb2f491-47c4-3745-995e-825bd5b8bad7 | -7.15051 | -48.44452 | 2026-09-23 00:01:00 | TERRA_M-M | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 0be00463-4c95-3285-a863-c2dfe7693c8b | -8.77997 | -45.62402 | 2026-09-23 00:01:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 200e499d-c14c-34bd-956f-70037783bc72 | -8.50084 | -57.60743 | 2026-09-23 00:01:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| ce5c3726-8b2f-381f-b9c9-fc0ab74358b7 | -10.15767 | -47.67438 | 2026-09-23 00:01:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5a2a32f3-1de6-32b0-bed6-c1593db0d2cc | -10.0556 | -48.84948 | 2026-09-23 00:01:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a1748db5-15e5-3850-a149-d0f924de9a65 | -11.00904 | -54.15407 | 2026-09-23 00:01:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 58350c65-e434-33b0-b114-af43b2228837 | -7.77748 | -49.31512 | 2026-09-23 00:01:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7372a1d8-2e59-32db-8fb6-0e92179b12c1 | -8.33286 | -50.82533 | 2026-09-23 00:01:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3f0b1f58-eb94-398c-bd12-2958676cc0a8 | -7.78288 | -50.22679 | 2026-09-23 00:01:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e39ea3ae-65eb-3668-8c89-9cf04e65053e | -9.57249 | -47.96538 | 2026-09-23 00:01:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8e128f64-5918-30f3-885e-163cf6b77f3d | -8.73607 | -47.59412 | 2026-09-23 00:01:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 782a9853-dd79-3485-9a04-75e54bf2b9c3 | -9.82281 | -46.10125 | 2026-09-23 00:01:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 79cd5b3b-52c7-3780-9c9e-a7a8b93ebe73 | -9.93958 | -48.48181 | 2026-09-23 00:01:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 8af99e51-f799-3083-8821-94599c47f87b | -7.39186 | -55.22696 | 2026-09-23 00:01:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b829c9ae-a791-3e36-92ec-0f75fe58be0a | -6.92048 | -46.56659 | 2026-09-23 00:01:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 139.6 |
| ca72de70-a46d-358e-8fce-6aa6af6888fb | -7.14159 | -48.44579 | 2026-09-23 00:01:00 | TERRA_M-M | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 85cc37f3-779d-38f5-bb41-6138f2683863 | -8.3863 | -45.598 | 2026-09-23 00:01:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 23d9a495-08d7-3d9d-b52f-e7a0ab99457c | -8.89952 | -45.95092 | 2026-09-23 00:01:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9fc9a0ec-c67b-350f-990e-cadca4324fc3 | -10.73326 | -50.81482 | 2026-09-23 00:01:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 03eadbb7-a35f-362d-8046-ece3d938d185 | -7.41791 | -49.85569 | 2026-09-23 00:01:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 0ce8c749-7192-3d01-b808-05fa41177c18 | -7.41038 | -44.7236 | 2026-09-23 00:01:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 08b688f3-18ec-3908-90f9-12469639afd3 | -6.89803 | -43.63514 | 2026-09-23 00:01:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 46.9 |
| f7e91f67-f11e-3453-a142-a183cb767db1 | -8.42484 | -45.85398 | 2026-09-23 00:01:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 03ce33bd-84db-3508-9d16-edc95739f083 | -10.62061 | -53.97679 | 2026-09-23 00:01:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 8670cf89-c394-311d-b443-5a6282783b71 | -10.44273 | -50.35974 | 2026-09-23 00:01:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 43e4a7c3-7f4e-3852-91c7-1fd8a6466460 | -8.44922 | -48.70982 | 2026-09-23 00:01:00 | TERRA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 11.6 |
| d7b0e55f-c3d3-335a-bdeb-7adaaed94a43 | -9.59756 | -43.95649 | 2026-09-23 00:01:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| f26d282a-9bc5-33b5-9cae-85e4ce441e80 | -8.46931 | -50.19953 | 2026-09-23 00:01:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 86849694-90b2-341e-9ddd-f6c2d6fe86d7 | -9.28852 | -50.33023 | 2026-09-23 00:01:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c94285bb-9d7f-33d3-884b-8768f43cf6e7 | -6.43522 | -43.72735 | 2026-09-23 00:01:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 701b7d81-7d0a-3d5b-aea7-bafbc4914675 | -8.19541 | -54.73127 | 2026-09-23 00:01:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 7e500397-4a4a-35b1-a579-fdc0632a4aca | -9.57539 | -48.44951 | 2026-09-23 00:01:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 15d21046-5b31-30b8-8ed1-83430d095f05 | -10.09839 | -48.83426 | 2026-09-23 00:01:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d1095f25-02c6-3719-89c0-f861304f41de | -6.8977 | -46.54719 | 2026-09-23 00:01:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| af734fce-5770-379c-8cf3-5d23e554061c | -7.43569 | -49.83825 | 2026-09-23 00:01:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 0b5bf8b5-aa14-39da-b6b9-e10db29fb376 | -8.5909 | -44.53743 | 2026-09-23 00:01:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| deee721e-3cf0-381d-829e-058a6ac2ffc3 | -8.1279 | -44.43885 | 2026-09-23 00:01:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| dec0a28c-0f8f-380f-aef2-ea6e943856f6 | -7.61678 | -50.42814 | 2026-09-23 00:01:00 | TERRA_M-M | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 8e12948d-4903-373f-90e2-a252fb6e824f | -3.86846 | -52.26152 | 2026-09-23 00:03:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 9354d128-c9a8-3fa5-8041-36a53d7cc960 | -2.26253 | -48.76117 | 2026-09-23 00:03:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 78d22cca-10ad-3cc4-a723-4bc1af7b9d55 | -3.89045 | -51.95502 | 2026-09-23 00:03:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 796dc97d-fbc4-361e-9c2a-4197c4f59794 | -5.34833 | -45.17677 | 2026-09-23 00:03:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 726d54e1-3b5c-3f02-becd-7f31a22244ff | -6.06812 | -57.81203 | 2026-09-23 00:03:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 8559a28f-9e17-3bdf-ab52-0ec021005170 | -5.7473 | -51.92695 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| fce96171-2fc9-38b6-a66b-e59768c21843 | -3.46772 | -59.56287 | 2026-09-23 00:03:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 80f45048-9f26-33c5-8c54-a17413500e5b | -3.94693 | -47.62169 | 2026-09-23 00:03:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| cfa3c031-e7b5-31a4-b2a0-c4a7ba9cd37f | -6.88677 | -55.34114 | 2026-09-23 00:03:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 664628d0-0284-3c4c-928a-e9cf93808eb1 | -5.11632 | -48.8017 | 2026-09-23 00:03:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| c6a5a3c4-4adb-31c3-a024-6f8165ecdc71 | -5.47691 | -48.87362 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6e4401b6-3bc5-35a6-b1cc-5eb7d7f3159b | -3.36571 | -50.46648 | 2026-09-23 00:03:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c56e94a6-b419-3e49-a3d3-73330c00b181 | -4.00108 | -52.09103 | 2026-09-23 00:03:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 49132dc2-0099-3cd3-a3d2-d34ad7f57846 | -4.8354 | -55.76511 | 2026-09-23 00:03:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| fd402365-a0dd-35d2-a495-012b6e0063ae | -6.899 | -55.33979 | 2026-09-23 00:03:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| d4dde257-3eab-304b-a888-f7692457a040 | -6.45287 | -59.9899 | 2026-09-23 00:03:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| bbd032e5-97be-3496-a0f5-bad0fd2d983b | -6.66416 | -50.94591 | 2026-09-23 00:03:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 5aee6dd3-65c0-3fc2-9e1e-0cdbafc13132 | -3.59029 | -50.02407 | 2026-09-23 00:03:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a5ec928c-e1c0-30e1-952c-69b1d09e98f6 | -2.45613 | -57.8984 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| c8aa90cc-df5a-3592-ab20-5b08434692a7 | -3.50853 | -53.21164 | 2026-09-23 00:03:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d9894763-7292-32c3-b344-48fe16383cc6 | -3.68834 | -60.60453 | 2026-09-23 00:03:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 05a24f75-ce4c-3d2e-bb9f-76eed8009dd0 | -3.47207 | -59.59715 | 2026-09-23 00:03:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 9e82918c-9779-3526-b17a-d2de61869d60 | -2.96628 | -50.39223 | 2026-09-23 00:03:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c1d55af6-4218-3a80-a5d0-e020b3d10cd7 | -6.38416 | -55.27541 | 2026-09-23 00:03:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 20756070-fad1-3e17-9cfc-6d2baf8aa958 | -1.13613 | -47.71242 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 27d99d6e-26d6-3564-b3a8-0754b999f6e1 | -5.82897 | -50.21836 | 2026-09-23 00:03:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| c609a98f-25bb-3390-ad94-c7962dac7333 | -5.77858 | -47.16481 | 2026-09-23 00:03:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 30.7 |
| bfab9505-d501-3f65-ad32-4f00d24e2ca2 | -7.33546 | -55.59533 | 2026-09-23 00:03:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1e7fdb3a-1f63-35e7-97c6-476fbb3b744c | -5.61263 | -45.2496 | 2026-09-23 00:03:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| a5613ec0-84d3-3bf6-aaa4-30fa10850c03 | -4.01346 | -48.95733 | 2026-09-23 00:03:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e6d1ab88-b006-3d37-bf40-3b8232f758c3 | -5.74068 | -53.47643 | 2026-09-23 00:03:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b1396155-8ad6-317c-90c4-cc9b7f5b8bcf | -5.8839 | -51.57625 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 74bda032-78de-3ef3-ac9d-c40df5b669ae | -3.10508 | -60.72224 | 2026-09-23 00:03:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 33.6 |
| c20fa2b1-b46a-3247-8543-64b96df41963 | -5.94137 | -45.38196 | 2026-09-23 00:03:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 2767af79-51a0-3ae1-92b6-88647b2518d2 | -2.92339 | -48.74117 | 2026-09-23 00:03:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a88c3bc3-fdf4-3eb3-9eac-a48a6cb94672 | -5.3959 | -49.08307 | 2026-09-23 00:03:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 11e53eb9-dfb0-32f3-9a35-a0e81b1bb376 | -5.00754 | -49.4763 | 2026-09-23 00:03:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c854cda1-da9a-3d2f-a7f0-eadd5c058b33 | -2.37234 | -48.42829 | 2026-09-23 00:03:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5e294207-cd39-35a5-82a9-189b398a9663 | -2.81805 | -49.2485 | 2026-09-23 00:03:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 02bef6f5-4f3c-3d97-870a-bbd3beffa692 | -0.75659 | -49.20181 | 2026-09-23 00:03:00 | TERRA_M-M | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d1c09cc7-0514-3949-b419-216a4aed990b | -3.68877 | -60.59943 | 2026-09-23 00:03:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 6eb4b35d-6ad1-315e-8411-256e2ce9bcf3 | -3.5827 | -50.03407 | 2026-09-23 00:03:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 63411d63-3fef-3247-9970-64efac747476 | -6.01211 | -52.74743 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1f4563a7-61f2-3ef3-84ea-6009af4d7b43 | -2.97628 | -50.39976 | 2026-09-23 00:03:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 5c4362ca-b295-371a-a3d6-b785f11e67f5 | -3.21837 | -46.95238 | 2026-09-23 00:03:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 28d59f27-7fb6-337b-9b67-187229bff93a | -5.76737 | -45.12709 | 2026-09-23 00:03:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 41.6 |
| fd50d857-1329-3551-92b2-5f3c7a839949 | -3.00551 | -54.17245 | 2026-09-23 00:03:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c5fd4506-25aa-3411-8fb6-9fc900884c3d | -7.28682 | -56.46251 | 2026-09-23 00:03:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 1ac838a6-95b1-3634-90e0-aaafa6c81fff | -6.04258 | -53.28022 | 2026-09-23 00:03:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 27a542c7-5799-3b42-a9bf-4be0afe86776 | -4.45911 | -47.92148 | 2026-09-23 00:03:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 90b2d86a-b4d8-3516-834d-b59e4462b506 | -4.99871 | -49.47754 | 2026-09-23 00:03:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2f3a6d02-5f55-315c-ad65-63a253853fae | -4.27935 | -55.44128 | 2026-09-23 00:03:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| e1b9e4c8-a075-3b32-9c7e-a2c0b95afcc8 | -3.55357 | -49.82333 | 2026-09-23 00:03:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5dc132d9-293e-332c-9a53-67d8e97232ed | -3.57725 | -51.95787 | 2026-09-23 00:03:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| c5394e3f-21f0-3168-83f4-1dadb7fe1a1e | -6.63079 | -59.9495 | 2026-09-23 00:03:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 623d1df9-184e-3d88-8b09-ffe76e9e2001 | -4.07264 | -56.23757 | 2026-09-23 00:03:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| a53f2f0c-35f3-3b94-940f-ef4120c7bc59 | -1.14344 | -54.16336 | 2026-09-23 00:03:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 716bb908-0523-3ad7-9c03-a1627f2f29b5 | -0.7812 | -49.24614 | 2026-09-23 00:03:00 | TERRA_M-M | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |


[Clique aqui para ver as próximas entradas](README5.md)
