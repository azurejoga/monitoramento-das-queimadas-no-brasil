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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d87f1ef7-6a95-395d-82e4-d05b94b3f51d | -4.43263 | -55.10395 | 2026-09-08 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fd5259c-c91c-34d7-844c-91e9119fc8fb | -3.27182 | -50.02502 | 2026-09-08 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 451ce37d-b276-373e-9902-fb17cc302827 | -3.37558 | -59.42473 | 2026-09-08 05:04:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a48bb7d8-7d74-36fa-b23d-ace49240bf7b | -7.37215 | -47.02382 | 2026-09-08 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 45a3ae89-fa1e-393b-8fcc-a4c4b3b0e8d3 | -4.34123 | -55.22427 | 2026-09-08 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d34762f8-a868-386b-bea2-683879811aae | -6.56949 | -58.98122 | 2026-09-08 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c1b6920-da62-3809-ad17-a68aee23a892 | -4.04119 | -50.87925 | 2026-09-08 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 245919e4-ead4-3c05-ab2c-8b10acef7b6a | -4.34402 | -55.22837 | 2026-09-08 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 212c6591-8604-35f4-9883-0757e147cf09 | -6.44488 | -58.15125 | 2026-09-08 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09b45c82-e191-3ca7-a9b0-3a5cf58dcfe4 | -3.25095 | -50.82522 | 2026-09-08 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e300ad05-1fbc-3bef-b029-240d8071ab34 | -6.61083 | -44.72245 | 2026-09-08 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2183bbc-7245-3c80-b528-0a71b4f85bbb | -5.45175 | -60.17492 | 2026-09-08 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 708bff73-19da-3fd0-9eb8-9e0472899b44 | -3.77648 | -58.857 | 2026-09-08 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b31696e8-2870-30eb-a646-2d5bc733e7b6 | -9.71078 | -43.47364 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9ada67a4-3ba8-3a72-908e-6219f2b7a70d | -6.76055 | -45.48507 | 2026-09-08 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e8dd112-7c17-3551-a2c8-96effa02c4cd | -2.83917 | -53.99095 | 2026-09-08 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 037299dc-b921-3e5b-9b64-241483936b77 | -5.82288 | -53.81284 | 2026-09-08 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b959d1b8-a0c8-3d63-aa18-74ef783ecef7 | -3.37494 | -59.42862 | 2026-09-08 05:04:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 264a8dbb-c120-3191-92f2-a78719a67200 | -3.4739 | -52.8779 | 2026-09-08 05:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2c463888-7c16-3684-94c8-65dcaf7b55dc | -3.46133 | -59.50922 | 2026-09-08 05:04:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c6ef7fe1-f8e2-3065-9fe9-9a1f79afb83e | -4.98174 | -50.64311 | 2026-09-08 05:04:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae71a9a8-ccfe-3729-b852-1f4c1ac7633e | -6.02967 | -42.64442 | 2026-09-08 05:04:00 | NOAA-20 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 79a718ab-ccd3-343f-8741-50c97bc9805f | -2.7226 | -53.97679 | 2026-09-08 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ada170d2-e404-3650-9570-4a207519e018 | -5.44754 | -60.23956 | 2026-09-08 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b109171b-f883-3fca-945e-a704b5d374f8 | -4.34622 | -47.58132 | 2026-09-08 05:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 375ee1c6-bccd-3c08-86fd-a363bbed8679 | -9.72274 | -43.48003 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b3f5414-1795-3873-8c4f-8425a7deaa3b | -3.15948 | -58.65131 | 2026-09-08 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c42ef21-1f14-3aaa-9b46-ec3f6901bbaf | -6.37842 | -58.28991 | 2026-09-08 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ecea86a8-7f5a-37e2-8d99-19a4e9fe579c | -9.76422 | -43.45465 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dca3c1ab-9507-3291-83f6-c0961cb71e92 | -3.77361 | -58.84928 | 2026-09-08 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e314b89-329a-3605-a268-1c23ff01f1e7 | -9.71936 | -43.40387 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 2b55ae3c-55ac-382f-9820-e08d2cf5cc5a | -2.84249 | -53.99147 | 2026-09-08 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8654b3d5-c8cc-34c9-89f6-1661e8dc7f2a | -9.76549 | -43.4446 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d46d6466-59e3-3d69-9a3f-4388b3f69628 | -5.44968 | -60.17281 | 2026-09-08 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab552979-89de-3335-b063-ad4bf22ef8bd | -3.61312 | -58.01001 | 2026-09-08 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fee164db-2547-3d54-92aa-76560896812c | -5.36369 | -56.01743 | 2026-09-08 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44090812-5fa1-3fc7-8705-8db844c06b10 | -3.95632 | -58.95601 | 2026-09-08 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 729dcf45-d177-3417-804c-ddfd90b7059b | -4.67168 | -55.63037 | 2026-09-08 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5856b5c-8bc4-39c2-845a-8405c0dd58e1 | -5.28818 | -60.12088 | 2026-09-08 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c815a1da-8919-3205-a683-2bff689adde3 | -5.18384 | -59.75996 | 2026-09-08 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93a03725-dca5-350d-bceb-a0925a74680f | -3.71194 | -51.13887 | 2026-09-08 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad8ce92a-8ce3-3bf6-87c0-712b75d25995 | -7.06554 | -56.46869 | 2026-09-08 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d358a5d2-a392-3d46-acb9-5a4a981e3f40 | -6.6823 | -59.9268 | 2026-09-08 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a4842e6-ad2a-39cd-9889-6984bb4ba593 | -3.55135 | -48.1825 | 2026-09-08 05:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| a82e9fa5-c185-3ae1-8af9-7cd6756435f1 | -4.82091 | -55.77363 | 2026-09-08 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c3846f45-88b3-36f4-9e46-3e6a7fbed767 | -5.40944 | -49.11485 | 2026-09-08 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3c56137-0ef6-3f13-be0d-7342827683ee | -9.71138 | -43.46875 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7eff42ae-caf7-3579-b4ad-bc0475763479 | -5.45397 | -60.17354 | 2026-09-08 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2caac61e-5cc2-3800-aaf9-200174784477 | -2.66981 | -56.46777 | 2026-09-08 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbac5c76-1f3f-35aa-b413-03c9b8d2f774 | -4.97873 | -50.63829 | 2026-09-08 05:04:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a50cdd03-aeb2-3836-995e-5c3a7809e242 | -5.83006 | -53.81042 | 2026-09-08 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48ecba4b-2cb5-3c0b-a951-4c2bda50b46a | -3.54658 | -48.18563 | 2026-09-08 05:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 9fde391b-3779-32cb-92a1-8474d9d22b8c | -5.36028 | -56.01687 | 2026-09-08 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94ba2305-12c5-3c6e-a54d-8f00e2ba58c6 | -9.7592 | -43.4438 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 90314aa5-bd93-3e45-86e8-0d9d6e9403c1 | -5.45054 | -60.23335 | 2026-09-08 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| efcecf05-8309-35ba-b528-c35cafb334d1 | -3.33937 | -53.407 | 2026-09-08 05:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 942b699e-278f-3c8f-992c-65c7a3b1f09c | -9.76864 | -43.41968 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c24d0b9b-cb0a-35bb-97ff-bd78cfe0cbe0 | -5.54822 | -60.2451 | 2026-09-08 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e62dcbfc-d001-329a-a259-a24ab1dce672 | -9.70679 | -43.47632 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 30617ce5-ceb0-3579-833a-ae4386b5ba63 | -6.76386 | -59.43463 | 2026-09-08 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f4ae6697-0826-3713-a76a-fbd5eadb0581 | -9.70742 | -43.47144 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 94d016b0-dcfd-3bb7-9c21-cbb209540341 | -5.18803 | -59.76068 | 2026-09-08 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30345b62-b38f-3e44-88a0-a90b453bc8ec | -3.33606 | -53.40649 | 2026-09-08 05:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8b4c652-dda6-3344-9c9b-b5d15b055a47 | -4.16361 | -55.84857 | 2026-09-08 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 028121e3-3e30-38bd-9849-e36024acc8ee | -2.18227 | -60.22648 | 2026-09-08 05:04:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a890dcfd-a6e1-3b8c-bea9-437c38902ae3 | -5.81957 | -53.81233 | 2026-09-08 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d6004c1-3790-3204-938b-1948f501fb3d | -9.72062 | -43.39366 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 3ef61823-d22f-388b-9d97-f17cfbf8206e | -9.72684 | -43.3952 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 35b04468-f8e2-377b-868c-9391a9f1eec0 | -4.04961 | -50.87215 | 2026-09-08 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42518d94-4663-3c35-a4cb-a2b17475e656 | -5.48192 | -60.20509 | 2026-09-08 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a9365a9-3147-3ed4-87e0-70b7118f64b0 | -4.4802 | -48.18824 | 2026-09-08 05:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3f8f08bd-0a5d-3fc5-a82c-a94ec72ad35e | -9.73719 | -43.51743 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fcec2dd7-2827-3db7-a2b2-9673d7cae78e | -9.70929 | -43.45704 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1906bfb1-c5b5-3fa2-9650-be1130282bea | -5.48261 | -60.20102 | 2026-09-08 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1060e8e2-f0c4-39eb-8010-a49bb4d6fa6b | -6.5313 | -58.51411 | 2026-09-08 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec5e980f-efd3-3a47-be84-fd8980eabf6b | -5.15867 | -55.96189 | 2026-09-08 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d9bd03e-8b03-3ac7-9ada-979594db974c | -3.92539 | -49.05127 | 2026-09-08 05:04:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8431f972-d84f-36d8-a8d1-b1ee5112df7d | -7.54287 | -45.01478 | 2026-09-08 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3136913c-d9c9-3cd6-971f-b0a582d4e8f1 | -7.54337 | -45.01114 | 2026-09-08 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e3b15eaa-7548-3c52-aecb-64192c982338 | -3.51121 | -56.90276 | 2026-09-08 05:04:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd8a16f4-7997-3853-98d9-8aa387086871 | -7.67257 | -46.04723 | 2026-09-08 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33a50912-3053-3ffe-ac12-e6afd19a3558 | -3.65069 | -50.95222 | 2026-09-08 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f32b49d-d2ba-342b-ac7b-44ffcc6fc5de | -9.71264 | -43.4313 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 9e9c2293-421c-3eab-9df3-294fcef743f1 | -3.85234 | -51.3791 | 2026-09-08 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77ff48c6-e958-3671-9f60-9264dc05d9c7 | -5.54893 | -60.24099 | 2026-09-08 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e63cf9a-0988-37b0-8ac1-cb94c9109dbc | -5.59193 | -60.24834 | 2026-09-08 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50840226-95cf-3d93-99a7-31cf9100ac7b | -5.44902 | -60.17685 | 2026-09-08 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c02f384-8042-31d2-a895-68fb44ca8927 | -3.81265 | -55.89306 | 2026-09-08 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 54a8ac1a-1c8f-3467-9c50-db52e6a54113 | -3.625 | -54.60575 | 2026-09-08 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c45c883-8b84-31df-ac88-54cbbdd510be | -9.71128 | -43.41753 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 16a5ce7b-a420-3bd7-86d8-68bc67841f7d | -3.38746 | -50.4572 | 2026-09-08 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d048076-9f94-329d-8929-64fcefbb09d9 | -3.70161 | -58.93258 | 2026-09-08 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a910e6f-d1b0-3b6b-86b1-658b4207d42c | -5.55252 | -60.24583 | 2026-09-08 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4202b676-30d3-30b6-a95c-ddcc24870e13 | -3.54835 | -48.17421 | 2026-09-08 05:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 907c20ba-0458-36be-8003-a32824a08c3b | -3.89021 | -55.82488 | 2026-09-08 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| eba07719-3e22-325a-8a82-13e9d6f2fbbe | -4.9279 | -42.87989 | 2026-09-08 05:04:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e91cdd70-9962-3aee-9f16-29711716fe36 | -9.74344 | -43.5184 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7213d512-87e7-306e-a8ed-849836843e97 | -5.3631 | -56.02111 | 2026-09-08 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77f2327d-e728-349d-8636-65015fa09ae9 | -6.63357 | -59.44234 | 2026-09-08 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d76d55f0-bd64-3b29-a96b-7302b2884eb5 | -3.16062 | -50.82444 | 2026-09-08 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README21.md)
