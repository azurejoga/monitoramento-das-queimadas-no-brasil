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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9aaead35-98de-33a5-8ebf-e470eeaca551 | -13.3817 | -47.015 | 2025-08-30 01:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 162.5 |
| 3ca75f15-2d99-308c-b21d-426d76086428 | -9.0613 | -65.4542 | 2025-08-30 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| c278abc0-d104-3dfc-9f15-3eb3020abea5 | -11.312 | -43.6428 | 2025-08-30 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 2845bd7b-a920-3434-8f1e-532954a546ea | -11.3513 | -43.5897 | 2025-08-30 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 7cf0705e-63b5-3ae5-8c4d-3e743882126f | -9.0799 | -65.4536 | 2025-08-30 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| fe24daf4-e5da-3786-99bb-9b2784d2f05a | -8.894 | -62.1066 | 2025-08-30 01:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 5f3923c2-644a-3ce8-b93d-0dd4e2a06f66 | -8.9125 | -62.1249 | 2025-08-30 01:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 63661bba-b78e-3281-a35f-6c6a6951a6e6 | -9.0614 | -65.4355 | 2025-08-30 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 74828a64-dcb4-3abf-b919-ddc088b3515a | -11.8564 | -46.426 | 2025-08-30 01:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 4cc65ad5-12e0-33ea-91e3-5516669ac756 | -9.1156 | -65.7513 | 2025-08-30 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 1e8f302c-df8c-3e48-af74-810968495ee6 | -8.9126 | -62.1058 | 2025-08-30 01:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 146.4 |
| b30bc5fb-e165-3ac0-88e0-72f2c07b4c3b | -5.6081 | -45.0038 | 2025-08-30 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 144.8 |
| b131f705-d801-3fe9-a7c7-9e7e91126e9c | -11.3317 | -43.6162 | 2025-08-30 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 53358edb-234c-3b1f-ba3e-50afa83ec9f7 | -13.3628 | -46.9953 | 2025-08-30 01:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 2a640675-7d60-3fae-8052-afe540ccee91 | -11.3125 | -43.6191 | 2025-08-30 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 4120eeb4-9bc5-3286-8597-a71f52a582b8 | -13.3821 | -46.9924 | 2025-08-30 01:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 178.8 |
| 4f7aa2e9-3594-348c-ba2b-4cfb060aa4f6 | -9.1155 | -65.7699 | 2025-08-30 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 153d05eb-bde3-3488-962d-237ca81b48af | -13.3623 | -47.018 | 2025-08-30 01:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 0f15f7ba-0f87-3fe5-906d-8bdb0a002b08 | -12.0153 | -43.9818 | 2025-08-30 01:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 7b315689-fd3e-3216-8360-e73f10c8e21b | -9.462 | -60.549 | 2025-08-30 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| cd9b7520-9e48-30b2-a09b-24c5891ec940 | -8.8843 | -60.7315 | 2025-08-30 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 3c0934a5-cda7-3546-aa34-5c38006236e0 | -13.3821 | -46.9924 | 2025-08-30 02:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 188.2 |
| cfa10504-8599-3bf2-8673-5b979b4712c1 | -13.3623 | -47.018 | 2025-08-30 02:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 96b83692-8631-3e5c-8029-42630988fed5 | -8.894 | -62.1066 | 2025-08-30 02:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 5a4778d3-bbe7-343f-8d80-c9d21487f2d1 | -11.8384 | -46.3607 | 2025-08-30 02:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 92fa802f-7994-3f87-9018-2935c97a0a54 | -11.3517 | -43.566 | 2025-08-30 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 56.6 |
| f220c47a-21f0-31ea-922d-f311f3d3832d | -9.4618 | -60.5682 | 2025-08-30 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| e1d93af3-f4f8-38b3-8c6b-355fae04840e | -9.1156 | -65.7513 | 2025-08-30 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 71aeaf4e-c170-313c-8396-f953d575ba52 | -9.0614 | -65.4355 | 2025-08-30 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 101.6 |
| d0d67122-0894-349f-aa6d-840eb5993484 | -11.8576 | -46.358 | 2025-08-30 02:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 7743a44c-6581-38ab-a0d2-55086a5a2022 | -9.4433 | -60.5499 | 2025-08-30 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 192.8 |
| 54ee3557-b867-3661-872c-c64c157bb987 | -9.0799 | -65.4536 | 2025-08-30 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| abda247d-be12-34f4-ba0a-f8e5304c9a52 | -11.8764 | -46.378 | 2025-08-30 02:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| f92ffc0f-e13b-36de-ba35-1c61882f764d | -9.4432 | -60.5692 | 2025-08-30 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| de19e3a6-63bd-36b2-b897-da6d750a8d9c | -11.312 | -43.6428 | 2025-08-30 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 4ed29dbf-b507-3897-8669-244700f5ef13 | -9.462 | -60.549 | 2025-08-30 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 6a6a28c7-ff5d-31aa-bd3f-bccaef75b30e | -8.9126 | -62.1058 | 2025-08-30 02:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 148.7 |
| 18f20b1a-6eb1-3b3a-b2d3-f2be68ffac2c | -13.3825 | -46.9697 | 2025-08-30 02:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 7d9ecde3-a52e-3ed7-9347-80ea0b4f9901 | -13.3817 | -47.015 | 2025-08-30 02:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 175.4 |
| 287265d1-ad26-3bea-afea-f00f60211929 | -11.3125 | -43.6191 | 2025-08-30 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| c764e5f5-39a9-3b30-9abe-9d45a3058c77 | -13.9923 | -44.5649 | 2025-08-30 02:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| c63a13c4-745b-3a67-bfc7-2cd9f0b0b1c7 | -14.0113 | -44.5849 | 2025-08-30 02:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 159.4 |
| e31a0cae-e1b0-30d4-bfaa-71949fca2c37 | -11.8568 | -46.4034 | 2025-08-30 02:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 43ebbd6b-7d76-39f8-8beb-cfe900470236 | -11.8564 | -46.426 | 2025-08-30 02:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 539b2e40-6d8d-33fa-b572-ba3f74637b07 | -11.8572 | -46.3807 | 2025-08-30 02:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 221.0 |
| 83bd64ee-f628-34e6-bbe9-f8d917c6032c | -5.6081 | -45.0038 | 2025-08-30 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 333c599c-27fe-3ca7-a15d-0162537fa7d9 | -9.0613 | -65.4542 | 2025-08-30 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 61d11434-a1ee-3ce6-a695-0263c6c181c4 | -5.6268 | -45.0025 | 2025-08-30 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| ea20244f-ae71-330e-9bf6-6351d8d1f684 | -11.838 | -46.3834 | 2025-08-30 02:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 569b8184-a1e7-30c4-9e6d-52097d9b433b | -11.3317 | -43.6162 | 2025-08-30 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 320fa5fb-504b-3bef-ae51-a011e65ce337 | -9.1155 | -65.7699 | 2025-08-30 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 7e3beed3-9b55-337b-8703-1e5d9062c62c | -9.8311 | -63.8484 | 2025-08-30 02:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 3569a1a6-2f70-3138-abdc-71b32f5482a5 | -11.3513 | -43.5897 | 2025-08-30 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 49363a03-3e80-3b51-969d-7e3d8850c7ed | -9.4435 | -60.5307 | 2025-08-30 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| e7167d46-7499-3951-b2a4-9ceab67cd476 | -14.0118 | -44.5614 | 2025-08-30 02:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 142.7 |
| e84f1569-1673-3924-95aa-8e3703097a31 | -13.3628 | -46.9953 | 2025-08-30 02:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 9266171d-88e1-36da-b28c-23839af0eb26 | -9.0799 | -65.4349 | 2025-08-30 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| b0339fbc-588f-3ac8-ae10-4b3e03afe982 | -13.9918 | -44.5884 | 2025-08-30 02:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| a6db7c33-0e9c-3d2c-b0bd-f45b3ce0ba0e | -13.3825 | -46.9697 | 2025-08-30 02:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 3ad96843-f3b9-34b7-995b-ed72a8b0bc06 | -9.0614 | -65.4355 | 2025-08-30 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 4e25d264-9c20-3193-a2c1-4a98f9814832 | -11.838 | -46.3834 | 2025-08-30 02:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 2ead8426-e53b-3807-a788-1223d227e427 | -11.8572 | -46.3807 | 2025-08-30 02:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 236.1 |
| 65a2d40e-cce5-3386-9b91-94041e925547 | -9.462 | -60.549 | 2025-08-30 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| b1e42e7f-8e25-37c5-9673-99bdda0b9705 | -8.894 | -62.1066 | 2025-08-30 02:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 5757fb5b-ef14-3fa6-9c70-afb91698c850 | -13.3821 | -46.9924 | 2025-08-30 02:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 182.4 |
| acf0fc3c-8a8c-3ee8-962f-f0a89ceba734 | -5.6081 | -45.0038 | 2025-08-30 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 481811dc-0c09-32a2-b469-190aa71ab584 | -9.4432 | -60.5692 | 2025-08-30 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 231b86e3-5e2b-3025-9974-c55bb4db599d | -11.3321 | -43.5926 | 2025-08-30 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| c095d12c-c271-3b13-ab86-a1fb684a58ad | -9.0613 | -65.4542 | 2025-08-30 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 2a68e3d9-73e5-3639-95bc-dbe978cabe3c | -11.8384 | -46.3607 | 2025-08-30 02:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| ce2f3b30-3940-3f4a-9bf4-61cded03b9fb | -8.8658 | -60.7324 | 2025-08-30 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| f1be9016-6f69-39d2-b95a-671937a2bf10 | -11.8764 | -46.378 | 2025-08-30 02:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 45a437ea-2a51-32bd-b40e-bb5294bed7ec | -13.3628 | -46.9953 | 2025-08-30 02:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 46646fc7-1dcc-3770-bbdc-974f437e888c | -9.0799 | -65.4536 | 2025-08-30 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| f3ae4707-f0a4-3c88-b093-da9ff8dea124 | -11.312 | -43.6428 | 2025-08-30 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 0244461e-66b5-362d-af94-f7dce28b9d6d | -9.4433 | -60.5499 | 2025-08-30 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 189.6 |
| 77d342dd-3db1-3b20-b55e-8da824130792 | -14.0113 | -44.5849 | 2025-08-30 02:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 180.0 |
| a120be3d-ecb8-31a0-a995-9d0a5c6405ce | -13.3623 | -47.018 | 2025-08-30 02:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 202.3 |
| 9905d9fb-0d4f-3fb0-8d54-d159d0e34852 | -11.3317 | -43.6162 | 2025-08-30 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 0ba4ee55-7a7e-380a-82c0-675c99e38c56 | -9.4435 | -60.5307 | 2025-08-30 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 28e739d8-b160-3cfc-8fd7-6f0fcd2ba7ae | -14.0118 | -44.5614 | 2025-08-30 02:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 143.9 |
| d730fe45-6f8b-369d-9e5a-c66f3dfec0bd | -6.1853 | -43.3257 | 2025-08-30 02:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 4c13e42c-c669-37d9-b141-7dec64db1708 | -8.9126 | -62.1058 | 2025-08-30 02:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 136.8 |
| 18a005a3-a431-3597-bd53-5bf05cbf2e46 | -8.8843 | -60.7315 | 2025-08-30 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 126.9 |
| 5e211674-0719-3a5d-94a5-87a3796a361d | -11.8576 | -46.358 | 2025-08-30 02:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 6a86f7a6-ee0b-32b5-b8db-32beaa68e997 | -9.1156 | -65.7513 | 2025-08-30 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 4dccdc30-c17c-3778-86c1-9deef6d41fa4 | -9.1155 | -65.7699 | 2025-08-30 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 70f14cc9-e462-373e-8e8b-d1dd47d61596 | -13.3817 | -47.015 | 2025-08-30 02:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 203.5 |
| 8a395c57-42dd-3cae-9727-7b3bec027ba0 | -11.8568 | -46.4034 | 2025-08-30 02:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 70f04085-b5d9-3498-8dbf-83dacb7e60fe | -9.0799 | -65.4349 | 2025-08-30 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 8dc3cce6-5f07-3c1d-94a8-79e42afb6779 | -13.9918 | -44.5884 | 2025-08-30 02:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| bb06bef6-bc36-3304-ae32-40e0ea93c83a | -5.6268 | -45.0025 | 2025-08-30 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 4459a735-341e-3819-8ac7-2ba1742d5172 | -14.0118 | -44.5614 | 2025-08-30 02:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 145.6 |
| eaa12f0a-8c56-3b93-a636-8ca5f95cd034 | -11.838 | -46.3834 | 2025-08-30 02:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 144.8 |
| a1fda6a5-35ef-38a3-a92e-439a48c7942c | -9.4435 | -60.5307 | 2025-08-30 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 4457059e-1851-35c0-9b2c-ebae5b05928f | -14.0113 | -44.5849 | 2025-08-30 02:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 320.9 |
| a045aa27-fb90-31d7-8f9c-736457ac1318 | -11.8572 | -46.3807 | 2025-08-30 02:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 258.5 |
| 1ce65f5c-67ed-3c7c-b27b-82bb1130f46d | -11.8764 | -46.378 | 2025-08-30 02:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| a23f0563-52ad-31fd-97be-80cded25c839 | -11.8564 | -46.426 | 2025-08-30 02:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 7714786b-e4f9-3d76-99be-106578fb36c8 | -8.894 | -62.1066 | 2025-08-30 02:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 87.3 |


[Clique aqui para ver as próximas entradas](README8.md)
