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
| 7abfa376-2f8b-30d5-9d19-889d540105cc | -10.9515 | -50.8296 | 2025-08-31 00:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 85b407c0-3bc2-3c2b-97f2-c1b64aa47772 | -18.1452 | -50.2549 | 2025-08-31 00:00:00 | GOES-19 | CASTELÂNDIA | GOIÁS | Brasil | 5205059 | 52 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 5833c474-2877-35f7-a1f0-ffb3b3c27c1b | -7.9265 | -63.0158 | 2025-08-31 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| f63326e6-2967-3da3-b648-cc200a3cb04b | -11.2919 | -63.2509 | 2025-08-31 00:00:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 61.6 |
| af83ba00-7a15-33f3-b49d-c20d0d02f74e | -16.2221 | -52.6778 | 2025-08-31 00:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 516.9 |
| 90c0de47-0a03-32b6-8210-4c578c0f3465 | -18.1457 | -50.2326 | 2025-08-31 00:00:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 162.8 |
| 9d79bfd8-4c38-3ab3-8cf4-e76a22d72ca5 | -9.0614 | -65.4355 | 2025-08-31 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.5 |
| fd39fa6e-2d33-3a57-b514-adcd29444f08 | -7.0951 | -44.3128 | 2025-08-31 00:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 296.7 |
| f1241999-b9b9-34c9-8166-2a010939dfde | -11.3112 | -43.69 | 2025-08-31 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 165.1 |
| 450086e5-7d11-3493-8397-b3e7e4404695 | -4.1604 | -46.7881 | 2025-08-31 00:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 8cc07698-949d-3af2-938d-f113b7c329b1 | -6.1665 | -43.3273 | 2025-08-31 00:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| f14412b6-5542-33c9-bd09-dcb805694a51 | -7.908 | -63.0164 | 2025-08-31 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 922c0472-6cdb-33e9-98dd-ee0fa6b713a0 | -8.6697 | -62.42 | 2025-08-31 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 3cefa604-79a2-3f90-916c-d2a1cc2f4926 | -13.4986 | -46.9517 | 2025-08-31 00:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 7bb8f8a8-3917-39eb-bf10-257fa1295d6f | -7.0953 | -44.2898 | 2025-08-31 00:00:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 3c5d6d5c-859a-348e-8e72-37f1a3f16178 | -16.2217 | -52.6992 | 2025-08-31 00:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 0ff26184-1370-3fa3-a21d-5a95e7798678 | -11.3304 | -43.6871 | 2025-08-31 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 214.8 |
| 8a15fc2a-5899-38b8-9e53-7541c01bc71f | -7.1136 | -44.3341 | 2025-08-31 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 70eba0c2-d509-377a-b898-ba4e3ae6ad14 | -16.2025 | -52.6807 | 2025-08-31 00:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 1cb5c3f0-46eb-358b-9824-74cb1fd0da50 | -3.8146 | -48.9515 | 2025-08-31 00:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 8c5e737f-1219-3f1c-bcb0-0397fd55dab4 | -11.33 | -43.7108 | 2025-08-31 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 44.7 |
| fda2c47c-7170-3000-b451-be33efce7a29 | -9.7498 | -65.0938 | 2025-08-31 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.4 |
| a568d5f2-868d-3365-a758-b532c977e1f7 | -10.3127 | -59.1827 | 2025-08-31 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 74eddc57-8932-3967-bda3-6ef751886334 | -11.3308 | -43.6635 | 2025-08-31 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| bbb48d6d-b532-3fc9-a308-01035abf054f | -9.2745 | -67.6433 | 2025-08-31 00:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 9ebfc7a6-4d18-398e-bf45-ec14373a6039 | -12.0976 | -44.717 | 2025-08-31 00:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| ec3fe5b7-c0ef-3431-ac81-eafbf8dc5f9b | -7.1139 | -44.3111 | 2025-08-31 00:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 236.9 |
| b827fde3-1d79-370e-969b-01a0193d1cc6 | -9.1337 | -65.844 | 2025-08-31 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 4fea8fc0-e996-391f-b23b-ca2599b1315a | -8.5552 | -63.0114 | 2025-08-31 00:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 52990f72-cf2b-3b22-8d15-87ef036de652 | -11.3116 | -43.6664 | 2025-08-31 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 03afed0d-85dd-32cc-a5dc-9f50173c085b | -6.1853 | -43.3257 | 2025-08-31 00:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| c2524068-57c4-397b-84fc-892a925c0959 | -8.6673 | -62.8369 | 2025-08-31 00:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 6a59df3a-f1a1-3aed-9ca1-a8895c871c31 | -7.0948 | -44.3358 | 2025-08-31 00:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 19d495ca-9a86-36ba-a56e-cfc591fe3ac5 | -9.0615 | -65.4169 | 2025-08-31 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| f94924f1-9d13-392b-bafb-9ae380c434f6 | -8.6487 | -62.8376 | 2025-08-31 00:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 4e32738b-29ce-38bc-9d08-38f0439a26f0 | -9.0799 | -65.4536 | 2025-08-31 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| f93fcad4-b69e-39ac-9677-31b4b8d602cc | -9.1337 | -65.8253 | 2025-08-31 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 146023de-2740-3ada-b66e-58e3f57d2a80 | -8.6488 | -62.8187 | 2025-08-31 00:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 0e1fc8b9-de03-3a94-aac8-28cc010f732c | -7.1141 | -44.288 | 2025-08-31 00:00:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 75976eb0-5328-3dc0-86ba-ed77dcde9137 | -10.3313 | -59.2011 | 2025-08-31 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 106.8 |
| d84b46fd-0440-37e6-907b-fbd70655e6cf | -10.3314 | -59.1816 | 2025-08-31 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 9d1f57af-c3ba-3abf-af5d-e77f3900cc32 | -11.2921 | -63.2319 | 2025-08-31 00:00:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 71.3 |
| f22b8664-9660-396b-a80a-5b4dafb2815a | -9.0799 | -65.4349 | 2025-08-31 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 927a150a-f979-3586-959a-59d24e285e83 | -16.2225 | -52.6565 | 2025-08-31 00:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 19fa434a-e026-3154-b0e5-e736d6851187 | -16.2417 | -52.675 | 2025-08-31 00:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 20a247e3-0b25-315f-92e8-1697e5acd039 | -10.3126 | -59.2023 | 2025-08-31 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 134.0 |
| 52294ea7-eb16-3a49-bc91-60bf5e864a88 | -8.6882 | -62.4192 | 2025-08-31 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 2389d06f-a30a-382a-8f8a-689d555a780b | -8.6849 | -66.9355 | 2025-08-31 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 12135042-0942-3198-9db4-2fd5cf257b42 | -9.0613 | -65.4542 | 2025-08-31 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 122802fa-83b7-3883-b119-77b95e26d255 | -10.3124 | -59.2218 | 2025-08-31 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| d4410e40-c606-362a-893e-496fbd62059b | -9.2745 | -67.6433 | 2025-08-31 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 8c39b930-cf8f-36af-bca2-dc8cf47018df | -7.9265 | -63.0158 | 2025-08-31 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 0e9ca99a-022d-35ad-b3e3-f77059790df9 | -3.8146 | -48.9515 | 2025-08-31 00:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 2656781c-54ad-3f78-a2db-944039e6b36f | -7.1139 | -44.3111 | 2025-08-31 00:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 255.0 |
| fd729f71-a2de-31c6-853d-4f6d2a1b8a3e | -7.0948 | -44.3358 | 2025-08-31 00:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| b117b3f9-abd1-3e46-ab02-022ddca0e9d0 | -11.8373 | -46.4287 | 2025-08-31 00:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 3976b10c-33f0-3a0e-9d8d-926d25d31da4 | -9.0613 | -65.4542 | 2025-08-31 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 576ee092-207d-3c0b-be74-eb2bdc20be02 | -11.3509 | -43.6133 | 2025-08-31 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 156.3 |
| f2c060fe-80b9-3c57-a381-7290d9587957 | -9.0799 | -65.4349 | 2025-08-31 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 848c19d5-1e5c-37e4-acb7-70e84d6d422c | -10.3126 | -59.2023 | 2025-08-31 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |
| a66d1200-7dfb-3fd1-880e-aab3315e8dc3 | -10.3314 | -59.1816 | 2025-08-31 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 058a1c0d-4d9c-3e90-9e79-49abea4bb1e1 | -8.8939 | -45.094 | 2025-08-31 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 18947778-e748-3525-8918-5bb919c8aa29 | -11.3312 | -43.6399 | 2025-08-31 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 1a3de897-cfe9-3c76-8bbe-216f2ba220b4 | -8.875 | -45.0961 | 2025-08-31 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| aae4408e-81b0-3d74-a722-8054cb276158 | -11.3308 | -43.6635 | 2025-08-31 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.0 |
| e16ad136-b8c5-307f-8874-0373e98f74dc | -7.0951 | -44.3128 | 2025-08-31 00:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 320.3 |
| 5e454694-677d-3053-8793-a1d84e24708f | -11.3116 | -43.6664 | 2025-08-31 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 678ac4b6-fc63-348a-b5c2-98388db15c7c | -9.0615 | -65.4169 | 2025-08-31 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 8956a22d-ee05-3dfd-9569-64b65da0f457 | -10.9515 | -50.8296 | 2025-08-31 00:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| e0671466-54f1-334f-9400-d02079e2cd12 | -12.0976 | -44.717 | 2025-08-31 00:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 81aeeba6-de48-33dc-82cc-3170d52364a2 | -7.908 | -63.0164 | 2025-08-31 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| f701f81b-5d07-3bca-b510-e7876c6410b3 | -11.3112 | -43.69 | 2025-08-31 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.0 |
| a0fec59e-4a6e-3348-a9fa-6eeceb729b97 | -11.3304 | -43.6871 | 2025-08-31 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 168.7 |
| ca7d2aad-bc0e-3575-a962-529d634888a6 | -6.1665 | -43.3273 | 2025-08-31 00:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 6038e0f1-a5e5-3bbf-a451-5be7e057e111 | -11.3696 | -43.6341 | 2025-08-31 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 4d6f848d-f546-377f-8c5e-130787287822 | -4.1604 | -46.7881 | 2025-08-31 00:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 2529abee-929e-3ca1-b4c2-0119e18a671a | -10.4874 | -51.6374 | 2025-08-31 00:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 60280aaa-850e-3905-adff-994eb849912b | -9.1337 | -65.8253 | 2025-08-31 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 716fc60e-5a85-38c6-9a3b-ebcd706d030f | -11.3701 | -43.6104 | 2025-08-31 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 1a949cb7-7758-3398-b023-4c4659ce3afc | -10.3127 | -59.1827 | 2025-08-31 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| cfe0f16f-bf8e-3d0d-af4d-f929a7336a6d | -12.9192 | -56.9873 | 2025-08-31 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| d81e045e-fad5-3414-8c99-71d73d99a2eb | -9.0799 | -65.4536 | 2025-08-31 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 8d384242-b7b5-3d44-a91f-74470d1c64d1 | -11.2921 | -63.2319 | 2025-08-31 00:10:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 75d5e5ff-3b89-3123-91a2-65f23dd2444d | -11.3504 | -43.637 | 2025-08-31 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.7 |
| d66dca42-c669-3d0c-8e2a-af16a1deae17 | -9.0614 | -65.4355 | 2025-08-31 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 593b94b9-8061-3a46-9d76-b79f9d4050b9 | -10.3313 | -59.2011 | 2025-08-31 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| edc914b7-74c4-30f5-99e7-dfab9bd24510 | -7.1136 | -44.3341 | 2025-08-31 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 41337875-feeb-3fe1-876d-c79512c6f71d | -8.5552 | -63.0114 | 2025-08-31 00:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 297a4abe-407b-39d7-a565-c8dfbcd5fa6e | -11.2924 | -43.6693 | 2025-08-31 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 6ed9f4b2-5015-3986-b8ab-d960cc330b00 | -9.2745 | -67.6618 | 2025-08-31 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 4a3fc05e-f7e7-31fd-bc19-2e72840e5d30 | -11.3701 | -43.6104 | 2025-08-31 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 26102805-f023-3432-8de5-ee1510e5f302 | -12.9194 | -56.9672 | 2025-08-31 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 08bc4605-c5ae-3da6-a2c8-c07b8b5356a3 | -9.0613 | -65.4542 | 2025-08-31 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| bf9ee39e-9423-3fa3-9b9b-ed348cd493a4 | -12.0976 | -44.717 | 2025-08-31 00:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 84d9962b-0a8b-3d8b-814e-2ed4f2450437 | -13.4986 | -46.9517 | 2025-08-31 00:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| a6c7f734-da5b-34b9-96d1-2656e43b5c70 | -9.0799 | -65.4536 | 2025-08-31 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 0e9c24d7-8957-35c8-aa06-b1e026bc7de2 | -10.1359 | -58.0183 | 2025-08-31 00:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 7b5138b9-ba72-35ef-9cc2-3a9085150706 | -11.3509 | -43.6133 | 2025-08-31 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 8a685681-4052-35a9-a4f7-69b2905798ad | -7.0948 | -44.3358 | 2025-08-31 00:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 8c843585-8753-3d1a-a090-329204795a94 | -12.9192 | -56.9873 | 2025-08-31 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |


[Clique aqui para ver as próximas entradas](README2.md)
