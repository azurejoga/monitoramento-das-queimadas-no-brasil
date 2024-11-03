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
| 01b6f841-a345-3e91-bba5-d909d8b3b09a | -4.2257 | -46.482899 | 2024-11-03 00:25:23 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9b5928fa-6f1c-3cd5-9d83-19ac9c32a976 | -4.2277 | -46.4916 | 2024-11-03 00:25:23 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 874c2451-b2c5-3e0b-94f6-3e8566fc2ebb | -4.2159 | -46.485001 | 2024-11-03 00:25:23 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 173625c2-7b32-3745-af24-2afb5d49ef58 | -3.0734 | -54.167 | 2024-11-03 00:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 125.5 |
| e054cd45-3184-39bd-b318-b377e06d64a4 | -3.0734 | -54.147 | 2024-11-03 00:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 190.5 |
| a1db6be6-b1b7-348b-a103-9ede632abe5e | -3.0917 | -54.1666 | 2024-11-03 00:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| d5430558-ba0f-35da-a370-375f02ea526b | -3.0918 | -54.1465 | 2024-11-03 00:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| c44b98b3-5582-3234-8fa1-4547c2ff1033 | -3.1212 | -51.1244 | 2024-11-03 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 547079f1-6920-32ef-aa49-1d1fb4eb2ccb | -3.1213 | -51.1036 | 2024-11-03 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| f370f94a-7c3a-36bb-9053-c0ff170e2e9d | -3.1281 | -54.266 | 2024-11-03 00:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 86b21bd4-ef21-3f45-8af4-bd8a3996eebf | -3.1282 | -54.2459 | 2024-11-03 00:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 8202b482-2b89-3cdb-ab8d-0dc5a20d4d9f | -3.2047 | -53.4179 | 2024-11-03 00:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 3ce6d218-d39e-31c2-be49-dbbd88be7d84 | -3.2231 | -53.3972 | 2024-11-03 00:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| ee33c875-f461-359f-80e2-5b37202161c9 | -3.2415 | -53.3967 | 2024-11-03 00:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| e2a4d136-a0e2-3ab8-aefc-f70b53a207b6 | -4.7478 | -48.964699 | 2024-11-03 00:25:24 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0d73ae9-b6ba-3bb5-a186-f2bcb8830b1e | -4.1021 | -46.1618 | 2024-11-03 00:25:24 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 36ee2236-8333-3f2a-9076-98da00e53c78 | -4.104 | -46.170101 | 2024-11-03 00:25:24 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8bbc767b-5c02-3869-9c70-58ba97e933b2 | -3.2599 | -53.4164 | 2024-11-03 00:25:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 04cc4915-7915-3a72-87d5-f7d515912e03 | -3.2624 | -52.746 | 2024-11-03 00:25:25 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 0086fc48-7250-3466-9366-25acd8bee0e7 | -3.2624 | -52.7256 | 2024-11-03 00:25:25 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| cf9ef27d-284d-35da-874a-2575f251391f | -3.2808 | -52.7455 | 2024-11-03 00:25:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 4ed2dea8-13a5-3946-b3e6-fc3aec7ad7da | -3.2808 | -52.7251 | 2024-11-03 00:25:25 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| be2765b5-a166-3f1a-99a6-cc90b525cbee | -3.3276 | -50.2825 | 2024-11-03 00:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 7e1da1fb-5998-349c-9832-54a1cbdd5f68 | -3.3277 | -50.2615 | 2024-11-03 00:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 0e8fb623-ee51-3498-b5a0-342265119c34 | -3.3461 | -50.2819 | 2024-11-03 00:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| c40e8a74-fc50-3096-9696-a563a72e8ed8 | -3.3461 | -50.2609 | 2024-11-03 00:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| b99d7b25-856b-3e40-8530-24f7b802b555 | -3.4749 | -50.3826 | 2024-11-03 00:25:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 132.0 |
| 026695f0-5ae3-300e-9788-837c61d819ba | -3.5466 | -50.8611 | 2024-11-03 00:25:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 9d2f9064-fd2b-3a49-91c0-029854e0fb45 | -3.9321 | -45.864201 | 2024-11-03 00:25:26 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1d4f4a8f-49fb-3fdd-b097-ee91b3b4c03d | -3.9223 | -45.866402 | 2024-11-03 00:25:26 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 026d4f47-c29c-338d-944a-d91c0b3cd856 | -3.6875 | -45.146999 | 2024-11-03 00:25:27 | METOP-C | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e9b99f82-2489-3613-b90b-bddb8276147d | -3.6892 | -45.154499 | 2024-11-03 00:25:27 | METOP-C | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1be8f3cc-9f57-3490-b4e8-a566ed97f267 | -3.967 | -48.15 | 2024-11-03 00:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 0420f8ee-1219-37c2-840f-d3fcc965cfdd | -3.3914 | -44.162498 | 2024-11-03 00:25:28 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5e73a713-34ce-3a2d-876c-c9f0013d93cc | -3.393 | -44.169498 | 2024-11-03 00:25:28 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c11104b1-e030-3241-a710-86a4bdf12f17 | -4.5849 | -49.477402 | 2024-11-03 00:25:28 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 016f3a4b-0531-35ad-91e0-1e658f3a7608 | -3.6029 | -45.2285 | 2024-11-03 00:25:29 | METOP-C | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8c8d4d1a-11cb-357d-b3d5-ea09eb1a3e07 | -3.6046 | -45.236099 | 2024-11-03 00:25:29 | METOP-C | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fdd3d0f7-1747-3df3-a944-281ef546e991 | -4.032 | -47.130901 | 2024-11-03 00:25:29 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1e912b78-d5f1-359c-b6e4-c064083961ca | -4.0342 | -47.140301 | 2024-11-03 00:25:29 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 83c21de5-4ae7-326c-85a4-86681d425cf2 | -4.0363 | -47.1497 | 2024-11-03 00:25:29 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a18c0cc3-09c0-3d84-9686-f7221e60de3b | -4.0244 | -47.142399 | 2024-11-03 00:25:29 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| df97bae9-0bb6-3b5b-b3e5-996ddfa52165 | -3.3352 | -44.277802 | 2024-11-03 00:25:29 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 76f695a6-e1ef-357d-b25b-c7fdee1e5c32 | -3.3577 | -44.376202 | 2024-11-03 00:25:29 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8a9f2235-39c1-365f-8e3f-ca0581a2101d | -3.3479 | -44.378399 | 2024-11-03 00:25:30 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c8b4b573-40a6-345d-b271-c2dc80f36a97 | -3.3495 | -44.385502 | 2024-11-03 00:25:30 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5266c3d9-a918-3e82-942d-f336b5dad92c | -4.1678 | -48.6572 | 2024-11-03 00:25:32 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 378b1e17-59ae-3513-a1e2-4fdc25c0ad10 | -3.957 | -48.125801 | 2024-11-03 00:25:33 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fdd2608-a18d-3192-8afa-a760fd77fdd1 | -3.9594 | -48.136501 | 2024-11-03 00:25:33 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a8c660f-96d4-30c4-b9d4-5e436964c8bd | -3.9619 | -48.147301 | 2024-11-03 00:25:33 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3f5b58d-2e00-353a-bd60-2ce40d69e3d8 | -4.8723 | -48.7318 | 2024-11-03 00:25:34 | GOES-16 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| b085be64-7e96-3d6e-9135-215cff61c6f2 | -3.9496 | -48.138599 | 2024-11-03 00:25:34 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7fdd0b2-b827-34ce-a03e-722bc986ac6b | -3.9521 | -48.149399 | 2024-11-03 00:25:34 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94bdd56b-2dad-31ea-a287-875a50aa118d | -3.9423 | -48.335201 | 2024-11-03 00:25:34 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb517da9-6868-3bf3-8f95-20ea969944d6 | -3.9448 | -48.346298 | 2024-11-03 00:25:34 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 260c9778-6f51-3cfc-b8ba-2c1e50c68ff6 | -3.9473 | -48.357399 | 2024-11-03 00:25:34 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e58ef7c-e9d5-352e-b459-7e4a74392591 | -3.9325 | -48.337299 | 2024-11-03 00:25:35 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac1a6458-0899-345a-a634-7a8896728f41 | -3.935 | -48.3484 | 2024-11-03 00:25:35 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 908ee688-99a9-3014-ab33-b9b784628b71 | -3.9375 | -48.359501 | 2024-11-03 00:25:35 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c41cffc-f19d-30a0-b25d-bb6ec08aa0e8 | -3.0697 | -45.012299 | 2024-11-03 00:25:36 | METOP-C | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e9e6f6c5-a520-3812-9adf-63899c2f0ead | -3.0713 | -45.0196 | 2024-11-03 00:25:36 | METOP-C | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 22e875b3-1811-3a57-8b8f-e34713fc2e18 | -3.073 | -45.026901 | 2024-11-03 00:25:36 | METOP-C | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 299d366f-34e0-34a5-9fdb-21c378361184 | -3.3594 | -46.290001 | 2024-11-03 00:25:36 | METOP-C | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 39bd5025-bcca-3107-b866-77ad61818895 | -3.6146 | -47.5131 | 2024-11-03 00:25:37 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa0975dd-9673-3e4e-a30b-0363df8f4f6c | -3.6167 | -47.5228 | 2024-11-03 00:25:37 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79a2fd42-bcdb-3446-aa31-aeb9a4217a77 | -3.6189 | -47.5326 | 2024-11-03 00:25:37 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa1ef67d-746a-374e-9e58-b84cb128b675 | -3.6069 | -47.524899 | 2024-11-03 00:25:37 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a260eb4-4148-3014-82e3-495b86cbf355 | -3.9877 | -49.2747 | 2024-11-03 00:25:37 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cb72a82-ba8f-305c-a6c6-7489874d9d88 | -3.1537 | -45.745098 | 2024-11-03 00:25:38 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3b8c8e5e-2058-31b6-8007-917c96c3a570 | -3.1555 | -45.752899 | 2024-11-03 00:25:38 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 16bf8378-11d5-35d6-b43d-fe997e3c3359 | -2.6432 | -45.175999 | 2024-11-03 00:25:44 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0a93d9dc-cc96-345c-9128-f57f6520b57c | -3.6483 | -49.909801 | 2024-11-03 00:25:45 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e364d4b-7a64-3287-a0d3-75df375a801b | -3.0493 | -47.375401 | 2024-11-03 00:25:45 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e0ff7ce-6d46-37b2-9db3-79ef9ba32abe | -3.0514 | -47.384899 | 2024-11-03 00:25:45 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab12e719-10b8-3e0f-82e9-247dc990a871 | -3.0629 | -47.572498 | 2024-11-03 00:25:46 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab877cb6-75f3-3b34-bbd1-bdc0ead44b8a | -3.6406 | -50.150799 | 2024-11-03 00:25:46 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9005048c-6097-3be3-9380-7b2b406a3dbe | -3.6438 | -50.165298 | 2024-11-03 00:25:46 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32c11b89-4ad4-3038-ba7e-c108a49e0687 | -3.6309 | -50.152901 | 2024-11-03 00:25:46 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86bb54df-910a-351f-b0b7-b6148b7a446e | -3.6341 | -50.1675 | 2024-11-03 00:25:46 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0c82f4e-a5ea-3760-a0e5-9c039febe5e9 | -2.817 | -46.6208 | 2024-11-03 00:25:46 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47e2fff0-d850-3e9d-9826-395dfbcc6a92 | -3.3433 | -49.0485 | 2024-11-03 00:25:47 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0883542-7235-3c65-8f6f-697d2d45f19c | -3.346 | -49.0606 | 2024-11-03 00:25:47 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e3de41d-dff6-39c2-a3db-f65367d83e35 | -3.3336 | -49.050598 | 2024-11-03 00:25:47 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75af20bc-61f3-3c65-8b31-eb41684e30d8 | -3.3363 | -49.062698 | 2024-11-03 00:25:47 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3158639-09ee-30cc-b7aa-adc83c35cc28 | -3.8494 | -51.276501 | 2024-11-03 00:25:47 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 443d0ccb-e47b-3abb-acd1-e99e629d168f | -3.5334 | -50.266102 | 2024-11-03 00:25:48 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ed7e711-bab5-331b-99db-d0df54a9fe35 | -3.5367 | -50.280899 | 2024-11-03 00:25:48 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcd49043-3cb1-3044-b514-7c15c9c030d8 | -3.54 | -50.2957 | 2024-11-03 00:25:48 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55c8aaac-f669-3023-b886-56ab48868e79 | -3.1407 | -48.556301 | 2024-11-03 00:25:48 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 740bdfac-7cfb-3d8b-b09a-33a332e4c53b | -3.1432 | -48.567402 | 2024-11-03 00:25:48 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14e74d06-d634-3d2b-b696-f271d99fb32c | -3.527 | -50.283001 | 2024-11-03 00:25:48 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec72efb3-47af-39d7-a0ee-240e233444b9 | -2.7071 | -46.680698 | 2024-11-03 00:25:48 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7891eb0-7647-3011-80f4-134349d3f904 | -2.57 | -46.122299 | 2024-11-03 00:25:49 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5d7e4d79-344a-3a60-aee3-af67595beb09 | -2.5664 | -46.1063 | 2024-11-03 00:25:49 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ffa264c4-58f9-3f33-9609-5857f5bed7a8 | -2.5682 | -46.1143 | 2024-11-03 00:25:49 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e8fbca62-1202-3fbc-9da1-c133f74971cc | -2.6678 | -46.734299 | 2024-11-03 00:25:49 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4545222-de15-39cf-9116-10ab537a8373 | -2.6697 | -46.742802 | 2024-11-03 00:25:49 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f4ce015-c2f2-35c1-b179-7643151129c1 | -2.6717 | -46.7514 | 2024-11-03 00:25:49 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2449f7c-103c-3db4-85e8-cbeb22347b6d | -2.4585 | -45.8578 | 2024-11-03 00:25:49 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 35bbba43-63e4-3fa8-ad90-4c0cfd284313 | -2.6599 | -46.744999 | 2024-11-03 00:25:49 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
