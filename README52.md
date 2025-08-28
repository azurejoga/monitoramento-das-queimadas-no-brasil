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
| 9474f8ce-4743-38f5-b5ea-9c7538efeb52 | -8.23315 | -55.56772 | 2025-08-28 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2f89b53d-505b-317e-bd3a-6430ac575a68 | -7.37956 | -64.36502 | 2025-08-28 04:57:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2fe88681-e5d3-34f4-8ae1-30a676ec0537 | -7.74167 | -50.27512 | 2025-08-28 04:57:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8209e8a3-6b5c-3291-8801-7f409c5a2491 | -6.16016 | -44.39173 | 2025-08-28 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e495ab98-5fc9-3290-b700-a79c96b30fce | -5.52083 | -46.471 | 2025-08-28 04:57:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0099ce65-37d1-3873-a7f7-4e1ecee74561 | -7.34967 | -57.62594 | 2025-08-28 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 558606ea-c14d-3de7-a257-5f56246bfb4e | -7.2613 | -57.67107 | 2025-08-28 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f915df85-df0a-3f49-ba21-a6e4af01b44f | -6.75841 | -54.99525 | 2025-08-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 946a4cc2-2829-39a0-9089-74a999fec8f0 | -6.89117 | -62.92928 | 2025-08-28 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb757896-1d22-3f8b-8e6e-33f624204283 | -8.29158 | -45.145 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 670380d5-7a88-3157-a318-54b34715fe1f | -6.91917 | -62.94134 | 2025-08-28 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7f635d6-5f20-3acf-955c-39ef01eed461 | -6.65224 | -53.1897 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aa363c02-9cd0-3460-8318-793ccf1f5008 | -8.28319 | -45.16613 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 86e0e1cd-1684-3e22-93e9-a8b93e650829 | -7.41634 | -60.62576 | 2025-08-28 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9699a975-b1e6-3cad-b3eb-3c456a0a6027 | -7.37274 | -64.37135 | 2025-08-28 04:57:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| fa33bd68-5ad3-3ae5-aa97-0cecb4b89dbe | -5.7542 | -53.76055 | 2025-08-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a1bd9f0-4254-3438-a40f-88e510cd9f33 | -7.73362 | -50.29193 | 2025-08-28 04:57:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a5b168e9-2d15-310f-808d-1c6553ae0837 | -9.43398 | -48.24809 | 2025-08-28 04:57:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1ee1d68-c50c-3f63-9698-034094024486 | -7.42299 | -42.05731 | 2025-08-28 04:57:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 6396b5ca-0ba6-30bc-b818-230765ba278e | -9.05931 | -54.94326 | 2025-08-28 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5ef2c78-77bd-380a-a7f6-f9ed76ca9481 | -9.66134 | -48.30683 | 2025-08-28 04:57:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 76eb3c5b-6c98-38a1-b020-ae8f46712395 | -5.91246 | -46.16132 | 2025-08-28 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08b9d935-d05f-3360-8ee9-30c9fee703d2 | -6.18577 | -44.16389 | 2025-08-28 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba4384a7-d6d0-3d1a-9dac-9c4fb2b2c807 | -3.98312 | -47.88247 | 2025-08-28 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0cb1f0c9-dc94-37e5-a44e-6ebbdc3520e1 | -4.15924 | -43.88233 | 2025-08-28 04:57:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 903f2747-5f76-3cab-a5e6-93cb5eaf7bb3 | -6.16958 | -44.06846 | 2025-08-28 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab08aaeb-d7a3-310e-a7da-542110072642 | -6.15921 | -44.18811 | 2025-08-28 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed0eeb9d-c5f8-3c8e-a58f-51c8e32d885c | -6.08282 | -44.00663 | 2025-08-28 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c176e0a-194c-3bec-8ba8-6f7ee6e00fcc | -6.81381 | -45.00167 | 2025-08-28 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5ac14cc-6c81-34b4-8c4d-c61ccf798f4a | -3.7854 | -45.03852 | 2025-08-28 04:57:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 319f3beb-3944-35e7-8f08-26eb785e1561 | -5.15757 | -47.84502 | 2025-08-28 04:57:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04b588c1-599b-3ccd-bb97-9aa10d01da27 | -6.13296 | -44.42308 | 2025-08-28 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5aa68f2b-7145-3f56-907f-243aa95baecf | -3.7619 | -54.81752 | 2025-08-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5363f6d0-e293-373f-965e-367c80067030 | -8.29518 | -45.16018 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0e7fb97e-4f92-349c-bc2f-2d0b1fe1a5ee | -7.96993 | -55.29605 | 2025-08-28 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 65cbee47-2b65-3e65-9c72-ca6e75165c9c | -6.87505 | -43.62045 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 05324619-bc20-3a9e-9bcf-fc4c22925208 | -4.51399 | -43.64085 | 2025-08-28 04:57:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e589e61b-b03b-3f8f-b266-5a1e7fd5428a | -5.80535 | -59.21411 | 2025-08-28 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22141b5c-41b8-33ea-8b75-a806ed65465d | -6.1796 | -44.1664 | 2025-08-28 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c08fc98b-0d81-3fbb-8630-92963e60f05b | -8.24485 | -45.07184 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 26d312fa-cfb9-3e69-a942-a523079033d8 | -6.92582 | -62.9333 | 2025-08-28 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da327e8a-0adc-3d3d-acf4-8075b0153332 | -9.44953 | -49.45159 | 2025-08-28 04:57:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 63a76c9c-51b6-311e-a7ba-b578adc73146 | -4.00299 | -55.85011 | 2025-08-28 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ecd4955b-a652-3756-8cab-122a12888d9f | -5.90525 | -45.56365 | 2025-08-28 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 582a64fc-74af-311b-ba39-48aab36dd807 | -8.08744 | -44.9869 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e435db26-9127-31cb-ac38-274059d6fe81 | -3.74492 | -49.05134 | 2025-08-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32cb0281-a791-355f-96cd-403402f33a6c | -4.78691 | -47.27539 | 2025-08-28 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a87ec74c-e5b0-317a-adfe-900f0a34943a | -7.74907 | -61.08054 | 2025-08-28 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| de5897d1-3a5b-3d4e-a37b-346a41e4feaa | -7.90132 | -44.77743 | 2025-08-28 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7d963a8-cdaa-37e7-ad13-620e34494fee | -6.24122 | -43.37939 | 2025-08-28 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ec271a0-06f3-3891-8911-75bd5cc17e1d | -9.66527 | -48.31196 | 2025-08-28 04:57:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7dd1171-17d9-3b15-be07-f8c332456dd8 | -9.96323 | -46.51145 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31e9a8c2-c0d4-37ec-b25b-68831f44a196 | -5.89965 | -45.56591 | 2025-08-28 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96a3def4-9612-3e0e-8df4-d1c5cf76a968 | -7.22164 | -45.3119 | 2025-08-28 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51bf68db-3ef2-3367-9bd9-b9d6a8a9aa96 | -4.56082 | -55.96321 | 2025-08-28 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be1d5be9-ca46-3e9e-bd36-4f1d9d0af167 | -4.05624 | -56.33323 | 2025-08-28 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49dd09b7-787b-35f7-b7c4-f3bdcc1f78a6 | -3.23693 | -50.8065 | 2025-08-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d94e4a0c-d7d4-34c8-ba5b-4f4623e7cf9b | -7.43273 | -57.62663 | 2025-08-28 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df28a40a-4e67-3d4e-8700-9d2661ac1bce | -6.23583 | -43.37414 | 2025-08-28 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba2a2fd1-632d-38a0-94f0-014ae2f8faf9 | -3.73696 | -48.9415 | 2025-08-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6f14220b-7c5d-31d2-abbc-8bbd538e4ab7 | -4.56141 | -55.95949 | 2025-08-28 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60020f49-a9ce-3afe-9b4b-6905344f5fe8 | -7.96937 | -55.29953 | 2025-08-28 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e2f1cad-c7ff-3ea4-8134-9709dce2db5b | -8.55619 | -51.32125 | 2025-08-28 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4d1d92c-0577-343d-80ac-9e3c737bdd9a | -6.16547 | -47.2758 | 2025-08-28 04:57:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 389aa6e9-1ae7-3df9-9b0a-d5185e57f899 | -6.88329 | -43.60416 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| fb38b6be-3205-3ef5-ad75-86e2909658fb | -6.43931 | -44.56894 | 2025-08-28 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7fffb8ec-9019-3bcd-8e01-7344f159bfdf | -9.43516 | -48.25073 | 2025-08-28 04:57:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6954416a-6cbc-3120-aa6d-7e6a821583e7 | -8.44196 | -41.45586 | 2025-08-28 04:57:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 218ee6fe-dfbf-3a9c-b94c-1b0f51910881 | -5.3184 | -55.88108 | 2025-08-28 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9df20261-a01b-3be0-9a7d-67096e621f31 | -9.45018 | -51.96157 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 8021f53b-8c0d-3542-b848-cbf4748cbd3d | -7.60495 | -63.34335 | 2025-08-28 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0505cb4-2ddc-3653-97ef-6ccae5a36aa4 | -6.23894 | -60.01378 | 2025-08-28 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8094ede8-1115-3423-8f9d-fe5f973c57d7 | -6.12889 | -44.41105 | 2025-08-28 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0ffa0191-b54a-3c53-a0b1-e89eb605c389 | -6.24666 | -60.01916 | 2025-08-28 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ffff76c3-39b4-31b9-ae4a-58069f92074a | -3.78885 | -47.57132 | 2025-08-28 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46e0d549-b7cf-3e17-b965-b4c2c268e270 | -7.4892 | -45.04242 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 37ab489a-0ac6-3c63-b2a6-ece88654914e | -8.45358 | -43.65454 | 2025-08-28 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ebcc889c-6c17-3929-8d2b-867053165f52 | -3.76802 | -54.82207 | 2025-08-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d9321c4-c7d6-3e86-94fc-3db93f53bdce | -3.23533 | -43.43701 | 2025-08-28 04:57:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 69dba290-e8f7-3655-a30e-cef7f09b551e | -4.79349 | -47.26207 | 2025-08-28 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7b6ee720-252b-3731-bf0b-66a8a8d6416f | -8.29273 | -45.17875 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 934da5ad-9aef-37a2-acb0-66dc8ec47b1d | -8.55986 | -51.32187 | 2025-08-28 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0c0ec0a3-1b6f-3bac-8e3b-067c0dd92137 | -6.86796 | -43.6281 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e7c71eca-17f6-3b20-a4e0-694329c6a39d | -3.81801 | -51.22599 | 2025-08-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 892f0ce2-d697-3288-a1c5-c52e7862f496 | -8.29707 | -45.14587 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bf0b7eaa-b4ad-3491-a6af-70b7cc67f76b | -6.8708 | -43.60652 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c216263c-9bbe-33b1-b0e9-e159b4649212 | -6.44434 | -44.57377 | 2025-08-28 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0626e589-a981-3e8c-90b7-64e526d5b3a8 | -6.17724 | -44.01179 | 2025-08-28 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7cb6aeca-ab4c-35af-ac22-bb8f7a2d8616 | -6.49463 | -53.39392 | 2025-08-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a1c0c4c6-f984-32a7-b89f-406d0df19531 | -6.18635 | -44.15964 | 2025-08-28 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25580389-7125-3494-97e9-8c4f409334f2 | -8.2397 | -45.07077 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25f25a25-a672-3aef-8ecc-129ee7b085d9 | -8.23922 | -45.07432 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2d48369a-f9a2-353d-ba1c-a169ff4d2c11 | -8.45246 | -43.65576 | 2025-08-28 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23fd0071-546e-3d50-bbb0-dfba6fb60e5e | -7.5426 | -63.83875 | 2025-08-28 04:57:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 307df03f-bfce-3fd4-8606-cf38d6522229 | -6.8691 | -43.61943 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 240b77be-fe8c-3e22-ad27-d00dbb7aebde | -6.19198 | -44.16101 | 2025-08-28 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a37fc3c0-3f99-3587-9499-974122a09fa0 | -3.75912 | -54.81348 | 2025-08-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 442528d7-beeb-3d7d-9b80-7bc24b0c9b86 | -9.44806 | -51.96292 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8383502e-4f0b-3df4-b9d4-f55b599b62d1 | -7.43338 | -57.62262 | 2025-08-28 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c09e74ed-aa83-3d7e-9823-bb3b7b592cd5 | -8.45185 | -43.66032 | 2025-08-28 04:57:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README53.md)
