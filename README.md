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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1925d9b-b45f-328c-b8b5-3cf9c9237df8 | -14.0118 | -44.5614 | 2025-08-30 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 353.8 |
| 5930ec0f-a304-34eb-b0c5-1ada8ac82f95 | -8.2866 | -61.428 | 2025-08-30 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 7530dbc0-0bbc-3f0a-bf5d-5482d5908568 | -7.908 | -63.0164 | 2025-08-30 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 50e14271-14ee-377b-83c4-174a79c5cd5f | -6.5263 | -44.8659 | 2025-08-30 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 593d9ce5-4123-3283-97a5-7ececf615ea2 | -11.3106 | -63.2691 | 2025-08-30 00:00:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 950be910-cc74-37c5-8612-a05f6c2f5e33 | -9.7041 | -49.4825 | 2025-08-30 00:00:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 6a2ea556-ceb1-381b-a16b-53a925519846 | -8.9126 | -62.1058 | 2025-08-30 00:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 128.4 |
| 56b9176d-d937-32ed-a53c-0458dd967005 | -9.4498 | -62.3294 | 2025-08-30 00:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 04226f6e-a772-3d35-8c14-3d04cfaaa7ac | -6.4068 | -45.6004 | 2025-08-30 00:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 74059509-24a0-32c6-9290-c40aa6829a86 | -13.3825 | -46.9697 | 2025-08-30 00:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 110.0 |
| a928137d-4e8b-3037-a2dd-2a62e5a126f0 | -13.9923 | -44.5649 | 2025-08-30 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 137.9 |
| c1093a9b-3ea3-35e3-bee4-3f226ab92cc4 | -11.856 | -46.4487 | 2025-08-30 00:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 65f6e8dd-201b-31cc-a6d7-bd7472d9c1e6 | -9.0799 | -65.4536 | 2025-08-30 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| d146d8e5-a604-3343-906c-dd6fa9b27093 | -13.6295 | -48.1874 | 2025-08-30 00:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 246dc3ee-0d71-387a-b1cb-74bcd63cba1c | -14.0113 | -44.5849 | 2025-08-30 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 7d37f264-2e84-393d-9b7f-4dadef79f179 | -9.4497 | -62.3485 | 2025-08-30 00:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 84d1cd35-5f8e-3d43-84a6-8bf0feaf7de5 | -13.3821 | -46.9924 | 2025-08-30 00:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 130.9 |
| bf59d402-1944-35f0-99a9-8cd2114e3743 | -13.4019 | -46.9667 | 2025-08-30 00:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 98.2 |
| a634b838-d1f5-3fc4-88d8-aa4333696f70 | -9.7044 | -49.4609 | 2025-08-30 00:00:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| a1d71d44-698e-3257-b528-c7371c57a836 | -5.8753 | -46.5112 | 2025-08-30 00:00:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 41d0a65c-4415-344a-b24b-e68230727682 | -11.8373 | -46.4287 | 2025-08-30 00:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 30c77533-5ea3-3149-b450-8ea5c0d53045 | -9.0799 | -65.4349 | 2025-08-30 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 117.7 |
| dfcf293e-b6fb-311d-8cae-c0c8099a8e2f | -13.6682 | -48.1816 | 2025-08-30 00:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 3d118446-bbae-302a-989e-35e4991e1949 | -9.1155 | -65.7699 | 2025-08-30 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 179.5 |
| ac03e314-83a4-3d49-85a4-56cf9be90242 | -11.8564 | -46.426 | 2025-08-30 00:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 153.6 |
| badb0351-71af-3780-8645-ec676aafc7ab | -6.0033 | -44.7247 | 2025-08-30 00:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| d938193c-b95b-3dee-a95c-8a896213c54e | -8.894 | -62.1066 | 2025-08-30 00:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 142.1 |
| bd406780-8d6e-31e0-9d83-de8696aadac3 | -7.9081 | -62.9976 | 2025-08-30 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 073f7bbc-1d2a-3c56-b5cd-0f3577c6d1dd | -8.2867 | -61.409 | 2025-08-30 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| ea29f4ab-f0d3-3119-8210-6fed3feed854 | -8.8941 | -62.0876 | 2025-08-30 00:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| bec0519d-8d49-394d-aef3-9f04877033a8 | -8.5552 | -63.0114 | 2025-08-30 00:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 63.5 |
| d138950a-1dd8-3748-b88e-7268bdc0be89 | -9.0613 | -65.4542 | 2025-08-30 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 480b0b05-8b6c-378b-b704-b82ea2a01afc | -13.9918 | -44.5884 | 2025-08-30 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 824d5417-97d9-3551-abdb-c7686672141e | -13.6484 | -48.2068 | 2025-08-30 00:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 01abb593-fec8-3c2a-af3c-b1ae0e72013c | -8.8843 | -60.7315 | 2025-08-30 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 2487037e-a7ad-3c02-8e71-abbac460a844 | -5.8755 | -46.489 | 2025-08-30 00:00:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 38.2 |
| f1c5a0c6-9a4e-359c-913f-87e8d2003937 | -13.0154 | -56.8982 | 2025-08-30 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| a251c21a-1805-3386-979d-f0b50224c5ba | -7.7257 | -50.2751 | 2025-08-30 00:00:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 601646d6-f5f3-311a-a866-3fbfb6c4cd49 | -7.8895 | -63.0171 | 2025-08-30 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| ea288ef7-92e8-39da-8f82-04af048e0e88 | -11.8572 | -46.3807 | 2025-08-30 00:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 52b3862a-4248-3bb3-b7fe-8b98fbb88419 | -6.6129 | -43.7317 | 2025-08-30 00:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| e0937fb2-8d7c-347f-98d9-87eacbd13448 | -11.8568 | -46.4034 | 2025-08-30 00:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 0298903a-a6cb-3ec7-9e26-f18fcd5c555d | -9.1156 | -65.7513 | 2025-08-30 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 108.7 |
| e817d506-2b8d-3129-a00b-fe3f83f57bb7 | -8.5551 | -63.0303 | 2025-08-30 00:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 84.5 |
| d0d210b3-08a6-3b6c-9549-3201e84a59dd | -13.6488 | -48.1845 | 2025-08-30 00:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 192.6 |
| 3a5bf62d-161e-3c56-b115-994a20922327 | -9.0614 | -65.4355 | 2025-08-30 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 160.6 |
| 9a4ba3b3-c4b0-384f-b1ba-df57589e0512 | -13.3821 | -46.9924 | 2025-08-30 00:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 165.3 |
| 22a9127f-b6cb-340d-a45d-54c3ec993d6d | -9.4683 | -62.3476 | 2025-08-30 00:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 45.1 |
| d5cc40e1-848e-312a-9c3d-d360daa50379 | -8.894 | -62.1066 | 2025-08-30 00:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 96fbfeb6-dafa-3a85-9101-1b9143a608e4 | -9.1156 | -65.7513 | 2025-08-30 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 35.5 |
| fda2c923-61aa-3d31-8fee-e45c29d886a6 | -8.2867 | -61.409 | 2025-08-30 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| ce9d304b-5c3b-3e71-b361-e0857e7fe10c | -13.4019 | -46.9667 | 2025-08-30 00:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 9608f4b3-de28-3e6f-8325-48f2ea80de5c | -11.3106 | -63.2691 | 2025-08-30 00:10:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 104e75e4-4101-3bcb-90cf-152a1f48fce2 | -11.876 | -46.4007 | 2025-08-30 00:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| ecc792da-6985-3659-9994-32c67021b2be | -11.8572 | -46.3807 | 2025-08-30 00:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 2466b7e5-7ef6-35ae-be93-461f839c42f1 | -9.7041 | -49.4825 | 2025-08-30 00:10:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| ab24ea3e-6cf8-3dd0-b3b0-aab46e028f1f | -8.5551 | -63.0303 | 2025-08-30 00:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 957eeb09-e1b4-386f-b47c-9fe02dfc04a1 | -9.7044 | -49.4609 | 2025-08-30 00:10:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| b34a1a3d-81ac-348b-8454-c1d8009d85f6 | -6.0033 | -44.7247 | 2025-08-30 00:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| f058779b-6d53-36d9-b3d7-4f06f724d5a2 | -13.3825 | -46.9697 | 2025-08-30 00:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 114.0 |
| f8e02493-6530-374d-a703-19f0ca94e376 | -9.0799 | -65.4349 | 2025-08-30 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.8 |
| afab3020-0a73-333e-a239-3fa8efbbcab7 | -13.9918 | -44.5884 | 2025-08-30 00:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| f45ddca1-23ad-386a-9bda-1aa4bc2e1ecc | -9.0614 | -65.4355 | 2025-08-30 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 176.5 |
| 5d0d632a-9f9f-3681-a4b9-23917cd5678e | -9.4495 | -62.3675 | 2025-08-30 00:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 57eb337f-baa2-3d8d-bb8a-962820d2f437 | -7.8895 | -63.0171 | 2025-08-30 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 80a6627d-0106-31a2-a757-6d38c871a308 | -8.2866 | -61.428 | 2025-08-30 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| d237762c-0275-3aaa-849b-978f03caa927 | -9.4312 | -62.3303 | 2025-08-30 00:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 927af1a3-7e42-32d3-b3c6-cb937ebf1a63 | -13.9923 | -44.5649 | 2025-08-30 00:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| a500a869-6c1c-3afc-b576-830ba65c6070 | -7.908 | -63.0164 | 2025-08-30 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 112.0 |
| e0c1fed7-3860-3254-885c-c2dfe982c82d | -13.4014 | -46.9894 | 2025-08-30 00:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 29d0a46e-8d4c-3efe-a0a3-1e7b6bc29aea | -9.4311 | -62.3493 | 2025-08-30 00:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 105a2c48-ecca-365c-9133-8520b41e694b | -14.0113 | -44.5849 | 2025-08-30 00:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 8aa6dae1-3477-341d-a008-49b0fe65f9e7 | -13.6488 | -48.1845 | 2025-08-30 00:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 2c8360a3-231b-3460-b868-4fc85d48c93d | -9.0799 | -65.4536 | 2025-08-30 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 53ceb5b5-0028-33d5-afdc-30b1ab11c894 | -7.9081 | -62.9976 | 2025-08-30 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 27a2c611-7061-3654-bd54-661ff0d33b67 | -9.1155 | -65.7699 | 2025-08-30 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| adee723a-45d3-3e53-84e5-ba85cae11f08 | -11.8568 | -46.4034 | 2025-08-30 00:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| a6ed1331-6fc2-3227-8d63-bb6115214046 | -11.8764 | -46.378 | 2025-08-30 00:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| b5f51647-d28d-3a17-a09d-d218c72f0326 | -8.5314 | -64.0108 | 2025-08-30 00:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 38.1 |
| be22bf51-a9c0-30f9-9703-2299ef975090 | -11.3517 | -43.566 | 2025-08-30 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 4991e50f-609b-3e50-b854-daff2f59c7ff | -14.0118 | -44.5614 | 2025-08-30 00:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 127.2 |
| f25fb9cf-3a60-30e2-b6b2-b6805812692c | -11.8564 | -46.426 | 2025-08-30 00:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| ab489a30-fd47-3454-9642-715246683010 | -9.0613 | -65.4542 | 2025-08-30 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 110.2 |
| dde4d9d5-6b13-3b22-b8ba-d7e4e303c36c | -7.4157 | -49.5116 | 2025-08-30 00:10:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| d2eb2082-7243-307f-abf3-f9946afb64f7 | -9.4497 | -62.3485 | 2025-08-30 00:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 144.4 |
| 77e306db-d817-3ee4-85bf-4fc58f95831d | -9.4498 | -62.3294 | 2025-08-30 00:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 162.0 |
| efb757e5-b161-398c-8f1d-123f6cf834df | -8.9126 | -62.1058 | 2025-08-30 00:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 129.3 |
| 8976ae17-55fa-379b-a7ef-b1e9a2cf3a94 | -11.8568 | -46.4034 | 2025-08-30 00:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 65868e47-36bd-3e7c-8539-b44aab9ab4ef | -13.3821 | -46.9924 | 2025-08-30 00:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 123.0 |
| d50f1c49-4276-3944-bf6d-8561ce55e788 | -9.4498 | -62.3294 | 2025-08-30 00:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 186.2 |
| b07624f3-9b44-3adc-a88b-2484ab1ff229 | -13.3825 | -46.9697 | 2025-08-30 00:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 86.7 |
| a17094a3-84cb-3b7e-9553-b40655b62d93 | -11.3321 | -43.5926 | 2025-08-30 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 05974bcb-dc9a-3062-9527-b954ef8057e6 | -11.3513 | -43.5897 | 2025-08-30 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 30cfd2ef-8f69-321c-a23c-5f218a7d523c | -7.8896 | -62.9982 | 2025-08-30 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| e654021c-0150-30be-b805-de6b685a5603 | -9.4495 | -62.3675 | 2025-08-30 00:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 713ec09f-72b9-32c5-94e3-4fe91a011ed8 | -9.4312 | -62.3303 | 2025-08-30 00:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 3f0ef2b6-3fee-31a0-b8f9-94be0838081a | -5.6268 | -45.0025 | 2025-08-30 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 176.3 |
| 43d7f080-d524-3db7-b286-08364a157772 | -13.6488 | -48.1845 | 2025-08-30 00:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 90.9 |
| a83cf21a-e043-3f6c-a5c4-87dc71397abb | -9.0799 | -65.4536 | 2025-08-30 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 4c26e7ee-b7a1-3818-ac4a-c2b58f293496 | -5.6081 | -45.0038 | 2025-08-30 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 275.2 |


[Clique aqui para ver as próximas entradas](README2.md)
