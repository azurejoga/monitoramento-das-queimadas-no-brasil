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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af36a090-1e0b-3c61-98e4-978c9c47a6f9 | -9.82453 | -48.9816 | 2024-10-25 04:38:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c447f84-451e-31da-a4b1-2d6009690b9a | -9.82398 | -48.98517 | 2024-10-25 04:38:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3de55195-bc64-3aa4-af6f-2ad37e15e0d5 | -9.82061 | -48.98465 | 2024-10-25 04:38:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9aa8c197-219f-35b1-ba8d-f33444dcdf7c | -9.5855 | -49.64439 | 2024-10-25 04:38:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 35cde63b-4200-3a2c-b7ba-0e5805793fc9 | -9.58495 | -49.64789 | 2024-10-25 04:38:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4117418f-304d-39b5-93fe-bd6b73f4c5f2 | -9.58217 | -49.64386 | 2024-10-25 04:38:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8512d135-f845-394c-bb37-0570b1e50cc1 | -9.58147 | -49.56102 | 2024-10-25 04:38:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31438b85-66e0-305b-a6e3-5bd298daf344 | -9.82516 | -48.98545 | 2024-10-25 04:38:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db6dbb4f-f591-3f7f-a45f-749016edd4e3 | -9.81333 | -48.98718 | 2024-10-25 04:38:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b1db1cf-3844-31b6-a5cd-c0d1a1c17915 | -9.52422 | -49.19085 | 2024-10-25 04:38:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62914fe7-ae6e-3171-8412-7fd2cd5e016e | -9.51522 | -48.95982 | 2024-10-25 04:38:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4e983de-e168-3a53-9ceb-05334b5a35e3 | -3.34937 | -50.32009 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ca9e79d1-efc6-36a4-babe-a7c1fb2c4975 | -3.33417 | -49.95569 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de2c4c4a-295d-3d0f-9610-b695af02ea8b | -3.33332 | -49.72274 | 2024-10-25 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f68c17b2-5097-305e-abac-5b896ad7c583 | -3.3308 | -49.95515 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4977281-ea97-3229-b653-67865209e64b | -3.33023 | -49.95872 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f2687de-c2ae-324f-ace2-3e0600fdb5e9 | -3.32378 | -50.10844 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ea2da56-8eea-369a-a110-b232a685c3e6 | -3.31983 | -50.1115 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b5a4545-28d5-33fb-bbcd-3814a2c33f9e | -3.31341 | -49.5322 | 2024-10-25 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c9f82355-4230-31d0-a742-a326b5d42896 | -3.31062 | -49.52816 | 2024-10-25 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b96bdbf8-1f2d-3327-82e4-9200a7bcd7bd | -3.31006 | -49.53167 | 2024-10-25 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6592c83-9790-3b90-ac73-5af6c0c97822 | -3.30672 | -49.53115 | 2024-10-25 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eadfe976-bdb8-39c7-810c-b5e199d4c995 | -3.30562 | -49.55975 | 2024-10-25 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e355735-f632-3c36-8196-4fa5197bbecd | -3.30228 | -49.55923 | 2024-10-25 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c701b63-3a48-3860-b0ea-51126e9c73d1 | -3.30106 | -50.16403 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 971860c0-ee47-3bcd-a3f4-e1087e0e10a7 | -3.30048 | -50.16764 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a91ab23e-9fab-3b0e-8b8d-c5dc2e3b12d4 | -3.30008 | -50.10471 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eca74130-1faa-356e-8006-39d32ffac1a4 | -3.29824 | -50.15988 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43db0e04-13fa-349f-8b0e-a1db450f1b5a | -3.29767 | -50.16349 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69b3387e-3b42-3d96-90b2-e272dd4a3a58 | -3.29709 | -50.16711 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c110e47b-f14b-3bf5-b77b-e31fbcd2050b | -3.29669 | -50.10418 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40165b97-ae8a-3f83-83c6-ef247e23c3dd | -3.29498 | -49.1155 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41bd6e38-c9fa-3698-b4c5-c888b9752764 | -3.29485 | -50.15934 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 381a87ae-00de-3693-94fa-585ac3f4693d | -3.26968 | -50.07778 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a892afe4-7efc-3ec4-9f0a-9b8ddcb2d483 | -3.26837 | -50.12928 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f1ca009-9174-3781-a2c1-6b249e4d277c | -3.26094 | -50.154 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8de78b6-606f-3e43-a5c9-a8ce6657f729 | -3.25812 | -50.14986 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca2361e9-f664-3fa0-bde7-af761172a7c8 | -3.25754 | -50.15347 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7359b003-9abc-3379-baa6-0999a5ea1828 | -3.25679 | -50.20159 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16f9b0ea-285f-38de-952c-01f785f6f759 | -3.25621 | -50.20523 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88e82d7c-ac20-3f1b-9289-4b772782d68c | -3.25473 | -50.14933 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b29048b-cebd-323c-9dca-64e358a90447 | -3.25339 | -50.20105 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 604e6e77-08fd-3ffa-917f-550f8bfd498d | -3.25281 | -50.20468 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8047dcd7-e7b1-3e6a-993d-dac80a52a1b8 | -3.25099 | -49.49369 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4c2ba282-0a7e-3035-b000-a26dacfe66fe | -3.25 | -50.20052 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a1b20f8-fa42-340b-a03a-290eec0369be | -3.24942 | -50.20414 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d5dfe942-ff80-3b46-824b-f0716e2d19a1 | -3.24911 | -49.49363 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a79fe5ac-189b-376b-bcc4-13f0e52c9578 | -3.24204 | -49.59298 | 2024-10-25 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12e5d9e3-8b77-3310-aeb9-cfd71d993d55 | -3.23624 | -49.12052 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2e355d9d-335b-3b6e-8c8c-ada75476fad6 | -3.23346 | -49.11654 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5d32df7-63b7-31f7-b04e-8a71b198deb9 | -3.23014 | -49.11602 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f73b4d81-34f0-3433-a301-e9edeae3a789 | -3.22959 | -49.11948 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f0cdff6-a179-3a36-84b8-4cac676c1f25 | -3.22736 | -49.11203 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fbd2a6c9-f1df-3d7c-87f6-3d83b6c67902 | -3.22681 | -49.11549 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce623290-fd01-36f4-b9c4-84bbaea7983a | -3.22403 | -49.11151 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 44c5ae5f-739d-30b7-9708-29a74a43bba8 | -3.22343 | -50.16687 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a224d38-da44-3d4f-89a3-feecf48fd0a2 | -3.22286 | -50.17049 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 018abbbe-5751-30d0-be59-100110736ab0 | -3.22004 | -50.16634 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 696cd045-61e8-3322-a96f-2f23f2c2fb0f | -3.21961 | -49.11792 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90080ef6-388a-3d73-9bbb-32d09b8def06 | -3.21947 | -50.16996 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba6f0767-0277-316b-a566-24931c6140b0 | -3.21889 | -50.17358 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a045976e-6d6a-3e88-bae4-32abade864e0 | -3.21664 | -50.16581 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b6e26dd-def9-3393-9360-f201e53da203 | -3.21628 | -49.1174 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 932b4ecc-e579-3fe0-a72e-372718c6e894 | -3.21607 | -50.16942 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42834e47-dcb2-3d5d-aafc-881b6a9eb414 | -3.2155 | -50.17304 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59f3079c-d8de-3fb2-9b4c-49df34aa37ac | -3.21268 | -50.16888 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b25b1d0f-e5ca-38ee-aa6d-3852f10326d9 | -3.21239 | -50.303 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71abcc78-5ff5-3c60-9ddc-1b63ed93e50e | -3.2121 | -50.1725 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd3a6218-586c-300b-a9b5-bb62fe534cf7 | -3.21063 | -49.45532 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cce75d64-8970-3a40-a13b-d64bf458ed6a | -3.20898 | -50.30246 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45de9807-7e63-32c2-8f1f-5cdd13bab074 | -3.17831 | -50.29763 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 67c17a9c-bfe0-340a-960b-879bcdcc6c25 | -3.16779 | -49.53111 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2aa427b6-0329-3fe8-8c9e-c0a9aa8afc1c | -3.16723 | -49.53463 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7f6507f0-0cec-32e3-896e-7adbe9ef5c76 | -3.1655 | -50.3782 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7520f4f5-41b5-3c54-9b00-56e66717abf1 | -3.16231 | -50.46452 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92bcbd54-2e47-3405-87d6-984274766eed | -3.1615 | -50.38133 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c56905af-a60c-3307-8fb1-4dc29738ab66 | -3.15947 | -50.46029 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c866b97b-cf34-3d43-85e8-3eacb28a288f | -3.15889 | -50.46398 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfc2f3b0-4d25-3359-8ac3-0d5039ce4fbb | -3.15715 | -49.77163 | 2024-10-25 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f0ca24b-ff4a-38db-9f68-1d64f80d1a51 | -3.15659 | -49.77517 | 2024-10-25 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3c0e9b8-490a-3f61-94b2-abcb6a4fedf8 | -3.15605 | -50.45974 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e437a073-4a77-3600-b5fd-833f83909182 | -3.15546 | -50.46343 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6ae8eb84-cffb-3947-8b7f-e3520d82d2bd | -3.15487 | -50.46713 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3eaea02e-bdd9-37d2-b036-ffecd5f0cc1e | -3.15379 | -49.7711 | 2024-10-25 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d88c5f98-7a2b-3d3e-8f68-5504bff39ec6 | -3.15321 | -50.45552 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 92f3be02-666d-347c-9c10-244397e93c7a | -3.15262 | -50.4592 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a922f67b-0b5e-3da3-8926-fc47edaa9b90 | -3.15203 | -50.46289 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 93d9d254-2b55-3a5c-874f-7b76ac64f23a | -3.15144 | -50.46659 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a651b0e7-c5ea-3142-906c-c40513af4046 | -3.15043 | -49.77057 | 2024-10-25 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94e02e3a-6e88-3bfd-a930-eb5da1f8b163 | -3.15037 | -50.45129 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 631bb928-81cb-30dd-b44d-d7ccba7026bd | -3.14978 | -50.45497 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1b97ea0a-bffc-3f15-8186-991c070d662a | -3.14919 | -50.45866 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8f1ff182-019c-378d-b989-daf42d2734a7 | -3.14694 | -50.45074 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2999f82b-4b47-3e54-a415-680c24e1e61e | -3.14635 | -50.45443 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0d5f4df5-7968-370f-a07c-77dbfdeeaf50 | -3.14577 | -50.45812 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7d91882a-8f51-346f-aacb-307fcb86d76e | -3.14352 | -50.45021 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5219792-1f6e-3865-b625-6b39468f390c | -3.14293 | -50.45389 | 2024-10-25 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea57dc4f-0c14-3996-a780-d695078f6980 | -3.14047 | -49.53043 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83f5ee1d-4906-3c19-be5f-e8cef6d4e975 | -3.13768 | -49.52639 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cae5360e-c648-3135-8dd5-791383102741 | -3.13712 | -49.52991 | 2024-10-25 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README61.md)
