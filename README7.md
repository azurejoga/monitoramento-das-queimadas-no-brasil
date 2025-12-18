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
| f3a12171-0be0-399d-bab6-36cf473d2ae4 | -15.12053 | -52.95704 | 2025-12-18 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea26ead7-a7ff-39c5-b5ce-90874ce5a062 | -15.12113 | -52.95272 | 2025-12-18 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7846511-7b57-30ea-a711-5cc00efe4c00 | -15.11691 | -52.95646 | 2025-12-18 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8921da0-2526-34b9-a6a9-116618d175e0 | -14.38906 | -43.9809 | 2025-12-18 04:59:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afa678fa-5c6a-3264-b989-638845b173cf | -14.39307 | -43.9645 | 2025-12-18 04:59:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 409fd238-697a-3a70-a2c3-e0f96a13f346 | -21.22944 | -49.36404 | 2025-12-18 05:01:00 | NOAA-21 | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| db45321f-ba49-3de8-8521-2d386fbd80a4 | -21.35844 | -56.86206 | 2025-12-18 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 62189397-0b73-3af2-b0da-4db2d6c47179 | -18.98213 | -55.30104 | 2025-12-18 05:01:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 71e148db-0d33-32c0-a487-023a748a98af | -18.91122 | -55.5927 | 2025-12-18 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| fe53ce84-5cf8-3cbe-a46f-ba3d96aeb1db | -16.23206 | -59.3342 | 2025-12-18 05:01:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97084c8f-9ccb-3ee7-bd66-b730df37f197 | -21.19559 | -56.92665 | 2025-12-18 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ce676cd-efd7-37b0-a12c-1522896795fd | -18.38608 | -51.44881 | 2025-12-18 05:01:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37af0958-0a6a-39a8-9942-bf4a23a12da0 | -20.19829 | -54.76556 | 2025-12-18 05:01:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2def3e8c-3231-3402-9e6c-80d46ca146e1 | -19.00336 | -57.62575 | 2025-12-18 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 7ac6192c-b10b-3976-b257-c9df6b61b4f3 | -18.39021 | -51.44945 | 2025-12-18 05:01:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89eb7e49-ca3c-3bad-b044-4f97af754a4b | -20.87583 | -50.07553 | 2025-12-18 05:01:00 | NOAA-21 | MONÇÕES | SÃO PAULO | Brasil | 3531001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| efb39c10-23ab-3e42-aa85-7dc905858804 | -19.56571 | -50.99154 | 2025-12-18 05:01:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a6a7ce66-f6f8-38bc-977e-56eb91e1a13f | -16.11003 | -56.75942 | 2025-12-18 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6446b462-d15c-385d-bdc0-3d9f3b3263c2 | -18.39069 | -51.44561 | 2025-12-18 05:01:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb40c6b2-acef-340f-9b69-440b5accb021 | -21.20168 | -56.93154 | 2025-12-18 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f91f5196-6a86-3c3a-bb4b-3ecf82a1e815 | -21.19502 | -56.93037 | 2025-12-18 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1064e977-2ce5-33eb-870f-8080c8daa017 | -19.56139 | -50.99094 | 2025-12-18 05:01:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 048ed248-37e4-3234-90ab-e898702a0bc0 | -29.10486 | -49.54389 | 2025-12-18 05:03:00 | NOAA-21 | BALNEÁRIO GAIVOTA | SANTA CATARINA | Brasil | 4202073 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 86a5bced-e845-39cb-a9e2-ffdd57977da0 | -29.1102 | -49.54449 | 2025-12-18 05:03:00 | NOAA-21 | BALNEÁRIO GAIVOTA | SANTA CATARINA | Brasil | 4202073 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c9c196fc-7d26-3056-ae20-64ef184f2d00 | -29.10514 | -49.54012 | 2025-12-18 05:03:00 | NOAA-21 | BALNEÁRIO GAIVOTA | SANTA CATARINA | Brasil | 4202073 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a511c635-f40a-311d-81ea-1ee4fe88ff53 | -29.10684 | -49.54288 | 2025-12-18 05:03:00 | NOAA-21 | BALNEÁRIO GAIVOTA | SANTA CATARINA | Brasil | 4202073 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| fe10b9f7-d791-323b-b3ab-44cd38ff6f45 | -33.63696 | -53.45439 | 2025-12-18 05:05:00 | NOAA-21 | CHUÍ | RIO GRANDE DO SUL | Brasil | 4305439 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| ef05df07-ec7a-3e52-b532-1e47ad4b3779 | -32.35342 | -52.37177 | 2025-12-18 05:05:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 3.5 |
| 01a3cc2e-2bf7-39f9-b66e-cf966885d165 | -32.36094 | -52.3672 | 2025-12-18 05:05:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 4.3 |
| 1248ba44-9db6-3d94-809a-fcfd9d9029dd | -32.35809 | -52.37238 | 2025-12-18 05:05:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 3.5 |
| dde12c24-c9af-34fa-8781-e71835724e0a | -32.36045 | -52.37291 | 2025-12-18 05:05:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 4.3 |
| e10d5102-c96e-3f28-ab32-7f58b7c0efcb | -32.36277 | -52.37298 | 2025-12-18 05:05:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 7.0 |
| 21c5bf8e-a463-3a5e-95d1-5f4906ff1958 | -32.35578 | -52.37229 | 2025-12-18 05:05:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 4.3 |
| 161c7d97-003a-3b7b-ada2-ae207d5d7bba | -1.40613 | -51.7363 | 2025-12-18 05:25:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9243d7d0-db55-3220-8d79-e43ef37ed81f | -3.15312 | -48.1436 | 2025-12-18 05:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e27cf44a-e8e8-3b68-bab1-33a8d2ff6b62 | -3.1595 | -48.14449 | 2025-12-18 05:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff39b19e-a62c-3bd9-a3ca-d8390067836d | -2.37592 | -51.91695 | 2025-12-18 05:25:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7bbc055b-f069-3a47-8854-9e2869431b25 | -3.66255 | -47.54949 | 2025-12-18 05:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 573fe552-f853-3a3e-beab-2a5da9112f6a | -1.40755 | -51.7387 | 2025-12-18 05:25:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c34b1c4-6cbd-3cee-b490-7e05ffe7af5e | -2.89094 | -53.01444 | 2025-12-18 05:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7967e70d-d9eb-3b30-98f6-7034b4e16175 | -2.98953 | -52.37276 | 2025-12-18 05:25:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c000ffce-d927-3d93-94eb-5e8058f27e4c | -1.40528 | -51.74168 | 2025-12-18 05:25:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06c44c36-dcad-353e-bfd2-050ea28f983d | -1.42637 | -55.34501 | 2025-12-18 05:25:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b83b9472-1849-37eb-ad15-0a76811fc188 | -3.15161 | -48.15387 | 2025-12-18 05:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ed87031-bc5c-38d2-96f7-2be42a8867db | -2.97096 | -52.69047 | 2025-12-18 05:25:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0355204-9086-3a6e-b4c2-7f63a8d03060 | -1.40266 | -51.73795 | 2025-12-18 05:25:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cdc05cbe-b923-3730-a4ae-90c357ca0bfc | -3.15875 | -48.14958 | 2025-12-18 05:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1add7b0-caaf-3106-af2f-951d2bfb61ee | -2.98874 | -52.37796 | 2025-12-18 05:25:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f99e277-4629-35ee-a277-47d46a225287 | -1.4271 | -55.3403 | 2025-12-18 05:25:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b206c1f-0300-3b16-8292-3235b0ac0c16 | -3.14523 | -48.15303 | 2025-12-18 05:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ea80497-9521-37ca-8d95-37553302a71b | -15.1191 | -52.95581 | 2025-12-18 05:29:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07df8521-5df5-3ebb-979b-1a97e8ae1e98 | -12.42598 | -64.1351 | 2025-12-18 05:29:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9234c897-52ac-3dbf-93c3-c503e6bb839c | -12.17943 | -64.12202 | 2025-12-18 05:29:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 261ea470-1e45-343b-bbb3-3779faeeec32 | -32.36156 | -52.37219 | 2025-12-18 05:33:00 | NPP-375D | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| a1749dad-8577-397c-b789-8150c2a98317 | -32.35481 | -52.37178 | 2025-12-18 05:33:00 | NPP-375D | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| d060526b-cfc8-3eb6-9dcf-012d57cd6679 | 3.22229 | -60.7413 | 2025-12-18 05:46:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d38457f1-ae9a-38df-baf6-8b4a48e618f0 | -12.18084 | -64.12326 | 2025-12-18 05:50:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71d6ca90-b723-3b42-9fd7-f52ced62e755 | -32.35768 | -52.36883 | 2025-12-18 06:16:00 | AQUA_M-M | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 23.7 |
| b49ef4f7-0676-37ec-97ae-a7c5b6408ef8 | -4.20521 | -44.21854 | 2025-12-18 12:14:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 2174e6a6-8b81-3979-a831-7ba0d2c07f51 | -4.19491 | -44.21714 | 2025-12-18 12:14:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 37.3 |
| b1dc286f-4aa4-33e1-a99a-1a20300eecda | -1.713 | -47.01847 | 2025-12-18 12:14:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a9742692-3db3-3382-a0fa-ac213b8921b0 | -3.73712 | -48.85296 | 2025-12-18 12:14:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d7c11bc4-4f99-34da-a4a6-889b8fc9ecc4 | -3.72058 | -43.68614 | 2025-12-18 12:14:00 | TERRA_M-T | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 8d88cd4f-0ab7-3b84-8028-a3922aee21f5 | -4.19638 | -44.22395 | 2025-12-18 12:14:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 832538e8-be93-3055-ad58-3138a3039914 | -3.15669 | -48.1387 | 2025-12-18 12:14:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 82d1b250-89c4-3d7d-a264-c3e709833792 | -2.84366 | -46.72605 | 2025-12-18 12:14:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 1dbeb9c0-9da2-300a-a0ab-718568af50ff | -3.51123 | -44.73174 | 2025-12-18 12:14:00 | TERRA_M-T | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 11ec94e8-0719-3413-bde2-1509b53c8c07 | -3.15542 | -48.14753 | 2025-12-18 12:14:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 0749a94d-0581-3f2c-a3af-4508880fb80a | -1.70284 | -45.14692 | 2025-12-18 12:14:00 | TERRA_M-T | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 1f40ef5e-11c1-3b5a-b317-826db11ccbab | -3.7358 | -48.862 | 2025-12-18 12:14:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1a473026-34b7-35bb-b9b3-228e453ce500 | -4.19811 | -44.21172 | 2025-12-18 12:14:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 25f4be5a-ef30-3eaa-ac27-33d526e66917 | -1.71174 | -47.02724 | 2025-12-18 12:14:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 76a2f420-16f4-3b47-a7e8-bed2956db40c | -2.51327 | -47.80822 | 2025-12-18 12:14:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9f506e38-0f67-36a9-9a51-0cc5865addcb | -11.91306 | -43.82238 | 2025-12-18 12:16:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| d860f62b-1180-3c48-9c1d-fe237554af9e | -12.74334 | -43.44085 | 2025-12-18 12:16:00 | TERRA_M-T | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| f9d1affc-ef00-311f-a680-25d4359744d5 | -11.84445 | -43.73652 | 2025-12-18 12:16:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 7170a271-ad38-3e5c-ac92-75bf4120ba79 | -11.15118 | -43.32816 | 2025-12-18 12:16:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 38.9 |
| 9fb51550-9d9c-34a9-aaf1-b30e6282c8d7 | -11.84663 | -43.71894 | 2025-12-18 12:16:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 6e26b346-32f3-3d64-b4a4-cecaa57eb4f4 | -11.15345 | -43.30971 | 2025-12-18 12:16:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 32.1 |
| b633bf51-cc01-34cc-b682-8cf53d255498 | -13.39991 | -43.96461 | 2025-12-18 12:16:00 | TERRA_M-T | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| d63a796c-fc27-33b1-a23d-1a952ce06c10 | -22.5359 | -52.8937 | 2025-12-18 12:21:00 | TERRA_M-T | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 0acc3e90-bcdd-34d6-9ae2-d5e6e81758ec | -24.2091 | -49.41373 | 2025-12-18 12:21:00 | TERRA_M-T | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d4b3515b-85f3-3354-b353-eefd0cb44b9c | -29.03068 | -51.18573 | 2025-12-18 12:23:00 | TERRA_M-T | FLORES DA CUNHA | RIO GRANDE DO SUL | Brasil | 4308201 | 43 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 76ea2d4d-2b53-381d-bf26-f2c553d12b77 | -28.97289 | -51.06731 | 2025-12-18 12:23:00 | TERRA_M-T | SÃO MARCOS | RIO GRANDE DO SUL | Brasil | 4319000 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| f068d34f-15dc-3fba-84d8-519d1f983e8c | -29.03208 | -51.17459 | 2025-12-18 12:23:00 | TERRA_M-T | FLORES DA CUNHA | RIO GRANDE DO SUL | Brasil | 4308201 | 43 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| d3e779a8-e4f6-37b1-91d1-821e23260e2a | -29.50664 | -51.49668 | 2025-12-18 12:23:00 | TERRA_M-T | SÃO JOSÉ DO SUL | RIO GRANDE DO SUL | Brasil | 4318614 | 43 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| c108e089-30a8-3062-8c40-c87b0107fb06 | -28.93057 | -51.54586 | 2025-12-18 12:23:00 | TERRA_M-T | VERANÓPOLIS | RIO GRANDE DO SUL | Brasil | 4322806 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| edcddaf9-5925-31b4-a7e9-a58279836243 | -27.32001 | -50.50934 | 2025-12-18 12:23:00 | TERRA_M-T | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| b5ba1e70-da6d-3478-937a-36681e3b3b06 | -32.35675 | -52.37137 | 2025-12-18 12:25:00 | TERRA_M-T | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 10.3 |
| a199a7a7-a760-3e42-9ae9-19763bced6b9 | -32.36595 | -52.37296 | 2025-12-18 12:25:00 | TERRA_M-T | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 6.5 |
| f0e5e9ad-ec51-3667-bbed-5185f80a59f1 | -32.37516 | -52.37455 | 2025-12-18 12:25:00 | TERRA_M-T | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 20.5 |
| 99b1caee-2d79-3f21-b5ea-62c312e3a3f1 | -2.713 | -51.9004 | 2025-12-18 14:40:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 144.1 |
| d44f4d1b-59ee-3d9d-930c-a0a119203809 | -3.2022 | -49.3574 | 2025-12-18 14:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 52ed5ee4-8f0b-3f71-9e07-cdd5b9c9d33c | -3.2207 | -49.3568 | 2025-12-18 14:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 115.1 |


