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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9cf03f2d-0880-3a0e-bd17-15791847a875 | -6.07251 | -59.96436 | 2025-08-17 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8da1a393-328a-3aed-a3c5-41e2f457078d | -6.141 | -57.93468 | 2025-08-17 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e57d9195-4583-3be1-be5d-06874b07fcf4 | -3.15298 | -45.65188 | 2025-08-17 05:04:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdf6c5de-4d2d-3eb5-a730-f16b76c63a50 | -2.89976 | -51.47298 | 2025-08-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8376617d-e04d-3a1b-b427-b6c74d7d234a | -7.53276 | -50.52989 | 2025-08-17 05:04:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4905e0e-74a7-3914-9f3a-e6c3bde41447 | -2.81444 | -49.0113 | 2025-08-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb37e4a0-88ce-3321-8c06-b078d7c52a98 | -6.07328 | -59.95971 | 2025-08-17 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 501766b4-cf9c-359f-b332-cece2cf90859 | -6.13415 | -57.93356 | 2025-08-17 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 271c54d6-d7cc-39f5-a157-486ceb96d0b5 | -5.95517 | -46.15294 | 2025-08-17 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac808c31-7b4d-3bbe-9c49-a1ff84202022 | -6.35911 | -44.5245 | 2025-08-17 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ce3c5fac-6c56-31ee-91a8-be6a0365e4b0 | -8.03751 | -47.67334 | 2025-08-17 05:04:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 612ff234-16eb-3e16-a030-361cdc8cf81b | -8.51314 | -44.73554 | 2025-08-17 05:04:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3045fa85-6c56-3ef4-85cf-3b1940922c05 | -6.13758 | -57.93412 | 2025-08-17 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e77c0a02-87f5-31bf-88a4-d026290b3f4e | -6.65993 | -58.82047 | 2025-08-17 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8753404f-2fd2-3178-b7f7-eea4c92b2bbc | -6.19181 | -45.44617 | 2025-08-17 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a9234ef8-ff13-3a9c-b835-cf1d162384ee | -1.18164 | -50.5261 | 2025-08-17 05:04:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7c25071-af4e-3c9b-b151-68b4f0dd254a | -6.66829 | -58.81361 | 2025-08-17 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fb10218-47c1-30c4-8e31-aeb413c6b09e | -6.66057 | -58.81647 | 2025-08-17 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff9e9876-fc1c-366b-804a-6be7b311a445 | -4.92091 | -43.24969 | 2025-08-17 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9c7938e6-306b-3030-8e62-ae1bd2d08f1d | -3.87542 | -54.22853 | 2025-08-17 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0708f369-9244-3309-8d47-20ce47b68516 | -7.53697 | -50.53053 | 2025-08-17 05:04:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 865902ff-cb0f-39d2-b914-55a835bf9470 | -6.46524 | -55.89775 | 2025-08-17 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7aead84-5a2b-34b5-9650-2f9a3eda7fe3 | -3.4471 | -48.96811 | 2025-08-17 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 434d6d6c-caa8-368a-b165-3db66d588c82 | -4.59977 | -43.31927 | 2025-08-17 05:04:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 551d4262-d7ff-35ce-b75a-54a34595ffb2 | -7.1575 | -44.38084 | 2025-08-17 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bbb155dc-37ee-3b33-aa45-c420aa579f72 | -6.07405 | -59.95505 | 2025-08-17 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab853717-2f0c-3d87-9388-2ca22c01740f | -8.03792 | -47.67026 | 2025-08-17 05:04:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6fbcc0be-0973-3eda-950b-3265dab4eedd | -2.90279 | -51.47796 | 2025-08-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9bda1c7-f9fa-3eca-b860-6ddf9e461e50 | -7.14442 | -44.64093 | 2025-08-17 05:04:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5b078550-7646-3b71-ab0b-5f28916f0a61 | -8.49994 | -44.73866 | 2025-08-17 05:04:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b2601b69-8ea1-3e7b-82ff-03198d73740e | -5.9547 | -46.15643 | 2025-08-17 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d20576e6-b80d-39ce-bb8a-a58e12c840f6 | -7.59784 | -55.19393 | 2025-08-17 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc41db14-170a-39d0-ae43-9c1f290bd1d7 | -6.17782 | -47.2732 | 2025-08-17 05:04:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77137a5d-5664-3df7-a3b1-50a742f3cf2a | -6.63906 | -55.54596 | 2025-08-17 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d19ecdde-c8a9-35e6-bbc8-dd128d10bd73 | -5.4497 | -60.14379 | 2025-08-17 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea2cf2aa-2cc6-39de-a1d1-7760be6961f1 | -6.08167 | -59.9325 | 2025-08-17 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6431bb5b-e4b6-3a3d-9172-b53eec228093 | -6.07629 | -59.96505 | 2025-08-17 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0fe6899d-dfaa-33f8-9f91-3649bb878598 | -6.46248 | -55.89379 | 2025-08-17 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15da5c4d-38e2-3d93-90e3-6905342cc8a5 | -5.00779 | -62.39969 | 2025-08-17 05:04:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 12cf26ee-3ece-3863-842d-e90ad3e9dac6 | -6.63577 | -60.01242 | 2025-08-17 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd0ba6bf-f0fc-39be-af0e-beb70e4695f2 | -6.0786 | -59.95108 | 2025-08-17 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32ee4f2d-4ab6-37e5-8898-a4f82726d4f4 | -6.63852 | -55.54943 | 2025-08-17 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70675f29-c120-3ee6-b45b-380e8b112b18 | -4.92593 | -43.26186 | 2025-08-17 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7dd23404-e5af-38a1-9822-fd9a5acdef84 | -6.635 | -60.0171 | 2025-08-17 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 39918b00-eadd-3699-8d22-8df650b513e8 | -7.51799 | -44.97746 | 2025-08-17 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9d88e87c-6296-3f12-93c6-9762c6eecd73 | -6.08391 | -59.94245 | 2025-08-17 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc4a0de7-d028-32c5-8bcf-9989286c8d98 | -7.3701 | -57.62461 | 2025-08-17 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8cf6b159-b848-362d-8c17-f4b745cad07c | -6.07706 | -59.96039 | 2025-08-17 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf739e0a-a1be-336a-8f8e-212959427b0f | -4.45104 | -55.48775 | 2025-08-17 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d9a3801-f028-3155-b1ee-821384270286 | -8.50687 | -44.73461 | 2025-08-17 05:04:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 77dbd3ee-8449-3c52-9cbb-f218b72e093d | -8.70491 | -49.41191 | 2025-08-17 05:04:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8bd076c5-6db4-3ccb-9d62-dcca198b286d | -8.74838 | -44.04086 | 2025-08-17 05:04:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7f505135-bc66-3786-8dad-bf78ea36bc5e | -2.98633 | -49.30525 | 2025-08-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0587dfe8-547b-3b37-b306-1fe21e0a6d8b | -6.61825 | -43.88242 | 2025-08-17 05:04:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f473d71e-ac6b-3ac6-a153-e42eb7930142 | -2.89908 | -51.47739 | 2025-08-17 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 875d6b8d-4ad9-3045-8fbe-3a91eb6fc991 | -7.14513 | -44.62647 | 2025-08-17 05:04:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5861aca-270b-3dbc-80f2-d72b0edfb1c2 | -4.91934 | -43.26102 | 2025-08-17 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 67925084-9faa-3e24-ae3c-6791096fda99 | -5.95506 | -46.1576 | 2025-08-17 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f373082-f270-39a3-830d-54a927ea66f2 | -6.08014 | -59.94176 | 2025-08-17 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3be4dbec-83e4-3f7a-bae1-25b0858a3dba | -3.45087 | -48.97305 | 2025-08-17 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41ffbcff-8848-39a9-bdcd-8ba075d2957f | -6.67178 | -58.81337 | 2025-08-17 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb24ec1d-d6c3-3486-95aa-eb93cc24496b | -6.93193 | -59.64893 | 2025-08-17 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b1d57588-6e5d-308d-96b4-7c2fe4e0ad8f | -8.50478 | -44.7294 | 2025-08-17 05:04:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9aa4448d-66bf-3108-9871-2a9b5da6ff20 | -6.13817 | -57.93037 | 2025-08-17 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78ffac40-f857-34ce-a213-93bb38dba3a7 | -7.60553 | -44.93266 | 2025-08-17 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4c27b944-3cdc-3185-aec8-ce712796cd4f | -4.45542 | -55.48138 | 2025-08-17 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d19ea95-cdab-3b73-bde0-cf0c76f61954 | -3.64976 | -48.32748 | 2025-08-17 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00021772-6300-3837-863f-866f2db3a90d | -5.45513 | -60.13475 | 2025-08-17 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4550b78-59a4-3316-a364-da8a59394967 | -7.93869 | -48.18351 | 2025-08-17 05:04:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ac64207-b108-3342-9329-4a50b4d68b82 | -7.14323 | -44.64123 | 2025-08-17 05:04:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 78ad5b88-180a-3a17-8faf-8d930a2b392b | -8.51106 | -44.73034 | 2025-08-17 05:04:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 985bbd14-cfbb-399f-acba-e34367d4381b | -7.6261 | -44.96664 | 2025-08-17 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 53480c1d-38e3-3a99-a5f7-77f34df22c5f | -8.51249 | -44.74048 | 2025-08-17 05:04:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b7d2617b-bcbc-3ecf-8f3e-4e8ab69e33e9 | -6.14787 | -57.93578 | 2025-08-17 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a111235c-2ce1-3797-9331-dfa951aa878f | -6.54424 | -43.03776 | 2025-08-17 05:04:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 18e6f17c-90ce-32b9-936b-dab799fc0331 | -7.15689 | -44.38558 | 2025-08-17 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2e6ccab7-f282-3091-a488-cd1893ae5f53 | -8.51044 | -44.73531 | 2025-08-17 05:04:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 47d57289-81e7-36a4-8408-1add481e8081 | -5.62713 | -51.29785 | 2025-08-17 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21a75815-e54d-3aa9-9540-0332ead6b592 | -5.45048 | -60.13895 | 2025-08-17 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 841207de-e84a-34d7-8914-0d6ec141aba8 | -5.24183 | -56.10712 | 2025-08-17 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f595da1b-8e25-3f9f-b074-3f25276154f8 | -7.18982 | -43.96994 | 2025-08-17 05:04:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d3162461-ed1f-3d03-9498-85c117c5c486 | -2.81532 | -48.61235 | 2025-08-17 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2aa7bef6-c87f-3112-ba26-d778d86586a9 | -6.17739 | -47.27627 | 2025-08-17 05:04:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be90a467-4389-3b5e-8788-37509e101822 | -6.1876 | -45.43328 | 2025-08-17 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c74d730d-72ba-34a2-a02b-1ee4c9732bd0 | -8.04267 | -47.67405 | 2025-08-17 05:04:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9dc44e82-d3f8-3575-8f80-457468196a5c | -2.81673 | -48.61404 | 2025-08-17 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8ab56cbe-99d8-3f8a-8c2d-63302e2b369e | -6.13474 | -57.92981 | 2025-08-17 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c363d16d-4c9c-376d-914f-d4a74a4bfd91 | -5.67557 | -52.217 | 2025-08-17 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 436c284c-32e6-3c0c-a1d1-7d948d97895d | -6.07937 | -59.9464 | 2025-08-17 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75f1886b-dd72-3e00-8c91-08b8c98a3f6c | -2.81227 | -48.61333 | 2025-08-17 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4c746ab9-59c1-34be-9dd7-2015439dd156 | -7.14508 | -44.63615 | 2025-08-17 05:04:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| eeb944d0-e919-398d-bdd9-aa8ef2ddffb0 | -7.14262 | -44.64591 | 2025-08-17 05:04:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4c003fea-7750-3a2f-87f6-40e90bb2ec0e | -7.51861 | -44.97768 | 2025-08-17 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 94e000b7-a21d-32a1-84b6-ef41698d141f | -6.7364 | -55.51118 | 2025-08-17 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8209b8da-1397-3572-bb67-eb9447955211 | -7.15421 | -44.38004 | 2025-08-17 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19590c3d-331c-3c1b-8202-50b8c1cceab8 | -6.07173 | -59.96903 | 2025-08-17 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d25ad59-5049-32f6-ae8f-ff2eb1a73151 | -8.50622 | -44.73955 | 2025-08-17 05:04:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3c7cb5a1-ac30-319b-8b7f-44a2d3b10e75 | -6.55351 | -43.01992 | 2025-08-17 05:04:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9356642a-ac32-3aff-8b91-298ba82581de | -7.14378 | -44.64561 | 2025-08-17 05:04:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 0cf95fc1-0f0f-35d8-a4fa-71803c19ebac | -6.92896 | -59.64397 | 2025-08-17 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README25.md)
