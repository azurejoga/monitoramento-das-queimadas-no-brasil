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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0846d483-4b54-3d64-bbbc-f08da84da4d5 | -2.9371 | -51.0465 | 2024-11-06 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| e0832a0f-50de-3bd9-aa45-f599b1791f8c | -2.937 | -51.0673 | 2024-11-06 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| e958d5d2-1545-37b0-8b47-9a88c090c036 | -6.5012 | -47.5033 | 2024-11-06 04:20:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 23dc3111-8be5-34bb-ba0a-e2b93829da09 | -3.1213 | -51.1036 | 2024-11-06 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 6086f312-31c0-37b7-a04d-fe2a875f7948 | -1.2922 | -54.5585 | 2024-11-06 04:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 61cc966b-b3b0-33d5-acd6-c5b118e9644c | -3.1616 | -50.2248 | 2024-11-06 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| b1136781-4c8c-39d0-a6db-c0cf20ee08a4 | -3.2164 | -50.3701 | 2024-11-06 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| ac92005f-0428-3f19-ab9c-dd0830424913 | -3.0207 | -53.4227 | 2024-11-06 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| e8c66b76-7fbb-301f-8a9c-ca380c79928d | -6.4827 | -47.4827 | 2024-11-06 04:20:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 5b608e53-f86b-3722-95e3-bb147fcce263 | -2.7243 | -54.1552 | 2024-11-06 04:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 0953eeb3-ea4e-3d01-b4fd-f9ab0ad22404 | -2.8423 | -51.7735 | 2024-11-06 04:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 9704f76d-0b49-31de-9c40-d0a637d26a31 | -3.526 | -47.3862 | 2024-11-06 04:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 09787eb0-dd69-310b-9e07-b30e6e7cbcdc | 3.6184 | -51.3162 | 2024-11-06 04:20:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 57.4 |
| bffccefb-0eff-3dd3-a514-cc76cc9bd01a | -3.0396 | -53.2805 | 2024-11-06 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| b957e2a7-a29d-3e78-ab5d-5598ca0c4a67 | -6.5014 | -47.4813 | 2024-11-06 04:20:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 105.2 |
| dced8900-5a9c-34c7-8a96-fe68c2795086 | -2.9185 | -51.0678 | 2024-11-06 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| c12d4494-a60a-305d-9c8c-0ee7d7bf892c | -2.6764 | -51.8189 | 2024-11-06 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 610106fd-96ab-34c5-88f4-0f8ffe1bd296 | -3.0397 | -53.2603 | 2024-11-06 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| d14457b4-b20d-3134-9ae3-1a4dca25a808 | -3.0023 | -53.4232 | 2024-11-06 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| c720847a-b401-3a27-8ead-ca6abf47643c | -4.1246 | -43.5833 | 2024-11-06 04:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| d352f841-b8c4-3171-bc70-c8a513d1d722 | -6.4906 | -44.6862 | 2024-11-06 04:20:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 78e8d683-24c3-379a-b3eb-0c5770fb2281 | -2.9187 | -51.0262 | 2024-11-06 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| d94b790f-cf22-334c-8457-76e92088d45a | -3.0207 | -53.443 | 2024-11-06 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 9233f153-efd8-3e18-b5b7-5ec3d3073851 | -3.2348 | -50.3904 | 2024-11-06 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 508cc280-a40a-3a33-bdec-8ba8025eab88 | -2.7244 | -54.1351 | 2024-11-06 04:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 681edee7-2852-32ee-b539-3f0a82d72641 | -3.1617 | -50.2038 | 2024-11-06 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 126.1 |
| 1a09fc0f-bf80-3a7d-9bdf-fc062a6f302e | -6.1226 | -43.9809 | 2024-11-06 04:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 3aeef5a1-1641-351e-aa98-90e58c3ad4ea | -3.967 | -48.15 | 2024-11-06 04:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| af6ab215-82e8-3552-ab8a-438d56afa4c9 | -4.1432 | -43.5822 | 2024-11-06 04:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 119.9 |
| c20676ff-0d17-30bf-9061-5f05fcbe7197 | -3.5446 | -47.3855 | 2024-11-06 04:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 131.0 |
| 9848ffbf-5193-3ae7-a98a-e3d437db8186 | -3.5447 | -47.3636 | 2024-11-06 04:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 615f6372-5868-395c-bd05-6412db31c8e1 | -6.1229 | -43.9578 | 2024-11-06 04:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| e58fb400-8c0c-3fd1-bae9-fdef8d0b7d44 | -3.2163 | -50.391 | 2024-11-06 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| d9a78eb3-0921-3191-893b-f48e2c2f5689 | -3.2349 | -50.3695 | 2024-11-06 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| fc63e758-7bb9-3adb-bc69-f9ac3fa326ec | -2.9186 | -51.047 | 2024-11-06 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| c1e48bf5-188f-38f0-9d0a-267c563ca3f4 | -6.5094 | -44.6847 | 2024-11-06 04:20:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| e2435b82-c08b-3eab-bfff-1fd0692c412b | -6.5096 | -44.6618 | 2024-11-06 04:20:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 291d1993-e8f6-347e-8cc8-5dc6a5052580 | -3.0213 | -53.2607 | 2024-11-06 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| f23150e7-721b-3d07-a62a-7f3aa06b02a2 | -6.1229 | -43.9578 | 2024-11-06 04:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| c64208da-dc7d-35a1-91b9-00c312bab86f | -4.5614 | -48.0141 | 2024-11-06 04:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 0f6521d0-1742-3903-b9ad-c29dc21d2464 | -4.1246 | -43.5833 | 2024-11-06 04:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 508132fd-798a-3b82-9424-33dec6f1406c | -6.5094 | -44.6847 | 2024-11-06 04:30:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| a3346228-8ed3-3409-bada-20eeb885bd11 | -2.8608 | -51.7731 | 2024-11-06 04:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 159.1 |
| 4540ca5c-4f11-38b0-aacb-bbae1e89f034 | -2.7244 | -54.1351 | 2024-11-06 04:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| ce7b6d1f-bf92-3d8e-8243-41f87269f45c | -6.4906 | -44.6862 | 2024-11-06 04:30:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| eefd2faf-a210-356c-af7a-43b15c9b6f85 | -4.1432 | -43.5822 | 2024-11-06 04:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 92c2e46f-b16b-34c8-9c74-88bea3493988 | -6.5096 | -44.6618 | 2024-11-06 04:30:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 769aa09c-5f7d-3156-b425-8f742acd2658 | -2.937 | -51.0673 | 2024-11-06 04:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 3fe205cc-dabf-30a7-9aad-1cd7058c19a1 | -2.7243 | -54.1552 | 2024-11-06 04:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 113.9 |
| b713433f-7e69-38a6-957e-de5c6315fe67 | -2.8506 | -49.4744 | 2024-11-06 04:30:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 34b377ad-b8a2-3168-9af4-5d5d1dbb4b97 | -2.8423 | -51.7735 | 2024-11-06 04:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 7e968161-79ab-30e5-a189-fd782cb54f4f | -3.5446 | -47.3855 | 2024-11-06 04:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 151.9 |
| 2d24a871-6a7a-342e-a779-abff8050132d | -3.2164 | -50.3701 | 2024-11-06 04:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 3e56f2f0-81fa-3db5-9cdc-f7db9913a886 | -2.9371 | -51.0465 | 2024-11-06 04:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| d11b1374-987a-335b-b839-f8ee6158fcf9 | -3.2163 | -50.391 | 2024-11-06 04:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 56515d21-1cce-3b3f-b71f-aae3562a7b04 | -6.1226 | -43.9809 | 2024-11-06 04:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 0985e607-7267-3a62-9ee0-540f7b1f3802 | -3.2348 | -50.3904 | 2024-11-06 04:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 1abd194f-3d9f-399b-9a8c-9ae759742f0d | 3.6 | -51.3168 | 2024-11-06 04:30:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 1765ad78-18c5-325a-b082-2cbd66ce5a3f | -3.0207 | -53.443 | 2024-11-06 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| f9daa38e-68e2-35ca-86f0-a6e140945f32 | -2.9186 | -51.047 | 2024-11-06 04:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| c69c16af-fe8f-3cf6-bcef-27acdbb47a31 | -6.5012 | -47.5033 | 2024-11-06 04:30:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 88dfcb60-9b76-3d17-b788-ccb695679076 | -3.5447 | -47.3636 | 2024-11-06 04:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| ae4fef50-1ff0-3b11-a950-40d1aca97eda | -6.5014 | -47.4813 | 2024-11-06 04:30:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 57148536-97d7-3397-bb94-409895492c12 | -3.0023 | -53.4434 | 2024-11-06 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 0c271f30-61cd-3f22-8bde-8789927e97aa | -3.967 | -48.15 | 2024-11-06 04:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 81e68190-4e0f-3314-ad4a-7cfd13f16c53 | -3.0023 | -53.4232 | 2024-11-06 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 35172246-9709-358e-a8f2-4e1660390191 | -3.0396 | -53.2805 | 2024-11-06 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| bac967cc-6408-3fe0-9f84-06d425248c8a | -3.1617 | -50.2038 | 2024-11-06 04:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| b18b9a2f-de1c-3e48-9618-b4591aa60ffe | -3.2349 | -50.3695 | 2024-11-06 04:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 00fe8d54-55a2-36c7-97db-b089abc05a4a | -3.0207 | -53.4227 | 2024-11-06 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 92c79cbe-4d78-38d1-8a0c-3f6636b46430 | -3.0397 | -53.2603 | 2024-11-06 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| ab260ede-fc26-3d1d-a9fc-9c2762e29cc8 | 3.35182 | -51.28404 | 2024-11-06 04:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bb8bfbb6-d807-372b-9b63-0dffd48d418e | 3.61541 | -51.31295 | 2024-11-06 04:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a3c28aa0-d226-3caf-bd37-160f24c7a9a9 | 3.61302 | -51.32286 | 2024-11-06 04:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 79de049c-5002-3765-b594-dbc5e5286e05 | 3.5276 | -51.24337 | 2024-11-06 04:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eec151c6-a786-3d3a-a8b3-d68c6d260fcd | 3.51934 | -51.23993 | 2024-11-06 04:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 981a8d36-ef3c-39bf-a654-b7f78b1949e2 | 1.78573 | -50.43326 | 2024-11-06 04:33:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6f1a9e6-213a-352b-b074-00683a313592 | 3.52004 | -51.24453 | 2024-11-06 04:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4c46f383-fd82-335a-9b12-2476282e7fac | 3.61471 | -51.3083 | 2024-11-06 04:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2ef5cc6f-61b6-3224-a4a6-e10452669be4 | 3.51626 | -51.2451 | 2024-11-06 04:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2218d690-2dfb-3f08-a599-a9385467e65e | 3.61372 | -51.32753 | 2024-11-06 04:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f8b0f9ef-7a90-3cc8-a1f3-955671136eb8 | 3.60851 | -51.31876 | 2024-11-06 04:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 82edd7b6-2c80-350c-8ab0-92140ae60447 | 3.51248 | -51.24568 | 2024-11-06 04:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 202e3468-847a-35dc-b1cd-d46aeaba7d17 | 3.54866 | -51.48418 | 2024-11-06 04:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d06e5f5-7110-3f62-9a42-16565bf7614a | 3.34804 | -51.28461 | 2024-11-06 04:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fcf15ade-d101-3099-a670-e651ca3d0387 | 3.55322 | -51.48833 | 2024-11-06 04:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88b8d94b-22d6-3977-afb9-34057e365445 | 1.7899 | -50.43671 | 2024-11-06 04:33:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89c09459-dcba-33c1-973f-a58f615abecc | 3.49427 | -51.25317 | 2024-11-06 04:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2ed26fb3-01df-3386-b7b7-623eee7aa1c9 | 3.49049 | -51.25375 | 2024-11-06 04:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5f409bc-b805-36db-91de-e6c0bdff92d8 | 3.54411 | -51.48002 | 2024-11-06 04:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bc777ef-90dc-3c61-9122-c0a5578d7dda | 3.60781 | -51.31409 | 2024-11-06 04:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 0b314b30-9227-3b48-b45b-6a14ee56b38f | 3.52382 | -51.24395 | 2024-11-06 04:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 886fd4e2-a550-3e50-9684-93b6782e117a | 3.49357 | -51.24857 | 2024-11-06 04:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8fc2dfd5-9b5f-3ed3-84ff-44969b19baab | 1.78218 | -50.43381 | 2024-11-06 04:33:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 643e251b-ea9a-30a4-93e5-7e1723d7a973 | 3.60921 | -51.32343 | 2024-11-06 04:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 0b6324cf-fdf5-3292-b792-768cad312acb | 3.61161 | -51.31353 | 2024-11-06 04:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ad1ad8ff-8fff-3f8b-93be-019eac7859d1 | 3.49735 | -51.24799 | 2024-11-06 04:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 57a3dcb8-e235-3b3b-803d-b9e0f104a6f7 | 3.50114 | -51.24741 | 2024-11-06 04:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 719c1b4c-e38b-3a72-bb15-c64897b30589 | 3.53209 | -51.24739 | 2024-11-06 04:33:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a313461e-4825-36bc-9f19-9c0ec84ba7b8 | 1.77864 | -50.43436 | 2024-11-06 04:33:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README30.md)
