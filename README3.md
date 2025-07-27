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
| 7d8b28ac-ea05-3dca-ae80-0bacf1eb7d75 | -18.0027 | -53.1584 | 2025-07-27 02:00:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 11de91ea-3f46-3f6e-99b4-9e4492964aaf | -10.05291 | -64.9871 | 2025-07-27 02:04:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9f89dbb8-3570-36e1-bacf-41e86007e698 | -8.61044 | -64.04888 | 2025-07-27 02:04:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 54fd7e08-f33a-3e36-91d4-d8e122e0c19e | -10.04915 | -64.9812 | 2025-07-27 02:04:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 13.6 |
| e92ffb87-f336-3ce0-aabe-26db7aeef336 | -8.60737 | -64.02895 | 2025-07-27 02:04:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 3a1faeba-0af5-3bb9-920b-46c4cf94aba9 | -8.60937 | -64.04261 | 2025-07-27 02:04:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 3fc38485-29dd-32d5-ba2b-5970bc6c1e41 | -10.01658 | -67.76286 | 2025-07-27 02:04:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.6 |
| da609ade-f2f3-3a10-b91e-7d03653f698e | -18.0023 | -53.1799 | 2025-07-27 02:10:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 02c23b5e-f6dc-34b2-95f7-a24014656d03 | -6.639 | -58.8475 | 2025-07-27 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 146.4 |
| 43be18da-b40c-30e8-98c5-22866eebdfe1 | -6.6575 | -58.8468 | 2025-07-27 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 113.2 |
| a83104dc-4cd6-31e8-83d0-381d890d594b | -18.0027 | -53.1584 | 2025-07-27 02:10:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| b77537e3-6874-3c08-a52b-c370000743ae | -6.6206 | -58.8483 | 2025-07-27 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| f0c9aff1-2226-3083-93a0-bb2587d0400a | -6.6389 | -58.8669 | 2025-07-27 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 3adc750d-9190-3abb-b7d4-4961739c0fec | -6.6574 | -58.8661 | 2025-07-27 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 1bdb640d-bc9d-3d0f-a345-f58c60a025f3 | -6.6759 | -58.846 | 2025-07-27 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 81310673-55c4-3923-bdc5-df33dd4742b1 | -18.0023 | -53.1799 | 2025-07-27 02:20:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 615973ff-4eb5-3aa1-97ee-3d62d76c182c | -6.6391 | -58.8282 | 2025-07-27 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| a564e01b-263b-3245-9546-9c6061606afe | -6.6206 | -58.8483 | 2025-07-27 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 0bbec547-cd7c-3a07-b948-d581190b18f3 | -6.6389 | -58.8669 | 2025-07-27 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.1 |
| cde0a27e-1fcb-3a00-9bb6-381b6db554f4 | -8.6052 | -64.0458 | 2025-07-27 02:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| f6e51b55-cf2e-3267-9bf5-1117542da121 | -6.639 | -58.8475 | 2025-07-27 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 131.6 |
| ea4d91e6-8740-3185-91bb-389a394445d1 | -6.6575 | -58.8468 | 2025-07-27 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| a0853060-8c0b-393b-a93c-b9431f3e5e34 | -6.6574 | -58.8661 | 2025-07-27 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| d75620fa-560a-3902-b816-59e780aa1993 | -6.6206 | -58.8483 | 2025-07-27 02:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| ecb7081c-fa91-3cfb-bafd-e263b6160823 | -6.639 | -58.8475 | 2025-07-27 02:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 134.3 |
| 0fa4d60a-3486-339e-96ce-420e08726e06 | -6.6391 | -58.8282 | 2025-07-27 02:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 85d52979-b084-3d7b-9f3f-9ab098a18fdd | -6.6389 | -58.8669 | 2025-07-27 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| b9fea559-4909-3030-b351-2fc62834acc7 | -6.6575 | -58.8468 | 2025-07-27 02:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 102.1 |
| a0e91090-f271-39ca-bd35-21c89a79328f | -6.6574 | -58.8661 | 2025-07-27 02:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 1b724164-0bba-3bde-930a-f00d3946919f | -8.6052 | -64.0458 | 2025-07-27 02:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 6a773357-2118-3d16-b1c6-9cd47338627e | -6.6206 | -58.8483 | 2025-07-27 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 7a29a4fa-d70d-3f27-b0b8-9ba37ae5b4ed | -6.6575 | -58.8468 | 2025-07-27 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 5a1806e0-e211-3167-a6ad-2ad646e5d55f | -6.639 | -58.8475 | 2025-07-27 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 3a952d3b-f32a-3e37-afc9-56e490adfe33 | -6.6389 | -58.8669 | 2025-07-27 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 512fceff-d79a-3e44-828c-dbb6d64ccd42 | -6.6206 | -58.8483 | 2025-07-27 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 1a0620bc-a3e4-3980-bad7-cf48edb76bc7 | -18.0226 | -53.1553 | 2025-07-27 03:00:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 13f740a4-1e6e-3d7d-baef-1f25012e2a3c | -6.639 | -58.8475 | 2025-07-27 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 125.3 |
| 374243d8-2796-32de-a871-2422d22bd511 | -18.0027 | -53.1584 | 2025-07-27 03:00:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 516da66b-d4ba-3e5b-9a06-dc1d5c0e9a15 | -18.0023 | -53.1799 | 2025-07-27 03:00:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 488840de-4e39-327a-a963-b0e682a59cc6 | -6.6575 | -58.8468 | 2025-07-27 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 7b9b48cd-1c7b-3bd1-bbba-c0978f7664b6 | -6.6389 | -58.8669 | 2025-07-27 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 254c5d58-7d54-32d1-9726-889d75837f9b | -6.6389 | -58.8669 | 2025-07-27 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 64934f80-f2da-3221-a8d8-d731cbfd13dc | -18.0221 | -53.1768 | 2025-07-27 03:10:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 221.9 |
| 56ae0d6e-1dad-300a-91d4-3d87422b7d87 | -18.0023 | -53.1799 | 2025-07-27 03:10:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 244.3 |
| 19c1c539-29ca-381e-a333-cd422ee5ffb9 | -18.0027 | -53.1584 | 2025-07-27 03:10:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 210.2 |
| 33315d08-1b4a-3611-92b3-f662c7dd5e4e | -6.639 | -58.8475 | 2025-07-27 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 1be19c51-b29b-3aab-854a-2824112439b6 | -6.6206 | -58.8483 | 2025-07-27 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 05480ff6-c887-3168-80e6-a4c61ce95f89 | -18.0226 | -53.1553 | 2025-07-27 03:10:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 194.8 |
| 84c6f3ed-b03f-3a63-8ddd-0fbf8ca40779 | -6.6391 | -58.8282 | 2025-07-27 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 48b54515-b371-35f7-b09f-48f3afb6e489 | -6.6574 | -58.8661 | 2025-07-27 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| ee0fba0d-7527-372e-b57f-6c390b824b8b | -6.6575 | -58.8468 | 2025-07-27 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 76672f6d-9969-33a2-a8a9-a025d2c5424d | -10.52015 | -42.553 | 2025-07-27 03:17:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 742c22fb-7bb4-300e-9730-71f4e80c8b49 | -10.51905 | -42.55853 | 2025-07-27 03:17:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 70a0d339-480c-3c60-85bc-8c4743c50238 | -8.16948 | -43.19848 | 2025-07-27 03:17:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| a935950e-61a3-3f15-9ff4-7b4e3acd97ac | -8.17044 | -43.20574 | 2025-07-27 03:17:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 870be5d5-5bc8-3ba3-a11d-6e9a85aae22c | -10.51248 | -42.5575 | 2025-07-27 03:17:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 94aa17e6-23a1-3913-a47b-282a3d17d697 | -9.50964 | -40.38031 | 2025-07-27 03:17:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5a7098f4-aad4-32e7-ad13-1531aa03e82c | -8.17176 | -43.19889 | 2025-07-27 03:17:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 31a9917a-66cd-39de-ad3d-7f50d811080f | -7.16733 | -38.43948 | 2025-07-27 03:17:00 | NOAA-21 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1c354e14-c69a-3690-b681-e1521d0ad2b4 | -8.17379 | -43.2135 | 2025-07-27 03:17:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 9cd18c84-d743-31b2-bb2d-a06712c41f7c | -6.66175 | -36.4149 | 2025-07-27 03:17:00 | NOAA-21 | NOVA PALMEIRA | PARAÍBA | Brasil | 2510303 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 00803e5b-9a46-3e44-a2b1-d17275cd8376 | -8.17515 | -43.20668 | 2025-07-27 03:17:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 9189439d-3414-3280-bc1d-a2f4d5f343ac | -15.18489 | -43.27698 | 2025-07-27 03:19:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 302bc8c5-2f89-3a44-ac9d-f2bd6890c53f | -17.61809 | -42.28112 | 2025-07-27 03:19:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9508701f-e0b6-36fd-b068-4b91cf726566 | -15.19114 | -43.27842 | 2025-07-27 03:19:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 985ea001-6d7d-3651-a727-219eeada6e07 | -15.27327 | -43.07729 | 2025-07-27 03:19:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5f6380ae-ffb0-388f-a3fb-71aac4fe763f | -15.98903 | -42.64965 | 2025-07-27 03:19:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8a514292-3c24-3e02-9c24-bffd3bbfe88f | -15.99491 | -42.65126 | 2025-07-27 03:19:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 046581bd-9829-3ead-a617-fa6c30360410 | -17.21082 | -44.84877 | 2025-07-27 03:19:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59051e3c-452a-3bfb-b5cc-35ad06747a8c | -15.26714 | -43.0757 | 2025-07-27 03:19:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 0d190988-4a9a-3360-9282-f30ba2e10bcc | -15.26605 | -43.08086 | 2025-07-27 03:19:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 8.3 |
| a2d33880-4786-3da4-b174-6091e31c67fb | -17.20944 | -44.85476 | 2025-07-27 03:19:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0dca9e4c-a008-3c4d-a237-21a5ecc6eacf | -6.6575 | -58.8468 | 2025-07-27 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 573a3203-eec1-3c49-a1f5-db33b8e7b6dc | -6.6206 | -58.8483 | 2025-07-27 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| be6be9ca-4078-3269-ac3d-a1c35342a6c8 | -26.0229 | -49.0079 | 2025-07-27 03:20:00 | GOES-19 | GARUVA | SANTA CATARINA | Brasil | 4205803 | 42 | 33 | nan | nan | nan | Mata Atlântica | 75.8 |
| 2c213d22-e0e5-3b11-9833-5ac44cbbb6bf | -18.0226 | -53.1553 | 2025-07-27 03:20:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 197.5 |
| 54741a8b-14fd-380f-b3aa-1a64a3926d6b | -6.639 | -58.8475 | 2025-07-27 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 95.0 |
| c06cd098-dedb-35d3-98cc-131f4d37a9e7 | -18.0027 | -53.1584 | 2025-07-27 03:20:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 154.4 |
| f4ac207e-08c8-3b4f-8d10-8a1010e4b64b | -18.0221 | -53.1768 | 2025-07-27 03:20:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 216.4 |
| 418bcf00-4932-366e-aba6-1295f3697e18 | -18.0023 | -53.1799 | 2025-07-27 03:20:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 168.4 |
| 76d1babe-628b-3b10-8e47-a628f8d3500e | -6.6389 | -58.8669 | 2025-07-27 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 310279b2-166e-321b-b7a4-d75ddf55b745 | -21.33928 | -45.64235 | 2025-07-27 03:21:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 011839d6-658d-3d47-9e7f-9652877820f0 | -21.34075 | -45.63631 | 2025-07-27 03:21:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 052bcc6f-c67d-3299-a325-bfc9f4a8af0b | -26.02221 | -49.01153 | 2025-07-27 03:23:00 | NOAA-21 | GARUVA | SANTA CATARINA | Brasil | 4205803 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| cf927db2-ddf4-3458-8e88-e1c336400588 | -26.01546 | -49.00902 | 2025-07-27 03:23:00 | NOAA-21 | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 55484561-7508-3413-bb2c-9d687d4bc458 | -6.6575 | -58.8468 | 2025-07-27 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| cad67f44-0f57-3c1a-9d97-a431ad37f5af | -6.639 | -58.8475 | 2025-07-27 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 38.2 |
| cf9f07ad-9181-3bf2-b2dd-89c8295150ee | -6.639 | -58.8475 | 2025-07-27 03:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| cefe0039-c40a-37d6-b288-5f827941677d | -18.0023 | -53.1799 | 2025-07-27 03:40:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 54dc06c7-6a75-3182-bac4-4124d7fde0c7 | -18.0027 | -53.1584 | 2025-07-27 03:40:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| c7b71cdb-181d-3ae0-b6ce-853cdf282910 | -4.10858 | -47.9376 | 2025-07-27 03:45:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c4d6afe5-3620-3a4e-bf90-6fb250aa9e90 | -8.29719 | -45.00851 | 2025-07-27 03:45:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b67880c0-602e-36a3-a157-643b7c1e9d17 | -9.57784 | -43.86699 | 2025-07-27 03:45:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4d113d5a-9be4-3556-9050-2b711866e370 | -6.42202 | -41.14647 | 2025-07-27 03:45:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| aa5b9d43-483b-3628-b2f7-bb1f052d097e | -8.01389 | -48.1711 | 2025-07-27 03:45:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6435193c-9c7c-3f3f-94d7-1a6ae074d518 | -6.70357 | -43.0743 | 2025-07-27 03:45:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63aeee5e-d9ef-3dd9-8755-905da22144d5 | -4.61501 | -43.32063 | 2025-07-27 03:45:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ff2d477e-2d0b-31ac-bc5f-bdcf1de67336 | -4.6145 | -43.32371 | 2025-07-27 03:45:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0dc41ca8-9424-34bc-b204-15df05f24ad9 | -6.5609 | -41.51756 | 2025-07-27 03:45:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 21471010-8a5d-3cc0-877f-bec147f9bd83 | -9.12763 | -45.86963 | 2025-07-27 03:45:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README4.md)
