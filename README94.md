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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd1a8497-c17e-3be8-be98-608d54e67c7e | -7.9446 | -63.0717 | 2025-08-24 14:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 5c058371-53da-3493-9698-35ac8858e998 | -11.5245 | -51.8685 | 2025-08-24 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 548a68e6-33bb-37ec-a3f8-443318806da9 | -11.6112 | -46.2337 | 2025-08-24 14:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 2847110a-289d-3dc4-894a-c55947c10461 | -11.7356 | -51.6984 | 2025-08-24 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 101.1 |
| f7f4b698-2f46-3a66-b924-be32b9841a5a | -8.527 | -48.8609 | 2025-08-24 14:20:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 7ac653a0-db82-38bd-afb6-5d38523a93b8 | -5.4364 | -60.1779 | 2025-08-24 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 70ed9e0c-bdc0-38e5-b416-28734757e5aa | -8.0685 | -49.6524 | 2025-08-24 14:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 5581780f-ed66-34d7-879e-3cabadfa24d2 | -10.9145 | -50.7698 | 2025-08-24 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 8bc7e6dd-8fa6-328f-9409-e87f806a4aec | -9.0232 | -65.6982 | 2025-08-24 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| f3e5f87d-7fc6-3fcd-ae48-693dc5d68c0c | -11.5434 | -51.8665 | 2025-08-24 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 813b7623-d645-38c7-b2ae-f0b5ad7d0ed1 | -9.1722 | -59.4629 | 2025-08-24 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| ae0a748e-4da0-3239-98cf-12db46030d6b | -8.4833 | -49.4032 | 2025-08-24 14:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 148.8 |
| eaf3762c-b9f0-343d-a027-28ecdb01cc07 | -7.9225 | -45.9193 | 2025-08-24 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| aba3dda5-d3ba-36d4-8973-1dd616ce192f | -5.7431 | -57.5814 | 2025-08-24 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| e8f910fd-db98-37c0-a186-3e154216e9c7 | -6.6944 | -58.8453 | 2025-08-24 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 33a5771b-f000-3061-9ed0-e0a2eaa1a860 | -15.112 | -48.6459 | 2025-08-24 14:20:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 155.4 |
| a8dbbf38-1b14-32f9-9ae2-0f162f9bac46 | -7.9447 | -63.0528 | 2025-08-24 14:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| e9266a5e-9e0f-3d36-a275-bcdaa4e1fa35 | -6.4357 | -44.5535 | 2025-08-24 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 413.6 |
| fb2a96d3-a7fc-3b18-9e4b-2e2a52e50f1c | -6.436 | -44.5306 | 2025-08-24 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 115.2 |
| c6357785-d778-3881-b28d-41a45c4418fd | -9.1721 | -59.4823 | 2025-08-24 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 5899e516-01a6-379d-bb5b-6f9fd57bbf57 | -8.1304 | -62.8763 | 2025-08-24 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 9156e3e1-ab1d-3d67-abba-4dc88282e525 | -8.7582 | -49.978 | 2025-08-24 14:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 4fe0514f-2f65-36bf-befc-834f1d69956b | -8.7375 | -45.4981 | 2025-08-24 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 368.3 |
| 1b7ed033-88d7-3384-977e-10c99b5d6865 | -10.8075 | -46.4308 | 2025-08-24 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 3d45f5d5-134a-37e3-adcf-e49ed31075c7 | -11.5251 | -50.4898 | 2025-08-24 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 196.6 |
| 258663fe-3c02-35d6-95a7-06e343c06402 | -10.6006 | -50.2058 | 2025-08-24 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 181.3 |
| f9275784-c4bf-3b8f-8de2-5a5abf5d7b16 | -9.2083 | -59.6161 | 2025-08-24 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 217.6 |
| 915860fb-66a6-3d05-92d9-f7a257078201 | -8.7378 | -45.4753 | 2025-08-24 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 245.5 |
| e7e68dab-1975-365a-8654-44b353005377 | -6.1375 | -44.3941 | 2025-08-24 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 1c9269e5-a806-3b23-9c63-36a655f53809 | -8.7591 | -46.7547 | 2025-08-24 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 57b79735-9e49-362b-9808-c8412d3e86c4 | -14.2965 | -52.9999 | 2025-08-24 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 9137ff13-4821-3b10-be67-a8b6611b2c59 | -8.5458 | -48.8592 | 2025-08-24 14:20:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 95cdd88a-b185-32a6-abf7-0145325dc962 | -8.7769 | -49.9763 | 2025-08-24 14:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 120.8 |
| 0a213709-54e7-3fe4-963b-8030767682ea | -7.9631 | -63.071 | 2025-08-24 14:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 76f08736-a408-3ad6-919a-ebb2280ff69d | -5.678 | -41.3987 | 2025-08-24 14:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 110.2 |
| 5bbb2248-37a0-3365-b7f3-7d8c5d7ca5c5 | -14.2968 | -52.9788 | 2025-08-24 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 214.9 |
| 8ec2bbc2-8971-351c-b04a-9b224cd2ee55 | -5.4182 | -60.1593 | 2025-08-24 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| ff24ca0c-f7ca-398e-b796-edc9cc8d2166 | -5.4365 | -60.1588 | 2025-08-24 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 4c74200e-b53a-3b83-8bb2-b1c406a84228 | -15.1115 | -48.6682 | 2025-08-24 14:20:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 127.0 |
| e04c3375-e2a5-37fc-a915-4f14c651fade | -5.663 | -45.136 | 2025-08-24 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 233.0 |
| 61129fbd-193a-39b8-9d0f-df199bab4675 | -8.546 | -48.8376 | 2025-08-24 14:20:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 79.1 |
| a47ded6a-5a9f-3916-b57c-f1b3d76ffe8b | -13.4393 | -47.0287 | 2025-08-24 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 59.0 |
| b942639d-6af1-38d2-8a46-5f48c557432c | -8.7567 | -45.4733 | 2025-08-24 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 148.4 |
| eb28f986-f8e6-378a-9bac-ee084f20a7da | -7.9263 | -63.0535 | 2025-08-24 14:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 4ef724f9-7fde-3199-a77a-4622c3ca6b1f | -5.6628 | -45.1586 | 2025-08-24 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 237.8 |
| 1ae91222-3322-3cbc-b0cd-bc99d03d47e9 | -4.8161 | -43.5423 | 2025-08-24 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 61f3e878-d06e-36d5-9a75-da43b3ee9839 | -11.5921 | -46.2363 | 2025-08-24 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 195.6 |
| ce800b75-59ac-3537-b35a-a7391c641831 | -5.4182 | -60.1593 | 2025-08-24 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 9cb9879e-9e4f-3e6d-be16-422af46985c7 | -5.678 | -41.3987 | 2025-08-24 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 113.8 |
| 9e39418c-83cd-3f1c-b428-8b66cf7a15f9 | -12.7463 | -48.1153 | 2025-08-24 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 292ee7d3-fa50-37b7-a72c-c02a2bdb65d5 | -8.7769 | -49.9763 | 2025-08-24 14:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 75f5efd6-51ab-35fa-829b-86d58bdb5c6a | -11.5254 | -50.4683 | 2025-08-24 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 0850e745-96d2-31f3-9b6d-af99d0a9f73e | -9.1722 | -59.4629 | 2025-08-24 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 0867c4ae-69e6-3a17-ab6b-0ee76d4f7104 | -13.354 | -54.4006 | 2025-08-24 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 5708121a-eb2b-3e79-960a-93b3c30b8f26 | -4.8159 | -43.5656 | 2025-08-24 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| db4a1bff-9b9c-3f2e-8654-ae9baf38df45 | -9.743 | -47.9568 | 2025-08-24 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 8eaaf6c5-75e7-37d9-b8cc-42de6977905a | -5.4365 | -60.1588 | 2025-08-24 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| b39035fe-0bdb-3f33-8e60-e5a1b77b9734 | -8.1304 | -62.8763 | 2025-08-24 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 101.6 |
| f8af6722-fd8f-3491-88c6-0fcce0534624 | -11.1204 | -44.7681 | 2025-08-24 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 5a81e1ef-f3b2-3a6b-88e4-794f63c374c2 | -10.8075 | -46.4308 | 2025-08-24 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 132.0 |
| d186ea27-d2fd-3c83-a340-c59ecc3ff1b0 | -15.1115 | -48.6682 | 2025-08-24 14:30:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 62.8 |
| eb742638-f5a9-3ca2-986e-1f12fcd67e88 | -9.0232 | -65.6982 | 2025-08-24 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 3740b554-805e-3623-8fc0-45eaf82ab0ae | -10.5874 | -47.1527 | 2025-08-24 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 7ebc8373-46bc-38b2-a39b-5016e8b83ed2 | -5.4548 | -60.1773 | 2025-08-24 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| beeb521b-3ec2-35e4-9535-ccbbe8357939 | -6.4357 | -44.5535 | 2025-08-24 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 316.1 |
| b99cecb5-7740-335e-82ab-c3cc868b282c | -13.4612 | -46.8896 | 2025-08-24 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 1f7fef1e-2e7a-3385-a694-64a189ce8ce1 | -8.4833 | -49.4032 | 2025-08-24 14:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 446814be-e3fb-3dbb-bb92-7d9160693eaf | -7.4644 | -44.8976 | 2025-08-24 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.5 |
| caaf6c35-f8ce-3731-a53f-4debee8edc52 | -14.5068 | -53.0998 | 2025-08-24 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 116.9 |
| bff6aff4-4ef4-389a-9df7-86698434de27 | -4.8348 | -43.5412 | 2025-08-24 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 58cb2294-21ca-3abc-a28f-4e841299a99e | -5.7431 | -57.5814 | 2025-08-24 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| a2b22a00-d8ce-3f96-99be-81315e05b176 | -9.0046 | -65.6988 | 2025-08-24 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 01a7852b-25c5-339a-a7de-f051662b55a0 | -8.5082 | -48.8626 | 2025-08-24 14:30:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 83.3 |
| c688182d-6d26-3e9c-8ffb-974b933dad45 | -12.0055 | -61.0201 | 2025-08-24 14:30:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 9560c3c3-8717-3f73-a9f7-d6d0ad349835 | -7.185 | -44.6719 | 2025-08-24 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 51ad363d-db23-3db5-b0a4-80c1120e047f | -6.6944 | -58.8453 | 2025-08-24 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| f7556d6b-caa2-3f14-8765-90fce13a4ad3 | -5.6198 | -60.2295 | 2025-08-24 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| bda280e3-e3d9-35fd-9e2a-ce3dc4b00771 | -8.0685 | -49.6524 | 2025-08-24 14:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 198.0 |
| 19803b6a-e414-3a9d-96fd-8b513df9accc | -8.546 | -48.8376 | 2025-08-24 14:30:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 83.3 |
| b750ba62-94f8-3155-835c-26612d3388c3 | -7.9631 | -63.071 | 2025-08-24 14:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 9ebc1cc8-9dbc-34ff-ab23-5edef0a38482 | -5.8507 | -52.0878 | 2025-08-24 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 79f8d014-fcc9-3003-bdb5-496ec31c66cd | -6.436 | -44.5306 | 2025-08-24 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 1cbc4f29-f96d-3c0a-94ef-49ff339ad827 | -5.663 | -45.136 | 2025-08-24 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 300.5 |
| 13698329-546d-337a-8678-07bf661c7c19 | -11.6112 | -46.2337 | 2025-08-24 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 200.3 |
| 182054fa-92ef-3e3b-8a3f-07b778d99047 | -5.4364 | -60.1779 | 2025-08-24 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 8619380d-08ab-3db9-894c-3189671b2481 | -14.1462 | -53.9802 | 2025-08-24 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 9b549872-df08-365d-9e17-cabd6e9d5dbc | -8.5458 | -48.8592 | 2025-08-24 14:30:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 23b1c846-8a9c-3cd5-a935-0bda4fa0608f | -8.6131 | -62.5929 | 2025-08-24 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 769ff3dc-1b1a-3fc7-9a42-8a18b8533446 | -8.7591 | -46.7547 | 2025-08-24 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 3ae1657e-36ec-3bc5-916e-4472c32375eb | -12.6748 | -47.8143 | 2025-08-24 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 2fb6c098-d9fd-3b99-b809-0c8e4adfb057 | -8.7772 | -49.955 | 2025-08-24 14:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| ad43721e-3895-3185-9396-223996e09008 | -8.7582 | -49.978 | 2025-08-24 14:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| f17d78d0-cfd3-3c5c-9d10-3013fd5fdb5f | -8.527 | -48.8609 | 2025-08-24 14:30:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 165.5 |
| 07ab770e-4e69-30cd-9471-68d6fb900dad | -8.1489 | -62.8756 | 2025-08-24 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 80094ba5-e9f7-3294-8db7-4216855effbd | -8.778 | -46.7528 | 2025-08-24 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| a5ee1044-6a00-3e68-9152-0381e1a2a6f1 | -6.6082 | -48.0412 | 2025-08-24 14:30:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 97.1 |
| f063bdf6-29d1-358a-8873-b1fe64fb4975 | -7.9263 | -63.0535 | 2025-08-24 14:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| c2a61e54-9c53-3b3a-bdd5-dbdce9fa1ca2 | -13.4393 | -47.0287 | 2025-08-24 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 8ed09886-4060-39d3-a463-495c9e9a70e9 | -11.5251 | -50.4898 | 2025-08-24 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 395.6 |
| e5d92ce8-4997-34f8-be84-2530b5b04876 | -10.5937 | -44.331 | 2025-08-24 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |


[Clique aqui para ver as próximas entradas](README95.md)
