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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4884a4d6-8ada-3d7c-b3c1-3defb263f397 | -6.62888 | -53.35491 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1ca2d02-5fae-304d-a2c6-c183517fa2fc | -6.27266 | -53.44043 | 2025-09-08 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f4ab5dc-10ce-3e0c-a38a-9dae4ee954e1 | -6.26845 | -53.4239 | 2025-09-08 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47cf8728-baee-3663-b38c-ca52f611fd21 | -6.19747 | -53.266 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe9ec169-b0f2-3b2c-8232-e659240da817 | -5.2483 | -57.12526 | 2025-09-08 05:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2b15eb5f-db7c-3b8e-ad42-c5ed80a3a693 | -6.62317 | -53.3488 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ea00376-1182-3f09-8758-16a7aaa87ded | -5.76717 | -56.52298 | 2025-09-08 05:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31c36d51-bfa0-37de-9f4e-bd3cd305487c | -6.20395 | -53.27385 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7cc42ed4-03fe-35f2-a318-8164bed9b57f | -6.19898 | -53.26192 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89fd3f1f-4fa0-3793-b133-6287022301af | -6.62324 | -53.35547 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8aa6f9b-343a-34ea-b5fb-7e9b6726c095 | -6.28415 | -53.4207 | 2025-09-08 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 596dedd9-ba3b-3d7c-ba1d-2f72e170807e | -6.62966 | -53.35641 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 47160c46-8ae9-32d1-9132-997b28846c33 | -5.76763 | -56.51985 | 2025-09-08 05:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d439ab37-7f53-35fc-bd9c-e9a4b7bd3134 | -6.62826 | -53.36707 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7d530263-e35c-3ad8-9ef9-2f56e9b42e64 | -6.63538 | -53.36266 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 011cd57b-7c25-311a-93bb-4bedb15ae48c | -6.27776 | -53.41987 | 2025-09-08 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aaf4304d-ab13-398c-8965-a6005187e704 | -6.62814 | -53.36023 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f3630c81-8304-3402-b20b-a8df195eca48 | -6.28346 | -53.42588 | 2025-09-08 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bdf29dfa-1331-32ba-b869-8b0d9f665ff6 | -6.62741 | -53.36552 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 79e3e0bd-8c76-34b7-b98f-369d6765c7c8 | -6.63398 | -53.37328 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dd085035-2db7-3e50-984f-e97cd4968d5c | -6.62116 | -53.37132 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8acfd8ec-4fd2-3711-bf65-de62eb615cf4 | -6.62101 | -53.36445 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f577e7a-c9dd-3931-9c49-d16cf2cf74db | -6.34606 | -55.55931 | 2025-09-08 05:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 09bcffcd-4b90-311e-9ad7-5561328bd479 | -6.82082 | -51.88379 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f8e9f912-3af7-35bd-8831-7dd3d0a96631 | -6.63035 | -53.35114 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d05da0b-0e09-333f-a0cb-6a1d360fb54c | -5.25323 | -57.12594 | 2025-09-08 05:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4f3d2807-7f36-3925-94f6-52f6676c04fd | -6.27482 | -53.42478 | 2025-09-08 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc8c9a39-4f0e-3957-88e4-71fdd08f92fc | -5.25003 | -57.12539 | 2025-09-08 05:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c70a2237-390e-313a-9828-27f06b132cec | -6.63468 | -53.368 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1d829928-1a5e-3164-a3fe-d14c41d7b377 | -6.28048 | -53.43082 | 2025-09-08 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc413d33-e46f-328f-bace-99355e5b0ef6 | -6.63951 | -53.37265 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 475e4a8d-a1b6-3137-9b00-e37f65e40dd5 | -6.62688 | -53.37752 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6354e3cf-1ac2-3f71-8472-6b6b070128cf | -6.62186 | -53.36599 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bad107f0-2277-36d5-ac0e-026420925a34 | -6.63383 | -53.36645 | 2025-09-08 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2c4eb93a-94fe-3fa6-8d5f-b17a9a9b81f4 | -9.81522 | -53.32198 | 2025-09-08 05:42:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa6f82a4-3db7-37f4-8ca5-b90822aa4e95 | -11.22404 | -55.01417 | 2025-09-08 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd3d60b5-a279-31c3-a074-93b8ddfd4ae6 | -6.8282 | -52.80317 | 2025-09-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0bd32f5e-86fc-3a97-8ae5-bd54d58c1061 | -7.11312 | -63.07067 | 2025-09-08 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 862ed64f-1e08-3d71-895b-bd28ddbc10bb | -6.9641 | -62.93056 | 2025-09-08 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3ed84e6-3a0d-309b-9f9b-62192495ff5f | -6.9664 | -62.9389 | 2025-09-08 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb5285fb-8b84-3208-8b5c-64f2402d583f | -9.66596 | -67.74962 | 2025-09-08 05:42:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79906190-ff96-3e04-81eb-02ffcb805a19 | -9.85957 | -67.59686 | 2025-09-08 05:42:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ee6a87f-5290-3a97-9ca1-449debaf4fe2 | -7.39807 | -61.63793 | 2025-09-08 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 96e3049f-4cbc-33c9-9f9e-ca356010d5a2 | -9.85175 | -53.3014 | 2025-09-08 05:42:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71ce08b1-628f-3346-9c42-d31f73b2f418 | -12.81764 | -52.88484 | 2025-09-08 05:42:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bafad84b-84ff-3761-84ca-9cfcdbf3c780 | -9.44002 | -66.57429 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78920fea-6bdc-3b6a-95f5-ff81064b3eb7 | -9.07714 | -65.40738 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c711daf-d9e7-3ac4-97c6-d6f2a60c5b4d | -9.8345 | -53.33152 | 2025-09-08 05:42:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e4ea1159-af1f-3937-a36d-35ed48f1f008 | -10.57633 | -61.25822 | 2025-09-08 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb652a95-25b1-3673-a7e7-ae7f958dffd5 | -6.83114 | -52.80141 | 2025-09-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 817f1999-da29-3010-a0e3-419f77021ca7 | -6.95358 | -62.92896 | 2025-09-08 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f1e4072-76ca-3da5-bbb5-c56eeaf38669 | -9.53893 | -59.06743 | 2025-09-08 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| edd0b50e-20e4-31c5-b6c3-c35ff01effaf | -9.12975 | -65.95912 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10b1a4f2-6e04-3652-85c4-34eb6150e572 | -8.3604 | -70.06551 | 2025-09-08 05:42:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8badefed-b819-3a3e-a143-0975d38a0d33 | -11.21787 | -55.01358 | 2025-09-08 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0843def-9be8-3e61-a8e8-9fc3248749de | -7.12708 | -63.0728 | 2025-09-08 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e152d573-67c7-3e3e-b96f-eea5e47f45f7 | -9.12699 | -65.95512 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b8d6a17-a530-3335-bae3-0290c4d53298 | -9.93151 | -60.52059 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9050f3d3-91eb-3ffa-aebb-172398a5db80 | -10.89129 | -55.71608 | 2025-09-08 05:42:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6243767f-1ff0-347a-bb05-9221c022a44a | -10.08454 | -59.17851 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca88ff4d-746f-39ee-883c-925eac7193e4 | -9.38537 | -62.34097 | 2025-09-08 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 111b2faa-5fa1-39ac-b2e2-46da84136c35 | -9.20354 | -67.55415 | 2025-09-08 05:42:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5352fc6a-28b0-3a5a-a0b4-78f86dcb220a | -9.30405 | -65.82304 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 057041cf-898a-3079-a79e-05bb101c99fd | -9.62398 | -64.20882 | 2025-09-08 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d5711daa-135d-33e0-b3d2-9e54c9afa1bd | -9.46207 | -56.05186 | 2025-09-08 05:42:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84b354cf-26cf-397c-b8bf-2d85c154d72c | -9.20294 | -67.55782 | 2025-09-08 05:42:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e60868c1-6042-3095-ac4f-daaf32efb9d0 | -9.1519 | -60.85061 | 2025-09-08 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61e7f8c0-0306-3c1b-aee8-0465db9f0cc9 | -10.08388 | -59.18328 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae95f0a0-b5dc-3a8d-949d-db934bf1e9eb | -10.08914 | -59.1791 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6067e89-267f-377a-9627-7344d60b3b46 | -12.19583 | -53.91256 | 2025-09-08 05:42:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af541bfb-1d28-3827-bcf0-1d8b03f1014f | -12.82032 | -52.89268 | 2025-09-08 05:42:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5c64d000-4af9-3215-ae0b-c409dc9d91da | -7.39431 | -61.63736 | 2025-09-08 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a26bc9c8-16f2-36a5-be00-b76c9b072cbe | -10.50718 | -61.30275 | 2025-09-08 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86fd710c-d066-37bb-8cd0-ccc586a5c707 | -9.19955 | -67.55727 | 2025-09-08 05:42:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4db69475-0591-3e5f-bc12-b068fa90527e | -11.21844 | -55.00877 | 2025-09-08 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1e493a6-9b58-3e93-8a36-a3b47dc8294a | -9.47659 | -60.49802 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2080dc1-b018-3d05-b56e-882372cec98c | -11.18156 | -55.05696 | 2025-09-08 05:42:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9772d1fe-c5c4-3f8b-a9b2-362d19a09c09 | -9.84579 | -56.04391 | 2025-09-08 05:42:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51dff84c-2901-35f6-8043-b8ce1b750349 | -10.50654 | -57.80117 | 2025-09-08 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88f58da8-aec4-36f6-90ee-bab8b37dc6ba | -9.24724 | -57.06528 | 2025-09-08 05:42:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d94b788-f20b-3e7b-8972-d02125f0ad06 | -9.8875 | -56.14567 | 2025-09-08 05:42:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f1e4ff0-6263-3319-82da-a34ffa192f99 | -10.25256 | -59.38463 | 2025-09-08 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 828ce305-e691-33ac-9642-783ace58711d | -9.08998 | -64.01535 | 2025-09-08 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6511140c-75af-381d-8009-5b98fbfe5716 | -9.13692 | -65.9567 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbfc182e-7789-3598-b733-d0bbe4053f1e | -9.43396 | -62.37081 | 2025-09-08 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1371920-4083-3910-ac7c-eb84f32913f4 | -10.14786 | -61.13953 | 2025-09-08 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4376c8e9-b807-3aa2-8c64-0162c7064155 | -7.3956 | -61.6258 | 2025-09-08 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a8e293b-7795-3a19-8b68-b4fd6beaffdd | -9.30128 | -66.61271 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 54065e57-19db-3ca7-8f61-3c3c817d7af8 | -7.40316 | -61.62938 | 2025-09-08 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 38c45f57-000b-3fc2-b606-2a92d812670d | -7.39352 | -61.63944 | 2025-09-08 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0765c81c-d703-3dc0-85cf-25f8a1b98b7d | -10.28954 | -67.27417 | 2025-09-08 05:42:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02779226-6065-390f-8eed-0dfe5649f6da | -6.84212 | -52.85181 | 2025-09-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 507f5d19-6b8b-35fb-a58b-0ca87b7004e3 | -9.20804 | -65.91451 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84f63b77-8d18-30eb-8faa-c8687fc40e3a | -7.90274 | -61.78153 | 2025-09-08 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2aa209ac-2466-3399-9d6f-ebdd0fdf0cda | -10.33964 | -68.07205 | 2025-09-08 05:42:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2c75924-8df0-37f2-86a0-03236a076f74 | -7.39873 | -61.63337 | 2025-09-08 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 4e779e24-28ba-3cf0-8145-26d5b43d2674 | -9.36714 | -65.93961 | 2025-09-08 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 08095ba7-9ede-3618-9daa-bf71c17d8e61 | -9.17075 | -59.3646 | 2025-09-08 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5df040cf-bca8-3713-8892-212f31f1a035 | -9.81814 | -53.32843 | 2025-09-08 05:42:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee11843c-202f-312d-a69d-59e1d6688640 | -8.88056 | -64.21864 | 2025-09-08 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README90.md)
