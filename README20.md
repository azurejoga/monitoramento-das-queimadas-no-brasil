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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ef7eb7a-0341-3636-b8eb-b3c16b5bceaa | -3.2635 | -50.35072 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d436223-0731-324e-8713-cf044d151347 | -3.26114 | -50.33969 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1a4f15f7-b44e-3d16-9516-80d6cf5f0bfd | -3.2606 | -50.34314 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a53b3f75-647d-3a5e-9e08-6427d90fadef | -3.26005 | -50.3466 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d915be6f-86c7-30bf-9f19-c2211bd5a3cd | -3.2595 | -50.35007 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f41a52d-e8b1-3f3c-a4cf-42b33ebaab33 | -3.25604 | -50.34595 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5727402-6ad7-3e9d-a5ff-88db44e460f2 | -3.25549 | -50.34941 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6652a1c-7284-3e9b-a8c9-1f490627bbd1 | -3.25203 | -50.34531 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ae6858e-3272-37aa-a54c-1395377da84b | -3.24456 | -50.34056 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ecd6397-0392-3811-8ef7-0e096f237913 | -2.80303 | -49.6244 | 2024-10-31 04:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35bd2ee1-95f5-3835-a635-209f54726ae7 | -2.79052 | -49.48193 | 2024-10-31 04:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd034a99-2f37-34ba-b4b6-711164b8826b | -2.78669 | -49.48131 | 2024-10-31 04:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18ce828f-1d5c-3daf-8592-458d1585e1e6 | -2.78216 | -49.55778 | 2024-10-31 04:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5bb4a0e-d984-314a-a2d9-1fc4e96f7c09 | -3.92374 | -49.89905 | 2024-10-31 04:23:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1bcf7f70-1de7-3a14-803a-cff661866041 | -3.65186 | -50.44261 | 2024-10-31 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 45cd4750-aa44-3e69-8f0a-596d414d06f7 | 1.38711 | -50.87204 | 2024-10-31 04:23:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f0d7b25-fa53-371d-a6c7-1d7b6d65d755 | 1.13647 | -50.9381 | 2024-10-31 04:23:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e2d24eb6-e4b1-32de-a05f-8236f247eb74 | 1.13367 | -50.93773 | 2024-10-31 04:23:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 481f6cb7-0703-30b0-ad4c-55531ffbe176 | 1.13201 | -50.93879 | 2024-10-31 04:23:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b817ab9d-4b3a-30e3-8ac4-b4f467aa2547 | 0.06022 | -51.0742 | 2024-10-31 04:23:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4fb91ef9-a65c-3ba1-a9b2-62fc324da525 | 0.05647 | -51.07919 | 2024-10-31 04:23:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a35334f7-e4fb-3d8d-b77d-da9c71ed9a01 | 0.05579 | -51.07488 | 2024-10-31 04:23:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d54be7a7-1aaa-3b15-8d4a-6b61a0ceb154 | -3.53934 | -51.03397 | 2024-10-31 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad49a65c-5783-3168-9beb-bb23ce8c41ac | -3.02164 | -51.45498 | 2024-10-31 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e485569f-6c9e-36db-b538-d6891d63b0ef | -2.83785 | -51.80951 | 2024-10-31 04:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0431c7f8-3dd9-3488-8e37-f41ad083f183 | -2.83411 | -51.80445 | 2024-10-31 04:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49e53dbe-76c2-30e3-86d3-77e8a395d9ac | -2.82966 | -51.80376 | 2024-10-31 04:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c352fcdb-78df-3468-bfc3-60fca2d998ea | -2.82894 | -51.80811 | 2024-10-31 04:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7d80652-e441-30bd-a389-6c83df0440b1 | -2.795 | -51.9459 | 2024-10-31 04:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6db0a8b-c4ab-3ae4-9430-c949443f38e8 | -2.74253 | -51.64956 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f6fa554-39dc-3f2e-89d4-b51b80e4d6e5 | -2.73542 | -51.83075 | 2024-10-31 04:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee90d6a8-0b00-38ff-b6a3-42cc5b9c841e | -2.73417 | -51.72744 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5ad25f4-8898-3048-889d-becceddd4c9c | -2.6417 | -51.74596 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f8499de-b2b8-3ba7-ad33-f1f8a51a00e8 | -2.58321 | -51.92343 | 2024-10-31 04:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c21d02a4-33f6-31b9-8c6b-f2ecaf85ddde | -2.58046 | -51.92212 | 2024-10-31 04:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d9f33b7-efc8-388a-9d3f-393f68db76df | -3.53996 | -51.03015 | 2024-10-31 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97a0c022-e4b3-3e0d-b7dc-abdafdc2d266 | -3.02231 | -51.45092 | 2024-10-31 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1b4c62d4-6544-35a4-83b2-2cbc75328342 | -2.90049 | -51.48366 | 2024-10-31 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efe48a8d-e369-3144-bcb9-13351f118e2e | -2.89614 | -51.48298 | 2024-10-31 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acdf3dff-7b0e-3ec3-8ea3-d2833724e4a5 | -2.80164 | -51.94499 | 2024-10-31 04:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 069e6dd1-e62b-3171-9dc9-b7c21a358b7e | -2.7995 | -51.94664 | 2024-10-31 04:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef98326b-b72f-30c3-830e-c2109faa82c3 | -2.79715 | -51.94426 | 2024-10-31 04:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f60836c3-5a60-3a5e-b3cb-e703a88b4eee | -2.7964 | -51.94873 | 2024-10-31 04:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f2c6c23-9cff-39e2-8c7d-996e0ab1fc4f | -2.74323 | -51.64531 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d7b7f14-9d02-3e07-836f-9a9c72cc260a | -2.7386 | -51.72817 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb33be41-e777-3259-a8c6-259c12ba9f04 | -2.64917 | -51.75613 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a14bdc3-6ce4-3d99-bc94-e03142b42516 | -2.64544 | -51.75104 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bdf80de-7e07-316a-8523-905441ea27ba | -2.64472 | -51.7554 | 2024-10-31 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51d413c1-3ca4-3561-aaeb-2e73909f99aa | -2.58497 | -51.9228 | 2024-10-31 04:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 097da7f9-39ae-3c9b-b609-148679bae61a | -0.69619 | -51.99707 | 2024-10-31 04:23:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63515934-597c-36cb-b0bb-7579938c8b46 | -0.15709 | -51.56158 | 2024-10-31 04:23:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7c70419e-987b-3e61-ba05-e806bb4410d2 | -0.15702 | -51.55995 | 2024-10-31 04:23:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d47a0f0e-05be-34d0-a593-cbd6142130d6 | -0.15628 | -51.56456 | 2024-10-31 04:23:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f0dc619-fa0b-3368-a74b-ce65ef476602 | -1.85887 | -52.03629 | 2024-10-31 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcc56793-a428-3764-99e7-d6f76f8910c3 | -1.8581 | -52.041 | 2024-10-31 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 152d84be-0a7d-3c17-9ed9-12913a7af25b | -1.84056 | -52.12036 | 2024-10-31 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ca10cfae-05dc-352d-b809-45e8f9d5280b | -1.83593 | -52.11963 | 2024-10-31 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b8644ce8-bc6a-328c-9f81-a358c389de90 | -1.82352 | -53.23746 | 2024-10-31 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2e542588-945a-3f20-a49f-1f507df45f70 | -1.74407 | -52.35876 | 2024-10-31 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| df327336-3d77-3ba0-8955-894aaa22b065 | -1.74321 | -52.35717 | 2024-10-31 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 99a892ea-455f-34eb-a1e0-014dd9de22e1 | -1.73929 | -52.35145 | 2024-10-31 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce12e9a0-539d-3c03-afbb-733716606078 | -1.65174 | -52.6548 | 2024-10-31 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5139bdab-2c34-3ea2-a235-7ac966344d83 | -1.64693 | -52.65403 | 2024-10-31 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96f02934-05a6-38dc-9276-4a873710072b | -1.64429 | -52.57927 | 2024-10-31 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 69d14ed6-a249-3201-9830-fa0be907fb0c | -1.64345 | -52.58441 | 2024-10-31 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| aa312f7c-d3c4-367e-b77e-fe7412cb7531 | -1.63951 | -52.57849 | 2024-10-31 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6268af8e-b0e4-382f-8efc-b4c400a58d5d | -1.60396 | -53.20505 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 260d25cd-629d-3fe9-a07e-203bfe4c1373 | -1.60324 | -53.20555 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1432f479-4bed-354f-9449-eb518cabeb77 | -1.57854 | -53.10826 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 367a5916-0463-3bb2-94f1-6dc3d9f786f4 | -1.55943 | -52.03919 | 2024-10-31 04:23:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fa3128c-2aa8-30b5-9663-f5f63ca5db9e | -1.53337 | -52.11325 | 2024-10-31 04:23:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 13072863-3d02-3a70-be3d-195eac5d8566 | -1.5326 | -52.11806 | 2024-10-31 04:23:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 270209bf-399b-3b4a-ae7f-ba37ea139d8f | -1.52873 | -52.1125 | 2024-10-31 04:23:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5af99b53-c497-33cb-9ace-337e07ed7bef | -1.52486 | -52.10695 | 2024-10-31 04:23:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2de0ca54-4c03-37e2-95a4-824878a622d5 | -1.45397 | -52.29852 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 654d1ad4-b245-360c-be06-fef286b01049 | -1.44115 | -52.26801 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7e4c268-e1b4-3e83-b01b-78bb357ff75d | -1.44033 | -52.27293 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e9159b5c-327d-3082-a800-ffcc11a270d3 | -1.43952 | -52.27786 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a8d3e6b7-6985-3bb3-af2e-031f4b84a308 | -1.43902 | -52.2707 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 770244e5-ea78-3cae-85e3-9a9707384b65 | -1.43825 | -52.27564 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3bc923e4-9d4e-35e5-ae9c-d8bf102c6c9b | -1.43747 | -52.28057 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9084a9d0-5a2d-3f78-9388-4c2a6d4a9694 | -1.43645 | -52.26724 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07f9a460-94e8-38c0-8670-54b90c264495 | -1.43564 | -52.27217 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7a101c5c-e560-31cd-8f2e-2efb6e44f99a | -1.43482 | -52.2771 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 58d36e27-3d73-37a8-a7e6-ed1ab7d7a167 | -1.43433 | -52.26992 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fe86abc0-dc81-3194-969a-fbae1f052ce1 | -1.43355 | -52.27487 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 00507ed7-0768-38c9-bcf0-cf0283f73917 | -1.42885 | -52.27409 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c66d6be-4f1f-3b11-a28c-aa14356bbe82 | -1.42879 | -52.21358 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7557b5de-af8b-3b12-a5c0-feb3f6280bc3 | -1.42489 | -52.20792 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 464ed9c9-9b99-382c-af9c-e96387951fdb | -1.41943 | -52.21206 | 2024-10-31 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 656f2799-e36b-315e-a98e-d1132e6a125a | -0.84915 | -51.94889 | 2024-10-31 04:23:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 41c231fb-eb8c-39dc-955f-5b35efaef961 | -0.84797 | -51.94594 | 2024-10-31 04:23:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3220dd55-1cbb-3684-afc8-dd725ca04f6d | -0.84719 | -51.95073 | 2024-10-31 04:23:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d5d1934d-bbad-3cb9-8671-33a13b56672d | -0.84451 | -51.94815 | 2024-10-31 04:23:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 59810916-d841-3513-8d08-70f7b3c0b78e | -0.84334 | -51.94521 | 2024-10-31 04:23:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 41e3bd5c-e004-34b8-806d-bd78ddd34298 | -3.2355 | -53.27314 | 2024-10-31 04:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0bc76973-9065-365e-9641-8392c8e3d1b7 | -3.10565 | -53.12128 | 2024-10-31 04:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 65e18431-635f-36e5-a270-3861f308c39d | -2.78155 | -52.09394 | 2024-10-31 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f867aeb-bc7e-36b0-af5f-4d802d1249a4 | -3.24039 | -53.27397 | 2024-10-31 04:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5e7b1b4e-d190-35b9-96d0-ffd9b55c9696 | -3.23461 | -53.27843 | 2024-10-31 04:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |


[Clique aqui para ver as próximas entradas](README21.md)
