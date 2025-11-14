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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe430a21-4e69-3f64-a8c8-cda67f76e659 | 3.1586 | -60.27624 | 2025-11-14 05:31:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 649a2632-f098-32c8-b782-30b7980cdeeb | 1.52985 | -55.6558 | 2025-11-14 05:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c876b67-76a6-3691-9dfe-46f0df48edbe | 1.52798 | -55.65395 | 2025-11-14 05:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6789a97d-6243-3510-aa5d-77b5ddb61463 | 3.15582 | -60.28028 | 2025-11-14 05:31:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 27052a92-d9d3-3f67-8a5e-ba010e06b1c3 | 3.10034 | -60.76832 | 2025-11-14 05:31:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 9ad924a4-464a-3e44-b333-025ce0930d77 | 3.1031 | -60.76435 | 2025-11-14 05:31:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 7c83d8dd-67e6-3ac7-ae11-09fe327b6e4c | 3.09979 | -60.76487 | 2025-11-14 05:31:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 31e42911-ccb0-3083-b74c-848a78c04100 | 4.25948 | -59.85065 | 2025-11-14 05:31:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75f2963f-0302-349b-b9d4-208bdb504ada | 1.31289 | -50.68144 | 2025-11-14 05:31:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59ed0e49-692e-34f0-9537-5f3f7cc7ef26 | 3.16639 | -60.28224 | 2025-11-14 05:31:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6baae823-1b44-351f-9a7a-6ce451c69a68 | 3.27244 | -61.19632 | 2025-11-14 05:31:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 503b5906-0591-3696-a935-b8925c89a5ce | 3.29399 | -60.11788 | 2025-11-14 05:31:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7567e615-ec00-3f6e-ab7f-195c8d9704d1 | 3.09602 | -60.76542 | 2025-11-14 05:31:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da9c25c9-9a61-3624-b3b0-bc74759a21fe | 2.63519 | -61.62316 | 2025-11-14 05:31:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f94fb83-a59e-3401-b0a9-e74932b39251 | 3.15046 | -61.02187 | 2025-11-14 05:31:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 688af5c1-72b5-32e8-aea0-30d1d02f10f3 | 3.16361 | -60.28627 | 2025-11-14 05:31:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f2d6331-91fa-3687-b845-2dd21a773486 | 3.29344 | -60.11435 | 2025-11-14 05:31:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf8370a6-80db-30f7-a326-9e7c23ffe18d | 4.25277 | -59.8516 | 2025-11-14 05:31:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a39c746e-a417-3341-b700-7156cccff663 | 3.09657 | -60.76888 | 2025-11-14 05:31:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| faabfcef-a100-30b1-b541-c7127d283e63 | 3.27391 | -60.12098 | 2025-11-14 05:31:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0e36c8c-b2c5-31cd-b6a9-5e388a25b59d | 4.25221 | -59.84801 | 2025-11-14 05:31:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc38ebf9-57d8-3e8e-91fb-136e27c5afc7 | 3.16249 | -60.27924 | 2025-11-14 05:31:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d974329-ddd1-3833-8899-94a89f4b0011 | 3.27447 | -60.12453 | 2025-11-14 05:31:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e46575f2-7745-3ce7-90fd-d3deb05d1bef | 3.13905 | -60.71267 | 2025-11-14 05:31:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 87a8c7e7-89fb-38c2-a25d-1d2d173604ec | 3.15304 | -60.28432 | 2025-11-14 05:31:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2075357b-dbce-305d-8c6a-8c8e8f079764 | 3.10255 | -60.7609 | 2025-11-14 05:31:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 30f0713c-2125-3bab-aec4-52f263bf8d18 | 3.10365 | -60.76781 | 2025-11-14 05:31:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 7d2fc101-df41-3a03-bf57-d4aa5d862646 | 1.31364 | -50.68607 | 2025-11-14 05:31:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a40155ed-e102-3456-9b7f-59dc75e5742c | 3.13573 | -60.71318 | 2025-11-14 05:31:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 540b5792-c9a2-3ba8-864c-c34968325831 | 2.75074 | -60.36577 | 2025-11-14 05:31:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 12.5 |
| f6234e56-5a3e-3602-8b51-660ce80a1640 | -1.41461 | -55.43956 | 2025-11-14 05:33:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f81f4601-8360-311f-94a5-526b15bfa1f2 | -1.34119 | -54.60924 | 2025-11-14 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3fda0656-9d36-38e0-b7ad-a56f68da92a3 | -1.34608 | -54.60995 | 2025-11-14 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9ce41ebd-fa37-3e7c-9af9-fb8b01a392bc | -1.83672 | -53.80276 | 2025-11-14 05:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 09c65ba6-f3ba-3ce2-9f68-a63aa2c89afa | -2.27991 | -53.64301 | 2025-11-14 05:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 888550c2-24da-3019-869b-a8c36f2defbc | -3.91304 | -54.68831 | 2025-11-14 05:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11289653-5259-31cd-a3e7-e3679544387c | -5.00749 | -50.91241 | 2025-11-14 05:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 185b59fc-43b6-31c4-8aad-3e5440ab42e7 | -1.8372 | -53.7996 | 2025-11-14 05:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ae2fdb44-b5e6-3ef2-96fd-0c56a33602fd | -1.34695 | -54.60413 | 2025-11-14 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9d38c3c2-7d04-3d08-96c9-08e7564f0a84 | -2.79754 | -52.96867 | 2025-11-14 05:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 105b2918-3f3b-3e2d-a4b6-d5864b8fb2c5 | -3.53083 | -52.7987 | 2025-11-14 05:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb5953db-d4ea-3f53-9f16-1a93cb6450a8 | -1.11065 | -52.59568 | 2025-11-14 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79b8f212-f85f-3618-86a9-b278d1ac9ad3 | -1.34204 | -54.60352 | 2025-11-14 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 61204207-8b08-363e-844d-7c93a696f88a | -3.8232 | -52.33541 | 2025-11-14 05:33:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5209d90-6272-3b30-be37-07f0d5dd5e31 | -2.94502 | -49.35909 | 2025-11-14 05:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c2be7fd8-510e-3dab-9216-a8929e7b57ee | -1.42636 | -55.30308 | 2025-11-14 05:33:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4eaa0f45-81d1-37ed-89f0-0dde6828ac29 | -1.37386 | -52.52958 | 2025-11-14 05:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4569e4ab-3da1-3eb0-a11e-25ba8a64b4aa | -2.4658 | -55.8164 | 2025-11-14 05:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5eb6eadf-b768-3ccc-af56-a754c10520fb | -1.83768 | -53.79644 | 2025-11-14 05:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38d8d043-11ee-3b95-b974-92661d6647a8 | -4.23284 | -49.67641 | 2025-11-14 05:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 107466ce-9e82-3fde-a0c6-fe5c7f7a7e78 | -1.83863 | -53.79012 | 2025-11-14 05:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2453026-da49-3842-8f61-eadff35fcd05 | -2.79703 | -52.97217 | 2025-11-14 05:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4026cf33-6199-3a9e-91dc-0b742bb6b289 | -3.82383 | -52.33115 | 2025-11-14 05:33:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 996bf6d9-c19a-37fa-b56e-dd03ddebeab2 | -4.23219 | -49.67326 | 2025-11-14 05:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1a8b2a9c-983b-3826-93d0-a5b5d223b451 | -2.94405 | -49.3657 | 2025-11-14 05:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2fff2ce2-496a-3e5e-b580-b905e47dd424 | -1.4256 | -55.308 | 2025-11-14 05:33:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 199b1467-8d68-3480-a61b-da6d673fee62 | -1.34338 | -54.60783 | 2025-11-14 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 940ff215-d162-358d-b2d9-6c16551c9ca9 | -1.83816 | -53.79328 | 2025-11-14 05:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5afa2944-9f85-3d20-821f-16e4a3c59134 | -3.61179 | -54.71299 | 2025-11-14 05:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a7cce02-00de-31e0-a5db-2c4a5770683e | -1.83343 | -53.7893 | 2025-11-14 05:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a62b266d-60e4-3bac-a8a3-d17e48fc68fd | -4.23126 | -49.67992 | 2025-11-14 05:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 20c0c13c-08d1-39c6-a250-1d150336090a | -1.83248 | -53.79562 | 2025-11-14 05:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3fb6393e-ffbf-3bbd-94a6-a65818e20abf | -3.8221 | -52.33142 | 2025-11-14 05:33:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 254882f3-d56c-383d-97dd-e54358548bdd | -1.43026 | -55.30869 | 2025-11-14 05:33:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4de5d319-4e25-3f04-a284-a4bbe3d2b480 | -2.33432 | -55.69152 | 2025-11-14 05:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3544ae68-ec59-3d34-9515-7f10230201d6 | -3.60677 | -54.71214 | 2025-11-14 05:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 407e981e-2e67-3694-9b79-416152d75777 | -1.34828 | -54.60847 | 2025-11-14 05:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b286c949-803f-3c61-bfe5-4aaee5f92a9b | -1.83577 | -53.80906 | 2025-11-14 05:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73bdc2d0-4864-37b7-84a5-107f1707963c | -3.9123 | -54.68782 | 2025-11-14 05:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f130f6bf-6f2f-3d21-85e5-c7903bd0f31c | -5.0141 | -50.91302 | 2025-11-14 05:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0852365-0950-32ed-9542-da54a87999ab | -1.832 | -53.79878 | 2025-11-14 05:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 27ca6dd3-bec8-379e-bc75-0952865d92a4 | -1.83625 | -53.80591 | 2025-11-14 05:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5dac1f9f-4615-3576-b487-8e95c347695f | -3.52891 | -52.79714 | 2025-11-14 05:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14eca1b8-fe94-3ed4-8a4f-d27f4e2b8ad7 | -2.28039 | -53.63977 | 2025-11-14 05:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ab84b3f-283b-35ff-8842-812cbebbe538 | -4.34398 | -68.43823 | 2025-11-14 05:35:00 | NOAA-21 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 0.0 |
| de402e9a-2211-3eac-8b52-24c11e6d8788 | -9.64583 | -63.76401 | 2025-11-14 05:35:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c540114-b50c-3d33-8db1-4f0f9fd5dc97 | -8.12824 | -55.30255 | 2025-11-14 05:35:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40d79b7a-24bb-3f14-8e14-e20afbd8695f | -7.79377 | -54.97053 | 2025-11-14 05:35:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e496725-04f7-3fe4-b8cd-f45eaf24b729 | -8.10961 | -55.09077 | 2025-11-14 05:35:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b618a0b5-6211-3a78-8409-f7a077f8bac2 | -8.1231 | -55.3017 | 2025-11-14 05:35:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 87b8a85c-3b3c-3cd2-aacf-69b8abf882a9 | 3.0911 | -60.7653 | 2025-11-14 05:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 309066fe-d260-3993-a433-2be78aeb47c2 | 3.1094 | -60.765 | 2025-11-14 05:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 441a6028-f7c3-38f0-a366-64775794f8c1 | -6.1633 | -48.03874 | 2025-11-14 05:42:00 | AQUA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 33.2 |
| f0c46cfa-91c1-30e4-97a5-5d829c1761e9 | -9.35551 | -46.59757 | 2025-11-14 05:42:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 32fbd082-318e-30c6-abe9-5cc4803e824e | -4.24555 | -42.73584 | 2025-11-14 05:42:00 | AQUA_M-M | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8c981e1f-b4f1-3ca2-aee5-f6710206a69a | -6.88101 | -42.85206 | 2025-11-14 05:42:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| bdf9aa50-3739-3f6c-8005-3c7ac8d0f956 | -8.90819 | -41.06708 | 2025-11-14 05:42:00 | AQUA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 716d85ba-07da-31c4-b569-7618c22c455f | -2.94394 | -49.36532 | 2025-11-14 05:42:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| b7207d8d-137d-32cd-ab5c-5c0dc00dfc59 | -6.92697 | -39.21506 | 2025-11-14 05:42:00 | AQUA_M-M | GRANJEIRO | CEARÁ | Brasil | 2304806 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 57b5bf4e-3b7e-3868-8841-65436e011d30 | -7.8442 | -44.28558 | 2025-11-14 05:42:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 24fab3c5-bfe1-386e-b401-a59a05b3a260 | -9.14454 | -45.17266 | 2025-11-14 05:42:00 | AQUA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| abdd56ee-7446-3111-8837-546b9783c517 | -4.70685 | -46.43963 | 2025-11-14 05:42:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 69e6299b-2c09-33a5-80fa-b0e8a83d3e68 | -7.45149 | -42.56791 | 2025-11-14 05:42:00 | AQUA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 3999d802-ecb5-3bda-981b-6cd8f415c114 | -2.8405 | -45.47129 | 2025-11-14 05:42:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 6e503f75-79bf-321d-bffd-f1a95e3d21fc | -9.96026 | -44.9439 | 2025-11-14 05:42:00 | AQUA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 9b18c4ec-0a12-3329-beb6-ff180d238431 | -3.33823 | -45.30985 | 2025-11-14 05:42:00 | AQUA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 13d94e06-3630-313b-a5b7-23a6aaac0350 | -5.52361 | -41.75036 | 2025-11-14 05:42:00 | AQUA_M-M | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 8d45c1c8-8683-3cca-a7dd-98a3d2e33872 | -6.72223 | -42.0251 | 2025-11-14 05:42:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 282d82f8-ad3a-34b6-a697-075cb7321c85 | -7.84858 | -44.292 | 2025-11-14 05:42:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f8f38626-d59a-3a58-85a6-cee16d42e40b | -10.10502 | -40.89786 | 2025-11-14 05:42:00 | AQUA_M-M | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |


[Clique aqui para ver as próximas entradas](README51.md)
