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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eda813c4-5255-371c-ba2a-0055dce35927 | -11.08536 | -45.1307 | 2025-08-30 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1837f86-9247-367a-8f93-ca505b4fc1f5 | -11.07349 | -44.77241 | 2025-08-30 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf2b74d4-fa20-3b63-b3ff-ecc000fb894d | -7.7154 | -50.28 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 782297f7-e9c3-3b19-bdf8-6dde8abb3e28 | -11.65726 | -46.87209 | 2025-08-30 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42e9ae50-696e-38d8-a3e1-a0e79d606a09 | -9.43728 | -62.37189 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7774dc75-d296-3b37-a983-3ee5695b1474 | -7.58874 | -42.70073 | 2025-08-30 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 186dfb1e-6a9d-3e29-ba66-30dac9fdceee | -11.36245 | -43.56718 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 008da3c3-674f-3061-9d3a-24f3aa98179a | -11.31924 | -43.61959 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04da3add-053e-3278-9abb-07d32463004e | -7.1089 | -44.58349 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d899038c-cb0c-3d8f-9aaa-7185032a19ad | -9.44517 | -62.3293 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| da2b2965-68c3-32a1-aca7-f64f290bf455 | -11.82574 | -46.46796 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 3e062141-60d2-33fd-be68-8816f5382dc8 | -10.37757 | -57.83358 | 2025-08-30 04:49:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47102f57-924f-359e-bf5f-e9d860f1f1fa | -7.39338 | -60.59497 | 2025-08-30 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b8984b12-269f-363c-b1eb-fbada921e697 | -9.44971 | -60.5646 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2f0ff1ff-6c98-3ea5-a07c-f806a748014c | -8.70711 | -50.36036 | 2025-08-30 04:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 04b7a7d5-2c81-3bc7-a94a-37760aa35ed2 | -11.2962 | -43.63775 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dadbc121-fe60-3a50-86d5-dbed896ea002 | -10.6467 | -48.65894 | 2025-08-30 04:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad871b3e-bce1-30bc-be23-94d16fe80acf | -8.89687 | -62.09988 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4c6fc280-0c2e-3e88-992e-991aa87d3243 | -6.68286 | -49.7747 | 2025-08-30 04:49:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a020d48-edb7-3aac-be34-a8dd18785926 | -7.72095 | -50.26632 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 35847c77-16d4-3df3-a137-8f27b790d64d | -9.69884 | -47.05444 | 2025-08-30 04:49:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 255ff145-198c-3428-a9f0-68d99fa4881d | -9.44849 | -62.33174 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 897b5d69-fb43-332f-8614-c30f9f5ee858 | -9.45613 | -60.55922 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 698ce6ba-a909-3c64-b971-e0acbc8b2da5 | -11.06941 | -52.03593 | 2025-08-30 04:49:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 433e9d52-a8e7-39ae-9fad-3ae508bb8692 | -6.86626 | -44.44569 | 2025-08-30 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e64cc9c0-e070-326e-83c8-329a28205ec7 | -9.13799 | -65.8243 | 2025-08-30 04:49:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 885faaf0-689f-3a00-a4ce-80757b0e36fa | -9.45431 | -60.56896 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 64ecf3e2-36e2-309a-a9c9-364417c3df39 | -11.84777 | -46.43211 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b49a65f3-702f-307a-90c0-5b0608ac52b2 | -10.99664 | -46.95216 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 21801a12-074e-33f6-a520-1d15e631f3ab | -10.16486 | -48.47059 | 2025-08-30 04:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0da5fcd4-1256-3664-9b7f-21958febf3ab | -9.53467 | -45.84925 | 2025-08-30 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6db40b87-ae8d-3674-ac8f-fa0c4e5dab72 | -11.82945 | -46.47239 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 4484d5a3-3737-3956-959f-84a03abd8774 | -10.38328 | -57.82635 | 2025-08-30 04:49:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8aa4775-4871-3272-a470-84fc08b377af | -10.34858 | -59.18345 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a156916e-1feb-3545-90ae-ec95ff327ac1 | -11.3521 | -43.58476 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bfdb415-3b0b-3f3f-aa6a-28357904a74b | -11.30509 | -43.5688 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31ab4b03-800f-3f34-b8b1-c992374aad54 | -7.39945 | -60.59243 | 2025-08-30 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a769625b-f41c-3c74-a483-651f66640189 | -9.22074 | -60.8731 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f98642f-cdcc-3338-a369-fa3c69483228 | -9.64186 | -48.30859 | 2025-08-30 04:49:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5755a50b-e43a-31c3-b53c-a2a69bb7723e | -10.88006 | -45.13531 | 2025-08-30 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 788c2911-052f-32d7-92ce-2b91fb27034e | -8.11584 | -45.01259 | 2025-08-30 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2fe3b417-6fef-3119-9353-701c8f25e25e | -6.00957 | -57.85538 | 2025-08-30 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c205c320-db6d-3b1d-8e3e-7abaa3a4d4a6 | -11.93731 | -46.69132 | 2025-08-30 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4456a36d-54e4-3ed9-9f4d-f3c75294c37a | -8.56086 | -63.01163 | 2025-08-30 04:49:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c526549-c233-3644-8ef5-c6a0dabb1c65 | -9.8197 | -63.85892 | 2025-08-30 04:49:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b263f2ad-54b0-3999-86fe-fa13f25bef6e | -7.15104 | -44.90973 | 2025-08-30 04:49:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4707dc5f-6c5d-3e56-90f4-c3a02cba2dea | -11.31609 | -43.64376 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d568b99-1929-3973-8d23-5c0456d7ead6 | -9.44122 | -62.35062 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3e29d78b-700d-3b03-bf7c-a2be0275908a | -7.39864 | -60.59299 | 2025-08-30 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7a7461af-3443-38a4-b597-0704a0e574fc | -11.87216 | -46.37933 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 840af6f5-139e-318f-972c-9a6f7d1fe1b2 | -7.71821 | -50.28402 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 62b8f34a-60ff-33c3-87b6-b730958a1db1 | -9.45592 | -62.32468 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 19.9 |
| f6a3f6a3-ea9f-3665-914f-c804fd01d07d | -11.85681 | -46.39694 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e82f4ece-279e-374a-8e30-ce9248c724d7 | -7.16664 | -44.14758 | 2025-08-30 04:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f5e7197-d256-3c60-b835-3b57f13ae4d1 | -9.44287 | -60.54343 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 30c8e14b-045c-352b-bb41-991e455b71d6 | -11.74707 | -49.0878 | 2025-08-30 04:49:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f51f49da-85eb-30cf-9f3c-6c7a6d44d0b8 | -10.36265 | -59.21266 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b32ea139-ef03-3bf0-aad0-d6f1dbb814ac | -8.34259 | -62.93306 | 2025-08-30 04:49:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa931062-76d3-3154-b1b3-fb3f65b62dd9 | -11.30946 | -43.65498 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52f4a7e9-12d2-382f-9d24-398ba5a94782 | -11.30478 | -43.6114 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51980c1f-c401-3517-a521-ccfd7e6e5c53 | -10.0241 | -48.08685 | 2025-08-30 04:49:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 608ad180-da03-332f-b668-2871b559df6c | -11.07051 | -52.05054 | 2025-08-30 04:49:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed310323-6ec1-3c24-a142-c4e7e68fe749 | -8.18918 | -61.37953 | 2025-08-30 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6dde451-74d9-34f8-8121-79f3070591e3 | -8.50617 | -54.71658 | 2025-08-30 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef0df53b-f162-3122-a39d-7e661d3290e4 | -11.88291 | -46.42743 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 347efd6f-5466-3253-ab62-e0675af8134b | -11.07107 | -52.04702 | 2025-08-30 04:49:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e949c02b-7242-392e-8b10-d825d05fa5e2 | -11.83434 | -46.44185 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ad9597a3-179b-3fd2-8012-4b7407292d5b | -10.37476 | -59.1995 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad8c1b25-90a6-326e-8cb8-b3547be672aa | -7.40659 | -44.29626 | 2025-08-30 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f24e7ade-d1d0-3a8d-acb1-55aec9bc0e6c | -9.69067 | -48.30781 | 2025-08-30 04:49:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3f4941f4-e8c5-3bed-b0a5-05a817b9fc11 | -7.75905 | -50.30827 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f5391ba-7f29-3ab1-854e-0b472100b763 | -7.77864 | -45.4752 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b26eefc6-5535-3c53-adc6-7b697afb21c7 | -9.48966 | -45.41027 | 2025-08-30 04:49:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b3a2abe-178f-3cf1-a6cb-d36530f0fbb3 | -7.60154 | -42.72151 | 2025-08-30 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ba873292-3d3b-3092-a918-766c39a7ebd3 | -11.32623 | -43.64522 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ff04968f-9b86-3ded-9ca8-1c930f8600d2 | -11.58303 | -46.36472 | 2025-08-30 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0daba802-cced-3d86-9d54-b6cc1d341989 | -9.44535 | -60.5601 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| be25f699-80f5-3931-82d6-f4401de1d032 | -11.30013 | -43.64729 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdb374e5-82b4-3f15-abec-c1c7912a972a | -9.58062 | -54.4738 | 2025-08-30 04:49:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 66599815-d9b8-3c09-beb4-1b04063a3864 | -10.36449 | -59.20256 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62e6b8fe-fb79-339f-b2ab-dd6365429dc3 | -7.16333 | -44.13771 | 2025-08-30 04:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e2a20f8-e3db-3d0f-8849-cbf97abf9c39 | -11.29919 | -43.57436 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70f8cebf-fc08-33aa-81bd-56cba710952d | -11.31685 | -43.63792 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6984d348-37e9-3bb8-b728-bb373103fc61 | -11.87116 | -46.38676 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 034e1370-a6b6-352c-ba74-e35d7302ab31 | -11.84504 | -46.38805 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f46b23fb-a150-3cad-98c9-a275bdf395ea | -11.72869 | -51.75527 | 2025-08-30 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f646fc2-40f3-377d-b39e-f75222253962 | -9.8059 | -61.19953 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6856cde2-0c25-355c-be1f-0ac9873ad753 | -9.43603 | -60.55187 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a063b252-6905-3910-9b62-0329f5507c6e | -11.32 | -43.65334 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a72df54-b427-3372-81aa-830eca104100 | -11.83783 | -46.44193 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| d82d7b97-b359-36f1-9e28-ffeb2ef4868f | -8.55899 | -63.02134 | 2025-08-30 04:49:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 73eec314-ebf7-395b-b5d6-83121d0f73f7 | -9.58352 | -54.47836 | 2025-08-30 04:49:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c182ad7-d9f3-3744-8e98-6c8401fce869 | -8.70319 | -50.36343 | 2025-08-30 04:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03193e90-9fd3-3c11-bf93-043835a7f0b4 | -11.86259 | -46.3862 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2e5978e9-c4b7-3596-b445-3044d5ba2214 | -11.30549 | -43.5657 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 007277a4-fd51-3ccc-aade-45794422a614 | -9.45435 | -62.33284 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 0ac4f346-df31-35ee-8f71-dfb54903c239 | -9.43694 | -62.34092 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b32b9ec0-ffca-3a25-9077-90fe94728aee | -9.41568 | -60.57463 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 727f6ca4-ba84-328c-af87-199f9aca82eb | -9.43965 | -62.35909 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2953013b-29a0-389e-83fc-f4b06ca8b3fa | -11.0808 | -45.12997 | 2025-08-30 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README47.md)
