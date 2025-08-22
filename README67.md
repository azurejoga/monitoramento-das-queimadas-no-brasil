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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b16f0ab-32db-3cde-a935-d62d5861e016 | -7.1662 | -44.6736 | 2025-08-22 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 218b44dc-84c0-30d2-aa05-4800610683ea | -12.9925 | -45.202 | 2025-08-22 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 210.4 |
| 90031eb8-3940-3a07-8260-f973ab85e4b5 | -14.5063 | -48.8307 | 2025-08-22 13:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 1db7e9c1-df27-38e8-b5b6-b33a1fcbd34e | -14.6519 | -54.875 | 2025-08-22 13:00:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 6af07a02-63fb-354c-841e-d1aceba94c0a | -12.2938 | -50.0121 | 2025-08-22 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 395069c4-19c2-354a-ae1d-f29ce4a746e4 | -7.6296 | -45.2464 | 2025-08-22 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 8934a5eb-7765-3ada-8ce1-f953dd5d8ea2 | -6.436 | -44.5306 | 2025-08-22 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| ea2340f3-787d-3165-9fd2-dc25484a085e | -19.3227 | -45.0698 | 2025-08-22 13:00:00 | GOES-19 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 206.8 |
| 732a8d36-367a-34dc-8cb7-8742ba0bcc0d | -12.9921 | -45.2252 | 2025-08-22 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 238.4 |
| 359cd767-c304-3921-9e09-27c8624620a3 | -14.6523 | -54.8543 | 2025-08-22 13:00:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 73.1 |
| b0620813-64f8-3f20-bc7b-80798944de62 | -13.3966 | -46.2406 | 2025-08-22 13:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 38cab092-f340-326f-98b6-40943ab06532 | -6.3311 | -43.7557 | 2025-08-22 13:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 7d33d459-cd28-3ab4-a440-edd5c17a4673 | -14.6713 | -54.8728 | 2025-08-22 13:00:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 911a95e3-8e4c-3a53-a0cc-8dae4789c600 | -12.3129 | -50.0097 | 2025-08-22 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 173.7 |
| 48be588e-9247-368a-9448-b526cedeb95a | -7.1017 | -43.7108 | 2025-08-22 13:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 2fc75ca7-0597-3130-9286-5076f2ac959f | -6.4362 | -44.5076 | 2025-08-22 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| b8ed60e6-9de4-3f4d-9732-b17857554e21 | -7.0354 | -44.6167 | 2025-08-22 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| caa85cb7-6fc9-366d-a714-7bb11d5fb885 | -14.8343 | -47.9536 | 2025-08-22 13:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 85.2 |
| c94fce29-8bb4-327d-9af6-6ac065548891 | -12.3133 | -49.9881 | 2025-08-22 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 304.0 |
| c9c4540e-4963-322e-8468-053451efeb5d | -7.6557 | -46.2582 | 2025-08-22 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 364e6bea-01d6-3672-bec6-718330571ef4 | -7.6559 | -46.2358 | 2025-08-22 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 7f6cd48b-86ec-3b9b-aa6c-bd7d15d289c6 | -19.322 | -45.094 | 2025-08-22 13:00:00 | GOES-19 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 4b14ae7f-2aa7-345d-9eb4-00cc4c9be265 | -7.0352 | -44.6396 | 2025-08-22 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 98a236c0-c6fc-3a49-bd0f-65db0def2bf4 | -7.6181 | -46.2616 | 2025-08-22 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| f9a42992-0d51-31c3-9f98-21ad7049be2f | -12.3129 | -50.0097 | 2025-08-22 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 00154d24-c38e-3ab9-9f78-b602af890047 | -8.7759 | -45.4486 | 2025-08-22 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 107.8 |
| dd4952c2-3535-3c3f-9fa0-207a26d11c54 | -12.9921 | -45.2252 | 2025-08-22 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 217.2 |
| 79587228-edb0-3de9-93f1-72ce1210d1dc | -14.5063 | -48.8307 | 2025-08-22 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 207.7 |
| 319f4cdb-01c0-3a0e-8e62-69da60962833 | -6.4362 | -44.5076 | 2025-08-22 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 3f3fc4ee-49c9-3969-a729-52fcd2c7a7f4 | -7.6369 | -46.2599 | 2025-08-22 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 1d329b6c-a9ef-37d8-8bd6-abbe4222f60f | -5.7782 | -44.787 | 2025-08-22 13:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 7ed34db0-d39b-3ace-9716-1b982c83c7a7 | -12.3133 | -49.9881 | 2025-08-22 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 246.7 |
| f31f0283-a118-3b23-ba1a-872f2dfd0585 | -8.7785 | -46.7082 | 2025-08-22 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 49aabefd-bcb4-3079-a501-d40d5ff7a342 | -8.3011 | -47.2873 | 2025-08-22 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 82737b00-8ab2-35b9-96c7-3e6ac723686d | -14.6519 | -54.875 | 2025-08-22 13:10:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 02f2b4d9-bcdb-3bb1-a636-51fec00c6c8b | -7.6559 | -46.2358 | 2025-08-22 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| afe4c2a7-dbe7-3e63-848f-2b429ef7a393 | -8.4591 | -48.2377 | 2025-08-22 13:10:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 123.8 |
| d99a7c56-9869-364a-ab82-460d10684190 | -8.4776 | -48.2578 | 2025-08-22 13:10:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 40e9d51a-f906-39eb-90cb-47bffbabfede | -5.7784 | -44.7642 | 2025-08-22 13:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 8434e052-ee25-3cb1-8570-1dd98ceeeabd | -6.436 | -44.5306 | 2025-08-22 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 2c37505c-a4a7-3478-ae1e-64ae93d9617d | -8.7756 | -45.4713 | 2025-08-22 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 825dd1cc-b00e-3fd8-9f17-8a7d9aebb062 | -7.0352 | -44.6396 | 2025-08-22 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| af0b1e6a-6e8d-3ad2-8a75-7dd3526ccbcd | -14.8348 | -47.9311 | 2025-08-22 13:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 120.0 |
| e3b2991d-fe86-3b41-b03d-95d8f766325b | -14.6523 | -54.8543 | 2025-08-22 13:10:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 76657a1e-71ce-3bea-8495-ef8e510ea216 | -7.6484 | -45.2446 | 2025-08-22 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.1 |
| b2b3a556-314b-3bf4-8fab-a89308e1ebdc | -14.6713 | -54.8728 | 2025-08-22 13:10:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 5b72d2d9-7693-3daa-84be-b400d96bfe52 | -6.7319 | -43.1379 | 2025-08-22 13:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 77413959-cedb-3482-a70d-cd43143e4214 | -8.4588 | -48.2595 | 2025-08-22 13:10:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 162.7 |
| 061a8135-8d3f-3d53-8d79-71da3b71d348 | -13.1456 | -40.6567 | 2025-08-22 13:10:00 | GOES-19 | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 110.2 |
| 4ee77fa6-1436-3b54-8eee-a887d14593d3 | -7.6296 | -45.2464 | 2025-08-22 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 29adeaa3-ddc3-3bac-8090-da6e506c21c0 | -8.4779 | -48.236 | 2025-08-22 13:10:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 016985e0-a2b7-3a40-883a-3e0d28501c38 | -8.7567 | -45.4733 | 2025-08-22 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 31355ec3-f5f0-3c7a-9fe3-624e189e0dba | -7.1017 | -43.7108 | 2025-08-22 13:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 7e7904f4-066c-3fe1-a9e6-19bcbf95ebf5 | -12.9925 | -45.202 | 2025-08-22 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 211.8 |
| dadc1797-e295-329c-a015-a80047e78887 | -8.7783 | -46.7305 | 2025-08-22 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| f7034546-4578-34bf-b174-159f02081f37 | -12.9925 | -45.202 | 2025-08-22 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 206.2 |
| 61508a1f-0ac0-39de-9393-9830856a4372 | -7.6181 | -46.2616 | 2025-08-22 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 0f963928-675d-3d26-8b80-286989fad34b | -8.3011 | -47.2873 | 2025-08-22 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 155.5 |
| 90378b24-d07f-3722-960e-c4b913c22b4c | -7.6369 | -46.2599 | 2025-08-22 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 7a1d4d63-44cb-30f5-b1a0-c905660bb97e | -14.7717 | -45.4055 | 2025-08-22 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| a9e963a0-88f0-3863-88ca-ed99a87aa5b7 | -7.6484 | -45.2446 | 2025-08-22 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 84.8 |
| f6e00ce3-cecd-3013-900e-5a5ce52b54ce | -8.4588 | -48.2595 | 2025-08-22 13:20:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| c0984888-c912-3a9c-a5a0-180f707cbc26 | -7.1662 | -44.6736 | 2025-08-22 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 8edf0ab7-4203-3e46-950f-e887e8158bf9 | -7.6296 | -45.2464 | 2025-08-22 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 902b5d97-740a-344b-bc4d-377f19efeaed | -12.9353 | -46.1762 | 2025-08-22 13:20:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 5d6f8f06-40bf-3c45-99df-d3ba92e9c7c4 | -8.3009 | -47.3094 | 2025-08-22 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| b08e4d48-3146-3906-99e9-bd19a907de79 | -7.6559 | -46.2358 | 2025-08-22 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 130.1 |
| a20387d5-4f30-3546-88e7-747097ff4b54 | -7.0352 | -44.6396 | 2025-08-22 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 0b475ad7-973d-3aaa-b313-dfab88b7d842 | -6.5105 | -44.5702 | 2025-08-22 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| ef1293fe-3e7e-350d-9413-5e1be16db00f | -6.7319 | -43.1379 | 2025-08-22 13:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 1e23dc53-312b-3ed6-8043-8181fcd88477 | -6.436 | -44.5306 | 2025-08-22 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 1c7add9c-b577-3118-a2c6-1cb472aac0a1 | -12.3129 | -50.0097 | 2025-08-22 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 7e31ebf8-7b69-3675-8775-4602cca7ea30 | -6.4266 | -45.4861 | 2025-08-22 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 3986d4d0-2a95-301e-8310-bd818d3a866c | -14.8348 | -47.9311 | 2025-08-22 13:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 68c7ceb3-227d-33e7-bd71-03e53c9aafcb | -14.6519 | -54.875 | 2025-08-22 13:20:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 58e62069-7f0a-34d3-8172-3211c40d2565 | -12.3133 | -49.9881 | 2025-08-22 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 195.3 |
| 8f0c2383-5c43-3bc6-b0ad-ff547153da3b | -6.3311 | -43.7557 | 2025-08-22 13:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 223a3cd7-141a-3bdc-8298-af0eb9968ba3 | -20.2492 | -46.7017 | 2025-08-22 13:20:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 133.8 |
| b4f65945-7d03-38b5-af0c-96ad6b882602 | -12.9921 | -45.2252 | 2025-08-22 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 221.5 |
| 69b9ab22-fdc8-3222-90e9-35d639405e52 | -14.596 | -54.7575 | 2025-08-22 13:20:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 6b2f3db0-71e4-30ad-8c8f-be5d6d0ed1d2 | -7.6366 | -46.2823 | 2025-08-22 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 7ac0bfa3-ea9c-3bda-94b8-4751c15ee38c | -20.2287 | -46.7066 | 2025-08-22 13:20:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 95.8 |
| d4edd34c-ad85-37f8-8362-5f35814db830 | -7.1017 | -43.7108 | 2025-08-22 13:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 1de99fdb-b3c3-3aec-9c30-0cf0eb064c6f | -7.6557 | -46.2582 | 2025-08-22 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 5cf156aa-eb98-3251-b327-0a7eaa27339e | -7.1662 | -44.6736 | 2025-08-22 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 3b8964bf-4f8b-343f-a0a7-5d1b1d6599fd | -14.7501 | -56.0356 | 2025-08-22 13:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 778054ce-1ccd-3939-bc64-293be10e83df | -14.5257 | -47.8469 | 2025-08-22 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 36d3b314-fdfd-3be6-a58a-8c3996182a16 | -14.7694 | -56.0335 | 2025-08-22 13:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 0ab60b00-31db-3b83-bdc7-1379b3a4b561 | -14.8343 | -47.9536 | 2025-08-22 13:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 2612ed9d-875a-393e-9eaa-81069af74517 | -7.1017 | -43.7108 | 2025-08-22 13:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| acb81147-fb8f-3de4-817b-5a81699ccfc0 | -7.6484 | -45.2446 | 2025-08-22 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 3dac2450-3762-34ba-9417-7564287cc289 | -6.3311 | -43.7557 | 2025-08-22 13:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 03e0649b-50dc-32ef-9561-24a9fc1ec5f3 | -12.3129 | -50.0097 | 2025-08-22 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 4295fd71-41f9-3605-a8be-865de7fdb7a4 | -14.6519 | -54.875 | 2025-08-22 13:30:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 135.0 |
| d8cab1e0-ffaa-3e06-875d-092c917539fa | -14.6713 | -54.8728 | 2025-08-22 13:30:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 92.9 |
| a9cd3b05-ace1-31df-a0e5-47dce45e39a2 | -12.9925 | -45.202 | 2025-08-22 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 184.4 |
| d7fd8070-3a4c-36e7-8b02-50a8267f49ab | -6.5196 | -45.5464 | 2025-08-22 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 8a01b65c-3f59-3b73-9780-ce62eb155135 | -6.7319 | -43.1379 | 2025-08-22 13:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 23eb2da3-9d60-3b21-a461-5f562b88e2fe | -5.7971 | -44.7628 | 2025-08-22 13:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| cc5020cd-e513-303a-8a69-7378902e64de | -14.6523 | -54.8543 | 2025-08-22 13:30:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |


[Clique aqui para ver as próximas entradas](README68.md)
