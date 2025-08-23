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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8dc54b4f-0a8d-30be-8d02-085b06c010c0 | -9.52616 | -60.52438 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ce5151f7-25b6-3171-b86b-217eeef0593c | -9.21811 | -60.79282 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15c087b1-fe56-3caf-a75f-94c27456a384 | -9.24336 | -60.47766 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7fb68053-d3fb-3828-9484-0b699703a625 | -9.8426 | -64.29174 | 2025-08-23 05:42:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df6f0b29-f077-39a8-900f-9cd303f80a9a | -9.21128 | -59.63475 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4a880a41-e3ca-3e68-b6ed-5445de0f5bb3 | -9.95278 | -60.18198 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 58f89e20-2c04-30fe-aefd-edd4409e0aef | -7.8118 | -63.56362 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9dd99b4-5b5f-3815-8983-249d4efdab8d | -7.42775 | -60.59872 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bdc5a1f-a5e4-3926-ba90-543a4e19733d | -9.18104 | -59.62592 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16108a47-6233-39dc-83b4-8eddca75a3d1 | -9.20891 | -59.45525 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f36afd28-1ac1-3fcd-adc8-fb33153e29f2 | -9.20179 | -59.44068 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 18960db0-a056-3b0a-bff9-92eb5ab233cf | -9.18743 | -59.64479 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 551cb881-9891-3e5f-94ce-a34935d3934d | -9.95763 | -60.17847 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 3082abcb-52d4-3f05-ab56-ee4b155fdb95 | -9.21543 | -60.78551 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d41aefea-be10-36ac-a623-e82896008388 | -8.69186 | -62.86876 | 2025-08-23 05:42:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50f592e0-cb31-388a-9844-bb4c4d4e2ea4 | -9.20057 | -59.44961 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 23ef4b6a-5879-3fb2-9705-69bbcfa667d3 | -6.57666 | -59.87862 | 2025-08-23 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fae31b9b-b8f9-36ac-9fc0-faf3e17eb354 | -9.20565 | -59.44574 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 308573f6-1f38-38b4-9485-68fb47bb83cb | -9.10462 | -61.4297 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 27970f06-b365-35af-8831-d76308b4fe38 | -9.524 | -60.53962 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 698252ca-1fff-3120-84b0-f9a0c33c6000 | -9.16577 | -59.60595 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6bb2b07-641a-3356-a740-d423f1424e11 | -9.25026 | -59.61356 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 943e4cbd-71fc-3c91-9b6e-9c335f33042a | -5.75076 | -57.58833 | 2025-08-23 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 1278d635-f48b-3ee1-b776-47d66be782d1 | -5.43416 | -60.16463 | 2025-08-23 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa13591c-38bc-31ed-8983-1787bad7a79d | -6.57249 | -59.878 | 2025-08-23 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 26cbd412-95a2-31e5-8382-d960267c57fb | -5.87772 | -57.75593 | 2025-08-23 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 71321e26-2367-38fd-acaa-ba5bd55e52ed | -7.51137 | -63.83253 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9699f700-0767-36e9-81af-72ef0a455378 | -7.55681 | -63.85462 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b7352ae-6914-3608-8a08-e8ff85d60188 | -7.79195 | -61.57963 | 2025-08-23 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a799731-cb56-3ea7-a232-633e5620c596 | -9.71837 | -65.71316 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05235bd5-f1d9-328a-b038-9089cd35ba2c | -9.65379 | -59.64575 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ecc67cde-74eb-34eb-bbb1-c2a868aed22e | -9.52239 | -60.55104 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 319e4c77-7675-326f-af0b-39229ced5325 | -9.17358 | -59.61775 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c955e1db-9365-37be-a252-c65b029d8dca | -5.87303 | -57.75758 | 2025-08-23 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 29d9b39d-dec7-3661-8b33-711578d7d814 | -9.95383 | -60.18768 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 695a65d4-b6c8-3ee7-aec7-7a08db925536 | -9.1918 | -59.45954 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1412e73-ca4e-338f-bad1-82e8408438d4 | -6.57361 | -59.87025 | 2025-08-23 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7e4cf247-8310-3f26-b371-a4ddaf320125 | -9.19103 | -59.61866 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 85085049-a8a3-33bb-a1e3-b4c28e8d579d | -7.73208 | -67.07217 | 2025-08-23 05:42:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5426ea99-48e1-3534-9f23-738bbb16bf8c | -9.25467 | -59.6142 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1edb0a27-f4b1-3236-945d-b660717ae3e4 | -9.94155 | -60.18177 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e975a8db-d637-3218-93b3-ceef92dd4e8c | -9.16194 | -59.60096 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b7dc8967-df52-3466-a4ee-88eacb484442 | -9.19121 | -59.64991 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 326bc576-dc5d-3132-9e31-d34e6e546c04 | -8.97403 | -67.73999 | 2025-08-23 05:42:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94ac1e73-7b24-3b4d-9b19-78cbaa02e478 | -9.2428 | -60.4815 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7d9bc992-d42c-344c-8e56-2b7606f0e04c | -8.92122 | -60.7219 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1987d244-a3ea-3737-ae15-1f00a682fa78 | -9.96024 | -60.19143 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| f7e50cbb-0b33-340c-82ce-d7c4484607c7 | -5.73962 | -57.59736 | 2025-08-23 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 733aa5e2-fa6d-389f-a80a-398e789a630a | -8.99804 | -67.72118 | 2025-08-23 05:42:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d937ace8-8801-3514-a7a5-193503b4a745 | -7.54943 | -63.85725 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 619b2250-9e2f-340a-b70a-535530663405 | -7.02504 | -59.9107 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6656a488-d63e-3f5f-8dfe-29a55594c8c3 | -9.2133 | -60.80008 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a0fc6fc-43e1-34a6-93f1-4b0bc3df250b | -9.16849 | -59.59053 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6237da67-2789-323b-b5d3-b962975536c7 | -11.185 | -55.02273 | 2025-08-23 05:42:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 29151a5b-3b56-3af6-9a47-0a3e4c390282 | -9.21301 | -60.79959 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 301a8ed6-73a8-3496-b64d-87f2a09d1e73 | -9.83862 | -64.29494 | 2025-08-23 05:42:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d5b4d14-c938-3581-b176-4aba4cb1e956 | -9.15463 | -59.59293 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5d2208b-b979-3a2f-aabc-063304c1d6a8 | -8.88045 | -62.40817 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 381d7e51-b8a9-3e3c-bffa-15741fd2baa5 | -8.86373 | -62.39898 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec3ed9d7-f5f2-3147-8bc9-ba6aa4470de4 | -9.65439 | -59.64147 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae240581-2156-39b3-bace-20c915d6f97b | -10.60843 | -55.41069 | 2025-08-23 05:42:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8534d65f-0e7c-34f5-b59e-d53fe032e2ca | -9.9496 | -60.17313 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09ab6c48-57a9-3a6a-be79-ee084f7451b2 | -9.1943 | -59.46234 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5cc8de8-965d-3ed3-958f-506d2c3c6ea4 | -8.86545 | -62.41256 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4824816a-dde5-3f51-ac33-5c95f32882d2 | -5.88185 | -57.76421 | 2025-08-23 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c3a92edd-69f6-3e5b-9390-010ec861c941 | -5.80882 | -59.22203 | 2025-08-23 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c904d7e3-702c-38d3-8483-74a77ab53539 | -9.21134 | -60.78497 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d63c4d4d-e785-3cdb-a3cf-a779966b377b | -10.3428 | -58.60729 | 2025-08-23 05:42:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfda0a33-723c-3ade-bd24-752d4d49878e | -11.18831 | -55.04753 | 2025-08-23 05:42:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f077fc1-316b-335d-ab11-ff921257ad1f | -5.75153 | -57.58302 | 2025-08-23 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 21914fbe-2b5a-3261-8c7a-55adde13e6c9 | -9.39078 | -60.50957 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff29ac06-f874-3bda-821d-bad8a9691d5b | -7.50684 | -63.83939 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d814b4a7-016d-3e10-b50a-dbb7e1f680b6 | -9.02614 | -59.01269 | 2025-08-23 05:42:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e687fa44-9c2a-3f41-a860-f005e9e53b83 | -7.79505 | -61.58484 | 2025-08-23 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 663d7f0e-6449-3508-b7d7-56a448c6ef92 | -9.18077 | -59.59493 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2772ebf7-66a1-3d7e-bef9-d4daf6d304bd | -9.17042 | -59.60845 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5636a76-4058-3782-acc0-22fbeaa98c26 | -8.67627 | -62.87484 | 2025-08-23 05:42:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac01fdd7-cec8-3a45-a4fb-c910a07e8d8e | -9.18983 | -59.46173 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 811526c9-4353-3356-a5ef-aad484cf93da | -7.81297 | -63.55604 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 657bfd12-35b8-397a-bf09-5e2a51e6adb3 | -9.94895 | -60.1912 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| ce15a0c2-0c12-37c7-b746-01dbb763ff4e | -7.73603 | -67.06911 | 2025-08-23 05:42:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96eda5a3-1750-36b2-b208-c757ca5db153 | -7.29964 | -59.62575 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07259f07-48a9-3423-bab2-8fe29019039d | -6.57611 | -59.88243 | 2025-08-23 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 87d38421-a6f0-3f5d-a527-1b7b77c2f293 | -7.81987 | -63.55707 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4db873ea-256b-37db-8a88-bdb7514a881a | -10.40854 | -57.68404 | 2025-08-23 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e22e9c4-19e9-38c0-bbf1-d3def1831bb6 | -9.45216 | -63.50247 | 2025-08-23 05:42:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cde25ae2-0a28-338d-ab5e-4f5ad2cd0cec | -5.80941 | -59.21799 | 2025-08-23 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f905e4d-0d86-3bd3-9162-a4471a57c2cd | -9.82094 | -64.27314 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b95c398-6396-3d93-990c-00ca26559ddb | -9.51876 | -60.54663 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbf9c8f5-a994-3b3c-907f-93536629e5cf | -8.61575 | -62.60646 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c14f7e51-30df-3c68-b730-af018bd21d5c | -7.72988 | -67.06441 | 2025-08-23 05:42:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cfc6b19c-5e44-31de-84c4-6acc3f1b7819 | -8.61212 | -62.60592 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e6045a07-26e1-3f52-a320-80b1e2310558 | -9.52253 | -60.51996 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 18adf16c-f6c2-3c42-9e41-b357a50485a5 | -8.44221 | -63.85724 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3dd8c00e-2548-3f74-9664-f6941628f994 | -9.15718 | -59.60658 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f5760e9-2296-30bc-8803-a05ca21f0bce | -9.95539 | -60.19497 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 3a501d70-16a7-3557-b936-4d1e115e98ad | -9.20586 | -59.47751 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a2a42f4-cda8-3088-9866-932cdb611e6d | -7.55965 | -63.85883 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4873cbb9-f6b3-3f2a-b196-4d460a67191f | -5.4417 | -60.16933 | 2025-08-23 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84770a27-153e-3fe4-b6d8-874610b92611 | -9.52817 | -60.54024 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README79.md)
