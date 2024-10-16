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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d6b7940-1877-3ebb-b6d3-e29f8e9ed81c | -3.1227 | -54.276001 | 2024-10-16 00:43:10 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc1a9ba7-8f32-314a-8fec-fedd1f9c6fc5 | -1.4908 | -47.320202 | 2024-10-16 00:43:11 | METOP-B | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7890b88c-755c-321a-863d-fa68a6b39b28 | -1.4811 | -47.322399 | 2024-10-16 00:43:11 | METOP-B | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ed0f6f7-3505-33cb-a686-265c78858b7c | -1.4369 | -47.3992 | 2024-10-16 00:43:12 | METOP-B | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc16c381-d4af-31aa-8320-543231051b7e | -1.4271 | -47.401402 | 2024-10-16 00:43:13 | METOP-B | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ae5f637-c192-37b5-ae4f-b1c0ab94f140 | -2.8718 | -54.165001 | 2024-10-16 00:43:14 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a679ded8-0c2d-33e8-9c3e-a44c1fd9adf0 | -2.8737 | -54.173302 | 2024-10-16 00:43:14 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 216fa5bd-ba84-306d-ab7e-cf68fddd9dfe | -2.8627 | -54.492802 | 2024-10-16 00:43:15 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35610d85-49cf-3cc8-8d27-f36e55d89f19 | -2.8646 | -54.5014 | 2024-10-16 00:43:15 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7147c039-6791-3401-8759-3c392508fdac | -2.9326 | -54.807098 | 2024-10-16 00:43:15 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ad7fa06-2a42-3bb5-bf91-93de8900103c | -2.5679 | -54.001099 | 2024-10-16 00:43:18 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17b011f1-9f55-3e08-b481-0990d948c434 | -2.2002 | -53.644798 | 2024-10-16 00:43:23 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31fa4bf7-be93-392f-9bb5-52b43b5f9651 | -2.2019 | -53.6525 | 2024-10-16 00:43:23 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43353e13-0050-342d-a36b-86b6afc20363 | -2.3395 | -54.3596 | 2024-10-16 00:43:23 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5b51a5a-bfd0-3193-bacd-9875708419d8 | -2.3414 | -54.367901 | 2024-10-16 00:43:23 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 677b2aed-6870-3d7b-b9be-85e15d794dbb | -2.0932 | -53.397301 | 2024-10-16 00:43:24 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd154d5b-acb8-3822-aa4f-bcefcaa27fc7 | -0.8609 | -48.713799 | 2024-10-16 00:43:27 | METOP-B | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e83040c-4a37-332f-9c51-131993604265 | -1.7116 | -52.523602 | 2024-10-16 00:43:27 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9efb592d-fbd5-3578-8ae2-fee83738a744 | -0.7735 | -48.691799 | 2024-10-16 00:43:28 | METOP-B | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 603c1b4b-88e6-3034-b693-d82c0e733da7 | -0.7601 | -48.6782 | 2024-10-16 00:43:28 | METOP-B | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe45c7aa-7bf6-386b-b9d5-1fbd0ee944d2 | -0.7619 | -48.6861 | 2024-10-16 00:43:28 | METOP-B | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0ab9e25-b52a-3daf-a985-03e02d931603 | -1.7292 | -54.159801 | 2024-10-16 00:43:32 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 037b0e82-958d-3ca7-8923-a045c402dab5 | -1.1195 | -53.6908 | 2024-10-16 00:43:41 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8366d63-3f25-3e08-85e6-0eb90aa2bd68 | -1.1212 | -53.698299 | 2024-10-16 00:43:41 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12e1252c-808d-35b3-b645-b2e16b3fc14d | -1.1114 | -53.700401 | 2024-10-16 00:43:41 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72828e7f-beb2-3ba5-bd33-7c28c107f3c2 | -0.6079 | -52.380001 | 2024-10-16 00:43:44 | METOP-B | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 2635a743-3e02-3281-8767-153ef6fd3445 | 1.1027 | -50.9632 | 2024-10-16 00:44:07 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| fbefe9ac-bf29-31d4-adc3-c91194476e88 | 1.1141 | -50.958401 | 2024-10-16 00:44:07 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 529747c6-04f7-32e6-9b34-ccef5298a519 | 1.1223 | -50.967499 | 2024-10-16 00:44:07 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 401ebb08-41c8-3235-9014-6959bff2da89 | 1.008 | -52.205101 | 2024-10-16 00:44:10 | METOP-B | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a683fb11-778c-386c-8cc9-6b3c63cf867a | 1.0065 | -52.211899 | 2024-10-16 00:44:10 | METOP-B | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 6aca0deb-008f-322a-b1e3-ae7bc5519b29 | 1.005 | -52.2187 | 2024-10-16 00:44:10 | METOP-B | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 48553cdd-a247-330b-b6e3-869b0ca596e0 | 1.0016 | -52.2164 | 2024-10-16 00:45:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 57.8 |
| b85084ad-c775-3d7d-81a3-85edd52d7cc8 | -3.1099 | -54.2263 | 2024-10-16 00:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 161.8 |
| e82df5e5-41c1-3331-944f-e6cdbe38913b | -3.1098 | -54.2464 | 2024-10-16 00:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 666403c1-ed19-332c-b65e-c555d7faca5e | -3.11 | -54.2063 | 2024-10-16 00:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 3f575580-97bd-3ec8-a769-f3fd0f434bbe | -3.1282 | -54.2459 | 2024-10-16 00:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 5210760a-b9b5-32c3-97e8-fc68e856146e | -3.1283 | -54.2259 | 2024-10-16 00:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 149.4 |
| 1841d6f9-4746-3346-9c0a-e729b4c1a4fa | -3.2225 | -48.9306 | 2024-10-16 00:45:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| aa2649b0-8196-3569-83d4-2e1b0fb92ee0 | -3.2226 | -48.9092 | 2024-10-16 00:45:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| e8b2e3e4-ede2-37cd-9fe7-ece8452969f9 | -3.2879 | -50.9529 | 2024-10-16 00:45:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 68e7380e-0bc2-32fc-bdce-e585b15aedab | -3.288 | -50.9321 | 2024-10-16 00:45:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 97c10daf-64e0-3a96-90c7-f7df1c23eda2 | -3.4104 | -44.5599 | 2024-10-16 00:45:25 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 31a2d1ba-f33d-3070-86fc-cca8aab3fb10 | -3.5107 | -43.2429 | 2024-10-16 00:45:26 | GOES-16 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 110.0 |
| c1183bb1-605f-3ab9-a370-1f6e8c99d608 | -3.5041 | -52.1659 | 2024-10-16 00:45:26 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| cb6794e6-3162-3601-bdb7-20466bed51c9 | -3.958 | -46.4442 | 2024-10-16 00:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 5d485002-1023-3150-9113-46d411c14445 | -3.9581 | -46.422 | 2024-10-16 00:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 5ea1767d-3c9d-3394-b45a-df834ddd6c9a | -5.5178 | -46.9109 | 2024-10-16 00:45:37 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 148.3 |
| c931bdf4-c660-3d27-9e17-e2ed83ecafdc | -5.5179 | -46.8889 | 2024-10-16 00:45:37 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 02feaf78-3e90-3b9c-a4c9-aa298b383272 | -9.1727 | -65.4132 | 2024-10-16 00:45:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| f75a216f-c315-3d1f-8779-e553054ac0d0 | -9.1728 | -65.3945 | 2024-10-16 00:45:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 143.8 |
| c046c6dc-82b1-3f6e-a5c0-dfb50ca8a701 | -9.1729 | -65.3758 | 2024-10-16 00:45:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 250c5b89-57a3-3bb1-9ff0-7828339f6df6 | -9.9588 | -47.3816 | 2024-10-16 00:46:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| ed72332f-e117-3da4-ab1b-b9c9fa12b41d | -10.8224 | -49.2343 | 2024-10-16 00:46:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 6ef48fc8-43fd-32f6-bd6f-1f3873f62e7f | -11.6915 | -65.2432 | 2024-10-16 00:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| cbf10cec-e019-3553-bd4e-aed4d7154d4e | -11.6917 | -65.2243 | 2024-10-16 00:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 7d3efba5-70e3-3bfd-89a8-24e42f5e9b28 | -11.6918 | -65.2054 | 2024-10-16 00:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 0f453d1f-16e4-304a-b046-3e671fb53dd8 | -11.7103 | -65.2424 | 2024-10-16 00:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 7610bf45-6bd5-31ff-b1de-153856e818cb | -11.7104 | -65.2235 | 2024-10-16 00:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 797b63fb-c7a1-33f4-80b9-417aafe13ec6 | -12.0427 | -46.7161 | 2024-10-16 00:46:14 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 84bdeab3-30f0-3d36-b359-b7ba0d3d560c | -12.0431 | -46.6935 | 2024-10-16 00:46:14 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 114.5 |
| e3f4b1a7-fcc7-3b8a-a5fa-62cd96d50a72 | -12.0619 | -46.7134 | 2024-10-16 00:46:14 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| acbfeef5-4045-30f2-b02b-0b422bf02b4e | -12.0623 | -46.6908 | 2024-10-16 00:46:14 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 21549822-184c-3e40-b4e8-951c7d5f2d92 | -11.9381 | -64.8729 | 2024-10-16 00:46:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 6255f89b-a453-3c84-ba3b-65275e2a9d4a | -12.004 | -63.5199 | 2024-10-16 00:46:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 1b340c0b-9617-371b-bfed-12302c25a8b9 | -12.3795 | -63.7103 | 2024-10-16 00:46:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 061f32d4-20f8-3ba0-8324-66e494fe3fde | -12.3982 | -63.7284 | 2024-10-16 00:46:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 407afffc-6d5a-3597-9a3b-c0db5ed8e2da | -12.3983 | -63.7093 | 2024-10-16 00:46:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 135.3 |
| cf2f230e-2c8b-3d72-b332-0b0924298982 | -12.5149 | -63.2822 | 2024-10-16 00:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 148.4 |
| ee693c16-d9fb-3f46-8164-c78d7821dfba | -12.515 | -63.263 | 2024-10-16 00:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 109.6 |
| bdcfe3c1-6ef2-358c-a4f0-90b3015eb7b8 | -12.5338 | -63.2812 | 2024-10-16 00:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 168.7 |
| d7e7d322-8fd1-3e2a-bf32-81c3e968ef86 | -12.5339 | -63.262 | 2024-10-16 00:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 2c827731-6b0c-36e4-94ff-eb0a8493c728 | -12.9728 | -62.7951 | 2024-10-16 00:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 89840158-1f49-3879-a2f4-2900cf719b24 | -13.0325 | -62.4638 | 2024-10-16 00:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 51.5 |
| aeaf5cc4-169d-3635-a56c-b28722996f41 | -13.383 | -46.947 | 2024-10-16 00:46:21 | GOES-16 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 12c72d7d-7185-393e-9195-d29c2f7ecc75 | -13.3834 | -46.9244 | 2024-10-16 00:46:21 | GOES-16 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 097ab62f-a5d3-3382-a680-013c35eb52c6 | -13.4023 | -46.944 | 2024-10-16 00:46:21 | GOES-16 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 1da83644-ac98-3449-a5be-aff2afae31fa | -17.2439 | -42.6575 | 2024-10-16 00:46:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 98.6 |
| f99d0efb-4c50-382c-862a-55698fd07599 | -17.2639 | -42.6527 | 2024-10-16 00:46:41 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 143.1 |
| e424126d-e318-37e3-ac46-53f70fd3ede6 | -16.9707 | -56.8264 | 2024-10-16 00:46:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.6 |
| 515d80eb-0557-3f56-a569-bf8b043ebfc5 | -16.9711 | -56.8058 | 2024-10-16 00:46:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.3 |
| 0840cc80-32f0-3a83-8e68-5acd61fced05 | -17.0066 | -58.2934 | 2024-10-16 00:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 196.6 |
| 3842fa33-55fb-31d9-9f7f-3be7072878f4 | -17.0262 | -58.2912 | 2024-10-16 00:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 184.0 |
| 9d3b8312-49e5-3037-a067-3d9b5c6284c7 | -17.0682 | -56.8558 | 2024-10-16 00:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.7 |
| 241c4151-1645-3e1e-bb68-dc838803b97d | -17.553 | -42.3096 | 2024-10-16 00:46:43 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 78.6 |
| b2adc17b-8ae4-3ec5-a873-6e1d6a49f60d | -17.1754 | -57.4995 | 2024-10-16 00:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.0 |
| ed79de9a-c7ce-385f-8550-b8c8e8f94569 | -17.1758 | -57.479 | 2024-10-16 00:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.6 |
| de7435e2-45ab-3bf4-98b4-51651bdb3293 | -17.1951 | -57.4972 | 2024-10-16 00:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 143.9 |
| 4cc37e06-c474-38c1-b407-22b018e9ca14 | -17.1954 | -57.4767 | 2024-10-16 00:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 124.6 |
| 4805c757-e343-3305-b29d-f04c2c883706 | -17.2157 | -57.4334 | 2024-10-16 00:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.4 |
| bd0281b2-ee88-354a-9dd6-c0785fae05ea | -17.2177 | -57.3102 | 2024-10-16 00:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.6 |
| 43ac1c1f-0e03-336e-9729-f9162a47dafc | -18.2544 | -56.5821 | 2024-10-16 00:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 247.1 |
| e93653db-f1d6-3b8e-82f0-8458e97b2af2 | -18.2548 | -56.5613 | 2024-10-16 00:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.4 |
| 54d5f43a-5167-350b-8da3-87b281b3c3c2 | -18.2742 | -56.5795 | 2024-10-16 00:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 240.3 |
| e5c60c59-c64d-3cfe-80ab-6c78adcdb155 | -18.2746 | -56.5587 | 2024-10-16 00:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.1 |
| 92cb0b20-724b-335a-baca-d9472e94d561 | -20.8536 | -49.8742 | 2024-10-16 00:47:01 | GOES-16 | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.6 |
| 30769f25-937f-3eda-ba5c-ab5799aead63 | -21.1448 | -47.521 | 2024-10-16 00:47:02 | GOES-16 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 6d9eed9a-305e-3b9d-a3c6-abb42187ebaa | -21.1455 | -47.4973 | 2024-10-16 00:47:02 | GOES-16 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 165ca988-6586-39f4-8caa-d6482df028ea | -21.1655 | -47.516 | 2024-10-16 00:47:02 | GOES-16 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 47362c45-4aa8-3cfe-bfed-2a4a34595049 | -21.1662 | -47.4923 | 2024-10-16 00:47:02 | GOES-16 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 95.3 |


[Clique aqui para ver as próximas entradas](README10.md)
