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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4bad868-0b79-354f-9e2e-5c716ee3f55e | -2.84298 | -54.08045 | 2025-10-18 04:49:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2752f3a-82ac-3b03-b37b-78df21fd5993 | -8.23788 | -44.01256 | 2025-10-18 04:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 13d6c4d7-97c3-3158-bed2-2e9e56b2794f | -9.72036 | -44.56418 | 2025-10-18 04:49:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9e632058-4730-3733-b784-69f4a82103c8 | -6.23475 | -44.16053 | 2025-10-18 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d39afc83-2f6f-3f76-b0fb-68e0a501245c | -9.03223 | -47.72043 | 2025-10-18 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84734f24-1ffb-386b-954e-e0891187c934 | -7.75791 | -42.51021 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2febadd9-1c29-3bdd-a7a1-503789bb2c75 | -2.92334 | -49.17789 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 064b40a4-c78c-3c5b-994a-37bba9b03355 | -8.54542 | -44.58162 | 2025-10-18 04:49:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 051829f3-7d16-311e-a647-4f3bdc89ec1f | -2.8718 | -50.73669 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00c8ebb3-1f28-3582-aaae-42cf78473164 | -4.93631 | -49.76377 | 2025-10-18 04:49:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a09f9844-be0c-3976-9aff-6c0a3921f1aa | -6.29655 | -44.7214 | 2025-10-18 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6bc6a342-98cb-3b2b-bf74-4ded701774a0 | -6.32044 | -44.31172 | 2025-10-18 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ca7c753-83ba-3885-9ded-eb39059587ab | -7.14487 | -46.41123 | 2025-10-18 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba602050-8ba8-3045-90a5-ade803cfc6f0 | -3.3313 | -50.10577 | 2025-10-18 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 578c9c98-89cc-3886-a46f-16a0dd6eaae6 | -6.54913 | -43.91557 | 2025-10-18 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c35b4e0c-e0ba-3b16-bdde-5e5a8d0873fe | -3.52758 | -50.30579 | 2025-10-18 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0974f49c-398b-31e1-bfba-3c10b4acf177 | -7.57807 | -44.98392 | 2025-10-18 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 38737bf9-003f-3470-89ae-b98c39525da4 | -7.17527 | -42.17901 | 2025-10-18 04:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b22a4fc0-9ad0-3c93-a605-cbf9cad4e775 | -5.8928 | -44.70674 | 2025-10-18 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86b9c24c-2ef5-3dea-9259-a394d1af890b | -2.74542 | -49.3933 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69230edd-c4ca-3a02-b940-40456e747fa8 | -3.37224 | -52.17516 | 2025-10-18 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2e439f1-0bc9-3e10-8eb3-334d4b7f59ae | -5.98582 | -44.15043 | 2025-10-18 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6cbc3262-f8c0-385d-9be5-6f368a458d9c | -2.65975 | -47.87003 | 2025-10-18 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5835700e-801e-3fd3-9617-1c95ef832673 | -3.75546 | -49.04115 | 2025-10-18 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| affd716a-6813-3324-9bf2-7b20120360e0 | -6.5846 | -47.07588 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 878f7190-6436-373e-acaf-43d62b5af92a | -8.55775 | -50.08106 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03ae60ff-0a69-352f-9fe9-00a90efcec45 | -2.87622 | -50.73022 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 043def12-5861-36e9-b42d-a44e12e2c1e9 | -9.08437 | -48.02949 | 2025-10-18 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3dd7a9e-2481-3ffe-99d5-099eeb5ff85e | -3.50595 | -52.91752 | 2025-10-18 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb8956ee-ed9a-33ed-a4c7-bf87a1d929bf | -8.18316 | -47.04138 | 2025-10-18 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6989a7da-84ad-3387-920f-d3da98cd07ae | -7.34837 | -43.86295 | 2025-10-18 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cebf56a7-e33f-3a5a-aca3-33460647b1f9 | -7.4527 | -46.52904 | 2025-10-18 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9bc10b4-7718-3ea8-8ae0-b221821e28c2 | -7.80046 | -54.93908 | 2025-10-18 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 46adf992-ef98-38fa-9af2-ca1f9385078f | -2.72345 | -48.83647 | 2025-10-18 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4d15b097-6a78-3b4d-901a-673d7ec91790 | -6.42701 | -47.2991 | 2025-10-18 04:49:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9f0b255e-e992-3a0d-93bc-6efa07d08c6a | -5.89205 | -44.71206 | 2025-10-18 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed0f3537-35a9-377d-a053-0537b9601f58 | -5.12313 | -45.12502 | 2025-10-18 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 27e971e6-19d8-37c6-bb84-cf720afe514c | -7.48963 | -47.02902 | 2025-10-18 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 323479e2-99ca-32ec-9f26-caad53b0860c | -5.99045 | -44.15383 | 2025-10-18 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5384cdfd-59c2-30c5-8330-30414c7040f7 | -7.33757 | -43.86435 | 2025-10-18 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3af4ba5-535a-323c-9d35-4787d590cf5f | -9.72755 | -44.54941 | 2025-10-18 04:49:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0979a079-8e4a-35b0-ad97-cc38dd87721d | -6.24506 | -46.39029 | 2025-10-18 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01c180c9-de96-3b3e-a9e9-38aa0964ffc3 | -8.94535 | -46.57255 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff473380-065d-360c-a5fb-c09951e39429 | -4.87289 | -46.70549 | 2025-10-18 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b6c2263-4120-372a-af47-71221955f2de | -3.97741 | -59.16916 | 2025-10-18 04:49:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5624be9c-c956-3ca4-af25-98656d233cdb | -8.36056 | -46.23881 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dfcafebc-5003-347f-a34e-d77c45fb6a38 | -4.25069 | -48.56467 | 2025-10-18 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bac5f566-4459-3e11-bbb0-08010f069b4e | -7.36791 | -44.23279 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| beeaa14c-2453-3775-8493-e1bde6dd70d3 | -4.33484 | -51.08936 | 2025-10-18 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6328badc-3cd4-3f63-a28a-438b72bbb9b9 | -4.37511 | -46.53421 | 2025-10-18 04:49:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37876acf-347d-3d53-90a5-f89ecddfe604 | -7.65867 | -44.64465 | 2025-10-18 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2c15edd-7068-3226-aa38-917a639156f0 | -9.71996 | -44.56721 | 2025-10-18 04:49:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2f792a98-a051-359a-a3bc-0c993db5d117 | -5.35622 | -45.03583 | 2025-10-18 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03c7fadd-5476-3434-82c0-cda9e7e94eea | -8.80889 | -49.68533 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21b9a834-c35c-35f4-9840-305fc4dd61a5 | -2.79096 | -49.59595 | 2025-10-18 04:49:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc40f8e5-8fa0-364d-8df5-1c94ba8cc259 | -7.44475 | -44.74829 | 2025-10-18 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ce1125a-d394-3ada-b82b-c994c430b4e2 | -4.39711 | -43.4357 | 2025-10-18 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24566a96-bc91-3a25-b52b-75ab5358741f | -5.09358 | -49.0662 | 2025-10-18 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8578db7c-89a5-3a42-a515-d3378e6ffd10 | -3.54972 | -53.11013 | 2025-10-18 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6fdb26bf-0944-369b-b48e-7e8b90361591 | -3.24957 | -45.96926 | 2025-10-18 04:49:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49c7d7b6-ac64-3e0d-b49c-c2b6ac00777e | -3.52269 | -52.89847 | 2025-10-18 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6bbb80f-5109-38d3-9a60-6dd5bc315e8c | -2.74255 | -49.38901 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31091954-7cbb-3b38-8378-3ae4919d5753 | -5.26001 | -50.90762 | 2025-10-18 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99717018-d5f7-3ec9-8b21-dd0ee6602754 | -2.44417 | -49.37215 | 2025-10-18 04:49:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a6a4c6b8-d839-37c9-a1c5-6129961a9fb2 | -6.33763 | -44.00777 | 2025-10-18 04:49:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc6ecf0a-2f46-3681-81fd-fd30db167e34 | -8.35994 | -46.21145 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aac3b8cd-a0cb-394a-acb4-efe3c66a1a21 | -3.14079 | -50.25356 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2862f9e2-0c59-3bbe-92e1-b6870c0bac4a | -3.42064 | -52.72755 | 2025-10-18 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24cf7a8f-5637-329b-8a81-cb156efd81f2 | -6.3706 | -45.78164 | 2025-10-18 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1daa2854-06c4-3c63-acff-72628eecf075 | -5.93057 | -44.95255 | 2025-10-18 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1543de4e-a9dc-3066-b7f7-c3d122c34024 | -7.76421 | -42.50677 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 457ca67a-c647-3329-9ce6-8b0db9a7ea11 | -5.89782 | -43.901 | 2025-10-18 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb42638f-3a92-3405-a33c-8df53ce6c507 | -3.06371 | -43.22408 | 2025-10-18 04:49:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2fb96161-e90d-33d0-bc27-a3c47b73664b | -6.48488 | -44.56015 | 2025-10-18 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddad0210-d9e3-36c7-ab76-c660606d9f04 | -3.14246 | -50.24282 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| c64be9b8-5290-376f-84c3-9f85837a8a32 | -4.45752 | -43.23957 | 2025-10-18 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 178b939e-394b-3fbe-afa1-e17873d5baf4 | -6.1294 | -44.21725 | 2025-10-18 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6cea6c62-3b57-31e3-8163-7d8f4533e840 | -5.36949 | -45.9555 | 2025-10-18 04:49:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c9f6ee9-55e4-389e-92a0-e334ce04988c | -2.78118 | -48.72257 | 2025-10-18 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19198a0d-47c3-3228-a42b-338843a37f6d | -3.85061 | -41.58834 | 2025-10-18 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 51f4da28-4313-34af-921e-7a198d0c84c9 | -3.49333 | -42.72784 | 2025-10-18 04:49:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11efc82b-0003-35f1-8eb6-4f302b712c09 | -6.65996 | -46.53419 | 2025-10-18 04:49:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af3aa7ed-12dc-39f2-91e2-1891dbeb5be1 | -5.5774 | -44.18259 | 2025-10-18 04:49:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1848d1a0-eb23-358b-9280-da3b9039c7f3 | -8.75059 | -48.59753 | 2025-10-18 04:49:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8c55d75-b50a-3953-a22d-4736021e5387 | -7.18052 | -42.18394 | 2025-10-18 04:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 05023f46-739e-354c-87f9-d66e5b46e3d1 | -9.75342 | -43.95895 | 2025-10-18 04:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a72624a3-36ad-332b-8c8b-684db26494a4 | -7.79764 | -54.93474 | 2025-10-18 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7fae073-a276-36d7-abdd-a733ca2cf08e | -6.37259 | -45.76821 | 2025-10-18 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a545abf-38d6-3d6d-99f6-9a58d70d7b74 | -5.92366 | -45.44767 | 2025-10-18 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 34938ba5-aca5-32c3-8363-74986782b423 | -3.83903 | -52.23101 | 2025-10-18 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd2da45b-0916-313f-99af-2dafe45fed6f | -8.36228 | -46.20963 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 278dca13-0b4c-3bcf-ae4a-fd0560e5d2d4 | -5.2975 | -47.93548 | 2025-10-18 04:49:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e776bd4-ffd9-36cb-9506-c5c4e3141f26 | -6.44572 | -43.81351 | 2025-10-18 04:49:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 660fa55e-e12b-3803-90e1-c4d47d865192 | -5.36318 | -45.56889 | 2025-10-18 04:49:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 261cea32-d333-3c96-b0ab-e3bb68982a9d | -3.12952 | -50.21504 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 906719be-3441-377b-bdf1-77c9a0783148 | -7.42769 | -46.89291 | 2025-10-18 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8e239bd-cb69-3111-8f92-d78a35698395 | -6.41212 | -43.472 | 2025-10-18 04:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50866313-cfbc-3f8a-bdd2-cd88e9f6f8da | -7.14299 | -46.42397 | 2025-10-18 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f1ba659-9e83-36e3-beaa-377a1fdba0ae | -4.71151 | -44.36258 | 2025-10-18 04:49:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d435df61-8b1a-367c-ad19-ca2b7e7e215b | -6.52475 | -41.4891 | 2025-10-18 04:49:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README76.md)
