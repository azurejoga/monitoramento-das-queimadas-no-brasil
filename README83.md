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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c65115d-6564-35ca-898d-05e02e084449 | -3.53651 | -45.74413 | 2024-11-09 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b2adba1-a6e6-36b0-a5d2-306f3bfe731e | -3.24725 | -53.36219 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e20a758-cbfd-3ae6-8426-a4201b8f0f38 | -1.30493 | -55.72633 | 2024-11-09 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f3f3d6d-a381-3491-8713-6d1b59be0fbf | -1.57338 | -46.84425 | 2024-11-09 04:55:00 | NPP-375D | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81c896a9-cd3e-3598-b5b8-2ba17b1abaaa | -3.58626 | -51.43279 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78e6988b-68ac-3d74-b308-3815178de94f | -1.75942 | -52.68816 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 59519615-a96c-334b-9f1b-18aba14c7771 | -1.45301 | -55.31533 | 2024-11-09 04:55:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 289a0f21-1600-3d22-b10d-c8f4c1efff11 | -2.55122 | -53.97984 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9770d0b4-3377-3c5c-b3ff-4c400a5c2aa0 | -3.58504 | -47.35335 | 2024-11-09 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f9a93756-13e9-364f-ad76-2c086c2ae9f0 | -1.4579 | -52.56319 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20254eb3-8caf-35ff-a405-4b4afb0c80f2 | -1.81304 | -52.25958 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| baee6bb1-0e0f-3c59-bbcd-6c0386014c06 | -3.71002 | -53.75271 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a177c6d2-4469-3950-8710-7799aa864939 | -2.97236 | -51.43291 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cce56b96-22e4-310e-8c38-da86b1b29b3b | -3.53615 | -51.10347 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d96de224-bce9-3ecb-bf2c-a1a5042d3a05 | -2.40597 | -50.30844 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8eda49c0-5a65-36ea-bd67-4dc67dae5b8a | -2.33025 | -48.94337 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5ad221f-c4a5-36c9-bb1c-f1dc03882a0e | -5.04251 | -49.60587 | 2024-11-09 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16d44565-0cd0-3889-9188-6c58af27b54a | -4.3975 | -49.40834 | 2024-11-09 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7de2bac5-6164-3272-98f3-692216212fae | -3.29908 | -50.08333 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20fd0320-8d72-386b-b9a2-fbbb0c915d50 | -1.25643 | -55.71037 | 2024-11-09 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16ed9716-1d49-3c11-9973-97cb6ace3828 | -3.77472 | -51.09878 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7b701de-860d-3837-b911-a58646af7229 | -1.53241 | -52.21946 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58da43ea-c1d5-34b9-9290-9da6e16306ea | -3.98037 | -46.41521 | 2024-11-09 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6be0a158-6eee-39e3-ac98-96f82ba7f34a | -2.27062 | -50.64111 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c24b30d-2601-3c3c-ade0-5b87ccd8f139 | -6.13204 | -42.56115 | 2024-11-09 04:55:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| a161c5b6-67f4-3eec-b1f0-cb0d1355dcbf | -1.15039 | -53.65333 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3598dbaa-af92-3a9d-b961-0bae692b7de1 | -5.2723 | -44.77207 | 2024-11-09 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a223dc5e-2eda-37b7-b07c-2467710d4cf9 | -1.50441 | -51.53114 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc1a15c3-951e-3fbb-9af6-6245951cb99c | -2.10636 | -46.19855 | 2024-11-09 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2dceb11-8d37-3345-8076-69133934210a | -3.38616 | -51.46435 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07fff734-1fcd-3e39-bcd2-5650f91a3969 | -1.51906 | -52.21739 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c1cfd556-16f8-387f-9686-b2aea4b4c68f | -3.08319 | -50.95814 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2994d24c-3396-337c-a4bd-5e7a6a1ebc36 | -2.30588 | -50.73799 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e76ec734-f0bb-37c4-9ab0-5f827bcbc0ba | -3.09721 | -53.32832 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c907e560-5192-3241-b5e1-dafa94f194eb | -0.30094 | -51.72064 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ac96e6c-7c6e-3bee-95a5-c613c59d0416 | -2.87517 | -50.41624 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a5de9932-96cf-372a-82a1-43dcf2ed951e | -4.37479 | -47.46622 | 2024-11-09 04:55:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c6dfc0a-7b52-3c09-aa98-cee2aedfd244 | -3.24298 | -50.27617 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1f88e116-9a56-397e-8cd2-101e52d8f93d | -2.05782 | -52.01318 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f570129-a9ae-39a4-b37c-0255f0ae940a | -3.14647 | -52.97194 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 33986683-f093-337f-b91c-0f755ec304e0 | -2.37502 | -48.57113 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c843dc84-10ec-3ea9-8db2-552aac18e08a | -0.19176 | -60.77051 | 2024-11-09 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44af004e-db66-3246-939f-f2d721c3e0e5 | -3.75075 | -52.10135 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8c47912-9dd0-34e7-bb49-6cf106613730 | -4.24651 | -46.01387 | 2024-11-09 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30e1bdad-46f6-326c-ac79-4a8866dd1d16 | -3.3811 | -50.22775 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2ffb3080-9ceb-316e-bcba-9b1ea2b3dbce | -2.61405 | -51.73358 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd6a5d96-0f97-3e28-a2c5-14cc9b6d952a | -5.21321 | -48.62976 | 2024-11-09 04:55:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55118273-f3ca-3375-bc1e-f1cbbae3702a | -2.82057 | -52.95615 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca982b63-2b67-3083-be48-9f10fafeb9b0 | -2.34071 | -50.51524 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7244d98f-2a67-385e-9982-d3bc4d3b6d6e | -3.23342 | -50.26625 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b7476f8e-73df-38c0-acd0-c53c7b3a0487 | -3.0983 | -51.34111 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec3e97f0-c6ee-341e-9305-8190bce479b6 | -3.92153 | -50.25059 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f623e909-ae39-323f-b5fa-9fc6b5b79414 | -2.27621 | -51.13042 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b71e2231-61c8-3cd6-896e-54b9267ab4a6 | -3.06295 | -48.05901 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 994c5580-4002-3aff-9741-7580999f9fee | -3.68388 | -50.1963 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b0832eb-dffc-35f3-8f18-c8244a5f79d0 | -2.83839 | -48.46659 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 693508a3-3ed6-3f1b-93b4-cfbff3064868 | -2.15459 | -53.66143 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d26c43b7-9f3f-3b09-bfed-ef093e120cea | -1.14875 | -53.66375 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| dae32655-fe3d-3951-8eeb-7a326d7fdad5 | -1.59802 | -52.48906 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7e3535a2-9731-3cac-9c56-2e81078b6be1 | -2.45713 | -53.69411 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 048b7b47-ab9e-314b-ae2e-14e3934ab045 | -2.19483 | -50.229 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 409bf056-4470-3450-9bcb-ecfb18a8c2de | -5.63109 | -44.82773 | 2024-11-09 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe47aa66-f212-375a-ae56-f09275add284 | -4.43745 | -43.64447 | 2024-11-09 04:55:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c42d66e6-e2f8-387c-b2d9-7a49b5395411 | -3.25057 | -53.36271 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eee0e34e-5e54-3b75-86e4-370e19b4548c | -2.67487 | -51.81636 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 15c9af70-4b9a-3100-a05d-eab78f484a5f | -3.00932 | -51.46061 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d4a765e-1cb9-35a5-b21e-5aa4de475bcf | -2.29456 | -49.78286 | 2024-11-09 04:55:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4745619f-aeb7-36b7-8194-aea02f42de7d | -1.43519 | -54.50167 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0641ddfd-b781-3449-bd21-27c5e94b8e35 | 0.8108 | -50.21764 | 2024-11-09 04:55:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d99b0bf3-0739-3211-b845-19d94869a8a6 | -1.62401 | -52.23699 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73f90c39-6ae9-3e6d-a18a-24d3dc3fbfcb | 0.33191 | -50.97026 | 2024-11-09 04:55:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe49f020-66c0-32b5-bc9d-a90adf84468e | -2.20971 | -53.6735 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6428fa45-9286-316f-9aef-25d59cf2f1b8 | -3.60743 | -48.92441 | 2024-11-09 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 51c6715f-7381-3c22-91ae-78980bddc326 | -4.20706 | -48.54465 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 91346a37-ce73-3616-bc3f-4f02bbd99946 | -1.63113 | -52.19165 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59c28dcf-75b8-3988-947a-c83ac132d231 | -3.25619 | -49.92363 | 2024-11-09 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dfc0bd0b-7d85-37b4-88d3-bba061fab854 | -2.19905 | -50.22549 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24f5e652-d831-3825-931f-d62203eb1cc2 | -5.44346 | -43.2604 | 2024-11-09 04:55:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8845494-5ba8-3f21-bc70-3a2a484e6692 | -3.23704 | -50.26679 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| db0f0598-a1f0-3db4-a633-be83adb1e606 | -4.20429 | -50.62025 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 784aa2d0-c7f5-32f6-82cf-575a8093f44e | -1.55863 | -52.26988 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 91344cd8-81c4-3a46-affb-1e13d72b5137 | -1.13142 | -53.60742 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0dddd94-b880-38ac-8cfe-a31398e81fd0 | -2.06952 | -52.26679 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 266a323e-510b-3440-b3ea-9246fa37086d | -2.26051 | -48.97817 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc3431c5-0ac4-3c14-afc9-9e6f51b029a3 | -3.35904 | -51.63793 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2cc65bb-0551-30e5-9992-2ba27d25fa34 | -2.87727 | -49.3768 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7fd2143d-0631-31bd-b896-1261e12a9752 | -2.59679 | -54.0295 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d30bb5b-1a78-32c6-b260-8d0317923efe | -1.22008 | -56.17089 | 2024-11-09 04:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66a6a3df-593e-342b-a22f-82b7e293b039 | 0.68251 | -52.16197 | 2024-11-09 04:55:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a4eeea9-664b-3da8-bcd6-215f624c8968 | -1.21954 | -52.93863 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38dca5d8-6bdd-3de0-b51a-c0298f3f4a88 | -2.65706 | -48.56084 | 2024-11-09 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d56ee1ee-cee3-3019-b5a1-33cf37163048 | -2.38889 | -53.74405 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 52995adf-3a51-316d-a23d-3e98079c4a3a | -0.22674 | -51.63361 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 763c4e44-cfef-3ced-a6bf-f400e0b24d4d | -3.54844 | -43.56593 | 2024-11-09 04:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 603f58e6-8059-36c7-8a5d-9519960df9bf | -3.18472 | -51.11821 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 946e4911-b059-3739-885b-610e4a098d41 | -2.28228 | -48.73612 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 32e214d7-93d6-3a0d-b99f-81aa5bbb9a41 | -5.93057 | -43.65549 | 2024-11-09 04:55:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17d79221-c51a-33ff-be14-4a027b54a359 | -2.67226 | -50.95695 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8a3fd811-57ea-3ae9-8517-64d10828aba9 | -1.18512 | -51.99009 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ca9535a0-c011-3d0f-83b4-3d39e0d66558 | -2.87208 | -51.47015 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README84.md)
