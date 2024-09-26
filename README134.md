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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e941abd-7b5a-3fcc-a384-4291996a32b0 | -15.28963 | -58.18655 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a54ff005-a39a-335c-83c4-2f85b24890d6 | -15.28901 | -58.19032 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae27798e-300a-3b92-84fe-2f496cc2866b | -15.28559 | -58.18978 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c19fcbb-34b4-3ecf-8c5a-602dc0f65ce8 | -15.28496 | -58.19357 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 75619340-c0a6-3137-97a6-e545851d5207 | -15.28433 | -58.19739 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 05165b0d-b513-3422-99de-2c68c4f9f75c | -15.28369 | -58.20127 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 19fe8380-48d3-361b-9c6d-2c8ab8178b97 | -15.28026 | -58.20078 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e525fc35-b1c8-3203-a397-6e89bfd9c7da | -15.27962 | -58.20465 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f7be19b1-61cb-3f01-8de2-6388e6bae7ec | -15.279 | -58.20842 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c4af5818-f84b-3318-919d-831492bcad9b | -9.16605 | -58.53885 | 2024-09-26 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a452366e-256e-32fb-9227-6445018c653a | -9.13872 | -59.40593 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bab5c260-dcf1-3251-9ba9-a48efb1c3797 | -9.95256 | -59.5545 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bd92238a-5149-34f7-8248-141711a7fc62 | -12.02391 | -59.62499 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d8b14a82-5f9a-3221-bffa-4b376fe87a51 | -9.95157 | -59.55641 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bf9eb66e-3ce4-36a1-9777-f6432f0a0db6 | -9.95125 | -59.53906 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0cd043a5-e36c-32db-81e6-b151f17f51f9 | -9.95016 | -59.54093 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d9480b90-a81a-348d-8b2c-4993886bf567 | -9.67289 | -59.08232 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bb72d231-b730-3e53-b3b4-75d49538903d | -9.66916 | -58.43145 | 2024-09-26 04:59:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 736642c1-5e48-3b94-8dba-6c0a0cfc3aef | -9.66771 | -58.4402 | 2024-09-26 04:59:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1504bf34-eadc-3c15-b52c-3ee14921d348 | -9.6655 | -58.43084 | 2024-09-26 04:59:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4194ffb1-e0fb-3025-bda4-fab9c0cac8b5 | -9.66477 | -58.4352 | 2024-09-26 04:59:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a99331a5-af99-3ec4-a1d6-3f20b0ba7383 | -9.66027 | -59.04142 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80a9fae3-a3c0-359d-b94a-8d043f9dbdbb | -9.65947 | -59.04615 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| df1075a7-6555-3250-9b72-38ed0191d65d | -9.40584 | -58.91259 | 2024-09-26 04:59:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 987855df-9cbb-3e7f-870b-445cfa119447 | -9.40537 | -58.91601 | 2024-09-26 04:59:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82a1f7bf-d4e1-3b2b-9a4c-9ca951445beb | -9.39389 | -59.63351 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da2a464f-c43d-3d62-8516-5005d8eedb7b | -9.393 | -59.63863 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aad7a663-e14a-3fbb-89d3-f7cede4a8d5f | -9.39041 | -59.60987 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9d3119a-72f2-3d2e-88d3-c8745611ebf7 | -9.39007 | -59.6361 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e6b28fb9-a3a4-3d44-b001-0ed5b676f2a7 | -9.38994 | -59.63286 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2807370a-26dc-3018-95ad-dc2c96c4c955 | -9.38956 | -59.61498 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cf78385-79ae-3dfb-a346-ba66c0161c76 | -9.38922 | -59.6412 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae4118d4-5c00-3dae-8b9d-c58abb2ce991 | -9.38905 | -59.63797 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c433ba88-b06f-3f4b-8a65-f1d9517a1960 | -10.47026 | -59.13005 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29892269-6af5-3a5b-b4b5-c3d11e398d0d | -10.46955 | -59.13213 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 815782a7-1d1a-3c52-b178-3ee782f32e00 | -10.46649 | -59.1294 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14bc1846-fe19-3605-8437-bb410fb2c4d9 | -10.46578 | -59.13148 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee819a3a-2fc8-3802-8914-de8e38c7be52 | -10.45894 | -59.12824 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f97ce7db-5f34-3ad6-b89f-214313810979 | -10.45823 | -59.13031 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 278c3bd1-e91d-374a-9fd7-93c37aa1b04f | -10.45811 | -59.133 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 147fe626-a900-36aa-ad83-924184d0cddc | -10.45744 | -59.13506 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ac21f99a-c764-3cd3-b88b-e66fa9b3afb5 | -10.39441 | -58.89341 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| eeee60dc-c06a-36fa-847c-051e4329ab47 | -10.39313 | -58.88985 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0605e2db-275d-3297-b113-6ee68f60e59c | -10.39238 | -58.89433 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ff88b7c9-1d51-3922-9f90-c3184a5b6dc8 | -10.39164 | -58.89883 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c9fc04bd-d1fd-3358-bd1c-50f68331f798 | -10.39148 | -58.88823 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0753f33d-a84d-376f-8999-7da63492e3ea | -10.39071 | -58.8927 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bcfb83dd-643e-3584-a9ba-e8848cd1138d | -10.38993 | -58.89718 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 20fb6332-ead5-3897-b35f-b2d745a8a3f4 | -10.38942 | -58.88914 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 21a5323e-f10a-3752-94f7-85118bb39cf0 | -10.38867 | -58.89361 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 72519033-a722-3263-8f53-6563bd8dc877 | -10.38793 | -58.89813 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a17c604b-f16d-32bc-bdbc-a6d20bec2b1b | -10.38571 | -58.88841 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0ebd6ad9-eef4-379f-ba7f-1746e9f706eb | -10.38497 | -58.89289 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d8cab56e-06ec-3675-975d-8dbcc2924a7f | -10.38416 | -58.92076 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79ba79c2-2fdf-3573-8f18-cd1ecc6859e2 | -10.38346 | -58.90194 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d9219a22-5202-345b-a307-9903e70f1ff1 | -10.38045 | -58.92005 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a445a9f5-5590-3579-8c5c-ff09bc3a4aee | -10.3768 | -58.89596 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fca8b0c-fece-3cad-8adc-c463d382eb9a | -10.37604 | -58.9005 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e7a8d93b-e8ba-3da2-81a3-e2c01122ef69 | -10.37309 | -58.89529 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd89d2ed-e58d-3124-b7a0-a72449187e91 | -10.37233 | -58.89981 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a672fbfa-29b2-3975-9a8d-ea6f3a3cdfe5 | -10.36559 | -58.89432 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9d380e8c-6521-32a6-acbd-9cf6d9ca31e5 | -10.36485 | -58.89874 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9c905c2c-362c-38cd-a361-815768c9e557 | -10.36184 | -58.89389 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f004b1cf-5c69-3c9d-91b5-80fc96c09526 | -10.3611 | -58.89828 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a9efba1d-b1f0-3c22-a8db-e1302e19fe7b | -10.36036 | -58.90269 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d725b4c8-a0d2-3c8c-8e82-7b0464ef6036 | -10.35584 | -58.9068 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 581d3a00-c78d-3cea-bebc-6e2372dd3ae9 | -10.3551 | -58.91122 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1e8d137e-53cc-349b-8ffc-5a853fe5cd4c | -10.35059 | -58.91523 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 864b051d-b8a0-3d07-b394-1c46488350de | -10.34983 | -58.91971 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6696bc38-cbcb-3af0-8046-4ef406699e26 | -10.34908 | -58.92421 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f61c0ea0-fb69-316f-8519-bd381c503f34 | -10.29938 | -59.08118 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0b459da4-f76d-3de6-ad55-33395fc0afdc | -10.28231 | -59.0451 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d3453e1-4d69-3a5c-9a2c-6ec7693255f5 | -10.03673 | -58.81604 | 2024-09-26 04:59:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc788e74-07b5-3e9e-ba84-d9143edc39b6 | -10.03301 | -58.81541 | 2024-09-26 04:59:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6810a7d8-dcd4-3171-9202-5cced21631da | -10.03224 | -58.81998 | 2024-09-26 04:59:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59053531-a5d1-399d-95ca-db7657188738 | -10.19276 | -59.75095 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fcb7554b-a2cf-3aec-b4d9-803a628f85d3 | -10.17541 | -59.57246 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1cd771a7-5d6a-3490-836c-00376ca0fb85 | -10.15543 | -59.63849 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43647127-6b00-3a58-9c88-4927c13d7e77 | -10.15542 | -59.64094 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b752e29-bc19-34c3-8729-c5cbf312de6a | -10.22281 | -59.41381 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc0718e2-9f88-3fd2-9ebe-1fbef6a2eee8 | -10.06765 | -59.41806 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 65e14b39-318d-3e50-84c4-31c1e779fbcc | -10.0676 | -59.34795 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96942759-1be3-3541-bfc1-56a3a3dc0c7d | -10.06375 | -59.34739 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a6ad040-491e-3654-bf6c-92d0fe5edd50 | -10.05443 | -59.35575 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8f783279-8696-3f2d-8954-359a46daa9c8 | -12.15781 | -59.72933 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 212924af-f132-3b60-b658-02f0ea5eba95 | -12.15698 | -59.73414 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0f67311-28a0-3826-975e-2464ef07be05 | -12.15614 | -59.73896 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb7cc62b-d4ba-3a2b-be25-418e380fd235 | -12.15531 | -59.74379 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c616b8de-b173-3fd1-9fa6-7c5893f66e0d | -12.15448 | -59.7486 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0918012b-4e23-37b8-b5c8-a6817859edfd | -12.15365 | -59.75342 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 973540d4-2605-3f69-a7a6-5e7caf46949e | -12.03263 | -59.59737 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36fb01d6-f07e-3770-b685-bf445e433de0 | -12.02885 | -59.59669 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 756a2d2a-83ea-324c-9e63-7b561720a6a6 | -12.02425 | -59.60072 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a1f8fcd-2ca2-3d4d-a97a-19b4264d0cde | -12.02394 | -59.60314 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59bfd659-8669-34e0-a479-b1f512281c71 | -12.02342 | -59.60545 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4bf3b5f3-4052-30c6-965b-ea5465cb74e5 | -12.02315 | -59.60788 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e66137b3-97bb-33e8-9500-3867ac682141 | -12.02155 | -59.61737 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c202c6f2-e33e-3c66-940c-ccab9616ac3d | -12.02094 | -59.61964 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2d104a2d-55bf-3d9b-b49f-ab7e049f33fb | -12.02075 | -59.62211 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 185f738c-9bef-38b1-8ed4-1361d5a01087 | -11.27296 | -59.55349 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README135.md)
