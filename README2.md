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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a4b702e-06da-3867-87bc-6ad29800f399 | -18.14577 | -40.19645 | 2026-01-27 04:12:00 | NOAA-21 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ba744866-2345-3ef2-9f23-31c88dd26b4b | -21.50672 | -49.02055 | 2026-01-27 04:12:00 | NOAA-21 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a613bdb-c6cd-3fee-93d3-b2a8cea370b6 | -19.70985 | -56.82118 | 2026-01-27 04:12:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 78e83e7f-f17f-3fa5-a5db-14343035d4e4 | -19.61446 | -57.37197 | 2026-01-27 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a6350658-c787-3ae2-a4c3-a0257e3a95ef | -19.71588 | -56.82269 | 2026-01-27 04:12:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| da955ecf-f567-3d3b-9e6f-03f8a9e7113d | -20.16289 | -50.60611 | 2026-01-27 04:12:00 | NOAA-21 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 39e78c2a-1c9e-36d4-9860-87e3af49479b | -19.26708 | -49.35366 | 2026-01-27 04:12:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e10f30ac-0b77-3503-9670-f2071e7c3c06 | -19.26418 | -49.35513 | 2026-01-27 04:12:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a65fc65-89fe-3c0b-b32f-4101c91ef0b4 | -21.24185 | -49.37124 | 2026-01-27 04:12:00 | NOAA-21 | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 30c15610-eab5-3f84-ac75-ca9de6558f0f | -20.64335 | -48.83278 | 2026-01-27 04:12:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 794fdca9-93e5-37f2-ad4c-815a00abc7c7 | -19.66793 | -56.83433 | 2026-01-27 04:12:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d80c4eff-ad32-3179-a209-ca8882773b2b | -21.30586 | -49.33949 | 2026-01-27 04:12:00 | NOAA-21 | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bfabe4e4-cb06-3d13-86ec-f768e70d9cd2 | -20.16216 | -50.60994 | 2026-01-27 04:12:00 | NOAA-21 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e5445de4-bf06-39cd-8b3f-fec577e0c262 | -19.49443 | -44.27765 | 2026-01-27 04:12:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 77d7c8a1-48ee-33ea-9c5f-65261b21fcdb | -19.72191 | -56.82419 | 2026-01-27 04:12:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 4c20e9f9-34d4-35e2-86f5-58674349cd7a | -19.1053 | -57.77473 | 2026-01-27 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 784b5947-c233-3d92-bce4-650305361cd1 | -19.60571 | -57.35294 | 2026-01-27 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d12d149d-6d95-3085-b9fe-45d9ebce5637 | -18.77056 | -49.07837 | 2026-01-27 04:12:00 | NOAA-21 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 106c9497-7b5c-3438-a847-4cea2cbcbdd1 | -19.60823 | -57.37038 | 2026-01-27 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a25e8a1e-cb70-3307-ad71-60ee62b96685 | -19.61069 | -57.35982 | 2026-01-27 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 4361ead9-680a-30b5-baeb-48a19e68abc7 | -19.60694 | -57.34765 | 2026-01-27 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 004778b8-9cff-37c0-8548-e065b8b04fa0 | -19.60946 | -57.3651 | 2026-01-27 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 617c75b0-e95e-3039-8803-1885be4a3c70 | -18.15936 | -51.12424 | 2026-01-27 04:12:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 047de4f4-65f0-37d0-ba57-fedf736092ee | -20.8445 | -51.74006 | 2026-01-27 04:12:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b0146879-6a6c-369a-a947-ebd5e81cc7c8 | -19.70872 | -56.82606 | 2026-01-27 04:12:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9fdb0bc2-dfe4-38a0-99d7-320727d75a00 | -19.34374 | -54.17335 | 2026-01-27 04:12:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 367595bd-5766-34cc-b410-9ddc25b0cb4c | -19.66078 | -56.83771 | 2026-01-27 04:12:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 957ea584-344b-3ee0-8c77-1454b1173bfa | -19.70856 | -56.82389 | 2026-01-27 04:12:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 46c7fe42-3767-3ee5-b0e5-12d206feb40c | -19.10662 | -57.7691 | 2026-01-27 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7856f45e-55b5-3adc-aaa7-ba8d0212c5fd | -21.24276 | -49.36634 | 2026-01-27 04:12:00 | NOAA-21 | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 17c29e93-0984-324d-96af-6e57bd7eeda0 | -19.71459 | -56.82542 | 2026-01-27 04:12:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 672d2604-b059-3b4e-b020-f50d797efeb2 | -20.16142 | -50.61381 | 2026-01-27 04:12:00 | NOAA-21 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e2f4a164-fb11-397e-a2bf-a08046360c41 | -19.61323 | -57.37726 | 2026-01-27 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e3647738-7b91-3fe2-928e-98d6d5a171e4 | -19.71568 | -56.82053 | 2026-01-27 04:12:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 642e2a3f-7343-396f-a445-42a7517a762a | -19.34447 | -54.1699 | 2026-01-27 04:12:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8077df9e-c66d-375f-86f0-6f5afe65077e | -18.15952 | -51.12248 | 2026-01-27 04:12:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cafa077e-92bd-3889-9df7-c6e05b19e69a | -27.76304 | -50.38248 | 2026-01-27 04:14:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fd23abf4-f50c-3dda-becc-9fa8f7c1e1f1 | -21.992 | -48.41022 | 2026-01-27 04:14:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29b4e437-cac9-3995-ab38-6fd5929980bb | -23.51982 | -46.97531 | 2026-01-27 04:14:00 | NOAA-21 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 579c4b77-3631-3f9c-8910-00d4483f4e15 | -23.05353 | -49.09706 | 2026-01-27 04:14:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f32378e-a2d0-3fad-b93b-7d665fc23ecc | -23.23215 | -46.79891 | 2026-01-27 04:14:00 | NOAA-21 | VÁRZEA PAULISTA | SÃO PAULO | Brasil | 3556503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 66b5f5d9-c0c2-3718-913a-0fb427608153 | -27.09802 | -50.52707 | 2026-01-27 04:14:00 | NOAA-21 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a18d743f-2002-320a-9934-0664a085a255 | -23.98281 | -47.51126 | 2026-01-27 04:14:00 | NOAA-21 | TAPIRAÍ | SÃO PAULO | Brasil | 3553500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 50c64f1b-89a0-3cd7-b067-09d60d73a9c4 | -22.83942 | -48.64556 | 2026-01-27 04:14:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 79318ea5-a2f5-392d-b3f9-1051a74650ba | -23.55593 | -46.35941 | 2026-01-27 04:14:00 | NOAA-21 | FERRAZ DE VASCONCELOS | SÃO PAULO | Brasil | 3515707 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| af559285-6244-3004-b491-d3b018c6bd44 | -22.83865 | -48.64991 | 2026-01-27 04:14:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 0a5021fc-0fc9-3b87-abad-f3004cc2719b | -22.03717 | -49.50424 | 2026-01-27 04:14:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 58592f16-5780-3a21-a3ba-7077037da03a | -22.84297 | -48.64622 | 2026-01-27 04:14:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18736b2a-c700-31bd-95d8-a4fac38542c1 | -20.30384 | -57.82635 | 2026-01-27 04:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| af1208f4-3a46-3f4d-82e2-5816392adaf3 | -23.98347 | -47.50732 | 2026-01-27 04:14:00 | NOAA-21 | TAPIRAÍ | SÃO PAULO | Brasil | 3553500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| faa300d7-9e62-3ce0-bbac-ec24cd618291 | -22.30973 | -47.15902 | 2026-01-27 04:14:00 | NOAA-21 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00d30303-f1bc-38ec-9c5e-d143168067b0 | -27.45778 | -48.45364 | 2026-01-27 04:14:00 | NOAA-21 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4843b1d8-82b9-33d2-b857-37d34a8bdf68 | -25.0009 | -49.33933 | 2026-01-27 04:14:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a4ab6098-8263-3d1a-b92b-e0bfb42c0a69 | -27.77188 | -49.72967 | 2026-01-27 04:14:00 | NOAA-21 | BOM RETIRO | SANTA CATARINA | Brasil | 4202602 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fb6c22fb-e1f1-3e13-9c36-abdb77e7a648 | -22.7333 | -49.34574 | 2026-01-27 04:14:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f0af914-9699-373b-ad32-f894fe5ab00d | -20.91792 | -56.37049 | 2026-01-27 04:14:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7b5b46f6-1d50-32ef-9098-f76cc27afd15 | -23.57246 | -51.54264 | 2026-01-27 04:14:00 | NOAA-21 | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 856a3c1a-b20d-3b95-bfb4-cf291684f1b0 | -20.92369 | -56.37181 | 2026-01-27 04:14:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e2a76d5-158f-3624-98ff-c30bfe9d5bcf | -22.73415 | -49.34105 | 2026-01-27 04:14:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9d2b33e-f6cb-3aba-88c6-2837235656c2 | -23.34826 | -52.20488 | 2026-01-27 04:14:00 | NOAA-21 | SÃO JORGE DO IVAÍ | PARANÁ | Brasil | 4125308 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9f86fbbc-4a77-369d-b914-fe89beca5159 | -22.83788 | -48.65426 | 2026-01-27 04:14:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d1bc4b2-bf75-343f-8657-0f20b3a4b591 | -29.67661 | -49.97461 | 2026-01-27 04:16:00 | NOAA-21 | CAPÃO DA CANOA | RIO GRANDE DO SUL | Brasil | 4304630 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| 4b8cf01f-9ad6-3280-90aa-b3290f6b6501 | -19.7246 | -56.8198 | 2026-01-27 04:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 51.5 |
| 00e6f772-5ff1-3be2-9846-481fd70cb562 | -8.15883 | -43.18837 | 2026-01-27 04:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 59129ccb-dcd8-304d-94a4-43a461b934d3 | -9.28733 | -43.15343 | 2026-01-27 04:38:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d9e2c76d-de19-33c8-ad51-0dc7a51b52c9 | -10.57289 | -49.73083 | 2026-01-27 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff9dfb29-4e04-310e-9d77-673eba7aee76 | -14.86912 | -45.19406 | 2026-01-27 04:40:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a34572a7-20fa-3c64-8110-9d1daf1b1f22 | -15.85255 | -43.50699 | 2026-01-27 04:40:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 45273720-279c-348d-8bfd-bfe4a49d84a0 | -12.09405 | -43.77436 | 2026-01-27 04:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e2290c9-dc15-34e6-9667-3ed7ae4133a2 | -11.61278 | -42.05672 | 2026-01-27 04:40:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e199d573-1d0f-3996-8c1e-64d68073a023 | -14.80569 | -48.75905 | 2026-01-27 04:40:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da3461de-8908-31ac-b8d6-3f07a8f76cde | -12.35074 | -47.89811 | 2026-01-27 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0019c7f6-9627-3e75-86ce-1c36a557cf3a | -12.35357 | -47.90232 | 2026-01-27 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc9d9ad9-f7a6-355f-8cc7-10427a08f783 | -11.40228 | -48.44218 | 2026-01-27 04:40:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b50dba1e-f8fa-366b-8de5-45b5d58b7887 | -8.7229 | -48.32656 | 2026-01-27 04:40:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ddff744-a71e-3448-acbc-38e36f95e6fa | -11.40284 | -48.43862 | 2026-01-27 04:40:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ffd8392-45ae-3a52-9070-6e0a9ce463c1 | -10.10219 | -47.55186 | 2026-01-27 04:40:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3121a24-f4e7-3f62-b1d1-b7cb19b440c1 | -10.56954 | -49.73028 | 2026-01-27 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d2dfbf4-d281-3677-9d16-1bd5f7f696f1 | -10.56897 | -49.73383 | 2026-01-27 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59d9c7d2-64a7-3dd2-b61a-c7c7ca596069 | -15.85013 | -43.50816 | 2026-01-27 04:40:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3d21fadb-95e4-33a5-96c5-67a1ea80c570 | -10.34935 | -44.83327 | 2026-01-27 04:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad0a14a9-494c-3355-8edb-09ba2ad7e396 | -12.35413 | -47.89864 | 2026-01-27 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8a683dc-9aa6-3f27-b684-9629a1f13c92 | -10.57346 | -49.72728 | 2026-01-27 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3e7e467-3a04-3620-875f-e1355d94ddfd | -14.87113 | -45.19307 | 2026-01-27 04:40:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54b6d54e-a796-3133-ad70-fd84587ae613 | -11.60747 | -42.06097 | 2026-01-27 04:40:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 249c96bb-0ddc-37ea-b5a4-b09259eb4f8b | -10.34554 | -44.83269 | 2026-01-27 04:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 778e8913-511f-3ea0-9cca-215784f866a5 | -10.89115 | -48.51718 | 2026-01-27 04:40:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0d331a2b-6440-3e94-851a-c7148b307fad | -11.39949 | -48.43808 | 2026-01-27 04:40:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36f9cbc4-f66f-3247-a39b-cc263ea3fd3a | -12.08988 | -43.77381 | 2026-01-27 04:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13640bd9-3eeb-36cd-84d5-9bc0ec88b7cd | -20.92187 | -56.37059 | 2026-01-27 04:42:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 405632cc-59a8-3f3a-bae9-e16bb6279691 | -21.03069 | -49.56896 | 2026-01-27 04:42:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 011a3487-2e7c-3cc7-b1d3-d8df78f2c0de | -19.60869 | -57.37131 | 2026-01-27 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d11a790c-d670-39b0-baad-910cd7bd8bad | -19.68697 | -56.92616 | 2026-01-27 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 95212d11-e5b1-3b04-a415-b6b9e492821e | -19.60775 | -57.35344 | 2026-01-27 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e16d43ec-f622-30ea-a950-1e879e4d025e | -19.6113 | -57.38073 | 2026-01-27 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 782bd358-4d23-300c-9baf-283b8c7e79df | -19.60942 | -57.34498 | 2026-01-27 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 60f6028b-e91f-3b28-9136-9e8c6cfcdac7 | -19.69215 | -56.82622 | 2026-01-27 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 018c47e7-287d-3eaf-bfb7-78ceb3e0ac64 | -21.79249 | -52.73067 | 2026-01-27 04:42:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f93b541f-9da3-390b-93ba-63c1aa4a3b68 | -19.68677 | -56.92388 | 2026-01-27 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 22d2c9c6-96b8-3447-af75-61fd6b5c28dd | -19.6644 | -56.83664 | 2026-01-27 04:42:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |


[Clique aqui para ver as próximas entradas](README3.md)
