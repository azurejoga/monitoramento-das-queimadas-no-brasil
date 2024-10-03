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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20bcdbef-4694-360b-b5e9-5557ff85aff9 | -20.86621 | -47.07909 | 2024-10-03 04:29:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7098a2bb-491d-3eaa-aa97-27bf2bed972f | -20.86502 | -47.03661 | 2024-10-03 04:29:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e4470d4-6b2f-3fe5-841b-1d49529d024a | -20.86443 | -47.04084 | 2024-10-03 04:29:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fc204a3-b5ea-35f6-9085-0093cb3f902d | -20.2806 | -46.89951 | 2024-10-03 04:29:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| eac4b960-e256-327a-bb7b-f770227d1237 | -20.27767 | -46.89496 | 2024-10-03 04:29:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2abb762d-b55a-39fe-8ac2-2c42eab823aa | -20.27709 | -46.89904 | 2024-10-03 04:29:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 324b9876-de78-3adc-80f3-217c765871af | -21.3015 | -47.61278 | 2024-10-03 04:29:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26a51c69-00a7-3020-8d19-7c4752465e38 | -21.29919 | -47.60448 | 2024-10-03 04:29:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 920c71a9-6b0e-3946-a3e5-51d1870cc8ea | -21.07512 | -47.31076 | 2024-10-03 04:29:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c38befc5-963d-31f0-98fe-4885235c9841 | -15.19955 | -47.52202 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 190b5896-dc63-3cfc-a621-049a1141e82d | -15.10215 | -48.23653 | 2024-10-03 04:29:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd1f1d83-6768-398e-95c3-7d36213a8ab2 | -15.20397 | -47.51538 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d90289d-083d-36dc-90b8-c66b56153ae3 | -15.20011 | -47.51841 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5a6928b6-d5e2-3376-a11a-ac7f1be9f956 | -15.21538 | -47.14973 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aec57229-f8a1-3cf0-94c3-362d6dfdd813 | -15.28628 | -47.5323 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4e17eba-7e6a-3ffb-9537-f81f8a7879cc | -15.27634 | -47.50829 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7f3f4173-ec31-385b-b3a6-e39f201679d8 | -15.26637 | -47.50683 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 203d1928-af91-3ea4-a2d1-6ba31a523e19 | -15.24646 | -47.50369 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 850e8450-d089-3953-b202-7c7a9f94775b | -15.23824 | -47.5136 | 2024-10-03 04:29:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab4d42d8-c378-382a-929e-32e251d44834 | -15.23272 | -47.50531 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af683468-79cf-3b5f-b365-f46702acdef5 | -15.6633 | -47.1989 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 882b5830-8da7-3759-add2-fa54699b91dd | -15.66275 | -47.20257 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f733f03d-6c5f-3e4f-a39e-8b1c24e204c4 | -15.41842 | -47.64598 | 2024-10-03 04:29:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed51bc99-7ef3-393d-9ca7-e7f2604cd72b | -15.4151 | -47.64544 | 2024-10-03 04:29:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07572a7c-ed35-37c4-bf92-f498ac93de34 | -15.41399 | -47.65263 | 2024-10-03 04:29:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6e54788-20bc-3a4d-ad51-359bec7d6952 | -15.41344 | -47.65622 | 2024-10-03 04:29:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dfd581ec-2178-372e-9cf4-ccee5b6c37e1 | -15.41227 | -47.42002 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d3c20e7-9a0f-3751-81e5-74385d2840a2 | -15.40894 | -47.41948 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b3ffc85-3575-3bcc-b1dc-41ba155530fa | -15.40506 | -47.42262 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c960cd2-8da9-3bcb-acf5-288408742cec | -15.40174 | -47.42201 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59a8034d-53a7-3834-bb24-9013586a4d15 | -15.40119 | -47.42567 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3fb5cafe-468f-3e47-ab83-3d34e379cdac | -15.39124 | -47.42382 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6fafb19c-2e6b-3718-ad70-0cbd1cef4609 | -15.38736 | -47.42688 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1bd72969-2976-3e9c-a672-dcf8ddb2a382 | -15.38404 | -47.4263 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e4b035e-c5fc-33de-82f1-258c66453946 | -15.38072 | -47.42571 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c9dbdb48-593e-3c11-b9b1-fbf4c2111e7d | -15.28739 | -47.52504 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 010255ab-07d4-3607-98f2-a00a0798fa96 | -15.2697 | -47.50733 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 959b9b8a-46b9-38e4-bb42-217792e3b0aa | -15.25309 | -47.50475 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 20c5eb29-0c20-31e1-9f35-fffa45f7cae7 | -15.2366 | -47.50222 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5854e2bc-d674-377e-ab88-b4fc806b9ceb | -15.23603 | -47.50588 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4dd2f725-52b1-3c7c-9118-aff7f39898d5 | -15.27967 | -47.50879 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 96cef1f7-9fbb-3cef-8d6d-9a1a0ac69e25 | -15.27911 | -47.51246 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29fb8ace-dcf8-3f13-bef8-b7f71e4804a3 | -15.27578 | -47.51199 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b4009eba-3740-3906-b092-9f8e9ef33b72 | -15.24978 | -47.50423 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 743af31b-fd68-3407-a8f5-85bee1988152 | -15.24701 | -47.49997 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8ef5c930-cff5-3b3f-ad23-e3293144fc9d | -15.23991 | -47.50279 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1e3bb95f-4938-373b-b0a0-ef459657cd54 | -15.22498 | -47.51142 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f09e934-9685-3ca0-b72c-6322073c31cd | -15.1523 | -48.0918 | 2024-10-03 04:29:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6f152c6-00ef-3760-9ab2-6c25e098edec | -15.1497 | -48.08413 | 2024-10-03 04:29:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 93344929-ba3b-301f-b3e6-b5a61086ae9f | -15.14915 | -48.08768 | 2024-10-03 04:29:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 518fbd11-cedb-3860-8094-93f2021c6c12 | -15.14859 | -48.09123 | 2024-10-03 04:29:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c084c0c4-f087-30fd-a8ab-454ab238e94f | -15.14804 | -48.09478 | 2024-10-03 04:29:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1640dda1-cd02-3443-ba96-455effa4ce27 | -15.14585 | -48.08714 | 2024-10-03 04:29:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 031e2d6f-e0c8-3612-be57-9db68da99847 | -15.14529 | -48.09068 | 2024-10-03 04:29:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7748da00-7b9a-3686-8180-4b177fafd286 | -15.14474 | -48.09423 | 2024-10-03 04:29:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dfd770d7-02c6-3092-865d-a065acdf861e | -15.27966 | -47.48651 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2fcae50a-ce28-3d5b-a501-5985797ef0e2 | -15.25641 | -47.50527 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 964895b0-8aed-3e78-b05b-4c91d67e6ecc | -15.24314 | -47.50315 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bc05e18a-edaf-3779-9c2f-ff929144533d | -15.22941 | -47.50472 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5351b1a1-a6c6-3279-9947-1504e3a82dd0 | -15.22885 | -47.50836 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 73771c3b-7dc6-38d2-a387-5be9d7ce2c1d | -15.22554 | -47.50778 | 2024-10-03 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6cb67df6-9690-31c6-a6da-45ce569325ea | -16.23368 | -48.025 | 2024-10-03 04:29:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cea12b5b-625f-3d5a-ac63-1cb0148910c6 | -15.99056 | -47.81631 | 2024-10-03 04:29:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39efa8a5-1bca-3731-b573-a170510668be | -15.86236 | -48.55343 | 2024-10-03 04:29:00 | NOAA-21 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54c5fb3b-61b4-3c51-9711-260db07ee940 | -15.85963 | -48.54932 | 2024-10-03 04:29:00 | NOAA-21 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9e1981d-a0e0-37d8-b95f-6f0e022a5693 | -15.85688 | -48.5452 | 2024-10-03 04:29:00 | NOAA-21 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff5ef0db-b05e-34a0-acc4-3f955730317b | -15.85633 | -48.54876 | 2024-10-03 04:29:00 | NOAA-21 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c2831b3d-8ea4-32a8-83ee-40084ac8a37f | -15.73859 | -48.38636 | 2024-10-03 04:29:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 49edeba1-edf7-3c96-ada0-5deff7867cd5 | -15.73529 | -48.38581 | 2024-10-03 04:29:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8f434e2-41a9-30a0-9537-499ce1b05384 | -15.73198 | -48.38526 | 2024-10-03 04:29:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c7088495-8b62-3396-8eef-826bc86e6b9f | -15.73143 | -48.38882 | 2024-10-03 04:29:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 016ebe65-1871-30c6-ba7e-3c90478acac0 | -15.72594 | -48.3806 | 2024-10-03 04:29:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92981321-0b95-3aa2-aacc-0d8b95144057 | -15.72538 | -48.38416 | 2024-10-03 04:29:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1b038ab-77aa-39ce-b00d-46ee431fa40a | -15.72207 | -48.38361 | 2024-10-03 04:29:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a808ce62-2c62-34c8-b4f8-ddb5051777cf | -15.72096 | -48.39074 | 2024-10-03 04:29:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 023ad3d6-8074-3de7-a7a6-45d81e23ea30 | -15.71821 | -48.38662 | 2024-10-03 04:29:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c029610-94d4-3704-b67c-d49d93b1ae15 | -15.71765 | -48.39018 | 2024-10-03 04:29:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c3eaded2-f448-372f-bd5e-a036e0ed47d8 | -15.60054 | -48.54983 | 2024-10-03 04:29:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 210af7dd-f618-315e-817b-49ee3685600f | -15.56945 | -47.8572 | 2024-10-03 04:29:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53939740-0a03-3bc6-a6cc-097aafcc6abf | -17.74571 | -48.44928 | 2024-10-03 04:29:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 224f0542-a941-37b1-9cce-2cd8464a795c | -17.74297 | -48.4451 | 2024-10-03 04:29:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 697ed0b1-2b8d-3efb-953d-c94186862240 | -17.73966 | -48.44454 | 2024-10-03 04:29:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ac1937f-bc92-30a9-8457-55a5bdb6b1e0 | -17.73635 | -48.44397 | 2024-10-03 04:29:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf507ab1-cab8-302f-8895-ed80a2283383 | -17.18442 | -48.69081 | 2024-10-03 04:29:00 | NOAA-21 | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc220391-7269-3939-9446-ef5d707534c3 | -18.7935 | -47.99612 | 2024-10-03 04:29:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b13f79b0-1bfb-3169-a013-48623e55f526 | -18.7896 | -47.99926 | 2024-10-03 04:29:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 04dfab43-24a0-3463-817d-471d8998d54f | -19.09716 | -48.05306 | 2024-10-03 04:29:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4115cf57-0e01-3360-9746-327749204b27 | -19.09438 | -48.04876 | 2024-10-03 04:29:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5172525-ab4c-3c30-8da8-1dc189896915 | -19.09104 | -48.0482 | 2024-10-03 04:29:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7b8b1eb4-6dfd-3978-9466-0313b2da5fde | -19.09089 | -48.27609 | 2024-10-03 04:29:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a9d14fe-b9d3-3180-a404-d4cd71630779 | -19.09048 | -48.05193 | 2024-10-03 04:29:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6951fcd8-b535-3908-a9ed-ab3ee08e5b84 | -19.0877 | -48.04764 | 2024-10-03 04:29:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6c6e95f9-02fa-3216-992c-863c441c8b3a | -19.08714 | -48.05136 | 2024-10-03 04:29:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| dc69afad-7682-351e-bccf-fd9bfd0436d5 | -19.08658 | -48.0551 | 2024-10-03 04:29:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b3722208-5089-3627-b2b0-a4ed78f11445 | -19.05198 | -48.35266 | 2024-10-03 04:29:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eeb13643-98b7-3ac6-a5f9-298b8f58db88 | -18.89064 | -48.00391 | 2024-10-03 04:29:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bcf99c5e-378b-3e50-b52a-6bc1d93a68c3 | -18.79016 | -47.99555 | 2024-10-03 04:29:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d12831e9-5cf2-3950-8b32-24c20af40f7d | -18.61983 | -49.19068 | 2024-10-03 04:29:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 15142454-f01c-3f38-9f31-75bfdcc30213 | -20.57331 | -49.61871 | 2024-10-03 04:29:00 | NOAA-21 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99c1a8e0-5127-3087-94b8-01fa7d0462a1 | -20.57274 | -49.62238 | 2024-10-03 04:29:00 | NOAA-21 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README105.md)
