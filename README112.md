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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6789277-9acd-3a7f-86b0-4fa25d196f7f | -1.11665 | -53.61464 | 2024-10-09 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8da74a62-b286-3a92-a71e-c341b98cf6ae | -1.11607 | -53.61824 | 2024-10-09 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 071953dd-8347-32ee-b29e-fb27518eee92 | -1.11574 | -53.61517 | 2024-10-09 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| dd135949-3c54-3018-9d92-03a1e36390d2 | -1.11548 | -53.62184 | 2024-10-09 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7bdb91cc-d296-3b76-8d7f-23de270f19db | -1.11518 | -53.61877 | 2024-10-09 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| ee3d44f6-4700-36e8-bf8a-3334973ef1ac | -1.11462 | -53.62239 | 2024-10-09 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 050878f3-bb72-3a16-8e5e-492d1b9be764 | -1.11251 | -53.61373 | 2024-10-09 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| a7d66e14-3d11-3864-a03c-b41f96fc0a39 | -1.11192 | -53.61736 | 2024-10-09 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 6e4f809c-5ba9-3b58-b544-faaa1c084169 | -1.11159 | -53.6143 | 2024-10-09 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 96fc3fff-7f3e-3f04-bc3c-b9d7575a786c | -1.11132 | -53.62102 | 2024-10-09 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| ee087faa-17c5-35a8-ab3d-e89d6a76cb1e | -1.11101 | -53.61798 | 2024-10-09 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| efd43968-0f3d-396d-b84d-af3d464e65ac | -1.11044 | -53.62169 | 2024-10-09 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 6dfdf611-feb2-32e8-ab92-5866938540f4 | -1.1077 | -53.61689 | 2024-10-09 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 42a9c873-1820-31bc-b5d0-44d63f789178 | -1.1071 | -53.62062 | 2024-10-09 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 4dfbbe3e-a44f-3410-83d7-44d6244f8f95 | -1.1068 | -53.61753 | 2024-10-09 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 34765c74-85f9-3322-b3c5-cd2e7ec6f4c9 | -1.10621 | -53.6213 | 2024-10-09 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1080ad25-f64b-3c83-aa92-178995350e8e | -1.07882 | -46.57878 | 2024-10-09 04:36:00 | NPP-375D | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8dca13b-ae73-3510-8645-ccaa82440b79 | -1.02824 | -53.73316 | 2024-10-09 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae958b9f-c7e0-3623-a47b-059b6bddf084 | -1.02522 | -53.72498 | 2024-10-09 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14dde0e7-e9bf-3677-9dbe-1dbca1a508db | -1.02462 | -53.72873 | 2024-10-09 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 599dcd31-1208-35d7-8433-5cd3b0269cec | -1.02404 | -53.73236 | 2024-10-09 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b36deeee-6dd6-33a6-bc9b-c9d867edecf4 | -1.02046 | -53.72771 | 2024-10-09 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0455e56d-2ae0-3d5e-8231-06b2ec5f7717 | -0.9776 | -48.62289 | 2024-10-09 04:36:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d33127c-3798-33eb-8163-1eee82e75238 | -0.97705 | -48.62636 | 2024-10-09 04:36:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 197cad96-052e-3f30-bbf4-1445a54d72a0 | -0.97427 | -48.62238 | 2024-10-09 04:36:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b0ccee5-8750-31e6-a844-d22284d8cd70 | -0.97372 | -48.62584 | 2024-10-09 04:36:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52ff3e49-b9b8-32b5-a944-c910e85a35bc | -0.83718 | -48.63328 | 2024-10-09 04:36:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ad47e34-4a9b-3e4b-a0cb-8a38f17bfa6e | -0.71118 | -48.03741 | 2024-10-09 04:36:00 | NPP-375D | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70b4fec8-39e8-35e1-8292-978adf90f2ce | -0.70732 | -48.04034 | 2024-10-09 04:36:00 | NPP-375D | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78065c19-36ea-3bc8-9668-74d970fae2b8 | -0.56955 | -52.11685 | 2024-10-09 04:36:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1fa775e-2635-3c86-b9e4-4f693663e881 | -10.3655 | -64.8451 | 2024-10-09 04:36:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 22cea6cc-527e-39e4-a683-f2e3dbda9b05 | -10.3656 | -64.8262 | 2024-10-09 04:36:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 66.9 |
| fb8634a4-8022-361a-add4-92e3d16e9e6b | -10.3894 | -61.2502 | 2024-10-09 04:36:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| e14bb6a8-fe9e-3a7a-8fb9-eeccd94ff5f7 | -10.4287 | -60.9979 | 2024-10-09 04:36:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 5c2d34d1-ebb1-3d2a-9468-cea33b2f7c13 | -10.6256 | -55.9154 | 2024-10-09 04:36:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 6238aac3-cc89-384b-b6c4-1b9a6108cf11 | -10.6258 | -55.8953 | 2024-10-09 04:36:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 9be0a72c-f841-3753-a5ea-8e2433486d46 | -10.6068 | -55.9169 | 2024-10-09 04:36:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 41.6 |
| af758565-acac-34a4-b8cb-2b3d5ea4cf99 | -10.8754 | -63.9169 | 2024-10-09 04:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 72.8 |
| ef386d17-2272-37f1-8d12-4d873cae3ae2 | -10.8755 | -63.8979 | 2024-10-09 04:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 99e4b468-9556-3fa2-9da9-8c190cc53f7c | -11.2583 | -60.3885 | 2024-10-09 04:36:10 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 90f1208f-40c4-3398-bf04-b2a569c118d7 | -11.5233 | -65.137 | 2024-10-09 04:36:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 7686e0ff-05d2-3aeb-853e-8ba6eadb10e2 | -11.693 | -65.0163 | 2024-10-09 04:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 0bc9597f-cce9-3fbf-8ac5-a03c64071fea | -11.6931 | -64.9974 | 2024-10-09 04:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 89.4 |
| ed6c38b4-4981-347c-aab2-f70db837f91f | -11.6806 | -64.0312 | 2024-10-09 04:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 0e58e448-b819-3b05-8868-f2bd1d80d37d | -11.7117 | -65.0155 | 2024-10-09 04:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 155.4 |
| 00364de4-b35d-3c06-9d73-977c1b00e4a8 | -11.7119 | -64.9966 | 2024-10-09 04:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 227.2 |
| af209093-172f-3c59-a113-0cbff0ecf53f | -11.9726 | -51.0788 | 2024-10-09 04:36:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 9f9de360-4c10-3ac2-82f4-362298d985a0 | -11.9729 | -51.0575 | 2024-10-09 04:36:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 094dd97e-68d3-3c09-9ff6-fe94b4c304d9 | -13.288 | -53.6832 | 2024-10-09 04:36:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 3dd880a4-5652-312b-b962-858aa30bcd93 | -13.3786 | -61.9582 | 2024-10-09 04:36:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 5b9b5c08-8992-365f-a71e-79746b8df35a | -13.817 | -44.5961 | 2024-10-09 04:36:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 8384f6c5-9326-32a3-ad9f-efc89682bcf9 | -13.3978 | -61.9376 | 2024-10-09 04:36:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 2adfb8a0-c60f-316a-9944-a09c86170430 | -13.398 | -61.9182 | 2024-10-09 04:36:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 79.1 |
| dcf633fa-3aa7-3de2-a4ae-8d03587bee67 | -13.417 | -61.9169 | 2024-10-09 04:36:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 37c727e1-6d6d-3fae-b446-784625d1e8f3 | -13.8739 | -44.6564 | 2024-10-09 04:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 26103f5e-986f-32f9-847c-49baf8c57220 | -13.8744 | -44.6329 | 2024-10-09 04:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 76c85851-d275-3a02-b88c-d51f4737236b | -16.9091 | -55.8222 | 2024-10-09 04:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 71.1 |
| b793ee09-3ca7-37d2-976b-a54d6fc35aca | -16.8901 | -55.7831 | 2024-10-09 04:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 106.1 |
| 10a65528-5744-3b9b-a7a4-4c94afdb5115 | -16.9098 | -55.7806 | 2024-10-09 04:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 170.9 |
| 771896e9-c1ff-38ca-83e3-509a78f7ceef | -16.9094 | -55.8014 | 2024-10-09 04:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 209.9 |
| 21684f6c-6fc8-3243-b55d-560054d09548 | -16.8898 | -55.8039 | 2024-10-09 04:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 106.1 |
| 142ef482-2cd8-3c57-ad42-ffeaca2db94b | -16.8241 | -57.438 | 2024-10-09 04:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.2 |
| 81dd2c61-6793-390a-a780-44409b970d2d | -16.929 | -55.7989 | 2024-10-09 04:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.8 |
| dd0064ba-a351-35f3-9eb1-858a05284801 | -17.0623 | -56.0308 | 2024-10-09 04:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 82.1 |
| c5888d88-d778-3848-b0ca-5f6e7db02df3 | -18.1193 | -56.3921 | 2024-10-09 04:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.3 |
| 3c8cdf28-6b0f-3cd0-bd31-b5a01f96adbc | -18.9286 | -54.5526 | 2024-10-09 04:36:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 6fd68c14-1450-3fb8-9b5f-71d64fbf1e91 | -19.7927 | -45.6252 | 2024-10-09 04:36:55 | GOES-16 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 389.8 |
| 83956541-4735-32b3-87e5-e79d35cb5fc7 | -19.7934 | -45.6012 | 2024-10-09 04:36:55 | GOES-16 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 484.8 |
| b91c1977-0e92-38ef-acd3-91aab07c4785 | -19.8131 | -45.6202 | 2024-10-09 04:36:55 | GOES-16 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 460.2 |
| c87c409b-a3ef-3423-bf67-8b888928a7c0 | -19.8138 | -45.5961 | 2024-10-09 04:36:55 | GOES-16 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 617.3 |
| f258e910-0276-3a08-a296-19bfe353032d | -20.3346 | -48.7307 | 2024-10-09 04:36:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 224.2 |
| 4c3ce44e-61e2-33a6-a470-677b029ac557 | -20.3352 | -48.7076 | 2024-10-09 04:36:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 160.0 |
| 335cd7d4-6061-3f9d-989f-ec83ace746d8 | -20.3551 | -48.7262 | 2024-10-09 04:36:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 154.3 |
| c6af6881-7bde-3f49-b9fa-2a0ab50fa0ff | -20.3557 | -48.7031 | 2024-10-09 04:36:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 101.5 |
| f2db6d66-08f1-34e8-b5c0-8642b1a32c70 | -8.13109 | -44.41246 | 2024-10-09 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ceaedf5-cb22-30a9-8d3c-4cd8741af08c | -8.23077 | -41.55823 | 2024-10-09 04:38:00 | NPP-375D | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4ad74f59-dafc-3e9a-98ee-fe1c6aa22a34 | -8.14504 | -42.96032 | 2024-10-09 04:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a754b654-12b6-34e6-891f-fe18baa26c4b | -8.14441 | -42.96494 | 2024-10-09 04:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 304322fe-0878-3d0b-808f-cebd4d5773b8 | -8.14371 | -42.96268 | 2024-10-09 04:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d74909b4-01c5-3623-aacd-e62c9f3dc75d | -8.10102 | -41.08447 | 2024-10-09 04:38:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5803343d-991f-34ba-aa95-7e5798d6d12c | -8.10061 | -41.08755 | 2024-10-09 04:38:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 770cef58-c390-3f69-ad60-4da88873109c | -8.10007 | -41.08413 | 2024-10-09 04:38:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 787449dc-b7dd-3b9c-8e74-f3c92cf26a07 | -8.09964 | -41.08718 | 2024-10-09 04:38:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 73e12417-f269-30a1-98aa-7221f2bab41a | -8.09584 | -41.08385 | 2024-10-09 04:38:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3a557792-7fae-36e7-b65f-0c26303ae363 | -8.09544 | -41.08686 | 2024-10-09 04:38:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 518f9eb7-851a-3d61-8f95-b2bd9c90f635 | -8.09489 | -41.08353 | 2024-10-09 04:38:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 201a8f28-e86d-3818-9a56-1a38ba4c04a1 | -8.09447 | -41.08652 | 2024-10-09 04:38:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 50c7c639-9734-3cc0-9b8e-2d78a8f58aa5 | -7.92595 | -42.45201 | 2024-10-09 04:38:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fa74df4b-9f38-3f59-af0c-ee51d552ab3f | -7.92127 | -42.45124 | 2024-10-09 04:38:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 14c23c61-d112-3f86-aadb-3730d0dd4439 | -7.80341 | -43.82775 | 2024-10-09 04:38:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5fac4d00-b6d9-37c2-b116-2421f5949fa6 | -7.79078 | -43.08518 | 2024-10-09 04:38:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d2375ceb-5d27-36a6-80d9-a4da4946504a | -7.78953 | -43.09386 | 2024-10-09 04:38:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| fb42450a-81d9-358d-a931-5282ddfdb5bb | -7.78891 | -43.09817 | 2024-10-09 04:38:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 365c9df4-b494-3cdd-8151-507334e931e6 | -7.7863 | -43.08461 | 2024-10-09 04:38:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 67d96e81-ea94-3f7f-90bf-0a7864a8e094 | -7.77421 | -43.10525 | 2024-10-09 04:38:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5992297d-1ea0-3143-b200-428034d70c52 | -7.77036 | -43.10029 | 2024-10-09 04:38:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 9de9e0c9-4e9d-3b58-af68-830232073116 | -7.76974 | -43.10459 | 2024-10-09 04:38:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e5744131-a16a-318a-b7f6-ba65e16be514 | -7.76654 | -43.09507 | 2024-10-09 04:38:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5ce35d81-838c-3101-aaf5-42bb15c39410 | -7.76592 | -43.09944 | 2024-10-09 04:38:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9207fadc-2fb4-34b2-8559-53e0b9c1561d | -7.7653 | -43.10376 | 2024-10-09 04:38:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |


[Clique aqui para ver as próximas entradas](README113.md)
