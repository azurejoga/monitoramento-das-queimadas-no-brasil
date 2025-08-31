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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 884c97b9-611e-3152-a70d-1b838963d2e8 | -9.4684 | -62.3286 | 2025-08-31 01:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 99b52c6e-eced-3f44-b603-b3265e95cac9 | -8.6539 | -61.9457 | 2025-08-31 01:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 054ca5d4-776f-3522-95b8-d755543f529d | -9.4498 | -62.3294 | 2025-08-31 01:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 71.0 |
| a7bfdc6f-edf0-33a5-aa47-cd0bc6ccdacd | -7.0951 | -44.3128 | 2025-08-31 01:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 33abb53b-4f39-32d0-8d7a-61f45cd354df | -8.7439 | -62.3979 | 2025-08-31 01:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 45cfc6c5-1567-3e1a-8dda-29f47b227f46 | -8.6673 | -62.8369 | 2025-08-31 01:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 29c6100f-07b8-30de-b0c5-ebb62cb50509 | -9.0613 | -65.4542 | 2025-08-31 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 572a72aa-9fa6-36ce-9edd-98b37b5eaf8d | -9.2745 | -67.6433 | 2025-08-31 01:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| a4497bbe-ab0e-35c2-81cc-c0f8bead906e | -13.3443 | -46.953 | 2025-08-31 01:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 8b66c3b2-17e7-330a-bd22-9bec76558d4a | -10.3126 | -59.2023 | 2025-08-31 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| db3bf01a-09f4-3207-8e92-5baac558769b | -9.4311 | -62.3493 | 2025-08-31 01:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| debde87b-54e8-38be-bcb8-6a4d612de091 | -11.3504 | -43.637 | 2025-08-31 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| ccbf8a6e-119a-3030-99e2-e529ac2d3df6 | -11.3116 | -43.6664 | 2025-08-31 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| a6f1a18f-01cf-3a86-9e29-5ede5611ce21 | -8.744 | -62.379 | 2025-08-31 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 5fa0a684-a309-385d-b369-86d42ba4ebd5 | -7.908 | -63.0164 | 2025-08-31 01:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 57c72241-336c-352d-a880-f388b33996c3 | -8.8337 | -66.7275 | 2025-08-31 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| a1f49736-e270-36ef-8a62-614a8c3cde9d | -8.8522 | -66.727 | 2025-08-31 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 3cedccf4-2fba-3189-8722-a352090744ad | -9.4312 | -62.3303 | 2025-08-31 01:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 856eb8e1-b343-3a9f-a679-68e7aee0651a | -12.9192 | -56.9873 | 2025-08-31 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| a1b6a00e-1904-3994-ae70-eb95e5f078ee | -16.2221 | -52.6778 | 2025-08-31 01:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 203.5 |
| 25a4541a-c324-31a9-a628-b6d8ea7fff8d | -9.0615 | -65.4169 | 2025-08-31 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| b7dc8093-dbb2-3145-b02a-e5a5409ea055 | -19.0926 | -48.3106 | 2025-08-31 01:10:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 7b81b802-0eaf-30ce-8721-81a526a9f56a | -6.1665 | -43.3273 | 2025-08-31 01:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 24ec0450-1604-34f2-9a4d-5d57f817da59 | -11.8373 | -46.4287 | 2025-08-31 01:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 2fa6fadc-02dc-3198-97ad-d8846ddf41fb | -10.6128 | -44.3284 | 2025-08-31 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| cff3e08b-3138-3eff-a526-5c144ddb3fa4 | -3.5994 | -47.5359 | 2025-08-31 01:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| d132df8f-7178-36d3-bcd9-61d97d742bda | -13.3636 | -46.95 | 2025-08-31 01:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 83704a0c-7709-3d28-ba30-0dfdbc0175a5 | -12.0976 | -44.717 | 2025-08-31 01:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 74600130-12d1-3807-9da8-71204cda25b9 | -16.2221 | -52.6778 | 2025-08-31 01:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 1a37062c-68e0-348a-b5ae-7a601067b518 | -8.7471 | -61.8656 | 2025-08-31 01:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 31e7dade-b449-38ae-9420-9e85ec64b98f | -10.3313 | -59.2011 | 2025-08-31 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 4c2cb2db-5c3c-3237-b840-3011ee035e5a | -18.6715 | -49.102 | 2025-08-31 01:10:00 | GOES-19 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 68.3 |
| caf20609-dc6c-3486-8449-c59f211adacb | -18.672 | -49.0793 | 2025-08-31 01:10:00 | GOES-19 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 65.2 |
| ded78d59-876c-3cc1-8027-cbb2d0a6d2c1 | -3.8146 | -48.9515 | 2025-08-31 01:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| eb6db481-dda9-349f-861b-e072b9c46e06 | -13.3632 | -46.9727 | 2025-08-31 01:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 65.8 |
| da065ad7-b24e-3ecd-8c3b-47503bc59b86 | -14.5452 | -51.9729 | 2025-08-31 01:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| c9e64613-e8fb-3136-bf12-0de35104a066 | -16.2417 | -52.675 | 2025-08-31 01:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| acc1c080-333a-3477-94a2-e46097da278a | -19.1128 | -48.3063 | 2025-08-31 01:10:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 118.1 |
| f07263b4-0b58-3bdf-92b2-369f0c022e40 | -7.1139 | -44.3111 | 2025-08-31 01:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 6393a506-8b3e-3145-bcb4-9ff8774e74d1 | -10.3126 | -59.2023 | 2025-08-31 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| c60a4a12-c63a-3799-835e-7c5a05df8860 | -8.8522 | -66.727 | 2025-08-31 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| e1131966-073f-39ac-bc8f-36c27883fded | -3.5995 | -47.5142 | 2025-08-31 01:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 6dbd0c60-ede2-36a9-b06d-dd6340ec5d8c | -9.0799 | -65.4349 | 2025-08-31 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| ae4e1ee0-0b5c-369f-aa31-014ea5431495 | -11.3509 | -43.6133 | 2025-08-31 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| c49a5f42-93a0-3ea1-b60a-08b11aa88a68 | -9.2745 | -67.6433 | 2025-08-31 01:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| c87aae07-f54f-33a9-8356-86d43a31ce0a | -9.0799 | -65.4536 | 2025-08-31 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| cd90d85e-0406-3080-a993-c48565900903 | -16.2217 | -52.6992 | 2025-08-31 01:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| a9f00e76-d61e-3605-825a-624b936a0cad | -10.1359 | -58.0183 | 2025-08-31 01:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 1182f97a-ad9e-3c56-8fcc-a48a1f5cca60 | -12.9192 | -56.9873 | 2025-08-31 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 24e2fc58-e203-3310-a429-c23792c7c3da | -8.6487 | -62.8376 | 2025-08-31 01:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 0cbda101-4882-3dea-8378-92829d01723b | -7.908 | -63.0164 | 2025-08-31 01:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 5ccf61f6-a6f6-3fee-a425-36b0ca486962 | -8.7472 | -61.8465 | 2025-08-31 01:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 78fedb20-8bec-353f-8183-a3f89d3f2a3e | -9.0613 | -65.4542 | 2025-08-31 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 90b0e831-6bc2-3c0b-95f7-954d91fa554a | -9.0614 | -65.4355 | 2025-08-31 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| a36ab67e-329d-3f30-93d3-81ba136d700d | -14.5448 | -51.9943 | 2025-08-31 01:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.8 |
| f0f86eb3-b703-31d5-84f0-ae028ed95fad | -8.6673 | -62.8369 | 2025-08-31 01:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 59.7 |
| eceeb09d-d783-39e2-9ce6-db8b0182c03c | -13.3443 | -46.953 | 2025-08-31 01:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 90.8 |
| d2d89ac7-2237-340b-b29a-3116e73ffc47 | -6.1853 | -43.3257 | 2025-08-31 01:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 2fd558f3-09f4-3268-9c89-9793673b7975 | -11.3504 | -43.637 | 2025-08-31 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 3ab15424-8638-3940-949f-8cf23212a990 | -7.0951 | -44.3128 | 2025-08-31 01:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| eda2633f-1634-3eac-b64a-1e705ac7b28f | -19.0926 | -48.3106 | 2025-08-31 01:20:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 23dc32a9-4d29-33c7-97de-fbf3d0309b48 | -11.8357 | -46.5194 | 2025-08-31 01:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 9375f5dd-1c5d-3022-b1a8-22d95420fd8e | -16.2221 | -52.6778 | 2025-08-31 01:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| ed6236fb-aff2-3478-8bd3-1045256f3040 | -7.0951 | -44.3128 | 2025-08-31 01:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 37a2cbf6-614c-3ea8-8539-559f886aeeb7 | -18.672 | -49.0793 | 2025-08-31 01:20:00 | GOES-19 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 91.2 |
| d4c465bf-8b90-3320-88b1-e774e1321126 | -12.0976 | -44.717 | 2025-08-31 01:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| cc2c30b5-2caf-32d8-b7fa-4f4f6c9e55d1 | -10.3313 | -59.2011 | 2025-08-31 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 9fdcab33-012d-3a76-98db-0dfbdcae661c | -3.8146 | -48.9515 | 2025-08-31 01:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| f03e44f3-3a56-3aa6-81c4-f98d197ff797 | -10.7567 | -59.8175 | 2025-08-31 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| ba59ab32-6539-31c0-9cc4-51709516b819 | -10.1359 | -58.0183 | 2025-08-31 01:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 886a7f48-202a-3d3c-878f-bb299ff3de48 | -7.908 | -63.0164 | 2025-08-31 01:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| c6595422-1529-3605-8e23-f43a09e0dc3c | -3.5995 | -47.5142 | 2025-08-31 01:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| e6b283e9-0925-3c11-b283-9164ee94061a | -11.3509 | -43.6133 | 2025-08-31 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| daff4160-d76f-3a7a-ad76-baf5b7ff93b8 | -8.6673 | -62.8369 | 2025-08-31 01:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 63.9 |
| c7c9ca0f-a526-329e-98db-1ec03c8171ff | -19.1128 | -48.3063 | 2025-08-31 01:20:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 357f6b3e-e00b-3a93-a51d-57f52ab021d1 | -11.3504 | -43.637 | 2025-08-31 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 082f76d5-bb17-3440-b52f-2ddb8e9a5702 | -6.1853 | -43.3257 | 2025-08-31 01:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 6dca541f-1834-3318-8137-4593285f735c | -11.8373 | -46.4287 | 2025-08-31 01:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 5b6d6742-8d7d-3770-917b-ab44b07f46a6 | -18.6715 | -49.102 | 2025-08-31 01:20:00 | GOES-19 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 801c782f-05b2-301f-bbd6-c7fcf105dc6b | -7.1139 | -44.3111 | 2025-08-31 01:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 2a545249-54d9-37c9-9e2b-37bf16a90a35 | -10.3126 | -59.2023 | 2025-08-31 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 6f7a7305-056c-349d-bf70-a4bbd6dd038b | -9.0614 | -65.4355 | 2025-08-31 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 1374815b-061a-35f4-aa0e-796ff7a179cb | -6.1665 | -43.3273 | 2025-08-31 01:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 06a320d9-fa7a-3650-975b-4a21508f640b | -8.7439 | -62.3979 | 2025-08-31 01:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 8dcff2bb-ebbb-3bc7-acd7-6aaf4488f0af | -3.5994 | -47.5359 | 2025-08-31 01:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| fb9f8adb-0936-3f5c-a72c-0020a8211d67 | -13.3636 | -46.95 | 2025-08-31 01:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 78.2 |
| a6aaaeae-82e6-354d-9c6e-598d7df956e0 | -8.7472 | -61.8465 | 2025-08-31 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 324331f2-1689-347e-8d40-e6dc233fd7b9 | -8.6538 | -61.9647 | 2025-08-31 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| eb588ec2-1d21-3476-80b9-4cdd8cc519be | -8.6539 | -61.9457 | 2025-08-31 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 2f25db33-a1ed-32c6-8b89-87937c95068d | -8.6882 | -62.4192 | 2025-08-31 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 8c3bad3c-84e1-3f9d-aa9e-4c91e4f13aad | -8.7471 | -61.8656 | 2025-08-31 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 2018a715-e08d-388c-9989-eeb6106a9c09 | -9.0799 | -65.4349 | 2025-08-31 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 51e4d600-0277-3d1e-b7a7-8ee53e0173f0 | -8.744 | -62.379 | 2025-08-31 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 7f0af462-2a1a-3cf5-918e-c541304f9b1e | -8.6487 | -62.8376 | 2025-08-31 01:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 2b4e5408-3f77-3b9e-a0b3-a6dc860e3a23 | -13.3636 | -46.95 | 2025-08-31 01:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 5c0d9e5e-2ab1-39ca-b2e6-288644ddc911 | -12.0976 | -44.717 | 2025-08-31 01:30:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| fd441d9a-9ed9-3c9f-b68c-d9d90b98c170 | -19.1128 | -48.3063 | 2025-08-31 01:30:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 94281ab5-4412-32c3-bef3-19e79442871d | -10.3126 | -59.2023 | 2025-08-31 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| ceaf1b87-363f-31a5-970a-e3316d823100 | -10.1359 | -58.0183 | 2025-08-31 01:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 52805b5c-64d6-3c49-80fa-029ce28f3dc3 | -6.1853 | -43.3257 | 2025-08-31 01:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |


[Clique aqui para ver as próximas entradas](README9.md)
