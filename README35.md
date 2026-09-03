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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 478c3a58-d047-3c73-9c63-cf8b347a59aa | -6.14729 | -55.6739 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 015ffe3f-831d-3a35-8bab-031ba6c86d5f | -9.71097 | -54.33798 | 2026-09-03 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ae349a9-4474-32c2-a473-d1ab0a9c1a85 | -3.1988 | -61.21084 | 2026-09-03 04:57:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69eeb3e8-83fa-3b13-8964-e4695152510b | -10.48785 | -48.6446 | 2026-09-03 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 09e47146-7cd9-3c36-bfa9-b65b281ad6aa | -6.68452 | -59.93854 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2b33682a-31ef-3dac-92e6-a79825e08500 | -7.72923 | -49.58983 | 2026-09-03 04:57:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5812124-142d-3342-82b3-271dd876b30d | -8.70543 | -52.36247 | 2026-09-03 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 472f51ed-69c9-3024-a625-6868a46a39f5 | -6.69288 | -59.94518 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58c84aeb-c441-3b70-acdc-029b2d282a16 | -5.802 | -50.13261 | 2026-09-03 04:57:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f006f4f8-d47b-3b71-981c-cac67a910a08 | -10.91279 | -45.34586 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 33b3ec25-1852-3332-b560-62b8bcf56ef7 | -3.12014 | -61.23508 | 2026-09-03 04:57:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 352e6d17-f6a8-33e1-a7c0-0fe62fe6f0af | -7.24723 | -59.52177 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0750101e-084e-3b2a-a815-950d7f706998 | -9.7203 | -51.23118 | 2026-09-03 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4384cc8c-947c-39f9-9d0b-ef0d7fdd9923 | -10.23105 | -50.29032 | 2026-09-03 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9672a03-55e6-3c02-be49-7468def2d284 | -4.09735 | -60.66576 | 2026-09-03 04:57:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40244ae8-24d0-3aeb-a943-a01f79ecc92c | -5.2462 | -55.90805 | 2026-09-03 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a444e327-3da2-31af-b91e-0917fb2bab9d | -7.82804 | -50.2427 | 2026-09-03 04:57:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 207f0f1a-2b0b-35b9-aaab-2698e808f5fa | -6.25527 | -55.43626 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ca9005f-fece-3dc6-aa6d-d80d55123093 | -8.42916 | -54.7006 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16bcf393-b609-3958-8b9f-e23cf41e39bf | -5.88771 | -49.88087 | 2026-09-03 04:57:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67ea41dd-ac18-3bcc-b344-5bfaed9bb582 | -6.05542 | -53.80334 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 085297b0-63c1-3640-a775-809dd7499a8b | -5.80697 | -43.6445 | 2026-09-03 04:57:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d7219737-1042-3763-9860-fb6b524e60bf | -8.45566 | -54.68634 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a16eef61-55fe-3a3a-9310-9de27a695767 | -5.85309 | -57.55101 | 2026-09-03 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 45eb1fc0-a8e3-3085-8048-39c6b63b9c16 | -8.08724 | -50.96728 | 2026-09-03 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f9550bd1-f290-3fce-aef8-2aa9087380b6 | -9.70297 | -57.89215 | 2026-09-03 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bab25d5a-7a26-38d8-acba-1c0b97d68179 | -3.07943 | -61.18349 | 2026-09-03 04:57:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f1b4cae-83df-3bb3-bb94-38292ed1b30f | -6.31827 | -56.04363 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d2b862f0-465d-303d-a505-a36f060463c9 | -4.97303 | -55.85926 | 2026-09-03 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 64798101-61df-3ae4-a31e-72f4b3d00ccd | -6.07018 | -53.66843 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3936d28-1961-302a-b696-e0a654244265 | -6.74695 | -59.43853 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b64839b0-f9c1-3848-8a86-4375c427bb3a | -4.9621 | -55.85741 | 2026-09-03 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b48ba0e-69b3-33f6-9e2e-2fff3ec7f1c1 | -3.19991 | -61.2042 | 2026-09-03 04:57:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e02e1b26-ce15-34c0-bd79-6ad1c60bf327 | -6.31325 | -56.05147 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 45a2fd80-9175-393e-89c6-62ce648c6f28 | -7.04171 | -59.22004 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e995ef92-b630-37b0-b1df-9bd107318575 | -8.43369 | -54.69392 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4f026abb-0c55-3d97-91c4-8ad313191187 | -10.88626 | -45.31127 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34b53223-f2bf-3341-986d-1193942c7720 | -3.3249 | -59.45583 | 2026-09-03 04:57:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec9dc6f2-9e78-38c5-8849-e33273fcd902 | -5.97997 | -55.70379 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d57c4e4e-9e68-3b28-a0e1-5ca86c5040cc | -6.65102 | -59.44692 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1fe0fc67-0f97-32e3-b3b7-fe4dc3f96473 | -8.46144 | -54.65038 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2f4c006-8ab4-3006-99fb-763d97a4162d | -10.31462 | -49.94716 | 2026-09-03 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 032d193c-907b-31f1-a277-133669bb87b9 | -9.01782 | -65.45657 | 2026-09-03 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebec43d6-a600-3e2e-8b71-592988a36f9d | -6.24758 | -55.43913 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 194ca1f9-2b43-3357-8c5f-6aafd366587e | -7.3201 | -55.1359 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3436a77f-a078-3d17-8769-fdd1d5642a1e | -6.32119 | -56.04846 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fe53f79-f593-3c4f-abb3-6d6c995b5c29 | -8.4596 | -54.68329 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1fa88ed-7b64-3458-a769-d48a45c41fe7 | -3.02326 | -61.48241 | 2026-09-03 04:57:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98d93b76-4f87-38ae-a5dc-f8b13cfae3e6 | -8.46086 | -54.65398 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f347a92-c1e0-3b4e-a3e8-7cf6bd771e41 | -9.15338 | -49.97899 | 2026-09-03 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5224af10-08d6-36ff-b079-69e85635734a | -6.31611 | -54.75423 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e86a8731-e63b-3122-a4e2-434595ef0f69 | -5.58776 | -60.20074 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2d211d60-d4dd-37e4-9ee6-ca52d349f054 | -8.43168 | -54.74932 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 1210db0c-05e0-3082-8531-cd022594053d | -8.45518 | -54.66783 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f623bd4c-f03a-36eb-b679-c7aaacedd8de | -6.3067 | -56.04604 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| de168cc4-eae2-3def-89af-2ae36ff1f540 | -11.27978 | -45.1694 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c55c3282-18fc-3629-a4b6-39ba2327c51d | -6.31757 | -56.04786 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1e434ec3-333b-3c41-8b23-166dcc2219c7 | -6.24822 | -55.43517 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26195181-ec0d-3f0c-b6ff-8fb50133909e | -3.61485 | -60.5673 | 2026-09-03 04:57:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e5835a8e-765e-3f93-97ca-51d4df4510bb | -6.6211 | -55.23393 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4ecb475-d149-35ba-b778-f36204ef5480 | -10.89178 | -45.30876 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08d05cbf-cb3a-36be-813b-d41232da7040 | -6.75822 | -44.57568 | 2026-09-03 04:57:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7611c02b-3375-3ec1-8c17-c38aa2cb689a | -5.54766 | -60.23409 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0560e80e-fca7-37e4-a108-d84fb9d688f0 | -6.76141 | -56.33326 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46ada67d-7418-37b5-9402-7fc969b41306 | -7.44998 | -61.37343 | 2026-09-03 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a65ff1a-2005-3d58-ae87-7fc9ff8196a0 | -11.30237 | -50.518 | 2026-09-03 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 0e5da3e9-6fd2-385a-bc9d-13c86af0541f | -6.59853 | -59.11838 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e264ce9c-666a-347d-b9d2-f8cb698083d1 | -11.32003 | -50.52509 | 2026-09-03 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 45311394-90e2-3d4c-94bc-2f600e907972 | -8.46019 | -54.67967 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c96af1b-bc19-3d77-8f69-85c3da0a17b2 | -6.87558 | -59.40082 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d2fa607-8cd3-39bf-b377-041e34e7ebc6 | -8.45413 | -54.65287 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3593e0ba-6562-3bd8-b515-d40e761c1dbe | -8.46355 | -54.68021 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee3c147a-db3c-332f-af86-4a4ee64a767b | -8.46076 | -54.67608 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0abf4931-cb1e-3095-a447-a9f12c8203df | -8.08262 | -50.97441 | 2026-09-03 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3ec25fe7-3ac5-30bf-a56d-e683b02fcfa1 | -6.52537 | -55.24285 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16e19f8c-3d85-3b2c-9e44-975abcad64c0 | -7.04313 | -59.21159 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| beb315a9-44c2-3652-9311-7a923a822478 | -8.46875 | -54.64786 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 423560b7-7402-35cb-bc76-16641bdb2296 | -7.07957 | -56.51864 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6538261e-44e4-335c-a65c-a7acc0024f73 | -8.07397 | -50.96131 | 2026-09-03 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1cd7c5f-e70b-3afd-9445-4ea850cd596a | -8.43428 | -54.6903 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5b2ea46d-5866-3740-9ea2-248f60c70dcf | -11.28417 | -45.17639 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbe14f3d-33b0-3bde-9f69-a201492758cc | -5.92787 | -52.20992 | 2026-09-03 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23348b56-1a8c-3331-997d-b2ede661fb55 | -10.75478 | -48.9749 | 2026-09-03 04:57:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 47aa441d-7b52-3955-9169-7aea03885781 | -7.33648 | -55.2087 | 2026-09-03 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22ea8d30-6528-39e8-8a70-36ef12ca05f3 | -7.05549 | -59.21815 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff75142d-95b3-3d41-8b45-a0f66acda753 | -7.26897 | -61.11502 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52d97536-6253-37e3-84e7-3cdab3b1e8b9 | -6.62867 | -55.23123 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e11b4e2-2b44-336e-b40e-e188c4084133 | -6.39022 | -55.229 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f511c97b-5bd3-3707-9203-d3e0f5a03610 | -4.41411 | -55.7722 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 194c4ce8-8ef7-39d7-aa8f-cafd7093898b | -5.80118 | -43.64706 | 2026-09-03 04:57:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b09b1ba-07a2-3dae-892d-4b76d5f205ca | -6.67742 | -59.95224 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| edaa3c54-6f7f-3856-9c4f-94209467a9f4 | -9.08932 | -47.81908 | 2026-09-03 04:57:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e804c7cd-8a1c-310d-9ac4-1cb28d0322f8 | -9.82977 | -59.48004 | 2026-09-03 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68fffc24-b1fb-31bf-8434-e3b0a7cc0e0d | -6.10647 | -53.52681 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1195f9e5-c3d4-33ed-bf90-1bba09965c62 | -6.49119 | -53.60612 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51acc053-ecc0-3dec-ba80-11185dc2072f | -9.09478 | -65.5111 | 2026-09-03 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21d9c746-4896-38c0-8394-97e4318abf8d | -6.7744 | -56.41542 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06090605-3ee4-3268-9433-e87459f1d392 | -8.22044 | -54.97412 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9f118e0-15cb-3598-bebf-3a9beb5adde6 | -8.46413 | -54.67662 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80b2855b-0686-3212-9bef-6a0460a5c2b9 | -8.46481 | -54.65092 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README36.md)
