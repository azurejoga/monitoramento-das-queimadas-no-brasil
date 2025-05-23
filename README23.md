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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1dcdbcf-5226-381e-ac03-35b8427e7572 | -12.4089 | -49.9762 | 2025-05-23 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 334.0 |
| 9f4ed2cb-364a-361d-9410-2a86691d40f3 | -6.2409 | -43.3911 | 2025-05-23 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 202.2 |
| ed014495-692a-36b3-892a-791338d357ba | -6.9424 | -42.8126 | 2025-05-23 13:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 136.0 |
| 5120fc59-27e2-35b4-b289-7a9154aede3b | -12.3898 | -49.9786 | 2025-05-23 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 511.0 |
| 1b4efddf-96bd-3153-a56f-45c48676f67b | -11.7967 | -57.3627 | 2025-05-23 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 5076b229-db18-3db8-bf73-618a5e3d468b | -10.3293 | -46.6475 | 2025-05-23 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 5c4a18e4-b494-3751-9bcf-fe1c4b79ccaf | -6.9427 | -42.789 | 2025-05-23 13:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 156.7 |
| ea32b264-9164-3f68-af7f-8e4d619e6559 | -10.4922 | -42.409 | 2025-05-23 13:20:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 92.2 |
| 9ec14304-4f9a-37e8-8431-3a4c067092dc | -12.4281 | -49.9738 | 2025-05-23 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 119de9e9-2ee6-30f2-b07a-7ff504d1f5a0 | -6.2411 | -43.3677 | 2025-05-23 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 216.3 |
| 799c38d0-e73d-3df7-82a4-2047ef879605 | -12.4281 | -49.9738 | 2025-05-23 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 111.7 |
| eacde98a-c503-3ffe-8df8-0c0ff144f499 | -6.2411 | -43.3677 | 2025-05-23 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 232.6 |
| dd4cea9f-23a7-315c-814f-ea37ffa4a65e | -14.6615 | -45.0992 | 2025-05-23 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| d97986c1-70f1-3202-b5be-2133c368504f | -6.9427 | -42.789 | 2025-05-23 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 167.4 |
| 77ae6da5-5498-3b14-aaef-5a796b8b9180 | -12.4089 | -49.9762 | 2025-05-23 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 417.7 |
| 65b58d8e-c61f-3294-839b-1ceb966c863e | -6.9424 | -42.8126 | 2025-05-23 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 139.3 |
| 8e58249a-d089-341d-999b-eb3214a715e0 | -6.2409 | -43.3911 | 2025-05-23 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 200.9 |
| bfd5bfdf-35b9-37be-b168-b6b07e6aacb5 | -6.2226 | -43.3459 | 2025-05-23 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 9b28127a-9bb2-37a0-ae2d-5c6137fa1919 | -7.8063 | -46.222 | 2025-05-23 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 4c769c25-da43-347a-9a06-f085a26c65fc | -6.2224 | -43.3693 | 2025-05-23 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 185.2 |
| 937cba95-8aaf-3afe-aaac-1b96ed349094 | -12.3898 | -49.9786 | 2025-05-23 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 515.3 |
| 59f2d2f6-3271-3145-b450-a40a7304a13e | -11.7988 | -44.2733 | 2025-05-23 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 46997f87-ea5f-36fe-b0cb-d358e88db1dc | -6.2411 | -43.3677 | 2025-05-23 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 200.8 |
| a2213968-4bb6-3bf9-b36d-c39a6121d6fd | -6.2409 | -43.3911 | 2025-05-23 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 194.6 |
| 6530dba9-fd9d-33d9-b6c0-7a81c23d7fdc | -12.3331 | -49.9424 | 2025-05-23 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| cfa4318c-95d9-37a1-9c00-de747f274776 | -6.2226 | -43.3459 | 2025-05-23 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 927c7681-e451-323d-8be4-54d614814c85 | -12.3522 | -49.94 | 2025-05-23 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 292.1 |
| 92b88f3a-d2db-32db-a2ad-c4d51661842b | -7.8063 | -46.222 | 2025-05-23 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 882891a4-da15-3209-bc87-ab793e850eea | -6.9427 | -42.789 | 2025-05-23 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 154.3 |
| eaffb8e8-34df-3724-b534-40b7c86933ec | -14.681 | -45.0956 | 2025-05-23 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 7cd8eab9-5048-37d2-8499-5088015646d4 | -11.8156 | -57.3612 | 2025-05-23 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 8d9bb171-183a-364e-80dc-906bd86de323 | -6.9424 | -42.8126 | 2025-05-23 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 129.1 |
| bb8fa0dd-f050-32c3-ad62-2d9cb9552adc | -14.6615 | -45.0992 | 2025-05-23 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 4f43a4e8-87d4-333c-9143-e43395e5166e | -14.681 | -45.0956 | 2025-05-23 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 208f7ebf-c45e-33af-ba8c-6afa2e4e347d | -7.8063 | -46.222 | 2025-05-23 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| cbd82a66-0123-360e-bf3a-6d6f910e4226 | -6.9424 | -42.8126 | 2025-05-23 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 162.4 |
| 16312872-ce01-3572-9638-146bd293ec55 | -10.3293 | -46.6475 | 2025-05-23 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| dc65d45f-aece-398c-bdd0-374e5bd96465 | -6.9427 | -42.789 | 2025-05-23 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 173.0 |
| a9f3bfdc-46d8-3445-af49-e25e114a74db | -11.7967 | -57.3627 | 2025-05-23 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 3f4c16ae-71db-334b-a87b-92ced565202a | -12.9664 | -57.8039 | 2025-05-23 13:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| a1e9a881-bc5e-326e-981d-04933b24a33b | -6.2411 | -43.3677 | 2025-05-23 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 185.3 |
| f081d0f4-ca40-39e3-a610-7aada9ee605f | -11.8156 | -57.3612 | 2025-05-23 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 0f188ddf-5f9a-31df-8951-0342fbb4d463 | -10.5118 | -42.3821 | 2025-05-23 14:00:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 95.9 |
| ee8b6f27-d880-35bf-b7ba-2f1f640f3155 | -7.8063 | -46.222 | 2025-05-23 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| eb803611-c81c-34d3-9f47-908a3cb774c6 | -11.8156 | -57.3612 | 2025-05-23 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| d45124f6-bd4b-34c1-8d90-f372be682182 | -6.9427 | -42.789 | 2025-05-23 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 264.6 |
| 0da1adc5-032d-3ea8-bcd5-77069cf17f19 | -12.3331 | -49.9424 | 2025-05-23 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| fed9f817-3d27-3230-9a02-c263cfc06c93 | -6.9424 | -42.8126 | 2025-05-23 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 184.9 |
| 5d8fa053-6320-3aed-92d5-4d716730a596 | -10.3293 | -46.6475 | 2025-05-23 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 80d9de42-f838-3fb3-b996-5dbeab55a17c | -6.9615 | -42.7872 | 2025-05-23 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 146.5 |
| 7c7bb2ce-a5b9-3baa-8e1f-4a30d72472dd | -7.6574 | -46.1013 | 2025-05-23 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| f7288c05-c486-3210-b968-42b7a3a9bcee | -6.9424 | -42.8126 | 2025-05-23 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 164.8 |
| 086c2b40-4c34-3be4-8e3c-7a88e29a2c3c | -10.3293 | -46.6475 | 2025-05-23 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 541a6d8d-003a-3c2f-9846-765fa033704f | -7.6574 | -46.1013 | 2025-05-23 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| b81f68de-ba6c-3f11-9d1b-0a17d3cc47ca | -11.7967 | -57.3627 | 2025-05-23 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 1c7254b8-ce82-3ffe-bc80-73d78ac5cc94 | -11.8156 | -57.3612 | 2025-05-23 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 7329fba7-6ca2-3756-9d91-d5e96f54d0f3 | -7.8063 | -46.222 | 2025-05-23 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| e51c056c-5907-3b5f-8527-6be0854956e5 | -6.9427 | -42.789 | 2025-05-23 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 186.1 |
| 43135e63-a0c2-35eb-8988-bfed4eb89bc6 | -18.3596 | -55.1662 | 2025-05-23 14:10:00 | GOES-19 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 66.1 |
| ae1eb231-146f-35e5-a29e-d801d0026567 | -6.9615 | -42.7872 | 2025-05-23 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 129.6 |
| 30f43b9c-47ad-34d9-8ec1-1b913cf01044 | -12.9664 | -57.8039 | 2025-05-23 14:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 15ce1ca6-a7e5-399a-ba85-203008cefe95 | -12.3717 | -49.916 | 2025-05-23 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 7d82f301-f3b1-3c26-a6c7-14009755c307 | -18.3596 | -55.1662 | 2025-05-23 14:20:00 | GOES-19 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 67.4 |
| 071ed973-6e2c-3a66-9217-37fbcfc18bfa | -12.9664 | -57.8039 | 2025-05-23 14:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 5f1ad2ba-628f-37c7-bd47-011b7c6e4f47 | -12.3894 | -50.0002 | 2025-05-23 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 299.5 |
| 4833f79b-1c38-3964-ac0d-7183bc6a918c | -10.3293 | -46.6475 | 2025-05-23 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 150.0 |
| ce861002-f161-3ab0-9110-6805d9a86471 | -12.3706 | -49.981 | 2025-05-23 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 143.7 |
| f031633b-dd31-3d0a-8a31-9d26a9b58679 | -11.8156 | -57.3612 | 2025-05-23 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| fcfc162f-7aa3-3ea4-8802-131a6109ce70 | -13.9818 | -56.0151 | 2025-05-23 14:20:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 74a2ca54-c91c-3c11-86e5-72fbc443f740 | -21.4791 | -57.1107 | 2025-05-23 14:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 72c74fe7-dc43-3ecc-9433-6954eabdccb4 | -6.9427 | -42.789 | 2025-05-23 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 190.4 |
| 879774e8-0116-389d-9e35-df90addb9234 | -12.3526 | -49.9184 | 2025-05-23 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 279.2 |
| b0fd69ff-4f28-3707-9577-4aac31aaf070 | -10.3297 | -46.625 | 2025-05-23 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 0cdb6c0b-3634-340c-bfac-f22b00dea241 | -11.7967 | -57.3627 | 2025-05-23 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 8b55985a-d77e-3978-9506-7ac1090af702 | -7.6574 | -46.1013 | 2025-05-23 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 58a287a2-0d66-38d2-8a2c-2399ac20bdb5 | -12.4089 | -49.9762 | 2025-05-23 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 424.4 |
| 5ee2ebea-a40a-3503-aba6-a9c7ddaeddd2 | -6.9615 | -42.7872 | 2025-05-23 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 134.5 |
| 9125cbfb-12a3-3cba-97ff-01912fb8b7f1 | -12.3898 | -49.9786 | 2025-05-23 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 484.1 |
| 217b15cb-9903-3b49-bb15-3a2f15bcafb7 | -6.9424 | -42.8126 | 2025-05-23 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 169.1 |
| caf1ddc6-48b9-3f8f-97db-921dc1162bf3 | -13.1496 | -56.8255 | 2025-05-23 14:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 41835266-e3c3-3794-92a2-50571501399e | -13.9818 | -56.0151 | 2025-05-23 14:30:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 121.1 |
| db358956-e4b9-3a80-b10a-8014f02688ab | -11.7967 | -57.3627 | 2025-05-23 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 9e3cbd93-82ec-31aa-bb35-bb3af747334d | -7.6574 | -46.1013 | 2025-05-23 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| d90f5ead-54c8-32d9-98c3-c6089b9a8210 | -13.1687 | -56.8238 | 2025-05-23 14:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| b7f84113-1453-3959-89fb-f101e688c5a4 | -6.9615 | -42.7872 | 2025-05-23 14:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 113.1 |
| b51ffc2d-a681-30fa-ac6c-87b065345713 | -12.3717 | -49.916 | 2025-05-23 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| c3ff96ca-1133-3633-811c-cdc8566344e9 | -10.5118 | -42.3821 | 2025-05-23 14:30:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 86.6 |
| 0e777693-54fd-3093-b30a-a6bab652d552 | -11.8156 | -57.3612 | 2025-05-23 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 27c76d39-b0fa-3cbf-a637-1e780daa9dd7 | -6.2226 | -43.3459 | 2025-05-23 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 220.6 |
| 5b86b45a-66fb-31de-bfed-68d9e4562cc0 | -7.0695 | -44.9335 | 2025-05-23 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| c1bf851c-2113-3f7b-92bd-1a8191684f77 | -6.9424 | -42.8126 | 2025-05-23 14:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 167.1 |
| eac51b12-7486-3638-b867-8ee02b4418dc | -10.3293 | -46.6475 | 2025-05-23 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 8a84cf5d-109c-3ee2-a8ee-2e418e4cde11 | -12.3526 | -49.9184 | 2025-05-23 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 173.4 |
| c30f29a3-20ca-3d3f-96bb-8cf68ab5da6c | -6.9427 | -42.789 | 2025-05-23 14:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 190.3 |
| 20299d9f-7ff3-3b18-a4a8-86a0347fb553 | -13.1498 | -56.8054 | 2025-05-23 14:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 36cb080a-b31d-3910-a9c8-ebda7d607075 | -10.3297 | -46.625 | 2025-05-23 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 22025206-bc5c-3c28-ace9-04d87668082c | -21.4791 | -57.1107 | 2025-05-23 14:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 8f206b5a-b08a-32ee-8782-b6245211c6db | -14.0328 | -55.13 | 2025-05-23 14:30:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 501784c3-1f5d-3095-ac98-52e422dffb68 | -11.8156 | -57.3612 | 2025-05-23 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 1528c1ca-88b2-3db8-b052-065f1edeba97 | -12.3331 | -49.9424 | 2025-05-23 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |


[Clique aqui para ver as próximas entradas](README24.md)
