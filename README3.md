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
| fee77e1d-9509-3396-84ef-6f8937f5c08f | -8.2851 | -45.4999 | 2025-09-29 01:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 5e243c6b-2ded-3fc8-8c99-9e4f13777f17 | -9.4007 | -54.6984 | 2025-09-29 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 515ae48f-9d9b-306d-8afd-7f46ae9bfe1b | -20.0491 | -41.3251 | 2025-09-29 01:10:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 176.9 |
| 42416acf-4664-3e36-a24a-20077852e9e1 | -4.7159 | -41.9736 | 2025-09-29 01:10:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 92.4 |
| 1fa51f18-2334-3408-acbd-c469d426cde3 | -11.925 | -48.0273 | 2025-09-29 01:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 59e25018-4493-3fa6-bc2a-3bccc3682e07 | -10.0531 | -50.1978 | 2025-09-29 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 5c76357f-a933-3127-8ce5-b8b5ac6e85f7 | -4.6969 | -41.9987 | 2025-09-29 01:10:00 | GOES-19 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 60.1 |
| f066e4d4-9c3b-3a67-b08b-73d518892a9b | -4.7157 | -41.9974 | 2025-09-29 01:10:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 0cc0483b-61c8-35fd-8e83-ecf3ada11ca8 | -10.8429 | -45.4044 | 2025-09-29 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 2722a768-dce5-35d3-b5f2-1dfa57a38243 | -10.8238 | -45.407 | 2025-09-29 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 3e9a2b00-d3ae-3427-b2ce-0ff9d4c503f8 | -7.2402 | -44.7812 | 2025-09-29 01:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 19d42c4f-51fc-34fe-8a3f-5681cb65a920 | -4.6971 | -41.9748 | 2025-09-29 01:10:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 69.4 |
| 3abcb0de-3738-30e2-9610-5848ef46fcfc | -7.2211 | -44.8058 | 2025-09-29 01:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 9f83e472-c7d8-34cc-862e-efc3b1a9e3ed | -20.0482 | -41.351 | 2025-09-29 01:10:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.9 |
| 896f61af-0ebd-3608-a8c0-b95c0d292e1e | -2.5773 | -48.3931 | 2025-09-29 01:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 7dcc6f6f-ea6a-37b1-8aaa-3c03f7c0b8dc | -10.0339 | -50.2211 | 2025-09-29 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 907e53bc-084f-3a2f-b1d1-4f564621ac73 | -17.0938 | -48.5699 | 2025-09-29 01:10:00 | GOES-19 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 879a6110-e1af-38c5-a8fe-e395c82b8e89 | -15.2655 | -48.7544 | 2025-09-29 01:10:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 63.4 |
| c2927e8a-4591-3f38-93d2-0695d150eee7 | -14.5336 | -48.4268 | 2025-09-29 01:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 60.9 |
| a6b9267f-6dda-3e48-b9e0-5cb87362c1b4 | -20.0698 | -41.3189 | 2025-09-29 01:10:00 | GOES-19 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 84.7 |
| 4155984a-1044-37a4-9b13-75ecf542153f | -15.2893 | -49.5035 | 2025-09-29 01:10:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 8129a75a-f1a0-3b3b-8b3f-62d71567c60a | -9.4194 | -54.697 | 2025-09-29 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| ca7a55f4-f8dc-3239-846a-65d3d3a5dace | -3.1013 | -47.0082 | 2025-09-29 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 5c78bdb0-4084-31c6-ae7e-bf263abed74b | -10.0342 | -50.1997 | 2025-09-29 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| dea65667-30b2-3d1e-bd70-a986f7feaf6a | -14.553 | -48.4237 | 2025-09-29 01:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 3bd96080-97f7-3d9c-989b-d394a880a919 | -8.2854 | -45.4772 | 2025-09-29 01:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 63.8 |
| ade5ff20-4ccb-3cc9-a875-76ba07f02e04 | -10.0339 | -50.2211 | 2025-09-29 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 5bea07ce-5522-3235-92aa-565e99d1dd27 | -15.2893 | -49.5035 | 2025-09-29 01:20:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 4435f9b4-4578-3ac6-9d5e-fd36d776e06b | -9.4007 | -54.6984 | 2025-09-29 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 809b5d23-0beb-3f05-a4fa-71dc8b435b4e | -4.7159 | -41.9736 | 2025-09-29 01:20:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 143.8 |
| 3299d793-28ec-3d93-8ee0-7842432a9a15 | -7.2402 | -44.7812 | 2025-09-29 01:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 141.8 |
| c1a71011-a5a7-345e-baa3-90c4cacb6cc1 | -9.4194 | -54.697 | 2025-09-29 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 72a6ddb6-fdd0-3112-b0b8-5f813148fb94 | -10.0342 | -50.1997 | 2025-09-29 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| a45453e8-3ca7-3699-9426-cc5ea45474ab | -2.5772 | -48.4146 | 2025-09-29 01:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 33bf0642-271c-3120-b069-f981d1d41d8c | -10.0531 | -50.1978 | 2025-09-29 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 1574cdc8-10c1-31e2-9fa1-6fca6e3f3b54 | -3.1012 | -47.0301 | 2025-09-29 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 2c756230-0e60-35d5-b34a-4d4215ebc421 | -10.0528 | -50.2192 | 2025-09-29 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 15a34315-059f-3025-b8e8-9bb0552eeeea | -4.4013 | -44.0755 | 2025-09-29 01:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 5a86f737-83db-32f4-8542-faa6669d5a4e | -11.925 | -48.0273 | 2025-09-29 01:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 9a4c277f-0ade-3e29-8345-b4164bd1da23 | -11.9247 | -48.0495 | 2025-09-29 01:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| d5c9b961-478b-39f8-8b14-a843a258245a | -7.2214 | -44.783 | 2025-09-29 01:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 215.3 |
| b154b6bd-c08e-3323-938d-36327caf212c | -2.5957 | -48.4141 | 2025-09-29 01:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 955077d0-8c85-35e2-af5a-658447aa2f18 | -17.0938 | -48.5699 | 2025-09-29 01:20:00 | GOES-19 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 09d5f3d5-6743-3d29-bc6d-6ff734bbb4b2 | -22.3722 | -54.7512 | 2025-09-29 01:20:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 201.8 |
| d25548e7-05b5-34ff-80ee-9e3dfbc1c265 | -12.6913 | -46.8934 | 2025-09-29 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 68d81df6-d210-31f3-bab1-f210083c383d | -20.0698 | -41.3189 | 2025-09-29 01:20:00 | GOES-19 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 54.9 |
| dc0d4fae-9232-3e87-ad93-d01f065d4f18 | -7.2211 | -44.8058 | 2025-09-29 01:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 2f0c9378-8d71-310a-8f48-936bc68b77e6 | -12.7105 | -46.8906 | 2025-09-29 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 31d3c498-2ead-34c8-a920-585d23e767a3 | -3.1013 | -47.0082 | 2025-09-29 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 130.5 |
| ac0a4498-e621-3db2-9e37-3592686a483c | -20.0491 | -41.3251 | 2025-09-29 01:20:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 92.5 |
| 34a3a54c-b1f8-3e3d-9c6e-a34bc64271e8 | -16.54 | -45.2948 | 2025-09-29 01:20:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 73.4 |
| d3badffa-c46d-3c7c-9163-a092e167553b | -14.553 | -48.4237 | 2025-09-29 01:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 997dffdf-f532-3566-ac1e-174335076d0b | -2.5773 | -48.3931 | 2025-09-29 01:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 354856f4-c144-319e-bee2-9726c6659e66 | -20.3715 | -51.2111 | 2025-09-29 01:20:00 | GOES-19 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 55.4 |
| 19c036dd-087a-3811-a9b9-cb1cd226ae17 | -22.3929 | -54.7474 | 2025-09-29 01:20:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 99.9 |
| d63f1442-45a9-3c65-8a04-829c0922d811 | -4.7157 | -41.9974 | 2025-09-29 01:20:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 101.8 |
| aac2832c-87c8-3857-90b7-e2b36f90f03b | -22.3716 | -54.7731 | 2025-09-29 01:20:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 35d4c7af-4a1b-317e-91a4-dbc59fd014f7 | -14.5336 | -48.4268 | 2025-09-29 01:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 1ddbbc14-23f2-38da-be60-415fb5baea6f | -4.6971 | -41.9748 | 2025-09-29 01:20:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 71.6 |
| f6cbe98c-d4f0-32ce-9d6f-0eeccd3955df | -22.37485 | -54.76998 | 2025-09-29 01:26:00 | TERRA_M-M | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 23.8 |
| e26910c6-1b2b-3380-91a9-0734a82e711a | -22.37186 | -54.75285 | 2025-09-29 01:26:00 | TERRA_M-M | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 96.2 |
| bf4fd142-8a34-3c20-85c6-bac32d1a07a3 | -22.38638 | -54.7674 | 2025-09-29 01:26:00 | TERRA_M-M | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 82d3f009-60c0-3a54-b652-7891912b8aa7 | -22.38341 | -54.75025 | 2025-09-29 01:26:00 | TERRA_M-M | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 28ff6ce3-014d-3910-8bfb-1aed04496f2c | -18.17805 | -53.33451 | 2025-09-29 01:28:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 25.3 |
| c90bf174-886d-3811-85f9-647ad2ca425e | -18.17455 | -53.3411 | 2025-09-29 01:28:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 2d1484b5-8024-3d41-a133-26c7c60bb54d | -21.46893 | -57.68481 | 2025-09-29 01:28:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| f78471f1-58ae-3c96-a191-d8450af39450 | -18.17015 | -53.31659 | 2025-09-29 01:28:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 5769cfb3-8fb6-3265-9ad5-e122433acd27 | -3.1012 | -47.0301 | 2025-09-29 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| f8fef6d0-56a7-30c1-8d9e-fb7252cce39f | -2.5773 | -48.3931 | 2025-09-29 01:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| b5366d5e-6eb5-3847-abd1-1a44b71010f7 | -10.0528 | -50.2192 | 2025-09-29 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 5e2b5461-137c-31ea-b1fe-bf7d67058421 | -11.9442 | -48.0248 | 2025-09-29 01:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| a7712f07-215f-3441-be79-2f437cc0fc14 | -16.3351 | -49.951 | 2025-09-29 01:30:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 8edbf6d7-94a5-3603-adcf-ec03c681a9de | -11.925 | -48.0273 | 2025-09-29 01:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 2338b788-60b4-356d-a611-5f1127869f3e | -12.7105 | -46.8906 | 2025-09-29 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 168.1 |
| 49bf56ca-afa4-371f-924b-cf03207e921e | -12.7101 | -46.9132 | 2025-09-29 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 1e793413-f4ce-318a-95e5-242db4e66564 | -2.5772 | -48.4146 | 2025-09-29 01:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| c61c4939-d41c-388f-b991-b19ab25ab950 | -9.4194 | -54.697 | 2025-09-29 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 39dc70e8-6041-37d9-b013-3c0d77eedf7d | -8.2851 | -45.4999 | 2025-09-29 01:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 2ab42d87-8f61-3cea-b3b1-f58e2af7aa43 | -14.5336 | -48.4268 | 2025-09-29 01:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 41.1 |
| f26e6842-27ad-393f-b918-1ca9daae2bd9 | -12.8103 | -47.7505 | 2025-09-29 01:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| f08f08d5-341e-3eab-b17e-62445de89f5c | -10.0531 | -50.1978 | 2025-09-29 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 1c516530-c812-3f9f-be6b-cf9cb5669386 | -11.9247 | -48.0495 | 2025-09-29 01:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| fb31cf8c-6008-3a30-8a84-e02a71a0535d | -20.0491 | -41.3251 | 2025-09-29 01:30:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.0 |
| 612b58f3-86b0-3e63-a620-44d021a234fc | -12.6909 | -46.916 | 2025-09-29 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 129.4 |
| d9760b44-a3d2-3f04-945f-0c5af28ad7bc | -12.6913 | -46.8934 | 2025-09-29 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 234.6 |
| 6f0041b7-f34e-3467-97b3-14f295b1b4c5 | -14.553 | -48.4237 | 2025-09-29 01:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 66.9 |
| e006257a-b19d-3fc6-9b11-97aad64a6491 | -7.2402 | -44.7812 | 2025-09-29 01:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 133.6 |
| fba572d6-2bf8-3750-a56c-8b92acfc5f96 | -16.54 | -45.2948 | 2025-09-29 01:30:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 75.9 |
| cb4e5bf8-7de7-3ec3-a6bf-9b3355ae3d0e | -3.1013 | -47.0082 | 2025-09-29 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 144.6 |
| f65d75a5-f846-313e-8c70-2c3821a4ec23 | -15.2893 | -49.5035 | 2025-09-29 01:30:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 06cdf54f-7b07-3f1f-87ff-0ab49d75ebf1 | -10.0342 | -50.1997 | 2025-09-29 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 42c0bfbf-5b59-301b-becd-179eb7b35d99 | -4.7157 | -41.9974 | 2025-09-29 01:30:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 61.0 |
| 26d58a02-a63c-30cd-9046-d504cf3cc5c7 | -4.7159 | -41.9736 | 2025-09-29 01:30:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 93.9 |
| 8bf3c9ac-876d-3c26-96c8-45f03e0567b3 | -9.4007 | -54.6984 | 2025-09-29 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 823b760f-ddf5-3aa9-976b-d175ae7e899d | -7.2214 | -44.783 | 2025-09-29 01:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 185.3 |
| 04d19a3e-f466-3caa-a485-6a3f036f2b18 | -4.6971 | -41.9748 | 2025-09-29 01:30:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 66.4 |
| e7657fbc-15ff-3bfd-81d9-5e10af246c7e | -14.5526 | -48.4461 | 2025-09-29 01:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 86f1d76d-46ac-3e2b-9fe4-c337e80faa54 | -4.4013 | -44.0755 | 2025-09-29 01:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 4bb2ee19-67b6-3625-86b0-b418017c915e | -17.0938 | -48.5699 | 2025-09-29 01:30:00 | GOES-19 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 78014382-9a90-34c8-bc82-ee18fb605c2e | -16.01331 | -59.50744 | 2025-09-29 01:30:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |


[Clique aqui para ver as próximas entradas](README4.md)
