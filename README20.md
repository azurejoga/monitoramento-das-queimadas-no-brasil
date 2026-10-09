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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 019eaa25-f63e-3f0e-a08c-4c0356ea61ed | -13.2015 | -54.3757 | 2026-10-09 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| fa16330e-8651-3ee3-9521-7049fd200c2c | -1.5489 | -54.5556 | 2026-10-09 00:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| ee3f4f13-9262-3990-84f7-8efa9771eb65 | -13.1636 | -54.3591 | 2026-10-09 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 82db2a5e-b3c0-37df-9b65-dce66caf9642 | -12.0251 | -43.4609 | 2026-10-09 00:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 6ca5fa80-f89d-359a-8db0-a1a92cdc366d | -1.1277 | -54.18 | 2026-10-09 00:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 9bb45425-93cc-35d5-a957-7b5998ef93b4 | -6.4719 | -62.8559 | 2026-10-09 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 4a097ecb-bdbb-34d0-9312-3049bf76871d | -9.297 | -47.4313 | 2026-10-09 00:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 171.1 |
| a7e4c098-ccfd-3aeb-87fc-e57681eb182c | -3.5677 | -54.6746 | 2026-10-09 00:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 1e927949-b9d3-3f61-815d-efd34f858108 | -5.7679 | -43.8467 | 2026-10-09 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 3ac5f474-ae84-3d51-8581-d23adc1e5dda | -4.6362 | -50.9646 | 2026-10-09 00:10:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 37b1012e-3451-3e98-944a-cc6c16d951c1 | -15.3419 | -42.7704 | 2026-10-09 00:10:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 106.1 |
| e2e38e17-05c8-3cca-82f0-54a0d7c07058 | -3.1109 | -53.945 | 2026-10-09 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 29e17c07-5e14-3cf5-a03b-b2386d5e5080 | -8.5369 | -66.9949 | 2026-10-09 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| f7ed5c47-97d3-3c2e-bf22-a77d746754d7 | -7.5688 | -64.5476 | 2026-10-09 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| f964b7c4-d4d0-3054-9787-1c532013433b | -8.7231 | -45.1583 | 2026-10-09 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| e4b59c17-b7b9-33f7-84c7-301ce0801e8c | -4.6282 | -49.2147 | 2026-10-09 00:10:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 5b158c26-f482-35c7-ad2a-ecc6fbe084df | -9.2973 | -47.4092 | 2026-10-09 00:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| e19b95ab-35dd-3f15-a9ae-0c69b8867af5 | -13.2018 | -54.3551 | 2026-10-09 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 112.7 |
| d4c03541-3ed0-3ee7-a517-36decb12aca1 | -8.7423 | -45.1334 | 2026-10-09 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 121.5 |
| d6146f31-4278-3abf-a5b6-0fea333b05a0 | -8.6301 | -66.7886 | 2026-10-09 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 0a835466-e6c0-33a8-814e-b3009b43e726 | -5.7116 | -53.5065 | 2026-10-09 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 1d74000e-0a2a-300c-bdd8-7ad4fdcdad18 | -12.0058 | -43.464 | 2026-10-09 00:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 724bb28c-1f5c-3e01-af27-6b14916fc249 | -1.1094 | -54.1802 | 2026-10-09 00:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 184.8 |
| 8f71b05e-08b9-3b5d-889d-13aa9c117003 | -12.2154 | -57.1287 | 2026-10-09 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| a0e8eb0b-f0e7-3a53-8d78-5e570c55994c | -3.9299 | -56.034 | 2026-10-09 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 5bbebaed-473c-330c-b067-e0e0b2faef8d | -3.11 | -54.1862 | 2026-10-09 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 40541623-3fdd-307b-bece-35fc2c2a9190 | -5.6932 | -53.487 | 2026-10-09 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| c1359676-dabd-39d1-ba55-c8ce5cd5bce3 | -6.0076 | -53.4919 | 2026-10-09 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 404521f8-b2b5-3886-b37a-a1cab19dbf5e | -7.5834 | -61.5516 | 2026-10-09 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 207e6462-abdb-3a6b-98a2-540e902db4b6 | -2.7428 | -54.1146 | 2026-10-09 00:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| a17215a8-f95b-3696-8274-003428081d25 | -13.2209 | -54.353 | 2026-10-09 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| d3220756-61ca-3dd7-8532-c13073a042e0 | -8.742 | -45.1563 | 2026-10-09 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 595938e8-04b0-330c-867e-31348857ede0 | -5.6934 | -53.4667 | 2026-10-09 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| e8cb42a0-29b5-3218-80dc-e88e8d357c4c | -12.2158 | -57.0887 | 2026-10-09 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| ed7aacae-5294-3b3f-8b2e-87030b6b0708 | -3.0007 | -53.9075 | 2026-10-09 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 66c3ae60-c96b-31fc-8470-e88436f81741 | -5.9833 | -40.961 | 2026-10-09 00:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 136.2 |
| a0d26774-926c-3d9e-b342-8a810408f1fe | -5.9587 | -55.3448 | 2026-10-09 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 4b801379-9bcc-331c-bd9c-b3a4b1b7685a | -6.7365 | -55.1474 | 2026-10-09 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 22d9ec53-d22e-3b89-b4b9-157f7312b18a | -11.6562 | -43.6846 | 2026-10-09 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 164.8 |
| b1ae6e9a-b968-33b7-be8b-07ac9bfe5fe0 | -1.1094 | -54.1601 | 2026-10-09 00:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 160.1 |
| f788595a-bbc6-3c47-8cb8-2deb09ff70e7 | -13.1639 | -54.3385 | 2026-10-09 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 3e3b6cc9-9bec-391f-b2f8-719516313318 | -3.2945 | -54.0006 | 2026-10-09 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| dfa142ee-1914-3e2d-82a0-cfda6087c470 | -4.2768 | -49.0816 | 2026-10-09 00:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 3b94204b-5979-3ed8-912a-bfc6bfb6e8bb | -4.6096 | -49.2156 | 2026-10-09 00:10:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 277eed35-0a07-3b6e-869e-6955b4393d71 | -3.1114 | -53.7839 | 2026-10-09 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| e9a0aaa0-5667-3c2a-8f3d-91112b51eaef | -3.5493 | -54.6752 | 2026-10-09 00:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| a4cd0572-d826-33e9-b0a7-a64a63987276 | -6.0021 | -40.9594 | 2026-10-09 00:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 521.2 |
| 131e2db4-0366-3e0d-83fd-c40f0383a203 | -8.537 | -66.9764 | 2026-10-09 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 677e3787-7e3e-340f-b62d-4634a4bffe19 | -12.2156 | -57.1087 | 2026-10-09 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 7542ee0c-8499-32af-9f74-cbd12e980d98 | -7.4442 | -63.5589 | 2026-10-09 00:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 390165fa-cde9-33c9-8288-ce66e4f0a1a7 | -3.1108 | -53.9652 | 2026-10-09 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 099508c7-3465-32ab-a921-1eaa64c96c08 | -13.4922 | -44.3713 | 2026-10-09 00:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 06d63f06-8969-38a9-ae10-440316c69f64 | -3.0002 | -54.0684 | 2026-10-09 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| d127d9c7-3316-3040-ae63-ddbd1e9c98cc | -2.9823 | -53.908 | 2026-10-09 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 0fcc97ed-d27f-328f-8576-4ee2e68e9e7a | -7.4095 | -44.7656 | 2026-10-09 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 827d2074-51d7-30bf-9128-93a52ff1ac50 | -3.2759 | -54.0614 | 2026-10-09 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 25c9173c-9780-3f1d-a35e-518b07547d16 | -3.9912 | -59.356 | 2026-10-09 00:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 7b9363b1-8a26-362a-ab45-d7e7d0e8c5a3 | -3.5493 | -54.6951 | 2026-10-09 00:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 150.1 |
| 4b3c6bba-8ee8-3937-a8cb-f4e465fde009 | -8.7234 | -45.1355 | 2026-10-09 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 89ebab2f-9d8c-3493-be73-93b46273065d | -3.1285 | -54.1657 | 2026-10-09 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 152.0 |
| 78b6e417-f705-33cd-b4d6-152f23e6aa46 | -8.2313 | -61.3922 | 2026-10-09 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 43214d18-1469-3311-a70c-95c71061b515 | -6.7195 | -48.1201 | 2026-10-09 00:10:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 138f986f-8bbf-3a28-bf28-4824779a4e0f | -12.2346 | -57.1071 | 2026-10-09 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 65b601a5-a874-34c0-bbad-e0ed0faf48ad | -3.1284 | -54.1857 | 2026-10-09 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| b9f7e609-b137-3d1c-89ff-95c797884157 | -3.0924 | -53.9656 | 2026-10-09 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 9095185e-beb2-3f47-9f02-c77c6d23bde5 | -1.1277 | -54.16 | 2026-10-09 00:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| da9bc809-2858-39dc-abf4-80014af46e1e | -3.7346 | -59.4577 | 2026-10-09 00:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 9bb346a7-5f48-370e-9698-e90ed72f6bf0 | -5.983 | -40.9854 | 2026-10-09 00:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 69.9 |
| 0782879a-ce27-3f31-9ac0-9ecb57de0332 | -15.4287 | -43.2373 | 2026-10-09 00:10:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 124.8 |
| c304bd1b-de7b-329a-a838-3420632c77bb | -3.2577 | -54.0217 | 2026-10-09 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 3b76c9c9-0468-384f-a0eb-bb50cfbaa87a | -11.8499 | -43.5835 | 2026-10-09 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 162.7 |
| 52cd4976-6692-37f7-bb32-88cbe35cc8b8 | -3.2057 | -58.8354 | 2026-10-09 00:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 59f3c427-ef36-3295-949d-3c743a5c7328 | -9.6867 | -58.0865 | 2026-10-09 00:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 1df99bc8-9995-3844-bf6f-8f01d37e7888 | -9.2781 | -47.4333 | 2026-10-09 00:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 5afa2494-d274-3950-af72-a28a078aa35b | -3.2576 | -54.0418 | 2026-10-09 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| b83460c3-8c41-3654-b0ae-76dd3f875418 | -6.4949 | -55.2995 | 2026-10-09 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 7cbfc93b-5e0d-37d2-8d65-d2d696940428 | -8.73 | -45.15 | 2026-10-09 00:15:00 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 06c248d4-6362-315c-aef3-407c709baf29 | -8.73 | -45.2 | 2026-10-09 00:15:00 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 062efded-a1c0-30a5-92dc-0e11a337a381 | -8.76 | -45.16 | 2026-10-09 00:15:00 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 55cf1e8d-77ae-306f-a4b6-2d0ab71d0913 | -5.99 | -40.97 | 2026-10-09 00:15:00 | MSG-03 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c4a45c20-7854-3b6a-ae8c-12336bf14b88 | -5.7302 | -53.4853 | 2026-10-09 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 07fbc079-db6e-368d-a192-2656ef321ac4 | -6.6733 | -63.0379 | 2026-10-09 00:20:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 3bc848d3-ea47-3d97-92f2-a72e8320a455 | -2.7612 | -54.1142 | 2026-10-09 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| b69cd12e-6c10-3de4-b256-0b64d850ad96 | -5.9833 | -40.961 | 2026-10-09 00:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 56.0 |
| 388bc0a8-c12c-3f87-a618-00915093bae5 | -3.1109 | -53.945 | 2026-10-09 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 112.5 |
| d4dc124c-d470-3482-81e4-06eb09f40fc6 | -3.0186 | -54.068 | 2026-10-09 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| c5b92e0f-eef1-3c45-846e-db200a0d5580 | -5.6932 | -53.487 | 2026-10-09 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 123462f7-dddd-3f3c-8fb5-4710702b0110 | -3.5676 | -54.6946 | 2026-10-09 00:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 135.3 |
| 4fc6aaec-09cd-37e5-b405-ebfc2f6334d2 | -8.7234 | -45.1355 | 2026-10-09 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 177.6 |
| 46592a13-9aca-3c2f-ba17-056dae657c0a | -11.1465 | -54.8006 | 2026-10-09 00:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| e784fcac-892f-32e7-b117-61724e9107c9 | -5.6934 | -53.4667 | 2026-10-09 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 5c66b935-cc15-321b-b771-a921db3ace56 | -7.4443 | -63.5401 | 2026-10-09 00:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| c1a622e6-17e6-3d7d-895d-b58a3b93e35f | -8.742 | -45.1563 | 2026-10-09 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 565.0 |
| 14bc8aac-aa4a-3e2a-b829-c74a017fe6c4 | -4.6282 | -49.2147 | 2026-10-09 00:20:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| bed0f7cb-7904-3389-a9d1-b09f7bdff5a3 | -6.0024 | -40.935 | 2026-10-09 00:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 142.7 |
| 702fb61f-9926-3c70-bc25-121bdaec52e1 | -2.7428 | -54.1146 | 2026-10-09 00:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 205d844e-f022-3a80-911b-976db08daaaa | -13.5117 | -44.368 | 2026-10-09 00:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 8fe89f9a-cd3c-348e-8f67-6ecdb889217e | -3.7346 | -59.4577 | 2026-10-09 00:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| f6314b88-f155-35a7-a7ab-7367186078b7 | -1.1277 | -54.18 | 2026-10-09 00:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 23420eed-7055-343e-aa14-945ac4e0399a | -1.5489 | -54.5556 | 2026-10-09 00:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |


[Clique aqui para ver as próximas entradas](README21.md)
