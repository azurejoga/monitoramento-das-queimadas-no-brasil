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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4773e8c0-ea2a-3a3e-806e-5c3307617e4e | -5.20616 | -60.04765 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 565c2a90-158e-39aa-b393-3f6a050e1c48 | -8.29954 | -55.11182 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2a0f7ff1-50b6-3d2b-b8e3-5832db7d7f40 | -8.43706 | -54.69447 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 999a46ad-04c2-3308-8000-00ce107a072f | -3.19936 | -61.20752 | 2026-09-03 04:57:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae978a04-c9a6-3038-9647-4b07f3326001 | -8.43926 | -54.70227 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c3b28bd-cfa5-317f-bd7b-a5d0476e27a2 | -4.24192 | -62.23892 | 2026-09-03 04:57:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0104477d-b57d-3097-b134-2963c0af0e94 | -6.62457 | -55.23451 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f48dbda-d2b4-3edc-9cfd-82ee3a711415 | -7.04606 | -59.22086 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c72ee36-e336-39dc-ac45-06e7c750f7e0 | -4.54315 | -54.91454 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c099ad8-6607-3179-9230-967a71c3f7ca | -6.15874 | -53.75113 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 406a34a4-4238-33a3-865b-a8e32e8641ae | -7.45447 | -61.37719 | 2026-09-03 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bbca8f9f-abc4-3647-9c83-148799357596 | -8.45913 | -54.66477 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb905a89-0f36-3419-8267-15a5602c85ee | -6.69123 | -59.95481 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 689303a5-005d-3d2d-90be-a141afcb4566 | -3.02811 | -61.48682 | 2026-09-03 04:57:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae6b6ff2-6341-306c-8620-c735c987e660 | -6.31395 | -56.04725 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a08b5de0-2d8a-3e06-a229-abdfc678406b | -4.97008 | -55.85439 | 2026-09-03 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1590e057-1baf-30e4-900f-bb9178e99b88 | -8.47154 | -54.652 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1efd322-1e63-3389-b6bb-14a63a45ae25 | -8.46586 | -54.66586 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef8c245b-9240-317d-a7f4-b896f1d6f728 | -4.97215 | -55.84166 | 2026-09-03 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01c58f92-895d-313d-b3d8-813a722f5373 | -5.24984 | -55.90864 | 2026-09-03 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c822e479-8f4c-373d-840f-0211295ad768 | -8.46538 | -54.64732 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 2c4b83bb-4c01-3f61-9626-413031c9c725 | -5.97368 | -53.59141 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdac4125-245c-3b4c-95ea-13d802ef8efa | -6.9461 | -58.98738 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55ef6592-44dd-330a-9776-117b7a59d8f5 | -10.56362 | -47.72453 | 2026-09-03 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7dd762e2-fc53-3da1-b480-5318a6194b2a | -8.07858 | -50.97771 | 2026-09-03 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 55e6e0f0-3e31-37e5-9ae0-2188d994c636 | -8.43843 | -54.75045 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39492088-7161-319b-8d0e-f8a76ad4efca | -10.89015 | -45.32117 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14e92aba-697a-3dcb-8b1f-0d6e95db58be | -6.61922 | -55.24555 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95042270-ff86-33bc-832a-cc00b17b560e | -7.32071 | -55.13223 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37b3a689-452c-3422-87b5-4b8597f827eb | -6.5198 | -49.83286 | 2026-09-03 04:57:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d1a6d99-bfe3-3530-a367-c8dbb3e885b9 | -6.30449 | -56.03698 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c44fec5f-a06f-3087-95e0-cdc0d0df19d8 | -8.08493 | -50.95911 | 2026-09-03 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aec85c5f-1550-302c-ac6c-ff8be8b13ef2 | -5.59164 | -60.23647 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43338422-c81d-3525-9b28-98455924cd9a | -3.55217 | -59.0413 | 2026-09-03 04:57:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 13f9b3fe-015f-36e5-9e17-1d22a716f640 | -5.4637 | -60.06378 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 39273d99-c320-3a07-8461-0d5adaf5f784 | -4.69197 | -56.06496 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a78f1cc-cf5c-3e00-8e83-5b40c3e9fa9a | -9.61049 | -48.56096 | 2026-09-03 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3c53b43f-e13b-31a7-bc8f-967596021651 | -3.83118 | -59.39942 | 2026-09-03 04:57:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| baeac65f-5194-308a-80d6-177e1dde3453 | -4.63016 | -55.73427 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d59d9d1-2ef5-363a-904e-a97ff2742a6f | -6.68911 | -59.93941 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 000c7e44-0aed-31a2-8f36-c99430a9cef3 | -6.75139 | -59.43936 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5d27c41-fd18-35ee-98f4-a15b0b742a04 | -8.42579 | -54.70005 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cea94643-d2c8-320d-b565-0f62b5500df9 | -8.45576 | -54.66422 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c643b04-e120-39ba-8845-a30cc8cf5d09 | -5.85551 | -57.56097 | 2026-09-03 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f00a5c4b-d727-3780-a2b1-4fdb01f28850 | -6.62146 | -55.25385 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2863c89e-6ea5-3e9c-9317-4101e08fedaf | -8.13037 | -54.94456 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17afbe34-8741-3120-bff2-a6a9879b5105 | -10.99553 | -45.09298 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| e1b03051-c1e7-36c5-89b4-3204d53f0f10 | -11.30461 | -45.13983 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dcac3443-79b1-3807-8712-08b648d39343 | -6.04874 | -53.80224 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b9c8f6ab-ccae-371a-ba92-ad2c5cd48bb5 | -8.44239 | -54.74738 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 72691f8c-e314-304d-8198-600a1134f59c | -4.63086 | -55.73003 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e2ad0bc9-c874-3077-8e1c-a6cb42bb3d8f | -10.56303 | -47.72876 | 2026-09-03 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bbc19c80-195b-3c54-8c4a-8e3460e4c638 | -6.6252 | -55.23065 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 37523909-600a-3646-b63a-e3ef03dc47d8 | -7.18249 | -55.48433 | 2026-09-03 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1dc9afa-01c2-336d-a8a8-06b535242c8c | -6.75902 | -44.56987 | 2026-09-03 04:57:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1eff548a-1014-3e56-bc3e-3262118a1b0e | -8.08608 | -50.97494 | 2026-09-03 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2508b805-d32a-3847-ae0f-f050f6b6aea9 | -6.64968 | -59.4279 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e18a7187-de0c-3214-84c6-78307da24a88 | -8.79447 | -54.58672 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8ab8e610-299b-3df8-bc02-6f3a33f5441d | -6.05152 | -53.8063 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b3ca728-e743-36be-a9c0-d9c776b8c3cc | -6.32412 | -56.05329 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 20b3a0e3-2d7f-390a-b87c-9a50dbfcf1b5 | -7.82482 | -47.67094 | 2026-09-03 04:57:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb4d1049-9f8e-3ca6-b7fb-e7e8a5efb4b8 | -3.38994 | -59.36599 | 2026-09-03 04:57:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c741671-c4ee-3e77-b2c0-9b533c67baa9 | -5.26147 | -60.18531 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 23cc3bc3-0393-32f8-a164-df0d9cf0b4b0 | -10.91788 | -45.34652 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3dcd85f8-e3c1-355f-a1f2-ff68b7d51c64 | -7.04534 | -59.2251 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0aa43599-a89f-3923-bea9-b6f5091dd257 | -4.94202 | -55.79744 | 2026-09-03 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a58a2171-5004-3fb2-b7c2-10de2e3d79f6 | -10.99035 | -45.09224 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| f1e89690-48b6-363d-86f9-d515a214f48b | -10.89056 | -45.31808 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2924c541-9183-3120-918c-f8e3d1359800 | -4.2646 | -55.15535 | 2026-09-03 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e39e1c47-68b1-34a3-93b6-b49bdeff00cc | -10.47911 | -51.32647 | 2026-09-03 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cb176f48-0306-362a-93b3-e1075ea468bf | -8.43506 | -54.74989 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 8ced0d53-127c-38b7-906c-a063a19bb8e1 | -5.5893 | -61.47527 | 2026-09-03 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85fbb937-ba1e-3116-b5cb-8e8d9d27c852 | -5.59961 | -60.24573 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a34f9513-06b2-3d9e-ad4b-2fbc6e3b2862 | -7.26996 | -61.11495 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a6ce3d70-0f0a-3f70-bee9-10badb994c3d | -6.25943 | -55.43289 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98e13ac9-8902-3126-8b9b-507aac798444 | -8.07974 | -50.97005 | 2026-09-03 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| e8e4ea5c-00c8-3b41-84a2-86521a3cf0ab | -6.11471 | -53.76935 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c35aa6fa-51f6-39da-b857-3a1551a8ff0a | -10.87685 | -45.30391 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 2f814279-8e14-35a6-a03b-625351202ca1 | -6.76551 | -59.43713 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 02ca743b-ca8a-3a88-871c-ad3046213d17 | -4.35379 | -55.03096 | 2026-09-03 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57b5ecc8-e080-34cd-8f23-7f90b7ec0879 | -10.99077 | -49.67439 | 2026-09-03 04:57:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2418b47-dbbe-3dc5-90a9-60cd8119c12e | -8.46073 | -44.69359 | 2026-09-03 04:57:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ede8ff5f-bccb-3a8f-b933-3462aa4437e2 | -5.32699 | -60.14467 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c9fa4e8c-5c29-3e3f-a92c-ac2989ffd8bc | -10.27859 | -60.5342 | 2026-09-03 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4fb1c149-e685-34d1-aa17-b482a5c57817 | -8.13097 | -54.94091 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f96ab7a-56f2-33fa-9b35-78da32136349 | -9.82932 | -59.4794 | 2026-09-03 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0864651-b8d5-3896-8c30-7445fd27a24b | -9.08512 | -47.81852 | 2026-09-03 04:57:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 626f5d36-cafa-3683-a657-911b62fd0490 | -4.23502 | -62.24556 | 2026-09-03 04:57:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38c2ffc2-9e93-3f3d-a428-c6a03a95a583 | -12.08942 | -47.06634 | 2026-09-03 04:57:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4a10fe81-0c3f-30d5-b3d7-0df963671b99 | -3.12657 | -61.2294 | 2026-09-03 04:57:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 475cd1f6-d195-3057-a526-13349de551bc | -3.20077 | -61.23174 | 2026-09-03 04:57:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3bc75b0-041b-351e-8237-431fd59be708 | -6.68286 | -59.94822 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4cabd552-3196-3b26-a1e5-4020539173e8 | -10.87644 | -45.307 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4dda52b5-29e2-3f07-acbb-cba578f36a6b | -8.07685 | -50.96568 | 2026-09-03 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7767fd3e-3b5b-3159-9947-661bb414641f | -6.59925 | -59.11416 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4070868-9fc0-3e39-b126-d02dae1bebc5 | -9.60288 | -48.58489 | 2026-09-03 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41cd9741-59d8-310a-a37d-f1f645c6f052 | -8.4647 | -54.67305 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4fa63603-b963-3547-99e2-27efdd12c54f | -9.09051 | -53.04554 | 2026-09-03 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b43ab607-9cfe-3e47-9685-f962d2c17565 | -9.03536 | -65.74802 | 2026-09-03 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56399e8f-3d42-3527-bc5b-6f08c00c61c7 | -9.01882 | -65.45135 | 2026-09-03 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README35.md)
