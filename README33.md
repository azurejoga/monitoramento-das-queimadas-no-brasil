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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 984f8fd0-f906-3de3-8191-8b42df4f80d3 | -6.6145 | -59.9464 | 2026-09-23 01:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| d990d0fd-fc89-36aa-98bf-30f49a7358c8 | -5.7567 | -45.1067 | 2026-09-23 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 32856fd5-c8fc-3145-a8a5-ad5c5d0c1044 | -12.1287 | -50.8263 | 2026-09-23 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 29d5a621-db34-32d0-9017-8ada2069fba5 | -6.3293 | -43.9411 | 2026-09-23 01:30:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 873dcf8e-d206-3840-b024-970c08fe19da | -9.1025 | -61.4299 | 2026-09-23 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 020a9346-7a7d-3314-9f68-368b9d1c798d | -3.2314 | -46.9376 | 2026-09-23 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 241.3 |
| c7a76a63-5b4c-3eef-acce-473442e2c7ef | -3.6763 | -60.5839 | 2026-09-23 01:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 3610ffd9-d108-3d95-8104-ec49d659a22f | -6.6317 | -43.73 | 2026-09-23 01:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 43.4 |
| f4e35bd0-4d65-34c9-98a9-2205254ad279 | -11.7297 | -50.7869 | 2026-09-23 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 107.5 |
| b6130a45-3a13-3911-9c3e-153148c4b4b1 | -6.6815 | -55.0703 | 2026-09-23 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 788c97e5-2fcd-3fb1-aea7-2f7384c0ec34 | -6.5962 | -59.9279 | 2026-09-23 01:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| df9fb739-1a4d-3d1c-aa6f-6724f95691f2 | -5.7565 | -45.1293 | 2026-09-23 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| fd40d533-37e6-3f55-9451-19eab8c9c22a | -6.6129 | -43.7317 | 2026-09-23 01:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 7402afdc-d9c4-3ea9-a2d2-809a834cde58 | -6.0925 | -57.6847 | 2026-09-23 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 38560869-1ec9-39e1-9dee-5ce58466ab4d | -6.1109 | -57.684 | 2026-09-23 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 750113a4-e309-3784-acba-a4639093be53 | -6.6775 | -58.5748 | 2026-09-23 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 40.6 |
| a52d6345-05a1-3f85-9f2b-ce5d75e40c91 | -9.5596 | -65.9799 | 2026-09-23 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 23d8cb9a-5b07-3f02-bfc5-4e8cceed324c | -8.8108 | -44.2525 | 2026-09-23 01:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| f5aa2eb7-c0b8-3573-861f-47e703f0e641 | -8.4985 | -57.6075 | 2026-09-23 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| e6b15c5b-4657-30ea-b235-f6859e638638 | -9.5596 | -65.9985 | 2026-09-23 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 624a2342-5a55-393f-9cdf-8518c8b55780 | -3.6764 | -60.5649 | 2026-09-23 01:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| f1a1245b-52d6-3eda-b87a-61c23f7602a1 | 1.4085 | -50.7451 | 2026-09-23 01:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 327ce8f3-9f05-3176-a1fc-2bc3607e6862 | -8.935 | -61.495 | 2026-09-23 01:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 9368b88d-7470-37de-9667-332f94739ff4 | -3.2313 | -46.9596 | 2026-09-23 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 122.1 |
| becdbe9e-ccd4-3607-9a88-192cb88404aa | -6.1289 | -57.7613 | 2026-09-23 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 5730a5b9-12b6-325a-8ebb-2f275c0f42d0 | -6.5939 | -43.7565 | 2026-09-23 01:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 41.7 |
| ffee10f6-a1fa-364a-9122-6b2baa904b07 | -7.8811 | -61.1779 | 2026-09-23 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 63c99781-492e-3b8a-afff-8c42e7942a31 | -5.7754 | -45.1053 | 2026-09-23 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 96f7509e-ba8d-3778-891a-95e5659e2b53 | -8.9164 | -61.4958 | 2026-09-23 01:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 1eef21ae-ca12-3b32-aa50-addada1bf42a | -5.7752 | -45.128 | 2026-09-23 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 6143bf6e-8c27-3b0d-9349-c597a703d353 | -11.73 | -50.7656 | 2026-09-23 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 041c7dd7-6c5f-3ccd-ab0d-f38345cd8adf | -8.8105 | -44.2757 | 2026-09-23 01:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 9166d454-dada-3b9f-8c19-03af688c7737 | -10.6094 | -53.9902 | 2026-09-23 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 2a3c831b-2687-367f-8686-0f64451f7a84 | -11.5119 | -45.335 | 2026-09-23 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| b4fe5666-1f26-3e5b-a41f-a26f48a47ef6 | -4.0925 | -62.0874 | 2026-09-23 01:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 8e85a279-2dd5-3142-8a9b-6f322c2d2696 | -11.711 | -50.7677 | 2026-09-23 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| b7fce562-f8cb-3fe3-9e5b-6b2b09bfb74e | -11.7107 | -50.7891 | 2026-09-23 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 9f7ecd53-48e8-33df-a789-83b08c6daad3 | -8.4726 | -48.6927 | 2026-09-23 01:30:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 8126531c-3332-37f6-ae34-812c4947a0cf | -6.58 | -43.74 | 2026-09-23 01:30:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53b7b1bb-3783-3f0b-b202-25657afaeefd | -11.71 | -50.81 | 2026-09-23 01:30:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 88c1e3d9-62f9-3068-a476-4b64d980ae9b | -6.64 | -43.75 | 2026-09-23 01:30:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aa917997-0c3a-393c-8626-ed65789f67b0 | -6.61 | -43.83 | 2026-09-23 01:30:00 | MSG-03 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0dd10c0a-1ed2-37a8-9bf0-4dffa3ea5647 | -11.74 | -50.82 | 2026-09-23 01:30:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a3edfcf5-9042-3201-a76a-0ec23637bc24 | -6.61 | -43.74 | 2026-09-23 01:30:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 93a6a42f-f572-32d1-868d-17e3a7d978f7 | -12.73 | -50.88 | 2026-09-23 01:30:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 403de4d0-2fa8-39c1-ab12-d5e88d21d4fb | -6.58 | -43.78 | 2026-09-23 01:30:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0bc8f9af-958f-3ebc-ab6d-68a2fd8d8659 | -6.61 | -43.79 | 2026-09-23 01:30:00 | MSG-03 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 45f57e4b-9803-32b2-a3fc-f352b2a43069 | -6.58 | -43.69 | 2026-09-23 01:30:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2ef39690-4440-3cce-aadf-124f6e8b5668 | -12.79 | -50.91 | 2026-09-23 01:30:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5e3896d6-329f-30f0-a2ac-b69e3ff19a04 | -6.61 | -43.7 | 2026-09-23 01:30:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0ea23905-0bb7-324d-904a-06b9d4f50d7d | -12.76 | -50.9 | 2026-09-23 01:30:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ef78be34-8bfa-3768-9aba-a4036aedd8a9 | -11.73 | -50.77 | 2026-09-23 01:30:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2eeb9848-799e-392d-89e0-c3a08dba9351 | -11.7 | -50.76 | 2026-09-23 01:30:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b96ffe7a-1163-3fea-84c3-8466b8985786 | -3.23 | -46.93 | 2026-09-23 01:30:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ef8291f-630e-37d5-8ef1-c239586bfc53 | -9.55674 | -65.98714 | 2026-09-23 01:39:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.7 |
| aa997daa-e55f-37a4-ac00-db077609144c | -6.7211 | -44.1618 | 2026-09-23 01:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 6ad4af2a-3453-3d88-b40a-6356d89ef75a | -11.6701 | -50.9641 | 2026-09-23 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 0787d6c5-6152-3b84-b3b4-6c826507e508 | 1.4085 | -50.7451 | 2026-09-23 01:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 76.9 |
| ef682593-c977-306b-9c02-a8c368c5453f | -14.6302 | -45.6403 | 2026-09-23 01:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 500468c6-cae7-3a0f-9bae-b878068793fd | -11.5116 | -45.3581 | 2026-09-23 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 052f3013-7b1e-3a62-8a84-50c246b6b5fd | -11.6895 | -50.9406 | 2026-09-23 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 7c6cf90a-86b7-3411-b777-e6785d24e2ed | -11.6704 | -50.9428 | 2026-09-23 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 937ca6d0-f147-323e-8320-fd7246ac2c72 | -11.73 | -50.7656 | 2026-09-23 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 7a95bdd9-d810-37e3-9168-5b549b37fc25 | -11.6916 | -50.7913 | 2026-09-23 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 81715bc3-02cf-3cbc-9488-6a1b04af11ec | -6.3293 | -43.9411 | 2026-09-23 01:40:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| ba5847e5-d24b-346d-80ed-bacac9cae52c | -12.4212 | -46.9777 | 2026-09-23 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 143.1 |
| b0d5b7d5-1582-3843-a5be-ba68ac8a023b | -11.7107 | -50.7891 | 2026-09-23 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 133.3 |
| c06e5172-19f8-3088-b112-af499fd97db8 | -8.4538 | -48.6944 | 2026-09-23 01:40:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 658a3435-8fbd-3684-87b9-9dde2e09deee | -3.8648 | -58.8211 | 2026-09-23 01:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 6deff6ef-94db-3fde-bb07-38c0ef49c797 | -6.633 | -59.9457 | 2026-09-23 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 352c98fb-a271-306c-8cb1-5d772dd760e4 | -9.1025 | -61.4299 | 2026-09-23 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| c33856fa-75d0-3358-9ee0-5ea5eee0ca4a | -6.1289 | -57.7613 | 2026-09-23 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 60cb5426-6339-3878-827c-885b309e834b | -6.1109 | -57.684 | 2026-09-23 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| f07dedb5-5111-3447-b9cf-ef8babf1f485 | -12.402 | -46.9804 | 2026-09-23 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| f2ace2a8-b331-3263-9b30-353ed1bc9ba7 | -8.4985 | -57.6075 | 2026-09-23 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 5f1c01ac-1a36-3329-abc9-b20354154cdd | -11.711 | -50.7677 | 2026-09-23 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 119.2 |
| e79f2857-2446-3d02-b15d-d841caf24373 | -6.6146 | -59.9272 | 2026-09-23 01:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 244.3 |
| d66ee65b-7894-3b9a-b29f-30bcf5347cf4 | -5.6246 | -45.2518 | 2026-09-23 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| fec14f04-fe8d-384b-afe2-13392d31678a | -11.7297 | -50.7869 | 2026-09-23 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| cf801e29-4eda-3649-98f7-93d8a3193b68 | -3.6947 | -60.5645 | 2026-09-23 01:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 8e915aed-9c14-3494-8452-d27e6d930d31 | -3.2313 | -46.9596 | 2026-09-23 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 7d27cfd5-559c-32d9-9ad5-8bb9ebc7936e | -5.7565 | -45.1293 | 2026-09-23 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| bde8e74f-365d-3b54-aa44-e2deb96a915d | -8.4726 | -48.6927 | 2026-09-23 01:40:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 22fe3525-8683-36fb-9a9c-52df655dc177 | -11.5307 | -45.3553 | 2026-09-23 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 4e1c8a15-8c14-3abc-8b8d-afa6fcf1da35 | -10.3131 | -50.5128 | 2026-09-23 01:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| d0156b07-5be0-39e5-a032-e8655049e395 | -5.7567 | -45.1067 | 2026-09-23 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 26ecc7f0-3f01-3ec6-a526-fab9291b8ab3 | -6.6331 | -59.9265 | 2026-09-23 01:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 171.3 |
| 3576a03c-2d12-34da-91e4-3fff9496e154 | -6.6515 | -59.9258 | 2026-09-23 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| b43f71f6-da7a-33eb-9c97-04b33f25744f | -10.6094 | -53.9902 | 2026-09-23 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| a0ee2625-8e9a-3ea4-974d-7bdb7f244d94 | -8.9164 | -61.4958 | 2026-09-23 01:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 9fd3d8d6-316f-3706-b92b-2005150ca362 | -8.9165 | -61.4767 | 2026-09-23 01:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 44fb9d06-6e17-36c0-bc21-e1b2ea60a528 | -5.7754 | -45.1053 | 2026-09-23 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| f5d5c3bb-6e08-3a10-88c8-991aecc4864a | -11.5119 | -45.335 | 2026-09-23 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 9010480b-739f-3b5d-92ce-7c8dd055e46e | -4.0925 | -62.0874 | 2026-09-23 01:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 26.3 |
| ece16542-7d29-3633-ac44-117210d997cc | -4.2951 | -49.1234 | 2026-09-23 01:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 2613baf2-443c-37d7-a436-5cd580a136be | -3.6946 | -60.5835 | 2026-09-23 01:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 107cab24-bf62-3df3-be24-20db1428b418 | -8.9351 | -61.4759 | 2026-09-23 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 09781a32-c957-3ef3-872b-901cdf01f1b9 | -3.2314 | -46.9376 | 2026-09-23 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 201.2 |
| f1fc74a7-80ee-3be1-90e5-6789578c679a | -3.2128 | -46.9602 | 2026-09-23 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 6feb4903-e370-3061-988b-50a113e7fc05 | -10.294 | -50.536 | 2026-09-23 01:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |


[Clique aqui para ver as próximas entradas](README34.md)
