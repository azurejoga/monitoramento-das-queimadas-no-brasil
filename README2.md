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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11c36f29-534e-3984-bfe6-7b4b8f86229c | -2.3889 | -49.3755 | 2025-12-17 00:14:00 | METOP-B | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09242172-94e7-3854-a15c-357f627af44a | -1.4457 | -46.870602 | 2025-12-17 00:14:00 | METOP-B | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e911cd36-3061-3800-8b92-8c6489e82cae | -1.4126 | -46.054001 | 2025-12-17 00:14:00 | METOP-B | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cf2e63f0-940f-3585-a71b-0f96aaf85a2a | -1.4223 | -52.563099 | 2025-12-17 00:14:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22a4c352-5d8c-3ce7-8368-ee996b916263 | -3.3323 | -45.415798 | 2025-12-17 00:14:00 | METOP-B | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 51c6b55f-ac02-368f-9ab3-cc09ccf4b951 | -2.1277 | -46.256199 | 2025-12-17 00:14:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 42133595-6dd9-3a86-b061-2aae67581e18 | -4.3996 | -45.755501 | 2025-12-17 00:14:00 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0fb1149e-e92b-31f4-8d81-69ba55b648cb | -3.4854 | -50.8479 | 2025-12-17 00:14:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 530433ab-f93a-37d9-bb2d-a9856284e496 | -4.2906 | -45.332298 | 2025-12-17 00:14:00 | METOP-B | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c2232f09-a6fd-322c-bebc-771e60a9f136 | -2.4021 | -45.618401 | 2025-12-17 00:14:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aa2a7521-5d87-3535-8443-c0dad91bbb2c | -10.3687 | -44.875401 | 2025-12-17 00:14:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 262c31a2-09dc-3ee1-ba93-06eadb7b485e | -5.4696 | -45.397499 | 2025-12-17 00:14:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b6593234-77b1-3d40-9d06-aa71ed516024 | -1.8937 | -46.581001 | 2025-12-17 00:14:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f0df7ed-4a63-395c-a79a-d60d41b629e3 | -3.2976 | -45.487598 | 2025-12-17 00:14:00 | METOP-B | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 87d69721-136a-3fb0-94ab-7d298bd5d09d | -2.7041 | -51.629002 | 2025-12-17 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c077ad5-b1e9-3ac7-811b-50d74f6f3ba8 | -1.4478 | -46.879501 | 2025-12-17 00:14:00 | METOP-B | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c045975-bb2b-3c57-812a-38e0298b52fd | -3.0279 | -45.345299 | 2025-12-17 00:14:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 239447fb-b05e-3719-9875-605bdaffd960 | -2.4068 | -45.638599 | 2025-12-17 00:14:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 06523aa6-497e-386b-80c0-c06d17c60dbf | -0.7058 | -51.991199 | 2025-12-17 00:14:00 | METOP-B | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| bebe519c-c76b-3051-80a6-3704b3a7d313 | -1.4149 | -46.0639 | 2025-12-17 00:14:00 | METOP-B | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8f895255-67e1-3e2d-9fce-9c63b3c944aa | -2.8905 | -49.496799 | 2025-12-17 00:14:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf016589-774c-3d77-945b-b64eb576ac6b | -6.1894 | -39.733398 | 2025-12-17 00:14:00 | METOP-B | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f9b6d913-7d49-3148-b0b9-70a27fc3f098 | -2.6643 | -44.931599 | 2025-12-17 00:14:00 | METOP-B | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f6fffbcc-a9e1-383f-85d1-97f747bc0b73 | -3.3202 | -45.407902 | 2025-12-17 00:14:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fa4f63d8-25b8-3476-9d41-dc70e134d388 | -2.0419 | -45.438999 | 2025-12-17 00:14:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5fbdb24b-acf2-3e9b-8061-fad27e099ec2 | -2.9948 | -52.3708 | 2025-12-17 00:14:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f938c688-702a-397e-816e-1346f60b0531 | -1.8958 | -46.59 | 2025-12-17 00:14:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 655d4cfd-71b5-3575-ac77-db18e05e0b08 | -0.7027 | -51.9771 | 2025-12-17 00:14:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a514b7ee-cb9d-3b7b-b8d0-f03442cb1805 | -2.9861 | -49.101898 | 2025-12-17 00:14:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f58eef96-3c22-3a34-b314-fec30ffbfee6 | -3.4016 | -49.207001 | 2025-12-17 00:14:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9fff813-48b8-36dd-988e-a65a0de7ff36 | -12.6658 | -46.760502 | 2025-12-17 00:14:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0de18008-d08f-3851-be32-6684a1b91ce0 | -7.2236 | -43.070301 | 2025-12-17 00:14:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ab6157b5-fed3-3055-9c71-b597007edd60 | -3.3023 | -45.507702 | 2025-12-17 00:14:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 81a41022-318b-3482-911a-7de132f6dfe1 | -2.9914 | -52.3559 | 2025-12-17 00:14:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 715eaf0c-31f5-37cf-b0f6-c9f50172deb4 | -3.294 | -45.4919 | 2025-12-17 00:20:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 4ea14026-0cf9-3307-a22d-27e7ad590dd3 | -0.7077 | -51.9931 | 2025-12-17 00:20:00 | GOES-19 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 92a8fd85-83dc-3d83-8626-51792c8b9574 | -3.3502 | -45.4223 | 2025-12-17 00:20:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 69.6 |
| ee287927-a42a-3cb8-9b67-6d90b451bcc4 | -2.3632 | -51.9084 | 2025-12-17 00:20:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 24fe39f1-c980-3a42-9433-7e26829eb402 | -3.2939 | -45.5144 | 2025-12-17 00:20:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 75.0 |
| c0565192-c8d6-3c8e-bfdf-8e00d81f827d | -3.3316 | -45.423 | 2025-12-17 00:20:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 9ca13797-40ef-3d26-89d4-cef071ed4105 | -3.3125 | -45.5136 | 2025-12-17 00:20:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 143.3 |
| 352a55b2-169e-3ad5-bc4c-33643c5dd4cf | -2.9875 | -52.3859 | 2025-12-17 00:20:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 86fd03ea-90cd-3949-a24c-8afa36b60b8a | -2.9876 | -52.3654 | 2025-12-17 00:20:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 105a2335-1bb8-3f50-9a31-bee0f9034499 | -3.3317 | -45.4005 | 2025-12-17 00:20:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 5d96dc8f-519d-37f6-acef-854bb0dc9091 | -3.3126 | -45.4912 | 2025-12-17 00:20:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 136.6 |
| 81569662-9ca7-3e2f-bd2a-88eb33279729 | -2.4018 | -45.6349 | 2025-12-17 00:20:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 17d434f4-b7d8-302a-bc29-56ad5450bae0 | -2.9876 | -52.3654 | 2025-12-17 00:30:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 78b146b7-4b2c-3c75-84b5-76b5c29f8573 | -3.3316 | -45.423 | 2025-12-17 00:30:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 62ca12e9-31ba-3678-a643-ca36cf36b6bc | -2.9875 | -52.3859 | 2025-12-17 00:30:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 4a6fd804-a02e-31b8-8c3d-adfc4a2599bd | -3.294 | -45.4919 | 2025-12-17 00:30:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 69.6 |
| fd110f9a-5057-3877-89ce-9fa9c2d2b869 | -3.2939 | -45.5144 | 2025-12-17 00:30:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 77.4 |
| d4680f12-a193-33da-9621-aad868b2ade0 | -3.3311 | -45.5129 | 2025-12-17 00:30:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 64.5 |
| fffe010f-9023-3041-b43a-489543e6d919 | -0.7077 | -51.9931 | 2025-12-17 00:30:00 | GOES-19 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 65.7 |
| b17bc13d-6c5d-326f-bfe8-213d242c0de2 | -3.3125 | -45.5136 | 2025-12-17 00:30:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 144.1 |
| f9d64dc0-8376-3660-a525-79a1b5af13ff | -3.3126 | -45.4912 | 2025-12-17 00:30:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 1bf28693-af37-3e24-96e3-e2509e4cdd8c | -3.294 | -45.4919 | 2025-12-17 00:40:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 80.1 |
| ee565640-e3f6-3a3f-b0b8-824a685b05ce | -3.3312 | -45.4904 | 2025-12-17 00:40:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 5f8113ce-e40f-31ce-a1ba-29f36740aa17 | -3.3316 | -45.423 | 2025-12-17 00:40:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 104.8 |
| acc62e53-f4c3-3523-b8e1-994861462125 | -3.0345 | -45.3447 | 2025-12-17 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 54.8 |
| ff70dda4-c9d0-3adf-b786-e22b042667fd | -3.3125 | -45.5136 | 2025-12-17 00:40:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 148.8 |
| 9e879e4e-de40-3a2b-9e6f-149201da3311 | -2.9875 | -52.3859 | 2025-12-17 00:40:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| cfdb531c-589d-397c-bfa3-3591b5fe0039 | -2.3632 | -51.9084 | 2025-12-17 00:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| eaeeed5e-7be1-3b8f-aa4d-6c79b9e20449 | -9.3794 | -35.9228 | 2025-12-17 00:40:00 | GOES-19 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 73.3 |
| 2f61b66a-c1d8-3665-b5c5-55b46b15fc7c | -2.9876 | -52.3654 | 2025-12-17 00:40:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 4bf14159-1e60-330a-bd9f-2885e7a9b0e0 | -2.3631 | -51.929 | 2025-12-17 00:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| c37345dd-e999-371a-a616-ce1db4593f1a | -3.3311 | -45.5129 | 2025-12-17 00:40:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 36794148-4e10-311a-8f96-978e990c403b | -3.3126 | -45.4912 | 2025-12-17 00:40:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 169.0 |
| fe169778-b733-3dc4-baf2-63c1a5f5cf6b | -3.2939 | -45.5144 | 2025-12-17 00:40:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 71.5 |
| dc422b50-8945-3c23-a0ae-710e83311c7c | -2.9875 | -52.3859 | 2025-12-17 00:50:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 0c43488c-8468-38c4-90ce-1659e9001d65 | -3.3125 | -45.5136 | 2025-12-17 00:50:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 65963f94-5805-391e-bae1-1e8d2f9e6816 | -3.3316 | -45.423 | 2025-12-17 00:50:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 5d8e0686-d689-3d22-915c-383e5c34a441 | -3.3126 | -45.4912 | 2025-12-17 00:50:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 63.8 |
| cae94d13-84c5-36da-9fec-dd0cc4dea562 | -2.9876 | -52.3654 | 2025-12-17 00:50:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 31f8ce3a-6848-3c84-b23b-ee206a0d86f4 | -2.99234 | -52.3688 | 2025-12-17 00:52:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 011d8ece-c802-3772-b5e9-bc78f9788c51 | -2.98372 | -52.38287 | 2025-12-17 00:52:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 3bb7cac4-08a9-3bf6-92ca-43aaff2dd154 | -2.48251 | -49.31625 | 2025-12-17 00:52:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 9a49161e-35ca-36d1-ac2e-c870a0707d61 | -2.70281 | -51.63956 | 2025-12-17 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 6c3dfe24-38f7-3f32-96f4-5fad5161759b | -3.12317 | -54.18045 | 2025-12-17 00:52:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 356021ca-996b-3df5-9d3c-b9b00db5a098 | -1.4259 | -46.07728 | 2025-12-17 00:52:00 | TERRA_M-M | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 6442e32d-687b-3ff5-8a71-c41256e3c5e9 | -2.79619 | -51.40957 | 2025-12-17 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 491cc528-3c58-3c89-8db5-18600aac0841 | -2.68454 | -53.07908 | 2025-12-17 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1598ba0e-7ad5-382b-a635-b7a2d7996f49 | -3.12913 | -54.17309 | 2025-12-17 00:52:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 66066a71-6795-3558-88c3-c78d3f4548ee | -2.99413 | -52.38124 | 2025-12-17 00:52:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 12cb7ec4-a082-3e0d-9e8f-74059d1cd3ed | -2.9819 | -52.3703 | 2025-12-17 00:52:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| c762bb65-8aa9-3b78-8ac8-8c7ee19b0ed3 | -3.12182 | -54.17066 | 2025-12-17 00:52:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| dbced0b4-6a88-3e86-83d7-fb604c631740 | -6.57366 | -51.11754 | 2025-12-17 00:52:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| d71b48c4-c487-3fa1-9644-08b6afe4ffa8 | -2.6716 | -44.942402 | 2025-12-17 00:54:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 43718517-6d89-34a1-a9d8-1755bfc18118 | -2.9876 | -52.3797 | 2025-12-17 00:54:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3793bb0b-0c09-30cc-b081-600462e708a5 | -3.3997 | -49.209702 | 2025-12-17 00:54:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e29c3f1a-9c88-3b5c-8c75-c87705bfd594 | -2.0441 | -45.453499 | 2025-12-17 00:54:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c4640013-f7cd-3dbe-b1a3-50c98fce41ca | -3.3183 | -45.502102 | 2025-12-17 00:54:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 84d4be33-9b24-31ba-aa45-8cd0c230e736 | -3.649 | -46.893398 | 2025-12-17 00:54:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9f40db1a-3bdf-3648-8a1a-895d50901f0e | -3.3301 | -45.422501 | 2025-12-17 00:54:00 | METOP-C | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c43da3ac-dea7-3cbb-851c-9ca2919bdfbe | -2.8964 | -45.5854 | 2025-12-17 00:54:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a17b8760-0431-343b-8f6f-cb2c7b6f8c47 | -2.704 | -51.639702 | 2025-12-17 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0d6a542-984a-328f-a56e-b1736bdbd657 | -2.9062 | -45.583099 | 2025-12-17 00:54:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c218f7dc-65de-3c74-9db7-de10026c2525 | -2.986 | -52.372898 | 2025-12-17 00:54:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34611dad-28b7-35b0-8c4a-792d73c75005 | -3.3266 | -45.407799 | 2025-12-17 00:54:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 53171e3a-e94e-3e2a-bd8c-cd5badb42ec8 | -3.3086 | -45.504398 | 2025-12-17 00:54:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 09f03328-1317-3da5-9574-27f755877edd | -2.2272 | -51.943901 | 2025-12-17 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
