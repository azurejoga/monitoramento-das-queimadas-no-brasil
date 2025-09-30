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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0be460b-0142-327a-a0c4-c6595cbe6644 | -8.1914 | -47.0323 | 2025-09-30 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 152.5 |
| de5b97a6-f3b6-3dff-9f9e-bcea47197113 | -7.4131 | -44.4443 | 2025-09-30 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 770a7d9f-37c9-30c2-b076-e68e18f0ee42 | -7.8378 | -46.7544 | 2025-09-30 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 829f9302-0c87-3b45-914f-9d281a137f5f | -17.9411 | -57.5722 | 2025-09-30 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 131.7 |
| 95e1f529-c4b0-3ad5-9ca7-eb03005b2918 | -10.0339 | -50.2211 | 2025-09-30 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 277.0 |
| 9acbc0be-dfa1-39e1-a573-643e593c4a68 | -13.2006 | -47.4251 | 2025-09-30 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 43438ca4-7e92-3301-b1f0-96b8608db261 | -5.8616 | -45.9327 | 2025-09-30 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 174.8 |
| e041f3d9-1af9-37bf-9ebf-f31bc8b44e6e | -9.1248 | -47.6256 | 2025-09-30 14:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 59237981-756f-3111-81a7-f80264a6e340 | -8.8516 | -51.6998 | 2025-09-30 14:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 154.9 |
| f83664a5-ec2d-3d09-8733-f5fab0257a07 | -11.1753 | -47.2358 | 2025-09-30 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| ed283758-817a-3bd1-beed-92466497dff3 | -8.672 | -47.7144 | 2025-09-30 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 86117c37-a0ee-35ce-836c-4c3dc825b87d | -7.8028 | -50.0358 | 2025-09-30 14:40:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 9fe1289e-d283-3a72-aa02-353809476845 | -8.8417 | -46.187 | 2025-09-30 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| ea877312-610a-3819-9c1e-32ae02b6be98 | -9.0497 | -47.6112 | 2025-09-30 14:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 948f6a64-89b8-370c-b8d0-3791e794b090 | -6.098 | -42.6521 | 2025-09-30 14:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 93.9 |
| 77889ff8-54b8-3ca8-b1d4-fe493ed71247 | -7.1193 | -45.5417 | 2025-09-30 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| c0de7015-8ad8-3511-854d-1e00da456b8a | -12.4246 | -50.19 | 2025-09-30 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 49baddb1-9d92-3e42-a5fc-920c244e2ef5 | -15.149 | -52.8479 | 2025-09-30 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 378.2 |
| f42e9857-587d-3b6c-8209-bc165db35544 | -12.2348 | -47.7863 | 2025-09-30 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| cc290946-3a1b-3d34-a49b-22295bc3dc35 | -15.7917 | -43.6672 | 2025-09-30 14:40:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 554.3 |
| 3af7d512-8d52-3c99-b119-10662daf457f | -11.1948 | -47.211 | 2025-09-30 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 228.6 |
| 3b03c023-397b-30fa-b809-361200e3f8f6 | -12.1072 | -44.2021 | 2025-09-30 14:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| e0945605-9e83-3f6e-984c-a1bdbeefd7ae | -12.7022 | -45.2715 | 2025-09-30 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| a3787c33-7a54-3e67-9ce4-363e23098cda | -10.0531 | -50.1978 | 2025-09-30 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 140.5 |
| db4d9dc6-dcce-3de2-9050-1fff4468b12c | -11.1944 | -47.2334 | 2025-09-30 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 134.8 |
| d3893721-c025-3776-ac8a-b1715c15b662 | -14.0412 | -45.001 | 2025-09-30 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 272.2 |
| 8f74168c-783e-3c5d-a99b-01035ee89a98 | -6.3692 | -45.6258 | 2025-09-30 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 6d5f2005-75c5-3e28-b651-d17d40c3b00c | -15.8629 | -59.3379 | 2025-09-30 14:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| bf7c2eaa-37c1-3a3e-9eca-0b1f5438f0fa | -12.8774 | -45.1742 | 2025-09-30 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 886c482d-a814-3702-8f72-5f8a4c47a9ee | -10.7482 | -45.3713 | 2025-09-30 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 5aa9d57a-3ddb-33a4-8900-aa76d3118144 | -18.1782 | -53.3024 | 2025-09-30 14:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 93.2 |
| ca7e4651-c7bb-3f8e-85b5-7b13fa71c83e | -7.8375 | -46.7766 | 2025-09-30 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 190.1 |
| d6e68cf5-3704-30f0-a6e9-346675b7416e | -18.4862 | -44.0191 | 2025-09-30 14:40:00 | GOES-19 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 183.9 |
| d8b791db-dc08-3c50-8247-c3a1aee1ce2b | -6.5042 | -45.2085 | 2025-09-30 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 97d8f837-84e2-38c3-aa35-87472ab17e4d | -10.0342 | -50.1997 | 2025-09-30 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 49661c41-eee5-3317-919c-af7d991ed3dc | -9.4206 | -54.5753 | 2025-09-30 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 242.7 |
| 4b911988-bfa3-3f51-9f32-d43c43700466 | -7.2999 | -42.8486 | 2025-09-30 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.2 |
| 2adf605c-a93b-36e9-aa48-e2cb317701e5 | -5.7601 | -42.6561 | 2025-09-30 14:40:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 92.7 |
| 13a42fc2-10f1-36e6-b50f-8bdabb1e1c34 | -5.9192 | -43.6961 | 2025-09-30 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| c2752393-4626-33a7-a6b3-3d78905b24ed | -7.7271 | -44.941 | 2025-09-30 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 8a1493a4-edd7-33c4-963e-7ed2d78dd5bb | -10.6423 | -48.5802 | 2025-09-30 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| fed764ff-bbc8-3499-b2fb-3093332bb6f7 | -10.1855 | -44.8709 | 2025-09-30 14:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 144.5 |
| cf015460-a4ce-3c1a-9c16-09bf203e6574 | -9.0236 | -46.7052 | 2025-09-30 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 83b941fe-c705-3b1f-9c73-037bacaffe78 | -5.7413 | -42.6576 | 2025-09-30 14:40:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 95.7 |
| 94d1ae7d-e47f-3905-aa55-c4fb7b66b62d | -5.863 | -45.7757 | 2025-09-30 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 80937002-f8d8-328f-9942-7dcda224ec21 | -6.504 | -45.2312 | 2025-09-30 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 132.6 |
| e510b21a-7d53-39fb-b282-28bcde8296bd | -14.7367 | -45.2255 | 2025-09-30 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 427.8 |
| bb3e5774-6e16-3f84-b25c-4a369e6c4571 | -6.0623 | -42.466 | 2025-09-30 14:40:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 94.5 |
| d1b4170a-c912-3bb3-b3db-4c047c6731e5 | -13.2741 | -50.8997 | 2025-09-30 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 218.5 |
| 34416f34-e5c5-3d01-9ac9-c794540e9c15 | -7.0481 | -45.1856 | 2025-09-30 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 7c6e9d18-b1df-348b-9bb7-832897782f4b | -8.9182 | -46.1115 | 2025-09-30 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| f2e7bd09-75ef-318b-b8de-24d2bade9bbf | -18.2176 | -53.3177 | 2025-09-30 14:40:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 382.6 |
| ef1644d7-a16d-3b69-9139-1bfa296baf3e | -10.1045 | -47.7851 | 2025-09-30 14:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 488550dc-3b61-30f1-a9fb-e2252cbef995 | -6.0625 | -42.4422 | 2025-09-30 14:40:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 101.8 |
| d4763160-767f-3c39-88b7-07e221b9ba17 | -12.3867 | -50.1731 | 2025-09-30 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 590.7 |
| 80ff9067-2263-3e92-a928-2128ffe1b062 | -9.9581 | -43.5987 | 2025-09-30 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 208.4 |
| d0b5d340-e3a2-34b7-9b6c-bc36360ca62b | -16.7575 | -51.3482 | 2025-09-30 14:40:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 136.9 |
| e6771f95-75e3-3fb9-a953-0480255d8589 | -8.244 | -45.7754 | 2025-09-30 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| f012c30f-ee8d-33b9-9466-dd41828aee1f | -15.484 | -45.8773 | 2025-09-30 14:40:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 441e7ed2-dea0-331b-a699-5642b33f677a | -12.2344 | -47.8086 | 2025-09-30 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 145.2 |
| d87f7ca5-6719-345a-80ca-2241ff766b52 | -11.7984 | -47.6003 | 2025-09-30 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 81cad2a3-b85e-3c66-8c5b-5cdb080abe60 | -6.5232 | -45.1843 | 2025-09-30 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| c3a5c15a-9191-30ba-b5b7-7cb5835a9c8c | -9.0425 | -46.7032 | 2025-09-30 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 1314c119-5e13-359e-8e20-d1e0dc91d1a8 | -15.1684 | -52.8453 | 2025-09-30 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 318995ec-7080-3789-aca3-33f8bdde1dcc | -8.8734 | -46.6539 | 2025-09-30 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 178f928c-0e67-33fb-a032-9d6d8247f551 | -15.2746 | -49.263 | 2025-09-30 14:40:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 693d0d73-a110-3fe9-b3a1-5fb157b59227 | -3.8887 | -42.4975 | 2025-09-30 14:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 83.7 |
| 23f25b27-4432-31b9-acdd-4808b459b69c | -17.9408 | -57.5928 | 2025-09-30 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.1 |
| bb0d969a-aab7-30e0-a961-3bb33dbce08d | -7.0291 | -45.21 | 2025-09-30 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| cb6f0102-7445-3a0d-8416-54603268639c | -7.9194 | -44.6016 | 2025-09-30 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 0a47bd91-9479-37b5-9410-57f74c564159 | -10.1371 | -48.1553 | 2025-09-30 14:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 78cb6f97-f5b6-348b-acd9-5de51b4cc70c | -6.8148 | -45.9947 | 2025-09-30 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| d2991ab2-92b3-344b-94c2-ef93cf78c831 | -5.4752 | -43.054 | 2025-09-30 14:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 263.1 |
| 89fdbbbc-2272-36f9-8bfc-96cd82167a35 | -9.9585 | -43.5752 | 2025-09-30 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 1da0c322-a861-3e87-b91f-493a8ba3020a | -6.2142 | -44.2041 | 2025-09-30 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| b9a8c62b-54b1-32ed-915f-7871597807e8 | -6.2759 | -43.6442 | 2025-09-30 14:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 90d78217-122a-34e9-b49e-984217ba982d | -10.0717 | -50.2173 | 2025-09-30 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 8df4be4f-166e-3d1c-acfd-b7c3503894be | -14.8468 | -54.7489 | 2025-09-30 14:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 7d0caa8a-fddd-3737-9ad3-754f3de04dc8 | -14.5853 | -45.0197 | 2025-09-30 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 261.6 |
| 0d6fad33-e320-3998-8d48-1d4b06674ce9 | -9.1246 | -47.6476 | 2025-09-30 14:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 7316718a-c1fa-31b4-813f-a9064396e162 | -12.1076 | -44.1785 | 2025-09-30 14:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 221.3 |
| 15f5e44d-ae08-3b74-9daa-d760a2768c9e | -9.5703 | -54.5843 | 2025-09-30 14:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| dbe53bed-127a-35ba-b404-4e3ff616289f | -6.6981 | -42.7882 | 2025-09-30 14:40:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 85.1 |
| 6dfac299-c45b-3bc9-905c-6a2158b3fc70 | -10.8246 | -45.3611 | 2025-09-30 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| e9efa150-a3e2-35ae-a684-37aae166add4 | -15.9071 | -46.2371 | 2025-09-30 14:40:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 96.7 |
| f4863450-8495-3107-ab1e-e5465cff182a | -17.9214 | -57.5746 | 2025-09-30 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 221.9 |
| a6c2c851-ce55-3191-8cc7-b6653eda177a | -12.4055 | -50.1924 | 2025-09-30 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 353.5 |
| d9246be8-c358-3913-8560-4d1594380452 | -7.8188 | -46.7783 | 2025-09-30 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 3355aecf-18f2-30e3-814a-27b0be7d222f | -17.921 | -57.5952 | 2025-09-30 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.3 |
| aeb1b7f3-0d0e-33ef-86e4-d140c819168c | -5.9557 | -45.8588 | 2025-09-30 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| e1e2e30c-9802-3bee-8a6e-e97f96938ed3 | -9.1434 | -47.6457 | 2025-09-30 14:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| f99c2791-9335-3254-b65d-97488aa2d830 | -8.541 | -44.6515 | 2025-09-30 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 246.5 |
| 0951f83e-9f59-37e0-ac44-77b8ea65e2a7 | -14.7166 | -45.2525 | 2025-09-30 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 306.9 |
| 83ca0042-2f89-3cf8-b7f7-a8e83cf6d4b8 | -15.8632 | -59.3179 | 2025-09-30 14:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 691dc1c3-7f87-30de-8620-6e3720a6bb72 | -11.071 | -47.8262 | 2025-09-30 14:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 7845de85-5dde-3b30-b72a-908e44da0361 | -8.2102 | -47.0305 | 2025-09-30 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 80b050af-59e5-30c1-ac40-21efeeabd2e0 | -5.8632 | -45.7532 | 2025-09-30 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 2b62cb8f-846d-3920-ad6a-143b3279a2ac | -6.8454 | -44.8391 | 2025-09-30 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |


