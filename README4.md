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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c006c9cb-c0de-3c1f-8d36-f8ab353fbc7c | -4.5341 | -44.729401 | 2024-10-30 00:07:37 | METOP-C | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8be54be9-f577-3431-8811-638c26c15cce | -4.5369 | -44.7421 | 2024-10-30 00:07:37 | METOP-C | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6a9ef25f-b8ee-37de-a26a-40cfa0d62bd1 | -5.2291 | -47.907902 | 2024-10-30 00:07:37 | METOP-C | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9d664d9e-c51a-34b4-8060-007cf19a505a | -5.2338 | -47.9296 | 2024-10-30 00:07:37 | METOP-C | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bb31f9d0-c619-3452-956a-40355d40a236 | -4.7073 | -45.6535 | 2024-10-30 00:07:37 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7f1cdc2b-55f1-3b18-ace3-3f8171bd833b | -4.7106 | -45.668301 | 2024-10-30 00:07:37 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0184946f-62d8-32a5-8e1e-5ebe0ac9f714 | -4.7204 | -45.713001 | 2024-10-30 00:07:37 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 29c588dd-f9fe-33ce-84d1-9723d065230e | -4.7074 | -45.7001 | 2024-10-30 00:07:37 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 35cb938d-3e54-3e46-8a61-83281c0fb67d | -4.7106 | -45.715099 | 2024-10-30 00:07:37 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8a22ed04-4550-37ed-8285-f38eb4c34140 | -4.7139 | -45.73 | 2024-10-30 00:07:37 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b1e6ca40-ebc4-30e6-999c-c5a0b9da424e | -4.6294 | -45.577801 | 2024-10-30 00:07:38 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fd5596c5-f9d8-3456-bb91-bf61fcfb14c7 | -4.6326 | -45.5924 | 2024-10-30 00:07:38 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 91e0b75d-6007-390b-9fca-cd70b2ec960d | -4.0672 | -43.229599 | 2024-10-30 00:07:39 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a77677e7-9ecc-3435-8fc9-d91d83162610 | -4.0574 | -43.2318 | 2024-10-30 00:07:39 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2dd008e-eba2-38e1-9c02-9cd085131ad2 | -4.0596 | -43.241798 | 2024-10-30 00:07:39 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 64b476fa-bdde-3a8d-95a5-7fad6d5c1891 | -4.1588 | -43.823502 | 2024-10-30 00:07:40 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d2ee151d-8ec0-3483-8e2c-a9ac9fe6203f | -4.1491 | -43.825699 | 2024-10-30 00:07:40 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1b956baf-6c49-3307-99f2-1527fb94b46c | -4.1458 | -44.179298 | 2024-10-30 00:07:41 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd5e4465-8600-3503-a092-2210a00cd062 | -4.1484 | -44.1908 | 2024-10-30 00:07:41 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb8453f7-eb50-3ede-9f2e-3a5bd404e3b1 | -4.1243 | -44.220299 | 2024-10-30 00:07:42 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f20b6790-f205-3822-95b8-77eb22df8f31 | -4.441 | -45.7883 | 2024-10-30 00:07:42 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 88d1386f-f20b-3aad-8794-4c6f235d5942 | -4.4443 | -45.803299 | 2024-10-30 00:07:42 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e8fbc3c7-f659-3332-9e8f-d2c7f99f71fe | -4.4476 | -45.818401 | 2024-10-30 00:07:42 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 163627eb-fedf-3346-bbfc-0768c4b1126d | -4.4345 | -45.805401 | 2024-10-30 00:07:42 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9c23a21b-8b42-3193-ab98-7d671a5ea422 | -4.3499 | -45.652901 | 2024-10-30 00:07:43 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 454b06cf-cbc2-3297-8b44-984d2043ab11 | -4.3531 | -45.667599 | 2024-10-30 00:07:43 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2570333f-99d3-3609-9ad5-ccf398455f39 | -4.5117 | -46.4342 | 2024-10-30 00:07:43 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f0e9e7c1-5f4b-35d8-8a89-1491b70921b6 | -4.5154 | -46.450901 | 2024-10-30 00:07:43 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 85c46d45-5d48-33d1-94c7-48fc315f64e5 | -4.3271 | -45.642601 | 2024-10-30 00:07:43 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e97f9990-5212-326e-8189-16750da45fce | -3.0622 | -40.058498 | 2024-10-30 00:07:44 | METOP-C | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8a45bb00-8f7e-3e88-a9c0-24ac6b3f178c | -3.0638 | -40.065498 | 2024-10-30 00:07:44 | METOP-C | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7b50d09a-b00b-3a67-b8e3-8b5848b8ab7b | -3.0524 | -40.0606 | 2024-10-30 00:07:44 | METOP-C | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2e55b197-e4c8-3b82-b63b-3be39af34494 | -3.054 | -40.0676 | 2024-10-30 00:07:44 | METOP-C | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| eadd37c8-fc2b-3e62-902f-f6a1a63a6741 | -3.4164 | -41.6166 | 2024-10-30 00:07:44 | METOP-C | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2fa2871f-f6c8-3bbb-89cc-ebf351a66da9 | -3.4182 | -41.624599 | 2024-10-30 00:07:44 | METOP-C | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9dc58e57-e662-39e4-9baa-22c91fd9b10a | -3.4783 | -41.981499 | 2024-10-30 00:07:44 | METOP-C | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 89993fbf-41e7-3e41-a6bc-8156ca840d27 | -3.4802 | -41.989899 | 2024-10-30 00:07:44 | METOP-C | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2b62e71e-a808-3812-b88e-92591b1ac686 | -3.4821 | -41.998299 | 2024-10-30 00:07:44 | METOP-C | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 319e877d-87ff-3319-9115-a48a4da5d5ed | -3.4546 | -42.0131 | 2024-10-30 00:07:44 | METOP-C | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 20864104-de8c-3a46-aa1f-68f9c790247d | -4.2979 | -45.648899 | 2024-10-30 00:07:44 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a744dd29-cc65-3e2f-9788-38e62eae21f7 | -3.0191 | -40.276199 | 2024-10-30 00:07:45 | METOP-C | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6d8a79db-325c-3687-9d61-c1f87063233f | -4.1132 | -45.9216 | 2024-10-30 00:07:48 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f9b31964-e785-3e82-bedc-4c3aa09f80ae | -4.1 | -45.9086 | 2024-10-30 00:07:48 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 78d08d08-9dc0-39f4-9fb2-6062e3f68547 | -4.1034 | -45.923698 | 2024-10-30 00:07:48 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 37e03e6d-ced9-341d-9194-5532bdfa1358 | -4.1067 | -45.938801 | 2024-10-30 00:07:48 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 18950a10-9a0b-353e-8ca5-a04c67c977d3 | -3.5446 | -43.5998 | 2024-10-30 00:07:49 | METOP-C | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c4f117b1-f732-353e-9c84-e3c9ea85a8e7 | -3.5469 | -43.610199 | 2024-10-30 00:07:49 | METOP-C | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2836b953-fc03-3d0e-b955-2c2aeb16514d | -4.2022 | -46.695 | 2024-10-30 00:07:49 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d114eeac-2b5d-3f36-b19a-f9baf944061f | -4.0843 | -46.2528 | 2024-10-30 00:07:50 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3903f5c6-3823-386f-bcaf-4a7ef0782cc9 | -4.0878 | -46.2687 | 2024-10-30 00:07:50 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 990e50e3-3ac7-33c3-bbad-db084d4cdcb6 | -4.0746 | -46.254902 | 2024-10-30 00:07:50 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4cf892d7-2d33-3c3d-bc2e-796e06206f7b | -4.0781 | -46.270802 | 2024-10-30 00:07:50 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 084722eb-b39e-3bba-9c05-dfce53d4e0e3 | -3.3371 | -44.366798 | 2024-10-30 00:07:55 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5c276180-e677-3ce5-a307-f10203cbbffd | -4.1382 | -48.115101 | 2024-10-30 00:07:55 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afe51ca0-f0a8-3245-b283-36f9b4ba5cf3 | -3.2517 | -44.397499 | 2024-10-30 00:07:56 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 64fec3d2-0d18-36ad-a4da-cff15e9218e2 | -3.9592 | -48.085899 | 2024-10-30 00:07:58 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c38ea384-1007-3a99-aff3-33dfe94fedc9 | -3.9639 | -48.107201 | 2024-10-30 00:07:58 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b56bc71e-5e7f-3564-a027-e7e36818b46e | -3.9495 | -48.087898 | 2024-10-30 00:07:58 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f196903-2c10-3a6a-97e3-7961c016d299 | -3.9542 | -48.1092 | 2024-10-30 00:07:58 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c3e0818-2dc6-32bb-af19-6f812af96f88 | -3.157 | -44.934601 | 2024-10-30 00:08:00 | METOP-C | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4ab2935d-8eec-3122-b0fb-d789ae4e6a26 | -3.1444 | -44.924198 | 2024-10-30 00:08:00 | METOP-C | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e510ff0d-9953-37bc-94b2-74c8a46d7808 | -3.1472 | -44.936699 | 2024-10-30 00:08:00 | METOP-C | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4671fd55-3ecc-386a-91cc-81b28671db5f | -3.1501 | -44.9492 | 2024-10-30 00:08:00 | METOP-C | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 865e59b0-73f1-3d8e-bb88-b67febc79b20 | -3.5795 | -47.333599 | 2024-10-30 00:08:02 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68286e74-1e95-3f0c-9cdd-fd6b9375bb8f | -3.5837 | -47.3522 | 2024-10-30 00:08:02 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5246266a-3720-3d5c-8374-530229f76889 | -3.5878 | -47.370899 | 2024-10-30 00:08:02 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ed04fa2-71a1-3df8-8e95-d6bd3a0a2f02 | -3.5698 | -47.335602 | 2024-10-30 00:08:02 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32ca6f0b-cc6a-3a41-9720-95053fd45d56 | -3.574 | -47.354301 | 2024-10-30 00:08:02 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0a04af9-9c8b-32cb-8f61-74100b427ebf | -3.5781 | -47.373001 | 2024-10-30 00:08:02 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 335827b4-8b6e-31ce-969f-6dd07ea06577 | -3.5337 | -49.1917 | 2024-10-30 00:08:09 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49af3294-b2d8-332d-b09b-e17e9cdb706d | -3.5241 | -49.193802 | 2024-10-30 00:08:09 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7208e12d-ca3b-3920-80b0-f2cd6d6be92d | -3.2643 | -50.305099 | 2024-10-30 00:08:18 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1f9a708-4c67-3dcb-baf9-f06bd038039f | -3.2547 | -50.307201 | 2024-10-30 00:08:18 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08463110-681b-32e3-a376-7c6b784f9393 | -3.1762 | -50.5453 | 2024-10-30 00:08:20 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfe0a7fc-af1a-37f8-aee4-ae14000fec75 | -3.1666 | -50.547401 | 2024-10-30 00:08:20 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 799cb087-fb0c-3e37-aa0a-04b3f4ab087d | -2.843 | -49.184299 | 2024-10-30 00:08:21 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 703c90cc-d394-3b95-923e-9b2364ee910d | -2.8485 | -49.208698 | 2024-10-30 00:08:21 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbc61b59-80f2-3255-b68d-34c09db24ddf | -2.8334 | -49.186401 | 2024-10-30 00:08:21 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bd097f6-61e1-30be-9222-e6e609bde1cb | -2.8389 | -49.2108 | 2024-10-30 00:08:21 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 121de8cf-21d5-3243-9598-5feac538a4ed | -2.5291 | -49.050701 | 2024-10-30 00:08:25 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd6e819d-2f53-340a-a367-642fffb3880b | -2.5344 | -49.074402 | 2024-10-30 00:08:25 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e1da905-2501-333b-98d2-4d774c90328e | -2.3957 | -48.9086 | 2024-10-30 00:08:27 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8451a7bb-c24b-3607-990d-e268a01c4284 | -1.063 | -47.6452 | 2024-10-30 00:15:12 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 1b0191e1-3aaa-30a6-afa3-a674ebcf7bc5 | -1.5348 | -52.1284 | 2024-10-30 00:15:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 949163e8-7534-36c9-b04a-50cf7e916553 | -2.3906 | -48.9337 | 2024-10-30 00:15:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| e8e8431c-3a0f-3559-9179-fcc9ec4b2241 | -2.8146 | -49.2206 | 2024-10-30 00:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| ea945da5-cd54-37df-bb01-fe30091217b8 | -2.833 | -49.2413 | 2024-10-30 00:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 171.9 |
| 0297cb10-3403-37df-b64f-9c89ec3d3c0c | -2.8331 | -49.22 | 2024-10-30 00:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 21704362-9672-3443-b735-cbcc57ff42d9 | -2.8515 | -49.2408 | 2024-10-30 00:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 453ef6c2-947a-3dff-8f80-5282140ff71a | -3.0734 | -54.167 | 2024-10-30 00:15:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 15cf2953-357a-38a1-9164-358f6076acd5 | -3.0913 | -54.287 | 2024-10-30 00:15:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 78cf4ea4-bfa0-3f06-9fd6-e172c33ff307 | -3.0914 | -54.2669 | 2024-10-30 00:15:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 65a8163d-f669-3e7f-a513-8fe4a32d20d4 | -3.1028 | -51.1041 | 2024-10-30 00:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| dac17178-e8a5-3740-988c-b65a35e6a865 | -3.1097 | -54.2865 | 2024-10-30 00:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 4b85311a-9547-3de4-bdf9-656dbbe410a3 | -3.1098 | -54.2665 | 2024-10-30 00:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 37a465af-4bb5-38d2-bbf6-33c48c010878 | -3.1281 | -54.266 | 2024-10-30 00:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| a6bce6f4-a2c8-3e25-a6b5-b71fcb763b45 | -3.16 | -50.6231 | 2024-10-30 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| a75aa099-f78b-3138-937b-5547bdf95930 | -3.1601 | -50.6021 | 2024-10-30 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 191a4cf2-e76b-39bd-a202-680f9ed91f53 | -3.1602 | -50.5812 | 2024-10-30 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 9e7cd8d4-51c7-3f2f-b734-6fb24b95984c | -3.1786 | -50.6016 | 2024-10-30 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 109.4 |


[Clique aqui para ver as próximas entradas](README5.md)
