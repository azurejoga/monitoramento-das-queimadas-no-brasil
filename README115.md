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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20205a0e-1352-3738-af8d-20bf124e4c5a | -12.88093 | -53.53157 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d491009-3c1f-3a06-8892-15ce28a2568d | -12.88042 | -53.53525 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b81bbf76-1f4a-3f37-af63-3e82ced460d3 | -12.87991 | -53.53892 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a9cfd41-2c5b-3aa9-b012-bd62b1d7acc5 | -12.87941 | -53.54258 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b51dc501-d8e4-3720-85d3-5767c113dfb1 | -12.8789 | -53.54625 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 185f9b55-e662-3f3e-a707-565c5a159ba6 | -12.87736 | -53.52727 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c49829f5-c792-30e9-8630-0ec5cbd2a413 | -12.87685 | -53.53096 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54b19f97-d856-3f7f-ab75-dd266f097fc6 | -12.87533 | -53.54197 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e09a6f1d-06c0-3781-a9c6-79a21a52fa62 | -12.8743 | -53.51925 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87914ee2-adc3-3ceb-b69d-60f6069b2d30 | -12.87379 | -53.52295 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb2270b0-d71a-3f66-ae8b-91e4b46bf839 | -12.87227 | -53.53401 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 309eb1b6-3cec-3a6c-8882-1ebe935b8289 | -12.87177 | -53.53769 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c32a008-e883-38b8-b1e5-e22395a93b10 | -12.6707 | -53.1843 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2fb492c-f5e3-3d55-ae32-715b67a00cb7 | -12.57839 | -53.06881 | 2024-10-14 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 243086be-1126-3ddf-a10a-1d03ae59b9a4 | -9.27476 | -54.58364 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c5d6e3c-8e4b-3084-be05-f021baeb22b5 | -9.009 | -54.5118 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45552901-b8a1-30a2-8475-633ac1827bb6 | -9.00837 | -54.51612 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 262ceef2-1f17-38bf-9590-f3bf26581f0e | -9.00774 | -54.52045 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e83fa6b-68a5-3fbe-92be-91cad7b708f6 | -9.00535 | -54.51122 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8787df8b-02ec-3ceb-9a7a-8f3ab2299908 | -8.98742 | -54.58331 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9242d381-398b-3396-9a83-8963c9dd3c9c | -8.63932 | -53.65051 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a1b913d-87a0-33a2-b4e2-a581068a6bf7 | -8.63863 | -53.65527 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7d4cf1a-0049-33a2-9dd9-fe834691ec4d | -8.6355 | -53.64999 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a465a547-7c7d-3631-99b0-89b31fa507fc | -8.38029 | -53.28531 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c95d588-aa48-370c-b571-4bded7231dce | -10.62521 | -54.61149 | 2024-10-14 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c6fb911-f5ba-3d64-85d6-fe197e4eb361 | -10.62151 | -54.61086 | 2024-10-14 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e19c4d1-85bf-3be4-bed9-cfd80bcd9d3e | -10.03811 | -54.33989 | 2024-10-14 05:10:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0175ece1-d0aa-33a8-a0c5-9c563a460447 | -10.03744 | -54.34449 | 2024-10-14 05:10:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e700e37a-03fe-3bf2-a26f-6c3b52b042ec | -10.03437 | -54.33936 | 2024-10-14 05:10:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7b8838a-d38e-344c-a1cd-7d08c469a9ae | -10.0337 | -54.34395 | 2024-10-14 05:10:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09381ea9-d59d-36f3-bc4e-4886a494633a | -11.40045 | -55.0582 | 2024-10-14 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a20fe9c5-b4c3-330e-89bd-3efae31a49e8 | -11.4003 | -55.05994 | 2024-10-14 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 134f6ec3-b34b-3817-9bff-ad8d607268f7 | -11.3968 | -55.05762 | 2024-10-14 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6fe9b95-6038-3626-93bb-79f76f086d2d | -11.39665 | -55.05938 | 2024-10-14 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68ddfe4b-1a8a-397b-9cd4-ce3d4ca4e63e | -11.39299 | -55.05884 | 2024-10-14 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07e98321-55bb-3372-851c-5daaaa3c3b80 | -11.35625 | -55.20698 | 2024-10-14 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a37d0e3-7da9-32c1-91dd-3894956b79fd | -11.34537 | -55.07843 | 2024-10-14 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 132224bc-4be0-356f-adbd-b06f48b03763 | -11.27719 | -54.58957 | 2024-10-14 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c78d1fa-ba39-352e-95d6-57cf21cccf22 | -11.19481 | -54.75463 | 2024-10-14 05:10:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00d79684-0d94-39aa-ba62-7ec2d87ae291 | -11.1787 | -54.76137 | 2024-10-14 05:10:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2141d115-d99e-3ca1-ba74-aeeeb2f10972 | -11.17805 | -54.76586 | 2024-10-14 05:10:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57dfc6c6-2acf-325a-8c92-b044cc9eabfd | -11.07768 | -54.78904 | 2024-10-14 05:10:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6c765a0-7cdd-3b3e-8d0d-270e9a3e8bbc | -11.07702 | -54.79354 | 2024-10-14 05:10:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72cf035c-1131-38b0-b6fc-a102cb068080 | -11.07638 | -54.79799 | 2024-10-14 05:10:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6af97697-18e3-3d4a-bdeb-5a3c99dabdc8 | -12.61978 | -55.21951 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00a55710-c60b-331a-8adb-637c22ce5759 | -12.61054 | -55.23159 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7282d07-9daf-3257-9adf-23090640a1f8 | -12.60687 | -55.23105 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97c8332a-f486-31d9-a157-a8119b0eb01b | -12.60149 | -55.18974 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5aef7d9-2415-33a5-afb8-f585ad212a59 | -12.59782 | -55.18916 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2dd0fd16-114d-3142-a588-34c773ecd258 | -12.4564 | -54.57524 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b22e3fa-9b84-3bd6-8dfa-33e36936dec1 | -12.61673 | -55.21458 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e4c9bcf-47fc-3f6f-8c01-895a061fac79 | -12.6161 | -55.21898 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1bd5213-a21a-3c10-8973-219a96306d4f | -12.61547 | -55.22337 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36eb229b-218d-30c5-84d0-a2f74f2b1703 | -12.61484 | -55.22775 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ada7566d-861a-3a76-9a4c-7eac06b3a58a | -12.61421 | -55.23214 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7882a2b4-b0ba-33dd-ba01-2ecefea37eaf | -12.60257 | -55.23488 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3089d4b8-d43a-3762-ae71-1dffdd372ab7 | -12.59719 | -55.19356 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e7aaed57-060e-3e34-93bc-6e266067ecb0 | -12.59414 | -55.1886 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46d5db4c-e008-30aa-bbcd-9d3a860e4f3c | -12.59352 | -55.193 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 470cd88d-d8a0-3d4a-8550-b0387c2ad982 | -12.46087 | -54.571 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7b3c00e-fdd7-34ba-9068-fa3dc8434882 | -12.46021 | -54.57574 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec1308c2-6404-3060-ba89-abc7de79334a | -12.45706 | -54.57049 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9652a700-39de-3090-9dae-bad74daab7f6 | -12.45325 | -54.56998 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84a1fdfd-3d25-35b5-90ff-6aa6beacf24f | -12.45259 | -54.57473 | 2024-10-14 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a239ac0d-1497-3a95-8dc6-327e330c034c | -7.97519 | -54.86269 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ba94041-668c-310e-bb6c-ee794fcceed4 | -7.91163 | -54.87889 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d78124f9-f6ac-3486-a26e-e53b7a283089 | -7.90809 | -54.87833 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 549ef6b6-f854-3ff4-9415-f476151e0992 | -7.87934 | -54.72945 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08affb76-fc6f-33db-8c27-a1dc2c60bd9f | -7.87671 | -54.70521 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1116f15a-3c24-3d48-b280-242c7053f924 | -7.87483 | -54.71751 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16c1a485-65af-34f9-ac98-bca661c23e78 | -7.87344 | -54.71991 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9977224-9289-3b9c-ace2-f672af82c615 | -7.87315 | -54.70463 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c4bdde6-cf9b-353a-aa88-21448e5b89e4 | -7.87126 | -54.71696 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| abdcf5c3-3be2-34b1-8ea8-042d3de4d81d | -7.8702 | -54.69997 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c075e37e-b85a-3759-a5e0-e4e7f3ccb849 | -7.86957 | -54.70411 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6650e1b3-6e51-332c-bdb2-f014ed4d8d51 | -7.86894 | -54.70824 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11986b4e-ec27-3da6-83aa-4a85126500b8 | -7.86831 | -54.71236 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43608993-449d-3207-a153-9cc670e35512 | -7.86788 | -54.69121 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa970d1f-957a-3dfc-b98e-f830654ec444 | -7.86725 | -54.69532 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73d451cc-8f76-3dff-8110-7788d4457a4a | -7.86536 | -54.70776 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc1c32ee-90e1-327c-bcc5-74caf371fd73 | -7.8643 | -54.69067 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45103129-7518-3db0-abfa-92d16b05a4ab | -7.86368 | -54.69477 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7212c63-43b4-3066-b233-a5a4d71910f5 | -7.86011 | -54.69423 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 879301dd-9b8b-3a79-81c9-ae32193ff982 | -7.85947 | -54.69839 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2aea8ef8-c5b7-347b-8a9f-c8a53bb1e8e2 | -7.85884 | -54.70258 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00a8e862-6185-3618-9c30-027cf01f728f | -7.85591 | -54.6978 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53c2023d-e168-329d-9620-c91ac34a0b33 | -8.36652 | -54.95544 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11a58bf4-a740-3afc-a0cd-7b39e080dafc | -8.16888 | -55.18747 | 2024-10-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 381ec0f9-3ccf-3aa4-b5d2-a954fefb87cb | -9.98342 | -55.17999 | 2024-10-14 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a707e05-50b2-3035-898a-aad77bf00495 | -9.76018 | -55.34871 | 2024-10-14 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4992fbbb-371d-3ac4-8f3f-949be2fe8a58 | -9.75664 | -55.3482 | 2024-10-14 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 131eee5d-8efb-30b0-910f-78e11492773a | -10.65283 | -56.05096 | 2024-10-14 05:10:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e932f54-d200-344c-a5e5-50d2b21884a4 | -10.11269 | -55.21074 | 2024-10-14 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c32075e3-0f7f-317b-85e3-5c723c954269 | -10.11093 | -55.1978 | 2024-10-14 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c033e506-3ff2-3aaf-aa03-2219c4be6e39 | -10.11033 | -55.20193 | 2024-10-14 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73513be8-f4af-3ed5-9a62-eea245428d1d | -10.10675 | -55.20141 | 2024-10-14 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43488700-c870-3b07-8d79-2a380270e64e | -10.10615 | -55.20554 | 2024-10-14 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bff4a779-c892-3627-8043-feedc6eee0b2 | -10.10378 | -55.19674 | 2024-10-14 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eef89fed-2523-3718-9287-5c7d11cbdca6 | -10.10318 | -55.20087 | 2024-10-14 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b823a5f1-f894-328d-9e74-9e9877dd909e | -14.45659 | -56.83598 | 2024-10-14 05:10:00 | NOAA-20 | ARENÁPOLIS | MATO GROSSO | Brasil | 5101308 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README116.md)
