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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3dd83747-bdb4-3bee-a41c-0494a7166081 | -7.49123 | -45.79536 | 2026-10-01 06:48:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 897e1a79-3d29-3513-9a96-ba2fcde80e4f | -10.55752 | -50.03005 | 2026-10-01 06:48:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 0edc3f76-95ed-378a-8bfd-e9d4ae292a57 | -4.31278 | -50.78275 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 1d72ee1e-5112-36d9-a7c2-9ff835480ac3 | -4.27721 | -50.73901 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| ed42111e-6494-3e0f-a078-78307981461a | -11.17103 | -45.11584 | 2026-10-01 06:48:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c273fd2c-9a95-33ee-9627-aba265abef3b | -6.00423 | -49.55993 | 2026-10-01 06:48:00 | AQUA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a652e500-515d-31d0-8948-4242a61cff07 | -10.83543 | -48.70623 | 2026-10-01 06:48:00 | AQUA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 83e8695d-0b1e-331b-a8b9-fd4667d2791e | -3.29379 | -53.85712 | 2026-10-01 06:48:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| b0895b5e-b5e4-3b06-9d18-c2b048df40b0 | -7.0314 | -50.73253 | 2026-10-01 06:48:00 | AQUA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| daa63644-1ef4-3204-9a9f-758b56de41be | -4.62622 | -50.60508 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| cf1d9482-5cf9-3121-9323-19c64266b227 | -7.50396 | -45.83632 | 2026-10-01 06:48:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d34742f8-26e4-3d4a-b3e0-c7d9ff6fe972 | -7.01904 | -47.53738 | 2026-10-01 06:48:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 36929ab9-43f3-3543-afc7-27c2465eb704 | -4.26296 | -50.76234 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| e636129b-e913-350b-bbdf-a0f7eba74b2a | -8.76452 | -44.90555 | 2026-10-01 06:48:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 00a8abf7-0ed4-3044-9e59-73a0d76e88fa | -10.12659 | -45.12296 | 2026-10-01 06:48:00 | AQUA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| f53f1d4c-ac49-3941-b474-3bc5285286a6 | -4.29207 | -50.77954 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1112.1 |
| fdb87aff-27f3-3465-9e80-3ab5bb2ee927 | -9.21583 | -45.81509 | 2026-10-01 06:48:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 85f082d4-b5cd-3a68-92c6-4507e077cff2 | -4.62759 | -50.59951 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 31c78d7c-38ca-3923-9378-069a5b2307b4 | -6.26683 | -43.26186 | 2026-10-01 06:48:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 82b22c6e-b6de-3b40-b9b1-f5279a4bd26d | -4.28754 | -50.74057 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 57d61f58-02c0-332a-aaa6-a1049fc2f52c | -7.84852 | -45.8259 | 2026-10-01 06:48:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| eef94039-f8ff-3e95-bdbd-495d4ec54b2a | -4.27525 | -50.7515 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 8afbfbd3-9a5c-3aeb-886b-b885d56fa312 | -4.03628 | -54.21757 | 2026-10-01 06:48:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 97dd124a-015d-3064-aecc-f27554a6c8ec | -4.24619 | -50.73449 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 7c6a2600-2ced-3c36-8e2d-a1b0915ae64e | -4.25902 | -50.7873 | 2026-10-01 06:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 73a9570f-c754-34a8-812d-3c62e50afe76 | -4.27332 | -50.76384 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 150.3 |
| 2b50f175-3fcc-3a20-90e1-79b8c4f30aa4 | -4.29593 | -50.75465 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| b92e8416-776b-3de4-8c81-14bae78d1b49 | -4.25458 | -50.74833 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 154.4 |
| 5757771b-ed04-3bd1-9c45-3dba6a7a939e | -4.03868 | -54.23717 | 2026-10-01 06:48:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| db43dc86-2cb5-3a32-b670-cf7aed2f6322 | -4.25259 | -50.76087 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| d13f0997-09e3-34cf-bc72-641fa74ea53a | -4.25653 | -50.73599 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 31e76069-e1da-3fcf-83a9-477a72dfda0d | -4.30243 | -50.78112 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 77598f83-f4f7-34f3-9aa3-027daf965524 | -4.28559 | -50.75309 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 34fc1308-057f-39cd-ab0f-d67e859452d9 | -4.30049 | -50.79367 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2532e92a-3022-3a6e-b178-598b63663a3f | -4.05757 | -51.10012 | 2026-10-01 06:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| b7558908-7001-3310-95bb-4938a6dbd6e4 | -4.29012 | -50.79209 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| f7ef7683-9926-3588-a1f6-b5169c5a3f99 | -4.63451 | -50.6184 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 109c63b5-cd4d-3d3f-9118-ecae86a9fa08 | -4.45475 | -47.91468 | 2026-10-01 06:48:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 3505698b-8828-3cbe-a186-279d0d2355f6 | -6.27742 | -43.26337 | 2026-10-01 06:48:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| be25f3c6-043c-3f29-812b-907e7f6d92f0 | -4.28365 | -50.76553 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 498.5 |
| 3352d1ca-e081-3759-99be-e11559dae6ec | -4.8843 | -48.37646 | 2026-10-01 06:48:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 469f7f13-2844-3b33-b1a4-b7137ee552fd | -11.20135 | -45.19767 | 2026-10-01 06:48:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 799b6a19-27bd-3afc-a3c9-f8b2a549500a | -4.88571 | -48.36737 | 2026-10-01 06:48:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 3edb17ab-1aa8-310b-8c45-a41e45f763a2 | -4.26097 | -50.77491 | 2026-10-01 06:48:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| b31941b6-f1a4-3049-b5c5-058070aad10e | -15.15436 | -46.12287 | 2026-10-01 06:50:00 | AQUA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 79497c5e-7761-371a-ae1b-c7d3908c77e9 | -14.40204 | -51.24224 | 2026-10-01 06:50:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 3b93a762-3149-3145-abfa-311f324bb3cd | -14.42595 | -51.25287 | 2026-10-01 06:50:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 4367397c-42ca-3ee1-b5a6-958dd3a6d2d8 | -14.39725 | -51.27237 | 2026-10-01 06:50:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 91e819c6-0591-3c50-ac7b-4c19a3d29883 | -14.41126 | -51.24378 | 2026-10-01 06:50:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 29.5 |
| c7bc203b-8c64-32c9-8d8f-9453a99f3558 | -13.53563 | -49.19239 | 2026-10-01 06:50:00 | AQUA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8648998a-ae94-3897-8f56-3768ee9f59ee | -14.42049 | -51.24533 | 2026-10-01 06:50:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c679c0c9-1e08-3639-b4a1-7dbb5cbdfdda | -13.53699 | -49.18341 | 2026-10-01 06:50:00 | AQUA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a9531ef1-07ee-31cf-9dc1-5be48946f430 | -14.38199 | -51.2492 | 2026-10-01 06:50:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 121.1 |
| db52b193-e2ba-3c7f-bd23-f8e463894d6b | -14.39885 | -51.26232 | 2026-10-01 06:50:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 2aba879f-cf02-3c48-b1d8-2eba57cac894 | -13.38813 | -46.82308 | 2026-10-01 06:50:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 76fa853b-9aa3-3320-a1d0-1b0f4835d9d9 | -15.1528 | -46.1342 | 2026-10-01 06:50:00 | AQUA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f088da0e-7d8a-3c4a-9417-475809f50d79 | -10.76168 | -52.12785 | 2026-10-01 06:50:00 | AQUA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 12c1ded7-4ad8-3d38-a954-5b20bac43cfc | -13.64857 | -53.92762 | 2026-10-01 06:50:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| ffcd47a0-c769-3533-8de0-97db5d10b6ff | -14.43679 | -51.24439 | 2026-10-01 06:50:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 28.8 |
| a620b0ec-dbad-3e5a-bf1b-f415076a464f | -13.65974 | -53.92943 | 2026-10-01 06:50:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 37bc36e7-2d00-3441-b5e9-00205605525f | -14.48329 | -48.30468 | 2026-10-01 06:50:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 32182a55-19bf-319d-824c-70d5daffd467 | -14.42757 | -51.24285 | 2026-10-01 06:50:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 47d543a5-9a12-3ebc-a53c-0cbb2de49049 | -10.75543 | -52.12016 | 2026-10-01 06:50:00 | AQUA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4e73c825-70ce-3bd6-add8-3a8e63b2f787 | -14.49212 | -48.30616 | 2026-10-01 06:50:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 69038428-4c43-3d2f-ae5a-3e5151eb5286 | -14.14522 | -46.23568 | 2026-10-01 06:50:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 383473b1-ee3f-3846-9dfa-4d159d9bca87 | -14.43517 | -51.25441 | 2026-10-01 06:50:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 18ec35b6-06f7-31a5-b3a5-6afae071afc3 | -11.32481 | -50.95962 | 2026-10-01 06:50:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 75c96e81-dbb4-3fc4-b263-a544eb9e47a7 | -12.18496 | -48.42381 | 2026-10-01 06:50:00 | AQUA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3d8a2b84-2a0f-3f94-aded-58aa4c2fe4cb | -11.40804 | -51.02163 | 2026-10-01 06:50:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a69b1a13-8a0f-316a-b26c-6de38d2e99f3 | -12.19239 | -48.43407 | 2026-10-01 06:50:00 | AQUA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d1aa2de5-8da4-34ae-ba6d-3f73b55e35d4 | -11.31954 | -50.96272 | 2026-10-01 06:50:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 401048d5-dc5d-3a96-b891-19778df59d41 | -13.64601 | -53.94254 | 2026-10-01 06:50:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 98f029a9-ec0c-330a-a8dd-fc3524508743 | -12.18362 | -48.43273 | 2026-10-01 06:50:00 | AQUA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 215da0b0-7b50-351a-ba6d-a436d69a0ce6 | -11.40146 | -51.02551 | 2026-10-01 06:50:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f0d24ddf-6460-3698-bc9f-894f0f0675e5 | -13.65717 | -53.94445 | 2026-10-01 06:50:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 35fba148-5d8f-3214-8481-84bc2f6a29eb | -14.41614 | -51.31318 | 2026-10-01 06:50:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 00b5c7af-8fd9-350a-b03b-d5b365b33bbb | -14.39122 | -51.25074 | 2026-10-01 06:50:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 8e191c6a-1f32-3860-81d9-52d998947436 | -12.85619 | -44.33304 | 2026-10-01 06:50:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| e320d953-d72d-3952-8603-fcdeadc4b301 | -14.4189 | -51.25536 | 2026-10-01 06:50:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 78e93058-6a83-3d54-a219-c92c7a13e808 | -14.44439 | -51.25594 | 2026-10-01 06:50:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 37.0 |
| f580a965-0394-3abd-8649-69702a509c55 | -15.30138 | -42.76941 | 2026-10-01 06:50:00 | AQUA_M-M | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c89842a0-78d0-3290-bcd6-52565e6e45cb | -13.37736 | -46.83223 | 2026-10-01 06:50:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b3be6755-8e01-3ecf-8383-ce34997e6cf7 | -11.2818 | -50.95657 | 2026-10-01 06:50:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 7ed3f46d-a162-3616-9d0d-184b86e61e60 | -14.40044 | -51.25228 | 2026-10-01 06:50:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 5f7f0c2a-9799-36a8-a16b-484d6aac2cdb | -12.85808 | -44.34021 | 2026-10-01 06:50:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 01eb5165-a830-3baa-b578-63c4c6651e01 | -14.40967 | -51.25382 | 2026-10-01 06:50:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 1f765133-711f-39db-82ab-4264c9bb7740 | -14.38962 | -51.26078 | 2026-10-01 06:50:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| f552dc6c-a045-3de7-b7c8-eac8662ad831 | -11.28014 | -50.96699 | 2026-10-01 06:50:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 19b717a4-9a51-399d-80f6-1ff7b2a5954a | -14.44601 | -51.24593 | 2026-10-01 06:50:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 0ce30189-51e4-3c9b-b976-1f1a2bdc9a61 | -14.38038 | -51.25924 | 2026-10-01 06:50:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 146.6 |
| e887d55e-a667-3476-94d9-0267ddb82860 | -14.39282 | -51.24071 | 2026-10-01 06:50:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 07a06a35-8356-3393-9e87-dcb3f4bb4e6c | -14.41778 | -51.3031 | 2026-10-01 06:50:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9ba4827b-d20a-3724-abe8-cf8bde66382d | -14.86115 | -51.84347 | 2026-10-01 06:52:00 | AQUA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7e2cb966-1aae-3064-8103-c9fb848a3f83 | -18.87044 | -43.81139 | 2026-10-01 06:52:00 | AQUA_M-M | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f81d0cfd-74b5-324c-a960-765203498ac8 | -14.87974 | -51.87537 | 2026-10-01 06:52:00 | AQUA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 917f79fd-44da-3bf5-a657-2152e7b606ce | -15.51035 | -46.1377 | 2026-10-01 06:52:00 | AQUA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 454f9182-d66e-3180-8539-72a92937be33 | -16.43391 | -47.17408 | 2026-10-01 06:52:00 | AQUA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6c55e076-e290-3e55-bcd1-8c1d41bed45b | -14.87799 | -51.88601 | 2026-10-01 06:52:00 | AQUA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 17c15b85-e7f8-3ed6-b0ab-a80b6c5a4443 | -14.3838 | -51.2677 | 2026-10-01 07:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 132.5 |
| fa2a9697-f218-35d7-9dc2-16180c6b9fae | -14.3841 | -51.2462 | 2026-10-01 07:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 162.8 |


[Clique aqui para ver as próximas entradas](README93.md)
