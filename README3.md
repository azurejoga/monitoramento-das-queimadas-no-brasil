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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8706b0ce-dabf-3509-949a-3268b8fad021 | -9.1714 | -59.5793 | 2025-08-30 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 789fd629-3c02-32e3-878e-f6e8dfcab357 | -9.0799 | -65.4536 | 2025-08-30 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 3760cfa2-3b76-3fc5-9cae-3dc997301588 | -11.8576 | -46.358 | 2025-08-30 00:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 64272731-280b-3813-8108-4db12f9fd4a3 | -11.3312 | -43.6399 | 2025-08-30 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 6eed063f-fa4c-3553-b6df-c75814c0ef9b | -13.4019 | -46.9667 | 2025-08-30 00:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 840c28b2-3e4d-3552-bca6-de587b321668 | -11.838 | -46.3834 | 2025-08-30 00:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| a24a67fd-5b56-3b5c-be04-258016dcbc8b | -11.8568 | -46.4034 | 2025-08-30 00:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| facb5875-0cdb-33c2-8694-b3aa5f371e7b | -11.3517 | -43.566 | 2025-08-30 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.2 |
| f3deb7c2-c2f8-309f-945c-66917a164f8e | -11.3513 | -43.5897 | 2025-08-30 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 0d08602f-7ef8-3136-a1f5-68a77b21ba93 | -9.7044 | -49.4609 | 2025-08-30 00:40:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 5ef502a0-6e6a-395f-9411-ecf68f3a3afb | -11.2929 | -43.6456 | 2025-08-30 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 41.5 |
| fb8e7d1f-0b78-3a9e-834d-9499bd80ee78 | -5.6266 | -45.0252 | 2025-08-30 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 875fff99-3eb3-3a02-8244-0faffd2e0ab3 | -11.8572 | -46.3807 | 2025-08-30 00:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 271.9 |
| 85dd9000-d9b7-3757-a238-f2b541e0ad56 | -9.1155 | -65.7699 | 2025-08-30 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 115.7 |
| bbd47c54-217b-3f38-811b-25c5e8c73c96 | -23.6978 | -51.7916 | 2025-08-30 00:50:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 86.9 |
| 0dbf8f3f-5be4-3687-963e-b1d4b1d793de | -8.9126 | -62.1058 | 2025-08-30 00:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 53cf659b-27a5-3d08-8030-372cf29651f2 | -9.0799 | -65.4349 | 2025-08-30 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 102.7 |
| b43243df-69d7-3588-83a0-e72fef105ea2 | -13.3821 | -46.9924 | 2025-08-30 00:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 217.9 |
| fc18cdb3-1751-3045-9d99-c838a8108bf4 | -9.1156 | -65.7513 | 2025-08-30 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| dc413672-60e3-31fb-9d42-773c9c1e5e7a | -9.4435 | -60.5307 | 2025-08-30 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 132.7 |
| a5306058-1d44-3da8-b834-1812f1cb2ae4 | -8.8843 | -60.7315 | 2025-08-30 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 147.5 |
| 6692f952-fabf-3614-8b72-e330ab9fc056 | -9.462 | -60.549 | 2025-08-30 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 6d1c5f91-af11-32e1-9706-94e0771221bb | -13.3628 | -46.9953 | 2025-08-30 00:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 114.8 |
| f12a815f-6ee8-3a50-af07-f854ae204e34 | -9.1714 | -59.5793 | 2025-08-30 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 5de9c13d-1c0d-3a7e-aa5f-e195b978c238 | -11.856 | -46.4487 | 2025-08-30 00:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 1a957e9d-3484-38e1-9d26-4e3ee6218ffe | -5.6268 | -45.0025 | 2025-08-30 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 209.7 |
| 00b9d65a-cf6e-34f8-a271-cb9d79638724 | -11.2929 | -43.6456 | 2025-08-30 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 8f6f30a3-30dc-35df-851c-fb96e9024bb0 | -11.312 | -43.6428 | 2025-08-30 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 159.5 |
| 4961d688-3228-3449-9f81-46eb69dc3799 | -6.0033 | -44.7247 | 2025-08-30 00:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| a13265e7-3be5-30f0-b037-bc1c850ee3ca | -9.4432 | -60.5692 | 2025-08-30 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 147.9 |
| f5852a1d-df7b-3841-a19a-9e72a6a842d1 | -9.0799 | -65.4536 | 2025-08-30 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| ea9750d0-cfd2-3599-b45d-e5c0a2fcb796 | -13.3825 | -46.9697 | 2025-08-30 00:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 60bdab08-8a55-3f84-9d05-7fc066d1be63 | -11.3317 | -43.6162 | 2025-08-30 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| c13b5b89-bbb0-383d-a54a-09666bfb04f2 | -7.8895 | -63.0171 | 2025-08-30 00:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 76712863-8b55-3f93-a7f5-813626792899 | -11.3106 | -63.2691 | 2025-08-30 00:50:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 7c450122-aa94-3e3d-a5de-e4396894c566 | -9.7044 | -49.4609 | 2025-08-30 00:50:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 8b9ebc44-feb8-3d99-bf25-ca8868e2ada3 | -9.4433 | -60.5499 | 2025-08-30 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 276.9 |
| 41354af9-f09d-38a3-ac93-e23e188bee65 | -12.0153 | -43.9818 | 2025-08-30 00:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| daddd975-07ce-3443-a094-168fbb970cc9 | -8.894 | -62.1066 | 2025-08-30 00:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 2ee81c29-fda7-365a-9efc-a4fe5d0a12bd | -11.3125 | -43.6191 | 2025-08-30 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 909286a7-3c26-39d3-bc36-c449cae3c12c | -9.0613 | -65.4542 | 2025-08-30 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 6450366f-5109-3eb4-a3b9-de8ce5546b16 | -8.5551 | -63.0303 | 2025-08-30 00:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 9c1f6c03-bee3-3c6e-989b-9d58694e97fd | -9.0614 | -65.4355 | 2025-08-30 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 26760074-7ae4-3680-8c95-0499f62c8520 | -5.6081 | -45.0038 | 2025-08-30 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 208.0 |
| 88dac7df-c718-3926-80b2-bea619e82cf3 | -9.4497 | -62.3485 | 2025-08-30 00:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 65673fcc-3425-333e-a4fd-13c1f98cb541 | -9.1155 | -65.7699 | 2025-08-30 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 124.9 |
| b46b4dfa-191c-3210-a20d-b7c36afdcbd4 | -5.6266 | -45.0252 | 2025-08-30 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 6cd7459e-3ce5-3b36-affe-246913683105 | -13.3817 | -47.015 | 2025-08-30 00:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 4b6f8994-4f1d-3962-9e27-30ffcaf6c04b | -5.6079 | -45.0265 | 2025-08-30 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 5dcf06a7-144c-3ecc-bb2f-f3ce943aa392 | -8.8842 | -60.7507 | 2025-08-30 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| b8e7837b-1b8d-3613-8523-b7cdf97520ee | -11.2917 | -63.2891 | 2025-08-30 00:50:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 16d3c2af-86ab-3bc3-9d2e-2dd1b1f2a2bc | -13.6488 | -48.1845 | 2025-08-30 00:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 421756cc-4f17-3083-9801-e0103a5d2f13 | -11.3321 | -43.5926 | 2025-08-30 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| dbf4aed5-a23a-33f0-a165-fcfa315fd925 | -9.4247 | -60.5509 | 2025-08-30 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 5446840a-98eb-3063-b3e9-f10ed8f4fb67 | -7.908 | -63.0164 | 2025-08-30 00:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 4ff2191b-3929-3f6f-9c84-793fa3183213 | -11.3312 | -43.6399 | 2025-08-30 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 7bf63cea-0909-3a24-b8d9-70999f69f52a | -11.2918 | -63.27 | 2025-08-30 00:50:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 46.7 |
| d407ad4d-34d6-314e-b896-2a6ee8927299 | -8.8658 | -60.7324 | 2025-08-30 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| b2a73871-f261-3989-a716-6606f14167fb | -9.4618 | -60.5682 | 2025-08-30 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 9953a77b-fdb2-3470-af61-43642d92d4e6 | -13.4014 | -46.9894 | 2025-08-30 00:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 2c31d18d-3964-39c7-9cb8-c1c0f2d3b902 | -9.4311 | -62.3493 | 2025-08-30 01:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 99fa5264-9a1d-3536-a979-c760900e6245 | -11.3317 | -43.6162 | 2025-08-30 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 39f72427-b836-345f-b2d1-96b2be690eb1 | -9.7044 | -49.4609 | 2025-08-30 01:00:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 769869bc-c6cc-3cdd-901b-88d1f79591b2 | -9.4312 | -62.3303 | 2025-08-30 01:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 37.1 |
| c3c4b6ee-ca7f-30f1-906c-f9f39eca27a0 | -9.0799 | -65.4349 | 2025-08-30 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| caee01a3-2822-3e66-99a1-53a721f8cfbb | -9.4435 | -60.5307 | 2025-08-30 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 115.9 |
| b40f49e8-92b9-342d-b14d-4a5ec96194dc | -13.3817 | -47.015 | 2025-08-30 01:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 121.2 |
| b4e5bce0-5a8a-35a2-8295-34e8a13e0dfe | -5.6266 | -45.0252 | 2025-08-30 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 42.2 |
| e4876227-2035-30c7-9f07-d1d96bf6aa11 | -13.3821 | -46.9924 | 2025-08-30 01:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 275.3 |
| d40503cb-5ab1-3bfd-88a1-f832958bbb42 | -9.0614 | -65.4355 | 2025-08-30 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 117.7 |
| df82dd72-7f45-3dc9-b59b-8e278092d918 | -9.4618 | -60.5682 | 2025-08-30 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 727b6e2d-858e-3fb7-b945-80435482bc23 | -11.3321 | -43.5926 | 2025-08-30 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 94914790-babf-3722-8a07-9487d126e224 | -9.7041 | -49.4825 | 2025-08-30 01:00:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 3c374751-b6a9-368c-9da6-1d59da34fef5 | -11.3312 | -43.6399 | 2025-08-30 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 4f339eba-f6ac-3ac5-a556-00e86378aebf | -9.1155 | -65.7699 | 2025-08-30 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 125.6 |
| 7887a158-6144-3a98-a5fe-87f92c407627 | -11.2918 | -63.27 | 2025-08-30 01:00:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 28ffdfbe-2db9-3a96-838e-cd1ac10ddbc1 | -9.462 | -60.549 | 2025-08-30 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 03aef0cf-086d-3bd0-b2b2-c9089218e856 | -12.0153 | -43.9818 | 2025-08-30 01:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 8a96a371-53f4-3f98-b189-6f9021549c19 | -11.3517 | -43.566 | 2025-08-30 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 7dab90cb-67ae-3535-a476-3afaaca5a1e6 | -8.9126 | -62.1058 | 2025-08-30 01:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 119.9 |
| 76319fb9-bde6-37b0-8e8f-11ca564c4e4c | -8.8843 | -60.7315 | 2025-08-30 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 6ec88d32-5b49-3c4e-bd4b-4b2a038f646c | -9.4498 | -62.3294 | 2025-08-30 01:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 87d0f5dc-f9e0-3356-8228-38abba96f9e5 | -8.894 | -62.1066 | 2025-08-30 01:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 707c5c1b-e6a2-36e3-a7e6-79445ef27c20 | -5.6083 | -44.9811 | 2025-08-30 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 053c87ea-122f-3fef-9393-608ef510d203 | -5.6081 | -45.0038 | 2025-08-30 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 280.2 |
| 40bb6528-d8fe-3033-b3ee-7976817733a3 | -11.312 | -43.6428 | 2025-08-30 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 208.4 |
| fa0e3192-6c78-352e-b274-0783d901e16c | -9.4432 | -60.5692 | 2025-08-30 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 126.1 |
| 930df680-f4fa-305b-b498-2575042676ce | -9.4247 | -60.5509 | 2025-08-30 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 0426b18f-e534-31ec-b940-21c597bb083d | -13.4014 | -46.9894 | 2025-08-30 01:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 05f5215d-55cc-3544-9d21-c4586d47b203 | -11.3513 | -43.5897 | 2025-08-30 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| c7c76c10-ac4b-3bb9-b9dc-75b8431b8cec | -9.0799 | -65.4536 | 2025-08-30 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| dc9c6822-ea8f-3626-ba51-f7263c5a71e2 | -7.7257 | -50.2751 | 2025-08-30 01:00:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 4129dab7-d41a-31cd-816f-c2daba4911fd | -11.3116 | -43.6664 | 2025-08-30 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 5f330fb3-4102-39b3-80da-0b1bc880c6d9 | -9.4433 | -60.5499 | 2025-08-30 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 258.9 |
| ca088011-9029-38df-b7b5-38987b83dc68 | -5.6268 | -45.0025 | 2025-08-30 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 68551a1e-b7a1-304d-8ec8-7bec1a6b2d48 | -8.5551 | -63.0303 | 2025-08-30 01:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 14ba4aed-cacc-3d09-b247-28dc8554150c | -9.4497 | -62.3485 | 2025-08-30 01:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 60.1 |
| e9d3a075-3a74-3a4f-98e7-c097d96f2967 | -13.3628 | -46.9953 | 2025-08-30 01:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 16146050-e56a-3dc2-a295-78c4b2269cc5 | -13.3825 | -46.9697 | 2025-08-30 01:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 090394b5-155b-3138-9f33-04e180af9869 | -9.4383 | -40.3668 | 2025-08-30 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 82.5 |


[Clique aqui para ver as próximas entradas](README4.md)
