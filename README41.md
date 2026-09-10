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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 713f03e9-ea58-3427-9715-b4daf4e86cc5 | -6.95669 | -59.75591 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a86a1ec-2b61-3643-81eb-a88ce26d87f4 | -8.82323 | -62.48438 | 2026-09-10 05:48:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55253a58-862f-3b5c-b630-7c480800732f | -6.55023 | -62.89905 | 2026-09-10 05:48:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9f8cb1c9-30d6-38fc-9f74-dde5c8f387a4 | -6.95217 | -59.76008 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc538849-3a29-364d-a923-3299111091b3 | -9.23742 | -65.59406 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 616d4c46-b7c5-3f27-b00c-126f3f255665 | -9.2042 | -65.77755 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3502f137-11f3-342a-9f36-c37c35a21a83 | -8.36086 | -62.92757 | 2026-09-10 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 443075d3-a032-30f3-9fa4-fdda34540ea9 | -6.54744 | -62.89499 | 2026-09-10 05:48:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97da6109-9050-348e-bb09-1fa04a23a92e | -8.8961 | -61.42904 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a56a54be-85b7-3b90-91a1-004badaf96cf | -8.9788 | -60.60637 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c13346b5-cdfa-399f-a08b-3891ef28b916 | -9.0434 | -65.41158 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75e891a6-9cb4-39b5-8f47-0f97242cc507 | -6.96095 | -59.76412 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 90252fc2-964e-3b9d-be23-3ffa4cb35c64 | -6.62645 | -58.37854 | 2026-09-10 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92c1f6db-5904-3e27-96f7-679d98731c17 | -6.7928 | -58.88652 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 849de65c-5413-380c-9615-670f4bfca7c7 | -6.54688 | -62.89852 | 2026-09-10 05:48:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 77d56381-4967-3119-ae7b-22f5b0fc0d09 | -9.15363 | -60.36133 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93c69f34-2f27-380a-99eb-bad575ec1770 | -6.55859 | -62.88951 | 2026-09-10 05:48:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a387f1e0-a2e2-3e6b-8509-9f0f72959665 | -6.77814 | -58.90222 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f440a502-c23b-3b43-b940-13f77e496172 | -8.08614 | -54.85339 | 2026-09-10 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f74c7797-c0fa-38e7-922e-94e43a053063 | -8.82036 | -62.48013 | 2026-09-10 05:48:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdc60024-bad7-3968-9fc4-cdfec02db853 | -6.77592 | -58.61288 | 2026-09-10 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06f8d666-c480-36c5-8855-48d7985335f9 | -6.24193 | -51.68158 | 2026-09-10 05:48:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 83cbc291-c2c5-302b-9d18-05e45039114f | -6.95784 | -59.75883 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6ad4bea-bb3b-34b3-a469-2e01a0a7ba11 | -6.55078 | -62.89552 | 2026-09-10 05:48:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 267bc300-339c-3477-9ca3-cd52aa565cb9 | -4.85447 | -56.01281 | 2026-09-10 05:48:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6fd0f6f7-71e5-3a8d-be87-eef5fdaed55f | -6.78671 | -58.89997 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5232228f-0175-3f67-8a9f-157ffe0b708e | -6.18949 | -55.2747 | 2026-09-10 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef8d847d-1ba4-33e2-aeea-03ec7af89c62 | -6.09003 | -57.89844 | 2026-09-10 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6399e8e-c3ee-3eb9-94aa-21583b1a3206 | -6.76546 | -58.9611 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f503d0a-be1c-3d3a-ad4b-dd383c0560cf | -8.90562 | -61.43884 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3932d787-4200-30b5-8936-d4518bc4dd0d | -6.26111 | -53.11777 | 2026-09-10 05:48:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c20a35be-08d1-330d-88a8-a03e1edab7bb | -8.81524 | -62.49075 | 2026-09-10 05:48:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c0212779-178d-3b91-9497-4fcf1406ffe4 | -9.15875 | -58.30844 | 2026-09-10 05:48:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 583bf40f-861d-362e-8a1e-3f98e0b5466c | -6.50847 | -58.38224 | 2026-09-10 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b588999a-a967-3e99-8d41-1bce2807d066 | -9.00311 | -65.405 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 74a1aebf-8bc9-3a80-878a-f4cbaf538495 | -9.04618 | -65.4157 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c20ae280-d1b7-3ee5-a6fd-2cabefb1d604 | -6.55358 | -62.89957 | 2026-09-10 05:48:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ae827475-0358-369c-b06e-1037d78b39f1 | -9.37424 | -65.46174 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 53fc9a67-ecd8-3ca8-9333-c7ba365e7d15 | -8.90921 | -62.35955 | 2026-09-10 05:48:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3f894ce-0a95-3bd9-92c5-1395d1c0287c | -9.01087 | -65.42092 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12887b15-2dc7-3580-8ec9-ff805812f869 | -8.88833 | -61.43204 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e97ed81f-570f-3ea6-be1b-d258921607e7 | -9.22286 | -63.64624 | 2026-09-10 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65eabe1a-0115-3d73-8662-6abe21ef3d32 | -4.82895 | -55.76117 | 2026-09-10 05:48:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b15a877-65cd-37de-931b-7b641fc1f1d5 | -6.78473 | -58.88533 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1109406-c3f3-3fa1-9d65-a280037591be | -8.8198 | -62.48384 | 2026-09-10 05:48:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f073599b-d386-3b13-ac1d-c719b50b4208 | -6.55524 | -62.88898 | 2026-09-10 05:48:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1c824ab6-6d53-364d-9b82-54538c33d812 | -9.02662 | -65.40883 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 93a81e00-6658-3c33-99e7-2933ffbb9b89 | -8.08904 | -54.85759 | 2026-09-10 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 79bcf547-a886-3a3c-b243-0f0edebb2e02 | -8.89252 | -61.42849 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4da50ec5-4dbd-31ec-8694-d15ed273e916 | -5.59046 | -60.24599 | 2026-09-10 05:48:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7a1ead7-46a5-3bfd-a87c-f0049bd3284b | -8.37044 | -62.93274 | 2026-09-10 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5db81c74-4031-3f47-9c62-10fde97d8c79 | -8.9873 | -60.57547 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eecf4385-6fc3-37e1-9704-16217839e0e0 | -6.77666 | -58.88408 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef7a7057-4118-3109-96d9-7969aae1666c | -6.76717 | -58.61526 | 2026-09-10 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| adb140d2-2f33-38a5-aae3-c93e6200ba42 | -8.98761 | -60.57869 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40831d12-5ca6-32e2-a1b6-30c18dad657b | -8.99002 | -65.41421 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26de908d-1ca4-3e75-8a58-43d4e116766f | -6.76144 | -58.96054 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c5840791-422b-3124-bee7-2719b9e3adbc | -6.81687 | -59.00147 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6014120-0d0b-31c5-97dd-d7a202d1cd2e | -8.89007 | -61.44486 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b756940a-5308-329c-9979-6bad7175d871 | -6.78319 | -58.89585 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 635086d2-32df-3821-93f9-b818cdd87ef2 | -8.68449 | -62.45973 | 2026-09-10 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d055bda4-4991-39ec-aff0-b031edc9e60a | -6.77615 | -58.8876 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a00df51-31c0-34c5-89e1-bf537407f73c | -6.50791 | -58.38601 | 2026-09-10 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cfb65ba6-9aa8-3a70-a162-63267b7617b9 | -8.99395 | -65.41119 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47b7426a-6bfd-3e30-8a21-1d27f84275ab | -6.06181 | -57.79169 | 2026-09-10 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38d763c6-a1b4-3e4f-ab97-885ee7b592cc | -8.99135 | -60.5793 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6324c47-1757-3642-998c-1d6b7012bbfa | -9.0383 | -65.743 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f67d3c5d-7632-35cc-93f1-c52b2f17452c | -9.22341 | -63.6427 | 2026-09-10 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7989d2e-78e0-3bb3-af68-3cf817843b69 | -6.77865 | -58.89873 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd0061e1-ceb5-3747-8193-635e1bbb354e | -9.1625 | -58.31327 | 2026-09-10 05:48:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c82965b3-de05-3188-af6c-7025e7bfc14e | -9.21672 | -63.64164 | 2026-09-10 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 013bf42b-70cf-34e7-8669-2419edbe6859 | -6.4527 | -60.03816 | 2026-09-10 05:48:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d87502b7-0040-30ae-a153-9e54914fc1a8 | -9.15501 | -58.30358 | 2026-09-10 05:48:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d5a915c-6df9-3100-88b2-304c58bd717a | -8.68163 | -62.45547 | 2026-09-10 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af189140-dd48-3ee5-990a-d3e1490010be | -8.65734 | -64.27136 | 2026-09-10 05:48:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 037d8c9e-5a7a-3111-9ee8-fd5907a8f0c8 | -8.89846 | -61.43776 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bc5f950-a230-3a65-b399-ac0d75ea3334 | -6.82166 | -58.99683 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7bcdd4c3-30f3-3d59-897d-ba602c58f432 | -8.76158 | -61.40913 | 2026-09-10 05:48:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb4f5ad9-605c-32bd-b877-9994421c9033 | -9.04676 | -65.41212 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1f56c2a4-3684-30aa-ba30-c48bbdffc598 | -8.98944 | -65.41779 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b25cc1d-cd70-30fb-a9e6-82d7e43ac479 | -5.28492 | -55.96408 | 2026-09-10 05:48:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f95d403a-87c8-378c-b9f8-0eb8e40d49b2 | -9.15935 | -58.30422 | 2026-09-10 05:48:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b13dd8e4-7c08-3f5a-b7d8-20dd7d8fdc70 | -6.18993 | -55.27169 | 2026-09-10 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 831ea851-b35a-38c9-8d02-4dda0649a075 | -9.0456 | -65.41927 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| aa4f39f6-df68-33e4-be8a-d536d2482e19 | -8.15635 | -62.89636 | 2026-09-10 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9f6d092-0dde-3399-b1d8-99a4711cc88f | -9.30172 | -67.69613 | 2026-09-10 05:50:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 289dbeb8-ca99-3cc9-8a3d-a06712ffb7c1 | -10.62379 | -68.61324 | 2026-09-10 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd48e374-1b97-33ac-91ac-37a9cc84e7f1 | -10.60377 | -60.78616 | 2026-09-10 05:50:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee25d034-c72c-3423-aedf-7200fc80824a | -9.15356 | -68.25076 | 2026-09-10 05:50:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5c34bdb-8d43-3d08-b066-6cb6bf1d894b | -13.31256 | -61.65804 | 2026-09-10 05:50:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fea2795f-6e14-3b94-b735-998641dbb5ac | -10.75056 | -60.70509 | 2026-09-10 05:50:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7155363-d905-3177-a8ea-2a8dc063bd75 | -13.21993 | -61.66033 | 2026-09-10 05:50:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 700b597e-1a36-31c4-b80f-f8f69fee1871 | -9.15432 | -68.24619 | 2026-09-10 05:50:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e89a2a8b-77ff-37f4-a03f-62d7c9e76deb | -10.62004 | -68.61256 | 2026-09-10 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36ce566f-844b-3395-9a4c-25dacf87eb92 | -13.28971 | -61.63153 | 2026-09-10 05:50:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6434f4ca-4c68-352c-ab1e-7fb0eb52d084 | -9.91713 | -67.87957 | 2026-09-10 05:50:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 586a7301-2ac6-346f-9a61-e9255287237d | -9.33776 | -68.23669 | 2026-09-10 05:50:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0583db93-7bff-313c-bf11-3bc596a2eb6a | -13.31191 | -61.66255 | 2026-09-10 05:50:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbc4a31f-ba7c-3747-940e-008d2c57b892 | -10.8473 | -60.83184 | 2026-09-10 05:50:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fdb912c2-70b6-3c54-87ce-cf5f6284f56a | -10.9876 | -60.66381 | 2026-09-10 05:50:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README42.md)
