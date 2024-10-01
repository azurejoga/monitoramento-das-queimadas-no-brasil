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

## Dados Diários - Página 143

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b8f2371-27f4-3711-be79-a81edd59cad2 | -11.66392 | -65.0014 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a972da4b-85ea-36ae-bf4a-dec27ff5a7cd | -11.66387 | -65.1944 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba4ab767-df33-3249-a6f3-04979993e6ca | -11.66303 | -65.02815 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a83be1a3-3c6d-33e3-91fe-9891becba15b | -11.66296 | -64.98592 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d719e90-64de-3767-b416-94708315b9c9 | -11.66241 | -65.03191 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0fa7788d-96a8-34f1-97d5-90f1c9d9a9dc | -11.66235 | -64.98965 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2228f804-3782-3e11-9a5d-c243e4902e2c | -11.66173 | -64.99337 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 838994ad-3d64-3b64-836c-52cdb543d811 | -11.66112 | -64.9971 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5ca229bf-a7f0-3d36-b509-53a18e0d8793 | -11.66051 | -65.00082 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9dc2963f-62b6-3539-84dc-f98ec9c9c9e8 | -11.65955 | -64.98535 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1eb1f595-2ee1-35ce-90b3-23b6dc83dc6b | -11.659 | -65.03131 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81cce4db-4d43-3f96-905a-fc5254ea8c97 | -11.65893 | -64.98908 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0f0c2fb4-1e67-3ce2-8dd8-096997913cb0 | -11.65837 | -64.21014 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 45cb312e-a94c-3a4d-93d9-ffb1f8527a00 | -11.65832 | -64.99279 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c7ed87b7-1994-3628-96e5-0f760e35ed53 | -11.65771 | -64.99651 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e7dba08-30fe-34da-94bd-4b4d26deed3f | -11.65723 | -64.21732 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cfe1b4a4-b991-3407-b238-200530e29d31 | -11.65709 | -65.00024 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c834792-ec86-3b35-b1d3-f7eab163a405 | -11.65648 | -65.00397 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ffa7cba-f367-348e-8e03-11ce193f703b | -11.65614 | -64.98478 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19f33d2d-5c50-351b-b429-a125edd37f45 | -11.65552 | -64.98849 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0a9cb435-20a0-3628-a752-fa2af8fbbef1 | -11.65491 | -64.99222 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e6d5c39-8ed6-3f1c-bd8f-d63f15520679 | -11.65445 | -64.21317 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4a12406c-af9c-366c-8d24-5d98cbb7d847 | -11.6543 | -64.99593 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4839d72f-43be-3a30-8b82-c69c569a4f90 | -11.65387 | -64.21676 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f18ebe2e-5430-3613-b5e3-a6bb8b1b9c1e | -11.65368 | -64.99965 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 353312ec-a1d6-3034-a2d9-ff75335e3fc2 | -11.65307 | -65.00339 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02c2f692-681c-34be-9708-f5f11318b6f3 | -11.65245 | -65.00712 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8abe4ade-398b-3dc1-8f1e-adb7954a3aca | -11.65211 | -64.98792 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| edf152e1-47eb-324c-940c-94f7e11cac0a | -11.6515 | -64.99163 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cbe37c8e-d74e-3a15-af1f-6029a6084a7c | -11.65088 | -64.99535 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7463acd1-8b0a-34c4-b96f-8a3cd435eb0e | -11.65027 | -64.99908 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf423cb2-a803-3c31-8e45-2ef1c427bbcd | -11.64842 | -65.01028 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bfc74f09-9de6-3670-9f6f-abefe0aed2e1 | -11.64831 | -64.99213 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 989c4ee6-f18c-3e2e-b8c8-a9c84c2252e0 | -11.64808 | -64.99106 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| caccfad8-4245-35c1-a23d-55e0115b0931 | -11.64771 | -64.99586 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 485b45ad-58e2-396d-a5e1-ec438d654e8f | -11.64747 | -64.99478 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc4e756e-886f-3050-ba4a-ccbb174246ba | -11.64489 | -64.99155 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcab244e-6d67-335e-900c-63474a12f384 | -11.64429 | -64.99528 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 570e6398-4079-3096-b31b-4a2405305756 | -11.63807 | -64.99039 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3a97455-c594-329e-9ca2-e3010d99db50 | -11.63675 | -64.02321 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2d37fa4-ba6e-38e7-8d37-212a744e03d3 | -11.63466 | -64.98981 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61367d6c-d06d-3588-bc80-58efe871bfd9 | -11.63405 | -64.99353 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87d57648-4b97-3390-a808-90219031b7d9 | -11.63341 | -64.02265 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ca7007fe-4cc2-3c44-8875-972696003809 | -11.63064 | -64.99295 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f78b60cd-d4e8-3be1-980b-d06e6d6426d5 | -11.62662 | -64.99611 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04e3215d-28f9-309b-b972-e9da1427c7c9 | -11.62601 | -64.99985 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da649d76-cde7-387f-bf3c-8b9e05a980c8 | -11.6232 | -64.99554 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0bafff2-1ca3-3606-b4d9-0484926ecfdd | -11.6226 | -64.99928 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdd0b879-0dbb-31b2-8002-bc8c7ae6b93c | -11.61918 | -64.9987 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f34fdd08-7ee1-38ca-8be0-299d9fea6074 | -11.61797 | -65.00617 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6861d96f-e68e-3a25-9f0d-e9c8898ebf6c | -11.61455 | -65.00559 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 970bdd1a-6b8f-3f31-98e4-ec5220a9351a | -11.59959 | -63.97692 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8929aa3-7854-30c3-ad0a-e0467eef7961 | -11.58506 | -65.14339 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d16aaf57-123a-3324-aeed-c9eade159b17 | -11.58163 | -65.14281 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 117fc983-38e6-3b8d-bc53-ca30c8183873 | -11.57884 | -63.79528 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76e0077c-d96d-3f23-875c-5180f7132d74 | -11.57828 | -63.79884 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf6b5d30-4489-359f-a68d-3ede9fe67c2e | -11.57438 | -63.80183 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cc1fd2b-34a1-33ab-8f9c-761f6f11d24f | -11.57381 | -63.80537 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e916dbcf-bddd-3940-910d-6b810cdbc970 | -11.57048 | -63.80483 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19c94d55-42fa-3e91-be56-aadb0009ee65 | -11.56991 | -63.80837 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6f936c1-34da-3c36-94cf-86c662ec31bc | -11.56935 | -63.81192 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63f43b53-4027-30a0-93f1-a8c8c7ce8382 | -11.56879 | -63.81547 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad955edc-bf18-37cf-b2bd-e2114f14b4ff | -11.56822 | -63.81901 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adc17530-d85c-343c-a695-c63b6d34c71e | -11.56545 | -63.81491 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 504c7f46-b3df-344f-806b-043d84996db4 | -11.56489 | -63.81845 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a68a304-03e9-3cdd-a7cd-ed70d9d8222d | -11.56432 | -63.822 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba6755bb-3660-3dc5-8fc0-3dc19d839d79 | -11.56376 | -63.82555 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b0d51c9-e7b8-320d-b1e0-4a4148880d0c | -11.56319 | -63.82909 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 252a3c21-62b3-3897-a712-71012b05d646 | -11.56099 | -63.82145 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba623a55-de1a-3804-b65e-d48fef36a1d8 | -11.56042 | -63.825 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 78c43815-616a-3570-9076-dfdf29604e6a | -11.55986 | -63.82855 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 160d7f7e-d79e-3979-84d9-23012e4ddec3 | -11.55093 | -63.84164 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48773f84-c90b-3548-9d98-ea7605c198ac | -11.55036 | -63.84519 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 628ca270-d843-3754-adf9-7e4a3299b170 | -11.54979 | -63.84874 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb3b2438-0e03-3821-8bab-49bd34812730 | -11.53849 | -63.70516 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91c5d646-2c3d-31ad-8b8f-9403a346d568 | -11.53793 | -63.70869 | 2024-10-01 05:29:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac6a46e5-2e54-38f8-a225-ee92f8286dd1 | -11.44681 | -61.45445 | 2024-10-01 05:29:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4daff95a-2e60-325f-b7ec-285473f4ba91 | -11.44662 | -61.45381 | 2024-10-01 05:29:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4990898-a183-3b23-8178-23110b83f46c | -11.44338 | -61.45392 | 2024-10-01 05:29:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f861c2a9-c201-32fd-b323-8b5f9c411fb6 | -11.37856 | -55.11798 | 2024-10-01 05:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87cfc60d-19a7-3dbe-8b0d-674293fffc21 | -21.02572 | -57.51483 | 2024-10-01 05:31:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4d7c5837-6b56-3465-be22-6689372ad33c | -19.65263 | -56.47449 | 2024-10-01 05:31:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 4a441989-13fe-3caa-ad3f-af6bd6f0af53 | -19.16434 | -57.4775 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 9e58f3b0-48ac-3453-9835-12c183befb77 | -19.16365 | -57.47622 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 1fe9dcdb-f6e4-3964-853b-27ac8f1972ca | -19.15895 | -57.47552 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 16f05320-7244-305a-bb6e-45fb16d323de | -19.15821 | -57.48169 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| ae4ca55b-e511-32bd-be34-ca3f6a0cfa21 | -19.15424 | -57.47484 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 31f6c72d-6f04-3084-a6f0-da4a951ac2e9 | -19.14953 | -57.47414 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 97549e4f-1ecd-3ce3-a72f-328c0961a55d | -19.13132 | -57.4661 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.9 |
| a60dfee4-448c-38db-a30d-dab7c95c09b5 | -19.1307 | -57.47145 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.2 |
| 508aed0d-cd12-327a-8fa5-00fc7c5c6b7b | -19.1266 | -57.46548 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.9 |
| 47812144-8ab1-3b9f-8734-81c30f8525b7 | -19.12599 | -57.47077 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.2 |
| 04c8fb20-2211-3e2e-9fa5-224bf1d47bed | -19.12188 | -57.46486 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 38771bab-6843-32fd-b6d6-7f633e1ceb77 | -19.12128 | -57.47011 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 6465bd80-d221-3c80-9ae9-49717a158558 | -19.1206 | -57.47601 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| ff4693de-fee6-3efe-8f36-dfbb471c702b | -19.11716 | -57.46426 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 096035ea-3446-36c8-8b30-4194a80ddd3c | -19.11588 | -57.47543 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 540b1605-2952-3df0-b7b9-ac487ccd626b | -18.71348 | -57.31575 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 016361c3-48c7-388d-b857-9c80dc6ee041 | -18.71287 | -57.321 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| ec84419f-bcfa-3f44-9646-41bcf2fc19d1 | -18.70874 | -57.31513 | 2024-10-01 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |


[Clique aqui para ver as próximas entradas](README144.md)
