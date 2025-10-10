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
| a5b8898f-4336-3778-8f4b-81bc914fb0f2 | -10.1707 | -44.5959 | 2025-10-10 00:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| e7704867-e3e8-373f-88d2-031989a97ed7 | -3.7936 | -49.4424 | 2025-10-10 00:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| c7b33285-9725-3e22-9767-092f822e4188 | -3.7937 | -49.4211 | 2025-10-10 00:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 3b38d40d-abd2-333f-a93d-19971f8369fe | -6.5851 | -44.6098 | 2025-10-10 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| b6f99adf-8e56-3249-b000-41e2547b05d5 | -16.8903 | -49.7241 | 2025-10-10 00:40:00 | GOES-19 | CAMPESTRE DE GOIÁS | GOIÁS | Brasil | 5204607 | 52 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 69695830-2e92-3b00-ac43-b7ac990f9c08 | -8.5184 | -66.9954 | 2025-10-10 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 313f334e-d685-3018-a7e7-178ff1989f09 | -17.9175 | -45.0194 | 2025-10-10 00:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 156.2 |
| 693959bf-8a55-38ca-9eaf-afe8f7c5cf23 | -3.7751 | -49.4431 | 2025-10-10 00:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 99c87048-9661-3412-92a3-c9ce0718ab7c | -5.656 | -45.9692 | 2025-10-10 00:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| fb2485cf-d3fc-330f-9bda-c9068efa0f04 | -6.5851 | -44.6098 | 2025-10-10 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| e1989bcf-bdec-3748-be5b-cb7eb8ffab95 | -13.0778 | -43.83 | 2025-10-10 00:50:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 256d25a1-0ec7-3de3-8b41-5ec18622070b | -6.5849 | -44.6327 | 2025-10-10 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 9c4d4163-53e4-3b8d-b7c3-89694903d60a | -15.9189 | -43.3022 | 2025-10-10 00:50:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 891e60f0-f18c-36ae-91c2-072e0344075b | -15.9195 | -43.2779 | 2025-10-10 00:50:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 228.5 |
| b5f73dbd-03f9-3472-bc35-da751478899b | -4.6505 | -43.1805 | 2025-10-10 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 2dcec391-145e-389b-be1a-17388aec47d9 | -17.9369 | -45.0388 | 2025-10-10 00:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 163.3 |
| f45f45c9-0596-3e03-9e69-61d7fd30cc43 | -15.8991 | -43.3065 | 2025-10-10 00:50:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 772197c2-387d-3203-9192-e52b46f01482 | -3.7752 | -49.4219 | 2025-10-10 00:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 4dc5cc53-d709-3071-90a8-f3c112844549 | -3.7936 | -49.4424 | 2025-10-10 00:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 460ff39b-7907-3e58-95b6-1f8161477c41 | -17.9376 | -45.0148 | 2025-10-10 00:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 353.2 |
| 13214ae9-1cd6-308f-b650-b2f1adbb8611 | -17.9577 | -45.0103 | 2025-10-10 00:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 97.8 |
| ec8e038b-b463-3af4-bafd-b52bd5796ee7 | -15.8997 | -43.2822 | 2025-10-10 00:50:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 37ba98d9-8aee-3d0d-853d-9402b051911b | -7.3966 | -45.9227 | 2025-10-10 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| e11f4cc8-ff61-396d-9650-7b172e6f5d06 | -3.7937 | -49.4211 | 2025-10-10 00:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| e7f69972-031f-3d72-8574-d92380975538 | -17.9382 | -44.9909 | 2025-10-10 00:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 113.1 |
| b331e381-e3a8-3e19-aedb-1cd423ff8bf0 | -7.4154 | -45.9211 | 2025-10-10 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| d3d91936-1044-349f-88ae-3622b0a1e9a1 | -13.0584 | -43.8333 | 2025-10-10 00:50:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 79dd07fc-1840-3ff2-a445-1511bb5680c3 | -4.6504 | -43.2038 | 2025-10-10 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 222969e1-c848-3906-80ae-1cfbefb3783c | -13.058 | -43.8571 | 2025-10-10 00:50:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 1604860f-0175-34e6-959b-0640741272dc | -13.0773 | -43.8537 | 2025-10-10 00:50:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 959b86a1-bf87-333b-97e2-5f742cdcd292 | -10.1707 | -44.5959 | 2025-10-10 00:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 88.1 |
| b9c5f79b-a0b6-3a74-b7e9-7e539926be6f | -3.7751 | -49.4431 | 2025-10-10 01:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 5685cdb6-6ccd-367a-8f2c-b788337422eb | -8.5032 | -46.1321 | 2025-10-10 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 5132d816-ed1f-3598-bc0b-ca73c63ab13b | -4.4073 | -48.9474 | 2025-10-10 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 23912e48-f692-35dd-8e9d-83d4305234f2 | -6.5849 | -44.6327 | 2025-10-10 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 481b318f-d57c-36ca-9e8c-deea6b321bf1 | -8.5409 | -46.1282 | 2025-10-10 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 39b13872-a581-3978-b3c5-0049dbc7212e | -8.5221 | -46.1301 | 2025-10-10 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 231.2 |
| 447f80d6-02eb-33db-bcff-2e80ac187752 | -10.1711 | -44.5727 | 2025-10-10 01:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| b0d0fb1e-98ef-3fa0-b93a-183ab3d7d72e | -17.9382 | -44.9909 | 2025-10-10 01:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 204138ec-d02b-3cbc-8374-fe17efb0a075 | -4.4072 | -48.9688 | 2025-10-10 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 4fa35388-5e15-30d0-808f-bb334cc333aa | -17.9376 | -45.0148 | 2025-10-10 01:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 341.2 |
| ec0a84d7-1803-3beb-8db0-d0a1d792083f | -17.9577 | -45.0103 | 2025-10-10 01:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 6b535131-14b3-38e0-9a35-64fb9d6a7a26 | -7.4154 | -45.9211 | 2025-10-10 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 4bd9e629-4ca6-3eba-86a1-7ac6d7bc9605 | -4.6504 | -43.2038 | 2025-10-10 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 85444978-157e-3474-894c-f173bcb33d2a | -7.3966 | -45.9227 | 2025-10-10 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 2a30d7d4-fc6a-354f-b939-6d334201e4ad | -8.5218 | -46.1526 | 2025-10-10 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 193.2 |
| a0340dd5-98d8-3b06-b665-066aa0daf622 | -8.5407 | -46.1507 | 2025-10-10 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 7a64186e-c609-3c33-902c-fdbb100fe080 | -15.9195 | -43.2779 | 2025-10-10 01:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 167.4 |
| b833dc13-f37f-39a8-9cb3-b4172916124b | -17.9175 | -45.0194 | 2025-10-10 01:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 163.0 |
| 41e58d63-b127-3617-8eb2-32049add0ece | -10.1707 | -44.5959 | 2025-10-10 01:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 134.3 |
| cc652e4a-cfb8-3411-83a0-e337f239ec22 | -8.5184 | -66.9954 | 2025-10-10 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 473bbf4f-6d39-396d-80bb-1a281e80f187 | -3.7937 | -49.4211 | 2025-10-10 01:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 7396fa40-be13-3dfe-bee8-60869414f9ba | -3.7936 | -49.4424 | 2025-10-10 01:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 18030a89-8e2c-3156-8a52-3f2ca416cebb | -17.9369 | -45.0388 | 2025-10-10 01:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 130.8 |
| d899a60d-ac80-3117-a74c-0b5f82253ea7 | -6.5851 | -44.6098 | 2025-10-10 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 8072abd0-6022-32f0-905b-222eab141c3c | -3.7752 | -49.4219 | 2025-10-10 01:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| c88d0866-a31c-381e-b36d-6ca4917ff868 | -15.9189 | -43.3022 | 2025-10-10 01:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 49388fde-9b1c-3090-a34a-e6a5d849fcec | -8.5029 | -46.1545 | 2025-10-10 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 86bfdbd4-fb32-3284-ac0a-f994cfd3099c | -15.9189 | -43.3022 | 2025-10-10 01:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 106f667c-bb9a-3d3e-b03d-543d34436871 | -13.0778 | -43.83 | 2025-10-10 01:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 2490271a-5f71-3dd2-8ea6-d55c0eb09c86 | -4.6504 | -43.2038 | 2025-10-10 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| f967887f-fa7c-3966-ba1c-29381b9e796b | -17.9376 | -45.0148 | 2025-10-10 01:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 357.6 |
| 9a8de062-648b-3e1c-a424-65bd55db5ca9 | -13.0773 | -43.8537 | 2025-10-10 01:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 8dbc5acf-687c-3152-af42-0ba0c415a57b | -8.5032 | -46.1321 | 2025-10-10 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| e82ed786-2ac8-3637-a0af-110c41b74ed3 | -15.9195 | -43.2779 | 2025-10-10 01:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 1c913802-f156-3c72-a1c9-7cc3392064f3 | -10.1714 | -44.5496 | 2025-10-10 01:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 37e294f8-e9de-34be-9db0-b1283fb22dd1 | -10.1707 | -44.5959 | 2025-10-10 01:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 09168c86-ea28-354b-9356-6d14f0393ee4 | -8.1993 | -43.3424 | 2025-10-10 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.4 |
| 47098f97-878d-33ce-8d18-2237b5a415c3 | -10.1517 | -44.5984 | 2025-10-10 01:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 4302fb4d-b54d-337f-8f24-97f487c02944 | -3.7752 | -49.4219 | 2025-10-10 01:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 5844328c-bbcc-39d9-bbf4-1b25c2b47ab8 | -12.6294 | -45.0517 | 2025-10-10 01:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| f253822a-7430-3287-8bb8-dacb8141340e | -7.4154 | -45.9211 | 2025-10-10 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 6e5b27e7-2028-32b5-9999-b9807946116f | -13.058 | -43.8571 | 2025-10-10 01:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 1f1a9050-25a7-37a4-a55f-da189a1fd3ab | -17.9382 | -44.9909 | 2025-10-10 01:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 0d95d24c-c268-3f95-93ef-4fe48bd8de39 | -17.9577 | -45.0103 | 2025-10-10 01:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 108.4 |
| ebffb82d-acb1-3186-bc3b-3c5a85a56c09 | -13.0584 | -43.8333 | 2025-10-10 01:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 724dec67-117e-3d30-b34b-c9d1eb0c713a | -6.5849 | -44.6327 | 2025-10-10 01:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 188df86b-1001-3e0e-be9b-aadd7f9e66fe | -10.1711 | -44.5727 | 2025-10-10 01:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 4c8d2e40-dd3b-34d2-a921-2ce597afddf4 | -8.5221 | -46.1301 | 2025-10-10 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 0856a20b-e0df-3e4b-9afa-06d47ef31645 | -3.7937 | -49.4211 | 2025-10-10 01:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 3c98758f-0dce-3b96-b04c-90c55c71be6e | -3.7936 | -49.4424 | 2025-10-10 01:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 8e347631-c665-3952-a15a-268d203b7123 | -8.5218 | -46.1526 | 2025-10-10 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| f2f452ce-e1e1-39be-9b26-ccc8c3df87be | -6.5851 | -44.6098 | 2025-10-10 01:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 6bf29fc3-dbea-3ff3-b5f1-3d847290e2a7 | -17.9175 | -45.0194 | 2025-10-10 01:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 1afed3ae-a3a6-3b78-ab53-019abd958288 | -17.9369 | -45.0388 | 2025-10-10 01:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 177.6 |
| 7c481a89-d2b8-38cd-bc9e-d90950684b06 | -8.5221 | -46.1301 | 2025-10-10 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| a3cdf736-fa64-373d-8410-c982ac14e82f | -10.1707 | -44.5959 | 2025-10-10 01:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 2e8ccda7-535f-3a1e-8c2c-524ae1679ba4 | -8.5224 | -46.1076 | 2025-10-10 01:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 73012ac0-dd98-3612-ba4c-dc0eb188b05e | -17.9376 | -45.0148 | 2025-10-10 01:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 347.5 |
| 633d55c1-23e8-3ce5-b29e-22f545460426 | -12.6294 | -45.0517 | 2025-10-10 01:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 2c13eb79-c4ba-3c38-9975-1d762de1fb45 | -17.9369 | -45.0388 | 2025-10-10 01:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 144.6 |
| ba4a782c-0e2a-3061-a542-865ef18013d5 | -3.7751 | -49.4431 | 2025-10-10 01:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 6cb5cc63-eac7-3b2b-9e9f-67a52ce7ef54 | -15.9189 | -43.3022 | 2025-10-10 01:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 38ea66a1-4ffc-36c5-a0f3-d7866a54cdd0 | -4.9528 | -42.8095 | 2025-10-10 01:20:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 827f942a-863d-3dad-9fe5-189144a63eb2 | -3.7936 | -49.4424 | 2025-10-10 01:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 61550793-f13d-3ac9-8d49-bbfd6647122e | -8.5218 | -46.1526 | 2025-10-10 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 167114bd-387a-3e3a-831d-93c3c949f400 | -15.9195 | -43.2779 | 2025-10-10 01:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 420db241-637f-3435-b2bb-414217d5820b | -13.0584 | -43.8333 | 2025-10-10 01:20:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 70ff8ffc-54bf-3d68-95b4-3035baf16065 | -8.1993 | -43.3424 | 2025-10-10 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.0 |
| 7e10dde5-9cf5-3ce7-9fa0-b43104e960d1 | -4.6504 | -43.2038 | 2025-10-10 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |


[Clique aqui para ver as próximas entradas](README8.md)
