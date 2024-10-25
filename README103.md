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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e8cca1f-01d4-36fb-8906-84c80fb0cb88 | -17.05317 | -57.47373 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 89e36e2c-2b54-358c-8809-a8df13ff4bd1 | -17.05261 | -57.45499 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 65189e02-0d84-3c0d-8e0a-d12a3bbb3ccf | -17.0515 | -57.43988 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.9 |
| 94bd54e2-bda4-3842-b94b-8a896b73db32 | -17.04928 | -57.47681 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 6a2f2990-65b8-3574-a73d-26de9939bec4 | -17.04928 | -57.45444 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d3177c1c-ba2f-3020-ae69-5f42ee68a513 | -17.04762 | -57.44296 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 3b42179f-7bb0-3b20-81de-66b74c496e7a | -17.04651 | -57.47263 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 236a76b3-bbf0-3a81-b606-837da4422871 | -17.04651 | -57.45024 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 2bf3e48f-55a4-3568-a701-5d417a4189ed | -17.04651 | -57.42785 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 5ef18da9-cfb5-3e98-842a-a63aaa1bd65e | -17.04595 | -57.43149 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 92eab4a5-6c78-3911-99ea-b7f03b9e6c14 | -17.04429 | -57.44242 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 5f49c97c-be64-333e-98f1-3b5b0ed9b86c | -17.04318 | -57.4497 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 9ecd8028-9088-3a56-aa3a-7d43af6af26a | -17.04263 | -57.45334 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c2e2971a-5c17-38b3-a594-6633a157148d | -17.04262 | -57.52043 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| cea962b6-61b3-342d-974a-a0e1a23022a0 | -17.04207 | -57.45698 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 35e2ce45-416a-36bb-85c6-42213572b496 | -17.04152 | -57.46062 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b856d276-aa66-3f8e-836b-1322c99b7626 | -17.04096 | -57.46425 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e7a18a44-5f7a-3905-8caf-706e91a28e40 | -17.04095 | -57.4456 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 38bdf236-3739-3391-ab00-f43b19f088d6 | -17.0393 | -57.51988 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 7599c013-e53e-3831-8e09-67abddfd87bc | -17.03927 | -57.45652 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 485d1005-b496-3b22-a866-d70c3489c29f | -17.03871 | -57.46016 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 8c3dbcd3-466e-30a7-bd4b-f2bbcebe234b | -17.03819 | -57.5048 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| f4b820bf-aefb-300e-b7e6-a05fc674d63a | -17.03815 | -57.46379 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 96e341e1-9b5b-32c3-97b4-66bbf74f215b | -17.03764 | -57.50844 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 31028a45-aa21-36e8-b0f4-18f23e8b5feb | -17.03762 | -57.44505 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e1ec2fbe-36e1-369a-9767-c84a23c1eee0 | -17.03706 | -57.44869 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 47fcd9a4-1d25-3442-886d-701e2cca68ee | -17.03594 | -57.45597 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e92ad41c-d8fc-35fc-afdf-c0f32d6a5581 | -17.03486 | -57.52659 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.5 |
| e9673b8c-c568-3393-aad3-6eace2ede154 | -17.03431 | -57.50788 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 7368ad53-4b87-3244-91da-2f606f826159 | -17.03314 | -57.47416 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 60d44136-1b81-3be9-b1df-7ef744053e77 | -17.03262 | -57.45542 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c4f6d9a7-5ff5-3c32-9fb1-7fe8309cfdef | -17.03259 | -57.47779 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9a75bfaa-3b52-3cf7-8df2-4696f00cc0d5 | -17.03209 | -57.5224 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| e0fc4a5d-9005-38b8-8adb-7daa8b6923df | -17.03205 | -57.45906 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| dd2eb73d-af60-357e-84bd-18e22fdaff7b | -17.03199 | -57.50377 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 945b2e92-a445-3b13-bda4-b2a55b65a2d7 | -17.03094 | -57.46633 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| c80782bc-5eac-368b-bc87-3582f22878cc | -17.02982 | -57.4736 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| daf94721-2674-3f12-9044-d464da40288b | -17.02976 | -57.5183 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 84a2377b-f125-335f-b7ae-4560e18c7713 | -17.02873 | -57.45851 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 300aba3c-7e82-3d4c-a34b-d4ccf2c8902c | -17.02867 | -57.50323 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| e3bb0e6d-8199-38fb-bfeb-5187a70ecaf7 | -17.02864 | -57.52556 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| ba435ee9-d2cc-3c78-a407-659ae69306eb | -17.02811 | -57.50686 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 1bb8b1ab-0fc8-3ba5-bbc7-0e14b2661828 | -17.0259 | -57.49904 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 838b0647-df73-3554-b14e-46d3990b8bd9 | -17.02587 | -57.52138 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| e95842f8-e8c3-3cf1-b6d4-5a52bcebef94 | -17.02534 | -57.50267 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d0eabb52-34e3-3331-900c-c39994159362 | -17.02531 | -57.52501 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 9c6d99e3-77f3-3ece-b4b0-190e59d8b925 | -17.02478 | -57.50631 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a1ed27eb-a420-3552-87ee-beda84b3a34b | -17.02475 | -57.52864 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 1413ab41-a804-3939-b6a8-0d7a01b53998 | -17.02369 | -57.49123 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b595634d-2057-359a-8159-5b9caef25580 | -17.02199 | -57.52446 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 76323d3e-14b4-3199-b2f1-0ad19f4b6717 | -17.02146 | -57.50575 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 24138693-e733-3f94-86dd-ff63730e6c37 | -17.01981 | -57.4943 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9cbbf31f-68e8-3692-ab12-14d4523b2df1 | -17.01922 | -57.52028 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 80ccfb13-0919-3ec1-bafc-31003b3388d4 | -17.01866 | -57.52391 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| ade28c79-dee3-3874-aa53-9bc85bb5e00f | -17.01704 | -57.49013 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| f0039343-a134-37e1-8ac0-1b850a6b376d | -17.01648 | -57.49376 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c5b1a75e-ac14-3694-ba16-5cbbe10562fb | -17.01537 | -57.50102 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bdf2b725-1c6f-3a53-8ca5-301f34e67519 | -17.01372 | -57.48958 | 2024-10-25 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 33f2faa2-a63a-38c1-ad55-3e2886b51e15 | -17.28197 | -57.2675 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| dd8e8146-698b-36c3-aa05-f76f5b29266c | -17.27529 | -57.2664 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| fef74fc8-5ee9-3d68-85db-16e561949804 | -17.27251 | -57.26218 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| bd1fb831-6071-3026-8a58-80a751da1033 | -17.27195 | -57.26585 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 2b355184-1019-38cb-b7b9-c78fbe94a4cb | -17.26917 | -57.26163 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 831dd245-8c59-302a-9eaf-4c7c256bb0d5 | -17.26749 | -57.27265 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2916e9f6-e6d3-3a0a-9f84-f349c31b286e | -17.25638 | -57.21054 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 705f9959-53d6-369f-8a8c-d7f52b2342da | -17.24243 | -57.25725 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2b890b97-6d36-30c2-a768-040945429219 | -17.23964 | -57.27561 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| f65e4943-3439-326a-aaae-e48b7c3a5dde | -17.23743 | -57.22251 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 40401813-d0d6-32d9-b63a-edd96481e74b | -17.23687 | -57.22619 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 09fc6a85-f14a-3db6-834f-27fac57ee53b | -17.2363 | -57.27505 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| a696224f-8ab1-39df-83c3-b2fe7cae2261 | -17.23352 | -57.24826 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 66701cd2-42e2-3905-8793-661139bd02d0 | -17.23352 | -57.22564 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 0c46bbc2-19ce-3d3f-9446-3036e8ee649c | -17.23297 | -57.22932 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 8769482e-3510-38d7-8322-6938d6dad9a8 | -17.23241 | -57.233 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| a0db7ea3-ab6d-3525-a270-2b3be47de8ef | -17.23018 | -57.2477 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| eca7e8c5-25c9-3575-8319-3ce9d822f74d | -17.22963 | -57.22877 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 0236b718-736c-35bb-9ab6-11dc80e293cd | -17.22962 | -57.25138 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 2a714d01-cb2d-350c-9df5-36ea80b0c088 | -17.22907 | -57.23245 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| b9315541-9680-3779-97a7-3528b1dd44da | -17.22684 | -57.24715 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4dfe1451-5848-32ea-9348-2c4aaba3f98a | -17.22573 | -57.2319 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| d648e553-6366-36b2-b636-bb308c308d5f | -17.22517 | -57.23558 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.1 |
| d914d19f-d71a-318a-a99f-cc4a6ca6c931 | -17.22461 | -57.23926 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.1 |
| 13ba05a8-f905-360a-aa94-e33598c9bd32 | -17.22405 | -57.24293 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| bec4239b-0799-3b86-a7f8-dc526569f6f3 | -17.2235 | -57.24661 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b8c9088a-1a18-3204-b545-d5f9225a2cf4 | -17.22127 | -57.2387 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| efa59677-4583-3256-b7e9-28b58bed64d3 | -17.22071 | -57.24239 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| cd088811-2182-327e-8a5e-8701af3ddeb8 | -17.22016 | -57.24606 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 6bd08615-796a-3bdc-85ed-c42f6cceea76 | -17.2196 | -57.24973 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c8bf7ac9-d765-3a7c-97f9-c4871d59c2af | -17.21626 | -57.24918 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| cbfaad19-efc3-34bc-aa35-a07a14d95b98 | -17.2157 | -57.25285 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ca20418d-71cf-3716-b8c1-bb5303111040 | -17.2118 | -57.25598 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 546100c8-e3b2-30fb-8dce-6da8b8eaef72 | -17.21124 | -57.25965 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 403bd0b0-f45f-3dbc-9b12-14b503b4ae8c | -17.18342 | -56.74593 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 50b757d3-e8aa-37a6-9a7d-256a61ef3622 | -17.17666 | -56.74484 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2d61f9be-7099-396f-97b5-66ef01c0f8fc | -17.17445 | -56.78295 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 69eccd32-450e-396f-95cc-ac012f0825df | -17.17334 | -56.79045 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1ecdf6a8-1563-3b1f-96cc-4bbb79a710ec | -17.17052 | -56.78616 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a18d7bc7-cb7b-3a36-b47c-5d3186efc85c | -17.16996 | -56.78991 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0c9f1e37-9365-3467-ab78-068c81c512f7 | -17.1637 | -56.7389 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 8713754e-5c8d-3faf-8790-b0e384e11e87 | -17.15479 | -56.79898 | 2024-10-25 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |


[Clique aqui para ver as próximas entradas](README104.md)
