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
| 0120c6df-e037-3ff2-ad0f-16795e5edb73 | -5.16199 | -55.99667 | 2026-09-27 07:31:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ca11b749-2401-3065-9cf3-ecd55dce8320 | -11.80578 | -50.4937 | 2026-09-27 07:33:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 9de06406-569d-3979-a0a3-302a8dda2bf5 | -11.7737 | -50.99736 | 2026-09-27 07:33:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 52.8 |
| c4d5903a-0530-36b4-a613-4534c57d0280 | -11.93881 | -50.48615 | 2026-09-27 07:33:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 9a47cf60-a6dc-3717-9acd-6bd72254cd2b | -7.27711 | -55.57067 | 2026-09-27 07:33:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e395c174-5993-3d3a-b1c3-6f3d77c362f9 | -8.03727 | -54.89546 | 2026-09-27 07:33:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| e996a27e-89f9-3106-9c02-b0f83ef2de77 | -11.27965 | -54.43998 | 2026-09-27 07:33:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 8ac32784-98ac-3f75-bb53-cfb0ca82e9c3 | -10.01905 | -50.12299 | 2026-09-27 07:33:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 3ed2edf1-1894-38a5-8584-5b2706802439 | -10.25073 | -59.12411 | 2026-09-27 07:33:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8794dc22-fdcf-3cd6-a6b4-a9b378ef7254 | -6.07149 | -57.82449 | 2026-09-27 07:33:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| eb364106-86d3-398f-9d89-148f1c8a32ff | -8.03914 | -54.88208 | 2026-09-27 07:33:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| b7e38b09-d989-3a22-836f-726435ba6c12 | -11.93017 | -50.48095 | 2026-09-27 07:33:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 8827e3ce-9cf9-34f6-8b54-cd404466635d | -6.63751 | -59.94969 | 2026-09-27 07:33:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 174d7e9a-f513-3451-a43f-8948608935e8 | -6.09224 | -57.62578 | 2026-09-27 07:33:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 158c99a0-b877-39c3-a59a-fdaa71f91898 | -10.81698 | -60.73817 | 2026-09-27 07:33:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 26f0d608-93f8-3fd9-942c-f3c3c5c9d801 | -7.68892 | -54.75399 | 2026-09-27 07:33:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c292e981-3fae-3718-9fa5-0456c5dd35c0 | -10.81838 | -60.72906 | 2026-09-27 07:33:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 1e7257e0-27ec-3ebf-9b4f-aba12168fd80 | -6.63891 | -59.94059 | 2026-09-27 07:33:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c2e15c3b-0e02-34ff-82c6-b2ef2ca3bb84 | -11.76322 | -50.98867 | 2026-09-27 07:33:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 34.6 |
| da548bc5-7b6e-34c8-b7c0-61006f0adedf | -6.07417 | -57.80665 | 2026-09-27 07:33:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3c356e59-180b-3596-a5c2-d90b93b2563a | -11.27137 | -54.43361 | 2026-09-27 07:33:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 26ee31ba-d02f-3ee6-8010-ef868fd9f3b2 | -6.07015 | -57.8334 | 2026-09-27 07:33:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ef2d6c9d-dd0b-33ab-8e4a-de6a62efa195 | -12.8953 | -61.71298 | 2026-09-27 07:35:00 | AQUA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| df68511b-6cb1-363d-b8fd-e16a9c9e4848 | -11.9434 | -50.4844 | 2026-09-27 07:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 109088d1-6c8a-3fa6-ab50-9bcb8b94a460 | -11.9434 | -50.4844 | 2026-09-27 07:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 0f6f9569-426c-35c6-9a52-225b08218f5f | -11.7643 | -51.0173 | 2026-09-27 07:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 91d42549-f709-3e5e-b20b-71fe5dd7e7ad | -11.9244 | -50.4866 | 2026-09-27 08:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 5c17b018-5ca3-3be2-b775-9c492cd1c946 | -11.9434 | -50.4844 | 2026-09-27 08:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 2e0c310d-e91e-3123-8cb4-39d136bdaca4 | -11.9434 | -50.4844 | 2026-09-27 08:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 3c509e1a-648e-3b0f-9816-54fe31127ae1 | -10.0159 | -50.1588 | 2026-09-27 08:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| eda0318f-892c-3f02-9acc-16d812502c9f | -10.0162 | -50.1374 | 2026-09-27 08:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 42feb96a-c27a-3610-987f-4aa32434cacb | -8.0373 | -54.8926 | 2026-09-27 08:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| ba88d513-422b-3227-bc54-ba9c17af362d | -10.0159 | -50.1588 | 2026-09-27 08:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 7b82bbfd-d106-3707-ae44-8f624b1a1991 | -11.9434 | -50.4844 | 2026-09-27 08:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 6c5576ed-8939-3a64-a7b4-b11d5af59523 | -10.0162 | -50.1374 | 2026-09-27 08:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| a45b7cc6-79f4-3d2a-962e-bc66b65f20a8 | -10.0162 | -50.1374 | 2026-09-27 09:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 66b3b4ad-3a9e-3797-a6b3-541888dd0d9b | -10.0162 | -50.1374 | 2026-09-27 09:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| e41e5c3b-83e5-3aed-82bb-168ae2466ee3 | -10.0159 | -50.1588 | 2026-09-27 09:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| b0ae72c8-3b3c-3abe-8df4-518fca7757a8 | -10.0159 | -50.1588 | 2026-09-27 09:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 54486532-1df4-37b0-8dc8-13bb00aacbaf | -10.0162 | -50.1374 | 2026-09-27 09:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 9a43a488-5c7b-3123-a606-89d4a6b0746d | -8.3586 | -44.1638 | 2026-09-27 10:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 131.9 |
| b6335999-8e37-3541-bd62-cbc27520265a | -10.0162 | -50.1374 | 2026-09-27 10:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 85304ab5-9a95-397b-9fce-5ab3a5516515 | -10.0159 | -50.1588 | 2026-09-27 10:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 944c17a1-d4a9-3e57-91d9-d5368dcdb5ff | -8.3589 | -44.1406 | 2026-09-27 10:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 0b525f17-5e0e-378c-85f2-151f698ce4b3 | -8.3586 | -44.1638 | 2026-09-27 10:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 202.4 |
| f5d61240-4c18-3006-910c-e9df53d7bc34 | -8.3778 | -44.1386 | 2026-09-27 10:50:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 477e43a8-a10c-395d-b149-cfbc1873213c | -8.3586 | -44.1638 | 2026-09-27 10:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 274.2 |
| ef6f1985-bdc7-3d9b-b8e3-bc0ad6fe2308 | -8.3589 | -44.1406 | 2026-09-27 10:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 168.1 |
| 863489c1-9a82-3c8b-a2e1-9f9eefca148b | -8.3775 | -44.1617 | 2026-09-27 10:50:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 87fcfec5-5a37-36a4-8338-ab03314ddc53 | -8.3778 | -44.1386 | 2026-09-27 11:00:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 6c0e329e-f68a-3d9b-b664-dc2a477e1611 | -11.9244 | -50.4866 | 2026-09-27 11:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 200aaede-3e35-3082-aab0-7559391d03a4 | -8.3589 | -44.1406 | 2026-09-27 11:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 176.1 |
| 577c9ec8-646c-3d2d-bde6-e0b7cd010241 | -8.3586 | -44.1638 | 2026-09-27 11:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 290.3 |
| 5cf52f8b-b3ec-399c-b8e0-292dd85d292f | -8.3397 | -44.1658 | 2026-09-27 11:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 02c436c0-3288-399b-a1ea-ad1d3ed877c0 | -8.3586 | -44.1638 | 2026-09-27 11:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 334.2 |
| 940e6de3-28ea-3542-a654-d18e58548dfd | -8.3589 | -44.1406 | 2026-09-27 11:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 162.2 |
| a2c7d393-7b50-3b1f-a464-57213c0fff7c | -8.36 | -44.16 | 2026-09-27 11:15:00 | MSG-03 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 68aefe36-219a-3269-abc6-ed3f4ab83639 | -8.3586 | -44.1638 | 2026-09-27 11:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 336.4 |
| 8c7ce18a-ae60-30fe-91af-71bb08e804f6 | -11.9244 | -50.4866 | 2026-09-27 11:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| fc5df371-5968-3fb3-8442-8a05db97c636 | -11.924 | -50.5081 | 2026-09-27 11:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| ed7decec-a6ca-3104-b5c8-0cc7718e6aec | -8.3778 | -44.1386 | 2026-09-27 11:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 87.1 |
| d5f9fc1f-7b66-37a8-977a-679d6c27212e | -8.3397 | -44.1658 | 2026-09-27 11:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| eb4a7db5-8df0-3d87-b6ba-9e294a6e0e48 | -8.3589 | -44.1406 | 2026-09-27 11:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 191.2 |
| 54161c86-c7ce-31c4-8672-6e7fd3ea6e80 | -11.9244 | -50.4866 | 2026-09-27 11:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| a19ecbcd-256d-3fdc-ac13-bc1491216e41 | -8.3586 | -44.1638 | 2026-09-27 11:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 342.1 |
| 72e1c2ad-ab11-37cd-aab3-bacc7cc1f5a2 | -8.3778 | -44.1386 | 2026-09-27 11:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 3054d4bb-813b-364c-ae23-59ddf0ff9b21 | -10.0162 | -50.1374 | 2026-09-27 11:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 8908179c-8017-3180-8b39-54a52acc7c48 | -8.3397 | -44.1658 | 2026-09-27 11:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 44e4fb37-933c-3a95-a035-4a3638d83ea3 | -10.0159 | -50.1588 | 2026-09-27 11:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 1acc6463-5635-3361-8c56-4cdbb8e3ed8e | -8.3589 | -44.1406 | 2026-09-27 11:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 174.5 |
| 4759a463-b5a5-34a6-b724-3ab43792e35c | -14.13 | -46.326 | 2026-09-27 11:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 78e0f2fb-c18e-381d-8c92-c20cacb0c7b7 | -8.34 | -44.1427 | 2026-09-27 11:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| ff6ec746-66be-38fc-8d7a-2a62a127a30e | -8.3586 | -44.1638 | 2026-09-27 11:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 716.1 |
| 3b7dca0d-a0d1-3f19-9b43-cb18ddcb27fe | -8.3397 | -44.1658 | 2026-09-27 11:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 37117a75-cab6-3e93-8de9-35eae5ba7ee1 | -8.3589 | -44.1406 | 2026-09-27 11:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 314.4 |
| a01641e6-0eb1-382f-8e78-916d466ef5f4 | -10.0162 | -50.1374 | 2026-09-27 11:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 89f49d68-ed1f-3b83-9b84-4839cb71fddf | -12.1366 | -50.3112 | 2026-09-27 11:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| c56cfa35-6a5e-3a8e-8e4d-985edc068af0 | -12.1175 | -50.3135 | 2026-09-27 11:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 06465565-ef09-302f-8236-399faf84c616 | -8.3778 | -44.1386 | 2026-09-27 11:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 174.2 |
| 6ad80cb2-2329-357f-acee-33316e025cb1 | -12.1362 | -50.3328 | 2026-09-27 11:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 9ac8a683-0c32-313c-8dcf-a7ef5f3a1d03 | -0.51443 | -49.1195 | 2026-09-27 11:42:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| e6d3cd7d-1e19-398f-a2e1-c5bc62530f5a | -3.42551 | -50.44014 | 2026-09-27 11:42:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ddbaddc8-4a06-3f80-9ba5-9a438e676a8e | -1.10405 | -47.94677 | 2026-09-27 11:42:00 | TERRA_M-M | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b95bdff6-2e0e-3737-befc-2175fb82517c | -0.52279 | -49.13226 | 2026-09-27 11:42:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| ca8c4e4c-4905-33d7-a440-61a0cd322be8 | -3.41688 | -50.42607 | 2026-09-27 11:42:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 0fa92d9f-0a43-3bba-9bfe-0ae7fbb472d2 | -0.51282 | -49.13089 | 2026-09-27 11:42:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| b577bbff-a90e-31da-9e7d-cffb004fa56e | -2.98204 | -44.28052 | 2026-09-27 11:42:00 | TERRA_M-M | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 264a80bc-1220-31ed-a560-36bc6a879bd3 | 0.51585 | -50.79646 | 2026-09-27 11:42:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 110.3 |
| e451b197-61fd-3921-b840-8cc2f8028ddf | -2.99138 | -44.28182 | 2026-09-27 11:42:00 | TERRA_M-M | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| e297605b-4906-3bd7-adb6-6fc25abe0900 | 0.5136 | -50.78087 | 2026-09-27 11:42:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 313c8038-3d2d-314d-bf11-1baae7436c43 | -4.56119 | -44.08223 | 2026-09-27 11:42:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 9729d1b0-1a2e-35f3-a65a-30e2a888af22 | -0.52439 | -49.12087 | 2026-09-27 11:42:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 8b8aabc1-2d1a-3a84-8cd6-173e00a7c906 | -5.42772 | -43.44387 | 2026-09-27 11:42:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 4d5b2020-40e8-3b09-802d-35c7bd2a9970 | -3.42738 | -50.42743 | 2026-09-27 11:42:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 7f86b52c-0996-398c-ad08-8e30e3e7a68a | -1.10545 | -47.9371 | 2026-09-27 11:42:00 | TERRA_M-M | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| f48aed10-0b9c-3087-871a-af056a26974c | -1.24916 | -49.06577 | 2026-09-27 11:42:00 | TERRA_M-M | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| ab0b3f24-08ad-38f3-bcfd-63863406ad9a | -3.67565 | -42.72353 | 2026-09-27 11:42:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 07d89c0e-0663-3e9a-abda-9b400c2220af | 0.31913 | -51.42865 | 2026-09-27 11:42:00 | TERRA_M-M | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 24.4 |
| ef8d3567-3f03-304d-b634-acad9eba1f8b | -11.06812 | -52.47899 | 2026-09-27 11:45:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 5d42a1ee-7031-31ff-b97a-96b414d47665 | -16.04776 | -44.91624 | 2026-09-27 11:45:00 | TERRA_M-M | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |


[Clique aqui para ver as próximas entradas](README53.md)
