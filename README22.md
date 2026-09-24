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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8bee1ef1-7813-38c2-88b5-c2c67ed01899 | -3.6947 | -60.5645 | 2026-09-24 01:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 45c5ce32-9c18-37e4-91af-174249c4e381 | -10.111 | -46.0209 | 2026-09-24 01:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| cfe3f5f2-4534-3b9e-9919-d2aea96c105e | -6.4302 | -59.9724 | 2026-09-24 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 728907f5-db20-386a-a7c6-d5c0581206b1 | -8.6542 | -61.9076 | 2026-09-24 01:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 6300127a-74af-3976-bf12-3ef833c266cd | -10.2827 | -49.9606 | 2026-09-24 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 3f7d2c8f-1d0f-3d6c-aae3-fccb0e3b08b7 | -6.789 | -48.6779 | 2026-09-24 01:10:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 57.4 |
| bda332fe-c084-37ff-a28f-17e30d2cc7f1 | -6.6145 | -59.9464 | 2026-09-24 01:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 7aaf986c-dac5-38ba-8f39-4d833064420b | -3.6763 | -60.5839 | 2026-09-24 01:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 50fd02dc-2488-37da-a47a-c87a45d0f754 | -9.8488 | -48.5146 | 2026-09-24 01:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 74a2bf92-b5d6-31e6-a7b4-8aa80f064359 | -6.7211 | -44.1618 | 2026-09-24 01:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| e8b45a50-2fac-3d3d-b477-0e6f305710b1 | -10.0921 | -46.0232 | 2026-09-24 01:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 322.3 |
| 30c5f340-0793-37bf-9958-78f708d1c93c | -10.2637 | -49.9626 | 2026-09-24 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 4054fc21-16f3-3584-8a95-6b4c1862a3ab | -6.3501 | -57.7717 | 2026-09-24 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 57068732-9fee-358f-b108-adaba63c1442 | -3.6947 | -60.5455 | 2026-09-24 01:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 9d59f4d5-ec3d-3dc4-97aa-6ae6b3f0557e | -15.5686 | -42.3547 | 2026-09-24 01:10:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 4e4e77ec-f078-367a-9938-0b6e59083763 | -6.4303 | -59.9532 | 2026-09-24 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| e21bc9cf-035c-36af-beb1-50ead4d004dc | -4.2951 | -49.1234 | 2026-09-24 01:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| a81920fe-8256-3a89-8d58-f72fba38a6c4 | -10.1107 | -46.0435 | 2026-09-24 01:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 8af99f0d-3685-371b-9812-28ccf2e55c1e | -9.275 | -46.2527 | 2026-09-24 01:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| faa73249-6330-35ce-af09-1e7e30a1815d | -4.3137 | -49.1226 | 2026-09-24 01:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 278181dd-b086-3d09-9c92-b0c72a4ff83e | -10.0924 | -46.0005 | 2026-09-24 01:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 26520e54-2ef4-353c-b3f5-82c5db92de58 | -9.8491 | -48.4927 | 2026-09-24 01:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 508dcacd-4f53-3752-8cdb-18d7b21775f1 | -4.1181 | -51.0695 | 2026-09-24 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 93f6df92-e955-3a3f-a5c2-1be3b0999662 | -6.4486 | -59.9717 | 2026-09-24 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| b0030247-8a54-3020-9910-6f5f5608bb57 | -6.4487 | -59.9526 | 2026-09-24 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| fe2f09f8-c140-3294-aff7-43a3eb3751d1 | -11.9396 | -50.7415 | 2026-09-24 01:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 97.4 |
| b9ae1912-8d3d-3d48-afa7-dd6b32ba0840 | -15.5679 | -42.3794 | 2026-09-24 01:10:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 723d66d4-3add-3a25-8b19-1506e58af6b5 | -11.9583 | -50.7607 | 2026-09-24 01:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 162.3 |
| 7bea65db-5dd7-3005-a08b-1e887adbdc74 | -9.4953 | -64.0316 | 2026-09-24 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 249da69e-2dfe-3b2c-9229-64dc1f8ebaa4 | -11.9392 | -50.7629 | 2026-09-24 01:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 139.2 |
| b62ed849-f619-353a-9bcc-e443c29d119f | -3.4577 | -50.089 | 2026-09-24 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 92dcb432-80c2-34f2-a105-0d58bcc1d91c | -5.7754 | -45.1053 | 2026-09-24 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| c3b07c5f-4867-3aa5-a5b8-a14ec6bbc53c | -3.1637 | -54.6054 | 2026-09-24 01:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 5173e935-bc4c-32c9-8be2-0ea99e09b348 | -3.4578 | -50.0679 | 2026-09-24 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| da0b1a6e-981b-39ef-a3bd-ad281f8cdd06 | -10.0917 | -46.0458 | 2026-09-24 01:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 257.8 |
| 2ad425ac-001d-37c3-a5c2-c7d6213c5b61 | -3.4387 | -60.5695 | 2026-09-24 01:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 834eeb24-35e7-3b2b-8164-5ac710e37747 | -6.6775 | -58.5748 | 2026-09-24 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| fce5d41a-1968-3643-8ff3-ba5350caa1db | -12.4216 | -46.9551 | 2026-09-24 01:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 147.0 |
| ff917d22-e388-3cf8-ade1-beab86017f8f | -6.6148 | -59.908 | 2026-09-24 01:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 8d0315ad-0711-368e-8f34-5444f63e0aa1 | -6.05 | -47.29 | 2026-09-24 01:15:00 | MSG-03 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f554637d-2d32-35f6-9dbf-808f22c26459 | -5.7754 | -45.1053 | 2026-09-24 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| b785f84a-6ec7-332f-96fd-22dbca7e85cf | -4.2951 | -49.1234 | 2026-09-24 01:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 5b8794be-491d-3695-916e-928137012ca2 | -7.7679 | -72.9879 | 2026-09-24 01:20:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 8903126e-dba0-3413-ac83-b8d5005c9af1 | -6.789 | -48.6779 | 2026-09-24 01:20:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 51.2 |
| d85d898c-90a5-38a0-8fd1-ef6e718dccfc | -10.9115 | -53.9429 | 2026-09-24 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| cd3eacbc-5694-3696-885c-9020f4759b06 | -15.5488 | -42.3591 | 2026-09-24 01:20:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.2 |
| 574b960e-c183-34fe-9c72-f6bd85df90cb | -4.118 | -51.0903 | 2026-09-24 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 0b4d116c-deb2-3745-8e48-57f2ac9b9e54 | -15.5686 | -42.3547 | 2026-09-24 01:20:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 350.4 |
| 29e38eac-38f5-335a-9e1b-6e90e07008dc | -8.2616 | -54.7776 | 2026-09-24 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 79161b33-259b-3716-b73b-95c8572f2d93 | -6.6146 | -59.9272 | 2026-09-24 01:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 8a744134-6042-3f66-bdea-3f1791cebf2b | -4.1181 | -51.0695 | 2026-09-24 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| e4f8bbf8-cb97-3337-954e-b728206f7405 | -6.4302 | -59.9724 | 2026-09-24 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 546507ee-0862-3e8f-8c75-4f2a2155b799 | -12.4216 | -46.9551 | 2026-09-24 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 120.8 |
| f69c4e49-c3ea-3db3-b070-fa83ab1fbd2b | -10.2637 | -49.9626 | 2026-09-24 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 8a1ea29e-ed62-3d58-9558-7be39838a28b | -6.4487 | -59.9526 | 2026-09-24 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 7ec7f2e3-1232-3424-9a89-17dbc9db960f | -10.2827 | -49.9606 | 2026-09-24 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 9e524d31-5894-31ff-8fad-3ed1d8c41b95 | -6.4303 | -59.9532 | 2026-09-24 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 74189974-4897-3a60-b659-2dcefd2bb0ce | -3.4578 | -50.0679 | 2026-09-24 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 337b2b50-55c8-3ad3-b2a6-e8a44cc601d9 | -9.275 | -46.2527 | 2026-09-24 01:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 63a644af-72fb-3839-bbeb-7bfe409af67a | -15.5884 | -42.3504 | 2026-09-24 01:20:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 4b0e4888-a149-3bf2-a8f9-c0d93141860b | -15.5692 | -42.33 | 2026-09-24 01:20:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 91.3 |
| da758c75-08c2-3200-a8da-6447d694519b | -3.4577 | -50.089 | 2026-09-24 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| c2063173-b58f-38e8-91c4-0bc0f0dda532 | -3.4387 | -60.5695 | 2026-09-24 01:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| a0e5c095-b5b6-3bad-b6d9-fd8248d61688 | -15.5679 | -42.3794 | 2026-09-24 01:20:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 196.9 |
| b000dd90-7547-3ee6-92e6-6de6750098e3 | -6.0928 | -57.6262 | 2026-09-24 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| e5d6bd30-2b37-3cdd-8089-fe4632284f7d | -9.8491 | -48.4927 | 2026-09-24 01:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 24aeb998-778a-3071-a5b9-dce1afd3372a | -3.1637 | -54.6054 | 2026-09-24 01:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| db72a4a5-685d-3548-951c-739652354680 | -6.4486 | -59.9717 | 2026-09-24 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 8c288b35-52b6-3ea6-af4c-ce74efc7475a | -9.0158 | -60.5138 | 2026-09-24 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 82b8c205-414b-3461-80f7-ccb5dce661a1 | -11.9586 | -50.7393 | 2026-09-24 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 53f6a2d4-c216-3a6c-bc3e-b23f694297ef | -7.7679 | -72.9879 | 2026-09-24 01:30:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 286fa8eb-167d-3597-a74c-e11648650e7b | -10.2637 | -49.9626 | 2026-09-24 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 487bf931-3d33-31f2-8ade-47941335920c | -11.9583 | -50.7607 | 2026-09-24 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 6d4fd6fc-604e-3232-8c53-4a2b9fd5a6d8 | -4.9877 | -45.5412 | 2026-09-24 01:30:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 825f1760-c4e2-3fb6-9c7f-af8cb77ee61e | -6.7211 | -44.1618 | 2026-09-24 01:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 8e4217cc-513f-3df3-8505-4fcd4458cefa | -9.6949 | -64.9269 | 2026-09-24 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 0e357aac-d52d-3358-a2a0-6caea51017e6 | -9.695 | -64.9081 | 2026-09-24 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 77b8a9d7-f0b5-322a-85a7-089fd05f1615 | -4.1181 | -51.0695 | 2026-09-24 01:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 84c6faf2-1716-336e-b050-74c9c7288a92 | -15.5488 | -42.3591 | 2026-09-24 01:30:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 88.4 |
| 43d3358a-c30c-3a7e-8755-c2b8558ff9c5 | -4.9876 | -45.5637 | 2026-09-24 01:30:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 38149ad2-5221-30f3-9fba-29658721179f | -12.4216 | -46.9551 | 2026-09-24 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| bf6669db-baa4-32f4-ab7d-d830b939bf7d | -4.118 | -51.0903 | 2026-09-24 01:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 880fa60d-e5ce-3058-92a7-bc7a0c14ec78 | -12.0414 | -50.3011 | 2026-09-24 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 1f6efc76-d6a0-37e8-a114-570243104083 | -6.6146 | -59.9272 | 2026-09-24 01:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| c86d8336-4c68-34e7-925b-45472f83653d | -5.7754 | -45.1053 | 2026-09-24 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 5cf9b7f5-fa92-3d40-8fe1-630d9b536431 | -3.4577 | -50.089 | 2026-09-24 01:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 49fd17a2-4055-3aee-987e-4c498508924b | -11.9392 | -50.7629 | 2026-09-24 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 99.9 |
| bf27eece-3e74-32be-b915-c3ba766d9d22 | -8.2616 | -54.7776 | 2026-09-24 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 936e5bd1-b323-3d2e-a6ed-121804f300f6 | -15.5884 | -42.3504 | 2026-09-24 01:30:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 98074e11-471f-3f0f-b3fc-3012c90a7c75 | -11.9396 | -50.7415 | 2026-09-24 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 14da4150-16ca-3668-8f57-9c635f87294d | -3.4392 | -50.0896 | 2026-09-24 01:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 53abd81f-e085-3a4f-8109-7ea7948495c3 | -9.8491 | -48.4927 | 2026-09-24 01:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 4a60573e-f681-3b7a-acc1-d55804e3a970 | -10.2827 | -49.9606 | 2026-09-24 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 590d1ae4-387f-313c-9fba-fb5016dc1f76 | -6.3501 | -57.7717 | 2026-09-24 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| efb3de4e-b55e-3576-84d3-76e06dea9fb5 | -6.6331 | -59.9265 | 2026-09-24 01:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 414d8433-359a-3c5f-9db1-7f7a1bf25638 | -4.4304 | -55.0668 | 2026-09-24 01:30:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 8d245fa5-06f6-347a-96be-dc32af58d8ca | -12.0418 | -50.2796 | 2026-09-24 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| d7bd8d09-b341-372a-8934-1f6778620d8d | -3.1637 | -54.6054 | 2026-09-24 01:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 13677279-bbbd-3509-b56d-9605a36bde6c | -15.5686 | -42.3547 | 2026-09-24 01:30:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 213.1 |
| 26074f76-b6f4-303e-a682-52910a12a88f | -10.1284 | -50.2116 | 2026-09-24 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |


[Clique aqui para ver as próximas entradas](README23.md)
