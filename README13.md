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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed5d6e4d-0fb3-3db1-b7d2-675dadb89573 | -4.88195 | -48.6638 | 2024-10-26 01:09:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 3ea1c67c-9cc8-3460-b314-23d8b7e94098 | -4.87681 | -48.56 | 2024-10-26 01:09:00 | TERRA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 34e0b21e-0925-33af-86f0-ed908fcb8f01 | -4.84392 | -48.61803 | 2024-10-26 01:09:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 0726ffc0-0610-3f24-bbdd-9c0239f97723 | -4.83994 | -49.88157 | 2024-10-26 01:09:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 458ded4d-b08b-3916-9dfb-0349d0299d88 | -4.75314 | -49.20209 | 2024-10-26 01:09:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| dec24e1d-340f-3bff-8c52-4a3dbe812c9d | -4.71715 | -49.08792 | 2024-10-26 01:09:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 4eb26dd6-caf9-35b4-a537-7892f67a149b | -4.62638 | -50.65181 | 2024-10-26 01:09:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 68712ae1-9711-3e48-8085-07b1176e7d98 | -4.61799 | -55.90517 | 2024-10-26 01:09:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b77e0f95-9d2d-3098-be98-aad0b8c33872 | -4.57593 | -48.03557 | 2024-10-26 01:09:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 182.2 |
| cdba3b90-53d2-38ea-b365-c38298010997 | -4.57414 | -48.02322 | 2024-10-26 01:09:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 508.1 |
| 9b41b790-189c-3e17-a53b-a2e959458a1b | -4.56369 | -48.02465 | 2024-10-26 01:09:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 61732404-f7e0-3536-bb0d-3e0c8f5dbc54 | -4.52529 | -45.80041 | 2024-10-26 01:09:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 47b0a35b-b861-310c-aa52-d25b5dd08fc0 | -4.48715 | -48.13103 | 2024-10-26 01:09:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 397f9d54-e9b3-36cf-9755-0ed53b6ffd97 | -4.48535 | -48.11863 | 2024-10-26 01:09:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 541fcda5-8b36-3258-9bb2-45d30a88c2c5 | -4.42002 | -50.56226 | 2024-10-26 01:09:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 97d35541-5ad9-3857-ab9f-d1b5e4880a8c | -4.40795 | -50.73906 | 2024-10-26 01:09:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5ce40743-0820-3aff-8848-9753b71219c3 | -4.40667 | -50.72992 | 2024-10-26 01:09:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e8a0c374-6942-384c-8d31-f48b933886cc | -4.39757 | -50.53404 | 2024-10-26 01:09:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 2f1fd9b9-1a26-3073-8c2e-e569d24d8c09 | -4.39627 | -50.52475 | 2024-10-26 01:09:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 9332571f-59c5-3ea3-9def-6c9ec2689d7b | -4.34289 | -55.36522 | 2024-10-26 01:09:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| e586a4aa-602d-38ec-9894-4f0a1841a079 | -4.34122 | -55.35324 | 2024-10-26 01:09:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 06a316eb-36b8-30ba-9ab5-a617d642583c | -4.3408 | -55.35909 | 2024-10-26 01:09:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 01f37403-0f18-3358-8ce7-77aafdc09616 | -4.3357 | -48.64094 | 2024-10-26 01:09:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c3a4b72b-94e7-392a-aaa0-54a4f305c549 | -4.30638 | -48.65136 | 2024-10-26 01:09:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 52a9885b-fa27-3b5a-8922-d1103f507318 | -4.29793 | -50.74209 | 2024-10-26 01:09:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f0437abc-2923-3a1f-820b-7d1499761fec | -4.29664 | -50.73296 | 2024-10-26 01:09:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 41397dc1-0df4-3c49-b85b-5ccc53e79acb | -4.29637 | -48.65287 | 2024-10-26 01:09:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| f68a57a7-9a99-3fb6-94b3-bf09619a119e | -4.29472 | -48.64139 | 2024-10-26 01:09:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 7a89ced8-1813-33e3-b9a8-453c51486da3 | -4.25111 | -48.55277 | 2024-10-26 01:09:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 2b20d96c-7349-3e05-81e5-a5559434e497 | -4.24942 | -48.54113 | 2024-10-26 01:09:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e5c6ee62-0996-31eb-873f-5e03a65cdb33 | -4.24102 | -48.55427 | 2024-10-26 01:09:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| fda34186-3c58-3ac4-9f0a-d5e27c090642 | -4.20602 | -44.24418 | 2024-10-26 01:09:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 6ab4ec45-f511-3115-8f96-00f704ff871d | -4.20253 | -44.25132 | 2024-10-26 01:09:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 736dd8ce-e09a-3003-b676-e6e183c6f8a6 | -4.1161 | -54.29101 | 2024-10-26 01:09:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 970c10aa-2703-37a2-a9c6-c81e2764a8ad | -4.0732 | -54.43892 | 2024-10-26 01:09:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c5a4b7a1-96bc-396d-a955-5398dcb47583 | -4.06251 | -45.68056 | 2024-10-26 01:09:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 325683af-1c35-3e24-9d4b-2c312876cc9f | -4.03498 | -54.54696 | 2024-10-26 01:09:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| eed6425d-1d62-3a62-9f1a-268e153d2a3a | -4.02447 | -54.61264 | 2024-10-26 01:09:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0c18252c-5a39-3c11-92ee-9b1a1e46afa2 | -4.01344 | -54.82149 | 2024-10-26 01:09:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7848827d-4b54-30c0-a4be-c31d6bcda620 | -3.98724 | -53.81081 | 2024-10-26 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| acb0541f-f249-36b0-9b94-820fce59e403 | -3.98591 | -53.80116 | 2024-10-26 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 697b535b-524e-3ce9-9301-bc0eb70d342d | -3.9623 | -45.80584 | 2024-10-26 01:09:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 52e537ee-1dd1-386f-b643-c17b88494c44 | -3.93638 | -48.36095 | 2024-10-26 01:09:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 63dc2eca-14d1-3bf6-85c3-fa5519d54224 | -3.93462 | -48.34894 | 2024-10-26 01:09:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 0d80e492-336e-3eb6-9d57-1bbf7a0fe5c8 | -3.93284 | -48.33676 | 2024-10-26 01:09:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| d769ea34-7a96-3bab-91d2-12fc2bd9092d | -3.92432 | -48.3504 | 2024-10-26 01:09:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 7b0e28ba-9372-3bfe-b222-a0786c593445 | -3.92253 | -48.33823 | 2024-10-26 01:09:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 9458f959-9380-3719-a383-31b8a178dd35 | -3.92213 | -50.17418 | 2024-10-26 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| fc859e09-c1b6-388a-a00c-874b6316bb02 | -3.91142 | -52.3982 | 2024-10-26 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ce1afdeb-5c72-302c-b47b-bff02f7c2d02 | -3.90875 | -48.37126 | 2024-10-26 01:09:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 845de219-94ce-3c84-9778-addfb936caa9 | -3.83837 | -52.40554 | 2024-10-26 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 36a78e96-9b84-3beb-ac6d-033554897fcc | -3.83715 | -52.39675 | 2024-10-26 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 055b81aa-ae73-3ec2-8f8a-0aa0392a104c | -3.82947 | -48.89092 | 2024-10-26 01:09:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c88c038f-c3f8-3eac-810b-48156f33dd30 | -3.81953 | -48.9613 | 2024-10-26 01:09:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| fc310847-8f68-316b-a460-f44a520559a5 | -3.81897 | -48.96784 | 2024-10-26 01:09:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 61750b01-9b70-3fb1-a384-e4fffe2e9127 | -3.78658 | -51.37288 | 2024-10-26 01:09:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c973906d-7c98-36a8-89d4-1f1b07f4ee9e | -3.76775 | -53.41998 | 2024-10-26 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| e6c128b2-507f-3cb7-a898-794559fa4c7d | -3.76648 | -53.41073 | 2024-10-26 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 97f242c7-3087-3d1e-baa1-2e8327825fb1 | -3.74837 | -53.41329 | 2024-10-26 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3d199cfe-46e8-3151-907b-6affb4561f2f | -3.74097 | -54.48862 | 2024-10-26 01:09:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ac233abf-0751-3e4a-9a28-96fc520d63ed | -3.70585 | -52.11633 | 2024-10-26 01:09:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3cea0785-ea86-389b-8f5b-5c8922d10eff | -3.70093 | -50.16504 | 2024-10-26 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 57e2eb31-7dcc-3c43-82c1-e3e54e40fbe1 | -3.68993 | -52.00204 | 2024-10-26 01:09:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 06507a88-f639-3a01-9bae-b964e6b9810a | -3.66635 | -50.12048 | 2024-10-26 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6b8413e9-2e08-3216-9dde-7e0a71af07e3 | -3.65847 | -50.13157 | 2024-10-26 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 0c73960f-43d8-388f-bca3-d9cb51b8c0db | -3.65709 | -50.12183 | 2024-10-26 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| dc6f4069-e0df-3529-b38c-8d48e56e4358 | -3.65364 | -51.93544 | 2024-10-26 01:09:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 25af1fe9-de40-3314-9d8b-d9372a8b105d | -3.63697 | -55.51637 | 2024-10-26 01:09:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 202a2dfe-30b0-3f9c-8f58-f8a6a96cc4f9 | -3.62722 | -55.51203 | 2024-10-26 01:09:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| fc195f88-6dc0-3b17-a7cf-f87315fc2585 | -3.62679 | -55.51772 | 2024-10-26 01:09:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 76c5d23c-0dd3-350f-9f20-639f69656873 | -3.62521 | -55.50585 | 2024-10-26 01:09:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 419f14ad-5d16-368a-bf5c-aea81289e035 | -3.61561 | -44.98731 | 2024-10-26 01:09:00 | TERRA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| b2138df6-c5a9-3300-b9ce-f81b004f0c65 | -3.61221 | -44.965 | 2024-10-26 01:09:00 | TERRA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 684ab078-3b82-3d0c-bd40-bee558a134b7 | -3.6119 | -54.03545 | 2024-10-26 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| dfb00ab8-0dd5-3760-8046-2a95f5f906d7 | -3.61074 | -45.82471 | 2024-10-26 01:09:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 0f43d9a9-41e6-3657-8e04-d3a3d04411aa | -3.60793 | -45.8055 | 2024-10-26 01:09:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 21.1 |
| a45129ff-62fb-3ad8-831f-a12021d8af07 | -3.60731 | -51.47398 | 2024-10-26 01:09:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7fd02195-4a39-3827-bdbf-208ff6622ffe | -3.60477 | -44.97278 | 2024-10-26 01:09:00 | TERRA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 98.0 |
| b87f0a7c-b72e-344b-baef-c17d62767887 | -3.59866 | -44.96716 | 2024-10-26 01:09:00 | TERRA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 601f4f09-d31e-3ff3-9807-fe3986b88e77 | -3.58012 | -51.21386 | 2024-10-26 01:09:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| f16d902d-db41-3c54-ab9d-ea5a91b73441 | -3.57887 | -51.20488 | 2024-10-26 01:09:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1cbb5e70-0ead-3cb5-926a-1646d597c270 | -3.57786 | -54.6404 | 2024-10-26 01:09:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2a006634-ab9b-3111-8fdd-f343ab7b9774 | -3.57641 | -54.62995 | 2024-10-26 01:09:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b96c2c8b-db41-34c9-a4c9-5fcb43938732 | -3.55675 | -51.43585 | 2024-10-26 01:09:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 85c9baac-aa2a-3168-91dc-45473589bbe8 | -3.55669 | -55.44991 | 2024-10-26 01:09:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e6c4acfb-b2c7-3544-b325-1df7e0c6970e | -3.55147 | -53.99077 | 2024-10-26 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 71ef5552-bfee-3410-93d3-e69a24491dbe | -3.54764 | -47.36609 | 2024-10-26 01:09:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 12659be3-c633-3731-954a-b21a7b674ce7 | -3.51662 | -51.02048 | 2024-10-26 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| b9f6c510-6d53-3a60-878e-6b462bc60a8a | -3.51099 | -54.02216 | 2024-10-26 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ec72b219-7f07-30da-8c0b-8c72f2d20cda | -3.50766 | -51.02176 | 2024-10-26 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2536d8e8-f1e2-3963-a595-feed883f9f96 | -3.49236 | -54.44165 | 2024-10-26 01:09:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 8823f403-2a54-3264-a7de-2c8c566f9762 | -3.47901 | -50.48839 | 2024-10-26 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4b0985b7-f247-3ed5-a7ed-927f5c6e3434 | -3.4696 | -54.52412 | 2024-10-26 01:09:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bc5dba0f-f993-3f16-bf73-b6305aae9875 | -3.46625 | -45.98857 | 2024-10-26 01:09:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 5e986f85-11b1-3604-9309-f135f67a1fd9 | -3.46304 | -49.26842 | 2024-10-26 01:09:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ff57937e-2338-3da0-a1c4-8aec7708220c | -3.46204 | -45.97557 | 2024-10-26 01:09:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 0fd26a76-b611-31af-8a56-131e8bf78211 | -3.44086 | -54.13184 | 2024-10-26 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6b110a64-c290-3cda-80db-abd88964f952 | -3.42902 | -54.58215 | 2024-10-26 01:09:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4e347347-98b2-3ca1-a153-77d2a9f5e749 | -3.41947 | -54.58339 | 2024-10-26 01:09:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 858ed639-f565-3042-acd5-310cbadbf318 | -3.41807 | -54.57306 | 2024-10-26 01:09:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README14.md)
