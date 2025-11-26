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
| e9c35d8f-416b-32d9-baac-7207258f611c | -6.47268 | -43.55201 | 2025-11-26 03:57:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7c46547-a8b5-36c1-b1d1-4c7d2a3c097b | -4.8255 | -43.81788 | 2025-11-26 03:57:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0637e6b5-8eef-3e5d-aa73-b9baa055f5b7 | -4.72354 | -46.46722 | 2025-11-26 03:57:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 291162c6-56bc-3426-86f2-ae673c5dd987 | -6.80658 | -41.71902 | 2025-11-26 03:57:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 65c623a4-4933-3d2e-852d-fe602c9426c4 | -2.54879 | -45.39104 | 2025-11-26 03:57:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d654fc64-827c-34d7-ac16-db0e998ccf76 | -4.24511 | -48.56757 | 2025-11-26 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a8c5751-999c-310c-a8d8-fda5206da550 | -6.06186 | -43.24933 | 2025-11-26 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 58114293-f1df-3322-876c-f79bbb1022b4 | -2.70056 | -47.4059 | 2025-11-26 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e97c7705-1e8d-3f6e-bc7a-2419135a8674 | -4.05654 | -48.82693 | 2025-11-26 03:57:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d31818b2-7d7d-32f7-8f7b-7ed229ca5f09 | -3.60707 | -40.43639 | 2025-11-26 03:57:00 | NPP-375D | MERUOCA | CEARÁ | Brasil | 2308203 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a90f88c5-5559-323e-b65a-28883d335b6e | -3.28359 | -42.18082 | 2025-11-26 03:57:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c589a7e-e416-3880-9d4a-2a9d832b0010 | -3.9574 | -49.03541 | 2025-11-26 03:57:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c44b9d1d-7de4-3b0e-941d-2a673d425b8c | -4.16323 | -43.72116 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2ece944-be7a-3515-bf1e-35a8d18ebe89 | -4.55645 | -43.30114 | 2025-11-26 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ad2988c4-dcbb-330b-93b9-f4e8690df704 | -5.41486 | -41.08067 | 2025-11-26 03:57:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 41e5d481-4a23-31f8-b327-9c72d950ec9d | -4.1797 | -43.72788 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b389b9e0-c983-30b5-b339-212c446d334f | -3.32555 | -50.27236 | 2025-11-26 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 01b07df1-d587-37fa-ba5a-d9eba40979ba | -4.17674 | -43.71914 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 97aec4d4-7b6b-3b91-afbf-88f045ce8115 | -3.13752 | -49.40379 | 2025-11-26 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6edfea04-3114-3f63-be0c-c80b2338c565 | -2.50081 | -47.81909 | 2025-11-26 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4fc647b8-fca7-37b9-8be0-0b06e2a106bf | -6.31211 | -43.79012 | 2025-11-26 03:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0938d44d-17fc-3551-873b-a31fa563e363 | -6.49991 | -38.84631 | 2025-11-26 03:57:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 316fd194-7faa-3dfd-a4ca-0770f7e39bec | -2.49807 | -47.83541 | 2025-11-26 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 19334431-fefb-3f00-a170-6e03a646a510 | -3.43956 | -50.19194 | 2025-11-26 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ea5932f5-e1a2-3894-b9a4-ce4daee30c79 | -3.48834 | -44.5094 | 2025-11-26 03:57:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e19e8ec-2529-34d8-83e1-edf8a7f952ac | -2.74492 | -47.13917 | 2025-11-26 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d8c2e4b-7015-3b2e-a5a5-b25eeae019e2 | -3.23074 | -51.17707 | 2025-11-26 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f7110ba-3e48-392b-9e69-a9f43f9a581f | -6.74397 | -39.05332 | 2025-11-26 03:57:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 435e446d-5b17-3ca7-ad01-3c4c9fb6de7d | -2.85516 | -45.2339 | 2025-11-26 03:57:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcbd57b1-ee2f-3e19-8241-9873411bdf2b | -3.47732 | -43.42775 | 2025-11-26 03:57:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1271dd96-a426-3eb3-9715-615d45d6349c | -4.60074 | -44.41493 | 2025-11-26 03:57:00 | NPP-375D | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ddb87df2-9065-3c7b-86db-b5a26267d135 | -4.17048 | -43.73046 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d0b007cf-792a-33af-82ea-95286ee274d7 | -4.72443 | -43.33552 | 2025-11-26 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f6c9699a-446f-33ad-9e38-7e394fa63e6c | -4.87118 | -38.67723 | 2025-11-26 03:57:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3c9733f0-b855-3aeb-a229-eff115b41ead | -6.47208 | -43.5556 | 2025-11-26 03:57:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09e04f41-b302-38ee-8230-f1b6ac235691 | -6.1121 | -42.9505 | 2025-11-26 03:57:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e7680c11-d4a3-3edc-b9fe-6c42f2bcea32 | -7.49884 | -42.88383 | 2025-11-26 03:57:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b49651b1-1f5b-36aa-8d0a-ed5a7938a93f | -6.68981 | -42.47696 | 2025-11-26 03:57:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1926f67f-2147-3343-bf82-ae6ac6f33a95 | -4.66022 | -43.97663 | 2025-11-26 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| fb8126fb-82e6-3446-924a-7e3bc2eac488 | -5.45419 | -38.39586 | 2025-11-26 03:57:00 | NPP-375D | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b3a24524-e8c7-35c8-85d2-36cca11f6e2b | -4.41632 | -43.4963 | 2025-11-26 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 66fbe1aa-2906-3944-bd42-110f74fbfc06 | -6.76265 | -46.51899 | 2025-11-26 03:57:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3dd1ba0f-822e-3532-a3f8-1a41b7fde7bd | -6.10729 | -42.95501 | 2025-11-26 03:57:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f2851931-ce7c-3846-9bd7-9c0c0661e2bd | -2.73616 | -49.46141 | 2025-11-26 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ae46759-523a-3779-b05b-25a57dab4a30 | -4.83733 | -38.6112 | 2025-11-26 03:57:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 261ca34a-9b5d-3a3c-979f-8ac7c64a1523 | -4.16752 | -43.72178 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| c614b58f-9bf7-30eb-bcf0-42e65375a1a2 | -4.53734 | -45.55902 | 2025-11-26 03:57:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6920e15d-39ba-3215-98d6-7b26cfbf3b5a | -6.76732 | -46.52032 | 2025-11-26 03:57:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 42650da1-7a92-369f-a420-ddebf9012259 | -7.1688 | -44.99491 | 2025-11-26 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fd472b9c-81aa-3d2c-8fcc-db95b472a7ea | -6.81309 | -38.57604 | 2025-11-26 03:57:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8f117636-d753-3238-b9c2-527fd61f2c02 | -5.57196 | -44.97136 | 2025-11-26 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 82250ee5-f909-34fb-850f-103a4ae3e8d8 | -4.66234 | -48.48641 | 2025-11-26 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3cb0bab-09d8-3c99-871c-483224eb7a41 | -4.26763 | -45.12075 | 2025-11-26 03:57:00 | NPP-375D | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d4a998c3-477d-3f33-b0c2-92f3ea35c7e7 | -6.31147 | -43.79391 | 2025-11-26 03:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 19a9eaba-6e52-38a2-8bde-9a9ed02ff4d0 | -2.71395 | -45.69057 | 2025-11-26 03:57:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a067774f-e0d3-38eb-ad91-cc887cdca728 | -4.26044 | -45.1349 | 2025-11-26 03:57:00 | NPP-375D | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 99e3a964-fc00-3bdb-87c2-75d2ac08dbca | -6.48659 | -38.8229 | 2025-11-26 03:57:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3616ef9f-f929-33e1-ac26-ef034c70983a | -3.32927 | -50.27378 | 2025-11-26 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3b1eddda-6c0c-3bd9-87a1-16b97313c5ce | -6.58525 | -43.86367 | 2025-11-26 03:57:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 540587a4-53e4-3bde-8e94-3ca6fa95b48f | -2.7132 | -45.69193 | 2025-11-26 03:57:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c82ee2ad-8974-31be-b1c2-f6ac3fc555f6 | -4.17608 | -43.72313 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 960bc5f8-f6cf-30c8-ba39-d34422cd631f | -5.20944 | -42.90408 | 2025-11-26 03:57:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f3848d1f-0c2d-3c6a-bd5e-952d805fa163 | -6.85455 | -39.36205 | 2025-11-26 03:57:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| daf9cd1c-eb74-3185-a2b3-1a619ebe4510 | -5.6066 | -35.63537 | 2025-11-26 03:57:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b616b71a-9d83-3fc7-a5fc-8438ae651596 | -3.1761 | -48.62096 | 2025-11-26 03:57:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46066605-3aaa-32d4-aded-e6fb77e6230f | -5.31965 | -44.82649 | 2025-11-26 03:57:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c08b82df-feb0-3209-970f-701c0139e71f | -3.48755 | -50.4404 | 2025-11-26 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 67149685-6c30-3ed5-8eb0-9377e938dc83 | -4.4526 | -44.30285 | 2025-11-26 03:57:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a4e5a14a-cc2e-3386-8a22-60cb80865317 | -4.90677 | -43.7931 | 2025-11-26 03:57:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c5bce02-b80a-3ee6-8385-9350e08c12e5 | -4.23573 | -40.38813 | 2025-11-26 03:57:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2e3e3925-88bc-32dc-94ae-c9ef49e24054 | -4.14114 | -42.54447 | 2025-11-26 03:57:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7081245f-45de-3156-b08b-88fd75774a92 | -4.79157 | -48.28795 | 2025-11-26 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9189491d-5675-31c9-82a1-ce75315f452e | -5.23472 | -45.42529 | 2025-11-26 03:57:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9653e07-60c3-3aec-bf5c-a9025a399038 | -4.16915 | -43.73854 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| e83b3839-f017-3f48-b1e4-5f092488da7b | -6.10815 | -42.94989 | 2025-11-26 03:57:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3bca64a3-9386-37e6-9214-984873f46d5f | -5.05681 | -44.16097 | 2025-11-26 03:57:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc52ed75-e916-3b88-babe-71613f66fd7c | -4.41696 | -43.49246 | 2025-11-26 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 602bb60e-84c5-3f44-8777-86da0ddf3b7e | -2.48922 | -47.8171 | 2025-11-26 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f6a7c748-eea3-3903-8a16-1d59a266f02e | -3.32373 | -49.71762 | 2025-11-26 03:57:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 88db9510-450c-3308-a578-1e7a790ed6a0 | -6.0601 | -43.25972 | 2025-11-26 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d78635cc-fcdb-399f-baf4-4cc0e8815a3c | -7.16959 | -44.99038 | 2025-11-26 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6102f6dd-0867-3fda-bd78-e87832216dd3 | -4.72508 | -46.45806 | 2025-11-26 03:57:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d234127b-1d10-3a4b-8b46-5fd9fd916a48 | -7.2636 | -42.53821 | 2025-11-26 03:57:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6bf53bac-666f-321a-a7c0-57172ce3bd92 | -5.59305 | -45.18256 | 2025-11-26 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0741cd1d-b5d1-33f8-b99a-e99c4f8ee00a | -5.03357 | -43.25855 | 2025-11-26 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6f4e0eb-1d9a-3071-aa3a-edf3d654c551 | -2.49227 | -47.83438 | 2025-11-26 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8bf57ea0-17b5-3923-9fe0-8c14bc193a3a | -5.71856 | -39.49825 | 2025-11-26 03:57:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4793779d-9013-3a4a-8fc3-fe98de3aee23 | -2.54766 | -45.38831 | 2025-11-26 03:57:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ef7fb90b-b7f5-37c6-b040-e6475fad1e29 | -2.48648 | -47.83335 | 2025-11-26 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b086481-b3de-3304-af64-757cffcc05e7 | -5.33419 | -43.56539 | 2025-11-26 03:57:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6dc554bd-8002-307c-a02c-423dfbca020b | -4.26128 | -45.12987 | 2025-11-26 03:57:00 | NPP-375D | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1c94c4b-a00e-3b7a-a400-137528f5820b | -4.26598 | -45.13066 | 2025-11-26 03:57:00 | NPP-375D | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6558d79a-8ae6-3d14-8310-1fe8af2fd4fe | -5.29091 | -43.64059 | 2025-11-26 03:57:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d83fe73b-0d05-3044-a848-f214e8b39e47 | -3.14308 | -40.17898 | 2025-11-26 03:57:00 | NPP-375D | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7c249337-69bb-364d-914d-9e2f93d2991e | -2.50457 | -47.83226 | 2025-11-26 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a83b973f-f592-3a8e-bcc1-14a67bc04952 | -6.51041 | -38.82306 | 2025-11-26 03:57:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0011e8fd-818f-3967-b570-e07813fae56a | -2.50525 | -47.82816 | 2025-11-26 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8c580290-4841-3cde-addf-5bb69fe4901b | -3.3228 | -49.72295 | 2025-11-26 03:57:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e3015720-1cde-3530-9a1c-6ed873b2b848 | -4.18855 | -43.70071 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0b5f6fb-2194-3176-af92-60e94ade00a6 | -3.67843 | -43.57216 | 2025-11-26 03:57:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README9.md)
