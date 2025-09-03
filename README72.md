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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95822e10-b855-3485-a0fc-7fafa0908476 | -16.54629 | -55.07473 | 2025-09-03 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| bc298cdd-8f9b-3de4-b24e-760bf3d93329 | -11.6584 | -57.35578 | 2025-09-03 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8863cc68-3a62-3de3-9395-54091204a72e | -13.51603 | -47.02203 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a2d4b20-cda0-3806-a6ea-cd23cf2508cd | -15.19261 | -52.34383 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 652b10c5-2fd5-3008-9330-08bf1efba9d1 | -16.15269 | -49.49535 | 2025-09-03 04:49:00 | NOAA-21 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d0c68fa4-7b1e-3964-af49-f0bd44330cc7 | -14.4064 | -51.70529 | 2025-09-03 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05c87754-c1c8-38d8-97b4-aeaeac47fe53 | -14.06063 | -44.5633 | 2025-09-03 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f822666b-5a7e-3668-ba3d-c4dfbefefc2a | -15.56154 | -48.41358 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3da6e216-5315-36ef-8bd8-ea108d6b2e01 | -15.01259 | -50.06677 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83f28687-b068-33d7-86fe-dc08c0fc8f9f | -13.49443 | -46.82267 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7561989-c602-3b01-8513-594264d9e1ec | -13.00224 | -48.10881 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a7434263-3a0f-3489-9df2-d34a0529d5cb | -14.5814 | -54.53513 | 2025-09-03 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54c107ef-1dd3-33ca-a164-3e630b3b849c | -14.84632 | -60.04361 | 2025-09-03 04:49:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a465057-576c-3f67-ba65-f1185a092f79 | -13.90606 | -48.11036 | 2025-09-03 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 51c1d48b-7fc4-3022-af46-e0787cb2fe86 | -15.11553 | -48.15955 | 2025-09-03 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| abd0b243-1a2e-3162-94b1-d440f6c3ff56 | -14.56069 | -53.04574 | 2025-09-03 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72593622-327e-393e-895c-03256d569f02 | -15.75302 | -53.68178 | 2025-09-03 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e1dd1e61-3e5f-3caf-84ac-96e17d113411 | -12.89348 | -48.05609 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| aaf85296-b236-3b39-83a0-f1aa463a0165 | -12.93324 | -56.94851 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 50462195-bcee-32d3-9f39-aa2d51f58fb3 | -15.14884 | -52.3625 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e27a5143-273d-35ab-977e-bac2a973abc6 | -15.60317 | -52.67941 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be5d9a0f-52ad-32dd-ab36-76fa5b921a15 | -15.55441 | -48.39873 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| af95f28d-a5f4-3eda-9190-880740ba7ab6 | -14.80368 | -48.21943 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1eaa8f4e-b2d9-3d07-8064-dcd14059b361 | -13.00125 | -48.11127 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a8b4045d-254d-3966-ab50-492382f31d34 | -12.89812 | -56.9474 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4fd7cfeb-834c-30c2-99c1-d4ed6971c936 | -15.24082 | -53.80143 | 2025-09-03 04:49:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 657b78da-8d4c-3f4f-9eac-bdee284d5ba0 | -14.89691 | -46.93042 | 2025-09-03 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7bf8c1fd-df51-351d-8aff-68d3b73b6e59 | -12.97605 | -48.09251 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b5854e4b-4e81-3e93-9c91-7ed9396574dc | -15.55072 | -48.37468 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 533c5541-1b64-322c-9d09-e7729c715d0e | -15.17613 | -48.01426 | 2025-09-03 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dba9acb9-f990-3846-b65e-d95c16bd1cc4 | -14.63837 | -48.93965 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d84709ba-a9d0-3671-94f9-b664ad30ab9e | -14.27051 | -51.23342 | 2025-09-03 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72f5c0e0-1c1e-3f52-b357-b4a07b2d0ecd | -15.55324 | -48.38576 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ac68321d-37bf-35f9-a1bf-e99d9eb6d8cc | -11.86081 | -51.46636 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 357745b1-5dcf-3105-9e90-163fd9af5f83 | -12.90769 | -48.09809 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5ac8f447-cc15-3cdd-8d6d-5eb632ab5b09 | -16.29443 | -52.9581 | 2025-09-03 04:49:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92197c06-a3a3-35c2-9c72-fa0cd83f9d8b | -13.29476 | -46.83593 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| df7db543-6893-3f94-8ce3-177ac2374ad2 | -11.82773 | -51.57059 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73a7dafb-85b7-3f9b-b8d6-b75653501699 | -13.51182 | -47.02145 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d6b4406-6406-36eb-b302-641afb5d6e85 | -15.55965 | -48.42036 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c02375d3-c60e-3d9c-832b-17055fd6a860 | -12.91741 | -56.99549 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8c93cc14-87a9-3900-b180-04d3509ae187 | -13.72808 | -51.94374 | 2025-09-03 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1cf60300-3817-36e7-998b-9d43ba2bbbaf | -16.8506 | -52.11543 | 2025-09-03 04:49:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 122ddd25-f520-3915-bbb0-628e50407e47 | -15.559 | -48.40273 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d9de396a-5b19-3f52-afd9-c1c024b9f050 | -14.59136 | -48.04298 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c41ca6bb-da55-3dcd-a47c-2346c0baf7dc | -14.83704 | -46.69264 | 2025-09-03 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 3188237d-99f5-3d9a-9a11-a6f4165e30bf | -13.34747 | -51.74009 | 2025-09-03 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0cb36ef8-4e25-38ec-a0d1-7e7aeb2d458e | -13.00158 | -48.11372 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c790355d-2b4d-33ce-b97f-bfa2ed679976 | -12.61164 | -57.0013 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 827f3762-ec8e-3ff4-95a1-46f1c26651cd | -12.92131 | -48.08564 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 197b56bf-9d13-3a9c-8f70-bfea4a4e601e | -12.99277 | -48.11501 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1c46ce44-ce72-36e6-a9c9-1a17806df5aa | -15.56361 | -48.42093 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c929cc8d-7804-3382-aeeb-a8af29613e4d | -12.93931 | -56.95295 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 287d1aaf-6aee-3308-86ec-e32af346d22e | -12.75692 | -47.67445 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4cdc4fef-5568-326b-92e5-87945305236c | -12.84453 | -48.03094 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 778a97a7-f6d4-33d7-ada8-6ced613b027b | -16.82255 | -52.14147 | 2025-09-03 04:49:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9da8a3d-0f87-3405-9dd7-705c4d5a06a6 | -12.49584 | -47.48192 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0bbada8-970c-32dc-af1d-2db27e2fec78 | -15.56427 | -48.41589 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 54c97b83-42b1-3c07-8791-e63f54cbacc9 | -14.57562 | -54.54938 | 2025-09-03 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dd8c5f47-f3b9-32cc-8d6d-6b2ebc45d05f | -13.31206 | -51.79734 | 2025-09-03 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50778908-564e-3e4b-8d5f-33f90a3b8c33 | -14.51988 | -53.23857 | 2025-09-03 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bfa85763-59b1-3240-9d5e-1e43e24f58a9 | -15.1444 | -52.34695 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5342ab4d-736b-3d29-aba7-37213209d96f | -12.94652 | -56.97904 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 343b0de7-4f9e-3c0f-8605-0ae06ef83a3a | -12.94948 | -56.98455 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 482eaaa9-9f30-3175-9553-0d6c4dad4bc2 | -16.29388 | -52.96169 | 2025-09-03 04:49:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aad7e3ac-fa3c-3ac9-a26e-199586987717 | -14.54926 | -51.9483 | 2025-09-03 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3323169-4ae5-3589-80ab-4263fa0203c2 | -12.92506 | -56.99678 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1585212-672e-34d2-97a2-47be88c9d6dc | -15.02874 | -50.05609 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d50c523d-6ee6-352d-b3ad-ac099b5b3a56 | -12.91038 | -56.94456 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 93602d40-15fa-36c6-9483-8393d3ee69d2 | -13.45968 | -46.92584 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f369f39f-267a-3a84-8028-c00939e228a0 | -14.98137 | -50.21122 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8251042c-665e-36b9-84db-0ac03fc9098e | -12.62569 | -56.98882 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f869bf9-3767-3887-83b7-6172457e61f0 | -12.41416 | -47.49977 | 2025-09-03 04:49:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed81eec1-3771-3407-bcfe-98fcafc69095 | -15.17663 | -48.01059 | 2025-09-03 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f0dee71-c925-3dd4-9a42-778e9c31e8ce | -16.59305 | -48.98081 | 2025-09-03 04:49:00 | NOAA-21 | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa78b862-4bb7-3764-a5bb-f319e0227e3c | -16.80676 | -49.20334 | 2025-09-03 04:49:00 | NOAA-21 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 516fd9e5-32a9-35d0-ad58-212a69698e45 | -11.53023 | -54.40658 | 2025-09-03 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8cb830c-3422-3bbe-86ca-a4d7c40216b3 | -17.92004 | -47.21291 | 2025-09-03 04:49:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61db29a1-d29e-326d-8c22-6140c50a9848 | -13.00329 | -48.09684 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 967f7e9a-2eea-39b5-8e0c-e76eb10ca065 | -12.97328 | -54.75864 | 2025-09-03 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f4b1da0-cfb6-328e-ad80-c52e62d7a8b5 | -11.85666 | -51.53495 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ff0eb65-def2-340d-8c83-20b808fef5ad | -12.99769 | -48.11313 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 08072cd8-539e-3285-b67d-325fad2c5b29 | -15.55903 | -48.39425 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e7e2b9b8-a680-3c51-8db4-54ce48147a08 | -11.66527 | -57.35347 | 2025-09-03 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a2312b2-254c-3787-9bd9-264059fe5787 | -14.60477 | -48.03431 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 389911b8-49e4-31e3-977d-f75add6b6434 | -16.53618 | -55.07291 | 2025-09-03 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ed7f62e7-25ca-3d5e-bf55-c389f2ff215c | -12.98762 | -54.75718 | 2025-09-03 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03f028bd-05b0-3e9e-b428-6da26fc870da | -11.86169 | -51.54666 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3faf079-3282-3144-ace7-475fe98697ed | -15.14549 | -52.33977 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5ef926a-3be6-3421-ab19-0e2832930c8c | -15.54819 | -48.36354 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cace1b2d-72e8-3509-9b72-2ab93c69197b | -14.61457 | -48.02222 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed1b8264-ade2-3e39-9169-15989cbaee14 | -14.98195 | -50.2071 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d24bed7f-044d-33fa-a2ab-3413938c7207 | -12.97544 | -54.76685 | 2025-09-03 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bdb016c9-6851-3552-9a32-9ee13104bedf | -11.85945 | -51.53904 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c7f3fff-ae13-33af-80d4-42841ad66ecc | -14.59834 | -54.57987 | 2025-09-03 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30984b3f-c8b8-3ef0-a31e-fd7e6ce2fb73 | -13.28159 | -46.83734 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b5936c8-c51f-3623-a88e-00fdae134bef | -15.55647 | -48.39172 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2a19de32-4824-340f-96e0-a5fe0051a9bd | -12.88957 | -48.08511 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17cbc5b0-dfa6-3a2e-b740-61785d0b15b1 | -16.3951 | -50.40406 | 2025-09-03 04:49:00 | NOAA-21 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e9372326-5db6-3ff7-8a9e-36e6177e2a79 | -12.92805 | -57.00232 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README73.md)
